# SNMP MIB module (JUNIPER-JS-FLOW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\junos\JUNIPER-JS-FLOW-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:03:26 2025
# On host DESKTOP-ORUUBP9 platform Windows version 11 by user speterman
# Using Python version 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(jnxJsFlow,) = mibBuilder.importSymbols(
    "JUNIPER-JS-SMI",
    "jnxJsFlow")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

jnxJsFlowMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 18, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxJsFlowGenPostFrags_ObjectIdentity = ObjectIdentity
jnxJsFlowGenPostFrags = _JnxJsFlowGenPostFrags_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 18, 1, 0)
)
_JnxJsFlowGenPostFragsCounter_Type = Counter64
_JnxJsFlowGenPostFragsCounter_Object = MibScalar
jnxJsFlowGenPostFragsCounter = _JnxJsFlowGenPostFragsCounter_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 18, 1, 0, 1),
    _JnxJsFlowGenPostFragsCounter_Type()
)
jnxJsFlowGenPostFragsCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsFlowGenPostFragsCounter.setStatus("current")
_JnxJsFlowGenPreFrags_ObjectIdentity = ObjectIdentity
jnxJsFlowGenPreFrags = _JnxJsFlowGenPreFrags_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 18, 1, 1)
)
_JnxJsFlowGenPreFragsCounter_Type = Counter64
_JnxJsFlowGenPreFragsCounter_Object = MibScalar
jnxJsFlowGenPreFragsCounter = _JnxJsFlowGenPreFragsCounter_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 18, 1, 1, 1),
    _JnxJsFlowGenPreFragsCounter_Type()
)
jnxJsFlowGenPreFragsCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsFlowGenPreFragsCounter.setStatus("current")
_JnxJsFlowSofSummary_ObjectIdentity = ObjectIdentity
jnxJsFlowSofSummary = _JnxJsFlowSofSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 18, 1, 2)
)
_JnxJsFlowSofPktProcessedNum_Type = Counter64
_JnxJsFlowSofPktProcessedNum_Object = MibScalar
jnxJsFlowSofPktProcessedNum = _JnxJsFlowSofPktProcessedNum_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 18, 1, 2, 1),
    _JnxJsFlowSofPktProcessedNum_Type()
)
jnxJsFlowSofPktProcessedNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsFlowSofPktProcessedNum.setStatus("current")
_JnxJsFlowSofSessNum_Type = Unsigned32
_JnxJsFlowSofSessNum_Object = MibScalar
jnxJsFlowSofSessNum = _JnxJsFlowSofSessNum_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 18, 1, 2, 2),
    _JnxJsFlowSofSessNum_Type()
)
jnxJsFlowSofSessNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsFlowSofSessNum.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-JS-FLOW-MIB",
    **{"jnxJsFlowMIB": jnxJsFlowMIB,
       "jnxJsFlowGenPostFrags": jnxJsFlowGenPostFrags,
       "jnxJsFlowGenPostFragsCounter": jnxJsFlowGenPostFragsCounter,
       "jnxJsFlowGenPreFrags": jnxJsFlowGenPreFrags,
       "jnxJsFlowGenPreFragsCounter": jnxJsFlowGenPreFragsCounter,
       "jnxJsFlowSofSummary": jnxJsFlowSofSummary,
       "jnxJsFlowSofPktProcessedNum": jnxJsFlowSofPktProcessedNum,
       "jnxJsFlowSofSessNum": jnxJsFlowSofSessNum}
)
