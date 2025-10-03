# SNMP MIB module (TN-ARP-INSPECTION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\transition\TN-ARP-INSPECTION-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:30:46 2025
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(tnDevMgmt,) = mibBuilder.importSymbols(
    "TN-MGMT-MIB",
    "tnDevMgmt")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnARPInspectionMIB_ObjectIdentity = ObjectIdentity
tnARPInspectionMIB = _TnARPInspectionMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 22)
)
_TnARPInspectionConfigTable_Object = MibTable
tnARPInspectionConfigTable = _TnARPInspectionConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 22, 1)
)
if mibBuilder.loadTexts:
    tnARPInspectionConfigTable.setStatus("current")
_TnARPInspectionConfigEntry_Object = MibTableRow
tnARPInspectionConfigEntry = _TnARPInspectionConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 22, 1, 1)
)
tnARPInspectionConfigEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    tnARPInspectionConfigEntry.setStatus("current")


class _TnARPInspectionMode_Type(Integer32):
    """Custom type tnARPInspectionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TnARPInspectionMode_Type.__name__ = "Integer32"
_TnARPInspectionMode_Object = MibTableColumn
tnARPInspectionMode = _TnARPInspectionMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 22, 1, 1, 1),
    _TnARPInspectionMode_Type()
)
tnARPInspectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnARPInspectionMode.setStatus("current")
_TnARPInspectionTranslation_Type = TruthValue
_TnARPInspectionTranslation_Object = MibTableColumn
tnARPInspectionTranslation = _TnARPInspectionTranslation_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 22, 1, 1, 2),
    _TnARPInspectionTranslation_Type()
)
tnARPInspectionTranslation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnARPInspectionTranslation.setStatus("current")
_TnARPInspectionPortModeTable_Object = MibTable
tnARPInspectionPortModeTable = _TnARPInspectionPortModeTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 22, 2)
)
if mibBuilder.loadTexts:
    tnARPInspectionPortModeTable.setStatus("current")
_TnARPInspectionPortModeEntry_Object = MibTableRow
tnARPInspectionPortModeEntry = _TnARPInspectionPortModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 22, 2, 1)
)
tnARPInspectionPortModeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnARPInspectionPortModeEntry.setStatus("current")


class _TnARPInspectionPortMode_Type(Integer32):
    """Custom type tnARPInspectionPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TnARPInspectionPortMode_Type.__name__ = "Integer32"
_TnARPInspectionPortMode_Object = MibTableColumn
tnARPInspectionPortMode = _TnARPInspectionPortMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 22, 2, 1, 1),
    _TnARPInspectionPortMode_Type()
)
tnARPInspectionPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnARPInspectionPortMode.setStatus("current")
_TnStaticARPInspectionTable_Object = MibTable
tnStaticARPInspectionTable = _TnStaticARPInspectionTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 22, 3)
)
if mibBuilder.loadTexts:
    tnStaticARPInspectionTable.setStatus("current")
_TnStaticARPInspectionEntry_Object = MibTableRow
tnStaticARPInspectionEntry = _TnStaticARPInspectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 22, 3, 1)
)
tnStaticARPInspectionEntry.setIndexNames(
    (0, "TN-ARP-INSPECTION-MIB", "tnStaticARPInspectionPort"),
    (0, "TN-ARP-INSPECTION-MIB", "tnStaticARPInspectionVLAN"),
    (0, "TN-ARP-INSPECTION-MIB", "tnStaticARPInspectionMAC"),
    (0, "TN-ARP-INSPECTION-MIB", "tnStaticARPInspectionAddrType"),
    (0, "TN-ARP-INSPECTION-MIB", "tnStaticARPInspectionAddr"),
)
if mibBuilder.loadTexts:
    tnStaticARPInspectionEntry.setStatus("current")


class _TnStaticARPInspectionPort_Type(Integer32):
    """Custom type tnStaticARPInspectionPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TnStaticARPInspectionPort_Type.__name__ = "Integer32"
_TnStaticARPInspectionPort_Object = MibTableColumn
tnStaticARPInspectionPort = _TnStaticARPInspectionPort_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 22, 3, 1, 1),
    _TnStaticARPInspectionPort_Type()
)
tnStaticARPInspectionPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnStaticARPInspectionPort.setStatus("current")


class _TnStaticARPInspectionVLAN_Type(Integer32):
    """Custom type tnStaticARPInspectionVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_TnStaticARPInspectionVLAN_Type.__name__ = "Integer32"
_TnStaticARPInspectionVLAN_Object = MibTableColumn
tnStaticARPInspectionVLAN = _TnStaticARPInspectionVLAN_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 22, 3, 1, 2),
    _TnStaticARPInspectionVLAN_Type()
)
tnStaticARPInspectionVLAN.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnStaticARPInspectionVLAN.setStatus("current")
_TnStaticARPInspectionMAC_Type = MacAddress
_TnStaticARPInspectionMAC_Object = MibTableColumn
tnStaticARPInspectionMAC = _TnStaticARPInspectionMAC_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 22, 3, 1, 3),
    _TnStaticARPInspectionMAC_Type()
)
tnStaticARPInspectionMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnStaticARPInspectionMAC.setStatus("current")
_TnStaticARPInspectionAddrType_Type = InetAddressType
_TnStaticARPInspectionAddrType_Object = MibTableColumn
tnStaticARPInspectionAddrType = _TnStaticARPInspectionAddrType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 22, 3, 1, 4),
    _TnStaticARPInspectionAddrType_Type()
)
tnStaticARPInspectionAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnStaticARPInspectionAddrType.setStatus("current")
_TnStaticARPInspectionAddr_Type = InetAddress
_TnStaticARPInspectionAddr_Object = MibTableColumn
tnStaticARPInspectionAddr = _TnStaticARPInspectionAddr_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 22, 3, 1, 5),
    _TnStaticARPInspectionAddr_Type()
)
tnStaticARPInspectionAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnStaticARPInspectionAddr.setStatus("current")
_TnStaticARPInspectionRowStatus_Type = RowStatus
_TnStaticARPInspectionRowStatus_Object = MibTableColumn
tnStaticARPInspectionRowStatus = _TnStaticARPInspectionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 22, 3, 1, 6),
    _TnStaticARPInspectionRowStatus_Type()
)
tnStaticARPInspectionRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnStaticARPInspectionRowStatus.setStatus("current")
_TnDynamicARPInspectionTable_Object = MibTable
tnDynamicARPInspectionTable = _TnDynamicARPInspectionTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 22, 4)
)
if mibBuilder.loadTexts:
    tnDynamicARPInspectionTable.setStatus("current")
