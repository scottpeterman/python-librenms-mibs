# SNMP MIB module (UBIQUOSS-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ubiquoss\UBIQUOSS-SMI
# Produced by pysmi-1.6.2 at Thu Oct  2 12:33:02 2025
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ubiquoss = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7800)
)
if mibBuilder.loadTexts:
    ubiquoss.setRevisions(
        ("1906-07-13 00:00",
         "1904-04-22 00:00",
         "1901-10-09 00:00",
         "2008-06-22 13:08")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LnsProducts_ObjectIdentity = ObjectIdentity
lnsProducts = _LnsProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 1)
)
if mibBuilder.loadTexts:
    lnsProducts.setStatus("current")
_UbiMgmt_ObjectIdentity = ObjectIdentity
ubiMgmt = _UbiMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 2)
)
if mibBuilder.loadTexts:
    ubiMgmt.setStatus("current")
_LnsKtEmsAgnt_ObjectIdentity = ObjectIdentity
lnsKtEmsAgnt = _LnsKtEmsAgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 2, 1)
)
if mibBuilder.loadTexts:
    lnsKtEmsAgnt.setStatus("current")
_SwitchAgent_ObjectIdentity = ObjectIdentity
switchAgent = _SwitchAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 2, 2)
)
if mibBuilder.loadTexts:
    switchAgent.setStatus("current")
_UbiEponGroupMIB_ObjectIdentity = ObjectIdentity
ubiEponGroupMIB = _UbiEponGroupMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 2, 500)
)
if mibBuilder.loadTexts:
    ubiEponGroupMIB.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "UBIQUOSS-SMI",
    **{"ubiquoss": ubiquoss,
       "lnsProducts": lnsProducts,
       "ubiMgmt": ubiMgmt,
       "lnsKtEmsAgnt": lnsKtEmsAgnt,
       "switchAgent": switchAgent,
       "ubiEponGroupMIB": ubiEponGroupMIB}
)
