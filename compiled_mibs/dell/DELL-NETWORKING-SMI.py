# SNMP MIB module (DELL-NETWORKING-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dell\DELL-NETWORKING-SMI
# Produced by pysmi-1.6.2 at Thu Oct  2 11:35:33 2025
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

dellNet = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6027)
)
if mibBuilder.loadTexts:
    dellNet.setRevisions(
        ("2007-06-15 12:00",
         "1900-10-10 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DellNetProducts_ObjectIdentity = ObjectIdentity
dellNetProducts = _DellNetProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1)
)
if mibBuilder.loadTexts:
    dellNetProducts.setStatus("current")
_DellNetCommon_ObjectIdentity = ObjectIdentity
dellNetCommon = _DellNetCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 2)
)
if mibBuilder.loadTexts:
    dellNetCommon.setStatus("current")
_DellNetMgmt_ObjectIdentity = ObjectIdentity
dellNetMgmt = _DellNetMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3)
)
if mibBuilder.loadTexts:
    dellNetMgmt.setStatus("current")
_DellNetModules_ObjectIdentity = ObjectIdentity
dellNetModules = _DellNetModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 4)
)
if mibBuilder.loadTexts:
    dellNetModules.setStatus("current")
_DellNetExperiment_ObjectIdentity = ObjectIdentity
dellNetExperiment = _DellNetExperiment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20)
)
if mibBuilder.loadTexts:
    dellNetExperiment.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DELL-NETWORKING-SMI",
    **{"dellNet": dellNet,
       "dellNetProducts": dellNetProducts,
       "dellNetCommon": dellNetCommon,
       "dellNetMgmt": dellNetMgmt,
       "dellNetModules": dellNetModules,
       "dellNetExperiment": dellNetExperiment}
)