_TnDynamicARPInspectionEntry_Object = MibTableRow
tnDynamicARPInspectionEntry = _TnDynamicARPInspectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 22, 4, 1)
)
tnDynamicARPInspectionEntry.setIndexNames(
    (0, "TN-ARP-INSPECTION-MIB", "tnDynamicARPInspectionPort"),
    (0, "TN-ARP-INSPECTION-MIB", "tnDynamicARPInspectionVLAN"),
    (0, "TN-ARP-INSPECTION-MIB", "tnDynamicARPInspectionMAC"),
)
if mibBuilder.loadTexts:
    tnDynamicARPInspectionEntry.setStatus("current")


class _TnDynamicARPInspectionPort_Type(Integer32):
    """Custom type tnDynamicARPInspectionPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TnDynamicARPInspectionPort_Type.__name__ = "Integer32"
_TnDynamicARPInspectionPort_Object = MibTableColumn
tnDynamicARPInspectionPort = _TnDynamicARPInspectionPort_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 22, 4, 1, 1),
    _TnDynamicARPInspectionPort_Type()
)
tnDynamicARPInspectionPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnDynamicARPInspectionPort.setStatus("current")


class _TnDynamicARPInspectionVLAN_Type(Integer32):
    """Custom type tnDynamicARPInspectionVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_TnDynamicARPInspectionVLAN_Type.__name__ = "Integer32"
_TnDynamicARPInspectionVLAN_Object = MibTableColumn
tnDynamicARPInspectionVLAN = _TnDynamicARPInspectionVLAN_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 22, 4, 1, 2),
    _TnDynamicARPInspectionVLAN_Type()
)
tnDynamicARPInspectionVLAN.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnDynamicARPInspectionVLAN.setStatus("current")
_TnDynamicARPInspectionMAC_Type = MacAddress
_TnDynamicARPInspectionMAC_Object = MibTableColumn
tnDynamicARPInspectionMAC = _TnDynamicARPInspectionMAC_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 22, 4, 1, 3),
    _TnDynamicARPInspectionMAC_Type()
)
tnDynamicARPInspectionMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnDynamicARPInspectionMAC.setStatus("current")
_TnDynamicARPInspectionAddrType_Type = InetAddressType
_TnDynamicARPInspectionAddrType_Object = MibTableColumn
tnDynamicARPInspectionAddrType = _TnDynamicARPInspectionAddrType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 22, 4, 1, 4),
    _TnDynamicARPInspectionAddrType_Type()
)
tnDynamicARPInspectionAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDynamicARPInspectionAddrType.setStatus("current")
_TnDynamicARPInspectionAddr_Type = InetAddress
_TnDynamicARPInspectionAddr_Object = MibTableColumn
tnDynamicARPInspectionAddr = _TnDynamicARPInspectionAddr_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 22, 4, 1, 5),
    _TnDynamicARPInspectionAddr_Type()
)
tnDynamicARPInspectionAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDynamicARPInspectionAddr.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-ARP-INSPECTION-MIB",
    **{"tnARPInspectionMIB": tnARPInspectionMIB,
       "tnARPInspectionConfigTable": tnARPInspectionConfigTable,
       "tnARPInspectionConfigEntry": tnARPInspectionConfigEntry,
       "tnARPInspectionMode": tnARPInspectionMode,
       "tnARPInspectionTranslation": tnARPInspectionTranslation,
       "tnARPInspectionPortModeTable": tnARPInspectionPortModeTable,
       "tnARPInspectionPortModeEntry": tnARPInspectionPortModeEntry,
       "tnARPInspectionPortMode": tnARPInspectionPortMode,
       "tnStaticARPInspectionTable": tnStaticARPInspectionTable,
       "tnStaticARPInspectionEntry": tnStaticARPInspectionEntry,
       "tnStaticARPInspectionPort": tnStaticARPInspectionPort,
       "tnStaticARPInspectionVLAN": tnStaticARPInspectionVLAN,
       "tnStaticARPInspectionMAC": tnStaticARPInspectionMAC,
       "tnStaticARPInspectionAddrType": tnStaticARPInspectionAddrType,
       "tnStaticARPInspectionAddr": tnStaticARPInspectionAddr,
       "tnStaticARPInspectionRowStatus": tnStaticARPInspectionRowStatus,
       "tnDynamicARPInspectionTable": tnDynamicARPInspectionTable,
       "tnDynamicARPInspectionEntry": tnDynamicARPInspectionEntry,
       "tnDynamicARPInspectionPort": tnDynamicARPInspectionPort,
       "tnDynamicARPInspectionVLAN": tnDynamicARPInspectionVLAN,
       "tnDynamicARPInspectionMAC": tnDynamicARPInspectionMAC,
       "tnDynamicARPInspectionAddrType": tnDynamicARPInspectionAddrType,
       "tnDynamicARPInspectionAddr": tnDynamicARPInspectionAddr}
)
