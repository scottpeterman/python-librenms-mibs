# SNMP MIB module (PACKETLOGIC-OVERVIEW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\procera\PACKETLOGIC-OVERVIEW-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:21:20 2025
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

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(packetlogic2,) = mibBuilder.importSymbols(
    "PACKETLOGIC-MIB",
    "packetlogic2")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

systemOverview = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 40)
)
if mibBuilder.loadTexts:
    systemOverview.setRevisions(
        ("2019-09-12 15:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Overview_Object = MibTable
overview = _Overview_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 40, 1)
)
if mibBuilder.loadTexts:
    overview.setStatus("current")
_OverviewEntry_Object = MibTableRow
overviewEntry = _OverviewEntry_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 40, 1, 1)
)
overviewEntry.setIndexNames(
    (0, "PACKETLOGIC-OVERVIEW-MIB", "overviewEntryIndex"),
)
if mibBuilder.loadTexts:
    overviewEntry.setStatus("current")
_Model_Type = DisplayString
_Model_Object = MibTableColumn
model = _Model_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 40, 1, 1, 1),
    _Model_Type()
)
model.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    model.setStatus("current")
_ConfigMd5Sum_Type = DisplayString
_ConfigMd5Sum_Object = MibTableColumn
configMd5Sum = _ConfigMd5Sum_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 40, 1, 1, 2),
    _ConfigMd5Sum_Type()
)
configMd5Sum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configMd5Sum.setStatus("current")
_MachineId_Type = DisplayString
_MachineId_Object = MibTableColumn
machineId = _MachineId_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 40, 1, 1, 3),
    _MachineId_Type()
)
machineId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    machineId.setStatus("current")
_FirmwareVersion_Type = DisplayString
_FirmwareVersion_Object = MibTableColumn
firmwareVersion = _FirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 40, 1, 1, 4),
    _FirmwareVersion_Type()
)
firmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareVersion.setStatus("current")


class _OverviewEntryIndex_Type(Integer32):
    """Custom type overviewEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OverviewEntryIndex_Type.__name__ = "Integer32"
_OverviewEntryIndex_Object = MibTableColumn
overviewEntryIndex = _OverviewEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 40, 1, 1, 999),
    _OverviewEntryIndex_Type()
)
overviewEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    overviewEntryIndex.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PACKETLOGIC-OVERVIEW-MIB",
    **{"systemOverview": systemOverview,
       "overview": overview,
       "overviewEntry": overviewEntry,
       "model": model,
       "configMd5Sum": configMd5Sum,
       "machineId": machineId,
       "firmwareVersion": firmwareVersion,
       "overviewEntryIndex": overviewEntryIndex}
)
