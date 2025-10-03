# SNMP MIB module (PACKETLOGIC-HW-SFP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\procera\PACKETLOGIC-HW-SFP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:21:12 2025
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

(hw,) = mibBuilder.importSymbols(
    "PACKETLOGIC-HW-MIB",
    "hw")

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

sfp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 30, 4)
)
if mibBuilder.loadTexts:
    sfp.setRevisions(
        ("2019-09-12 15:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ports_Object = MibTable
ports = _Ports_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 30, 4, 1)
)
if mibBuilder.loadTexts:
    ports.setStatus("current")
_PortEntry_Object = MibTableRow
portEntry = _PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 30, 4, 1, 1)
)
portEntry.setIndexNames(
    (0, "PACKETLOGIC-HW-SFP-MIB", "portEntryIndex"),
)
if mibBuilder.loadTexts:
    portEntry.setStatus("current")
_PortName_Type = DisplayString
_PortName_Object = MibTableColumn
portName = _PortName_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 30, 4, 1, 1, 1),
    _PortName_Type()
)
portName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portName.setStatus("current")
_PortCompatibility_Type = DisplayString
_PortCompatibility_Object = MibTableColumn
portCompatibility = _PortCompatibility_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 30, 4, 1, 1, 2),
    _PortCompatibility_Type()
)
portCompatibility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCompatibility.setStatus("current")
_PortVendorName_Type = DisplayString
_PortVendorName_Object = MibTableColumn
portVendorName = _PortVendorName_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 30, 4, 1, 1, 3),
    _PortVendorName_Type()
)
portVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portVendorName.setStatus("current")
_PortVendorOUI_Type = DisplayString
_PortVendorOUI_Object = MibTableColumn
portVendorOUI = _PortVendorOUI_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 30, 4, 1, 1, 4),
    _PortVendorOUI_Type()
)
portVendorOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portVendorOUI.setStatus("current")
_PortVendorPN_Type = DisplayString
_PortVendorPN_Object = MibTableColumn
portVendorPN = _PortVendorPN_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 30, 4, 1, 1, 5),
    _PortVendorPN_Type()
)
portVendorPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portVendorPN.setStatus("current")
_PortVendorRevisionLevel_Type = DisplayString
_PortVendorRevisionLevel_Object = MibTableColumn
portVendorRevisionLevel = _PortVendorRevisionLevel_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 30, 4, 1, 1, 6),
    _PortVendorRevisionLevel_Type()
)
portVendorRevisionLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portVendorRevisionLevel.setStatus("current")
_ChecksumBaseFields_Type = DisplayString
_ChecksumBaseFields_Object = MibTableColumn
checksumBaseFields = _ChecksumBaseFields_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 30, 4, 1, 1, 7),
    _ChecksumBaseFields_Type()
)
checksumBaseFields.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    checksumBaseFields.setStatus("current")
_PortVendorSN_Type = DisplayString
_PortVendorSN_Object = MibTableColumn
portVendorSN = _PortVendorSN_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 30, 4, 1, 1, 8),
    _PortVendorSN_Type()
)
portVendorSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portVendorSN.setStatus("current")
_PortVendorDateCode_Type = DisplayString
_PortVendorDateCode_Object = MibTableColumn
portVendorDateCode = _PortVendorDateCode_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 30, 4, 1, 1, 9),
    _PortVendorDateCode_Type()
)
portVendorDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portVendorDateCode.setStatus("current")
_ChecksumExtendedFields_Type = DisplayString
_ChecksumExtendedFields_Object = MibTableColumn
checksumExtendedFields = _ChecksumExtendedFields_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 30, 4, 1, 1, 10),
    _ChecksumExtendedFields_Type()
)
checksumExtendedFields.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    checksumExtendedFields.setStatus("current")


class _PortEntryIndex_Type(Integer32):
    """Custom type portEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PortEntryIndex_Type.__name__ = "Integer32"
_PortEntryIndex_Object = MibTableColumn
portEntryIndex = _PortEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 30, 4, 1, 1, 999),
    _PortEntryIndex_Type()
)
portEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portEntryIndex.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PACKETLOGIC-HW-SFP-MIB",
    **{"sfp": sfp,
       "ports": ports,
       "portEntry": portEntry,
       "portName": portName,
       "portCompatibility": portCompatibility,
       "portVendorName": portVendorName,
       "portVendorOUI": portVendorOUI,
       "portVendorPN": portVendorPN,
       "portVendorRevisionLevel": portVendorRevisionLevel,
       "checksumBaseFields": checksumBaseFields,
       "portVendorSN": portVendorSN,
       "portVendorDateCode": portVendorDateCode,
       "checksumExtendedFields": checksumExtendedFields,
       "portEntryIndex": portEntryIndex}
)
