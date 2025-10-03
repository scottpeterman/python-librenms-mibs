# SNMP MIB module (TRIPPLITE-PRODUCTS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\poweralert\TRIPPLITE-PRODUCTS
# Produced by pysmi-1.6.2 at Thu Oct  2 12:20:55 2025
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
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysUpTime,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysUpTime")

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
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(tripplite,) = mibBuilder.importSymbols(
    "TRIPPLITE",
    "tripplite")


# MODULE-IDENTITY

tlpProducts = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1)
)
if mibBuilder.loadTexts:
    tlpProducts.setRevisions(
        ("2021-05-12 00:00",
         "2021-02-02 00:00",
         "2019-11-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TlpHardware_ObjectIdentity = ObjectIdentity
tlpHardware = _TlpHardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1)
)
_TlpDevice_ObjectIdentity = ObjectIdentity
tlpDevice = _TlpDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 1)
)
_TlpDeviceNumDevices_Type = Unsigned32
_TlpDeviceNumDevices_Object = MibScalar
tlpDeviceNumDevices = _TlpDeviceNumDevices_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 1, 1),
    _TlpDeviceNumDevices_Type()
)
tlpDeviceNumDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpDeviceNumDevices.setStatus("current")
_TlpDeviceTable_Object = MibTable
tlpDeviceTable = _TlpDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    tlpDeviceTable.setStatus("current")
_TlpDeviceEntry_Object = MibTableRow
tlpDeviceEntry = _TlpDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 1, 2, 1)
)
tlpDeviceEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpDeviceEntry.setStatus("current")
_TlpDeviceIndex_Type = Unsigned32
_TlpDeviceIndex_Object = MibTableColumn
tlpDeviceIndex = _TlpDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 1, 2, 1, 1),
    _TlpDeviceIndex_Type()
)
tlpDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpDeviceIndex.setStatus("current")
_TlpDeviceRowStatus_Type = RowStatus
_TlpDeviceRowStatus_Object = MibTableColumn
tlpDeviceRowStatus = _TlpDeviceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 1, 2, 1, 2),
    _TlpDeviceRowStatus_Type()
)
tlpDeviceRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpDeviceRowStatus.setStatus("current")
_TlpDeviceType_Type = ObjectIdentifier
_TlpDeviceType_Object = MibTableColumn
tlpDeviceType = _TlpDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 1, 2, 1, 3),
    _TlpDeviceType_Type()
)
tlpDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpDeviceType.setStatus("current")
_TlpDeviceManufacturer_Type = DisplayString
_TlpDeviceManufacturer_Object = MibTableColumn
tlpDeviceManufacturer = _TlpDeviceManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 1, 2, 1, 4),
    _TlpDeviceManufacturer_Type()
)
tlpDeviceManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpDeviceManufacturer.setStatus("current")
_TlpDeviceModel_Type = DisplayString
_TlpDeviceModel_Object = MibTableColumn
tlpDeviceModel = _TlpDeviceModel_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 1, 2, 1, 5),
    _TlpDeviceModel_Type()
)
tlpDeviceModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpDeviceModel.setStatus("current")
_TlpDeviceName_Type = DisplayString
_TlpDeviceName_Object = MibTableColumn
tlpDeviceName = _TlpDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 1, 2, 1, 6),
    _TlpDeviceName_Type()
)
tlpDeviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpDeviceName.setStatus("current")


class _TlpDeviceID_Type(Integer32):
    """Custom type tlpDeviceID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TlpDeviceID_Type.__name__ = "Integer32"
_TlpDeviceID_Object = MibTableColumn
tlpDeviceID = _TlpDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 1, 2, 1, 7),
    _TlpDeviceID_Type()
)
tlpDeviceID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpDeviceID.setStatus("current")
_TlpDeviceLocation_Type = DisplayString
_TlpDeviceLocation_Object = MibTableColumn
tlpDeviceLocation = _TlpDeviceLocation_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 1, 2, 1, 8),
    _TlpDeviceLocation_Type()
)
tlpDeviceLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpDeviceLocation.setStatus("current")
_TlpDeviceRegion_Type = DisplayString
_TlpDeviceRegion_Object = MibTableColumn
tlpDeviceRegion = _TlpDeviceRegion_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 1, 2, 1, 9),
    _TlpDeviceRegion_Type()
)
tlpDeviceRegion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpDeviceRegion.setStatus("current")


class _TlpDeviceStatus_Type(Integer32):
    """Custom type tlpDeviceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("critical", 1),
          ("warning", 2),
          ("info", 3),
          ("status", 4),
          ("offline", 5),
          ("custom", 6),
          ("configuration", 7))
    )


_TlpDeviceStatus_Type.__name__ = "Integer32"
_TlpDeviceStatus_Object = MibTableColumn
tlpDeviceStatus = _TlpDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 1, 2, 1, 10),
    _TlpDeviceStatus_Type()
)
tlpDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpDeviceStatus.setStatus("current")
_TlpDeviceAssetTag_Type = DisplayString
_TlpDeviceAssetTag_Object = MibTableColumn
tlpDeviceAssetTag = _TlpDeviceAssetTag_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 1, 2, 1, 11),
    _TlpDeviceAssetTag_Type()
)
tlpDeviceAssetTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpDeviceAssetTag.setStatus("current")
_TlpDeviceDetail_ObjectIdentity = ObjectIdentity
tlpDeviceDetail = _TlpDeviceDetail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 2)
)
_TlpDeviceIdentTable_Object = MibTable
tlpDeviceIdentTable = _TlpDeviceIdentTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tlpDeviceIdentTable.setStatus("current")
_TlpDeviceIdentEntry_Object = MibTableRow
tlpDeviceIdentEntry = _TlpDeviceIdentEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 2, 1, 1)
)
tlpDeviceIdentEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpDeviceIdentEntry.setStatus("current")
_TlpDeviceIdentProtocol_Type = DisplayString
_TlpDeviceIdentProtocol_Object = MibTableColumn
tlpDeviceIdentProtocol = _TlpDeviceIdentProtocol_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 2, 1, 1, 1),
    _TlpDeviceIdentProtocol_Type()
)
tlpDeviceIdentProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpDeviceIdentProtocol.setStatus("current")


class _TlpDeviceIdentCommPortType_Type(Integer32):
    """Custom type tlpDeviceIdentCommPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("serial", 1),
          ("usb", 2),
          ("hid", 3),
          ("simulated", 4),
          ("unittest", 5))
    )


_TlpDeviceIdentCommPortType_Type.__name__ = "Integer32"
_TlpDeviceIdentCommPortType_Object = MibTableColumn
tlpDeviceIdentCommPortType = _TlpDeviceIdentCommPortType_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 2, 1, 1, 2),
    _TlpDeviceIdentCommPortType_Type()
)
tlpDeviceIdentCommPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpDeviceIdentCommPortType.setStatus("current")
_TlpDeviceIdentCommPortName_Type = DisplayString
_TlpDeviceIdentCommPortName_Object = MibTableColumn
tlpDeviceIdentCommPortName = _TlpDeviceIdentCommPortName_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 2, 1, 1, 3),
    _TlpDeviceIdentCommPortName_Type()
)
tlpDeviceIdentCommPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpDeviceIdentCommPortName.setStatus("current")
_TlpDeviceIdentFirmwareVersion_Type = DisplayString
_TlpDeviceIdentFirmwareVersion_Object = MibTableColumn
tlpDeviceIdentFirmwareVersion = _TlpDeviceIdentFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 2, 1, 1, 4),
    _TlpDeviceIdentFirmwareVersion_Type()
)
tlpDeviceIdentFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpDeviceIdentFirmwareVersion.setStatus("current")
_TlpDeviceIdentSerialNum_Type = DisplayString
_TlpDeviceIdentSerialNum_Object = MibTableColumn
tlpDeviceIdentSerialNum = _TlpDeviceIdentSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 2, 1, 1, 5),
    _TlpDeviceIdentSerialNum_Type()
)
tlpDeviceIdentSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpDeviceIdentSerialNum.setStatus("current")
_TlpDeviceIdentDateInstalled_Type = DisplayString
_TlpDeviceIdentDateInstalled_Object = MibTableColumn
tlpDeviceIdentDateInstalled = _TlpDeviceIdentDateInstalled_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 2, 1, 1, 6),
    _TlpDeviceIdentDateInstalled_Type()
)
tlpDeviceIdentDateInstalled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpDeviceIdentDateInstalled.setStatus("current")
_TlpDeviceIdentHardwareVersion_Type = DisplayString
_TlpDeviceIdentHardwareVersion_Object = MibTableColumn
tlpDeviceIdentHardwareVersion = _TlpDeviceIdentHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 2, 1, 1, 7),
    _TlpDeviceIdentHardwareVersion_Type()
)
tlpDeviceIdentHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpDeviceIdentHardwareVersion.setStatus("current")
_TlpDeviceIdentCurrentUptime_Type = DisplayString
_TlpDeviceIdentCurrentUptime_Object = MibTableColumn
tlpDeviceIdentCurrentUptime = _TlpDeviceIdentCurrentUptime_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 2, 1, 1, 8),
    _TlpDeviceIdentCurrentUptime_Type()
)
tlpDeviceIdentCurrentUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpDeviceIdentCurrentUptime.setStatus("current")
if mibBuilder.loadTexts:
    tlpDeviceIdentCurrentUptime.setUnits("hours")
_TlpDeviceIdentTotalUptime_Type = DisplayString
_TlpDeviceIdentTotalUptime_Object = MibTableColumn
tlpDeviceIdentTotalUptime = _TlpDeviceIdentTotalUptime_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 2, 1, 1, 9),
    _TlpDeviceIdentTotalUptime_Type()
)
tlpDeviceIdentTotalUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpDeviceIdentTotalUptime.setStatus("current")
if mibBuilder.loadTexts:
    tlpDeviceIdentTotalUptime.setUnits("days")
_TlpDeviceIdentFirmwareVersion2_Type = DisplayString
_TlpDeviceIdentFirmwareVersion2_Object = MibTableColumn
tlpDeviceIdentFirmwareVersion2 = _TlpDeviceIdentFirmwareVersion2_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 2, 1, 1, 10),
    _TlpDeviceIdentFirmwareVersion2_Type()
)
tlpDeviceIdentFirmwareVersion2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpDeviceIdentFirmwareVersion2.setStatus("current")
_TlpDeviceIdentFirmwareVersion3_Type = DisplayString
_TlpDeviceIdentFirmwareVersion3_Object = MibTableColumn
tlpDeviceIdentFirmwareVersion3 = _TlpDeviceIdentFirmwareVersion3_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 2, 1, 1, 11),
    _TlpDeviceIdentFirmwareVersion3_Type()
)
tlpDeviceIdentFirmwareVersion3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpDeviceIdentFirmwareVersion3.setStatus("current")
_TlpDeviceIdentNvrID_Type = DisplayString
_TlpDeviceIdentNvrID_Object = MibTableColumn
tlpDeviceIdentNvrID = _TlpDeviceIdentNvrID_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 2, 1, 1, 12),
    _TlpDeviceIdentNvrID_Type()
)
tlpDeviceIdentNvrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpDeviceIdentNvrID.setStatus("current")
_TlpDeviceTypes_ObjectIdentity = ObjectIdentity
tlpDeviceTypes = _TlpDeviceTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3)
)
_TlpUps_ObjectIdentity = ObjectIdentity
tlpUps = _TlpUps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1)
)
_TlpUpsIdent_ObjectIdentity = ObjectIdentity
tlpUpsIdent = _TlpUpsIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 1)
)
_TlpUpsIdentNumUps_Type = Unsigned32
_TlpUpsIdentNumUps_Object = MibScalar
tlpUpsIdentNumUps = _TlpUpsIdentNumUps_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 1, 1),
    _TlpUpsIdentNumUps_Type()
)
tlpUpsIdentNumUps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsIdentNumUps.setStatus("current")
_TlpUpsIdentTable_Object = MibTable
tlpUpsIdentTable = _TlpUpsIdentTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    tlpUpsIdentTable.setStatus("current")
_TlpUpsIdentEntry_Object = MibTableRow
tlpUpsIdentEntry = _TlpUpsIdentEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 1, 2, 1)
)
tlpUpsIdentEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpUpsIdentEntry.setStatus("current")
_TlpUpsIdentNumInputs_Type = Unsigned32
_TlpUpsIdentNumInputs_Object = MibTableColumn
tlpUpsIdentNumInputs = _TlpUpsIdentNumInputs_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 1, 2, 1, 1),
    _TlpUpsIdentNumInputs_Type()
)
tlpUpsIdentNumInputs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsIdentNumInputs.setStatus("current")
_TlpUpsIdentNumOutputs_Type = Unsigned32
_TlpUpsIdentNumOutputs_Object = MibTableColumn
tlpUpsIdentNumOutputs = _TlpUpsIdentNumOutputs_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 1, 2, 1, 2),
    _TlpUpsIdentNumOutputs_Type()
)
tlpUpsIdentNumOutputs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsIdentNumOutputs.setStatus("current")
_TlpUpsIdentNumBypass_Type = Unsigned32
_TlpUpsIdentNumBypass_Object = MibTableColumn
tlpUpsIdentNumBypass = _TlpUpsIdentNumBypass_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 1, 2, 1, 3),
    _TlpUpsIdentNumBypass_Type()
)
tlpUpsIdentNumBypass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsIdentNumBypass.setStatus("current")
_TlpUpsIdentNumPhases_Type = Unsigned32
_TlpUpsIdentNumPhases_Object = MibTableColumn
tlpUpsIdentNumPhases = _TlpUpsIdentNumPhases_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 1, 2, 1, 4),
    _TlpUpsIdentNumPhases_Type()
)
tlpUpsIdentNumPhases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsIdentNumPhases.setStatus("current")
_TlpUpsIdentNumOutlets_Type = Unsigned32
_TlpUpsIdentNumOutlets_Object = MibTableColumn
tlpUpsIdentNumOutlets = _TlpUpsIdentNumOutlets_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 1, 2, 1, 5),
    _TlpUpsIdentNumOutlets_Type()
)
tlpUpsIdentNumOutlets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsIdentNumOutlets.setStatus("current")
_TlpUpsIdentNumOutletGroups_Type = Unsigned32
_TlpUpsIdentNumOutletGroups_Object = MibTableColumn
tlpUpsIdentNumOutletGroups = _TlpUpsIdentNumOutletGroups_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 1, 2, 1, 6),
    _TlpUpsIdentNumOutletGroups_Type()
)
tlpUpsIdentNumOutletGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsIdentNumOutletGroups.setStatus("current")
_TlpUpsIdentNumBatteries_Type = Unsigned32
_TlpUpsIdentNumBatteries_Object = MibTableColumn
tlpUpsIdentNumBatteries = _TlpUpsIdentNumBatteries_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 1, 2, 1, 7),
    _TlpUpsIdentNumBatteries_Type()
)
tlpUpsIdentNumBatteries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsIdentNumBatteries.setStatus("current")
_TlpUpsIdentNumFans_Type = Unsigned32
_TlpUpsIdentNumFans_Object = MibTableColumn
tlpUpsIdentNumFans = _TlpUpsIdentNumFans_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 1, 2, 1, 8),
    _TlpUpsIdentNumFans_Type()
)
tlpUpsIdentNumFans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsIdentNumFans.setStatus("current")
_TlpUpsIdentNumHeatsinks_Type = Unsigned32
_TlpUpsIdentNumHeatsinks_Object = MibTableColumn
tlpUpsIdentNumHeatsinks = _TlpUpsIdentNumHeatsinks_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 1, 2, 1, 9),
    _TlpUpsIdentNumHeatsinks_Type()
)
tlpUpsIdentNumHeatsinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsIdentNumHeatsinks.setStatus("current")
_TlpUpsIdentNumInputContacts_Type = Unsigned32
_TlpUpsIdentNumInputContacts_Object = MibTableColumn
tlpUpsIdentNumInputContacts = _TlpUpsIdentNumInputContacts_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 1, 2, 1, 10),
    _TlpUpsIdentNumInputContacts_Type()
)
tlpUpsIdentNumInputContacts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsIdentNumInputContacts.setStatus("current")
_TlpUpsIdentNumOutputContacts_Type = Unsigned32
_TlpUpsIdentNumOutputContacts_Object = MibTableColumn
tlpUpsIdentNumOutputContacts = _TlpUpsIdentNumOutputContacts_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 1, 2, 1, 11),
    _TlpUpsIdentNumOutputContacts_Type()
)
tlpUpsIdentNumOutputContacts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsIdentNumOutputContacts.setStatus("current")
_TlpUpsIdentNumActiveControlModules_Type = Unsigned32
_TlpUpsIdentNumActiveControlModules_Object = MibTableColumn
tlpUpsIdentNumActiveControlModules = _TlpUpsIdentNumActiveControlModules_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 1, 2, 1, 12),
    _TlpUpsIdentNumActiveControlModules_Type()
)
tlpUpsIdentNumActiveControlModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsIdentNumActiveControlModules.setStatus("current")
_TlpUpsIdentNumRedundantControlModules_Type = Unsigned32
_TlpUpsIdentNumRedundantControlModules_Object = MibTableColumn
tlpUpsIdentNumRedundantControlModules = _TlpUpsIdentNumRedundantControlModules_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 1, 2, 1, 13),
    _TlpUpsIdentNumRedundantControlModules_Type()
)
tlpUpsIdentNumRedundantControlModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsIdentNumRedundantControlModules.setStatus("current")
_TlpUpsSupportsTable_Object = MibTable
tlpUpsSupportsTable = _TlpUpsSupportsTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 1, 3)
)
if mibBuilder.loadTexts:
    tlpUpsSupportsTable.setStatus("current")
_TlpUpsSupportsEntry_Object = MibTableRow
tlpUpsSupportsEntry = _TlpUpsSupportsEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 1, 3, 1)
)
tlpUpsSupportsEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpUpsSupportsEntry.setStatus("current")
_TlpUpsSupportsEnergywise_Type = TruthValue
_TlpUpsSupportsEnergywise_Object = MibTableColumn
tlpUpsSupportsEnergywise = _TlpUpsSupportsEnergywise_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 1, 3, 1, 1),
    _TlpUpsSupportsEnergywise_Type()
)
tlpUpsSupportsEnergywise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsSupportsEnergywise.setStatus("deprecated")
_TlpUpsSupportsRampShed_Type = TruthValue
_TlpUpsSupportsRampShed_Object = MibTableColumn
tlpUpsSupportsRampShed = _TlpUpsSupportsRampShed_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 1, 3, 1, 2),
    _TlpUpsSupportsRampShed_Type()
)
tlpUpsSupportsRampShed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsSupportsRampShed.setStatus("current")
_TlpUpsSupportsOutletGroup_Type = TruthValue
_TlpUpsSupportsOutletGroup_Object = MibTableColumn
tlpUpsSupportsOutletGroup = _TlpUpsSupportsOutletGroup_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 1, 3, 1, 3),
    _TlpUpsSupportsOutletGroup_Type()
)
tlpUpsSupportsOutletGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsSupportsOutletGroup.setStatus("current")
_TlpUpsSupportsOutletCurrent_Type = TruthValue
_TlpUpsSupportsOutletCurrent_Object = MibTableColumn
tlpUpsSupportsOutletCurrent = _TlpUpsSupportsOutletCurrent_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 1, 3, 1, 4),
    _TlpUpsSupportsOutletCurrent_Type()
)
tlpUpsSupportsOutletCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsSupportsOutletCurrent.setStatus("current")
_TlpUpsSupportsOutletVoltage_Type = TruthValue
_TlpUpsSupportsOutletVoltage_Object = MibTableColumn
tlpUpsSupportsOutletVoltage = _TlpUpsSupportsOutletVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 1, 3, 1, 5),
    _TlpUpsSupportsOutletVoltage_Type()
)
tlpUpsSupportsOutletVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsSupportsOutletVoltage.setStatus("current")
_TlpUpsSupportsOutletActivePower_Type = TruthValue
_TlpUpsSupportsOutletActivePower_Object = MibTableColumn
tlpUpsSupportsOutletActivePower = _TlpUpsSupportsOutletActivePower_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 1, 3, 1, 6),
    _TlpUpsSupportsOutletActivePower_Type()
)
tlpUpsSupportsOutletActivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsSupportsOutletActivePower.setStatus("current")
_TlpUpsDevice_ObjectIdentity = ObjectIdentity
tlpUpsDevice = _TlpUpsDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 2)
)
_TlpUpsDeviceTable_Object = MibTable
tlpUpsDeviceTable = _TlpUpsDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tlpUpsDeviceTable.setStatus("current")
_TlpUpsDeviceEntry_Object = MibTableRow
tlpUpsDeviceEntry = _TlpUpsDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 2, 1, 1)
)
tlpUpsDeviceEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpUpsDeviceEntry.setStatus("current")


class _TlpUpsDeviceMainLoadState_Type(Integer32):
    """Custom type tlpUpsDeviceMainLoadState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("off", 1),
          ("on", 2))
    )


_TlpUpsDeviceMainLoadState_Type.__name__ = "Integer32"
_TlpUpsDeviceMainLoadState_Object = MibTableColumn
tlpUpsDeviceMainLoadState = _TlpUpsDeviceMainLoadState_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 2, 1, 1, 1),
    _TlpUpsDeviceMainLoadState_Type()
)
tlpUpsDeviceMainLoadState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsDeviceMainLoadState.setStatus("current")
_TlpUpsDeviceMainLoadControllable_Type = TruthValue
_TlpUpsDeviceMainLoadControllable_Object = MibTableColumn
tlpUpsDeviceMainLoadControllable = _TlpUpsDeviceMainLoadControllable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 2, 1, 1, 2),
    _TlpUpsDeviceMainLoadControllable_Type()
)
tlpUpsDeviceMainLoadControllable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsDeviceMainLoadControllable.setStatus("current")


class _TlpUpsDeviceMainLoadCommand_Type(Integer32):
    """Custom type tlpUpsDeviceMainLoadCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("turnOff", 1),
          ("turnOn", 2),
          ("cycle", 3))
    )


_TlpUpsDeviceMainLoadCommand_Type.__name__ = "Integer32"
_TlpUpsDeviceMainLoadCommand_Object = MibTableColumn
tlpUpsDeviceMainLoadCommand = _TlpUpsDeviceMainLoadCommand_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 2, 1, 1, 3),
    _TlpUpsDeviceMainLoadCommand_Type()
)
tlpUpsDeviceMainLoadCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsDeviceMainLoadCommand.setStatus("current")
_TlpUpsDevicePowerOnDelay_Type = Integer32
_TlpUpsDevicePowerOnDelay_Object = MibTableColumn
tlpUpsDevicePowerOnDelay = _TlpUpsDevicePowerOnDelay_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 2, 1, 1, 4),
    _TlpUpsDevicePowerOnDelay_Type()
)
tlpUpsDevicePowerOnDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsDevicePowerOnDelay.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsDevicePowerOnDelay.setUnits("Seconds")
_TlpUpsDeviceTestDate_Type = DisplayString
_TlpUpsDeviceTestDate_Object = MibTableColumn
tlpUpsDeviceTestDate = _TlpUpsDeviceTestDate_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 2, 1, 1, 5),
    _TlpUpsDeviceTestDate_Type()
)
tlpUpsDeviceTestDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsDeviceTestDate.setStatus("current")


class _TlpUpsDeviceTestResultsStatus_Type(Integer32):
    """Custom type tlpUpsDeviceTestResultsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("noTest", 0),
          ("doneAndPassed", 1),
          ("doneAndWarning", 2),
          ("doneAndError", 3),
          ("aborted", 4),
          ("inProgress", 5),
          ("noTestInitiatedDeprecated", 6),
          ("badBattery", 7),
          ("overCurrent", 8),
          ("batteryFailed", 9))
    )


_TlpUpsDeviceTestResultsStatus_Type.__name__ = "Integer32"
_TlpUpsDeviceTestResultsStatus_Object = MibTableColumn
tlpUpsDeviceTestResultsStatus = _TlpUpsDeviceTestResultsStatus_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 2, 1, 1, 6),
    _TlpUpsDeviceTestResultsStatus_Type()
)
tlpUpsDeviceTestResultsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsDeviceTestResultsStatus.setStatus("current")
_TlpUpsDeviceTemperatureC_Type = Integer32
_TlpUpsDeviceTemperatureC_Object = MibTableColumn
tlpUpsDeviceTemperatureC = _TlpUpsDeviceTemperatureC_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 2, 1, 1, 7),
    _TlpUpsDeviceTemperatureC_Type()
)
tlpUpsDeviceTemperatureC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsDeviceTemperatureC.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsDeviceTemperatureC.setUnits("0.1 degrees Celsius")
_TlpUpsDeviceTemperatureF_Type = Integer32
_TlpUpsDeviceTemperatureF_Object = MibTableColumn
tlpUpsDeviceTemperatureF = _TlpUpsDeviceTemperatureF_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 2, 1, 1, 8),
    _TlpUpsDeviceTemperatureF_Type()
)
tlpUpsDeviceTemperatureF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsDeviceTemperatureF.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsDeviceTemperatureF.setUnits("0.1 degrees Fahrenheit")


class _TlpUpsDeviceLastACFailureReason_Type(Integer32):
    """Custom type tlpUpsDeviceLastACFailureReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("noACFailureSinceReset", 0),
          ("blackout", 1),
          ("instantaneousHighLineFrequency", 2),
          ("highLineVoltage", 3),
          ("lowLineVoltage", 4),
          ("averageFrequencyFault", 5),
          ("instantaneousLowLineFrequency", 6),
          ("delayedBrownout", 7))
    )


_TlpUpsDeviceLastACFailureReason_Type.__name__ = "Integer32"
_TlpUpsDeviceLastACFailureReason_Object = MibTableColumn
tlpUpsDeviceLastACFailureReason = _TlpUpsDeviceLastACFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 2, 1, 1, 9),
    _TlpUpsDeviceLastACFailureReason_Type()
)
tlpUpsDeviceLastACFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsDeviceLastACFailureReason.setStatus("current")


class _TlpUpsDeviceLastShutdownReason_Type(Integer32):
    """Custom type tlpUpsDeviceLastShutdownReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32)
        )
    )
    namedValues = NamedValues(
        *(("noShutdownSinceReset", 0),
          ("onOffButtonShutdown", 1),
          ("averageVbattSmallerThenLVCShutdown", 2),
          ("fastVbattKeepaliveVoltageFastShutdown", 3),
          ("averageCurrentLimitShutdown", 4),
          ("fastCurrentLimitShutdown", 5),
          ("heavyLoadThermalTimeLimitShutdown", 6),
          ("fixedInvertModeTimeLimitShutdown", 7),
          ("highBatteryVoltageFault", 8),
          ("averageVbattKeepaliveVoltageShutdown", 9),
          ("shutdownCommandWithAutorestartEnabled", 10),
          ("shutdownCommandWithoutAutorestartEnabled", 11),
          ("lineConnectRelayFault", 12),
          ("epoInvertMode", 13),
          ("epoRestartMode", 14),
          ("invalidLineStandbyMode", 15),
          ("chargerLimitMinBatteryVoltage", 16),
          ("chargerLimitMaxBatteryVoltage", 17),
          ("invalidLineDelayedWakeupAutorestartEnabled", 18),
          ("invalidLineDelayedWakeupAutorestartDisabled", 19),
          ("minBatteryVoltagePriorDelayedWakeupAutorestartEnabled", 20),
          ("minBatteryVoltagePriorDelayedWakeupAutorestartDisabled", 21),
          ("lvcShutdownAutorestartEnabled", 22),
          ("lvcShutdownAutorestartDisabled", 23),
          ("overloadShutdownAutorestartEnabled", 24),
          ("overloadShutdownAutorestartDisabled", 25),
          ("overTemperatureShutdownAutorestartEnabled", 26),
          ("overTemperatureShutdownAutorestartDisabled", 27),
          ("onOffButtonShutdownAutorestartEnabled", 28),
          ("onOffButtonShutdownAutorestartDisabled", 29),
          ("batteryReportedFault", 30),
          ("batteryCommunicationLost", 31),
          ("batteryJumpStartChargerTimeoutError", 32))
    )


_TlpUpsDeviceLastShutdownReason_Type.__name__ = "Integer32"
_TlpUpsDeviceLastShutdownReason_Object = MibTableColumn
tlpUpsDeviceLastShutdownReason = _TlpUpsDeviceLastShutdownReason_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 2, 1, 1, 10),
    _TlpUpsDeviceLastShutdownReason_Type()
)
tlpUpsDeviceLastShutdownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsDeviceLastShutdownReason.setStatus("current")


class _TlpUpsDeviceOutputCurrentPrecision_Type(Integer32):
    """Custom type tlpUpsDeviceOutputCurrentPrecision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wholeNumber", 0),
          ("tenths", 1),
          ("hundredths", 2))
    )


_TlpUpsDeviceOutputCurrentPrecision_Type.__name__ = "Integer32"
_TlpUpsDeviceOutputCurrentPrecision_Object = MibTableColumn
tlpUpsDeviceOutputCurrentPrecision = _TlpUpsDeviceOutputCurrentPrecision_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 2, 1, 1, 11),
    _TlpUpsDeviceOutputCurrentPrecision_Type()
)
tlpUpsDeviceOutputCurrentPrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsDeviceOutputCurrentPrecision.setStatus("current")
_TlpUpsDeviceOutputActivePowerTotal_Type = Unsigned32
_TlpUpsDeviceOutputActivePowerTotal_Object = MibTableColumn
tlpUpsDeviceOutputActivePowerTotal = _TlpUpsDeviceOutputActivePowerTotal_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 2, 1, 1, 12),
    _TlpUpsDeviceOutputActivePowerTotal_Type()
)
tlpUpsDeviceOutputActivePowerTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsDeviceOutputActivePowerTotal.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsDeviceOutputActivePowerTotal.setUnits("Watts")
_TlpUpsDeviceAggregatePowerFactor_Type = Unsigned32
_TlpUpsDeviceAggregatePowerFactor_Object = MibTableColumn
tlpUpsDeviceAggregatePowerFactor = _TlpUpsDeviceAggregatePowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 2, 1, 1, 13),
    _TlpUpsDeviceAggregatePowerFactor_Type()
)
tlpUpsDeviceAggregatePowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsDeviceAggregatePowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsDeviceAggregatePowerFactor.setUnits("0.1 Watts")
_TlpUpsDeviceGeneralFault_Type = TruthValue
_TlpUpsDeviceGeneralFault_Object = MibTableColumn
tlpUpsDeviceGeneralFault = _TlpUpsDeviceGeneralFault_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 2, 1, 1, 14),
    _TlpUpsDeviceGeneralFault_Type()
)
tlpUpsDeviceGeneralFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsDeviceGeneralFault.setStatus("current")


class _TlpUpsDeviceUpsType_Type(Integer32):
    """Custom type tlpUpsDeviceUpsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("onLine", 0),
          ("offLine", 1),
          ("lineInteractive", 2),
          ("threePhase", 3),
          ("splitPhase", 4),
          ("others", 5),
          ("splitPhaseOld", 6))
    )


_TlpUpsDeviceUpsType_Type.__name__ = "Integer32"
_TlpUpsDeviceUpsType_Object = MibTableColumn
tlpUpsDeviceUpsType = _TlpUpsDeviceUpsType_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 2, 1, 1, 15),
    _TlpUpsDeviceUpsType_Type()
)
tlpUpsDeviceUpsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsDeviceUpsType.setStatus("current")


class _TlpUpsDeviceLastBypassReason_Type(Integer32):
    """Custom type tlpUpsDeviceLastBypassReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("noBypassSinceReset", 0),
          ("overLoad", 1),
          ("overTemperature", 2),
          ("dcBusAbnormal", 3),
          ("inverterStsFailure", 4),
          ("inverterVoltageAbnormal", 5),
          ("fuseOpen", 6),
          ("internalCommunicationsFailure", 7),
          ("softStartFailure", 8))
    )


_TlpUpsDeviceLastBypassReason_Type.__name__ = "Integer32"
_TlpUpsDeviceLastBypassReason_Object = MibTableColumn
tlpUpsDeviceLastBypassReason = _TlpUpsDeviceLastBypassReason_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 2, 1, 1, 16),
    _TlpUpsDeviceLastBypassReason_Type()
)
tlpUpsDeviceLastBypassReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsDeviceLastBypassReason.setStatus("current")


class _TlpUpsDeviceBuzzerStatus_Type(Integer32):
    """Custom type tlpUpsDeviceBuzzerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("silent", 0),
          ("buzzing", 1))
    )


_TlpUpsDeviceBuzzerStatus_Type.__name__ = "Integer32"
_TlpUpsDeviceBuzzerStatus_Object = MibTableColumn
tlpUpsDeviceBuzzerStatus = _TlpUpsDeviceBuzzerStatus_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 2, 1, 1, 17),
    _TlpUpsDeviceBuzzerStatus_Type()
)
tlpUpsDeviceBuzzerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsDeviceBuzzerStatus.setStatus("current")
_TlpUpsDetail_ObjectIdentity = ObjectIdentity
tlpUpsDetail = _TlpUpsDetail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3)
)
_TlpUpsBattery_ObjectIdentity = ObjectIdentity
tlpUpsBattery = _TlpUpsBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1)
)
_TlpUpsBatterySummaryTable_Object = MibTable
tlpUpsBatterySummaryTable = _TlpUpsBatterySummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    tlpUpsBatterySummaryTable.setStatus("current")
_TlpUpsBatterySummaryEntry_Object = MibTableRow
tlpUpsBatterySummaryEntry = _TlpUpsBatterySummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 1, 1)
)
tlpUpsBatterySummaryEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpUpsBatterySummaryEntry.setStatus("current")


class _TlpUpsBatteryStatus_Type(Integer32):
    """Custom type tlpUpsBatteryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("batteryNormal", 2),
          ("batteryLow", 3),
          ("batteryDepleted", 4))
    )


_TlpUpsBatteryStatus_Type.__name__ = "Integer32"
_TlpUpsBatteryStatus_Object = MibTableColumn
tlpUpsBatteryStatus = _TlpUpsBatteryStatus_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 1, 1, 1),
    _TlpUpsBatteryStatus_Type()
)
tlpUpsBatteryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryStatus.setStatus("current")
_TlpUpsSecondsOnBattery_Type = Unsigned32
_TlpUpsSecondsOnBattery_Object = MibTableColumn
tlpUpsSecondsOnBattery = _TlpUpsSecondsOnBattery_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 1, 1, 2),
    _TlpUpsSecondsOnBattery_Type()
)
tlpUpsSecondsOnBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsSecondsOnBattery.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsSecondsOnBattery.setUnits("seconds")
_TlpUpsEstimatedMinutesRemaining_Type = Unsigned32
_TlpUpsEstimatedMinutesRemaining_Object = MibTableColumn
tlpUpsEstimatedMinutesRemaining = _TlpUpsEstimatedMinutesRemaining_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 1, 1, 3),
    _TlpUpsEstimatedMinutesRemaining_Type()
)
tlpUpsEstimatedMinutesRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsEstimatedMinutesRemaining.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsEstimatedMinutesRemaining.setUnits("minutes")


class _TlpUpsEstimatedChargeRemaining_Type(Integer32):
    """Custom type tlpUpsEstimatedChargeRemaining based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TlpUpsEstimatedChargeRemaining_Type.__name__ = "Integer32"
_TlpUpsEstimatedChargeRemaining_Object = MibTableColumn
tlpUpsEstimatedChargeRemaining = _TlpUpsEstimatedChargeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 1, 1, 4),
    _TlpUpsEstimatedChargeRemaining_Type()
)
tlpUpsEstimatedChargeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsEstimatedChargeRemaining.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsEstimatedChargeRemaining.setUnits("percent")
_TlpUpsBatteryRunTimeRemaining_Type = TimeTicks
_TlpUpsBatteryRunTimeRemaining_Object = MibTableColumn
tlpUpsBatteryRunTimeRemaining = _TlpUpsBatteryRunTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 1, 1, 5),
    _TlpUpsBatteryRunTimeRemaining_Type()
)
tlpUpsBatteryRunTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryRunTimeRemaining.setStatus("current")
_TlpUpsBatteryTotalMinutesOnBattery_Type = Unsigned32
_TlpUpsBatteryTotalMinutesOnBattery_Object = MibTableColumn
tlpUpsBatteryTotalMinutesOnBattery = _TlpUpsBatteryTotalMinutesOnBattery_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 1, 1, 6),
    _TlpUpsBatteryTotalMinutesOnBattery_Type()
)
tlpUpsBatteryTotalMinutesOnBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryTotalMinutesOnBattery.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsBatteryTotalMinutesOnBattery.setUnits("minutes")
_TlpUpsBatteryDetailTable_Object = MibTable
tlpUpsBatteryDetailTable = _TlpUpsBatteryDetailTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    tlpUpsBatteryDetailTable.setStatus("current")
_TlpUpsBatteryDetailEntry_Object = MibTableRow
tlpUpsBatteryDetailEntry = _TlpUpsBatteryDetailEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 2, 1)
)
tlpUpsBatteryDetailEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpUpsBatteryDetailEntry.setStatus("current")
_TlpUpsBatteryDetailVoltage_Type = Unsigned32
_TlpUpsBatteryDetailVoltage_Object = MibTableColumn
tlpUpsBatteryDetailVoltage = _TlpUpsBatteryDetailVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 2, 1, 1),
    _TlpUpsBatteryDetailVoltage_Type()
)
tlpUpsBatteryDetailVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryDetailVoltage.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsBatteryDetailVoltage.setUnits("0.1 Volt DC")
_TlpUpsBatteryDetailCurrent_Type = Integer32
_TlpUpsBatteryDetailCurrent_Object = MibTableColumn
tlpUpsBatteryDetailCurrent = _TlpUpsBatteryDetailCurrent_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 2, 1, 2),
    _TlpUpsBatteryDetailCurrent_Type()
)
tlpUpsBatteryDetailCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryDetailCurrent.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsBatteryDetailCurrent.setUnits("0.01 Amps DC")


class _TlpUpsBatteryDetailCapacity_Type(Integer32):
    """Custom type tlpUpsBatteryDetailCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TlpUpsBatteryDetailCapacity_Type.__name__ = "Integer32"
_TlpUpsBatteryDetailCapacity_Object = MibTableColumn
tlpUpsBatteryDetailCapacity = _TlpUpsBatteryDetailCapacity_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 2, 1, 3),
    _TlpUpsBatteryDetailCapacity_Type()
)
tlpUpsBatteryDetailCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryDetailCapacity.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsBatteryDetailCapacity.setUnits("percent")


class _TlpUpsBatteryDetailCharge_Type(Integer32):
    """Custom type tlpUpsBatteryDetailCharge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("floating", 0),
          ("charging", 1),
          ("resting", 2),
          ("discharging", 3),
          ("normal", 4),
          ("standby", 5))
    )


_TlpUpsBatteryDetailCharge_Type.__name__ = "Integer32"
_TlpUpsBatteryDetailCharge_Object = MibTableColumn
tlpUpsBatteryDetailCharge = _TlpUpsBatteryDetailCharge_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 2, 1, 4),
    _TlpUpsBatteryDetailCharge_Type()
)
tlpUpsBatteryDetailCharge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryDetailCharge.setStatus("current")


class _TlpUpsBatteryDetailChargerStatus_Type(Integer32):
    """Custom type tlpUpsBatteryDetailChargerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("inFaultCondition", 1))
    )


_TlpUpsBatteryDetailChargerStatus_Type.__name__ = "Integer32"
_TlpUpsBatteryDetailChargerStatus_Object = MibTableColumn
tlpUpsBatteryDetailChargerStatus = _TlpUpsBatteryDetailChargerStatus_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 2, 1, 5),
    _TlpUpsBatteryDetailChargerStatus_Type()
)
tlpUpsBatteryDetailChargerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryDetailChargerStatus.setStatus("current")
_TlpUpsBatteryDetailNominalVoltage_Type = Unsigned32
_TlpUpsBatteryDetailNominalVoltage_Object = MibTableColumn
tlpUpsBatteryDetailNominalVoltage = _TlpUpsBatteryDetailNominalVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 2, 1, 6),
    _TlpUpsBatteryDetailNominalVoltage_Type()
)
tlpUpsBatteryDetailNominalVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryDetailNominalVoltage.setStatus("current")
_TlpUpsBatteryDetailFullyCharged_Type = TruthValue
_TlpUpsBatteryDetailFullyCharged_Object = MibTableColumn
tlpUpsBatteryDetailFullyCharged = _TlpUpsBatteryDetailFullyCharged_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 2, 1, 7),
    _TlpUpsBatteryDetailFullyCharged_Type()
)
tlpUpsBatteryDetailFullyCharged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryDetailFullyCharged.setStatus("current")
_TlpUpsBatteryDetailOvercharged_Type = TruthValue
_TlpUpsBatteryDetailOvercharged_Object = MibTableColumn
tlpUpsBatteryDetailOvercharged = _TlpUpsBatteryDetailOvercharged_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 2, 1, 8),
    _TlpUpsBatteryDetailOvercharged_Type()
)
tlpUpsBatteryDetailOvercharged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryDetailOvercharged.setStatus("current")
_TlpUpsBatteryDetailVoltageNegative_Type = Unsigned32
_TlpUpsBatteryDetailVoltageNegative_Object = MibTableColumn
tlpUpsBatteryDetailVoltageNegative = _TlpUpsBatteryDetailVoltageNegative_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 2, 1, 9),
    _TlpUpsBatteryDetailVoltageNegative_Type()
)
tlpUpsBatteryDetailVoltageNegative.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryDetailVoltageNegative.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsBatteryDetailVoltageNegative.setUnits("0.1 Volt DC")
_TlpUpsBatteryDetailVoltagePositive_Type = Unsigned32
_TlpUpsBatteryDetailVoltagePositive_Object = MibTableColumn
tlpUpsBatteryDetailVoltagePositive = _TlpUpsBatteryDetailVoltagePositive_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 2, 1, 10),
    _TlpUpsBatteryDetailVoltagePositive_Type()
)
tlpUpsBatteryDetailVoltagePositive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryDetailVoltagePositive.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsBatteryDetailVoltagePositive.setUnits("0.1 Volt DC")


class _TlpUpsBatteryDetailMaxChargerCurrent_Type(Integer32):
    """Custom type tlpUpsBatteryDetailMaxChargerCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TlpUpsBatteryDetailMaxChargerCurrent_Type.__name__ = "Integer32"
_TlpUpsBatteryDetailMaxChargerCurrent_Object = MibTableColumn
tlpUpsBatteryDetailMaxChargerCurrent = _TlpUpsBatteryDetailMaxChargerCurrent_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 2, 1, 11),
    _TlpUpsBatteryDetailMaxChargerCurrent_Type()
)
tlpUpsBatteryDetailMaxChargerCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryDetailMaxChargerCurrent.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsBatteryDetailMaxChargerCurrent.setUnits("Amps")
_TlpUpsBatteryPackIdentTable_Object = MibTable
tlpUpsBatteryPackIdentTable = _TlpUpsBatteryPackIdentTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 3)
)
if mibBuilder.loadTexts:
    tlpUpsBatteryPackIdentTable.setStatus("current")
_TlpUpsBatteryPackIdentEntry_Object = MibTableRow
tlpUpsBatteryPackIdentEntry = _TlpUpsBatteryPackIdentEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 3, 1)
)
tlpUpsBatteryPackIdentEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpUpsBatteryPackIdentIndex"),
)
if mibBuilder.loadTexts:
    tlpUpsBatteryPackIdentEntry.setStatus("current")
_TlpUpsBatteryPackIdentIndex_Type = Unsigned32
_TlpUpsBatteryPackIdentIndex_Object = MibTableColumn
tlpUpsBatteryPackIdentIndex = _TlpUpsBatteryPackIdentIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 3, 1, 1),
    _TlpUpsBatteryPackIdentIndex_Type()
)
tlpUpsBatteryPackIdentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryPackIdentIndex.setStatus("current")
_TlpUpsBatteryPackIdentManufacturer_Type = DisplayString
_TlpUpsBatteryPackIdentManufacturer_Object = MibTableColumn
tlpUpsBatteryPackIdentManufacturer = _TlpUpsBatteryPackIdentManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 3, 1, 2),
    _TlpUpsBatteryPackIdentManufacturer_Type()
)
tlpUpsBatteryPackIdentManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryPackIdentManufacturer.setStatus("current")
_TlpUpsBatteryPackIdentModel_Type = DisplayString
_TlpUpsBatteryPackIdentModel_Object = MibTableColumn
tlpUpsBatteryPackIdentModel = _TlpUpsBatteryPackIdentModel_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 3, 1, 3),
    _TlpUpsBatteryPackIdentModel_Type()
)
tlpUpsBatteryPackIdentModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryPackIdentModel.setStatus("current")
_TlpUpsBatteryPackIdentSerialNum_Type = DisplayString
_TlpUpsBatteryPackIdentSerialNum_Object = MibTableColumn
tlpUpsBatteryPackIdentSerialNum = _TlpUpsBatteryPackIdentSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 3, 1, 4),
    _TlpUpsBatteryPackIdentSerialNum_Type()
)
tlpUpsBatteryPackIdentSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryPackIdentSerialNum.setStatus("current")
_TlpUpsBatteryPackIdentFirmware_Type = DisplayString
_TlpUpsBatteryPackIdentFirmware_Object = MibTableColumn
tlpUpsBatteryPackIdentFirmware = _TlpUpsBatteryPackIdentFirmware_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 3, 1, 5),
    _TlpUpsBatteryPackIdentFirmware_Type()
)
tlpUpsBatteryPackIdentFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryPackIdentFirmware.setStatus("current")
_TlpUpsBatteryPackIdentSKU_Type = DisplayString
_TlpUpsBatteryPackIdentSKU_Object = MibTableColumn
tlpUpsBatteryPackIdentSKU = _TlpUpsBatteryPackIdentSKU_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 3, 1, 6),
    _TlpUpsBatteryPackIdentSKU_Type()
)
tlpUpsBatteryPackIdentSKU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryPackIdentSKU.setStatus("current")
_TlpUpsBatteryPackConfigTable_Object = MibTable
tlpUpsBatteryPackConfigTable = _TlpUpsBatteryPackConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 4)
)
if mibBuilder.loadTexts:
    tlpUpsBatteryPackConfigTable.setStatus("current")
_TlpUpsBatteryPackConfigEntry_Object = MibTableRow
tlpUpsBatteryPackConfigEntry = _TlpUpsBatteryPackConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 4, 1)
)
tlpUpsBatteryPackConfigEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpUpsBatteryPackIdentIndex"),
)
if mibBuilder.loadTexts:
    tlpUpsBatteryPackConfigEntry.setStatus("current")


class _TlpUpsBatteryPackConfigChemistry_Type(Integer32):
    """Custom type tlpUpsBatteryPackConfigChemistry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("leadAcid", 1),
          ("nickelCadmium", 2),
          ("lithiumIon", 3))
    )


_TlpUpsBatteryPackConfigChemistry_Type.__name__ = "Integer32"
_TlpUpsBatteryPackConfigChemistry_Object = MibTableColumn
tlpUpsBatteryPackConfigChemistry = _TlpUpsBatteryPackConfigChemistry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 4, 1, 1),
    _TlpUpsBatteryPackConfigChemistry_Type()
)
tlpUpsBatteryPackConfigChemistry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryPackConfigChemistry.setStatus("current")


class _TlpUpsBatteryPackConfigStyle_Type(Integer32):
    """Custom type tlpUpsBatteryPackConfigStyle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("nonsmart", 1),
          ("smart", 2),
          ("bms", 3))
    )


_TlpUpsBatteryPackConfigStyle_Type.__name__ = "Integer32"
_TlpUpsBatteryPackConfigStyle_Object = MibTableColumn
tlpUpsBatteryPackConfigStyle = _TlpUpsBatteryPackConfigStyle_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 4, 1, 2),
    _TlpUpsBatteryPackConfigStyle_Type()
)
tlpUpsBatteryPackConfigStyle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryPackConfigStyle.setStatus("current")


class _TlpUpsBatteryPackConfigLocation_Type(Integer32):
    """Custom type tlpUpsBatteryPackConfigLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("internal", 1),
          ("external", 2))
    )


_TlpUpsBatteryPackConfigLocation_Type.__name__ = "Integer32"
_TlpUpsBatteryPackConfigLocation_Object = MibTableColumn
tlpUpsBatteryPackConfigLocation = _TlpUpsBatteryPackConfigLocation_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 4, 1, 3),
    _TlpUpsBatteryPackConfigLocation_Type()
)
tlpUpsBatteryPackConfigLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryPackConfigLocation.setStatus("current")
_TlpUpsBatteryPackConfigStrings_Type = Unsigned32
_TlpUpsBatteryPackConfigStrings_Object = MibTableColumn
tlpUpsBatteryPackConfigStrings = _TlpUpsBatteryPackConfigStrings_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 4, 1, 4),
    _TlpUpsBatteryPackConfigStrings_Type()
)
tlpUpsBatteryPackConfigStrings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryPackConfigStrings.setStatus("current")
_TlpUpsBatteryPackConfigBatteriesPerString_Type = Unsigned32
_TlpUpsBatteryPackConfigBatteriesPerString_Object = MibTableColumn
tlpUpsBatteryPackConfigBatteriesPerString = _TlpUpsBatteryPackConfigBatteriesPerString_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 4, 1, 5),
    _TlpUpsBatteryPackConfigBatteriesPerString_Type()
)
tlpUpsBatteryPackConfigBatteriesPerString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryPackConfigBatteriesPerString.setStatus("current")
_TlpUpsBatteryPackConfigCellsPerBattery_Type = Integer32
_TlpUpsBatteryPackConfigCellsPerBattery_Object = MibTableColumn
tlpUpsBatteryPackConfigCellsPerBattery = _TlpUpsBatteryPackConfigCellsPerBattery_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 4, 1, 6),
    _TlpUpsBatteryPackConfigCellsPerBattery_Type()
)
tlpUpsBatteryPackConfigCellsPerBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryPackConfigCellsPerBattery.setStatus("current")
_TlpUpsBatteryPackConfigNumBatteries_Type = Unsigned32
_TlpUpsBatteryPackConfigNumBatteries_Object = MibTableColumn
tlpUpsBatteryPackConfigNumBatteries = _TlpUpsBatteryPackConfigNumBatteries_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 4, 1, 7),
    _TlpUpsBatteryPackConfigNumBatteries_Type()
)
tlpUpsBatteryPackConfigNumBatteries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryPackConfigNumBatteries.setStatus("current")


class _TlpUpsBatteryPackConfigCapacityUnits_Type(Integer32):
    """Custom type tlpUpsBatteryPackConfigCapacityUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("mAHr", 0),
          ("mWHr", 1))
    )


_TlpUpsBatteryPackConfigCapacityUnits_Type.__name__ = "Integer32"
_TlpUpsBatteryPackConfigCapacityUnits_Object = MibTableColumn
tlpUpsBatteryPackConfigCapacityUnits = _TlpUpsBatteryPackConfigCapacityUnits_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 4, 1, 8),
    _TlpUpsBatteryPackConfigCapacityUnits_Type()
)
tlpUpsBatteryPackConfigCapacityUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryPackConfigCapacityUnits.setStatus("current")
_TlpUpsBatteryPackConfigDesignCapacity_Type = Unsigned32
_TlpUpsBatteryPackConfigDesignCapacity_Object = MibTableColumn
tlpUpsBatteryPackConfigDesignCapacity = _TlpUpsBatteryPackConfigDesignCapacity_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 4, 1, 9),
    _TlpUpsBatteryPackConfigDesignCapacity_Type()
)
tlpUpsBatteryPackConfigDesignCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryPackConfigDesignCapacity.setStatus("current")
_TlpUpsBatteryPackConfigCellCapacity_Type = Unsigned32
_TlpUpsBatteryPackConfigCellCapacity_Object = MibTableColumn
tlpUpsBatteryPackConfigCellCapacity = _TlpUpsBatteryPackConfigCellCapacity_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 4, 1, 10),
    _TlpUpsBatteryPackConfigCellCapacity_Type()
)
tlpUpsBatteryPackConfigCellCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryPackConfigCellCapacity.setStatus("current")
_TlpUpsBatteryPackConfigMinCellVoltage_Type = Unsigned32
_TlpUpsBatteryPackConfigMinCellVoltage_Object = MibTableColumn
tlpUpsBatteryPackConfigMinCellVoltage = _TlpUpsBatteryPackConfigMinCellVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 4, 1, 11),
    _TlpUpsBatteryPackConfigMinCellVoltage_Type()
)
tlpUpsBatteryPackConfigMinCellVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryPackConfigMinCellVoltage.setStatus("current")
_TlpUpsBatteryPackConfigMaxCellVoltage_Type = Unsigned32
_TlpUpsBatteryPackConfigMaxCellVoltage_Object = MibTableColumn
tlpUpsBatteryPackConfigMaxCellVoltage = _TlpUpsBatteryPackConfigMaxCellVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 4, 1, 12),
    _TlpUpsBatteryPackConfigMaxCellVoltage_Type()
)
tlpUpsBatteryPackConfigMaxCellVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryPackConfigMaxCellVoltage.setStatus("current")
_TlpUpsBatteryPackConfigRechargeable_Type = TruthValue
_TlpUpsBatteryPackConfigRechargeable_Object = MibTableColumn
tlpUpsBatteryPackConfigRechargeable = _TlpUpsBatteryPackConfigRechargeable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 4, 1, 13),
    _TlpUpsBatteryPackConfigRechargeable_Type()
)
tlpUpsBatteryPackConfigRechargeable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryPackConfigRechargeable.setStatus("current")
_TlpUpsBatteryPackConfigFullChargeCapacity_Type = Unsigned32
_TlpUpsBatteryPackConfigFullChargeCapacity_Object = MibTableColumn
tlpUpsBatteryPackConfigFullChargeCapacity = _TlpUpsBatteryPackConfigFullChargeCapacity_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 4, 1, 14),
    _TlpUpsBatteryPackConfigFullChargeCapacity_Type()
)
tlpUpsBatteryPackConfigFullChargeCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryPackConfigFullChargeCapacity.setStatus("current")
_TlpUpsBatteryPackDetailTable_Object = MibTable
tlpUpsBatteryPackDetailTable = _TlpUpsBatteryPackDetailTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 5)
)
if mibBuilder.loadTexts:
    tlpUpsBatteryPackDetailTable.setStatus("current")
_TlpUpsBatteryPackDetailEntry_Object = MibTableRow
tlpUpsBatteryPackDetailEntry = _TlpUpsBatteryPackDetailEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 5, 1)
)
tlpUpsBatteryPackDetailEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpUpsBatteryPackIdentIndex"),
)
if mibBuilder.loadTexts:
    tlpUpsBatteryPackDetailEntry.setStatus("current")


class _TlpUpsBatteryPackDetailCondition_Type(Integer32):
    """Custom type tlpUpsBatteryPackDetailCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("good", 1),
          ("weak", 2),
          ("bad", 3))
    )


_TlpUpsBatteryPackDetailCondition_Type.__name__ = "Integer32"
_TlpUpsBatteryPackDetailCondition_Object = MibTableColumn
tlpUpsBatteryPackDetailCondition = _TlpUpsBatteryPackDetailCondition_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 5, 1, 1),
    _TlpUpsBatteryPackDetailCondition_Type()
)
tlpUpsBatteryPackDetailCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryPackDetailCondition.setStatus("current")
_TlpUpsBatteryPackDetailTemperatureC_Type = Unsigned32
_TlpUpsBatteryPackDetailTemperatureC_Object = MibTableColumn
tlpUpsBatteryPackDetailTemperatureC = _TlpUpsBatteryPackDetailTemperatureC_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 5, 1, 2),
    _TlpUpsBatteryPackDetailTemperatureC_Type()
)
tlpUpsBatteryPackDetailTemperatureC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryPackDetailTemperatureC.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsBatteryPackDetailTemperatureC.setUnits("0.1 degrees Celsius")
_TlpUpsBatteryPackDetailTemperatureF_Type = Unsigned32
_TlpUpsBatteryPackDetailTemperatureF_Object = MibTableColumn
tlpUpsBatteryPackDetailTemperatureF = _TlpUpsBatteryPackDetailTemperatureF_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 5, 1, 3),
    _TlpUpsBatteryPackDetailTemperatureF_Type()
)
tlpUpsBatteryPackDetailTemperatureF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryPackDetailTemperatureF.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsBatteryPackDetailTemperatureF.setUnits("0.1 degrees Fahrenheit")
_TlpUpsBatteryPackDetailAge_Type = Unsigned32
_TlpUpsBatteryPackDetailAge_Object = MibTableColumn
tlpUpsBatteryPackDetailAge = _TlpUpsBatteryPackDetailAge_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 5, 1, 4),
    _TlpUpsBatteryPackDetailAge_Type()
)
tlpUpsBatteryPackDetailAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryPackDetailAge.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsBatteryPackDetailAge.setUnits("0.1 Years")
_TlpUpsBatteryPackDetailLastReplaceDate_Type = DisplayString
_TlpUpsBatteryPackDetailLastReplaceDate_Object = MibTableColumn
tlpUpsBatteryPackDetailLastReplaceDate = _TlpUpsBatteryPackDetailLastReplaceDate_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 5, 1, 5),
    _TlpUpsBatteryPackDetailLastReplaceDate_Type()
)
tlpUpsBatteryPackDetailLastReplaceDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsBatteryPackDetailLastReplaceDate.setStatus("current")
_TlpUpsBatteryPackDetailNextReplaceDate_Type = DisplayString
_TlpUpsBatteryPackDetailNextReplaceDate_Object = MibTableColumn
tlpUpsBatteryPackDetailNextReplaceDate = _TlpUpsBatteryPackDetailNextReplaceDate_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 5, 1, 6),
    _TlpUpsBatteryPackDetailNextReplaceDate_Type()
)
tlpUpsBatteryPackDetailNextReplaceDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryPackDetailNextReplaceDate.setStatus("current")
_TlpUpsBatteryPackDetailCycleCount_Type = Unsigned32
_TlpUpsBatteryPackDetailCycleCount_Object = MibTableColumn
tlpUpsBatteryPackDetailCycleCount = _TlpUpsBatteryPackDetailCycleCount_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 5, 1, 7),
    _TlpUpsBatteryPackDetailCycleCount_Type()
)
tlpUpsBatteryPackDetailCycleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryPackDetailCycleCount.setStatus("current")
_TlpUpsInput_ObjectIdentity = ObjectIdentity
tlpUpsInput = _TlpUpsInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 2)
)
_TlpUpsInputTable_Object = MibTable
tlpUpsInputTable = _TlpUpsInputTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    tlpUpsInputTable.setStatus("current")
_TlpUpsInputEntry_Object = MibTableRow
tlpUpsInputEntry = _TlpUpsInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 2, 1, 1)
)
tlpUpsInputEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpUpsInputEntry.setStatus("current")
_TlpUpsInputLineBads_Type = Integer32
_TlpUpsInputLineBads_Object = MibTableColumn
tlpUpsInputLineBads = _TlpUpsInputLineBads_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 2, 1, 1, 1),
    _TlpUpsInputLineBads_Type()
)
tlpUpsInputLineBads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsInputLineBads.setStatus("current")
_TlpUpsInputNominalVoltage_Type = Unsigned32
_TlpUpsInputNominalVoltage_Object = MibTableColumn
tlpUpsInputNominalVoltage = _TlpUpsInputNominalVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 2, 1, 1, 2),
    _TlpUpsInputNominalVoltage_Type()
)
tlpUpsInputNominalVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsInputNominalVoltage.setStatus("current")
_TlpUpsInputNominalFrequency_Type = Unsigned32
_TlpUpsInputNominalFrequency_Object = MibTableColumn
tlpUpsInputNominalFrequency = _TlpUpsInputNominalFrequency_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 2, 1, 1, 3),
    _TlpUpsInputNominalFrequency_Type()
)
tlpUpsInputNominalFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsInputNominalFrequency.setStatus("current")
_TlpUpsInputLowTransferVoltage_Type = Unsigned32
_TlpUpsInputLowTransferVoltage_Object = MibTableColumn
tlpUpsInputLowTransferVoltage = _TlpUpsInputLowTransferVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 2, 1, 1, 4),
    _TlpUpsInputLowTransferVoltage_Type()
)
tlpUpsInputLowTransferVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsInputLowTransferVoltage.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsInputLowTransferVoltage.setUnits("0.1 Volts")
_TlpUpsInputLowTransferVoltageLowerBound_Type = Unsigned32
_TlpUpsInputLowTransferVoltageLowerBound_Object = MibTableColumn
tlpUpsInputLowTransferVoltageLowerBound = _TlpUpsInputLowTransferVoltageLowerBound_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 2, 1, 1, 5),
    _TlpUpsInputLowTransferVoltageLowerBound_Type()
)
tlpUpsInputLowTransferVoltageLowerBound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsInputLowTransferVoltageLowerBound.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsInputLowTransferVoltageLowerBound.setUnits("0.1 Volts")
_TlpUpsInputLowTransferVoltageUpperBound_Type = Unsigned32
_TlpUpsInputLowTransferVoltageUpperBound_Object = MibTableColumn
tlpUpsInputLowTransferVoltageUpperBound = _TlpUpsInputLowTransferVoltageUpperBound_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 2, 1, 1, 6),
    _TlpUpsInputLowTransferVoltageUpperBound_Type()
)
tlpUpsInputLowTransferVoltageUpperBound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsInputLowTransferVoltageUpperBound.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsInputLowTransferVoltageUpperBound.setUnits("0.1 Volts")
_TlpUpsInputHighTransferVoltage_Type = Unsigned32
_TlpUpsInputHighTransferVoltage_Object = MibTableColumn
tlpUpsInputHighTransferVoltage = _TlpUpsInputHighTransferVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 2, 1, 1, 7),
    _TlpUpsInputHighTransferVoltage_Type()
)
tlpUpsInputHighTransferVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsInputHighTransferVoltage.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsInputHighTransferVoltage.setUnits("0.1 Volts")
_TlpUpsInputHighTransferVoltageLowerBound_Type = Unsigned32
_TlpUpsInputHighTransferVoltageLowerBound_Object = MibTableColumn
tlpUpsInputHighTransferVoltageLowerBound = _TlpUpsInputHighTransferVoltageLowerBound_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 2, 1, 1, 8),
    _TlpUpsInputHighTransferVoltageLowerBound_Type()
)
tlpUpsInputHighTransferVoltageLowerBound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsInputHighTransferVoltageLowerBound.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsInputHighTransferVoltageLowerBound.setUnits("0.1 Volts")
_TlpUpsInputHighTransferVoltageUpperBound_Type = Unsigned32
_TlpUpsInputHighTransferVoltageUpperBound_Object = MibTableColumn
tlpUpsInputHighTransferVoltageUpperBound = _TlpUpsInputHighTransferVoltageUpperBound_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 2, 1, 1, 9),
    _TlpUpsInputHighTransferVoltageUpperBound_Type()
)
tlpUpsInputHighTransferVoltageUpperBound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsInputHighTransferVoltageUpperBound.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsInputHighTransferVoltageUpperBound.setUnits("0.1 Volts")
_TlpUpsInputCurrentTotal_Type = Unsigned32
_TlpUpsInputCurrentTotal_Object = MibTableColumn
tlpUpsInputCurrentTotal = _TlpUpsInputCurrentTotal_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 2, 1, 1, 10),
    _TlpUpsInputCurrentTotal_Type()
)
tlpUpsInputCurrentTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsInputCurrentTotal.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsInputCurrentTotal.setUnits("0.01 Amps")
_TlpUpsInputLowTransferVoltageResetTolerance_Type = Unsigned32
_TlpUpsInputLowTransferVoltageResetTolerance_Object = MibTableColumn
tlpUpsInputLowTransferVoltageResetTolerance = _TlpUpsInputLowTransferVoltageResetTolerance_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 2, 1, 1, 11),
    _TlpUpsInputLowTransferVoltageResetTolerance_Type()
)
tlpUpsInputLowTransferVoltageResetTolerance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsInputLowTransferVoltageResetTolerance.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsInputLowTransferVoltageResetTolerance.setUnits("Volts")
_TlpUpsInputHighTransferVoltageResetTolerance_Type = Unsigned32
_TlpUpsInputHighTransferVoltageResetTolerance_Object = MibTableColumn
tlpUpsInputHighTransferVoltageResetTolerance = _TlpUpsInputHighTransferVoltageResetTolerance_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 2, 1, 1, 12),
    _TlpUpsInputHighTransferVoltageResetTolerance_Type()
)
tlpUpsInputHighTransferVoltageResetTolerance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsInputHighTransferVoltageResetTolerance.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsInputHighTransferVoltageResetTolerance.setUnits("Volts")


class _TlpUpsInputTransformerStatus_Type(Integer32):
    """Custom type tlpUpsInputTransformerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("reducing", 1),
          ("boosting", 2))
    )


_TlpUpsInputTransformerStatus_Type.__name__ = "Integer32"
_TlpUpsInputTransformerStatus_Object = MibTableColumn
tlpUpsInputTransformerStatus = _TlpUpsInputTransformerStatus_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 2, 1, 1, 13),
    _TlpUpsInputTransformerStatus_Type()
)
tlpUpsInputTransformerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsInputTransformerStatus.setStatus("current")
_TlpUpsInputAvrTransitionCount_Type = Unsigned32
_TlpUpsInputAvrTransitionCount_Object = MibTableColumn
tlpUpsInputAvrTransitionCount = _TlpUpsInputAvrTransitionCount_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 2, 1, 1, 14),
    _TlpUpsInputAvrTransitionCount_Type()
)
tlpUpsInputAvrTransitionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsInputAvrTransitionCount.setStatus("current")


class _TlpUpsInputSource_Type(Integer32):
    """Custom type tlpUpsInputSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("utility", 0),
          ("battery", 1),
          ("other", 2),
          ("none", 3),
          ("testing", 4))
    )


_TlpUpsInputSource_Type.__name__ = "Integer32"
_TlpUpsInputSource_Object = MibTableColumn
tlpUpsInputSource = _TlpUpsInputSource_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 2, 1, 1, 15),
    _TlpUpsInputSource_Type()
)
tlpUpsInputSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsInputSource.setStatus("current")
_TlpUpsInputPhaseTable_Object = MibTable
tlpUpsInputPhaseTable = _TlpUpsInputPhaseTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 2, 2)
)
if mibBuilder.loadTexts:
    tlpUpsInputPhaseTable.setStatus("current")
_TlpUpsInputPhaseEntry_Object = MibTableRow
tlpUpsInputPhaseEntry = _TlpUpsInputPhaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 2, 2, 1)
)
tlpUpsInputPhaseEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpUpsInputPhaseIndex"),
)
if mibBuilder.loadTexts:
    tlpUpsInputPhaseEntry.setStatus("current")
_TlpUpsInputPhaseIndex_Type = Unsigned32
_TlpUpsInputPhaseIndex_Object = MibTableColumn
tlpUpsInputPhaseIndex = _TlpUpsInputPhaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 2, 2, 1, 1),
    _TlpUpsInputPhaseIndex_Type()
)
tlpUpsInputPhaseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsInputPhaseIndex.setStatus("current")
_TlpUpsInputPhaseFrequency_Type = Unsigned32
_TlpUpsInputPhaseFrequency_Object = MibTableColumn
tlpUpsInputPhaseFrequency = _TlpUpsInputPhaseFrequency_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 2, 2, 1, 2),
    _TlpUpsInputPhaseFrequency_Type()
)
tlpUpsInputPhaseFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsInputPhaseFrequency.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsInputPhaseFrequency.setUnits("0.1 Hertz")
_TlpUpsInputPhaseVoltage_Type = Unsigned32
_TlpUpsInputPhaseVoltage_Object = MibTableColumn
tlpUpsInputPhaseVoltage = _TlpUpsInputPhaseVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 2, 2, 1, 3),
    _TlpUpsInputPhaseVoltage_Type()
)
tlpUpsInputPhaseVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsInputPhaseVoltage.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsInputPhaseVoltage.setUnits("0.1 Volts")
_TlpUpsInputPhaseVoltageMin_Type = Unsigned32
_TlpUpsInputPhaseVoltageMin_Object = MibTableColumn
tlpUpsInputPhaseVoltageMin = _TlpUpsInputPhaseVoltageMin_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 2, 2, 1, 4),
    _TlpUpsInputPhaseVoltageMin_Type()
)
tlpUpsInputPhaseVoltageMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsInputPhaseVoltageMin.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsInputPhaseVoltageMin.setUnits("0.1 Volts")
_TlpUpsInputPhaseVoltageMax_Type = Unsigned32
_TlpUpsInputPhaseVoltageMax_Object = MibTableColumn
tlpUpsInputPhaseVoltageMax = _TlpUpsInputPhaseVoltageMax_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 2, 2, 1, 5),
    _TlpUpsInputPhaseVoltageMax_Type()
)
tlpUpsInputPhaseVoltageMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsInputPhaseVoltageMax.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsInputPhaseVoltageMax.setUnits("0.1 Volts")
_TlpUpsInputPhaseCurrent_Type = Unsigned32
_TlpUpsInputPhaseCurrent_Object = MibTableColumn
tlpUpsInputPhaseCurrent = _TlpUpsInputPhaseCurrent_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 2, 2, 1, 6),
    _TlpUpsInputPhaseCurrent_Type()
)
tlpUpsInputPhaseCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsInputPhaseCurrent.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsInputPhaseCurrent.setUnits("0.01 Amps")
_TlpUpsInputPhasePower_Type = Unsigned32
_TlpUpsInputPhasePower_Object = MibTableColumn
tlpUpsInputPhasePower = _TlpUpsInputPhasePower_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 2, 2, 1, 7),
    _TlpUpsInputPhasePower_Type()
)
tlpUpsInputPhasePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsInputPhasePower.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsInputPhasePower.setUnits("Watts")
_TlpUpsOutput_ObjectIdentity = ObjectIdentity
tlpUpsOutput = _TlpUpsOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 3)
)
_TlpUpsOutputTable_Object = MibTable
tlpUpsOutputTable = _TlpUpsOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    tlpUpsOutputTable.setStatus("current")
_TlpUpsOutputEntry_Object = MibTableRow
tlpUpsOutputEntry = _TlpUpsOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 3, 1, 1)
)
tlpUpsOutputEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpUpsOutputEntry.setStatus("current")


class _TlpUpsOutputSource_Type(Integer32):
    """Custom type tlpUpsOutputSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("other", 1),
          ("none", 2),
          ("normal", 3),
          ("bypass", 4),
          ("battery", 5),
          ("boosting", 6),
          ("reducing", 7),
          ("second", 8),
          ("economy", 9),
          ("testing", 10))
    )


_TlpUpsOutputSource_Type.__name__ = "Integer32"
_TlpUpsOutputSource_Object = MibTableColumn
tlpUpsOutputSource = _TlpUpsOutputSource_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 3, 1, 1, 1),
    _TlpUpsOutputSource_Type()
)
tlpUpsOutputSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsOutputSource.setStatus("current")
_TlpUpsOutputNominalVoltage_Type = Unsigned32
_TlpUpsOutputNominalVoltage_Object = MibTableColumn
tlpUpsOutputNominalVoltage = _TlpUpsOutputNominalVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 3, 1, 1, 2),
    _TlpUpsOutputNominalVoltage_Type()
)
tlpUpsOutputNominalVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsOutputNominalVoltage.setStatus("current")
_TlpUpsOutputFrequency_Type = Unsigned32
_TlpUpsOutputFrequency_Object = MibTableColumn
tlpUpsOutputFrequency = _TlpUpsOutputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 3, 1, 1, 3),
    _TlpUpsOutputFrequency_Type()
)
tlpUpsOutputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsOutputFrequency.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsOutputFrequency.setUnits("0.1 Hertz")
_TlpUpsOutputVARating_Type = Unsigned32
_TlpUpsOutputVARating_Object = MibTableColumn
tlpUpsOutputVARating = _TlpUpsOutputVARating_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 3, 1, 1, 4),
    _TlpUpsOutputVARating_Type()
)
tlpUpsOutputVARating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsOutputVARating.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsOutputVARating.setUnits("VA")
_TlpUpsOutputPowerFactor_Type = Unsigned32
_TlpUpsOutputPowerFactor_Object = MibTableColumn
tlpUpsOutputPowerFactor = _TlpUpsOutputPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 3, 1, 1, 5),
    _TlpUpsOutputPowerFactor_Type()
)
tlpUpsOutputPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsOutputPowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsOutputPowerFactor.setUnits("percent")
_TlpUpsOutputTotalUtilization_Type = Integer32
_TlpUpsOutputTotalUtilization_Object = MibTableColumn
tlpUpsOutputTotalUtilization = _TlpUpsOutputTotalUtilization_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 3, 1, 1, 6),
    _TlpUpsOutputTotalUtilization_Type()
)
tlpUpsOutputTotalUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsOutputTotalUtilization.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsOutputTotalUtilization.setUnits("0.01 percent")
_TlpUpsOutputPowerRating_Type = Unsigned32
_TlpUpsOutputPowerRating_Object = MibTableColumn
tlpUpsOutputPowerRating = _TlpUpsOutputPowerRating_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 3, 1, 1, 7),
    _TlpUpsOutputPowerRating_Type()
)
tlpUpsOutputPowerRating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsOutputPowerRating.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsOutputPowerRating.setUnits("Watts")
_TlpUpsOutputChargerCurrent_Type = Unsigned32
_TlpUpsOutputChargerCurrent_Object = MibTableColumn
tlpUpsOutputChargerCurrent = _TlpUpsOutputChargerCurrent_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 3, 1, 1, 8),
    _TlpUpsOutputChargerCurrent_Type()
)
tlpUpsOutputChargerCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsOutputChargerCurrent.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsOutputChargerCurrent.setUnits("0.1 Amps")
_TlpUpsOutputCurrentRating_Type = Unsigned32
_TlpUpsOutputCurrentRating_Object = MibTableColumn
tlpUpsOutputCurrentRating = _TlpUpsOutputCurrentRating_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 3, 1, 1, 9),
    _TlpUpsOutputCurrentRating_Type()
)
tlpUpsOutputCurrentRating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsOutputCurrentRating.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsOutputCurrentRating.setUnits("Amps")
_TlpUpsOutputEfficiency_Type = Integer32
_TlpUpsOutputEfficiency_Object = MibTableColumn
tlpUpsOutputEfficiency = _TlpUpsOutputEfficiency_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 3, 1, 1, 10),
    _TlpUpsOutputEfficiency_Type()
)
tlpUpsOutputEfficiency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsOutputEfficiency.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsOutputEfficiency.setUnits("percent")
_TlpUpsOutputLineTable_Object = MibTable
tlpUpsOutputLineTable = _TlpUpsOutputLineTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 3, 2)
)
if mibBuilder.loadTexts:
    tlpUpsOutputLineTable.setStatus("current")
_TlpUpsOutputLineEntry_Object = MibTableRow
tlpUpsOutputLineEntry = _TlpUpsOutputLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 3, 2, 1)
)
tlpUpsOutputLineEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpUpsOutputLineIndex"),
)
if mibBuilder.loadTexts:
    tlpUpsOutputLineEntry.setStatus("current")
_TlpUpsOutputLineIndex_Type = Unsigned32
_TlpUpsOutputLineIndex_Object = MibTableColumn
tlpUpsOutputLineIndex = _TlpUpsOutputLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 3, 2, 1, 1),
    _TlpUpsOutputLineIndex_Type()
)
tlpUpsOutputLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsOutputLineIndex.setStatus("current")
_TlpUpsOutputLineVoltage_Type = Unsigned32
_TlpUpsOutputLineVoltage_Object = MibTableColumn
tlpUpsOutputLineVoltage = _TlpUpsOutputLineVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 3, 2, 1, 2),
    _TlpUpsOutputLineVoltage_Type()
)
tlpUpsOutputLineVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsOutputLineVoltage.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsOutputLineVoltage.setUnits("0.1 Volts")
_TlpUpsOutputLineCurrent_Type = Unsigned32
_TlpUpsOutputLineCurrent_Object = MibTableColumn
tlpUpsOutputLineCurrent = _TlpUpsOutputLineCurrent_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 3, 2, 1, 3),
    _TlpUpsOutputLineCurrent_Type()
)
tlpUpsOutputLineCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsOutputLineCurrent.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsOutputLineCurrent.setUnits("0.01 Amps")
_TlpUpsOutputLineActivePower_Type = Unsigned32
_TlpUpsOutputLineActivePower_Object = MibTableColumn
tlpUpsOutputLineActivePower = _TlpUpsOutputLineActivePower_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 3, 2, 1, 4),
    _TlpUpsOutputLineActivePower_Type()
)
tlpUpsOutputLineActivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsOutputLineActivePower.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsOutputLineActivePower.setUnits("Watts")


class _TlpUpsOutputLineUtilization_Type(Integer32):
    """Custom type tlpUpsOutputLineUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_TlpUpsOutputLineUtilization_Type.__name__ = "Integer32"
_TlpUpsOutputLineUtilization_Object = MibTableColumn
tlpUpsOutputLineUtilization = _TlpUpsOutputLineUtilization_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 3, 2, 1, 5),
    _TlpUpsOutputLineUtilization_Type()
)
tlpUpsOutputLineUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsOutputLineUtilization.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsOutputLineUtilization.setUnits("percent")
_TlpUpsOutputLineFrequency_Type = Unsigned32
_TlpUpsOutputLineFrequency_Object = MibTableColumn
tlpUpsOutputLineFrequency = _TlpUpsOutputLineFrequency_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 3, 2, 1, 6),
    _TlpUpsOutputLineFrequency_Type()
)
tlpUpsOutputLineFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsOutputLineFrequency.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsOutputLineFrequency.setUnits("0.1 Hertz")
_TlpUpsOutputLineCurrentMin_Type = Unsigned32
_TlpUpsOutputLineCurrentMin_Object = MibTableColumn
tlpUpsOutputLineCurrentMin = _TlpUpsOutputLineCurrentMin_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 3, 2, 1, 7),
    _TlpUpsOutputLineCurrentMin_Type()
)
tlpUpsOutputLineCurrentMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsOutputLineCurrentMin.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsOutputLineCurrentMin.setUnits("0.01 Amps")
_TlpUpsOutputLineCurrentMax_Type = Unsigned32
_TlpUpsOutputLineCurrentMax_Object = MibTableColumn
tlpUpsOutputLineCurrentMax = _TlpUpsOutputLineCurrentMax_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 3, 2, 1, 8),
    _TlpUpsOutputLineCurrentMax_Type()
)
tlpUpsOutputLineCurrentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsOutputLineCurrentMax.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsOutputLineCurrentMax.setUnits("0.01 Amps")
_TlpUpsOutputLineApparentPower_Type = Unsigned32
_TlpUpsOutputLineApparentPower_Object = MibTableColumn
tlpUpsOutputLineApparentPower = _TlpUpsOutputLineApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 3, 2, 1, 9),
    _TlpUpsOutputLineApparentPower_Type()
)
tlpUpsOutputLineApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsOutputLineApparentPower.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsOutputLineApparentPower.setUnits("Watts")
_TlpUpsOutputLinePowerKVA_Type = Unsigned32
_TlpUpsOutputLinePowerKVA_Object = MibTableColumn
tlpUpsOutputLinePowerKVA = _TlpUpsOutputLinePowerKVA_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 3, 2, 1, 10),
    _TlpUpsOutputLinePowerKVA_Type()
)
tlpUpsOutputLinePowerKVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsOutputLinePowerKVA.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsOutputLinePowerKVA.setUnits("0.01 KVA")
_TlpUpsOutputLinePowerKW_Type = Unsigned32
_TlpUpsOutputLinePowerKW_Object = MibTableColumn
tlpUpsOutputLinePowerKW = _TlpUpsOutputLinePowerKW_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 3, 2, 1, 11),
    _TlpUpsOutputLinePowerKW_Type()
)
tlpUpsOutputLinePowerKW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsOutputLinePowerKW.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsOutputLinePowerKW.setUnits("0.01 KW")
_TlpUpsOutputLine24hrEnergy_Type = Unsigned32
_TlpUpsOutputLine24hrEnergy_Object = MibTableColumn
tlpUpsOutputLine24hrEnergy = _TlpUpsOutputLine24hrEnergy_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 3, 2, 1, 12),
    _TlpUpsOutputLine24hrEnergy_Type()
)
tlpUpsOutputLine24hrEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsOutputLine24hrEnergy.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsOutputLine24hrEnergy.setUnits("0.01 KWH")
_TlpUpsOutputLineWattHours_Type = Unsigned32
_TlpUpsOutputLineWattHours_Object = MibTableColumn
tlpUpsOutputLineWattHours = _TlpUpsOutputLineWattHours_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 3, 2, 1, 13),
    _TlpUpsOutputLineWattHours_Type()
)
tlpUpsOutputLineWattHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsOutputLineWattHours.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsOutputLineWattHours.setUnits("WH")
_TlpUpsOutputLinePeakPower_Type = Unsigned32
_TlpUpsOutputLinePeakPower_Object = MibTableColumn
tlpUpsOutputLinePeakPower = _TlpUpsOutputLinePeakPower_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 3, 2, 1, 14),
    _TlpUpsOutputLinePeakPower_Type()
)
tlpUpsOutputLinePeakPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsOutputLinePeakPower.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsOutputLinePeakPower.setUnits("Watts")
_TlpUpsBypass_ObjectIdentity = ObjectIdentity
tlpUpsBypass = _TlpUpsBypass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 4)
)
_TlpUpsBypassTable_Object = MibTable
tlpUpsBypassTable = _TlpUpsBypassTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 4, 1)
)
if mibBuilder.loadTexts:
    tlpUpsBypassTable.setStatus("current")
_TlpUpsBypassEntry_Object = MibTableRow
tlpUpsBypassEntry = _TlpUpsBypassEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 4, 1, 1)
)
tlpUpsBypassEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpUpsBypassEntry.setStatus("current")
_TlpUpsBypassFrequency_Type = Unsigned32
_TlpUpsBypassFrequency_Object = MibTableColumn
tlpUpsBypassFrequency = _TlpUpsBypassFrequency_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 4, 1, 1, 1),
    _TlpUpsBypassFrequency_Type()
)
tlpUpsBypassFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBypassFrequency.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsBypassFrequency.setUnits("0.1 Hertz")
_TlpUpsBypassNominalFrequency_Type = Unsigned32
_TlpUpsBypassNominalFrequency_Object = MibTableColumn
tlpUpsBypassNominalFrequency = _TlpUpsBypassNominalFrequency_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 4, 1, 1, 2),
    _TlpUpsBypassNominalFrequency_Type()
)
tlpUpsBypassNominalFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBypassNominalFrequency.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsBypassNominalFrequency.setUnits("0.1 Hertz")
_TlpUpsBypassLineTable_Object = MibTable
tlpUpsBypassLineTable = _TlpUpsBypassLineTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 4, 2)
)
if mibBuilder.loadTexts:
    tlpUpsBypassLineTable.setStatus("current")
_TlpUpsBypassLineEntry_Object = MibTableRow
tlpUpsBypassLineEntry = _TlpUpsBypassLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 4, 2, 1)
)
tlpUpsBypassLineEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpUpsBypassLineIndex"),
)
if mibBuilder.loadTexts:
    tlpUpsBypassLineEntry.setStatus("current")
_TlpUpsBypassLineIndex_Type = Unsigned32
_TlpUpsBypassLineIndex_Object = MibTableColumn
tlpUpsBypassLineIndex = _TlpUpsBypassLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 4, 2, 1, 1),
    _TlpUpsBypassLineIndex_Type()
)
tlpUpsBypassLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBypassLineIndex.setStatus("current")
_TlpUpsBypassLineVoltage_Type = Unsigned32
_TlpUpsBypassLineVoltage_Object = MibTableColumn
tlpUpsBypassLineVoltage = _TlpUpsBypassLineVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 4, 2, 1, 2),
    _TlpUpsBypassLineVoltage_Type()
)
tlpUpsBypassLineVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBypassLineVoltage.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsBypassLineVoltage.setUnits("0.1 Volts")
_TlpUpsBypassLineCurrent_Type = Unsigned32
_TlpUpsBypassLineCurrent_Object = MibTableColumn
tlpUpsBypassLineCurrent = _TlpUpsBypassLineCurrent_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 4, 2, 1, 3),
    _TlpUpsBypassLineCurrent_Type()
)
tlpUpsBypassLineCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBypassLineCurrent.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsBypassLineCurrent.setUnits("0.1 Amps")
_TlpUpsBypassLinePower_Type = Unsigned32
_TlpUpsBypassLinePower_Object = MibTableColumn
tlpUpsBypassLinePower = _TlpUpsBypassLinePower_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 4, 2, 1, 4),
    _TlpUpsBypassLinePower_Type()
)
tlpUpsBypassLinePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBypassLinePower.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsBypassLinePower.setUnits("Watts")
_TlpUpsOutlet_ObjectIdentity = ObjectIdentity
tlpUpsOutlet = _TlpUpsOutlet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 5)
)
_TlpUpsOutletTable_Object = MibTable
tlpUpsOutletTable = _TlpUpsOutletTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 5, 1)
)
if mibBuilder.loadTexts:
    tlpUpsOutletTable.setStatus("current")
_TlpUpsOutletEntry_Object = MibTableRow
tlpUpsOutletEntry = _TlpUpsOutletEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 5, 1, 1)
)
tlpUpsOutletEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpUpsOutletIndex"),
)
if mibBuilder.loadTexts:
    tlpUpsOutletEntry.setStatus("current")
_TlpUpsOutletIndex_Type = Unsigned32
_TlpUpsOutletIndex_Object = MibTableColumn
tlpUpsOutletIndex = _TlpUpsOutletIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 5, 1, 1, 1),
    _TlpUpsOutletIndex_Type()
)
tlpUpsOutletIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsOutletIndex.setStatus("current")
_TlpUpsOutletName_Type = DisplayString
_TlpUpsOutletName_Object = MibTableColumn
tlpUpsOutletName = _TlpUpsOutletName_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 5, 1, 1, 2),
    _TlpUpsOutletName_Type()
)
tlpUpsOutletName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsOutletName.setStatus("current")
_TlpUpsOutletDescription_Type = DisplayString
_TlpUpsOutletDescription_Object = MibTableColumn
tlpUpsOutletDescription = _TlpUpsOutletDescription_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 5, 1, 1, 3),
    _TlpUpsOutletDescription_Type()
)
tlpUpsOutletDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsOutletDescription.setStatus("current")


class _TlpUpsOutletState_Type(Integer32):
    """Custom type tlpUpsOutletState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("off", 1),
          ("on", 2))
    )


_TlpUpsOutletState_Type.__name__ = "Integer32"
_TlpUpsOutletState_Object = MibTableColumn
tlpUpsOutletState = _TlpUpsOutletState_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 5, 1, 1, 4),
    _TlpUpsOutletState_Type()
)
tlpUpsOutletState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsOutletState.setStatus("current")
_TlpUpsOutletControllable_Type = TruthValue
_TlpUpsOutletControllable_Object = MibTableColumn
tlpUpsOutletControllable = _TlpUpsOutletControllable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 5, 1, 1, 5),
    _TlpUpsOutletControllable_Type()
)
tlpUpsOutletControllable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsOutletControllable.setStatus("current")


class _TlpUpsOutletCommand_Type(Integer32):
    """Custom type tlpUpsOutletCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("turnOff", 1),
          ("turnOn", 2),
          ("cycle", 3))
    )


_TlpUpsOutletCommand_Type.__name__ = "Integer32"
_TlpUpsOutletCommand_Object = MibTableColumn
tlpUpsOutletCommand = _TlpUpsOutletCommand_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 5, 1, 1, 6),
    _TlpUpsOutletCommand_Type()
)
tlpUpsOutletCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsOutletCommand.setStatus("current")
_TlpUpsOutletVoltage_Type = Unsigned32
_TlpUpsOutletVoltage_Object = MibTableColumn
tlpUpsOutletVoltage = _TlpUpsOutletVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 5, 1, 1, 7),
    _TlpUpsOutletVoltage_Type()
)
tlpUpsOutletVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsOutletVoltage.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsOutletVoltage.setUnits("0.1 Volts")
_TlpUpsOutletCurrent_Type = Unsigned32
_TlpUpsOutletCurrent_Object = MibTableColumn
tlpUpsOutletCurrent = _TlpUpsOutletCurrent_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 5, 1, 1, 8),
    _TlpUpsOutletCurrent_Type()
)
tlpUpsOutletCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsOutletCurrent.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsOutletCurrent.setUnits("0.01 Amps")
_TlpUpsOutletActivePower_Type = Unsigned32
_TlpUpsOutletActivePower_Object = MibTableColumn
tlpUpsOutletActivePower = _TlpUpsOutletActivePower_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 5, 1, 1, 9),
    _TlpUpsOutletActivePower_Type()
)
tlpUpsOutletActivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsOutletActivePower.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsOutletActivePower.setUnits("Watts")


class _TlpUpsOutletRampAction_Type(Integer32):
    """Custom type tlpUpsOutletRampAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("remainOff", 0),
          ("turnOnAfterDelay", 1))
    )


_TlpUpsOutletRampAction_Type.__name__ = "Integer32"
_TlpUpsOutletRampAction_Object = MibTableColumn
tlpUpsOutletRampAction = _TlpUpsOutletRampAction_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 5, 1, 1, 10),
    _TlpUpsOutletRampAction_Type()
)
tlpUpsOutletRampAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsOutletRampAction.setStatus("current")
_TlpUpsOutletRampDelay_Type = Integer32
_TlpUpsOutletRampDelay_Object = MibTableColumn
tlpUpsOutletRampDelay = _TlpUpsOutletRampDelay_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 5, 1, 1, 11),
    _TlpUpsOutletRampDelay_Type()
)
tlpUpsOutletRampDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsOutletRampDelay.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsOutletRampDelay.setUnits("seconds")


class _TlpUpsOutletShedAction_Type(Integer32):
    """Custom type tlpUpsOutletShedAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("remainOn", 0),
          ("turnOffAfterDelay", 1))
    )


_TlpUpsOutletShedAction_Type.__name__ = "Integer32"
_TlpUpsOutletShedAction_Object = MibTableColumn
tlpUpsOutletShedAction = _TlpUpsOutletShedAction_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 5, 1, 1, 12),
    _TlpUpsOutletShedAction_Type()
)
tlpUpsOutletShedAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsOutletShedAction.setStatus("current")
_TlpUpsOutletShedDelay_Type = Integer32
_TlpUpsOutletShedDelay_Object = MibTableColumn
tlpUpsOutletShedDelay = _TlpUpsOutletShedDelay_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 5, 1, 1, 13),
    _TlpUpsOutletShedDelay_Type()
)
tlpUpsOutletShedDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsOutletShedDelay.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsOutletShedDelay.setUnits("seconds")
_TlpUpsOutletGroup_Type = Integer32
_TlpUpsOutletGroup_Object = MibTableColumn
tlpUpsOutletGroup = _TlpUpsOutletGroup_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 5, 1, 1, 14),
    _TlpUpsOutletGroup_Type()
)
tlpUpsOutletGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsOutletGroup.setStatus("current")
_TlpUpsOutletBank_Type = Integer32
_TlpUpsOutletBank_Object = MibTableColumn
tlpUpsOutletBank = _TlpUpsOutletBank_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 5, 1, 1, 15),
    _TlpUpsOutletBank_Type()
)
tlpUpsOutletBank.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsOutletBank.setStatus("deprecated")
_TlpUpsOutletCircuit_Type = Integer32
_TlpUpsOutletCircuit_Object = MibTableColumn
tlpUpsOutletCircuit = _TlpUpsOutletCircuit_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 5, 1, 1, 16),
    _TlpUpsOutletCircuit_Type()
)
tlpUpsOutletCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsOutletCircuit.setStatus("current")


class _TlpUpsOutletPhase_Type(Integer32):
    """Custom type tlpUpsOutletPhase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("phase1", 1),
          ("phase2", 2),
          ("phase3", 3),
          ("phase1-2", 4),
          ("phase2-3", 5),
          ("phase3-1", 6))
    )


_TlpUpsOutletPhase_Type.__name__ = "Integer32"
_TlpUpsOutletPhase_Object = MibTableColumn
tlpUpsOutletPhase = _TlpUpsOutletPhase_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 5, 1, 1, 17),
    _TlpUpsOutletPhase_Type()
)
tlpUpsOutletPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsOutletPhase.setStatus("current")


class _TlpUpsOutletReceptacleType_Type(Integer32):
    """Custom type tlpUpsOutletReceptacleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("nema-515R", 1),
          ("nema-520R", 2),
          ("nema-530R", 3),
          ("nema-L515R", 4),
          ("nema-L520R", 5),
          ("nema-L530R", 6),
          ("nema-L615R", 7),
          ("nema-L620R", 8),
          ("nema-L630R", 9),
          ("nema-L1430R", 10),
          ("nema-L1520R", 11),
          ("nema-L1530R", 12),
          ("nema-L2120R", 13),
          ("nema-L2130R", 14),
          ("nema-L2230R", 15),
          ("iec-309-1620", 16),
          ("iec-309-3032", 17),
          ("iec-309-6063", 18),
          ("iec-320-C13", 19),
          ("iec-320-C14", 20),
          ("iec-320-C15", 21),
          ("iec-320-C17", 22),
          ("iec-320-C19", 23),
          ("iec-320-C20", 24))
    )


_TlpUpsOutletReceptacleType_Type.__name__ = "Integer32"
_TlpUpsOutletReceptacleType_Object = MibTableColumn
tlpUpsOutletReceptacleType = _TlpUpsOutletReceptacleType_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 5, 1, 1, 18),
    _TlpUpsOutletReceptacleType_Type()
)
tlpUpsOutletReceptacleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsOutletReceptacleType.setStatus("current")


class _TlpUpsOutletPowerFactor_Type(Integer32):
    """Custom type tlpUpsOutletPowerFactor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_TlpUpsOutletPowerFactor_Type.__name__ = "Integer32"
_TlpUpsOutletPowerFactor_Object = MibTableColumn
tlpUpsOutletPowerFactor = _TlpUpsOutletPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 5, 1, 1, 19),
    _TlpUpsOutletPowerFactor_Type()
)
tlpUpsOutletPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsOutletPowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsOutletPowerFactor.setUnits("percent")
_TlpUpsOutletApparentPower_Type = Unsigned32
_TlpUpsOutletApparentPower_Object = MibTableColumn
tlpUpsOutletApparentPower = _TlpUpsOutletApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 5, 1, 1, 20),
    _TlpUpsOutletApparentPower_Type()
)
tlpUpsOutletApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsOutletApparentPower.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsOutletApparentPower.setUnits("VA")
_TlpUpsOutletReactivePower_Type = Integer32
_TlpUpsOutletReactivePower_Object = MibTableColumn
tlpUpsOutletReactivePower = _TlpUpsOutletReactivePower_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 5, 1, 1, 21),
    _TlpUpsOutletReactivePower_Type()
)
tlpUpsOutletReactivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsOutletReactivePower.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsOutletReactivePower.setUnits("VAR")
_TlpUpsOutletFrequency_Type = Unsigned32
_TlpUpsOutletFrequency_Object = MibTableColumn
tlpUpsOutletFrequency = _TlpUpsOutletFrequency_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 5, 1, 1, 22),
    _TlpUpsOutletFrequency_Type()
)
tlpUpsOutletFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsOutletFrequency.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsOutletFrequency.setUnits("0.1 Hertz")
_TlpUpsOutletUtilization_Type = Unsigned32
_TlpUpsOutletUtilization_Object = MibTableColumn
tlpUpsOutletUtilization = _TlpUpsOutletUtilization_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 5, 1, 1, 23),
    _TlpUpsOutletUtilization_Type()
)
tlpUpsOutletUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsOutletUtilization.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsOutletUtilization.setUnits("0.01 percent")
_TlpUpsOutlet24hrEnergy_Type = Unsigned32
_TlpUpsOutlet24hrEnergy_Object = MibTableColumn
tlpUpsOutlet24hrEnergy = _TlpUpsOutlet24hrEnergy_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 5, 1, 1, 24),
    _TlpUpsOutlet24hrEnergy_Type()
)
tlpUpsOutlet24hrEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsOutlet24hrEnergy.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsOutlet24hrEnergy.setUnits("0.01 KWH")
_TlpUpsOutletOvercurrent_Type = TruthValue
_TlpUpsOutletOvercurrent_Object = MibTableColumn
tlpUpsOutletOvercurrent = _TlpUpsOutletOvercurrent_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 5, 1, 1, 25),
    _TlpUpsOutletOvercurrent_Type()
)
tlpUpsOutletOvercurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsOutletOvercurrent.setStatus("current")
_TlpUpsOutletGroupTable_Object = MibTable
tlpUpsOutletGroupTable = _TlpUpsOutletGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 5, 2)
)
if mibBuilder.loadTexts:
    tlpUpsOutletGroupTable.setStatus("current")
_TlpUpsOutletGroupEntry_Object = MibTableRow
tlpUpsOutletGroupEntry = _TlpUpsOutletGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 5, 2, 1)
)
tlpUpsOutletGroupEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpUpsOutletGroupIndex"),
)
if mibBuilder.loadTexts:
    tlpUpsOutletGroupEntry.setStatus("current")
_TlpUpsOutletGroupIndex_Type = Unsigned32
_TlpUpsOutletGroupIndex_Object = MibTableColumn
tlpUpsOutletGroupIndex = _TlpUpsOutletGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 5, 2, 1, 1),
    _TlpUpsOutletGroupIndex_Type()
)
tlpUpsOutletGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsOutletGroupIndex.setStatus("current")
_TlpUpsOutletGroupRowStatus_Type = RowStatus
_TlpUpsOutletGroupRowStatus_Object = MibTableColumn
tlpUpsOutletGroupRowStatus = _TlpUpsOutletGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 5, 2, 1, 2),
    _TlpUpsOutletGroupRowStatus_Type()
)
tlpUpsOutletGroupRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsOutletGroupRowStatus.setStatus("current")
_TlpUpsOutletGroupName_Type = DisplayString
_TlpUpsOutletGroupName_Object = MibTableColumn
tlpUpsOutletGroupName = _TlpUpsOutletGroupName_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 5, 2, 1, 3),
    _TlpUpsOutletGroupName_Type()
)
tlpUpsOutletGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsOutletGroupName.setStatus("current")
_TlpUpsOutletGroupDescription_Type = DisplayString
_TlpUpsOutletGroupDescription_Object = MibTableColumn
tlpUpsOutletGroupDescription = _TlpUpsOutletGroupDescription_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 5, 2, 1, 4),
    _TlpUpsOutletGroupDescription_Type()
)
tlpUpsOutletGroupDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsOutletGroupDescription.setStatus("current")


class _TlpUpsOutletGroupState_Type(Integer32):
    """Custom type tlpUpsOutletGroupState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("off", 1),
          ("on", 2),
          ("mixed", 3))
    )


_TlpUpsOutletGroupState_Type.__name__ = "Integer32"
_TlpUpsOutletGroupState_Object = MibTableColumn
tlpUpsOutletGroupState = _TlpUpsOutletGroupState_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 5, 2, 1, 5),
    _TlpUpsOutletGroupState_Type()
)
tlpUpsOutletGroupState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsOutletGroupState.setStatus("current")


class _TlpUpsOutletGroupCommand_Type(Integer32):
    """Custom type tlpUpsOutletGroupCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("turnOff", 1),
          ("turnOn", 2),
          ("cycle", 3))
    )


_TlpUpsOutletGroupCommand_Type.__name__ = "Integer32"
_TlpUpsOutletGroupCommand_Object = MibTableColumn
tlpUpsOutletGroupCommand = _TlpUpsOutletGroupCommand_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 5, 2, 1, 6),
    _TlpUpsOutletGroupCommand_Type()
)
tlpUpsOutletGroupCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsOutletGroupCommand.setStatus("current")
_TlpUpsWatchdog_ObjectIdentity = ObjectIdentity
tlpUpsWatchdog = _TlpUpsWatchdog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 6)
)
_TlpUpsWatchdogTable_Object = MibTable
tlpUpsWatchdogTable = _TlpUpsWatchdogTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 6, 1)
)
if mibBuilder.loadTexts:
    tlpUpsWatchdogTable.setStatus("current")
_TlpUpsWatchdogEntry_Object = MibTableRow
tlpUpsWatchdogEntry = _TlpUpsWatchdogEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 6, 1, 1)
)
tlpUpsWatchdogEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpUpsWatchdogEntry.setStatus("current")
_TlpUpsWatchdogSupported_Type = TruthValue
_TlpUpsWatchdogSupported_Object = MibTableColumn
tlpUpsWatchdogSupported = _TlpUpsWatchdogSupported_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 6, 1, 1, 1),
    _TlpUpsWatchdogSupported_Type()
)
tlpUpsWatchdogSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsWatchdogSupported.setStatus("current")
_TlpUpsWatchdogSecsBeforeRestart_Type = Unsigned32
_TlpUpsWatchdogSecsBeforeRestart_Object = MibTableColumn
tlpUpsWatchdogSecsBeforeRestart = _TlpUpsWatchdogSecsBeforeRestart_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 6, 1, 1, 2),
    _TlpUpsWatchdogSecsBeforeRestart_Type()
)
tlpUpsWatchdogSecsBeforeRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsWatchdogSecsBeforeRestart.setStatus("current")


class _TlpUpsWatchdogRestartAlarm_Type(Integer32):
    """Custom type tlpUpsWatchdogRestartAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TlpUpsWatchdogRestartAlarm_Type.__name__ = "Integer32"
_TlpUpsWatchdogRestartAlarm_Object = MibTableColumn
tlpUpsWatchdogRestartAlarm = _TlpUpsWatchdogRestartAlarm_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 6, 1, 1, 3),
    _TlpUpsWatchdogRestartAlarm_Type()
)
tlpUpsWatchdogRestartAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsWatchdogRestartAlarm.setStatus("current")


class _TlpUpsWatchdogStatus_Type(Integer32):
    """Custom type tlpUpsWatchdogStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TlpUpsWatchdogStatus_Type.__name__ = "Integer32"
_TlpUpsWatchdogStatus_Object = MibTableColumn
tlpUpsWatchdogStatus = _TlpUpsWatchdogStatus_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 6, 1, 1, 4),
    _TlpUpsWatchdogStatus_Type()
)
tlpUpsWatchdogStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsWatchdogStatus.setStatus("current")


class _TlpUpsWatchdogRetry_Type(Integer32):
    """Custom type tlpUpsWatchdogRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TlpUpsWatchdogRetry_Type.__name__ = "Integer32"
_TlpUpsWatchdogRetry_Object = MibTableColumn
tlpUpsWatchdogRetry = _TlpUpsWatchdogRetry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 6, 1, 1, 5),
    _TlpUpsWatchdogRetry_Type()
)
tlpUpsWatchdogRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsWatchdogRetry.setStatus("current")
_TlpUpsFan_ObjectIdentity = ObjectIdentity
tlpUpsFan = _TlpUpsFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 7)
)
_TlpUpsFanTable_Object = MibTable
tlpUpsFanTable = _TlpUpsFanTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 7, 1)
)
if mibBuilder.loadTexts:
    tlpUpsFanTable.setStatus("current")
_TlpUpsFanEntry_Object = MibTableRow
tlpUpsFanEntry = _TlpUpsFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 7, 1, 1)
)
tlpUpsFanEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpUpsFanIndex"),
)
if mibBuilder.loadTexts:
    tlpUpsFanEntry.setStatus("current")
_TlpUpsFanIndex_Type = Unsigned32
_TlpUpsFanIndex_Object = MibTableColumn
tlpUpsFanIndex = _TlpUpsFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 7, 1, 1, 1),
    _TlpUpsFanIndex_Type()
)
tlpUpsFanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsFanIndex.setStatus("current")


class _TlpUpsFanLocation_Type(Integer32):
    """Custom type tlpUpsFanLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("internal", 1),
          ("external", 2))
    )


_TlpUpsFanLocation_Type.__name__ = "Integer32"
_TlpUpsFanLocation_Object = MibTableColumn
tlpUpsFanLocation = _TlpUpsFanLocation_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 7, 1, 1, 2),
    _TlpUpsFanLocation_Type()
)
tlpUpsFanLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsFanLocation.setStatus("current")


class _TlpUpsFanStatus_Type(Integer32):
    """Custom type tlpUpsFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_TlpUpsFanStatus_Type.__name__ = "Integer32"
_TlpUpsFanStatus_Object = MibTableColumn
tlpUpsFanStatus = _TlpUpsFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 7, 1, 1, 3),
    _TlpUpsFanStatus_Type()
)
tlpUpsFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsFanStatus.setStatus("current")
_TlpUpsFanSpeed_Type = Unsigned32
_TlpUpsFanSpeed_Object = MibTableColumn
tlpUpsFanSpeed = _TlpUpsFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 7, 1, 1, 4),
    _TlpUpsFanSpeed_Type()
)
tlpUpsFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsFanSpeed.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsFanSpeed.setUnits("RPM")
_TlpUpsFanActivationTemperatureDegF_Type = Integer32
_TlpUpsFanActivationTemperatureDegF_Object = MibTableColumn
tlpUpsFanActivationTemperatureDegF = _TlpUpsFanActivationTemperatureDegF_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 7, 1, 1, 5),
    _TlpUpsFanActivationTemperatureDegF_Type()
)
tlpUpsFanActivationTemperatureDegF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsFanActivationTemperatureDegF.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsFanActivationTemperatureDegF.setUnits("0.1 degrees Fahrenheit")
_TlpUpsFanActivationTemperatureDegC_Type = Integer32
_TlpUpsFanActivationTemperatureDegC_Object = MibTableColumn
tlpUpsFanActivationTemperatureDegC = _TlpUpsFanActivationTemperatureDegC_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 7, 1, 1, 6),
    _TlpUpsFanActivationTemperatureDegC_Type()
)
tlpUpsFanActivationTemperatureDegC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsFanActivationTemperatureDegC.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsFanActivationTemperatureDegC.setUnits("0.1 degrees Celsius")
_TlpUpsHeatsink_ObjectIdentity = ObjectIdentity
tlpUpsHeatsink = _TlpUpsHeatsink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 8)
)
_TlpUpsHeatsinkTable_Object = MibTable
tlpUpsHeatsinkTable = _TlpUpsHeatsinkTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 8, 1)
)
if mibBuilder.loadTexts:
    tlpUpsHeatsinkTable.setStatus("current")
_TlpUpsHeatsinkEntry_Object = MibTableRow
tlpUpsHeatsinkEntry = _TlpUpsHeatsinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 8, 1, 1)
)
tlpUpsHeatsinkEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpUpsHeatsinkIndex"),
)
if mibBuilder.loadTexts:
    tlpUpsHeatsinkEntry.setStatus("current")
_TlpUpsHeatsinkIndex_Type = Unsigned32
_TlpUpsHeatsinkIndex_Object = MibTableColumn
tlpUpsHeatsinkIndex = _TlpUpsHeatsinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 8, 1, 1, 1),
    _TlpUpsHeatsinkIndex_Type()
)
tlpUpsHeatsinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsHeatsinkIndex.setStatus("current")
_TlpUpsHeatsinkTemperatureC_Type = Integer32
_TlpUpsHeatsinkTemperatureC_Object = MibTableColumn
tlpUpsHeatsinkTemperatureC = _TlpUpsHeatsinkTemperatureC_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 8, 1, 1, 2),
    _TlpUpsHeatsinkTemperatureC_Type()
)
tlpUpsHeatsinkTemperatureC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsHeatsinkTemperatureC.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsHeatsinkTemperatureC.setUnits("0.1 degrees Celsius")
_TlpUpsHeatsinkTemperatureF_Type = Integer32
_TlpUpsHeatsinkTemperatureF_Object = MibTableColumn
tlpUpsHeatsinkTemperatureF = _TlpUpsHeatsinkTemperatureF_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 8, 1, 1, 3),
    _TlpUpsHeatsinkTemperatureF_Type()
)
tlpUpsHeatsinkTemperatureF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsHeatsinkTemperatureF.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsHeatsinkTemperatureF.setUnits("0.1 degrees Fahrenheit")
_TlpUpsContact_ObjectIdentity = ObjectIdentity
tlpUpsContact = _TlpUpsContact_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 9)
)
_TlpUpsInputContact_ObjectIdentity = ObjectIdentity
tlpUpsInputContact = _TlpUpsInputContact_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 9, 1)
)
_TlpUpsInputContactTable_Object = MibTable
tlpUpsInputContactTable = _TlpUpsInputContactTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 9, 1, 1)
)
if mibBuilder.loadTexts:
    tlpUpsInputContactTable.setStatus("current")
_TlpUpsInputContactEntry_Object = MibTableRow
tlpUpsInputContactEntry = _TlpUpsInputContactEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 9, 1, 1, 1)
)
tlpUpsInputContactEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpUpsInputContactIndex"),
)
if mibBuilder.loadTexts:
    tlpUpsInputContactEntry.setStatus("current")
_TlpUpsInputContactIndex_Type = Unsigned32
_TlpUpsInputContactIndex_Object = MibTableColumn
tlpUpsInputContactIndex = _TlpUpsInputContactIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 9, 1, 1, 1, 1),
    _TlpUpsInputContactIndex_Type()
)
tlpUpsInputContactIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsInputContactIndex.setStatus("current")


class _TlpUpsInputContactInAlarm_Type(Integer32):
    """Custom type tlpUpsInputContactInAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notInAlarm", 0),
          ("inAlarm", 1))
    )


_TlpUpsInputContactInAlarm_Type.__name__ = "Integer32"
_TlpUpsInputContactInAlarm_Object = MibTableColumn
tlpUpsInputContactInAlarm = _TlpUpsInputContactInAlarm_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 9, 1, 1, 1, 2),
    _TlpUpsInputContactInAlarm_Type()
)
tlpUpsInputContactInAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsInputContactInAlarm.setStatus("current")
_TlpUpsOutputContact_ObjectIdentity = ObjectIdentity
tlpUpsOutputContact = _TlpUpsOutputContact_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 9, 2)
)
_TlpUpsOutputContactTable_Object = MibTable
tlpUpsOutputContactTable = _TlpUpsOutputContactTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 9, 2, 1)
)
if mibBuilder.loadTexts:
    tlpUpsOutputContactTable.setStatus("current")
_TlpUpsOutputContactEntry_Object = MibTableRow
tlpUpsOutputContactEntry = _TlpUpsOutputContactEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 9, 2, 1, 1)
)
tlpUpsOutputContactEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpUpsOutputContactIndex"),
)
if mibBuilder.loadTexts:
    tlpUpsOutputContactEntry.setStatus("current")
_TlpUpsOutputContactIndex_Type = Unsigned32
_TlpUpsOutputContactIndex_Object = MibTableColumn
tlpUpsOutputContactIndex = _TlpUpsOutputContactIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 9, 2, 1, 1, 1),
    _TlpUpsOutputContactIndex_Type()
)
tlpUpsOutputContactIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsOutputContactIndex.setStatus("current")


class _TlpUpsOutputContactInAlarm_Type(Integer32):
    """Custom type tlpUpsOutputContactInAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notInAlarm", 0),
          ("inAlarm", 1))
    )


_TlpUpsOutputContactInAlarm_Type.__name__ = "Integer32"
_TlpUpsOutputContactInAlarm_Object = MibTableColumn
tlpUpsOutputContactInAlarm = _TlpUpsOutputContactInAlarm_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 9, 2, 1, 1, 2),
    _TlpUpsOutputContactInAlarm_Type()
)
tlpUpsOutputContactInAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsOutputContactInAlarm.setStatus("current")
_TlpUpsControl_ObjectIdentity = ObjectIdentity
tlpUpsControl = _TlpUpsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 4)
)
_TlpUpsControlTable_Object = MibTable
tlpUpsControlTable = _TlpUpsControlTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 4, 1)
)
if mibBuilder.loadTexts:
    tlpUpsControlTable.setStatus("current")
_TlpUpsControlEntry_Object = MibTableRow
tlpUpsControlEntry = _TlpUpsControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 4, 1, 1)
)
tlpUpsControlEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpUpsControlEntry.setStatus("current")
_TlpUpsControlSelfTest_Type = TruthValue
_TlpUpsControlSelfTest_Object = MibTableColumn
tlpUpsControlSelfTest = _TlpUpsControlSelfTest_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 4, 1, 1, 1),
    _TlpUpsControlSelfTest_Type()
)
tlpUpsControlSelfTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsControlSelfTest.setStatus("current")
_TlpUpsControlRamp_Type = TruthValue
_TlpUpsControlRamp_Object = MibTableColumn
tlpUpsControlRamp = _TlpUpsControlRamp_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 4, 1, 1, 2),
    _TlpUpsControlRamp_Type()
)
tlpUpsControlRamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsControlRamp.setStatus("current")
_TlpUpsControlShed_Type = TruthValue
_TlpUpsControlShed_Object = MibTableColumn
tlpUpsControlShed = _TlpUpsControlShed_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 4, 1, 1, 3),
    _TlpUpsControlShed_Type()
)
tlpUpsControlShed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsControlShed.setStatus("current")
_TlpUpsControlUpsOn_Type = TruthValue
_TlpUpsControlUpsOn_Object = MibTableColumn
tlpUpsControlUpsOn = _TlpUpsControlUpsOn_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 4, 1, 1, 4),
    _TlpUpsControlUpsOn_Type()
)
tlpUpsControlUpsOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsControlUpsOn.setStatus("current")
_TlpUpsControlUpsOff_Type = TruthValue
_TlpUpsControlUpsOff_Object = MibTableColumn
tlpUpsControlUpsOff = _TlpUpsControlUpsOff_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 4, 1, 1, 5),
    _TlpUpsControlUpsOff_Type()
)
tlpUpsControlUpsOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsControlUpsOff.setStatus("current")
_TlpUpsControlUpsRestart_Type = TruthValue
_TlpUpsControlUpsRestart_Object = MibTableColumn
tlpUpsControlUpsRestart = _TlpUpsControlUpsRestart_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 4, 1, 1, 6),
    _TlpUpsControlUpsRestart_Type()
)
tlpUpsControlUpsRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsControlUpsRestart.setStatus("current")


class _TlpUpsControlBypass_Type(Integer32):
    """Custom type tlpUpsControlBypass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TlpUpsControlBypass_Type.__name__ = "Integer32"
_TlpUpsControlBypass_Object = MibTableColumn
tlpUpsControlBypass = _TlpUpsControlBypass_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 4, 1, 1, 7),
    _TlpUpsControlBypass_Type()
)
tlpUpsControlBypass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsControlBypass.setStatus("current")
_TlpUpsControlResetWattHours_Type = TruthValue
_TlpUpsControlResetWattHours_Object = MibTableColumn
tlpUpsControlResetWattHours = _TlpUpsControlResetWattHours_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 4, 1, 1, 8),
    _TlpUpsControlResetWattHours_Type()
)
tlpUpsControlResetWattHours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsControlResetWattHours.setStatus("current")
_TlpUpsControlCancelSelfTest_Type = TruthValue
_TlpUpsControlCancelSelfTest_Object = MibTableColumn
tlpUpsControlCancelSelfTest = _TlpUpsControlCancelSelfTest_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 4, 1, 1, 9),
    _TlpUpsControlCancelSelfTest_Type()
)
tlpUpsControlCancelSelfTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsControlCancelSelfTest.setStatus("current")
_TlpUpsControlResetAllParameters_Type = TruthValue
_TlpUpsControlResetAllParameters_Object = MibTableColumn
tlpUpsControlResetAllParameters = _TlpUpsControlResetAllParameters_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 4, 1, 1, 10),
    _TlpUpsControlResetAllParameters_Type()
)
tlpUpsControlResetAllParameters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsControlResetAllParameters.setStatus("current")
_TlpUpsControlMuteBuzzer_Type = TruthValue
_TlpUpsControlMuteBuzzer_Object = MibTableColumn
tlpUpsControlMuteBuzzer = _TlpUpsControlMuteBuzzer_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 4, 1, 1, 11),
    _TlpUpsControlMuteBuzzer_Type()
)
tlpUpsControlMuteBuzzer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsControlMuteBuzzer.setStatus("current")
_TlpUpsControlResetBatteryTransitionCount_Type = TruthValue
_TlpUpsControlResetBatteryTransitionCount_Object = MibTableColumn
tlpUpsControlResetBatteryTransitionCount = _TlpUpsControlResetBatteryTransitionCount_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 4, 1, 1, 12),
    _TlpUpsControlResetBatteryTransitionCount_Type()
)
tlpUpsControlResetBatteryTransitionCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsControlResetBatteryTransitionCount.setStatus("current")
_TlpUpsControlResetLastReasonForBypass_Type = TruthValue
_TlpUpsControlResetLastReasonForBypass_Object = MibTableColumn
tlpUpsControlResetLastReasonForBypass = _TlpUpsControlResetLastReasonForBypass_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 4, 1, 1, 13),
    _TlpUpsControlResetLastReasonForBypass_Type()
)
tlpUpsControlResetLastReasonForBypass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsControlResetLastReasonForBypass.setStatus("current")
_TlpUpsControlResetLastReasonStats_Type = TruthValue
_TlpUpsControlResetLastReasonStats_Object = MibTableColumn
tlpUpsControlResetLastReasonStats = _TlpUpsControlResetLastReasonStats_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 4, 1, 1, 14),
    _TlpUpsControlResetLastReasonStats_Type()
)
tlpUpsControlResetLastReasonStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsControlResetLastReasonStats.setStatus("current")
_TlpUpsControlResetAvrTransitionCount_Type = TruthValue
_TlpUpsControlResetAvrTransitionCount_Object = MibTableColumn
tlpUpsControlResetAvrTransitionCount = _TlpUpsControlResetAvrTransitionCount_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 4, 1, 1, 15),
    _TlpUpsControlResetAvrTransitionCount_Type()
)
tlpUpsControlResetAvrTransitionCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsControlResetAvrTransitionCount.setStatus("current")
_TlpUpsControlResetPeakPower_Type = TruthValue
_TlpUpsControlResetPeakPower_Object = MibTableColumn
tlpUpsControlResetPeakPower = _TlpUpsControlResetPeakPower_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 4, 1, 1, 16),
    _TlpUpsControlResetPeakPower_Type()
)
tlpUpsControlResetPeakPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsControlResetPeakPower.setStatus("current")
_TlpUpsControlClearEventLog_Type = TruthValue
_TlpUpsControlClearEventLog_Object = MibTableColumn
tlpUpsControlClearEventLog = _TlpUpsControlClearEventLog_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 4, 1, 1, 17),
    _TlpUpsControlClearEventLog_Type()
)
tlpUpsControlClearEventLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsControlClearEventLog.setStatus("current")
_TlpUpsControlOutputPhaseTable_Object = MibTable
tlpUpsControlOutputPhaseTable = _TlpUpsControlOutputPhaseTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 4, 2)
)
if mibBuilder.loadTexts:
    tlpUpsControlOutputPhaseTable.setStatus("current")
_TlpUpsControlOutputPhaseEntry_Object = MibTableRow
tlpUpsControlOutputPhaseEntry = _TlpUpsControlOutputPhaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 4, 2, 1)
)
tlpUpsControlOutputPhaseEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpUpsOutputLineIndex"),
)
if mibBuilder.loadTexts:
    tlpUpsControlOutputPhaseEntry.setStatus("current")
_TlpUpsControlResetOutputCurrentMinMax_Type = TruthValue
_TlpUpsControlResetOutputCurrentMinMax_Object = MibTableColumn
tlpUpsControlResetOutputCurrentMinMax = _TlpUpsControlResetOutputCurrentMinMax_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 4, 2, 1, 1),
    _TlpUpsControlResetOutputCurrentMinMax_Type()
)
tlpUpsControlResetOutputCurrentMinMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsControlResetOutputCurrentMinMax.setStatus("current")
_TlpUpsControlInputPhaseTable_Object = MibTable
tlpUpsControlInputPhaseTable = _TlpUpsControlInputPhaseTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 4, 3)
)
if mibBuilder.loadTexts:
    tlpUpsControlInputPhaseTable.setStatus("current")
_TlpUpsControlInputPhaseEntry_Object = MibTableRow
tlpUpsControlInputPhaseEntry = _TlpUpsControlInputPhaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 4, 3, 1)
)
tlpUpsControlInputPhaseEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpUpsInputPhaseIndex"),
)
if mibBuilder.loadTexts:
    tlpUpsControlInputPhaseEntry.setStatus("current")
_TlpUpsControlResetInputVoltageMinMax_Type = TruthValue
_TlpUpsControlResetInputVoltageMinMax_Object = MibTableColumn
tlpUpsControlResetInputVoltageMinMax = _TlpUpsControlResetInputVoltageMinMax_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 4, 3, 1, 1),
    _TlpUpsControlResetInputVoltageMinMax_Type()
)
tlpUpsControlResetInputVoltageMinMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsControlResetInputVoltageMinMax.setStatus("current")
_TlpUpsConfig_ObjectIdentity = ObjectIdentity
tlpUpsConfig = _TlpUpsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5)
)
_TlpUpsConfigTable_Object = MibTable
tlpUpsConfigTable = _TlpUpsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 1)
)
if mibBuilder.loadTexts:
    tlpUpsConfigTable.setStatus("current")
_TlpUpsConfigEntry_Object = MibTableRow
tlpUpsConfigEntry = _TlpUpsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 1, 1)
)
tlpUpsConfigEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpUpsConfigEntry.setStatus("current")
_TlpUpsConfigInputVoltage_Type = Unsigned32
_TlpUpsConfigInputVoltage_Object = MibTableColumn
tlpUpsConfigInputVoltage = _TlpUpsConfigInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 1, 1, 1),
    _TlpUpsConfigInputVoltage_Type()
)
tlpUpsConfigInputVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigInputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsConfigInputVoltage.setUnits("Volts")
_TlpUpsConfigInputFrequency_Type = Unsigned32
_TlpUpsConfigInputFrequency_Object = MibTableColumn
tlpUpsConfigInputFrequency = _TlpUpsConfigInputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 1, 1, 2),
    _TlpUpsConfigInputFrequency_Type()
)
tlpUpsConfigInputFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigInputFrequency.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsConfigInputFrequency.setUnits("0.1 Hertz")
_TlpUpsConfigOutputVoltage_Type = Unsigned32
_TlpUpsConfigOutputVoltage_Object = MibTableColumn
tlpUpsConfigOutputVoltage = _TlpUpsConfigOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 1, 1, 3),
    _TlpUpsConfigOutputVoltage_Type()
)
tlpUpsConfigOutputVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigOutputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsConfigOutputVoltage.setUnits("Volts")
_TlpUpsConfigOutputFrequency_Type = Unsigned32
_TlpUpsConfigOutputFrequency_Object = MibTableColumn
tlpUpsConfigOutputFrequency = _TlpUpsConfigOutputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 1, 1, 4),
    _TlpUpsConfigOutputFrequency_Type()
)
tlpUpsConfigOutputFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigOutputFrequency.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsConfigOutputFrequency.setUnits("0.1 Hertz")


class _TlpUpsConfigAudibleStatus_Type(Integer32):
    """Custom type tlpUpsConfigAudibleStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("muted", 3))
    )


_TlpUpsConfigAudibleStatus_Type.__name__ = "Integer32"
_TlpUpsConfigAudibleStatus_Object = MibTableColumn
tlpUpsConfigAudibleStatus = _TlpUpsConfigAudibleStatus_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 1, 1, 5),
    _TlpUpsConfigAudibleStatus_Type()
)
tlpUpsConfigAudibleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigAudibleStatus.setStatus("current")


class _TlpUpsConfigAutoBatteryTest_Type(Integer32):
    """Custom type tlpUpsConfigAutoBatteryTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("daily", 1),
          ("weekly", 2),
          ("biweekly", 3),
          ("monthly", 4),
          ("quarterly", 5),
          ("semiannually", 6))
    )


_TlpUpsConfigAutoBatteryTest_Type.__name__ = "Integer32"
_TlpUpsConfigAutoBatteryTest_Object = MibTableColumn
tlpUpsConfigAutoBatteryTest = _TlpUpsConfigAutoBatteryTest_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 1, 1, 6),
    _TlpUpsConfigAutoBatteryTest_Type()
)
tlpUpsConfigAutoBatteryTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigAutoBatteryTest.setStatus("current")


class _TlpUpsConfigAutoRestartAfterShutdown_Type(Integer32):
    """Custom type tlpUpsConfigAutoRestartAfterShutdown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TlpUpsConfigAutoRestartAfterShutdown_Type.__name__ = "Integer32"
_TlpUpsConfigAutoRestartAfterShutdown_Object = MibTableColumn
tlpUpsConfigAutoRestartAfterShutdown = _TlpUpsConfigAutoRestartAfterShutdown_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 1, 1, 7),
    _TlpUpsConfigAutoRestartAfterShutdown_Type()
)
tlpUpsConfigAutoRestartAfterShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigAutoRestartAfterShutdown.setStatus("current")


class _TlpUpsConfigAutoRampOnTransition_Type(Integer32):
    """Custom type tlpUpsConfigAutoRampOnTransition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TlpUpsConfigAutoRampOnTransition_Type.__name__ = "Integer32"
_TlpUpsConfigAutoRampOnTransition_Object = MibTableColumn
tlpUpsConfigAutoRampOnTransition = _TlpUpsConfigAutoRampOnTransition_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 1, 1, 8),
    _TlpUpsConfigAutoRampOnTransition_Type()
)
tlpUpsConfigAutoRampOnTransition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigAutoRampOnTransition.setStatus("current")


class _TlpUpsConfigAutoShedOnTransition_Type(Integer32):
    """Custom type tlpUpsConfigAutoShedOnTransition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TlpUpsConfigAutoShedOnTransition_Type.__name__ = "Integer32"
_TlpUpsConfigAutoShedOnTransition_Object = MibTableColumn
tlpUpsConfigAutoShedOnTransition = _TlpUpsConfigAutoShedOnTransition_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 1, 1, 9),
    _TlpUpsConfigAutoShedOnTransition_Type()
)
tlpUpsConfigAutoShedOnTransition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigAutoShedOnTransition.setStatus("current")


class _TlpUpsConfigBypassLowerLimitPercent_Type(Integer32):
    """Custom type tlpUpsConfigBypassLowerLimitPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20, -5),
    )


_TlpUpsConfigBypassLowerLimitPercent_Type.__name__ = "Integer32"
_TlpUpsConfigBypassLowerLimitPercent_Object = MibTableColumn
tlpUpsConfigBypassLowerLimitPercent = _TlpUpsConfigBypassLowerLimitPercent_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 1, 1, 10),
    _TlpUpsConfigBypassLowerLimitPercent_Type()
)
tlpUpsConfigBypassLowerLimitPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigBypassLowerLimitPercent.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsConfigBypassLowerLimitPercent.setUnits("percent")


class _TlpUpsConfigBypassUpperLimitPercent_Type(Integer32):
    """Custom type tlpUpsConfigBypassUpperLimitPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 20),
    )


_TlpUpsConfigBypassUpperLimitPercent_Type.__name__ = "Integer32"
_TlpUpsConfigBypassUpperLimitPercent_Object = MibTableColumn
tlpUpsConfigBypassUpperLimitPercent = _TlpUpsConfigBypassUpperLimitPercent_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 1, 1, 11),
    _TlpUpsConfigBypassUpperLimitPercent_Type()
)
tlpUpsConfigBypassUpperLimitPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigBypassUpperLimitPercent.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsConfigBypassUpperLimitPercent.setUnits("percent")
_TlpUpsConfigBypassLowerLimitVoltage_Type = Unsigned32
_TlpUpsConfigBypassLowerLimitVoltage_Object = MibTableColumn
tlpUpsConfigBypassLowerLimitVoltage = _TlpUpsConfigBypassLowerLimitVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 1, 1, 12),
    _TlpUpsConfigBypassLowerLimitVoltage_Type()
)
tlpUpsConfigBypassLowerLimitVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigBypassLowerLimitVoltage.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsConfigBypassLowerLimitVoltage.setUnits("Volts")
_TlpUpsConfigBypassUpperLimitVoltage_Type = Unsigned32
_TlpUpsConfigBypassUpperLimitVoltage_Object = MibTableColumn
tlpUpsConfigBypassUpperLimitVoltage = _TlpUpsConfigBypassUpperLimitVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 1, 1, 13),
    _TlpUpsConfigBypassUpperLimitVoltage_Type()
)
tlpUpsConfigBypassUpperLimitVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigBypassUpperLimitVoltage.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsConfigBypassUpperLimitVoltage.setUnits("Volts")


class _TlpUpsConfigColdStart_Type(Integer32):
    """Custom type tlpUpsConfigColdStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TlpUpsConfigColdStart_Type.__name__ = "Integer32"
_TlpUpsConfigColdStart_Object = MibTableColumn
tlpUpsConfigColdStart = _TlpUpsConfigColdStart_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 1, 1, 14),
    _TlpUpsConfigColdStart_Type()
)
tlpUpsConfigColdStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigColdStart.setStatus("current")


class _TlpUpsConfigPowerStrategy_Type(Integer32):
    """Custom type tlpUpsConfigPowerStrategy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("maximumQuality", 0),
          ("maximumEfficiency", 1),
          ("constant50Hz", 2),
          ("constant60Hz", 3),
          ("constantAuto", 4),
          ("autoAdaptive", 5))
    )


_TlpUpsConfigPowerStrategy_Type.__name__ = "Integer32"
_TlpUpsConfigPowerStrategy_Object = MibTableColumn
tlpUpsConfigPowerStrategy = _TlpUpsConfigPowerStrategy_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 1, 1, 15),
    _TlpUpsConfigPowerStrategy_Type()
)
tlpUpsConfigPowerStrategy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigPowerStrategy.setStatus("current")


class _TlpUpsConfigFaultAction_Type(Integer32):
    """Custom type tlpUpsConfigFaultAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bypass", 0),
          ("standby", 1))
    )


_TlpUpsConfigFaultAction_Type.__name__ = "Integer32"
_TlpUpsConfigFaultAction_Object = MibTableColumn
tlpUpsConfigFaultAction = _TlpUpsConfigFaultAction_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 1, 1, 16),
    _TlpUpsConfigFaultAction_Type()
)
tlpUpsConfigFaultAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigFaultAction.setStatus("current")


class _TlpUpsConfigOffMode_Type(Integer32):
    """Custom type tlpUpsConfigOffMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("standby", 0),
          ("bypass", 1))
    )


_TlpUpsConfigOffMode_Type.__name__ = "Integer32"
_TlpUpsConfigOffMode_Object = MibTableColumn
tlpUpsConfigOffMode = _TlpUpsConfigOffMode_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 1, 1, 17),
    _TlpUpsConfigOffMode_Type()
)
tlpUpsConfigOffMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigOffMode.setStatus("current")


class _TlpUpsConfigLineSensitivity_Type(Integer32):
    """Custom type tlpUpsConfigLineSensitivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("reduced", 1),
          ("fullyReduced", 2))
    )


_TlpUpsConfigLineSensitivity_Type.__name__ = "Integer32"
_TlpUpsConfigLineSensitivity_Object = MibTableColumn
tlpUpsConfigLineSensitivity = _TlpUpsConfigLineSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 1, 1, 18),
    _TlpUpsConfigLineSensitivity_Type()
)
tlpUpsConfigLineSensitivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigLineSensitivity.setStatus("current")
_TlpUpsConfigLineQualifyTime_Type = Unsigned32
_TlpUpsConfigLineQualifyTime_Object = MibTableColumn
tlpUpsConfigLineQualifyTime = _TlpUpsConfigLineQualifyTime_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 1, 1, 19),
    _TlpUpsConfigLineQualifyTime_Type()
)
tlpUpsConfigLineQualifyTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigLineQualifyTime.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsConfigLineQualifyTime.setUnits("seconds")


class _TlpUpsConfigACPowerSenseType_Type(Integer32):
    """Custom type tlpUpsConfigACPowerSenseType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("generator", 1),
          ("ups", 2))
    )


_TlpUpsConfigACPowerSenseType_Type.__name__ = "Integer32"
_TlpUpsConfigACPowerSenseType_Object = MibTableColumn
tlpUpsConfigACPowerSenseType = _TlpUpsConfigACPowerSenseType_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 1, 1, 20),
    _TlpUpsConfigACPowerSenseType_Type()
)
tlpUpsConfigACPowerSenseType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigACPowerSenseType.setStatus("current")


class _TlpUpsConfigAcPresentStartMode_Type(Integer32):
    """Custom type tlpUpsConfigAcPresentStartMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alwaysOff", 0),
          ("alwaysTurnOn", 1),
          ("lastState", 2))
    )


_TlpUpsConfigAcPresentStartMode_Type.__name__ = "Integer32"
_TlpUpsConfigAcPresentStartMode_Object = MibTableColumn
tlpUpsConfigAcPresentStartMode = _TlpUpsConfigAcPresentStartMode_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 1, 1, 21),
    _TlpUpsConfigAcPresentStartMode_Type()
)
tlpUpsConfigAcPresentStartMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigAcPresentStartMode.setStatus("current")


class _TlpUpsConfigBatteryCapacityCoefficient_Type(Integer32):
    """Custom type tlpUpsConfigBatteryCapacityCoefficient based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 20),
    )


_TlpUpsConfigBatteryCapacityCoefficient_Type.__name__ = "Integer32"
_TlpUpsConfigBatteryCapacityCoefficient_Object = MibTableColumn
tlpUpsConfigBatteryCapacityCoefficient = _TlpUpsConfigBatteryCapacityCoefficient_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 1, 1, 22),
    _TlpUpsConfigBatteryCapacityCoefficient_Type()
)
tlpUpsConfigBatteryCapacityCoefficient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigBatteryCapacityCoefficient.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsConfigBatteryCapacityCoefficient.setUnits("0.1")


class _TlpUpsConfigBatteryTemperatureCompensation_Type(Integer32):
    """Custom type tlpUpsConfigBatteryTemperatureCompensation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("twoAndOneHalf", 5),
          ("three", 6),
          ("threeAndOneHalf", 7),
          ("four", 8))
    )


_TlpUpsConfigBatteryTemperatureCompensation_Type.__name__ = "Integer32"
_TlpUpsConfigBatteryTemperatureCompensation_Object = MibTableColumn
tlpUpsConfigBatteryTemperatureCompensation = _TlpUpsConfigBatteryTemperatureCompensation_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 1, 1, 23),
    _TlpUpsConfigBatteryTemperatureCompensation_Type()
)
tlpUpsConfigBatteryTemperatureCompensation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigBatteryTemperatureCompensation.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsConfigBatteryTemperatureCompensation.setUnits("mV")


class _TlpUpsConfigBatteryTimedShutdownStatus_Type(Integer32):
    """Custom type tlpUpsConfigBatteryTimedShutdownStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TlpUpsConfigBatteryTimedShutdownStatus_Type.__name__ = "Integer32"
_TlpUpsConfigBatteryTimedShutdownStatus_Object = MibTableColumn
tlpUpsConfigBatteryTimedShutdownStatus = _TlpUpsConfigBatteryTimedShutdownStatus_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 1, 1, 24),
    _TlpUpsConfigBatteryTimedShutdownStatus_Type()
)
tlpUpsConfigBatteryTimedShutdownStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigBatteryTimedShutdownStatus.setStatus("current")


class _TlpUpsConfigBatteryTimedShutdownSeconds_Type(Unsigned32):
    """Custom type tlpUpsConfigBatteryTimedShutdownSeconds based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 65534),
    )


_TlpUpsConfigBatteryTimedShutdownSeconds_Type.__name__ = "Unsigned32"
_TlpUpsConfigBatteryTimedShutdownSeconds_Object = MibTableColumn
tlpUpsConfigBatteryTimedShutdownSeconds = _TlpUpsConfigBatteryTimedShutdownSeconds_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 1, 1, 25),
    _TlpUpsConfigBatteryTimedShutdownSeconds_Type()
)
tlpUpsConfigBatteryTimedShutdownSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigBatteryTimedShutdownSeconds.setStatus("current")


class _TlpUpsConfigBatteryMinCapacityToRestart_Type(Integer32):
    """Custom type tlpUpsConfigBatteryMinCapacityToRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 90),
    )


_TlpUpsConfigBatteryMinCapacityToRestart_Type.__name__ = "Integer32"
_TlpUpsConfigBatteryMinCapacityToRestart_Object = MibTableColumn
tlpUpsConfigBatteryMinCapacityToRestart = _TlpUpsConfigBatteryMinCapacityToRestart_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 1, 1, 26),
    _TlpUpsConfigBatteryMinCapacityToRestart_Type()
)
tlpUpsConfigBatteryMinCapacityToRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigBatteryMinCapacityToRestart.setStatus("current")


class _TlpUpsConfigShutdownCompletionBehavior_Type(Integer32):
    """Custom type tlpUpsConfigShutdownCompletionBehavior based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("complete", 0),
          ("cancel", 1))
    )


_TlpUpsConfigShutdownCompletionBehavior_Type.__name__ = "Integer32"
_TlpUpsConfigShutdownCompletionBehavior_Object = MibTableColumn
tlpUpsConfigShutdownCompletionBehavior = _TlpUpsConfigShutdownCompletionBehavior_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 1, 1, 27),
    _TlpUpsConfigShutdownCompletionBehavior_Type()
)
tlpUpsConfigShutdownCompletionBehavior.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigShutdownCompletionBehavior.setStatus("current")


class _TlpUpsConfigEmergencyPowerOff_Type(Integer32):
    """Custom type tlpUpsConfigEmergencyPowerOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TlpUpsConfigEmergencyPowerOff_Type.__name__ = "Integer32"
_TlpUpsConfigEmergencyPowerOff_Object = MibTableColumn
tlpUpsConfigEmergencyPowerOff = _TlpUpsConfigEmergencyPowerOff_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 1, 1, 28),
    _TlpUpsConfigEmergencyPowerOff_Type()
)
tlpUpsConfigEmergencyPowerOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigEmergencyPowerOff.setStatus("current")


class _TlpUpsConfigEnergySavingSetting_Type(Integer32):
    """Custom type tlpUpsConfigEnergySavingSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TlpUpsConfigEnergySavingSetting_Type.__name__ = "Integer32"
_TlpUpsConfigEnergySavingSetting_Object = MibTableColumn
tlpUpsConfigEnergySavingSetting = _TlpUpsConfigEnergySavingSetting_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 1, 1, 29),
    _TlpUpsConfigEnergySavingSetting_Type()
)
tlpUpsConfigEnergySavingSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigEnergySavingSetting.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsConfigEnergySavingSetting.setUnits("percent")


class _TlpUpsConfigFrequencyConvertMode_Type(Integer32):
    """Custom type tlpUpsConfigFrequencyConvertMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TlpUpsConfigFrequencyConvertMode_Type.__name__ = "Integer32"
_TlpUpsConfigFrequencyConvertMode_Object = MibTableColumn
tlpUpsConfigFrequencyConvertMode = _TlpUpsConfigFrequencyConvertMode_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 1, 1, 30),
    _TlpUpsConfigFrequencyConvertMode_Type()
)
tlpUpsConfigFrequencyConvertMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigFrequencyConvertMode.setStatus("current")


class _TlpUpsConfigBatteryCapacityConfiguration_Type(Integer32):
    """Custom type tlpUpsConfigBatteryCapacityConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(7, 100),
    )


_TlpUpsConfigBatteryCapacityConfiguration_Type.__name__ = "Integer32"
_TlpUpsConfigBatteryCapacityConfiguration_Object = MibTableColumn
tlpUpsConfigBatteryCapacityConfiguration = _TlpUpsConfigBatteryCapacityConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 1, 1, 31),
    _TlpUpsConfigBatteryCapacityConfiguration_Type()
)
tlpUpsConfigBatteryCapacityConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigBatteryCapacityConfiguration.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsConfigBatteryCapacityConfiguration.setUnits("AH")


class _TlpUpsConfigAutoBatteryTestMinutes_Type(Integer32):
    """Custom type tlpUpsConfigAutoBatteryTestMinutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TlpUpsConfigAutoBatteryTestMinutes_Type.__name__ = "Integer32"
_TlpUpsConfigAutoBatteryTestMinutes_Object = MibTableColumn
tlpUpsConfigAutoBatteryTestMinutes = _TlpUpsConfigAutoBatteryTestMinutes_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 1, 1, 32),
    _TlpUpsConfigAutoBatteryTestMinutes_Type()
)
tlpUpsConfigAutoBatteryTestMinutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigAutoBatteryTestMinutes.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsConfigAutoBatteryTestMinutes.setUnits("minutes")


class _TlpUpsConfigMaxBatteryChargerCurrent_Type(Integer32):
    """Custom type tlpUpsConfigMaxBatteryChargerCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TlpUpsConfigMaxBatteryChargerCurrent_Type.__name__ = "Integer32"
_TlpUpsConfigMaxBatteryChargerCurrent_Object = MibTableColumn
tlpUpsConfigMaxBatteryChargerCurrent = _TlpUpsConfigMaxBatteryChargerCurrent_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 1, 1, 33),
    _TlpUpsConfigMaxBatteryChargerCurrent_Type()
)
tlpUpsConfigMaxBatteryChargerCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigMaxBatteryChargerCurrent.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsConfigMaxBatteryChargerCurrent.setUnits("Amps")
_TlpUpsConfigAutoRestartTable_Object = MibTable
tlpUpsConfigAutoRestartTable = _TlpUpsConfigAutoRestartTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 2)
)
if mibBuilder.loadTexts:
    tlpUpsConfigAutoRestartTable.setStatus("current")
_TlpUpsConfigAutoRestartEntry_Object = MibTableRow
tlpUpsConfigAutoRestartEntry = _TlpUpsConfigAutoRestartEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 2, 1)
)
tlpUpsConfigAutoRestartEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpUpsConfigAutoRestartEntry.setStatus("current")


class _TlpUpsConfigAutoRestartInverterShutdown_Type(Integer32):
    """Custom type tlpUpsConfigAutoRestartInverterShutdown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TlpUpsConfigAutoRestartInverterShutdown_Type.__name__ = "Integer32"
_TlpUpsConfigAutoRestartInverterShutdown_Object = MibTableColumn
tlpUpsConfigAutoRestartInverterShutdown = _TlpUpsConfigAutoRestartInverterShutdown_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 2, 1, 1),
    _TlpUpsConfigAutoRestartInverterShutdown_Type()
)
tlpUpsConfigAutoRestartInverterShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigAutoRestartInverterShutdown.setStatus("current")


class _TlpUpsConfigAutoRestartDelayedWakeup_Type(Integer32):
    """Custom type tlpUpsConfigAutoRestartDelayedWakeup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TlpUpsConfigAutoRestartDelayedWakeup_Type.__name__ = "Integer32"
_TlpUpsConfigAutoRestartDelayedWakeup_Object = MibTableColumn
tlpUpsConfigAutoRestartDelayedWakeup = _TlpUpsConfigAutoRestartDelayedWakeup_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 2, 1, 2),
    _TlpUpsConfigAutoRestartDelayedWakeup_Type()
)
tlpUpsConfigAutoRestartDelayedWakeup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigAutoRestartDelayedWakeup.setStatus("current")


class _TlpUpsConfigAutoRestartLowVoltageCutoff_Type(Integer32):
    """Custom type tlpUpsConfigAutoRestartLowVoltageCutoff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TlpUpsConfigAutoRestartLowVoltageCutoff_Type.__name__ = "Integer32"
_TlpUpsConfigAutoRestartLowVoltageCutoff_Object = MibTableColumn
tlpUpsConfigAutoRestartLowVoltageCutoff = _TlpUpsConfigAutoRestartLowVoltageCutoff_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 2, 1, 3),
    _TlpUpsConfigAutoRestartLowVoltageCutoff_Type()
)
tlpUpsConfigAutoRestartLowVoltageCutoff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigAutoRestartLowVoltageCutoff.setStatus("current")


class _TlpUpsConfigAutoRestartOverLoad_Type(Integer32):
    """Custom type tlpUpsConfigAutoRestartOverLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TlpUpsConfigAutoRestartOverLoad_Type.__name__ = "Integer32"
_TlpUpsConfigAutoRestartOverLoad_Object = MibTableColumn
tlpUpsConfigAutoRestartOverLoad = _TlpUpsConfigAutoRestartOverLoad_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 2, 1, 4),
    _TlpUpsConfigAutoRestartOverLoad_Type()
)
tlpUpsConfigAutoRestartOverLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigAutoRestartOverLoad.setStatus("current")


class _TlpUpsConfigAutoRestartOverTemperature_Type(Integer32):
    """Custom type tlpUpsConfigAutoRestartOverTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TlpUpsConfigAutoRestartOverTemperature_Type.__name__ = "Integer32"
_TlpUpsConfigAutoRestartOverTemperature_Object = MibTableColumn
tlpUpsConfigAutoRestartOverTemperature = _TlpUpsConfigAutoRestartOverTemperature_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 2, 1, 5),
    _TlpUpsConfigAutoRestartOverTemperature_Type()
)
tlpUpsConfigAutoRestartOverTemperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigAutoRestartOverTemperature.setStatus("current")
_TlpUpsConfigThresholdTable_Object = MibTable
tlpUpsConfigThresholdTable = _TlpUpsConfigThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 3)
)
if mibBuilder.loadTexts:
    tlpUpsConfigThresholdTable.setStatus("current")
_TlpUpsConfigThresholdEntry_Object = MibTableRow
tlpUpsConfigThresholdEntry = _TlpUpsConfigThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 3, 1)
)
tlpUpsConfigThresholdEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpUpsConfigThresholdEntry.setStatus("current")
_TlpUpsConfigBatteryAgeThreshold_Type = Unsigned32
_TlpUpsConfigBatteryAgeThreshold_Object = MibTableColumn
tlpUpsConfigBatteryAgeThreshold = _TlpUpsConfigBatteryAgeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 3, 1, 1),
    _TlpUpsConfigBatteryAgeThreshold_Type()
)
tlpUpsConfigBatteryAgeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigBatteryAgeThreshold.setStatus("deprecated")
if mibBuilder.loadTexts:
    tlpUpsConfigBatteryAgeThreshold.setUnits("months")


class _TlpUpsConfigLowBatteryThreshold_Type(Integer32):
    """Custom type tlpUpsConfigLowBatteryThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(11, 90),
    )


_TlpUpsConfigLowBatteryThreshold_Type.__name__ = "Integer32"
_TlpUpsConfigLowBatteryThreshold_Object = MibTableColumn
tlpUpsConfigLowBatteryThreshold = _TlpUpsConfigLowBatteryThreshold_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 3, 1, 2),
    _TlpUpsConfigLowBatteryThreshold_Type()
)
tlpUpsConfigLowBatteryThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigLowBatteryThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsConfigLowBatteryThreshold.setUnits("percent")
_TlpUpsConfigLowBatteryTime_Type = Unsigned32
_TlpUpsConfigLowBatteryTime_Object = MibTableColumn
tlpUpsConfigLowBatteryTime = _TlpUpsConfigLowBatteryTime_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 3, 1, 3),
    _TlpUpsConfigLowBatteryTime_Type()
)
tlpUpsConfigLowBatteryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigLowBatteryTime.setStatus("deprecated")
if mibBuilder.loadTexts:
    tlpUpsConfigLowBatteryTime.setUnits("seconds")


class _TlpUpsConfigOverLoadThreshold_Type(Integer32):
    """Custom type tlpUpsConfigOverLoadThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 105),
    )


_TlpUpsConfigOverLoadThreshold_Type.__name__ = "Integer32"
_TlpUpsConfigOverLoadThreshold_Object = MibTableColumn
tlpUpsConfigOverLoadThreshold = _TlpUpsConfigOverLoadThreshold_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 3, 1, 4),
    _TlpUpsConfigOverLoadThreshold_Type()
)
tlpUpsConfigOverLoadThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigOverLoadThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsConfigOverLoadThreshold.setUnits("percent")


class _TlpUpsConfigLowBatteryCriticalThreshold_Type(Integer32):
    """Custom type tlpUpsConfigLowBatteryCriticalThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 89),
    )


_TlpUpsConfigLowBatteryCriticalThreshold_Type.__name__ = "Integer32"
_TlpUpsConfigLowBatteryCriticalThreshold_Object = MibTableColumn
tlpUpsConfigLowBatteryCriticalThreshold = _TlpUpsConfigLowBatteryCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 3, 1, 5),
    _TlpUpsConfigLowBatteryCriticalThreshold_Type()
)
tlpUpsConfigLowBatteryCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigLowBatteryCriticalThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsConfigLowBatteryCriticalThreshold.setUnits("percent")


class _TlpUpsConfigBatteryAgeWarningThreshold_Type(Integer32):
    """Custom type tlpUpsConfigBatteryAgeWarningThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_TlpUpsConfigBatteryAgeWarningThreshold_Type.__name__ = "Integer32"
_TlpUpsConfigBatteryAgeWarningThreshold_Object = MibTableColumn
tlpUpsConfigBatteryAgeWarningThreshold = _TlpUpsConfigBatteryAgeWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 3, 1, 6),
    _TlpUpsConfigBatteryAgeWarningThreshold_Type()
)
tlpUpsConfigBatteryAgeWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigBatteryAgeWarningThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsConfigBatteryAgeWarningThreshold.setUnits("0.1 years")


class _TlpUpsConfigBatteryAgeCriticalThreshold_Type(Integer32):
    """Custom type tlpUpsConfigBatteryAgeCriticalThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_TlpUpsConfigBatteryAgeCriticalThreshold_Type.__name__ = "Integer32"
_TlpUpsConfigBatteryAgeCriticalThreshold_Object = MibTableColumn
tlpUpsConfigBatteryAgeCriticalThreshold = _TlpUpsConfigBatteryAgeCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 3, 1, 7),
    _TlpUpsConfigBatteryAgeCriticalThreshold_Type()
)
tlpUpsConfigBatteryAgeCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigBatteryAgeCriticalThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsConfigBatteryAgeCriticalThreshold.setUnits("0.1 years")
_TlpUpsConfigLowBatteryRuntimeWarningThreshold_Type = Unsigned32
_TlpUpsConfigLowBatteryRuntimeWarningThreshold_Object = MibTableColumn
tlpUpsConfigLowBatteryRuntimeWarningThreshold = _TlpUpsConfigLowBatteryRuntimeWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 3, 1, 8),
    _TlpUpsConfigLowBatteryRuntimeWarningThreshold_Type()
)
tlpUpsConfigLowBatteryRuntimeWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigLowBatteryRuntimeWarningThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsConfigLowBatteryRuntimeWarningThreshold.setUnits("minutes")
_TlpUpsConfigLowBatteryRuntimeCriticalThreshold_Type = Unsigned32
_TlpUpsConfigLowBatteryRuntimeCriticalThreshold_Object = MibTableColumn
tlpUpsConfigLowBatteryRuntimeCriticalThreshold = _TlpUpsConfigLowBatteryRuntimeCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 3, 1, 9),
    _TlpUpsConfigLowBatteryRuntimeCriticalThreshold_Type()
)
tlpUpsConfigLowBatteryRuntimeCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigLowBatteryRuntimeCriticalThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsConfigLowBatteryRuntimeCriticalThreshold.setUnits("minutes")
_TlpUpsConfigVoltageTable_Object = MibTable
tlpUpsConfigVoltageTable = _TlpUpsConfigVoltageTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 4)
)
if mibBuilder.loadTexts:
    tlpUpsConfigVoltageTable.setStatus("current")
_TlpUpsConfigVoltageEntry_Object = MibTableRow
tlpUpsConfigVoltageEntry = _TlpUpsConfigVoltageEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 4, 1)
)
tlpUpsConfigVoltageEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpUpsConfigVoltageEntry.setStatus("current")
_TlpUpsConfigHighVoltageTransfer_Type = Unsigned32
_TlpUpsConfigHighVoltageTransfer_Object = MibTableColumn
tlpUpsConfigHighVoltageTransfer = _TlpUpsConfigHighVoltageTransfer_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 4, 1, 1),
    _TlpUpsConfigHighVoltageTransfer_Type()
)
tlpUpsConfigHighVoltageTransfer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigHighVoltageTransfer.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsConfigHighVoltageTransfer.setUnits("0.1 Volts")
_TlpUpsConfigHighVoltageResetTolerance_Type = Unsigned32
_TlpUpsConfigHighVoltageResetTolerance_Object = MibTableColumn
tlpUpsConfigHighVoltageResetTolerance = _TlpUpsConfigHighVoltageResetTolerance_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 4, 1, 2),
    _TlpUpsConfigHighVoltageResetTolerance_Type()
)
tlpUpsConfigHighVoltageResetTolerance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigHighVoltageResetTolerance.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsConfigHighVoltageResetTolerance.setUnits("Volts")
_TlpUpsConfigHighVoltageReset_Type = Unsigned32
_TlpUpsConfigHighVoltageReset_Object = MibTableColumn
tlpUpsConfigHighVoltageReset = _TlpUpsConfigHighVoltageReset_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 4, 1, 3),
    _TlpUpsConfigHighVoltageReset_Type()
)
tlpUpsConfigHighVoltageReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigHighVoltageReset.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsConfigHighVoltageReset.setUnits("0.1 Volts")
_TlpUpsConfigLowVoltageTransfer_Type = Unsigned32
_TlpUpsConfigLowVoltageTransfer_Object = MibTableColumn
tlpUpsConfigLowVoltageTransfer = _TlpUpsConfigLowVoltageTransfer_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 4, 1, 4),
    _TlpUpsConfigLowVoltageTransfer_Type()
)
tlpUpsConfigLowVoltageTransfer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigLowVoltageTransfer.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsConfigLowVoltageTransfer.setUnits("0.1 Volts")
_TlpUpsConfigLowVoltageResetTolerance_Type = Unsigned32
_TlpUpsConfigLowVoltageResetTolerance_Object = MibTableColumn
tlpUpsConfigLowVoltageResetTolerance = _TlpUpsConfigLowVoltageResetTolerance_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 4, 1, 5),
    _TlpUpsConfigLowVoltageResetTolerance_Type()
)
tlpUpsConfigLowVoltageResetTolerance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigLowVoltageResetTolerance.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsConfigLowVoltageResetTolerance.setUnits("Volts")
_TlpUpsConfigLowVoltageReset_Type = Unsigned32
_TlpUpsConfigLowVoltageReset_Object = MibTableColumn
tlpUpsConfigLowVoltageReset = _TlpUpsConfigLowVoltageReset_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 4, 1, 6),
    _TlpUpsConfigLowVoltageReset_Type()
)
tlpUpsConfigLowVoltageReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigLowVoltageReset.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsConfigLowVoltageReset.setUnits("0.1 Volts")
_TlpUpsConfigContact_ObjectIdentity = ObjectIdentity
tlpUpsConfigContact = _TlpUpsConfigContact_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 5)
)
_TlpUpsConfigContactTable_Object = MibTable
tlpUpsConfigContactTable = _TlpUpsConfigContactTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 5, 1)
)
if mibBuilder.loadTexts:
    tlpUpsConfigContactTable.setStatus("current")
_TlpUpsConfigContactEntry_Object = MibTableRow
tlpUpsConfigContactEntry = _TlpUpsConfigContactEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 5, 1, 1)
)
tlpUpsConfigContactEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpUpsConfigContactEntry.setStatus("current")


class _TlpUpsConfigOutputContactBackupTimer_Type(Unsigned32):
    """Custom type tlpUpsConfigOutputContactBackupTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 480),
    )


_TlpUpsConfigOutputContactBackupTimer_Type.__name__ = "Unsigned32"
_TlpUpsConfigOutputContactBackupTimer_Object = MibTableColumn
tlpUpsConfigOutputContactBackupTimer = _TlpUpsConfigOutputContactBackupTimer_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 5, 1, 1, 1),
    _TlpUpsConfigOutputContactBackupTimer_Type()
)
tlpUpsConfigOutputContactBackupTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigOutputContactBackupTimer.setStatus("current")
_TlpUpsConfigInputContactTable_Object = MibTable
tlpUpsConfigInputContactTable = _TlpUpsConfigInputContactTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 5, 2)
)
if mibBuilder.loadTexts:
    tlpUpsConfigInputContactTable.setStatus("current")
_TlpUpsConfigInputContactEntry_Object = MibTableRow
tlpUpsConfigInputContactEntry = _TlpUpsConfigInputContactEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 5, 2, 1)
)
tlpUpsConfigInputContactEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpUpsConfigInputContactIndex"),
)
if mibBuilder.loadTexts:
    tlpUpsConfigInputContactEntry.setStatus("current")
_TlpUpsConfigInputContactIndex_Type = Unsigned32
_TlpUpsConfigInputContactIndex_Object = MibTableColumn
tlpUpsConfigInputContactIndex = _TlpUpsConfigInputContactIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 5, 2, 1, 1),
    _TlpUpsConfigInputContactIndex_Type()
)
tlpUpsConfigInputContactIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsConfigInputContactIndex.setStatus("current")


class _TlpUpsConfigInputContactSetup_Type(Integer32):
    """Custom type tlpUpsConfigInputContactSetup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("userDefined", 0),
          ("externalAlarm", 1),
          ("externalBatteryAlarm", 2),
          ("externalFanFailed", 3),
          ("doorUnlock", 4))
    )


_TlpUpsConfigInputContactSetup_Type.__name__ = "Integer32"
_TlpUpsConfigInputContactSetup_Object = MibTableColumn
tlpUpsConfigInputContactSetup = _TlpUpsConfigInputContactSetup_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 5, 2, 1, 2),
    _TlpUpsConfigInputContactSetup_Type()
)
tlpUpsConfigInputContactSetup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigInputContactSetup.setStatus("current")
_TlpUpsConfigOutputContactTable_Object = MibTable
tlpUpsConfigOutputContactTable = _TlpUpsConfigOutputContactTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 5, 3)
)
if mibBuilder.loadTexts:
    tlpUpsConfigOutputContactTable.setStatus("current")
_TlpUpsConfigOutputContactEntry_Object = MibTableRow
tlpUpsConfigOutputContactEntry = _TlpUpsConfigOutputContactEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 5, 3, 1)
)
tlpUpsConfigOutputContactEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpUpsConfigOutputContactIndex"),
)
if mibBuilder.loadTexts:
    tlpUpsConfigOutputContactEntry.setStatus("current")
_TlpUpsConfigOutputContactIndex_Type = Unsigned32
_TlpUpsConfigOutputContactIndex_Object = MibTableColumn
tlpUpsConfigOutputContactIndex = _TlpUpsConfigOutputContactIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 5, 3, 1, 1),
    _TlpUpsConfigOutputContactIndex_Type()
)
tlpUpsConfigOutputContactIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsConfigOutputContactIndex.setStatus("current")


class _TlpUpsConfigOutputContactSetup_Type(Integer32):
    """Custom type tlpUpsConfigOutputContactSetup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("onBattery", 1),
          ("batteryLow", 2),
          ("timer", 3),
          ("alarm", 4),
          ("fault", 5),
          ("outputOff", 6))
    )


_TlpUpsConfigOutputContactSetup_Type.__name__ = "Integer32"
_TlpUpsConfigOutputContactSetup_Object = MibTableColumn
tlpUpsConfigOutputContactSetup = _TlpUpsConfigOutputContactSetup_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 5, 3, 1, 2),
    _TlpUpsConfigOutputContactSetup_Type()
)
tlpUpsConfigOutputContactSetup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigOutputContactSetup.setStatus("current")
_TlpUpsConfigDb9_ObjectIdentity = ObjectIdentity
tlpUpsConfigDb9 = _TlpUpsConfigDb9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 6)
)
_TlpUpsConfigDb9InputTable_Object = MibTable
tlpUpsConfigDb9InputTable = _TlpUpsConfigDb9InputTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 6, 1)
)
if mibBuilder.loadTexts:
    tlpUpsConfigDb9InputTable.setStatus("current")
_TlpUpsConfigDb9InputEntry_Object = MibTableRow
tlpUpsConfigDb9InputEntry = _TlpUpsConfigDb9InputEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 6, 1, 1)
)
tlpUpsConfigDb9InputEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpUpsConfigDb9InputEntry.setStatus("current")


class _TlpUpsConfigDb9InputPins3and9_Type(Integer32):
    """Custom type tlpUpsConfigDb9InputPins3and9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("shutdown", 0),
          ("outputOff", 1),
          ("reboot", 2),
          ("outputOn", 3),
          ("powerToggle", 4))
    )


_TlpUpsConfigDb9InputPins3and9_Type.__name__ = "Integer32"
_TlpUpsConfigDb9InputPins3and9_Object = MibTableColumn
tlpUpsConfigDb9InputPins3and9 = _TlpUpsConfigDb9InputPins3and9_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 6, 1, 1, 1),
    _TlpUpsConfigDb9InputPins3and9_Type()
)
tlpUpsConfigDb9InputPins3and9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigDb9InputPins3and9.setStatus("current")
_TlpUpsConfigDb9OutputTable_Object = MibTable
tlpUpsConfigDb9OutputTable = _TlpUpsConfigDb9OutputTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 6, 2)
)
if mibBuilder.loadTexts:
    tlpUpsConfigDb9OutputTable.setStatus("current")
_TlpUpsConfigDb9OutputEntry_Object = MibTableRow
tlpUpsConfigDb9OutputEntry = _TlpUpsConfigDb9OutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 6, 2, 1)
)
tlpUpsConfigDb9OutputEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpUpsConfigDb9OutputEntry.setStatus("current")


class _TlpUpsConfigDb9OutputPins1and5_Type(Integer32):
    """Custom type tlpUpsConfigDb9OutputPins1and5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("onBattery", 0),
          ("onBypass", 1),
          ("outputOn", 2),
          ("lowBattery", 3),
          ("summaryAlarm", 4))
    )


_TlpUpsConfigDb9OutputPins1and5_Type.__name__ = "Integer32"
_TlpUpsConfigDb9OutputPins1and5_Object = MibTableColumn
tlpUpsConfigDb9OutputPins1and5 = _TlpUpsConfigDb9OutputPins1and5_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 6, 2, 1, 1),
    _TlpUpsConfigDb9OutputPins1and5_Type()
)
tlpUpsConfigDb9OutputPins1and5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigDb9OutputPins1and5.setStatus("current")


class _TlpUpsConfigDb9OutputPins8and5_Type(Integer32):
    """Custom type tlpUpsConfigDb9OutputPins8and5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("onBattery", 0),
          ("onBypass", 1),
          ("outputOn", 2),
          ("lowBattery", 3),
          ("summaryAlarm", 4))
    )


_TlpUpsConfigDb9OutputPins8and5_Type.__name__ = "Integer32"
_TlpUpsConfigDb9OutputPins8and5_Object = MibTableColumn
tlpUpsConfigDb9OutputPins8and5 = _TlpUpsConfigDb9OutputPins8and5_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 6, 2, 1, 2),
    _TlpUpsConfigDb9OutputPins8and5_Type()
)
tlpUpsConfigDb9OutputPins8and5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigDb9OutputPins8and5.setStatus("current")
_TlpUpsConfigOutputPhaseThresholdTable_Object = MibTable
tlpUpsConfigOutputPhaseThresholdTable = _TlpUpsConfigOutputPhaseThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 7)
)
if mibBuilder.loadTexts:
    tlpUpsConfigOutputPhaseThresholdTable.setStatus("current")
_TlpUpsConfigOutputPhaseThresholdEntry_Object = MibTableRow
tlpUpsConfigOutputPhaseThresholdEntry = _TlpUpsConfigOutputPhaseThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 7, 1)
)
tlpUpsConfigOutputPhaseThresholdEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpUpsOutputLineIndex"),
)
if mibBuilder.loadTexts:
    tlpUpsConfigOutputPhaseThresholdEntry.setStatus("current")
_TlpUpsConfigOutputCurrentThresholdTolerance_Type = Unsigned32
_TlpUpsConfigOutputCurrentThresholdTolerance_Object = MibTableColumn
tlpUpsConfigOutputCurrentThresholdTolerance = _TlpUpsConfigOutputCurrentThresholdTolerance_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 7, 1, 1),
    _TlpUpsConfigOutputCurrentThresholdTolerance_Type()
)
tlpUpsConfigOutputCurrentThresholdTolerance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigOutputCurrentThresholdTolerance.setStatus("deprecated")
if mibBuilder.loadTexts:
    tlpUpsConfigOutputCurrentThresholdTolerance.setUnits("0.1 Amps")
_TlpUpsConfigOutputCurrentHighThreshold_Type = Unsigned32
_TlpUpsConfigOutputCurrentHighThreshold_Object = MibTableColumn
tlpUpsConfigOutputCurrentHighThreshold = _TlpUpsConfigOutputCurrentHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 7, 1, 2),
    _TlpUpsConfigOutputCurrentHighThreshold_Type()
)
tlpUpsConfigOutputCurrentHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigOutputCurrentHighThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsConfigOutputCurrentHighThreshold.setUnits("0.1 Amps")
_TlpUpsConfigOutputCurrentLowThreshold_Type = Unsigned32
_TlpUpsConfigOutputCurrentLowThreshold_Object = MibTableColumn
tlpUpsConfigOutputCurrentLowThreshold = _TlpUpsConfigOutputCurrentLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 7, 1, 3),
    _TlpUpsConfigOutputCurrentLowThreshold_Type()
)
tlpUpsConfigOutputCurrentLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigOutputCurrentLowThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsConfigOutputCurrentLowThreshold.setUnits("0.1 Amps")
_TlpUpsConfigOutputVoltageThresholdTolerance_Type = Unsigned32
_TlpUpsConfigOutputVoltageThresholdTolerance_Object = MibTableColumn
tlpUpsConfigOutputVoltageThresholdTolerance = _TlpUpsConfigOutputVoltageThresholdTolerance_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 7, 1, 4),
    _TlpUpsConfigOutputVoltageThresholdTolerance_Type()
)
tlpUpsConfigOutputVoltageThresholdTolerance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigOutputVoltageThresholdTolerance.setStatus("deprecated")
if mibBuilder.loadTexts:
    tlpUpsConfigOutputVoltageThresholdTolerance.setUnits("0.1 Amps")
_TlpUpsConfigOutputVoltageHighCriticalThreshold_Type = Unsigned32
_TlpUpsConfigOutputVoltageHighCriticalThreshold_Object = MibTableColumn
tlpUpsConfigOutputVoltageHighCriticalThreshold = _TlpUpsConfigOutputVoltageHighCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 7, 1, 5),
    _TlpUpsConfigOutputVoltageHighCriticalThreshold_Type()
)
tlpUpsConfigOutputVoltageHighCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigOutputVoltageHighCriticalThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsConfigOutputVoltageHighCriticalThreshold.setUnits("0.1 Volts")
_TlpUpsConfigOutputVoltageHighWarningThreshold_Type = Unsigned32
_TlpUpsConfigOutputVoltageHighWarningThreshold_Object = MibTableColumn
tlpUpsConfigOutputVoltageHighWarningThreshold = _TlpUpsConfigOutputVoltageHighWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 7, 1, 6),
    _TlpUpsConfigOutputVoltageHighWarningThreshold_Type()
)
tlpUpsConfigOutputVoltageHighWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigOutputVoltageHighWarningThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsConfigOutputVoltageHighWarningThreshold.setUnits("0.1 Volts")
_TlpUpsConfigOutputVoltageLowWarningThreshold_Type = Unsigned32
_TlpUpsConfigOutputVoltageLowWarningThreshold_Object = MibTableColumn
tlpUpsConfigOutputVoltageLowWarningThreshold = _TlpUpsConfigOutputVoltageLowWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 7, 1, 7),
    _TlpUpsConfigOutputVoltageLowWarningThreshold_Type()
)
tlpUpsConfigOutputVoltageLowWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigOutputVoltageLowWarningThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsConfigOutputVoltageLowWarningThreshold.setUnits("0.1 Volts")
_TlpUpsConfigOutputVoltageLowCriticalThreshold_Type = Unsigned32
_TlpUpsConfigOutputVoltageLowCriticalThreshold_Object = MibTableColumn
tlpUpsConfigOutputVoltageLowCriticalThreshold = _TlpUpsConfigOutputVoltageLowCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 7, 1, 8),
    _TlpUpsConfigOutputVoltageLowCriticalThreshold_Type()
)
tlpUpsConfigOutputVoltageLowCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigOutputVoltageLowCriticalThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsConfigOutputVoltageLowCriticalThreshold.setUnits("0.1 Volts")
_TlpUpsConfigOutputUtilizationThresholdTolerance_Type = Unsigned32
_TlpUpsConfigOutputUtilizationThresholdTolerance_Object = MibTableColumn
tlpUpsConfigOutputUtilizationThresholdTolerance = _TlpUpsConfigOutputUtilizationThresholdTolerance_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 7, 1, 9),
    _TlpUpsConfigOutputUtilizationThresholdTolerance_Type()
)
tlpUpsConfigOutputUtilizationThresholdTolerance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigOutputUtilizationThresholdTolerance.setStatus("deprecated")
if mibBuilder.loadTexts:
    tlpUpsConfigOutputUtilizationThresholdTolerance.setUnits("0.1 Amps")


class _TlpUpsConfigOutputUtilizationWarningThreshold_Type(Integer32):
    """Custom type tlpUpsConfigOutputUtilizationWarningThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 105),
    )


_TlpUpsConfigOutputUtilizationWarningThreshold_Type.__name__ = "Integer32"
_TlpUpsConfigOutputUtilizationWarningThreshold_Object = MibTableColumn
tlpUpsConfigOutputUtilizationWarningThreshold = _TlpUpsConfigOutputUtilizationWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 7, 1, 10),
    _TlpUpsConfigOutputUtilizationWarningThreshold_Type()
)
tlpUpsConfigOutputUtilizationWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigOutputUtilizationWarningThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsConfigOutputUtilizationWarningThreshold.setUnits("percent")
_TlpUpsConfigInputPhaseThresholdTable_Object = MibTable
tlpUpsConfigInputPhaseThresholdTable = _TlpUpsConfigInputPhaseThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 8)
)
if mibBuilder.loadTexts:
    tlpUpsConfigInputPhaseThresholdTable.setStatus("current")
_TlpUpsConfigInputPhaseThresholdEntry_Object = MibTableRow
tlpUpsConfigInputPhaseThresholdEntry = _TlpUpsConfigInputPhaseThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 8, 1)
)
tlpUpsConfigInputPhaseThresholdEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpUpsInputPhaseIndex"),
)
if mibBuilder.loadTexts:
    tlpUpsConfigInputPhaseThresholdEntry.setStatus("current")
_TlpUpsConfigInputVoltageThresholdTolerance_Type = Unsigned32
_TlpUpsConfigInputVoltageThresholdTolerance_Object = MibTableColumn
tlpUpsConfigInputVoltageThresholdTolerance = _TlpUpsConfigInputVoltageThresholdTolerance_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 8, 1, 1),
    _TlpUpsConfigInputVoltageThresholdTolerance_Type()
)
tlpUpsConfigInputVoltageThresholdTolerance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigInputVoltageThresholdTolerance.setStatus("deprecated")
if mibBuilder.loadTexts:
    tlpUpsConfigInputVoltageThresholdTolerance.setUnits("0.1 Amps")
_TlpUpsConfigInputVoltageHighCriticalThreshold_Type = Unsigned32
_TlpUpsConfigInputVoltageHighCriticalThreshold_Object = MibTableColumn
tlpUpsConfigInputVoltageHighCriticalThreshold = _TlpUpsConfigInputVoltageHighCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 8, 1, 2),
    _TlpUpsConfigInputVoltageHighCriticalThreshold_Type()
)
tlpUpsConfigInputVoltageHighCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigInputVoltageHighCriticalThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsConfigInputVoltageHighCriticalThreshold.setUnits("0.1 Volts")
_TlpUpsConfigInputVoltageHighWarningThreshold_Type = Unsigned32
_TlpUpsConfigInputVoltageHighWarningThreshold_Object = MibTableColumn
tlpUpsConfigInputVoltageHighWarningThreshold = _TlpUpsConfigInputVoltageHighWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 8, 1, 3),
    _TlpUpsConfigInputVoltageHighWarningThreshold_Type()
)
tlpUpsConfigInputVoltageHighWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigInputVoltageHighWarningThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsConfigInputVoltageHighWarningThreshold.setUnits("0.1 Volts")
_TlpUpsConfigInputVoltageLowWarningThreshold_Type = Unsigned32
_TlpUpsConfigInputVoltageLowWarningThreshold_Object = MibTableColumn
tlpUpsConfigInputVoltageLowWarningThreshold = _TlpUpsConfigInputVoltageLowWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 8, 1, 4),
    _TlpUpsConfigInputVoltageLowWarningThreshold_Type()
)
tlpUpsConfigInputVoltageLowWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigInputVoltageLowWarningThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsConfigInputVoltageLowWarningThreshold.setUnits("0.1 Volts")
_TlpUpsConfigInputVoltageLowCriticalThreshold_Type = Unsigned32
_TlpUpsConfigInputVoltageLowCriticalThreshold_Object = MibTableColumn
tlpUpsConfigInputVoltageLowCriticalThreshold = _TlpUpsConfigInputVoltageLowCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 8, 1, 5),
    _TlpUpsConfigInputVoltageLowCriticalThreshold_Type()
)
tlpUpsConfigInputVoltageLowCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigInputVoltageLowCriticalThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsConfigInputVoltageLowCriticalThreshold.setUnits("0.1 Volts")
_TlpUpsConfigTemperatureFahrenheitTable_Object = MibTable
tlpUpsConfigTemperatureFahrenheitTable = _TlpUpsConfigTemperatureFahrenheitTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 9)
)
if mibBuilder.loadTexts:
    tlpUpsConfigTemperatureFahrenheitTable.setStatus("current")
_TlpUpsConfigTemperatureFahrenheitEntry_Object = MibTableRow
tlpUpsConfigTemperatureFahrenheitEntry = _TlpUpsConfigTemperatureFahrenheitEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 9, 1)
)
tlpUpsConfigTemperatureFahrenheitEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpUpsConfigTemperatureFahrenheitEntry.setStatus("current")
_TlpUpsConfigExternalFanActivationTemperatureDegF_Type = Integer32
_TlpUpsConfigExternalFanActivationTemperatureDegF_Object = MibTableColumn
tlpUpsConfigExternalFanActivationTemperatureDegF = _TlpUpsConfigExternalFanActivationTemperatureDegF_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 9, 1, 1),
    _TlpUpsConfigExternalFanActivationTemperatureDegF_Type()
)
tlpUpsConfigExternalFanActivationTemperatureDegF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigExternalFanActivationTemperatureDegF.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsConfigExternalFanActivationTemperatureDegF.setUnits("0.1 degrees Fahrenheit")
_TlpUpsConfigTemperatureCelsiusTable_Object = MibTable
tlpUpsConfigTemperatureCelsiusTable = _TlpUpsConfigTemperatureCelsiusTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 10)
)
if mibBuilder.loadTexts:
    tlpUpsConfigTemperatureCelsiusTable.setStatus("current")
_TlpUpsConfigTemperatureCelsiusEntry_Object = MibTableRow
tlpUpsConfigTemperatureCelsiusEntry = _TlpUpsConfigTemperatureCelsiusEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 10, 1)
)
tlpUpsConfigTemperatureCelsiusEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpUpsConfigTemperatureCelsiusEntry.setStatus("current")
_TlpUpsConfigExternalFanActivationTemperatureDegC_Type = Integer32
_TlpUpsConfigExternalFanActivationTemperatureDegC_Object = MibTableColumn
tlpUpsConfigExternalFanActivationTemperatureDegC = _TlpUpsConfigExternalFanActivationTemperatureDegC_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 10, 1, 1),
    _TlpUpsConfigExternalFanActivationTemperatureDegC_Type()
)
tlpUpsConfigExternalFanActivationTemperatureDegC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigExternalFanActivationTemperatureDegC.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsConfigExternalFanActivationTemperatureDegC.setUnits("0.1 degrees Celsius")
_TlpPdu_ObjectIdentity = ObjectIdentity
tlpPdu = _TlpPdu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2)
)
_TlpPduIdent_ObjectIdentity = ObjectIdentity
tlpPduIdent = _TlpPduIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 1)
)
_TlpPduIdentNumPdu_Type = Unsigned32
_TlpPduIdentNumPdu_Object = MibScalar
tlpPduIdentNumPdu = _TlpPduIdentNumPdu_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 1, 1),
    _TlpPduIdentNumPdu_Type()
)
tlpPduIdentNumPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduIdentNumPdu.setStatus("current")
_TlpPduIdentTable_Object = MibTable
tlpPduIdentTable = _TlpPduIdentTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 1, 2)
)
if mibBuilder.loadTexts:
    tlpPduIdentTable.setStatus("current")
_TlpPduIdentEntry_Object = MibTableRow
tlpPduIdentEntry = _TlpPduIdentEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 1, 2, 1)
)
tlpPduIdentEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpPduIdentEntry.setStatus("current")
_TlpPduIdentNumInputs_Type = Unsigned32
_TlpPduIdentNumInputs_Object = MibTableColumn
tlpPduIdentNumInputs = _TlpPduIdentNumInputs_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 1, 2, 1, 1),
    _TlpPduIdentNumInputs_Type()
)
tlpPduIdentNumInputs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduIdentNumInputs.setStatus("current")
_TlpPduIdentNumOutputs_Type = Unsigned32
_TlpPduIdentNumOutputs_Object = MibTableColumn
tlpPduIdentNumOutputs = _TlpPduIdentNumOutputs_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 1, 2, 1, 2),
    _TlpPduIdentNumOutputs_Type()
)
tlpPduIdentNumOutputs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduIdentNumOutputs.setStatus("current")
_TlpPduIdentNumPhases_Type = Unsigned32
_TlpPduIdentNumPhases_Object = MibTableColumn
tlpPduIdentNumPhases = _TlpPduIdentNumPhases_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 1, 2, 1, 3),
    _TlpPduIdentNumPhases_Type()
)
tlpPduIdentNumPhases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduIdentNumPhases.setStatus("current")
_TlpPduIdentNumOutlets_Type = Unsigned32
_TlpPduIdentNumOutlets_Object = MibTableColumn
tlpPduIdentNumOutlets = _TlpPduIdentNumOutlets_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 1, 2, 1, 4),
    _TlpPduIdentNumOutlets_Type()
)
tlpPduIdentNumOutlets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduIdentNumOutlets.setStatus("current")
_TlpPduIdentNumOutletGroups_Type = Unsigned32
_TlpPduIdentNumOutletGroups_Object = MibTableColumn
tlpPduIdentNumOutletGroups = _TlpPduIdentNumOutletGroups_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 1, 2, 1, 5),
    _TlpPduIdentNumOutletGroups_Type()
)
tlpPduIdentNumOutletGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduIdentNumOutletGroups.setStatus("current")
_TlpPduIdentNumCircuits_Type = Unsigned32
_TlpPduIdentNumCircuits_Object = MibTableColumn
tlpPduIdentNumCircuits = _TlpPduIdentNumCircuits_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 1, 2, 1, 6),
    _TlpPduIdentNumCircuits_Type()
)
tlpPduIdentNumCircuits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduIdentNumCircuits.setStatus("current")
_TlpPduIdentNumBreakers_Type = Unsigned32
_TlpPduIdentNumBreakers_Object = MibTableColumn
tlpPduIdentNumBreakers = _TlpPduIdentNumBreakers_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 1, 2, 1, 7),
    _TlpPduIdentNumBreakers_Type()
)
tlpPduIdentNumBreakers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduIdentNumBreakers.setStatus("current")
_TlpPduIdentNumHeatsinks_Type = Unsigned32
_TlpPduIdentNumHeatsinks_Object = MibTableColumn
tlpPduIdentNumHeatsinks = _TlpPduIdentNumHeatsinks_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 1, 2, 1, 8),
    _TlpPduIdentNumHeatsinks_Type()
)
tlpPduIdentNumHeatsinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduIdentNumHeatsinks.setStatus("current")
_TlpPduSupportsTable_Object = MibTable
tlpPduSupportsTable = _TlpPduSupportsTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 1, 3)
)
if mibBuilder.loadTexts:
    tlpPduSupportsTable.setStatus("current")
_TlpPduSupportsEntry_Object = MibTableRow
tlpPduSupportsEntry = _TlpPduSupportsEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 1, 3, 1)
)
tlpPduSupportsEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpPduSupportsEntry.setStatus("current")
_TlpPduSupportsEnergywise_Type = TruthValue
_TlpPduSupportsEnergywise_Object = MibTableColumn
tlpPduSupportsEnergywise = _TlpPduSupportsEnergywise_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 1, 3, 1, 1),
    _TlpPduSupportsEnergywise_Type()
)
tlpPduSupportsEnergywise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduSupportsEnergywise.setStatus("deprecated")
_TlpPduSupportsRampShed_Type = TruthValue
_TlpPduSupportsRampShed_Object = MibTableColumn
tlpPduSupportsRampShed = _TlpPduSupportsRampShed_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 1, 3, 1, 2),
    _TlpPduSupportsRampShed_Type()
)
tlpPduSupportsRampShed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduSupportsRampShed.setStatus("current")
_TlpPduSupportsOutletGroup_Type = TruthValue
_TlpPduSupportsOutletGroup_Object = MibTableColumn
tlpPduSupportsOutletGroup = _TlpPduSupportsOutletGroup_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 1, 3, 1, 3),
    _TlpPduSupportsOutletGroup_Type()
)
tlpPduSupportsOutletGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduSupportsOutletGroup.setStatus("current")
_TlpPduSupportsOutletCurrent_Type = TruthValue
_TlpPduSupportsOutletCurrent_Object = MibTableColumn
tlpPduSupportsOutletCurrent = _TlpPduSupportsOutletCurrent_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 1, 3, 1, 4),
    _TlpPduSupportsOutletCurrent_Type()
)
tlpPduSupportsOutletCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduSupportsOutletCurrent.setStatus("current")
_TlpPduSupportsOutletVoltage_Type = TruthValue
_TlpPduSupportsOutletVoltage_Object = MibTableColumn
tlpPduSupportsOutletVoltage = _TlpPduSupportsOutletVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 1, 3, 1, 5),
    _TlpPduSupportsOutletVoltage_Type()
)
tlpPduSupportsOutletVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduSupportsOutletVoltage.setStatus("current")
_TlpPduSupportsOutletActivePower_Type = TruthValue
_TlpPduSupportsOutletActivePower_Object = MibTableColumn
tlpPduSupportsOutletActivePower = _TlpPduSupportsOutletActivePower_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 1, 3, 1, 6),
    _TlpPduSupportsOutletActivePower_Type()
)
tlpPduSupportsOutletActivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduSupportsOutletActivePower.setStatus("current")
_TlpPduDisplayTable_Object = MibTable
tlpPduDisplayTable = _TlpPduDisplayTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 1, 4)
)
if mibBuilder.loadTexts:
    tlpPduDisplayTable.setStatus("deprecated")
_TlpPduDisplayEntry_Object = MibTableRow
tlpPduDisplayEntry = _TlpPduDisplayEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 1, 4, 1)
)
tlpPduDisplayEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpPduDisplayEntry.setStatus("deprecated")


class _TlpPduDisplayScheme_Type(Integer32):
    """Custom type tlpPduDisplayScheme based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("schemeReverse", 0),
          ("schemeNormal", 1))
    )


_TlpPduDisplayScheme_Type.__name__ = "Integer32"
_TlpPduDisplayScheme_Object = MibTableColumn
tlpPduDisplayScheme = _TlpPduDisplayScheme_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 1, 4, 1, 1),
    _TlpPduDisplayScheme_Type()
)
tlpPduDisplayScheme.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduDisplayScheme.setStatus("deprecated")


class _TlpPduDisplayOrientation_Type(Integer32):
    """Custom type tlpPduDisplayOrientation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("displayNormal", 0),
          ("displayReverse", 1))
    )


_TlpPduDisplayOrientation_Type.__name__ = "Integer32"
_TlpPduDisplayOrientation_Object = MibTableColumn
tlpPduDisplayOrientation = _TlpPduDisplayOrientation_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 1, 4, 1, 2),
    _TlpPduDisplayOrientation_Type()
)
tlpPduDisplayOrientation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduDisplayOrientation.setStatus("deprecated")


class _TlpPduDisplayAutoScroll_Type(Integer32):
    """Custom type tlpPduDisplayAutoScroll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("scrollDisabled", 0),
          ("scrollEnabled", 1))
    )


_TlpPduDisplayAutoScroll_Type.__name__ = "Integer32"
_TlpPduDisplayAutoScroll_Object = MibTableColumn
tlpPduDisplayAutoScroll = _TlpPduDisplayAutoScroll_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 1, 4, 1, 3),
    _TlpPduDisplayAutoScroll_Type()
)
tlpPduDisplayAutoScroll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduDisplayAutoScroll.setStatus("deprecated")


class _TlpPduDisplayIntensity_Type(Integer32):
    """Custom type tlpPduDisplayIntensity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("intensity25", 1),
          ("intensity50", 2),
          ("intensity75", 3),
          ("intensity100", 4))
    )


_TlpPduDisplayIntensity_Type.__name__ = "Integer32"
_TlpPduDisplayIntensity_Object = MibTableColumn
tlpPduDisplayIntensity = _TlpPduDisplayIntensity_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 1, 4, 1, 4),
    _TlpPduDisplayIntensity_Type()
)
tlpPduDisplayIntensity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduDisplayIntensity.setStatus("deprecated")


class _TlpPduDisplayUnits_Type(Integer32):
    """Custom type tlpPduDisplayUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("metric", 1))
    )


_TlpPduDisplayUnits_Type.__name__ = "Integer32"
_TlpPduDisplayUnits_Object = MibTableColumn
tlpPduDisplayUnits = _TlpPduDisplayUnits_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 1, 4, 1, 5),
    _TlpPduDisplayUnits_Type()
)
tlpPduDisplayUnits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduDisplayUnits.setStatus("deprecated")
_TlpPduDevice_ObjectIdentity = ObjectIdentity
tlpPduDevice = _TlpPduDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 2)
)
_TlpPduDeviceTable_Object = MibTable
tlpPduDeviceTable = _TlpPduDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    tlpPduDeviceTable.setStatus("current")
_TlpPduDeviceEntry_Object = MibTableRow
tlpPduDeviceEntry = _TlpPduDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 2, 1, 1)
)
tlpPduDeviceEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpPduDeviceEntry.setStatus("current")


class _TlpPduDeviceMainLoadState_Type(Integer32):
    """Custom type tlpPduDeviceMainLoadState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("off", 1),
          ("on", 2))
    )


_TlpPduDeviceMainLoadState_Type.__name__ = "Integer32"
_TlpPduDeviceMainLoadState_Object = MibTableColumn
tlpPduDeviceMainLoadState = _TlpPduDeviceMainLoadState_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 2, 1, 1, 1),
    _TlpPduDeviceMainLoadState_Type()
)
tlpPduDeviceMainLoadState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduDeviceMainLoadState.setStatus("current")
_TlpPduDeviceMainLoadControllable_Type = TruthValue
_TlpPduDeviceMainLoadControllable_Object = MibTableColumn
tlpPduDeviceMainLoadControllable = _TlpPduDeviceMainLoadControllable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 2, 1, 1, 2),
    _TlpPduDeviceMainLoadControllable_Type()
)
tlpPduDeviceMainLoadControllable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduDeviceMainLoadControllable.setStatus("current")


class _TlpPduDeviceMainLoadCommand_Type(Integer32):
    """Custom type tlpPduDeviceMainLoadCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("turnOff", 1),
          ("turnOn", 2),
          ("cycle", 3))
    )


_TlpPduDeviceMainLoadCommand_Type.__name__ = "Integer32"
_TlpPduDeviceMainLoadCommand_Object = MibTableColumn
tlpPduDeviceMainLoadCommand = _TlpPduDeviceMainLoadCommand_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 2, 1, 1, 3),
    _TlpPduDeviceMainLoadCommand_Type()
)
tlpPduDeviceMainLoadCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduDeviceMainLoadCommand.setStatus("current")
_TlpPduDevicePowerOnDelay_Type = Integer32
_TlpPduDevicePowerOnDelay_Object = MibTableColumn
tlpPduDevicePowerOnDelay = _TlpPduDevicePowerOnDelay_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 2, 1, 1, 4),
    _TlpPduDevicePowerOnDelay_Type()
)
tlpPduDevicePowerOnDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduDevicePowerOnDelay.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduDevicePowerOnDelay.setUnits("Seconds")
_TlpPduDeviceTotalInputPowerRating_Type = Integer32
_TlpPduDeviceTotalInputPowerRating_Object = MibTableColumn
tlpPduDeviceTotalInputPowerRating = _TlpPduDeviceTotalInputPowerRating_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 2, 1, 1, 5),
    _TlpPduDeviceTotalInputPowerRating_Type()
)
tlpPduDeviceTotalInputPowerRating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduDeviceTotalInputPowerRating.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduDeviceTotalInputPowerRating.setUnits("Watts")
_TlpPduDeviceTemperatureC_Type = Integer32
_TlpPduDeviceTemperatureC_Object = MibTableColumn
tlpPduDeviceTemperatureC = _TlpPduDeviceTemperatureC_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 2, 1, 1, 6),
    _TlpPduDeviceTemperatureC_Type()
)
tlpPduDeviceTemperatureC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduDeviceTemperatureC.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduDeviceTemperatureC.setUnits("degrees Celsius")
_TlpPduDeviceTemperatureF_Type = Integer32
_TlpPduDeviceTemperatureF_Object = MibTableColumn
tlpPduDeviceTemperatureF = _TlpPduDeviceTemperatureF_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 2, 1, 1, 7),
    _TlpPduDeviceTemperatureF_Type()
)
tlpPduDeviceTemperatureF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduDeviceTemperatureF.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduDeviceTemperatureF.setUnits("degrees Fahrenheit")


class _TlpPduDevicePhaseImbalance_Type(Integer32):
    """Custom type tlpPduDevicePhaseImbalance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_TlpPduDevicePhaseImbalance_Type.__name__ = "Integer32"
_TlpPduDevicePhaseImbalance_Object = MibTableColumn
tlpPduDevicePhaseImbalance = _TlpPduDevicePhaseImbalance_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 2, 1, 1, 8),
    _TlpPduDevicePhaseImbalance_Type()
)
tlpPduDevicePhaseImbalance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduDevicePhaseImbalance.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduDevicePhaseImbalance.setUnits("percent")
_TlpPduDeviceOutputActivePowerTotal_Type = Unsigned32
_TlpPduDeviceOutputActivePowerTotal_Object = MibTableColumn
tlpPduDeviceOutputActivePowerTotal = _TlpPduDeviceOutputActivePowerTotal_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 2, 1, 1, 9),
    _TlpPduDeviceOutputActivePowerTotal_Type()
)
tlpPduDeviceOutputActivePowerTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduDeviceOutputActivePowerTotal.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduDeviceOutputActivePowerTotal.setUnits("Watts")
_TlpPduDeviceAggregatePowerFactor_Type = Unsigned32
_TlpPduDeviceAggregatePowerFactor_Object = MibTableColumn
tlpPduDeviceAggregatePowerFactor = _TlpPduDeviceAggregatePowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 2, 1, 1, 10),
    _TlpPduDeviceAggregatePowerFactor_Type()
)
tlpPduDeviceAggregatePowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduDeviceAggregatePowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduDeviceAggregatePowerFactor.setUnits("0.1 Watts")


class _TlpPduDeviceOutputCurrentPrecision_Type(Integer32):
    """Custom type tlpPduDeviceOutputCurrentPrecision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wholeNumber", 0),
          ("tenths", 1),
          ("hundredths", 2))
    )


_TlpPduDeviceOutputCurrentPrecision_Type.__name__ = "Integer32"
_TlpPduDeviceOutputCurrentPrecision_Object = MibTableColumn
tlpPduDeviceOutputCurrentPrecision = _TlpPduDeviceOutputCurrentPrecision_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 2, 1, 1, 11),
    _TlpPduDeviceOutputCurrentPrecision_Type()
)
tlpPduDeviceOutputCurrentPrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduDeviceOutputCurrentPrecision.setStatus("current")
_TlpPduDeviceGeneralFault_Type = TruthValue
_TlpPduDeviceGeneralFault_Object = MibTableColumn
tlpPduDeviceGeneralFault = _TlpPduDeviceGeneralFault_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 2, 1, 1, 12),
    _TlpPduDeviceGeneralFault_Type()
)
tlpPduDeviceGeneralFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduDeviceGeneralFault.setStatus("current")
_TlpPduDeviceTotalOutputUtilization_Type = Integer32
_TlpPduDeviceTotalOutputUtilization_Object = MibTableColumn
tlpPduDeviceTotalOutputUtilization = _TlpPduDeviceTotalOutputUtilization_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 2, 1, 1, 13),
    _TlpPduDeviceTotalOutputUtilization_Type()
)
tlpPduDeviceTotalOutputUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduDeviceTotalOutputUtilization.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduDeviceTotalOutputUtilization.setUnits("percent")
_TlpPduDeviceOutputApparentPowerTotal_Type = Unsigned32
_TlpPduDeviceOutputApparentPowerTotal_Object = MibTableColumn
tlpPduDeviceOutputApparentPowerTotal = _TlpPduDeviceOutputApparentPowerTotal_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 2, 1, 1, 14),
    _TlpPduDeviceOutputApparentPowerTotal_Type()
)
tlpPduDeviceOutputApparentPowerTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduDeviceOutputApparentPowerTotal.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduDeviceOutputApparentPowerTotal.setUnits("Watts")
_TlpPduDeviceOutputReactivePowerTotal_Type = Integer32
_TlpPduDeviceOutputReactivePowerTotal_Object = MibTableColumn
tlpPduDeviceOutputReactivePowerTotal = _TlpPduDeviceOutputReactivePowerTotal_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 2, 1, 1, 15),
    _TlpPduDeviceOutputReactivePowerTotal_Type()
)
tlpPduDeviceOutputReactivePowerTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduDeviceOutputReactivePowerTotal.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduDeviceOutputReactivePowerTotal.setUnits("Watts")
_TlpPduDeviceOutputCurrentTotal_Type = Unsigned32
_TlpPduDeviceOutputCurrentTotal_Object = MibTableColumn
tlpPduDeviceOutputCurrentTotal = _TlpPduDeviceOutputCurrentTotal_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 2, 1, 1, 16),
    _TlpPduDeviceOutputCurrentTotal_Type()
)
tlpPduDeviceOutputCurrentTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduDeviceOutputCurrentTotal.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduDeviceOutputCurrentTotal.setUnits("0.01 Amps")
_TlpPduDeviceWattHoursTotal_Type = Unsigned32
_TlpPduDeviceWattHoursTotal_Object = MibTableColumn
tlpPduDeviceWattHoursTotal = _TlpPduDeviceWattHoursTotal_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 2, 1, 1, 17),
    _TlpPduDeviceWattHoursTotal_Type()
)
tlpPduDeviceWattHoursTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduDeviceWattHoursTotal.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduDeviceWattHoursTotal.setUnits("WH")
_TlpPduDevicePeakPowerTotal_Type = Unsigned32
_TlpPduDevicePeakPowerTotal_Object = MibTableColumn
tlpPduDevicePeakPowerTotal = _TlpPduDevicePeakPowerTotal_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 2, 1, 1, 18),
    _TlpPduDevicePeakPowerTotal_Type()
)
tlpPduDevicePeakPowerTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduDevicePeakPowerTotal.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduDevicePeakPowerTotal.setUnits("Watts")
_TlpPduDevice24hrEnergyTotal_Type = Unsigned32
_TlpPduDevice24hrEnergyTotal_Object = MibTableColumn
tlpPduDevice24hrEnergyTotal = _TlpPduDevice24hrEnergyTotal_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 2, 1, 1, 19),
    _TlpPduDevice24hrEnergyTotal_Type()
)
tlpPduDevice24hrEnergyTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduDevice24hrEnergyTotal.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduDevice24hrEnergyTotal.setUnits("0.01 KWH")
_TlpPduDetail_ObjectIdentity = ObjectIdentity
tlpPduDetail = _TlpPduDetail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3)
)
_TlpPduInput_ObjectIdentity = ObjectIdentity
tlpPduInput = _TlpPduInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 1)
)
_TlpPduInputTable_Object = MibTable
tlpPduInputTable = _TlpPduInputTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    tlpPduInputTable.setStatus("current")
_TlpPduInputEntry_Object = MibTableRow
tlpPduInputEntry = _TlpPduInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 1, 1, 1)
)
tlpPduInputEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpPduInputEntry.setStatus("current")
_TlpPduInputNominalVoltage_Type = Unsigned32
_TlpPduInputNominalVoltage_Object = MibTableColumn
tlpPduInputNominalVoltage = _TlpPduInputNominalVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 1, 1, 1, 1),
    _TlpPduInputNominalVoltage_Type()
)
tlpPduInputNominalVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduInputNominalVoltage.setStatus("current")
_TlpPduInputNominalVoltagePhaseToPhase_Type = Unsigned32
_TlpPduInputNominalVoltagePhaseToPhase_Object = MibTableColumn
tlpPduInputNominalVoltagePhaseToPhase = _TlpPduInputNominalVoltagePhaseToPhase_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 1, 1, 1, 2),
    _TlpPduInputNominalVoltagePhaseToPhase_Type()
)
tlpPduInputNominalVoltagePhaseToPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduInputNominalVoltagePhaseToPhase.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduInputNominalVoltagePhaseToPhase.setUnits("0.1 Volts")
_TlpPduInputNominalVoltagePhaseToNeutral_Type = Unsigned32
_TlpPduInputNominalVoltagePhaseToNeutral_Object = MibTableColumn
tlpPduInputNominalVoltagePhaseToNeutral = _TlpPduInputNominalVoltagePhaseToNeutral_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 1, 1, 1, 3),
    _TlpPduInputNominalVoltagePhaseToNeutral_Type()
)
tlpPduInputNominalVoltagePhaseToNeutral.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduInputNominalVoltagePhaseToNeutral.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduInputNominalVoltagePhaseToNeutral.setUnits("0.1 Volts")
_TlpPduInputLowTransferVoltage_Type = Unsigned32
_TlpPduInputLowTransferVoltage_Object = MibTableColumn
tlpPduInputLowTransferVoltage = _TlpPduInputLowTransferVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 1, 1, 1, 4),
    _TlpPduInputLowTransferVoltage_Type()
)
tlpPduInputLowTransferVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduInputLowTransferVoltage.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduInputLowTransferVoltage.setUnits("0.1 Volts")
_TlpPduInputLowTransferVoltageLowerBound_Type = Unsigned32
_TlpPduInputLowTransferVoltageLowerBound_Object = MibTableColumn
tlpPduInputLowTransferVoltageLowerBound = _TlpPduInputLowTransferVoltageLowerBound_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 1, 1, 1, 5),
    _TlpPduInputLowTransferVoltageLowerBound_Type()
)
tlpPduInputLowTransferVoltageLowerBound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduInputLowTransferVoltageLowerBound.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduInputLowTransferVoltageLowerBound.setUnits("0.1 Volts")
_TlpPduInputLowTransferVoltageUpperBound_Type = Unsigned32
_TlpPduInputLowTransferVoltageUpperBound_Object = MibTableColumn
tlpPduInputLowTransferVoltageUpperBound = _TlpPduInputLowTransferVoltageUpperBound_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 1, 1, 1, 6),
    _TlpPduInputLowTransferVoltageUpperBound_Type()
)
tlpPduInputLowTransferVoltageUpperBound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduInputLowTransferVoltageUpperBound.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduInputLowTransferVoltageUpperBound.setUnits("0.1 Volts")
_TlpPduInputHighTransferVoltage_Type = Unsigned32
_TlpPduInputHighTransferVoltage_Object = MibTableColumn
tlpPduInputHighTransferVoltage = _TlpPduInputHighTransferVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 1, 1, 1, 7),
    _TlpPduInputHighTransferVoltage_Type()
)
tlpPduInputHighTransferVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduInputHighTransferVoltage.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduInputHighTransferVoltage.setUnits("0.1 Volts")
_TlpPduInputHighTransferVoltageLowerBound_Type = Unsigned32
_TlpPduInputHighTransferVoltageLowerBound_Object = MibTableColumn
tlpPduInputHighTransferVoltageLowerBound = _TlpPduInputHighTransferVoltageLowerBound_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 1, 1, 1, 8),
    _TlpPduInputHighTransferVoltageLowerBound_Type()
)
tlpPduInputHighTransferVoltageLowerBound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduInputHighTransferVoltageLowerBound.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduInputHighTransferVoltageLowerBound.setUnits("0.1 Volts")
_TlpPduInputHighTransferVoltageUpperBound_Type = Unsigned32
_TlpPduInputHighTransferVoltageUpperBound_Object = MibTableColumn
tlpPduInputHighTransferVoltageUpperBound = _TlpPduInputHighTransferVoltageUpperBound_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 1, 1, 1, 9),
    _TlpPduInputHighTransferVoltageUpperBound_Type()
)
tlpPduInputHighTransferVoltageUpperBound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduInputHighTransferVoltageUpperBound.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduInputHighTransferVoltageUpperBound.setUnits("0.1 Volts")
_TlpPduInputCurrentLimit_Type = Unsigned32
_TlpPduInputCurrentLimit_Object = MibTableColumn
tlpPduInputCurrentLimit = _TlpPduInputCurrentLimit_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 1, 1, 1, 10),
    _TlpPduInputCurrentLimit_Type()
)
tlpPduInputCurrentLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduInputCurrentLimit.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduInputCurrentLimit.setUnits("Amps")
_TlpPduInputCurrentTotal_Type = Unsigned32
_TlpPduInputCurrentTotal_Object = MibTableColumn
tlpPduInputCurrentTotal = _TlpPduInputCurrentTotal_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 1, 1, 1, 11),
    _TlpPduInputCurrentTotal_Type()
)
tlpPduInputCurrentTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduInputCurrentTotal.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduInputCurrentTotal.setUnits("0.01 Amps")
_TlpPduInputPhaseTable_Object = MibTable
tlpPduInputPhaseTable = _TlpPduInputPhaseTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 1, 2)
)
if mibBuilder.loadTexts:
    tlpPduInputPhaseTable.setStatus("current")
_TlpPduInputPhaseEntry_Object = MibTableRow
tlpPduInputPhaseEntry = _TlpPduInputPhaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 1, 2, 1)
)
tlpPduInputPhaseEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpPduInputPhaseIndex"),
)
if mibBuilder.loadTexts:
    tlpPduInputPhaseEntry.setStatus("current")
_TlpPduInputPhaseIndex_Type = Unsigned32
_TlpPduInputPhaseIndex_Object = MibTableColumn
tlpPduInputPhaseIndex = _TlpPduInputPhaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 1, 2, 1, 1),
    _TlpPduInputPhaseIndex_Type()
)
tlpPduInputPhaseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduInputPhaseIndex.setStatus("current")


class _TlpPduInputPhasePhaseType_Type(Integer32):
    """Custom type tlpPduInputPhasePhaseType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("phaseToNeutral", 0),
          ("phaseToPhase", 1))
    )


_TlpPduInputPhasePhaseType_Type.__name__ = "Integer32"
_TlpPduInputPhasePhaseType_Object = MibTableColumn
tlpPduInputPhasePhaseType = _TlpPduInputPhasePhaseType_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 1, 2, 1, 2),
    _TlpPduInputPhasePhaseType_Type()
)
tlpPduInputPhasePhaseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduInputPhasePhaseType.setStatus("current")
_TlpPduInputPhaseFrequency_Type = Unsigned32
_TlpPduInputPhaseFrequency_Object = MibTableColumn
tlpPduInputPhaseFrequency = _TlpPduInputPhaseFrequency_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 1, 2, 1, 3),
    _TlpPduInputPhaseFrequency_Type()
)
tlpPduInputPhaseFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduInputPhaseFrequency.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduInputPhaseFrequency.setUnits("0.1 Hertz")
_TlpPduInputPhaseVoltage_Type = Unsigned32
_TlpPduInputPhaseVoltage_Object = MibTableColumn
tlpPduInputPhaseVoltage = _TlpPduInputPhaseVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 1, 2, 1, 4),
    _TlpPduInputPhaseVoltage_Type()
)
tlpPduInputPhaseVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduInputPhaseVoltage.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduInputPhaseVoltage.setUnits("0.1 Volts")
_TlpPduInputPhaseVoltageMin_Type = Unsigned32
_TlpPduInputPhaseVoltageMin_Object = MibTableColumn
tlpPduInputPhaseVoltageMin = _TlpPduInputPhaseVoltageMin_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 1, 2, 1, 5),
    _TlpPduInputPhaseVoltageMin_Type()
)
tlpPduInputPhaseVoltageMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduInputPhaseVoltageMin.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduInputPhaseVoltageMin.setUnits("0.1 Volts")
_TlpPduInputPhaseVoltageMax_Type = Unsigned32
_TlpPduInputPhaseVoltageMax_Object = MibTableColumn
tlpPduInputPhaseVoltageMax = _TlpPduInputPhaseVoltageMax_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 1, 2, 1, 6),
    _TlpPduInputPhaseVoltageMax_Type()
)
tlpPduInputPhaseVoltageMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduInputPhaseVoltageMax.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduInputPhaseVoltageMax.setUnits("0.1 Volts")
_TlpPduInputPhaseCurrent_Type = Unsigned32
_TlpPduInputPhaseCurrent_Object = MibTableColumn
tlpPduInputPhaseCurrent = _TlpPduInputPhaseCurrent_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 1, 2, 1, 7),
    _TlpPduInputPhaseCurrent_Type()
)
tlpPduInputPhaseCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduInputPhaseCurrent.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduInputPhaseCurrent.setUnits("0.01 Amps")
_TlpPduInputPhasePower_Type = Unsigned32
_TlpPduInputPhasePower_Object = MibTableColumn
tlpPduInputPhasePower = _TlpPduInputPhasePower_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 1, 2, 1, 8),
    _TlpPduInputPhasePower_Type()
)
tlpPduInputPhasePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduInputPhasePower.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduInputPhasePower.setUnits("Watts")
_TlpPduInputPhaseThdVoltage_Type = Unsigned32
_TlpPduInputPhaseThdVoltage_Object = MibTableColumn
tlpPduInputPhaseThdVoltage = _TlpPduInputPhaseThdVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 1, 2, 1, 9),
    _TlpPduInputPhaseThdVoltage_Type()
)
tlpPduInputPhaseThdVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduInputPhaseThdVoltage.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduInputPhaseThdVoltage.setUnits("0.01 percent")
_TlpPduOutput_ObjectIdentity = ObjectIdentity
tlpPduOutput = _TlpPduOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 2)
)
_TlpPduOutputTable_Object = MibTable
tlpPduOutputTable = _TlpPduOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    tlpPduOutputTable.setStatus("current")
_TlpPduOutputEntry_Object = MibTableRow
tlpPduOutputEntry = _TlpPduOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 2, 1, 1)
)
tlpPduOutputEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpPduOutputIndex"),
)
if mibBuilder.loadTexts:
    tlpPduOutputEntry.setStatus("current")
_TlpPduOutputIndex_Type = Unsigned32
_TlpPduOutputIndex_Object = MibTableColumn
tlpPduOutputIndex = _TlpPduOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 2, 1, 1, 1),
    _TlpPduOutputIndex_Type()
)
tlpPduOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduOutputIndex.setStatus("current")


class _TlpPduOutputPhase_Type(Integer32):
    """Custom type tlpPduOutputPhase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("phase1", 1),
          ("phase2", 2),
          ("phase3", 3))
    )


_TlpPduOutputPhase_Type.__name__ = "Integer32"
_TlpPduOutputPhase_Object = MibTableColumn
tlpPduOutputPhase = _TlpPduOutputPhase_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 2, 1, 1, 2),
    _TlpPduOutputPhase_Type()
)
tlpPduOutputPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduOutputPhase.setStatus("current")


class _TlpPduOutputPhaseType_Type(Integer32):
    """Custom type tlpPduOutputPhaseType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("phaseToNeutral", 0),
          ("phaseToPhase", 1))
    )


_TlpPduOutputPhaseType_Type.__name__ = "Integer32"
_TlpPduOutputPhaseType_Object = MibTableColumn
tlpPduOutputPhaseType = _TlpPduOutputPhaseType_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 2, 1, 1, 3),
    _TlpPduOutputPhaseType_Type()
)
tlpPduOutputPhaseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduOutputPhaseType.setStatus("current")
_TlpPduOutputVoltage_Type = Unsigned32
_TlpPduOutputVoltage_Object = MibTableColumn
tlpPduOutputVoltage = _TlpPduOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 2, 1, 1, 4),
    _TlpPduOutputVoltage_Type()
)
tlpPduOutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduOutputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduOutputVoltage.setUnits("0.1 Volts")
_TlpPduOutputCurrent_Type = Unsigned32
_TlpPduOutputCurrent_Object = MibTableColumn
tlpPduOutputCurrent = _TlpPduOutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 2, 1, 1, 5),
    _TlpPduOutputCurrent_Type()
)
tlpPduOutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduOutputCurrent.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduOutputCurrent.setUnits("0.01 Amps")
_TlpPduOutputCurrentMin_Type = Unsigned32
_TlpPduOutputCurrentMin_Object = MibTableColumn
tlpPduOutputCurrentMin = _TlpPduOutputCurrentMin_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 2, 1, 1, 6),
    _TlpPduOutputCurrentMin_Type()
)
tlpPduOutputCurrentMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduOutputCurrentMin.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduOutputCurrentMin.setUnits("0.01 Amps")
_TlpPduOutputCurrentMax_Type = Unsigned32
_TlpPduOutputCurrentMax_Object = MibTableColumn
tlpPduOutputCurrentMax = _TlpPduOutputCurrentMax_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 2, 1, 1, 7),
    _TlpPduOutputCurrentMax_Type()
)
tlpPduOutputCurrentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduOutputCurrentMax.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduOutputCurrentMax.setUnits("0.01 Amps")
_TlpPduOutputActivePower_Type = Unsigned32
_TlpPduOutputActivePower_Object = MibTableColumn
tlpPduOutputActivePower = _TlpPduOutputActivePower_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 2, 1, 1, 8),
    _TlpPduOutputActivePower_Type()
)
tlpPduOutputActivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduOutputActivePower.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduOutputActivePower.setUnits("Watts")
_TlpPduOutputPowerFactor_Type = Integer32
_TlpPduOutputPowerFactor_Object = MibTableColumn
tlpPduOutputPowerFactor = _TlpPduOutputPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 2, 1, 1, 9),
    _TlpPduOutputPowerFactor_Type()
)
tlpPduOutputPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduOutputPowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduOutputPowerFactor.setUnits("0.01")


class _TlpPduOutputSource_Type(Integer32):
    """Custom type tlpPduOutputSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("normal", 1))
    )


_TlpPduOutputSource_Type.__name__ = "Integer32"
_TlpPduOutputSource_Object = MibTableColumn
tlpPduOutputSource = _TlpPduOutputSource_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 2, 1, 1, 10),
    _TlpPduOutputSource_Type()
)
tlpPduOutputSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduOutputSource.setStatus("current")
_TlpPduOutputFrequency_Type = Unsigned32
_TlpPduOutputFrequency_Object = MibTableColumn
tlpPduOutputFrequency = _TlpPduOutputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 2, 1, 1, 11),
    _TlpPduOutputFrequency_Type()
)
tlpPduOutputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduOutputFrequency.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduOutputFrequency.setUnits("0.1 Hertz")
_TlpPduOutputPowerKVA_Type = Unsigned32
_TlpPduOutputPowerKVA_Object = MibTableColumn
tlpPduOutputPowerKVA = _TlpPduOutputPowerKVA_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 2, 1, 1, 12),
    _TlpPduOutputPowerKVA_Type()
)
tlpPduOutputPowerKVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduOutputPowerKVA.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduOutputPowerKVA.setUnits("0.01 KVA")
_TlpPduOutputPowerKW_Type = Unsigned32
_TlpPduOutputPowerKW_Object = MibTableColumn
tlpPduOutputPowerKW = _TlpPduOutputPowerKW_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 2, 1, 1, 13),
    _TlpPduOutputPowerKW_Type()
)
tlpPduOutputPowerKW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduOutputPowerKW.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduOutputPowerKW.setUnits("0.01 KW")
_TlpPduOutput24hrEnergy_Type = Unsigned32
_TlpPduOutput24hrEnergy_Object = MibTableColumn
tlpPduOutput24hrEnergy = _TlpPduOutput24hrEnergy_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 2, 1, 1, 14),
    _TlpPduOutput24hrEnergy_Type()
)
tlpPduOutput24hrEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduOutput24hrEnergy.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduOutput24hrEnergy.setUnits("0.01 KWH")
_TlpPduOutputApparentPower_Type = Unsigned32
_TlpPduOutputApparentPower_Object = MibTableColumn
tlpPduOutputApparentPower = _TlpPduOutputApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 2, 1, 1, 15),
    _TlpPduOutputApparentPower_Type()
)
tlpPduOutputApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduOutputApparentPower.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduOutputApparentPower.setUnits("VA")
_TlpPduOutputReactivePower_Type = Integer32
_TlpPduOutputReactivePower_Object = MibTableColumn
tlpPduOutputReactivePower = _TlpPduOutputReactivePower_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 2, 1, 1, 16),
    _TlpPduOutputReactivePower_Type()
)
tlpPduOutputReactivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduOutputReactivePower.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduOutputReactivePower.setUnits("VAR")
_TlpPduOutputUtilization_Type = Unsigned32
_TlpPduOutputUtilization_Object = MibTableColumn
tlpPduOutputUtilization = _TlpPduOutputUtilization_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 2, 1, 1, 17),
    _TlpPduOutputUtilization_Type()
)
tlpPduOutputUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduOutputUtilization.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduOutputUtilization.setUnits("0.01 percent")
_TlpPduOutputWattHours_Type = Unsigned32
_TlpPduOutputWattHours_Object = MibTableColumn
tlpPduOutputWattHours = _TlpPduOutputWattHours_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 2, 1, 1, 18),
    _TlpPduOutputWattHours_Type()
)
tlpPduOutputWattHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduOutputWattHours.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduOutputWattHours.setUnits("WH")
_TlpPduOutputPeakPower_Type = Unsigned32
_TlpPduOutputPeakPower_Object = MibTableColumn
tlpPduOutputPeakPower = _TlpPduOutputPeakPower_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 2, 1, 1, 19),
    _TlpPduOutputPeakPower_Type()
)
tlpPduOutputPeakPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduOutputPeakPower.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduOutputPeakPower.setUnits("Watts")
_TlpPduOutlet_ObjectIdentity = ObjectIdentity
tlpPduOutlet = _TlpPduOutlet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 3)
)
_TlpPduOutletTable_Object = MibTable
tlpPduOutletTable = _TlpPduOutletTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 3, 1)
)
if mibBuilder.loadTexts:
    tlpPduOutletTable.setStatus("current")
_TlpPduOutletEntry_Object = MibTableRow
tlpPduOutletEntry = _TlpPduOutletEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 3, 1, 1)
)
tlpPduOutletEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpPduOutletIndex"),
)
if mibBuilder.loadTexts:
    tlpPduOutletEntry.setStatus("current")
_TlpPduOutletIndex_Type = Unsigned32
_TlpPduOutletIndex_Object = MibTableColumn
tlpPduOutletIndex = _TlpPduOutletIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 3, 1, 1, 1),
    _TlpPduOutletIndex_Type()
)
tlpPduOutletIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduOutletIndex.setStatus("current")
_TlpPduOutletName_Type = DisplayString
_TlpPduOutletName_Object = MibTableColumn
tlpPduOutletName = _TlpPduOutletName_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 3, 1, 1, 2),
    _TlpPduOutletName_Type()
)
tlpPduOutletName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduOutletName.setStatus("current")
_TlpPduOutletDescription_Type = DisplayString
_TlpPduOutletDescription_Object = MibTableColumn
tlpPduOutletDescription = _TlpPduOutletDescription_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 3, 1, 1, 3),
    _TlpPduOutletDescription_Type()
)
tlpPduOutletDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduOutletDescription.setStatus("current")


class _TlpPduOutletState_Type(Integer32):
    """Custom type tlpPduOutletState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("off", 1),
          ("on", 2))
    )


_TlpPduOutletState_Type.__name__ = "Integer32"
_TlpPduOutletState_Object = MibTableColumn
tlpPduOutletState = _TlpPduOutletState_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 3, 1, 1, 4),
    _TlpPduOutletState_Type()
)
tlpPduOutletState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduOutletState.setStatus("current")
_TlpPduOutletControllable_Type = TruthValue
_TlpPduOutletControllable_Object = MibTableColumn
tlpPduOutletControllable = _TlpPduOutletControllable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 3, 1, 1, 5),
    _TlpPduOutletControllable_Type()
)
tlpPduOutletControllable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduOutletControllable.setStatus("current")


class _TlpPduOutletCommand_Type(Integer32):
    """Custom type tlpPduOutletCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("turnOff", 1),
          ("turnOn", 2),
          ("cycle", 3))
    )


_TlpPduOutletCommand_Type.__name__ = "Integer32"
_TlpPduOutletCommand_Object = MibTableColumn
tlpPduOutletCommand = _TlpPduOutletCommand_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 3, 1, 1, 6),
    _TlpPduOutletCommand_Type()
)
tlpPduOutletCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduOutletCommand.setStatus("current")
_TlpPduOutletVoltage_Type = Unsigned32
_TlpPduOutletVoltage_Object = MibTableColumn
tlpPduOutletVoltage = _TlpPduOutletVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 3, 1, 1, 7),
    _TlpPduOutletVoltage_Type()
)
tlpPduOutletVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduOutletVoltage.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduOutletVoltage.setUnits("0.1 Volts")
_TlpPduOutletCurrent_Type = Unsigned32
_TlpPduOutletCurrent_Object = MibTableColumn
tlpPduOutletCurrent = _TlpPduOutletCurrent_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 3, 1, 1, 8),
    _TlpPduOutletCurrent_Type()
)
tlpPduOutletCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduOutletCurrent.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduOutletCurrent.setUnits("0.01 Amps")
_TlpPduOutletActivePower_Type = Unsigned32
_TlpPduOutletActivePower_Object = MibTableColumn
tlpPduOutletActivePower = _TlpPduOutletActivePower_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 3, 1, 1, 9),
    _TlpPduOutletActivePower_Type()
)
tlpPduOutletActivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduOutletActivePower.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduOutletActivePower.setUnits("Watts")


class _TlpPduOutletRampAction_Type(Integer32):
    """Custom type tlpPduOutletRampAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("remainOff", 0),
          ("turnOnAfterDelay", 1))
    )


_TlpPduOutletRampAction_Type.__name__ = "Integer32"
_TlpPduOutletRampAction_Object = MibTableColumn
tlpPduOutletRampAction = _TlpPduOutletRampAction_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 3, 1, 1, 10),
    _TlpPduOutletRampAction_Type()
)
tlpPduOutletRampAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduOutletRampAction.setStatus("current")
_TlpPduOutletRampDelay_Type = Integer32
_TlpPduOutletRampDelay_Object = MibTableColumn
tlpPduOutletRampDelay = _TlpPduOutletRampDelay_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 3, 1, 1, 11),
    _TlpPduOutletRampDelay_Type()
)
tlpPduOutletRampDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduOutletRampDelay.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduOutletRampDelay.setUnits("seconds")


class _TlpPduOutletShedAction_Type(Integer32):
    """Custom type tlpPduOutletShedAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("remainOn", 0),
          ("turnOffAfterDelay", 1))
    )


_TlpPduOutletShedAction_Type.__name__ = "Integer32"
_TlpPduOutletShedAction_Object = MibTableColumn
tlpPduOutletShedAction = _TlpPduOutletShedAction_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 3, 1, 1, 12),
    _TlpPduOutletShedAction_Type()
)
tlpPduOutletShedAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduOutletShedAction.setStatus("current")
_TlpPduOutletShedDelay_Type = Integer32
_TlpPduOutletShedDelay_Object = MibTableColumn
tlpPduOutletShedDelay = _TlpPduOutletShedDelay_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 3, 1, 1, 13),
    _TlpPduOutletShedDelay_Type()
)
tlpPduOutletShedDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduOutletShedDelay.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduOutletShedDelay.setUnits("seconds")
_TlpPduOutletGroup_Type = Integer32
_TlpPduOutletGroup_Object = MibTableColumn
tlpPduOutletGroup = _TlpPduOutletGroup_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 3, 1, 1, 14),
    _TlpPduOutletGroup_Type()
)
tlpPduOutletGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduOutletGroup.setStatus("current")
_TlpPduOutletBank_Type = Integer32
_TlpPduOutletBank_Object = MibTableColumn
tlpPduOutletBank = _TlpPduOutletBank_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 3, 1, 1, 15),
    _TlpPduOutletBank_Type()
)
tlpPduOutletBank.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduOutletBank.setStatus("deprecated")
_TlpPduOutletCircuit_Type = Integer32
_TlpPduOutletCircuit_Object = MibTableColumn
tlpPduOutletCircuit = _TlpPduOutletCircuit_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 3, 1, 1, 16),
    _TlpPduOutletCircuit_Type()
)
tlpPduOutletCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduOutletCircuit.setStatus("current")


class _TlpPduOutletPhase_Type(Integer32):
    """Custom type tlpPduOutletPhase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("phase1", 1),
          ("phase2", 2),
          ("phase3", 3),
          ("phase1-2", 4),
          ("phase2-3", 5),
          ("phase3-1", 6))
    )


_TlpPduOutletPhase_Type.__name__ = "Integer32"
_TlpPduOutletPhase_Object = MibTableColumn
tlpPduOutletPhase = _TlpPduOutletPhase_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 3, 1, 1, 17),
    _TlpPduOutletPhase_Type()
)
tlpPduOutletPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduOutletPhase.setStatus("current")


class _TlpPduOutletReceptacleType_Type(Integer32):
    """Custom type tlpPduOutletReceptacleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("nema-515R", 1),
          ("nema-520R", 2),
          ("nema-530R", 3),
          ("nema-L515R", 4),
          ("nema-L520R", 5),
          ("nema-L530R", 6),
          ("nema-L615R", 7),
          ("nema-L620R", 8),
          ("nema-L630R", 9),
          ("nema-L1430R", 10),
          ("nema-L1520R", 11),
          ("nema-L1530R", 12),
          ("nema-L2120R", 13),
          ("nema-L2130R", 14),
          ("nema-L2230R", 15),
          ("iec-309-1620", 16),
          ("iec-309-3032", 17),
          ("iec-309-6063", 18),
          ("iec-320-C13", 19),
          ("iec-320-C14", 20),
          ("iec-320-C15", 21),
          ("iec-320-C17", 22),
          ("iec-320-C19", 23),
          ("iec-320-C20", 24))
    )


_TlpPduOutletReceptacleType_Type.__name__ = "Integer32"
_TlpPduOutletReceptacleType_Object = MibTableColumn
tlpPduOutletReceptacleType = _TlpPduOutletReceptacleType_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 3, 1, 1, 18),
    _TlpPduOutletReceptacleType_Type()
)
tlpPduOutletReceptacleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduOutletReceptacleType.setStatus("current")
_TlpPduOutletPowerFactor_Type = Integer32
_TlpPduOutletPowerFactor_Object = MibTableColumn
tlpPduOutletPowerFactor = _TlpPduOutletPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 3, 1, 1, 19),
    _TlpPduOutletPowerFactor_Type()
)
tlpPduOutletPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduOutletPowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduOutletPowerFactor.setUnits("0.01")
_TlpPduOutletApparentPower_Type = Unsigned32
_TlpPduOutletApparentPower_Object = MibTableColumn
tlpPduOutletApparentPower = _TlpPduOutletApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 3, 1, 1, 20),
    _TlpPduOutletApparentPower_Type()
)
tlpPduOutletApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduOutletApparentPower.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduOutletApparentPower.setUnits("VA")
_TlpPduOutletReactivePower_Type = Integer32
_TlpPduOutletReactivePower_Object = MibTableColumn
tlpPduOutletReactivePower = _TlpPduOutletReactivePower_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 3, 1, 1, 21),
    _TlpPduOutletReactivePower_Type()
)
tlpPduOutletReactivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduOutletReactivePower.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduOutletReactivePower.setUnits("VAR")
_TlpPduOutletFrequency_Type = Unsigned32
_TlpPduOutletFrequency_Object = MibTableColumn
tlpPduOutletFrequency = _TlpPduOutletFrequency_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 3, 1, 1, 22),
    _TlpPduOutletFrequency_Type()
)
tlpPduOutletFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduOutletFrequency.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduOutletFrequency.setUnits("0.1 Hertz")
_TlpPduOutletUtilization_Type = Unsigned32
_TlpPduOutletUtilization_Object = MibTableColumn
tlpPduOutletUtilization = _TlpPduOutletUtilization_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 3, 1, 1, 23),
    _TlpPduOutletUtilization_Type()
)
tlpPduOutletUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduOutletUtilization.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduOutletUtilization.setUnits("0.01 percent")
_TlpPduOutlet24hrEnergy_Type = Unsigned32
_TlpPduOutlet24hrEnergy_Object = MibTableColumn
tlpPduOutlet24hrEnergy = _TlpPduOutlet24hrEnergy_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 3, 1, 1, 24),
    _TlpPduOutlet24hrEnergy_Type()
)
tlpPduOutlet24hrEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduOutlet24hrEnergy.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduOutlet24hrEnergy.setUnits("0.01 KWH")
_TlpPduOutletOvercurrent_Type = TruthValue
_TlpPduOutletOvercurrent_Object = MibTableColumn
tlpPduOutletOvercurrent = _TlpPduOutletOvercurrent_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 3, 1, 1, 25),
    _TlpPduOutletOvercurrent_Type()
)
tlpPduOutletOvercurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduOutletOvercurrent.setStatus("current")
_TlpPduOutletGroupTable_Object = MibTable
tlpPduOutletGroupTable = _TlpPduOutletGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 3, 2)
)
if mibBuilder.loadTexts:
    tlpPduOutletGroupTable.setStatus("current")
_TlpPduOutletGroupEntry_Object = MibTableRow
tlpPduOutletGroupEntry = _TlpPduOutletGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 3, 2, 1)
)
tlpPduOutletGroupEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpPduOutletGroupIndex"),
)
if mibBuilder.loadTexts:
    tlpPduOutletGroupEntry.setStatus("current")
_TlpPduOutletGroupIndex_Type = Unsigned32
_TlpPduOutletGroupIndex_Object = MibTableColumn
tlpPduOutletGroupIndex = _TlpPduOutletGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 3, 2, 1, 1),
    _TlpPduOutletGroupIndex_Type()
)
tlpPduOutletGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduOutletGroupIndex.setStatus("current")
_TlpPduOutletGroupRowStatus_Type = RowStatus
_TlpPduOutletGroupRowStatus_Object = MibTableColumn
tlpPduOutletGroupRowStatus = _TlpPduOutletGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 3, 2, 1, 2),
    _TlpPduOutletGroupRowStatus_Type()
)
tlpPduOutletGroupRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduOutletGroupRowStatus.setStatus("current")
_TlpPduOutletGroupName_Type = DisplayString
_TlpPduOutletGroupName_Object = MibTableColumn
tlpPduOutletGroupName = _TlpPduOutletGroupName_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 3, 2, 1, 3),
    _TlpPduOutletGroupName_Type()
)
tlpPduOutletGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduOutletGroupName.setStatus("current")
_TlpPduOutletGroupDescription_Type = DisplayString
_TlpPduOutletGroupDescription_Object = MibTableColumn
tlpPduOutletGroupDescription = _TlpPduOutletGroupDescription_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 3, 2, 1, 4),
    _TlpPduOutletGroupDescription_Type()
)
tlpPduOutletGroupDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduOutletGroupDescription.setStatus("current")


class _TlpPduOutletGroupState_Type(Integer32):
    """Custom type tlpPduOutletGroupState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("off", 1),
          ("on", 2),
          ("mixed", 3))
    )


_TlpPduOutletGroupState_Type.__name__ = "Integer32"
_TlpPduOutletGroupState_Object = MibTableColumn
tlpPduOutletGroupState = _TlpPduOutletGroupState_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 3, 2, 1, 5),
    _TlpPduOutletGroupState_Type()
)
tlpPduOutletGroupState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduOutletGroupState.setStatus("current")


class _TlpPduOutletGroupCommand_Type(Integer32):
    """Custom type tlpPduOutletGroupCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("turnOff", 1),
          ("turnOn", 2),
          ("cycle", 3))
    )


_TlpPduOutletGroupCommand_Type.__name__ = "Integer32"
_TlpPduOutletGroupCommand_Object = MibTableColumn
tlpPduOutletGroupCommand = _TlpPduOutletGroupCommand_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 3, 2, 1, 6),
    _TlpPduOutletGroupCommand_Type()
)
tlpPduOutletGroupCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduOutletGroupCommand.setStatus("current")
_TlpPduCircuit_ObjectIdentity = ObjectIdentity
tlpPduCircuit = _TlpPduCircuit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 4)
)
_TlpPduCircuitTable_Object = MibTable
tlpPduCircuitTable = _TlpPduCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 4, 1)
)
if mibBuilder.loadTexts:
    tlpPduCircuitTable.setStatus("current")
_TlpPduCircuitEntry_Object = MibTableRow
tlpPduCircuitEntry = _TlpPduCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 4, 1, 1)
)
tlpPduCircuitEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpPduCircuitIndex"),
)
if mibBuilder.loadTexts:
    tlpPduCircuitEntry.setStatus("current")
_TlpPduCircuitIndex_Type = Unsigned32
_TlpPduCircuitIndex_Object = MibTableColumn
tlpPduCircuitIndex = _TlpPduCircuitIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 4, 1, 1, 1),
    _TlpPduCircuitIndex_Type()
)
tlpPduCircuitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduCircuitIndex.setStatus("current")


class _TlpPduCircuitPhase_Type(Integer32):
    """Custom type tlpPduCircuitPhase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("phase1", 1),
          ("phase2", 2),
          ("phase3", 3),
          ("phase1-2", 4),
          ("phase2-3", 5),
          ("phase3-1", 6))
    )


_TlpPduCircuitPhase_Type.__name__ = "Integer32"
_TlpPduCircuitPhase_Object = MibTableColumn
tlpPduCircuitPhase = _TlpPduCircuitPhase_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 4, 1, 1, 2),
    _TlpPduCircuitPhase_Type()
)
tlpPduCircuitPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduCircuitPhase.setStatus("current")
_TlpPduCircuitInputVoltage_Type = Integer32
_TlpPduCircuitInputVoltage_Object = MibTableColumn
tlpPduCircuitInputVoltage = _TlpPduCircuitInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 4, 1, 1, 3),
    _TlpPduCircuitInputVoltage_Type()
)
tlpPduCircuitInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduCircuitInputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduCircuitInputVoltage.setUnits("0.1 Volts")
_TlpPduCircuitTotalCurrent_Type = Integer32
_TlpPduCircuitTotalCurrent_Object = MibTableColumn
tlpPduCircuitTotalCurrent = _TlpPduCircuitTotalCurrent_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 4, 1, 1, 4),
    _TlpPduCircuitTotalCurrent_Type()
)
tlpPduCircuitTotalCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduCircuitTotalCurrent.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduCircuitTotalCurrent.setUnits("0.01 Amps")
_TlpPduCircuitCurrentLimit_Type = Integer32
_TlpPduCircuitCurrentLimit_Object = MibTableColumn
tlpPduCircuitCurrentLimit = _TlpPduCircuitCurrentLimit_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 4, 1, 1, 5),
    _TlpPduCircuitCurrentLimit_Type()
)
tlpPduCircuitCurrentLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduCircuitCurrentLimit.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduCircuitCurrentLimit.setUnits("0.01 Amps")
_TlpPduCircuitCurrentMin_Type = Integer32
_TlpPduCircuitCurrentMin_Object = MibTableColumn
tlpPduCircuitCurrentMin = _TlpPduCircuitCurrentMin_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 4, 1, 1, 6),
    _TlpPduCircuitCurrentMin_Type()
)
tlpPduCircuitCurrentMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduCircuitCurrentMin.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduCircuitCurrentMin.setUnits("0.01 Amps")
_TlpPduCircuitCurrentMax_Type = Integer32
_TlpPduCircuitCurrentMax_Object = MibTableColumn
tlpPduCircuitCurrentMax = _TlpPduCircuitCurrentMax_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 4, 1, 1, 7),
    _TlpPduCircuitCurrentMax_Type()
)
tlpPduCircuitCurrentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduCircuitCurrentMax.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduCircuitCurrentMax.setUnits("0.01 Amps")
_TlpPduCircuitTotalPower_Type = Integer32
_TlpPduCircuitTotalPower_Object = MibTableColumn
tlpPduCircuitTotalPower = _TlpPduCircuitTotalPower_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 4, 1, 1, 8),
    _TlpPduCircuitTotalPower_Type()
)
tlpPduCircuitTotalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduCircuitTotalPower.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduCircuitTotalPower.setUnits("Watts")
_TlpPduCircuitPowerFactor_Type = Integer32
_TlpPduCircuitPowerFactor_Object = MibTableColumn
tlpPduCircuitPowerFactor = _TlpPduCircuitPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 4, 1, 1, 9),
    _TlpPduCircuitPowerFactor_Type()
)
tlpPduCircuitPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduCircuitPowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduCircuitPowerFactor.setUnits("0.01")
_TlpPduCircuitUtilization_Type = Unsigned32
_TlpPduCircuitUtilization_Object = MibTableColumn
tlpPduCircuitUtilization = _TlpPduCircuitUtilization_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 4, 1, 1, 10),
    _TlpPduCircuitUtilization_Type()
)
tlpPduCircuitUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduCircuitUtilization.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduCircuitUtilization.setUnits("0.01 percent")
_TlpPduCircuitApparentPower_Type = Unsigned32
_TlpPduCircuitApparentPower_Object = MibTableColumn
tlpPduCircuitApparentPower = _TlpPduCircuitApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 4, 1, 1, 11),
    _TlpPduCircuitApparentPower_Type()
)
tlpPduCircuitApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduCircuitApparentPower.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduCircuitApparentPower.setUnits("VA")
_TlpPduCircuitReactivePower_Type = Integer32
_TlpPduCircuitReactivePower_Object = MibTableColumn
tlpPduCircuitReactivePower = _TlpPduCircuitReactivePower_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 4, 1, 1, 12),
    _TlpPduCircuitReactivePower_Type()
)
tlpPduCircuitReactivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduCircuitReactivePower.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduCircuitReactivePower.setUnits("VAR")
_TlpPduCircuitFrequency_Type = Unsigned32
_TlpPduCircuitFrequency_Object = MibTableColumn
tlpPduCircuitFrequency = _TlpPduCircuitFrequency_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 4, 1, 1, 13),
    _TlpPduCircuitFrequency_Type()
)
tlpPduCircuitFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduCircuitFrequency.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduCircuitFrequency.setUnits("0.1 Hertz")
_TlpPduCircuitWattHours_Type = Unsigned32
_TlpPduCircuitWattHours_Object = MibTableColumn
tlpPduCircuitWattHours = _TlpPduCircuitWattHours_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 4, 1, 1, 14),
    _TlpPduCircuitWattHours_Type()
)
tlpPduCircuitWattHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduCircuitWattHours.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduCircuitWattHours.setUnits("WH")
_TlpPduCircuitPeakPower_Type = Unsigned32
_TlpPduCircuitPeakPower_Object = MibTableColumn
tlpPduCircuitPeakPower = _TlpPduCircuitPeakPower_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 4, 1, 1, 15),
    _TlpPduCircuitPeakPower_Type()
)
tlpPduCircuitPeakPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduCircuitPeakPower.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduCircuitPeakPower.setUnits("Watts")
_TlpPduBreaker_ObjectIdentity = ObjectIdentity
tlpPduBreaker = _TlpPduBreaker_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 5)
)
_TlpPduBreakerTable_Object = MibTable
tlpPduBreakerTable = _TlpPduBreakerTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 5, 1)
)
if mibBuilder.loadTexts:
    tlpPduBreakerTable.setStatus("current")
_TlpPduBreakerEntry_Object = MibTableRow
tlpPduBreakerEntry = _TlpPduBreakerEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 5, 1, 1)
)
tlpPduBreakerEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpPduBreakerIndex"),
)
if mibBuilder.loadTexts:
    tlpPduBreakerEntry.setStatus("current")
_TlpPduBreakerIndex_Type = Unsigned32
_TlpPduBreakerIndex_Object = MibTableColumn
tlpPduBreakerIndex = _TlpPduBreakerIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 5, 1, 1, 1),
    _TlpPduBreakerIndex_Type()
)
tlpPduBreakerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduBreakerIndex.setStatus("current")


class _TlpPduBreakerStatus_Type(Integer32):
    """Custom type tlpPduBreakerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 0),
          ("closed", 1),
          ("notInstalled", 2))
    )


_TlpPduBreakerStatus_Type.__name__ = "Integer32"
_TlpPduBreakerStatus_Object = MibTableColumn
tlpPduBreakerStatus = _TlpPduBreakerStatus_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 5, 1, 1, 2),
    _TlpPduBreakerStatus_Type()
)
tlpPduBreakerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduBreakerStatus.setStatus("current")
_TlpPduHeatsink_ObjectIdentity = ObjectIdentity
tlpPduHeatsink = _TlpPduHeatsink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 6)
)
_TlpPduHeatsinkTable_Object = MibTable
tlpPduHeatsinkTable = _TlpPduHeatsinkTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 6, 1)
)
if mibBuilder.loadTexts:
    tlpPduHeatsinkTable.setStatus("current")
_TlpPduHeatsinkEntry_Object = MibTableRow
tlpPduHeatsinkEntry = _TlpPduHeatsinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 6, 1, 1)
)
tlpPduHeatsinkEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpPduHeatsinkIndex"),
)
if mibBuilder.loadTexts:
    tlpPduHeatsinkEntry.setStatus("current")
_TlpPduHeatsinkIndex_Type = Unsigned32
_TlpPduHeatsinkIndex_Object = MibTableColumn
tlpPduHeatsinkIndex = _TlpPduHeatsinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 6, 1, 1, 1),
    _TlpPduHeatsinkIndex_Type()
)
tlpPduHeatsinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduHeatsinkIndex.setStatus("current")


class _TlpPduHeatsinkStatus_Type(Integer32):
    """Custom type tlpPduHeatsinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("available", 1))
    )


_TlpPduHeatsinkStatus_Type.__name__ = "Integer32"
_TlpPduHeatsinkStatus_Object = MibTableColumn
tlpPduHeatsinkStatus = _TlpPduHeatsinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 6, 1, 1, 2),
    _TlpPduHeatsinkStatus_Type()
)
tlpPduHeatsinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduHeatsinkStatus.setStatus("current")
_TlpPduHeatsinkTemperatureC_Type = Integer32
_TlpPduHeatsinkTemperatureC_Object = MibTableColumn
tlpPduHeatsinkTemperatureC = _TlpPduHeatsinkTemperatureC_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 6, 1, 1, 3),
    _TlpPduHeatsinkTemperatureC_Type()
)
tlpPduHeatsinkTemperatureC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduHeatsinkTemperatureC.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduHeatsinkTemperatureC.setUnits("0.1 degrees Celsius")
_TlpPduHeatsinkTemperatureF_Type = Integer32
_TlpPduHeatsinkTemperatureF_Object = MibTableColumn
tlpPduHeatsinkTemperatureF = _TlpPduHeatsinkTemperatureF_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 6, 1, 1, 4),
    _TlpPduHeatsinkTemperatureF_Type()
)
tlpPduHeatsinkTemperatureF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduHeatsinkTemperatureF.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduHeatsinkTemperatureF.setUnits("0.1 degrees Fahrenheit")
_TlpPduControl_ObjectIdentity = ObjectIdentity
tlpPduControl = _TlpPduControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 4)
)
_TlpPduControlTable_Object = MibTable
tlpPduControlTable = _TlpPduControlTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 4, 1)
)
if mibBuilder.loadTexts:
    tlpPduControlTable.setStatus("current")
_TlpPduControlEntry_Object = MibTableRow
tlpPduControlEntry = _TlpPduControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 4, 1, 1)
)
tlpPduControlEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpPduControlEntry.setStatus("current")
_TlpPduControlRamp_Type = TruthValue
_TlpPduControlRamp_Object = MibTableColumn
tlpPduControlRamp = _TlpPduControlRamp_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 4, 1, 1, 1),
    _TlpPduControlRamp_Type()
)
tlpPduControlRamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduControlRamp.setStatus("current")
_TlpPduControlShed_Type = TruthValue
_TlpPduControlShed_Object = MibTableColumn
tlpPduControlShed = _TlpPduControlShed_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 4, 1, 1, 2),
    _TlpPduControlShed_Type()
)
tlpPduControlShed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduControlShed.setStatus("current")
_TlpPduControlPduOn_Type = TruthValue
_TlpPduControlPduOn_Object = MibTableColumn
tlpPduControlPduOn = _TlpPduControlPduOn_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 4, 1, 1, 3),
    _TlpPduControlPduOn_Type()
)
tlpPduControlPduOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduControlPduOn.setStatus("current")
_TlpPduControlPduOff_Type = TruthValue
_TlpPduControlPduOff_Object = MibTableColumn
tlpPduControlPduOff = _TlpPduControlPduOff_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 4, 1, 1, 4),
    _TlpPduControlPduOff_Type()
)
tlpPduControlPduOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduControlPduOff.setStatus("current")
_TlpPduControlPduRestart_Type = TruthValue
_TlpPduControlPduRestart_Object = MibTableColumn
tlpPduControlPduRestart = _TlpPduControlPduRestart_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 4, 1, 1, 5),
    _TlpPduControlPduRestart_Type()
)
tlpPduControlPduRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduControlPduRestart.setStatus("current")
_TlpPduControlResetGeneralFault_Type = TruthValue
_TlpPduControlResetGeneralFault_Object = MibTableColumn
tlpPduControlResetGeneralFault = _TlpPduControlResetGeneralFault_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 4, 1, 1, 6),
    _TlpPduControlResetGeneralFault_Type()
)
tlpPduControlResetGeneralFault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduControlResetGeneralFault.setStatus("current")
_TlpPduControlResetWattHours_Type = TruthValue
_TlpPduControlResetWattHours_Object = MibTableColumn
tlpPduControlResetWattHours = _TlpPduControlResetWattHours_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 4, 1, 1, 7),
    _TlpPduControlResetWattHours_Type()
)
tlpPduControlResetWattHours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduControlResetWattHours.setStatus("current")
_TlpPduControlResetPeakPower_Type = TruthValue
_TlpPduControlResetPeakPower_Object = MibTableColumn
tlpPduControlResetPeakPower = _TlpPduControlResetPeakPower_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 4, 1, 1, 8),
    _TlpPduControlResetPeakPower_Type()
)
tlpPduControlResetPeakPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduControlResetPeakPower.setStatus("current")
_TlpPduControlClearEventLog_Type = TruthValue
_TlpPduControlClearEventLog_Object = MibTableColumn
tlpPduControlClearEventLog = _TlpPduControlClearEventLog_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 4, 1, 1, 9),
    _TlpPduControlClearEventLog_Type()
)
tlpPduControlClearEventLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduControlClearEventLog.setStatus("current")
_TlpPduControlOutputPhaseTable_Object = MibTable
tlpPduControlOutputPhaseTable = _TlpPduControlOutputPhaseTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 4, 2)
)
if mibBuilder.loadTexts:
    tlpPduControlOutputPhaseTable.setStatus("current")
_TlpPduControlOutputPhaseEntry_Object = MibTableRow
tlpPduControlOutputPhaseEntry = _TlpPduControlOutputPhaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 4, 2, 1)
)
tlpPduControlOutputPhaseEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpPduOutputIndex"),
)
if mibBuilder.loadTexts:
    tlpPduControlOutputPhaseEntry.setStatus("current")
_TlpPduControlResetOutputCurrentMinMax_Type = TruthValue
_TlpPduControlResetOutputCurrentMinMax_Object = MibTableColumn
tlpPduControlResetOutputCurrentMinMax = _TlpPduControlResetOutputCurrentMinMax_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 4, 2, 1, 1),
    _TlpPduControlResetOutputCurrentMinMax_Type()
)
tlpPduControlResetOutputCurrentMinMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduControlResetOutputCurrentMinMax.setStatus("current")
_TlpPduControlInputPhaseTable_Object = MibTable
tlpPduControlInputPhaseTable = _TlpPduControlInputPhaseTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 4, 3)
)
if mibBuilder.loadTexts:
    tlpPduControlInputPhaseTable.setStatus("current")
_TlpPduControlInputPhaseEntry_Object = MibTableRow
tlpPduControlInputPhaseEntry = _TlpPduControlInputPhaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 4, 3, 1)
)
tlpPduControlInputPhaseEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpPduInputPhaseIndex"),
)
if mibBuilder.loadTexts:
    tlpPduControlInputPhaseEntry.setStatus("current")
_TlpPduControlResetInputVoltageMinMax_Type = TruthValue
_TlpPduControlResetInputVoltageMinMax_Object = MibTableColumn
tlpPduControlResetInputVoltageMinMax = _TlpPduControlResetInputVoltageMinMax_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 4, 3, 1, 1),
    _TlpPduControlResetInputVoltageMinMax_Type()
)
tlpPduControlResetInputVoltageMinMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduControlResetInputVoltageMinMax.setStatus("current")
_TlpPduConfig_ObjectIdentity = ObjectIdentity
tlpPduConfig = _TlpPduConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 5)
)
_TlpPduConfigTable_Object = MibTable
tlpPduConfigTable = _TlpPduConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 5, 1)
)
if mibBuilder.loadTexts:
    tlpPduConfigTable.setStatus("current")
_TlpPduConfigEntry_Object = MibTableRow
tlpPduConfigEntry = _TlpPduConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 5, 1, 1)
)
tlpPduConfigEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpPduConfigEntry.setStatus("current")
_TlpPduConfigInputVoltage_Type = Unsigned32
_TlpPduConfigInputVoltage_Object = MibTableColumn
tlpPduConfigInputVoltage = _TlpPduConfigInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 5, 1, 1, 1),
    _TlpPduConfigInputVoltage_Type()
)
tlpPduConfigInputVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduConfigInputVoltage.setStatus("current")


class _TlpPduConfigIsoBreakerSetting_Type(Integer32):
    """Custom type tlpPduConfigIsoBreakerSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 4))
    )


_TlpPduConfigIsoBreakerSetting_Type.__name__ = "Integer32"
_TlpPduConfigIsoBreakerSetting_Object = MibTableColumn
tlpPduConfigIsoBreakerSetting = _TlpPduConfigIsoBreakerSetting_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 5, 1, 1, 2),
    _TlpPduConfigIsoBreakerSetting_Type()
)
tlpPduConfigIsoBreakerSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduConfigIsoBreakerSetting.setStatus("current")


class _TlpPduConfigRelayCalibrationSetting_Type(Integer32):
    """Custom type tlpPduConfigRelayCalibrationSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TlpPduConfigRelayCalibrationSetting_Type.__name__ = "Integer32"
_TlpPduConfigRelayCalibrationSetting_Object = MibTableColumn
tlpPduConfigRelayCalibrationSetting = _TlpPduConfigRelayCalibrationSetting_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 5, 1, 1, 3),
    _TlpPduConfigRelayCalibrationSetting_Type()
)
tlpPduConfigRelayCalibrationSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduConfigRelayCalibrationSetting.setStatus("current")


class _TlpPduConfigThdSetting_Type(Integer32):
    """Custom type tlpPduConfigThdSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TlpPduConfigThdSetting_Type.__name__ = "Integer32"
_TlpPduConfigThdSetting_Object = MibTableColumn
tlpPduConfigThdSetting = _TlpPduConfigThdSetting_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 5, 1, 1, 4),
    _TlpPduConfigThdSetting_Type()
)
tlpPduConfigThdSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduConfigThdSetting.setStatus("current")


class _TlpPduConfigWaveformCaptureSetting_Type(Integer32):
    """Custom type tlpPduConfigWaveformCaptureSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TlpPduConfigWaveformCaptureSetting_Type.__name__ = "Integer32"
_TlpPduConfigWaveformCaptureSetting_Object = MibTableColumn
tlpPduConfigWaveformCaptureSetting = _TlpPduConfigWaveformCaptureSetting_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 5, 1, 1, 5),
    _TlpPduConfigWaveformCaptureSetting_Type()
)
tlpPduConfigWaveformCaptureSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduConfigWaveformCaptureSetting.setStatus("current")


class _TlpPduConfigRemoteResetSetting_Type(Integer32):
    """Custom type tlpPduConfigRemoteResetSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TlpPduConfigRemoteResetSetting_Type.__name__ = "Integer32"
_TlpPduConfigRemoteResetSetting_Object = MibTableColumn
tlpPduConfigRemoteResetSetting = _TlpPduConfigRemoteResetSetting_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 5, 1, 1, 6),
    _TlpPduConfigRemoteResetSetting_Type()
)
tlpPduConfigRemoteResetSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduConfigRemoteResetSetting.setStatus("current")
_TlpPduConfigOutputPhaseThresholdTable_Object = MibTable
tlpPduConfigOutputPhaseThresholdTable = _TlpPduConfigOutputPhaseThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 5, 2)
)
if mibBuilder.loadTexts:
    tlpPduConfigOutputPhaseThresholdTable.setStatus("current")
_TlpPduConfigOutputPhaseThresholdEntry_Object = MibTableRow
tlpPduConfigOutputPhaseThresholdEntry = _TlpPduConfigOutputPhaseThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 5, 2, 1)
)
tlpPduConfigOutputPhaseThresholdEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpPduOutputIndex"),
)
if mibBuilder.loadTexts:
    tlpPduConfigOutputPhaseThresholdEntry.setStatus("current")
_TlpPduConfigOutputCurrentThresholdTolerance_Type = Unsigned32
_TlpPduConfigOutputCurrentThresholdTolerance_Object = MibTableColumn
tlpPduConfigOutputCurrentThresholdTolerance = _TlpPduConfigOutputCurrentThresholdTolerance_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 5, 2, 1, 1),
    _TlpPduConfigOutputCurrentThresholdTolerance_Type()
)
tlpPduConfigOutputCurrentThresholdTolerance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduConfigOutputCurrentThresholdTolerance.setStatus("deprecated")
if mibBuilder.loadTexts:
    tlpPduConfigOutputCurrentThresholdTolerance.setUnits("0.01 Amps")
_TlpPduConfigOutputCurrentHighThreshold_Type = Unsigned32
_TlpPduConfigOutputCurrentHighThreshold_Object = MibTableColumn
tlpPduConfigOutputCurrentHighThreshold = _TlpPduConfigOutputCurrentHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 5, 2, 1, 2),
    _TlpPduConfigOutputCurrentHighThreshold_Type()
)
tlpPduConfigOutputCurrentHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduConfigOutputCurrentHighThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduConfigOutputCurrentHighThreshold.setUnits("0.01 Amps")
_TlpPduConfigOutputCurrentLowThreshold_Type = Unsigned32
_TlpPduConfigOutputCurrentLowThreshold_Object = MibTableColumn
tlpPduConfigOutputCurrentLowThreshold = _TlpPduConfigOutputCurrentLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 5, 2, 1, 3),
    _TlpPduConfigOutputCurrentLowThreshold_Type()
)
tlpPduConfigOutputCurrentLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduConfigOutputCurrentLowThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduConfigOutputCurrentLowThreshold.setUnits("0.01 Amps")
_TlpPduConfigOutputVoltageThresholdTolerance_Type = Unsigned32
_TlpPduConfigOutputVoltageThresholdTolerance_Object = MibTableColumn
tlpPduConfigOutputVoltageThresholdTolerance = _TlpPduConfigOutputVoltageThresholdTolerance_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 5, 2, 1, 4),
    _TlpPduConfigOutputVoltageThresholdTolerance_Type()
)
tlpPduConfigOutputVoltageThresholdTolerance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduConfigOutputVoltageThresholdTolerance.setStatus("deprecated")
if mibBuilder.loadTexts:
    tlpPduConfigOutputVoltageThresholdTolerance.setUnits("0.1 Amps")
_TlpPduConfigOutputVoltageHighCriticalThreshold_Type = Unsigned32
_TlpPduConfigOutputVoltageHighCriticalThreshold_Object = MibTableColumn
tlpPduConfigOutputVoltageHighCriticalThreshold = _TlpPduConfigOutputVoltageHighCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 5, 2, 1, 5),
    _TlpPduConfigOutputVoltageHighCriticalThreshold_Type()
)
tlpPduConfigOutputVoltageHighCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduConfigOutputVoltageHighCriticalThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduConfigOutputVoltageHighCriticalThreshold.setUnits("0.1 Volts")
_TlpPduConfigOutputVoltageHighWarningThreshold_Type = Unsigned32
_TlpPduConfigOutputVoltageHighWarningThreshold_Object = MibTableColumn
tlpPduConfigOutputVoltageHighWarningThreshold = _TlpPduConfigOutputVoltageHighWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 5, 2, 1, 6),
    _TlpPduConfigOutputVoltageHighWarningThreshold_Type()
)
tlpPduConfigOutputVoltageHighWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduConfigOutputVoltageHighWarningThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduConfigOutputVoltageHighWarningThreshold.setUnits("0.1 Volts")
_TlpPduConfigOutputVoltageLowWarningThreshold_Type = Unsigned32
_TlpPduConfigOutputVoltageLowWarningThreshold_Object = MibTableColumn
tlpPduConfigOutputVoltageLowWarningThreshold = _TlpPduConfigOutputVoltageLowWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 5, 2, 1, 7),
    _TlpPduConfigOutputVoltageLowWarningThreshold_Type()
)
tlpPduConfigOutputVoltageLowWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduConfigOutputVoltageLowWarningThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduConfigOutputVoltageLowWarningThreshold.setUnits("0.1 Volts")
_TlpPduConfigOutputVoltageLowCriticalThreshold_Type = Unsigned32
_TlpPduConfigOutputVoltageLowCriticalThreshold_Object = MibTableColumn
tlpPduConfigOutputVoltageLowCriticalThreshold = _TlpPduConfigOutputVoltageLowCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 5, 2, 1, 8),
    _TlpPduConfigOutputVoltageLowCriticalThreshold_Type()
)
tlpPduConfigOutputVoltageLowCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduConfigOutputVoltageLowCriticalThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduConfigOutputVoltageLowCriticalThreshold.setUnits("0.1 Volts")
_TlpPduConfigInputPhaseThresholdTable_Object = MibTable
tlpPduConfigInputPhaseThresholdTable = _TlpPduConfigInputPhaseThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 5, 3)
)
if mibBuilder.loadTexts:
    tlpPduConfigInputPhaseThresholdTable.setStatus("current")
_TlpPduConfigInputPhaseThresholdEntry_Object = MibTableRow
tlpPduConfigInputPhaseThresholdEntry = _TlpPduConfigInputPhaseThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 5, 3, 1)
)
tlpPduConfigInputPhaseThresholdEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpPduInputPhaseIndex"),
)
if mibBuilder.loadTexts:
    tlpPduConfigInputPhaseThresholdEntry.setStatus("current")
_TlpPduConfigInputVoltageThresholdTolerance_Type = Unsigned32
_TlpPduConfigInputVoltageThresholdTolerance_Object = MibTableColumn
tlpPduConfigInputVoltageThresholdTolerance = _TlpPduConfigInputVoltageThresholdTolerance_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 5, 3, 1, 1),
    _TlpPduConfigInputVoltageThresholdTolerance_Type()
)
tlpPduConfigInputVoltageThresholdTolerance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduConfigInputVoltageThresholdTolerance.setStatus("deprecated")
if mibBuilder.loadTexts:
    tlpPduConfigInputVoltageThresholdTolerance.setUnits("0.1 Amps")
_TlpPduConfigInputVoltageHighCriticalThreshold_Type = Unsigned32
_TlpPduConfigInputVoltageHighCriticalThreshold_Object = MibTableColumn
tlpPduConfigInputVoltageHighCriticalThreshold = _TlpPduConfigInputVoltageHighCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 5, 3, 1, 2),
    _TlpPduConfigInputVoltageHighCriticalThreshold_Type()
)
tlpPduConfigInputVoltageHighCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduConfigInputVoltageHighCriticalThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduConfigInputVoltageHighCriticalThreshold.setUnits("0.1 Volts")
_TlpPduConfigInputVoltageHighWarningThreshold_Type = Unsigned32
_TlpPduConfigInputVoltageHighWarningThreshold_Object = MibTableColumn
tlpPduConfigInputVoltageHighWarningThreshold = _TlpPduConfigInputVoltageHighWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 5, 3, 1, 3),
    _TlpPduConfigInputVoltageHighWarningThreshold_Type()
)
tlpPduConfigInputVoltageHighWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduConfigInputVoltageHighWarningThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduConfigInputVoltageHighWarningThreshold.setUnits("0.1 Volts")
_TlpPduConfigInputVoltageLowWarningThreshold_Type = Unsigned32
_TlpPduConfigInputVoltageLowWarningThreshold_Object = MibTableColumn
tlpPduConfigInputVoltageLowWarningThreshold = _TlpPduConfigInputVoltageLowWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 5, 3, 1, 4),
    _TlpPduConfigInputVoltageLowWarningThreshold_Type()
)
tlpPduConfigInputVoltageLowWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduConfigInputVoltageLowWarningThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduConfigInputVoltageLowWarningThreshold.setUnits("0.1 Volts")
_TlpPduConfigInputVoltageLowCriticalThreshold_Type = Unsigned32
_TlpPduConfigInputVoltageLowCriticalThreshold_Object = MibTableColumn
tlpPduConfigInputVoltageLowCriticalThreshold = _TlpPduConfigInputVoltageLowCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 5, 3, 1, 5),
    _TlpPduConfigInputVoltageLowCriticalThreshold_Type()
)
tlpPduConfigInputVoltageLowCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduConfigInputVoltageLowCriticalThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduConfigInputVoltageLowCriticalThreshold.setUnits("0.1 Volts")
_TlpPduConfigThresholdTable_Object = MibTable
tlpPduConfigThresholdTable = _TlpPduConfigThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 5, 4)
)
if mibBuilder.loadTexts:
    tlpPduConfigThresholdTable.setStatus("current")
_TlpPduConfigThresholdEntry_Object = MibTableRow
tlpPduConfigThresholdEntry = _TlpPduConfigThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 5, 4, 1)
)
tlpPduConfigThresholdEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpPduConfigThresholdEntry.setStatus("current")


class _TlpPduConfigThdOutOfRangeThreshold_Type(Unsigned32):
    """Custom type tlpPduConfigThdOutOfRangeThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_TlpPduConfigThdOutOfRangeThreshold_Type.__name__ = "Unsigned32"
_TlpPduConfigThdOutOfRangeThreshold_Object = MibTableColumn
tlpPduConfigThdOutOfRangeThreshold = _TlpPduConfigThdOutOfRangeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 5, 4, 1, 1),
    _TlpPduConfigThdOutOfRangeThreshold_Type()
)
tlpPduConfigThdOutOfRangeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduConfigThdOutOfRangeThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduConfigThdOutOfRangeThreshold.setUnits("0.01 percent")
_TlpEnvirosense_ObjectIdentity = ObjectIdentity
tlpEnvirosense = _TlpEnvirosense_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3)
)
_TlpEnvIdent_ObjectIdentity = ObjectIdentity
tlpEnvIdent = _TlpEnvIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 1)
)
_TlpEnvIdentNumEnvirosense_Type = Unsigned32
_TlpEnvIdentNumEnvirosense_Object = MibScalar
tlpEnvIdentNumEnvirosense = _TlpEnvIdentNumEnvirosense_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 1, 1),
    _TlpEnvIdentNumEnvirosense_Type()
)
tlpEnvIdentNumEnvirosense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpEnvIdentNumEnvirosense.setStatus("current")
_TlpEnvIdentTable_Object = MibTable
tlpEnvIdentTable = _TlpEnvIdentTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 1, 2)
)
if mibBuilder.loadTexts:
    tlpEnvIdentTable.setStatus("current")
_TlpEnvIdentEntry_Object = MibTableRow
tlpEnvIdentEntry = _TlpEnvIdentEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 1, 2, 1)
)
tlpEnvIdentEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpEnvIdentEntry.setStatus("current")
_TlpEnvIdentTempSupported_Type = TruthValue
_TlpEnvIdentTempSupported_Object = MibTableColumn
tlpEnvIdentTempSupported = _TlpEnvIdentTempSupported_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 1, 2, 1, 1),
    _TlpEnvIdentTempSupported_Type()
)
tlpEnvIdentTempSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpEnvIdentTempSupported.setStatus("current")
_TlpEnvIdentHumiditySupported_Type = TruthValue
_TlpEnvIdentHumiditySupported_Object = MibTableColumn
tlpEnvIdentHumiditySupported = _TlpEnvIdentHumiditySupported_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 1, 2, 1, 2),
    _TlpEnvIdentHumiditySupported_Type()
)
tlpEnvIdentHumiditySupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpEnvIdentHumiditySupported.setStatus("current")
_TlpEnvNumInputContacts_Type = Unsigned32
_TlpEnvNumInputContacts_Object = MibTableColumn
tlpEnvNumInputContacts = _TlpEnvNumInputContacts_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 1, 2, 1, 3),
    _TlpEnvNumInputContacts_Type()
)
tlpEnvNumInputContacts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpEnvNumInputContacts.setStatus("current")
_TlpEnvNumOutputContacts_Type = Unsigned32
_TlpEnvNumOutputContacts_Object = MibTableColumn
tlpEnvNumOutputContacts = _TlpEnvNumOutputContacts_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 1, 2, 1, 4),
    _TlpEnvNumOutputContacts_Type()
)
tlpEnvNumOutputContacts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpEnvNumOutputContacts.setStatus("current")
_TlpEnvDetail_ObjectIdentity = ObjectIdentity
tlpEnvDetail = _TlpEnvDetail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 3)
)
_TlpEnvTemperatureTable_Object = MibTable
tlpEnvTemperatureTable = _TlpEnvTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 3, 1)
)
if mibBuilder.loadTexts:
    tlpEnvTemperatureTable.setStatus("current")
_TlpEnvTemperatureEntry_Object = MibTableRow
tlpEnvTemperatureEntry = _TlpEnvTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 3, 1, 1)
)
tlpEnvTemperatureEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpEnvTemperatureEntry.setStatus("current")
_TlpEnvTemperatureC_Type = Integer32
_TlpEnvTemperatureC_Object = MibTableColumn
tlpEnvTemperatureC = _TlpEnvTemperatureC_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 3, 1, 1, 1),
    _TlpEnvTemperatureC_Type()
)
tlpEnvTemperatureC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpEnvTemperatureC.setStatus("current")
if mibBuilder.loadTexts:
    tlpEnvTemperatureC.setUnits("0.1 degrees Celsius")
_TlpEnvTemperatureF_Type = Integer32
_TlpEnvTemperatureF_Object = MibTableColumn
tlpEnvTemperatureF = _TlpEnvTemperatureF_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 3, 1, 1, 2),
    _TlpEnvTemperatureF_Type()
)
tlpEnvTemperatureF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpEnvTemperatureF.setStatus("current")
if mibBuilder.loadTexts:
    tlpEnvTemperatureF.setUnits("0.1 degrees Fahrenheit")
_TlpEnvTemperatureInAlarm_Type = TruthValue
_TlpEnvTemperatureInAlarm_Object = MibTableColumn
tlpEnvTemperatureInAlarm = _TlpEnvTemperatureInAlarm_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 3, 1, 1, 3),
    _TlpEnvTemperatureInAlarm_Type()
)
tlpEnvTemperatureInAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpEnvTemperatureInAlarm.setStatus("current")
_TlpEnvHumidityTable_Object = MibTable
tlpEnvHumidityTable = _TlpEnvHumidityTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 3, 2)
)
if mibBuilder.loadTexts:
    tlpEnvHumidityTable.setStatus("current")
_TlpEnvHumidityEntry_Object = MibTableRow
tlpEnvHumidityEntry = _TlpEnvHumidityEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 3, 2, 1)
)
tlpEnvHumidityEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpEnvHumidityEntry.setStatus("current")


class _TlpEnvHumidityHumidity_Type(Integer32):
    """Custom type tlpEnvHumidityHumidity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TlpEnvHumidityHumidity_Type.__name__ = "Integer32"
_TlpEnvHumidityHumidity_Object = MibTableColumn
tlpEnvHumidityHumidity = _TlpEnvHumidityHumidity_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 3, 2, 1, 1),
    _TlpEnvHumidityHumidity_Type()
)
tlpEnvHumidityHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpEnvHumidityHumidity.setStatus("current")
if mibBuilder.loadTexts:
    tlpEnvHumidityHumidity.setUnits("percent")
_TlpEnvHumidityInAlarm_Type = TruthValue
_TlpEnvHumidityInAlarm_Object = MibTableColumn
tlpEnvHumidityInAlarm = _TlpEnvHumidityInAlarm_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 3, 2, 1, 2),
    _TlpEnvHumidityInAlarm_Type()
)
tlpEnvHumidityInAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpEnvHumidityInAlarm.setStatus("current")
_TlpEnvInputContactTable_Object = MibTable
tlpEnvInputContactTable = _TlpEnvInputContactTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 3, 3)
)
if mibBuilder.loadTexts:
    tlpEnvInputContactTable.setStatus("current")
_TlpEnvInputContactEntry_Object = MibTableRow
tlpEnvInputContactEntry = _TlpEnvInputContactEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 3, 3, 1)
)
tlpEnvInputContactEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpEnvInputContactIndex"),
)
if mibBuilder.loadTexts:
    tlpEnvInputContactEntry.setStatus("current")
_TlpEnvInputContactIndex_Type = Unsigned32
_TlpEnvInputContactIndex_Object = MibTableColumn
tlpEnvInputContactIndex = _TlpEnvInputContactIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 3, 3, 1, 1),
    _TlpEnvInputContactIndex_Type()
)
tlpEnvInputContactIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpEnvInputContactIndex.setStatus("current")
_TlpEnvInputContactName_Type = DisplayString
_TlpEnvInputContactName_Object = MibTableColumn
tlpEnvInputContactName = _TlpEnvInputContactName_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 3, 3, 1, 2),
    _TlpEnvInputContactName_Type()
)
tlpEnvInputContactName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpEnvInputContactName.setStatus("current")


class _TlpEnvInputContactNormalState_Type(Integer32):
    """Custom type tlpEnvInputContactNormalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("open", 0),
          ("closed", 1))
    )


_TlpEnvInputContactNormalState_Type.__name__ = "Integer32"
_TlpEnvInputContactNormalState_Object = MibTableColumn
tlpEnvInputContactNormalState = _TlpEnvInputContactNormalState_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 3, 3, 1, 3),
    _TlpEnvInputContactNormalState_Type()
)
tlpEnvInputContactNormalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpEnvInputContactNormalState.setStatus("current")


class _TlpEnvInputContactCurrentState_Type(Integer32):
    """Custom type tlpEnvInputContactCurrentState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("open", 0),
          ("closed", 1))
    )


_TlpEnvInputContactCurrentState_Type.__name__ = "Integer32"
_TlpEnvInputContactCurrentState_Object = MibTableColumn
tlpEnvInputContactCurrentState = _TlpEnvInputContactCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 3, 3, 1, 4),
    _TlpEnvInputContactCurrentState_Type()
)
tlpEnvInputContactCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpEnvInputContactCurrentState.setStatus("current")
_TlpEnvInputContactInAlarm_Type = TruthValue
_TlpEnvInputContactInAlarm_Object = MibTableColumn
tlpEnvInputContactInAlarm = _TlpEnvInputContactInAlarm_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 3, 3, 1, 5),
    _TlpEnvInputContactInAlarm_Type()
)
tlpEnvInputContactInAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpEnvInputContactInAlarm.setStatus("current")
_TlpEnvOutputContactTable_Object = MibTable
tlpEnvOutputContactTable = _TlpEnvOutputContactTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 3, 4)
)
if mibBuilder.loadTexts:
    tlpEnvOutputContactTable.setStatus("current")
_TlpEnvOutputContactEntry_Object = MibTableRow
tlpEnvOutputContactEntry = _TlpEnvOutputContactEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 3, 4, 1)
)
tlpEnvOutputContactEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpEnvOutputContactIndex"),
)
if mibBuilder.loadTexts:
    tlpEnvOutputContactEntry.setStatus("current")
_TlpEnvOutputContactIndex_Type = Unsigned32
_TlpEnvOutputContactIndex_Object = MibTableColumn
tlpEnvOutputContactIndex = _TlpEnvOutputContactIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 3, 4, 1, 1),
    _TlpEnvOutputContactIndex_Type()
)
tlpEnvOutputContactIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpEnvOutputContactIndex.setStatus("current")
_TlpEnvOutputContactName_Type = DisplayString
_TlpEnvOutputContactName_Object = MibTableColumn
tlpEnvOutputContactName = _TlpEnvOutputContactName_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 3, 4, 1, 2),
    _TlpEnvOutputContactName_Type()
)
tlpEnvOutputContactName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpEnvOutputContactName.setStatus("current")


class _TlpEnvOutputContactNormalState_Type(Integer32):
    """Custom type tlpEnvOutputContactNormalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("open", 0),
          ("closed", 1))
    )


_TlpEnvOutputContactNormalState_Type.__name__ = "Integer32"
_TlpEnvOutputContactNormalState_Object = MibTableColumn
tlpEnvOutputContactNormalState = _TlpEnvOutputContactNormalState_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 3, 4, 1, 3),
    _TlpEnvOutputContactNormalState_Type()
)
tlpEnvOutputContactNormalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpEnvOutputContactNormalState.setStatus("current")


class _TlpEnvOutputContactCurrentState_Type(Integer32):
    """Custom type tlpEnvOutputContactCurrentState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("open", 0),
          ("closed", 1))
    )


_TlpEnvOutputContactCurrentState_Type.__name__ = "Integer32"
_TlpEnvOutputContactCurrentState_Object = MibTableColumn
tlpEnvOutputContactCurrentState = _TlpEnvOutputContactCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 3, 4, 1, 4),
    _TlpEnvOutputContactCurrentState_Type()
)
tlpEnvOutputContactCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpEnvOutputContactCurrentState.setStatus("current")
_TlpEnvOutputContactInAlarm_Type = TruthValue
_TlpEnvOutputContactInAlarm_Object = MibTableColumn
tlpEnvOutputContactInAlarm = _TlpEnvOutputContactInAlarm_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 3, 4, 1, 5),
    _TlpEnvOutputContactInAlarm_Type()
)
tlpEnvOutputContactInAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpEnvOutputContactInAlarm.setStatus("current")
_TlpEnvControl_ObjectIdentity = ObjectIdentity
tlpEnvControl = _TlpEnvControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 4)
)
_TlpEnvControlOutputContactTable_Object = MibTable
tlpEnvControlOutputContactTable = _TlpEnvControlOutputContactTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 4, 1)
)
if mibBuilder.loadTexts:
    tlpEnvControlOutputContactTable.setStatus("current")
_TlpEnvControlOutputContactEntry_Object = MibTableRow
tlpEnvControlOutputContactEntry = _TlpEnvControlOutputContactEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 4, 1, 1)
)
tlpEnvControlOutputContactEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpEnvOutputContactIndex"),
)
if mibBuilder.loadTexts:
    tlpEnvControlOutputContactEntry.setStatus("current")
_TlpEnvControlOutputContactOpen_Type = TruthValue
_TlpEnvControlOutputContactOpen_Object = MibTableColumn
tlpEnvControlOutputContactOpen = _TlpEnvControlOutputContactOpen_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 4, 1, 1, 1),
    _TlpEnvControlOutputContactOpen_Type()
)
tlpEnvControlOutputContactOpen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpEnvControlOutputContactOpen.setStatus("current")
_TlpEnvControlOutputContactClose_Type = TruthValue
_TlpEnvControlOutputContactClose_Object = MibTableColumn
tlpEnvControlOutputContactClose = _TlpEnvControlOutputContactClose_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 4, 1, 1, 2),
    _TlpEnvControlOutputContactClose_Type()
)
tlpEnvControlOutputContactClose.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpEnvControlOutputContactClose.setStatus("current")
_TlpEnvConfig_ObjectIdentity = ObjectIdentity
tlpEnvConfig = _TlpEnvConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 5)
)
_TlpEnvConfigTable_Object = MibTable
tlpEnvConfigTable = _TlpEnvConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 5, 1)
)
if mibBuilder.loadTexts:
    tlpEnvConfigTable.setStatus("current")
_TlpEnvConfigEntry_Object = MibTableRow
tlpEnvConfigEntry = _TlpEnvConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 5, 1, 1)
)
tlpEnvConfigEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpEnvConfigEntry.setStatus("current")
_TlpEnvTemperatureLowLimit_Type = Integer32
_TlpEnvTemperatureLowLimit_Object = MibTableColumn
tlpEnvTemperatureLowLimit = _TlpEnvTemperatureLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 5, 1, 1, 1),
    _TlpEnvTemperatureLowLimit_Type()
)
tlpEnvTemperatureLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpEnvTemperatureLowLimit.setStatus("current")
if mibBuilder.loadTexts:
    tlpEnvTemperatureLowLimit.setUnits("degrees Fahrenheit")
_TlpEnvTemperatureHighLimit_Type = Integer32
_TlpEnvTemperatureHighLimit_Object = MibTableColumn
tlpEnvTemperatureHighLimit = _TlpEnvTemperatureHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 5, 1, 1, 2),
    _TlpEnvTemperatureHighLimit_Type()
)
tlpEnvTemperatureHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpEnvTemperatureHighLimit.setStatus("current")
if mibBuilder.loadTexts:
    tlpEnvTemperatureHighLimit.setUnits("degrees Fahrenheit")


class _TlpEnvHumidityLowLimit_Type(Integer32):
    """Custom type tlpEnvHumidityLowLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TlpEnvHumidityLowLimit_Type.__name__ = "Integer32"
_TlpEnvHumidityLowLimit_Object = MibTableColumn
tlpEnvHumidityLowLimit = _TlpEnvHumidityLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 5, 1, 1, 3),
    _TlpEnvHumidityLowLimit_Type()
)
tlpEnvHumidityLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpEnvHumidityLowLimit.setStatus("current")
if mibBuilder.loadTexts:
    tlpEnvHumidityLowLimit.setUnits("percent")


class _TlpEnvHumidityHighLimit_Type(Integer32):
    """Custom type tlpEnvHumidityHighLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TlpEnvHumidityHighLimit_Type.__name__ = "Integer32"
_TlpEnvHumidityHighLimit_Object = MibTableColumn
tlpEnvHumidityHighLimit = _TlpEnvHumidityHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 5, 1, 1, 4),
    _TlpEnvHumidityHighLimit_Type()
)
tlpEnvHumidityHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpEnvHumidityHighLimit.setStatus("current")
if mibBuilder.loadTexts:
    tlpEnvHumidityHighLimit.setUnits("percent")
_TlpAts_ObjectIdentity = ObjectIdentity
tlpAts = _TlpAts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4)
)
_TlpAtsIdent_ObjectIdentity = ObjectIdentity
tlpAtsIdent = _TlpAtsIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 1)
)
_TlpAtsIdentNumAts_Type = Unsigned32
_TlpAtsIdentNumAts_Object = MibScalar
tlpAtsIdentNumAts = _TlpAtsIdentNumAts_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 1, 1),
    _TlpAtsIdentNumAts_Type()
)
tlpAtsIdentNumAts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsIdentNumAts.setStatus("current")
_TlpAtsIdentTable_Object = MibTable
tlpAtsIdentTable = _TlpAtsIdentTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 1, 2)
)
if mibBuilder.loadTexts:
    tlpAtsIdentTable.setStatus("current")
_TlpAtsIdentEntry_Object = MibTableRow
tlpAtsIdentEntry = _TlpAtsIdentEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 1, 2, 1)
)
tlpAtsIdentEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpAtsIdentEntry.setStatus("current")
_TlpAtsIdentNumInputs_Type = Unsigned32
_TlpAtsIdentNumInputs_Object = MibTableColumn
tlpAtsIdentNumInputs = _TlpAtsIdentNumInputs_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 1, 2, 1, 1),
    _TlpAtsIdentNumInputs_Type()
)
tlpAtsIdentNumInputs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsIdentNumInputs.setStatus("current")
_TlpAtsIdentNumOutputs_Type = Unsigned32
_TlpAtsIdentNumOutputs_Object = MibTableColumn
tlpAtsIdentNumOutputs = _TlpAtsIdentNumOutputs_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 1, 2, 1, 2),
    _TlpAtsIdentNumOutputs_Type()
)
tlpAtsIdentNumOutputs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsIdentNumOutputs.setStatus("current")
_TlpAtsIdentNumPhases_Type = Unsigned32
_TlpAtsIdentNumPhases_Object = MibTableColumn
tlpAtsIdentNumPhases = _TlpAtsIdentNumPhases_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 1, 2, 1, 3),
    _TlpAtsIdentNumPhases_Type()
)
tlpAtsIdentNumPhases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsIdentNumPhases.setStatus("current")
_TlpAtsIdentNumOutlets_Type = Unsigned32
_TlpAtsIdentNumOutlets_Object = MibTableColumn
tlpAtsIdentNumOutlets = _TlpAtsIdentNumOutlets_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 1, 2, 1, 4),
    _TlpAtsIdentNumOutlets_Type()
)
tlpAtsIdentNumOutlets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsIdentNumOutlets.setStatus("current")
_TlpAtsIdentNumOutletGroups_Type = Unsigned32
_TlpAtsIdentNumOutletGroups_Object = MibTableColumn
tlpAtsIdentNumOutletGroups = _TlpAtsIdentNumOutletGroups_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 1, 2, 1, 5),
    _TlpAtsIdentNumOutletGroups_Type()
)
tlpAtsIdentNumOutletGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsIdentNumOutletGroups.setStatus("current")
_TlpAtsIdentNumCircuits_Type = Unsigned32
_TlpAtsIdentNumCircuits_Object = MibTableColumn
tlpAtsIdentNumCircuits = _TlpAtsIdentNumCircuits_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 1, 2, 1, 6),
    _TlpAtsIdentNumCircuits_Type()
)
tlpAtsIdentNumCircuits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsIdentNumCircuits.setStatus("current")
_TlpAtsIdentNumBreakers_Type = Unsigned32
_TlpAtsIdentNumBreakers_Object = MibTableColumn
tlpAtsIdentNumBreakers = _TlpAtsIdentNumBreakers_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 1, 2, 1, 7),
    _TlpAtsIdentNumBreakers_Type()
)
tlpAtsIdentNumBreakers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsIdentNumBreakers.setStatus("current")
_TlpAtsIdentNumHeatsinks_Type = Unsigned32
_TlpAtsIdentNumHeatsinks_Object = MibTableColumn
tlpAtsIdentNumHeatsinks = _TlpAtsIdentNumHeatsinks_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 1, 2, 1, 8),
    _TlpAtsIdentNumHeatsinks_Type()
)
tlpAtsIdentNumHeatsinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsIdentNumHeatsinks.setStatus("current")
_TlpAtsSupportsTable_Object = MibTable
tlpAtsSupportsTable = _TlpAtsSupportsTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 1, 3)
)
if mibBuilder.loadTexts:
    tlpAtsSupportsTable.setStatus("current")
_TlpAtsSupportsEntry_Object = MibTableRow
tlpAtsSupportsEntry = _TlpAtsSupportsEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 1, 3, 1)
)
tlpAtsSupportsEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpAtsSupportsEntry.setStatus("current")
_TlpAtsSupportsEnergywise_Type = TruthValue
_TlpAtsSupportsEnergywise_Object = MibTableColumn
tlpAtsSupportsEnergywise = _TlpAtsSupportsEnergywise_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 1, 3, 1, 1),
    _TlpAtsSupportsEnergywise_Type()
)
tlpAtsSupportsEnergywise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsSupportsEnergywise.setStatus("deprecated")
_TlpAtsSupportsRampShed_Type = TruthValue
_TlpAtsSupportsRampShed_Object = MibTableColumn
tlpAtsSupportsRampShed = _TlpAtsSupportsRampShed_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 1, 3, 1, 2),
    _TlpAtsSupportsRampShed_Type()
)
tlpAtsSupportsRampShed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsSupportsRampShed.setStatus("current")
_TlpAtsSupportsOutletGroup_Type = TruthValue
_TlpAtsSupportsOutletGroup_Object = MibTableColumn
tlpAtsSupportsOutletGroup = _TlpAtsSupportsOutletGroup_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 1, 3, 1, 3),
    _TlpAtsSupportsOutletGroup_Type()
)
tlpAtsSupportsOutletGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsSupportsOutletGroup.setStatus("current")
_TlpAtsSupportsOutletCurrent_Type = TruthValue
_TlpAtsSupportsOutletCurrent_Object = MibTableColumn
tlpAtsSupportsOutletCurrent = _TlpAtsSupportsOutletCurrent_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 1, 3, 1, 4),
    _TlpAtsSupportsOutletCurrent_Type()
)
tlpAtsSupportsOutletCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsSupportsOutletCurrent.setStatus("current")
_TlpAtsSupportsOutletVoltage_Type = TruthValue
_TlpAtsSupportsOutletVoltage_Object = MibTableColumn
tlpAtsSupportsOutletVoltage = _TlpAtsSupportsOutletVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 1, 3, 1, 5),
    _TlpAtsSupportsOutletVoltage_Type()
)
tlpAtsSupportsOutletVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsSupportsOutletVoltage.setStatus("current")
_TlpAtsSupportsOutletActivePower_Type = TruthValue
_TlpAtsSupportsOutletActivePower_Object = MibTableColumn
tlpAtsSupportsOutletActivePower = _TlpAtsSupportsOutletActivePower_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 1, 3, 1, 6),
    _TlpAtsSupportsOutletActivePower_Type()
)
tlpAtsSupportsOutletActivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsSupportsOutletActivePower.setStatus("current")
_TlpAtsDisplayTable_Object = MibTable
tlpAtsDisplayTable = _TlpAtsDisplayTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 1, 4)
)
if mibBuilder.loadTexts:
    tlpAtsDisplayTable.setStatus("deprecated")
_TlpAtsDisplayEntry_Object = MibTableRow
tlpAtsDisplayEntry = _TlpAtsDisplayEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 1, 4, 1)
)
tlpAtsDisplayEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpAtsDisplayEntry.setStatus("deprecated")


class _TlpAtsDisplayScheme_Type(Integer32):
    """Custom type tlpAtsDisplayScheme based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("schemeReverse", 0),
          ("schemeNormal", 1))
    )


_TlpAtsDisplayScheme_Type.__name__ = "Integer32"
_TlpAtsDisplayScheme_Object = MibTableColumn
tlpAtsDisplayScheme = _TlpAtsDisplayScheme_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 1, 4, 1, 1),
    _TlpAtsDisplayScheme_Type()
)
tlpAtsDisplayScheme.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsDisplayScheme.setStatus("deprecated")


class _TlpAtsDisplayOrientation_Type(Integer32):
    """Custom type tlpAtsDisplayOrientation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("displayNormal", 0),
          ("displayReverse", 1))
    )


_TlpAtsDisplayOrientation_Type.__name__ = "Integer32"
_TlpAtsDisplayOrientation_Object = MibTableColumn
tlpAtsDisplayOrientation = _TlpAtsDisplayOrientation_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 1, 4, 1, 2),
    _TlpAtsDisplayOrientation_Type()
)
tlpAtsDisplayOrientation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsDisplayOrientation.setStatus("deprecated")


class _TlpAtsDisplayAutoScroll_Type(Integer32):
    """Custom type tlpAtsDisplayAutoScroll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("scrollDisabled", 0),
          ("scrollEnabled", 1))
    )


_TlpAtsDisplayAutoScroll_Type.__name__ = "Integer32"
_TlpAtsDisplayAutoScroll_Object = MibTableColumn
tlpAtsDisplayAutoScroll = _TlpAtsDisplayAutoScroll_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 1, 4, 1, 3),
    _TlpAtsDisplayAutoScroll_Type()
)
tlpAtsDisplayAutoScroll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsDisplayAutoScroll.setStatus("deprecated")


class _TlpAtsDisplayIntensity_Type(Integer32):
    """Custom type tlpAtsDisplayIntensity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("intensity25", 1),
          ("intensity50", 2),
          ("intensity75", 3),
          ("intensity100", 4))
    )


_TlpAtsDisplayIntensity_Type.__name__ = "Integer32"
_TlpAtsDisplayIntensity_Object = MibTableColumn
tlpAtsDisplayIntensity = _TlpAtsDisplayIntensity_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 1, 4, 1, 4),
    _TlpAtsDisplayIntensity_Type()
)
tlpAtsDisplayIntensity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsDisplayIntensity.setStatus("deprecated")


class _TlpAtsDisplayUnits_Type(Integer32):
    """Custom type tlpAtsDisplayUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("metric", 1))
    )


_TlpAtsDisplayUnits_Type.__name__ = "Integer32"
_TlpAtsDisplayUnits_Object = MibTableColumn
tlpAtsDisplayUnits = _TlpAtsDisplayUnits_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 1, 4, 1, 5),
    _TlpAtsDisplayUnits_Type()
)
tlpAtsDisplayUnits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsDisplayUnits.setStatus("deprecated")
_TlpAtsDevice_ObjectIdentity = ObjectIdentity
tlpAtsDevice = _TlpAtsDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 2)
)
_TlpAtsDeviceTable_Object = MibTable
tlpAtsDeviceTable = _TlpAtsDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 2, 1)
)
if mibBuilder.loadTexts:
    tlpAtsDeviceTable.setStatus("current")
_TlpAtsDeviceEntry_Object = MibTableRow
tlpAtsDeviceEntry = _TlpAtsDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 2, 1, 1)
)
tlpAtsDeviceEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpAtsDeviceEntry.setStatus("current")


class _TlpAtsDeviceMainLoadState_Type(Integer32):
    """Custom type tlpAtsDeviceMainLoadState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("off", 1),
          ("on", 2))
    )


_TlpAtsDeviceMainLoadState_Type.__name__ = "Integer32"
_TlpAtsDeviceMainLoadState_Object = MibTableColumn
tlpAtsDeviceMainLoadState = _TlpAtsDeviceMainLoadState_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 2, 1, 1, 1),
    _TlpAtsDeviceMainLoadState_Type()
)
tlpAtsDeviceMainLoadState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsDeviceMainLoadState.setStatus("current")
_TlpAtsDeviceMainLoadControllable_Type = TruthValue
_TlpAtsDeviceMainLoadControllable_Object = MibTableColumn
tlpAtsDeviceMainLoadControllable = _TlpAtsDeviceMainLoadControllable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 2, 1, 1, 2),
    _TlpAtsDeviceMainLoadControllable_Type()
)
tlpAtsDeviceMainLoadControllable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsDeviceMainLoadControllable.setStatus("current")


class _TlpAtsDeviceMainLoadCommand_Type(Integer32):
    """Custom type tlpAtsDeviceMainLoadCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("turnOff", 1),
          ("turnOn", 2),
          ("cycle", 3))
    )


_TlpAtsDeviceMainLoadCommand_Type.__name__ = "Integer32"
_TlpAtsDeviceMainLoadCommand_Object = MibTableColumn
tlpAtsDeviceMainLoadCommand = _TlpAtsDeviceMainLoadCommand_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 2, 1, 1, 3),
    _TlpAtsDeviceMainLoadCommand_Type()
)
tlpAtsDeviceMainLoadCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsDeviceMainLoadCommand.setStatus("current")
_TlpAtsDevicePowerOnDelay_Type = Integer32
_TlpAtsDevicePowerOnDelay_Object = MibTableColumn
tlpAtsDevicePowerOnDelay = _TlpAtsDevicePowerOnDelay_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 2, 1, 1, 4),
    _TlpAtsDevicePowerOnDelay_Type()
)
tlpAtsDevicePowerOnDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsDevicePowerOnDelay.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsDevicePowerOnDelay.setUnits("Seconds")
_TlpAtsDeviceTotalInputPowerRating_Type = Integer32
_TlpAtsDeviceTotalInputPowerRating_Object = MibTableColumn
tlpAtsDeviceTotalInputPowerRating = _TlpAtsDeviceTotalInputPowerRating_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 2, 1, 1, 5),
    _TlpAtsDeviceTotalInputPowerRating_Type()
)
tlpAtsDeviceTotalInputPowerRating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsDeviceTotalInputPowerRating.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsDeviceTotalInputPowerRating.setUnits("Watts")
_TlpAtsDeviceTemperatureC_Type = Integer32
_TlpAtsDeviceTemperatureC_Object = MibTableColumn
tlpAtsDeviceTemperatureC = _TlpAtsDeviceTemperatureC_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 2, 1, 1, 6),
    _TlpAtsDeviceTemperatureC_Type()
)
tlpAtsDeviceTemperatureC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsDeviceTemperatureC.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsDeviceTemperatureC.setUnits("degrees Celsius")
_TlpAtsDeviceTemperatureF_Type = Integer32
_TlpAtsDeviceTemperatureF_Object = MibTableColumn
tlpAtsDeviceTemperatureF = _TlpAtsDeviceTemperatureF_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 2, 1, 1, 7),
    _TlpAtsDeviceTemperatureF_Type()
)
tlpAtsDeviceTemperatureF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsDeviceTemperatureF.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsDeviceTemperatureF.setUnits("degrees Fahrenheit")


class _TlpAtsDevicePhaseImbalance_Type(Integer32):
    """Custom type tlpAtsDevicePhaseImbalance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_TlpAtsDevicePhaseImbalance_Type.__name__ = "Integer32"
_TlpAtsDevicePhaseImbalance_Object = MibTableColumn
tlpAtsDevicePhaseImbalance = _TlpAtsDevicePhaseImbalance_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 2, 1, 1, 8),
    _TlpAtsDevicePhaseImbalance_Type()
)
tlpAtsDevicePhaseImbalance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsDevicePhaseImbalance.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsDevicePhaseImbalance.setUnits("percent")
_TlpAtsDeviceOutputActivePowerTotal_Type = Unsigned32
_TlpAtsDeviceOutputActivePowerTotal_Object = MibTableColumn
tlpAtsDeviceOutputActivePowerTotal = _TlpAtsDeviceOutputActivePowerTotal_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 2, 1, 1, 9),
    _TlpAtsDeviceOutputActivePowerTotal_Type()
)
tlpAtsDeviceOutputActivePowerTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsDeviceOutputActivePowerTotal.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsDeviceOutputActivePowerTotal.setUnits("Watts")
_TlpAtsDeviceAggregatePowerFactor_Type = Unsigned32
_TlpAtsDeviceAggregatePowerFactor_Object = MibTableColumn
tlpAtsDeviceAggregatePowerFactor = _TlpAtsDeviceAggregatePowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 2, 1, 1, 10),
    _TlpAtsDeviceAggregatePowerFactor_Type()
)
tlpAtsDeviceAggregatePowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsDeviceAggregatePowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsDeviceAggregatePowerFactor.setUnits("0.1 Watts")


class _TlpAtsDeviceOutputCurrentPrecision_Type(Integer32):
    """Custom type tlpAtsDeviceOutputCurrentPrecision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("tenths", 1),
          ("hundredths", 2))
    )


_TlpAtsDeviceOutputCurrentPrecision_Type.__name__ = "Integer32"
_TlpAtsDeviceOutputCurrentPrecision_Object = MibTableColumn
tlpAtsDeviceOutputCurrentPrecision = _TlpAtsDeviceOutputCurrentPrecision_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 2, 1, 1, 11),
    _TlpAtsDeviceOutputCurrentPrecision_Type()
)
tlpAtsDeviceOutputCurrentPrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsDeviceOutputCurrentPrecision.setStatus("current")
_TlpAtsDeviceGeneralFault_Type = TruthValue
_TlpAtsDeviceGeneralFault_Object = MibTableColumn
tlpAtsDeviceGeneralFault = _TlpAtsDeviceGeneralFault_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 2, 1, 1, 12),
    _TlpAtsDeviceGeneralFault_Type()
)
tlpAtsDeviceGeneralFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsDeviceGeneralFault.setStatus("current")
_TlpAtsDeviceTotalOutputUtilization_Type = Integer32
_TlpAtsDeviceTotalOutputUtilization_Object = MibTableColumn
tlpAtsDeviceTotalOutputUtilization = _TlpAtsDeviceTotalOutputUtilization_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 2, 1, 1, 13),
    _TlpAtsDeviceTotalOutputUtilization_Type()
)
tlpAtsDeviceTotalOutputUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsDeviceTotalOutputUtilization.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsDeviceTotalOutputUtilization.setUnits("percent")
_TlpAtsDeviceOutputApparentPowerTotal_Type = Unsigned32
_TlpAtsDeviceOutputApparentPowerTotal_Object = MibTableColumn
tlpAtsDeviceOutputApparentPowerTotal = _TlpAtsDeviceOutputApparentPowerTotal_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 2, 1, 1, 14),
    _TlpAtsDeviceOutputApparentPowerTotal_Type()
)
tlpAtsDeviceOutputApparentPowerTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsDeviceOutputApparentPowerTotal.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsDeviceOutputApparentPowerTotal.setUnits("Watts")
_TlpAtsDeviceOutputReactivePowerTotal_Type = Integer32
_TlpAtsDeviceOutputReactivePowerTotal_Object = MibTableColumn
tlpAtsDeviceOutputReactivePowerTotal = _TlpAtsDeviceOutputReactivePowerTotal_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 2, 1, 1, 15),
    _TlpAtsDeviceOutputReactivePowerTotal_Type()
)
tlpAtsDeviceOutputReactivePowerTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsDeviceOutputReactivePowerTotal.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsDeviceOutputReactivePowerTotal.setUnits("Watts")
_TlpAtsDeviceOutputCurrentTotal_Type = Unsigned32
_TlpAtsDeviceOutputCurrentTotal_Object = MibTableColumn
tlpAtsDeviceOutputCurrentTotal = _TlpAtsDeviceOutputCurrentTotal_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 2, 1, 1, 16),
    _TlpAtsDeviceOutputCurrentTotal_Type()
)
tlpAtsDeviceOutputCurrentTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsDeviceOutputCurrentTotal.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsDeviceOutputCurrentTotal.setUnits("0.01 Amps")
_TlpAtsDeviceWattHoursTotal_Type = Unsigned32
_TlpAtsDeviceWattHoursTotal_Object = MibTableColumn
tlpAtsDeviceWattHoursTotal = _TlpAtsDeviceWattHoursTotal_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 2, 1, 1, 17),
    _TlpAtsDeviceWattHoursTotal_Type()
)
tlpAtsDeviceWattHoursTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsDeviceWattHoursTotal.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsDeviceWattHoursTotal.setUnits("WH")
_TlpAtsDevicePeakPowerTotal_Type = Unsigned32
_TlpAtsDevicePeakPowerTotal_Object = MibTableColumn
tlpAtsDevicePeakPowerTotal = _TlpAtsDevicePeakPowerTotal_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 2, 1, 1, 18),
    _TlpAtsDevicePeakPowerTotal_Type()
)
tlpAtsDevicePeakPowerTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsDevicePeakPowerTotal.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsDevicePeakPowerTotal.setUnits("Watts")
_TlpAtsDevice24hrEnergyTotal_Type = Unsigned32
_TlpAtsDevice24hrEnergyTotal_Object = MibTableColumn
tlpAtsDevice24hrEnergyTotal = _TlpAtsDevice24hrEnergyTotal_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 2, 1, 1, 19),
    _TlpAtsDevice24hrEnergyTotal_Type()
)
tlpAtsDevice24hrEnergyTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsDevice24hrEnergyTotal.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsDevice24hrEnergyTotal.setUnits("0.01 KWH")
_TlpAtsDetail_ObjectIdentity = ObjectIdentity
tlpAtsDetail = _TlpAtsDetail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3)
)
_TlpAtsInput_ObjectIdentity = ObjectIdentity
tlpAtsInput = _TlpAtsInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 1)
)
_TlpAtsInputTable_Object = MibTable
tlpAtsInputTable = _TlpAtsInputTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 1, 1)
)
if mibBuilder.loadTexts:
    tlpAtsInputTable.setStatus("current")
_TlpAtsInputEntry_Object = MibTableRow
tlpAtsInputEntry = _TlpAtsInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 1, 1, 1)
)
tlpAtsInputEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpAtsInputEntry.setStatus("current")
_TlpAtsInputNominalVoltage_Type = Unsigned32
_TlpAtsInputNominalVoltage_Object = MibTableColumn
tlpAtsInputNominalVoltage = _TlpAtsInputNominalVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 1, 1, 1, 1),
    _TlpAtsInputNominalVoltage_Type()
)
tlpAtsInputNominalVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsInputNominalVoltage.setStatus("current")
_TlpAtsInputNominalVoltagePhaseToPhase_Type = Unsigned32
_TlpAtsInputNominalVoltagePhaseToPhase_Object = MibTableColumn
tlpAtsInputNominalVoltagePhaseToPhase = _TlpAtsInputNominalVoltagePhaseToPhase_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 1, 1, 1, 2),
    _TlpAtsInputNominalVoltagePhaseToPhase_Type()
)
tlpAtsInputNominalVoltagePhaseToPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsInputNominalVoltagePhaseToPhase.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsInputNominalVoltagePhaseToPhase.setUnits("0.1 Volts")
_TlpAtsInputNominalVoltagePhaseToNeutral_Type = Unsigned32
_TlpAtsInputNominalVoltagePhaseToNeutral_Object = MibTableColumn
tlpAtsInputNominalVoltagePhaseToNeutral = _TlpAtsInputNominalVoltagePhaseToNeutral_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 1, 1, 1, 3),
    _TlpAtsInputNominalVoltagePhaseToNeutral_Type()
)
tlpAtsInputNominalVoltagePhaseToNeutral.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsInputNominalVoltagePhaseToNeutral.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsInputNominalVoltagePhaseToNeutral.setUnits("0.1 Volts")
_TlpAtsInputLowTransferVoltage_Type = Unsigned32
_TlpAtsInputLowTransferVoltage_Object = MibTableColumn
tlpAtsInputLowTransferVoltage = _TlpAtsInputLowTransferVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 1, 1, 1, 4),
    _TlpAtsInputLowTransferVoltage_Type()
)
tlpAtsInputLowTransferVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsInputLowTransferVoltage.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsInputLowTransferVoltage.setUnits("0.1 Volts")
_TlpAtsInputLowTransferVoltageLowerBound_Type = Unsigned32
_TlpAtsInputLowTransferVoltageLowerBound_Object = MibTableColumn
tlpAtsInputLowTransferVoltageLowerBound = _TlpAtsInputLowTransferVoltageLowerBound_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 1, 1, 1, 5),
    _TlpAtsInputLowTransferVoltageLowerBound_Type()
)
tlpAtsInputLowTransferVoltageLowerBound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsInputLowTransferVoltageLowerBound.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsInputLowTransferVoltageLowerBound.setUnits("Volts")
_TlpAtsInputLowTransferVoltageUpperBound_Type = Unsigned32
_TlpAtsInputLowTransferVoltageUpperBound_Object = MibTableColumn
tlpAtsInputLowTransferVoltageUpperBound = _TlpAtsInputLowTransferVoltageUpperBound_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 1, 1, 1, 6),
    _TlpAtsInputLowTransferVoltageUpperBound_Type()
)
tlpAtsInputLowTransferVoltageUpperBound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsInputLowTransferVoltageUpperBound.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsInputLowTransferVoltageUpperBound.setUnits("Volts")
_TlpAtsInputHighTransferVoltage_Type = Unsigned32
_TlpAtsInputHighTransferVoltage_Object = MibTableColumn
tlpAtsInputHighTransferVoltage = _TlpAtsInputHighTransferVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 1, 1, 1, 7),
    _TlpAtsInputHighTransferVoltage_Type()
)
tlpAtsInputHighTransferVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsInputHighTransferVoltage.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsInputHighTransferVoltage.setUnits("0.1 Volts")
_TlpAtsInputHighTransferVoltageLowerBound_Type = Unsigned32
_TlpAtsInputHighTransferVoltageLowerBound_Object = MibTableColumn
tlpAtsInputHighTransferVoltageLowerBound = _TlpAtsInputHighTransferVoltageLowerBound_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 1, 1, 1, 8),
    _TlpAtsInputHighTransferVoltageLowerBound_Type()
)
tlpAtsInputHighTransferVoltageLowerBound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsInputHighTransferVoltageLowerBound.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsInputHighTransferVoltageLowerBound.setUnits("Volts")
_TlpAtsInputHighTransferVoltageUpperBound_Type = Unsigned32
_TlpAtsInputHighTransferVoltageUpperBound_Object = MibTableColumn
tlpAtsInputHighTransferVoltageUpperBound = _TlpAtsInputHighTransferVoltageUpperBound_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 1, 1, 1, 9),
    _TlpAtsInputHighTransferVoltageUpperBound_Type()
)
tlpAtsInputHighTransferVoltageUpperBound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsInputHighTransferVoltageUpperBound.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsInputHighTransferVoltageUpperBound.setUnits("Volts")
_TlpAtsInputFairVoltageThreshold_Type = Unsigned32
_TlpAtsInputFairVoltageThreshold_Object = MibTableColumn
tlpAtsInputFairVoltageThreshold = _TlpAtsInputFairVoltageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 1, 1, 1, 10),
    _TlpAtsInputFairVoltageThreshold_Type()
)
tlpAtsInputFairVoltageThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsInputFairVoltageThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsInputFairVoltageThreshold.setUnits("Volts")
_TlpAtsInputBadVoltageThreshold_Type = Unsigned32
_TlpAtsInputBadVoltageThreshold_Object = MibTableColumn
tlpAtsInputBadVoltageThreshold = _TlpAtsInputBadVoltageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 1, 1, 1, 11),
    _TlpAtsInputBadVoltageThreshold_Type()
)
tlpAtsInputBadVoltageThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsInputBadVoltageThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsInputBadVoltageThreshold.setUnits("Volts")


class _TlpAtsInputSourceAvailability_Type(Integer32):
    """Custom type tlpAtsInputSourceAvailability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("inputSourceA", 1),
          ("inputSourceB", 2),
          ("inputSourceAB", 3))
    )


_TlpAtsInputSourceAvailability_Type.__name__ = "Integer32"
_TlpAtsInputSourceAvailability_Object = MibTableColumn
tlpAtsInputSourceAvailability = _TlpAtsInputSourceAvailability_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 1, 1, 1, 12),
    _TlpAtsInputSourceAvailability_Type()
)
tlpAtsInputSourceAvailability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsInputSourceAvailability.setStatus("current")


class _TlpAtsInputSourceInUse_Type(Integer32):
    """Custom type tlpAtsInputSourceInUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inputSourceA", 0),
          ("inputSourceB", 1))
    )


_TlpAtsInputSourceInUse_Type.__name__ = "Integer32"
_TlpAtsInputSourceInUse_Object = MibTableColumn
tlpAtsInputSourceInUse = _TlpAtsInputSourceInUse_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 1, 1, 1, 13),
    _TlpAtsInputSourceInUse_Type()
)
tlpAtsInputSourceInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsInputSourceInUse.setStatus("current")
_TlpAtsInputSourceTransitionCount_Type = Unsigned32
_TlpAtsInputSourceTransitionCount_Object = MibTableColumn
tlpAtsInputSourceTransitionCount = _TlpAtsInputSourceTransitionCount_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 1, 1, 1, 14),
    _TlpAtsInputSourceTransitionCount_Type()
)
tlpAtsInputSourceTransitionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsInputSourceTransitionCount.setStatus("current")
_TlpAtsInputCurrentLimit_Type = Unsigned32
_TlpAtsInputCurrentLimit_Object = MibTableColumn
tlpAtsInputCurrentLimit = _TlpAtsInputCurrentLimit_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 1, 1, 1, 15),
    _TlpAtsInputCurrentLimit_Type()
)
tlpAtsInputCurrentLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsInputCurrentLimit.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsInputCurrentLimit.setUnits("Amps")
_TlpAtsInputCurrentTotal_Type = Unsigned32
_TlpAtsInputCurrentTotal_Object = MibTableColumn
tlpAtsInputCurrentTotal = _TlpAtsInputCurrentTotal_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 1, 1, 1, 16),
    _TlpAtsInputCurrentTotal_Type()
)
tlpAtsInputCurrentTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsInputCurrentTotal.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsInputCurrentTotal.setUnits("0.01 Amps")
_TlpAtsInputPhaseTable_Object = MibTable
tlpAtsInputPhaseTable = _TlpAtsInputPhaseTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 1, 2)
)
if mibBuilder.loadTexts:
    tlpAtsInputPhaseTable.setStatus("current")
_TlpAtsInputPhaseEntry_Object = MibTableRow
tlpAtsInputPhaseEntry = _TlpAtsInputPhaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 1, 2, 1)
)
tlpAtsInputPhaseEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpAtsInputLineIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpAtsInputPhaseIndex"),
)
if mibBuilder.loadTexts:
    tlpAtsInputPhaseEntry.setStatus("current")
_TlpAtsInputLineIndex_Type = Unsigned32
_TlpAtsInputLineIndex_Object = MibTableColumn
tlpAtsInputLineIndex = _TlpAtsInputLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 1, 2, 1, 1),
    _TlpAtsInputLineIndex_Type()
)
tlpAtsInputLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsInputLineIndex.setStatus("current")
_TlpAtsInputPhaseIndex_Type = Unsigned32
_TlpAtsInputPhaseIndex_Object = MibTableColumn
tlpAtsInputPhaseIndex = _TlpAtsInputPhaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 1, 2, 1, 2),
    _TlpAtsInputPhaseIndex_Type()
)
tlpAtsInputPhaseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsInputPhaseIndex.setStatus("current")


class _TlpAtsInputPhaseType_Type(Integer32):
    """Custom type tlpAtsInputPhaseType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("phaseToNeutral", 0),
          ("phaseToPhase", 1))
    )


_TlpAtsInputPhaseType_Type.__name__ = "Integer32"
_TlpAtsInputPhaseType_Object = MibTableColumn
tlpAtsInputPhaseType = _TlpAtsInputPhaseType_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 1, 2, 1, 3),
    _TlpAtsInputPhaseType_Type()
)
tlpAtsInputPhaseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsInputPhaseType.setStatus("current")
_TlpAtsInputPhaseFrequency_Type = Unsigned32
_TlpAtsInputPhaseFrequency_Object = MibTableColumn
tlpAtsInputPhaseFrequency = _TlpAtsInputPhaseFrequency_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 1, 2, 1, 4),
    _TlpAtsInputPhaseFrequency_Type()
)
tlpAtsInputPhaseFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsInputPhaseFrequency.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsInputPhaseFrequency.setUnits("0.1 Hertz")
_TlpAtsInputPhaseVoltage_Type = Unsigned32
_TlpAtsInputPhaseVoltage_Object = MibTableColumn
tlpAtsInputPhaseVoltage = _TlpAtsInputPhaseVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 1, 2, 1, 5),
    _TlpAtsInputPhaseVoltage_Type()
)
tlpAtsInputPhaseVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsInputPhaseVoltage.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsInputPhaseVoltage.setUnits("0.1 Volts")
_TlpAtsInputPhaseVoltageMin_Type = Unsigned32
_TlpAtsInputPhaseVoltageMin_Object = MibTableColumn
tlpAtsInputPhaseVoltageMin = _TlpAtsInputPhaseVoltageMin_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 1, 2, 1, 6),
    _TlpAtsInputPhaseVoltageMin_Type()
)
tlpAtsInputPhaseVoltageMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsInputPhaseVoltageMin.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsInputPhaseVoltageMin.setUnits("0.1 Volts")
_TlpAtsInputPhaseVoltageMax_Type = Unsigned32
_TlpAtsInputPhaseVoltageMax_Object = MibTableColumn
tlpAtsInputPhaseVoltageMax = _TlpAtsInputPhaseVoltageMax_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 1, 2, 1, 7),
    _TlpAtsInputPhaseVoltageMax_Type()
)
tlpAtsInputPhaseVoltageMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsInputPhaseVoltageMax.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsInputPhaseVoltageMax.setUnits("0.1 Volts")
_TlpAtsInputPhaseCurrent_Type = Unsigned32
_TlpAtsInputPhaseCurrent_Object = MibTableColumn
tlpAtsInputPhaseCurrent = _TlpAtsInputPhaseCurrent_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 1, 2, 1, 8),
    _TlpAtsInputPhaseCurrent_Type()
)
tlpAtsInputPhaseCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsInputPhaseCurrent.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsInputPhaseCurrent.setUnits("0.01 Amps")
_TlpAtsInputPhasePower_Type = Unsigned32
_TlpAtsInputPhasePower_Object = MibTableColumn
tlpAtsInputPhasePower = _TlpAtsInputPhasePower_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 1, 2, 1, 9),
    _TlpAtsInputPhasePower_Type()
)
tlpAtsInputPhasePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsInputPhasePower.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsInputPhasePower.setUnits("Watts")
_TlpAtsInputPhaseThdVoltage_Type = Unsigned32
_TlpAtsInputPhaseThdVoltage_Object = MibTableColumn
tlpAtsInputPhaseThdVoltage = _TlpAtsInputPhaseThdVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 1, 2, 1, 10),
    _TlpAtsInputPhaseThdVoltage_Type()
)
tlpAtsInputPhaseThdVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsInputPhaseThdVoltage.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsInputPhaseThdVoltage.setUnits("0.01 percent")
_TlpAtsOutput_ObjectIdentity = ObjectIdentity
tlpAtsOutput = _TlpAtsOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 2)
)
_TlpAtsOutputTable_Object = MibTable
tlpAtsOutputTable = _TlpAtsOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 2, 1)
)
if mibBuilder.loadTexts:
    tlpAtsOutputTable.setStatus("current")
_TlpAtsOutputEntry_Object = MibTableRow
tlpAtsOutputEntry = _TlpAtsOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 2, 1, 1)
)
tlpAtsOutputEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpAtsOutputIndex"),
)
if mibBuilder.loadTexts:
    tlpAtsOutputEntry.setStatus("current")
_TlpAtsOutputIndex_Type = Unsigned32
_TlpAtsOutputIndex_Object = MibTableColumn
tlpAtsOutputIndex = _TlpAtsOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 2, 1, 1, 1),
    _TlpAtsOutputIndex_Type()
)
tlpAtsOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsOutputIndex.setStatus("current")


class _TlpAtsOutputPhase_Type(Integer32):
    """Custom type tlpAtsOutputPhase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("phase1", 1),
          ("phase2", 2),
          ("phase3", 3))
    )


_TlpAtsOutputPhase_Type.__name__ = "Integer32"
_TlpAtsOutputPhase_Object = MibTableColumn
tlpAtsOutputPhase = _TlpAtsOutputPhase_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 2, 1, 1, 2),
    _TlpAtsOutputPhase_Type()
)
tlpAtsOutputPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsOutputPhase.setStatus("current")


class _TlpAtsOutputPhaseType_Type(Integer32):
    """Custom type tlpAtsOutputPhaseType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("phaseToNeutral", 0),
          ("phaseToPhase", 1))
    )


_TlpAtsOutputPhaseType_Type.__name__ = "Integer32"
_TlpAtsOutputPhaseType_Object = MibTableColumn
tlpAtsOutputPhaseType = _TlpAtsOutputPhaseType_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 2, 1, 1, 3),
    _TlpAtsOutputPhaseType_Type()
)
tlpAtsOutputPhaseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsOutputPhaseType.setStatus("current")
_TlpAtsOutputVoltage_Type = Unsigned32
_TlpAtsOutputVoltage_Object = MibTableColumn
tlpAtsOutputVoltage = _TlpAtsOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 2, 1, 1, 4),
    _TlpAtsOutputVoltage_Type()
)
tlpAtsOutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsOutputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsOutputVoltage.setUnits("0.1 Volts")
_TlpAtsOutputCurrent_Type = Unsigned32
_TlpAtsOutputCurrent_Object = MibTableColumn
tlpAtsOutputCurrent = _TlpAtsOutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 2, 1, 1, 5),
    _TlpAtsOutputCurrent_Type()
)
tlpAtsOutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsOutputCurrent.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsOutputCurrent.setUnits("0.01 Amps")
_TlpAtsOutputCurrentMin_Type = Unsigned32
_TlpAtsOutputCurrentMin_Object = MibTableColumn
tlpAtsOutputCurrentMin = _TlpAtsOutputCurrentMin_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 2, 1, 1, 6),
    _TlpAtsOutputCurrentMin_Type()
)
tlpAtsOutputCurrentMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsOutputCurrentMin.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsOutputCurrentMin.setUnits("0.01 Amps")
_TlpAtsOutputCurrentMax_Type = Unsigned32
_TlpAtsOutputCurrentMax_Object = MibTableColumn
tlpAtsOutputCurrentMax = _TlpAtsOutputCurrentMax_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 2, 1, 1, 7),
    _TlpAtsOutputCurrentMax_Type()
)
tlpAtsOutputCurrentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsOutputCurrentMax.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsOutputCurrentMax.setUnits("0.01 Amps")
_TlpAtsOutputActivePower_Type = Unsigned32
_TlpAtsOutputActivePower_Object = MibTableColumn
tlpAtsOutputActivePower = _TlpAtsOutputActivePower_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 2, 1, 1, 8),
    _TlpAtsOutputActivePower_Type()
)
tlpAtsOutputActivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsOutputActivePower.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsOutputActivePower.setUnits("Watts")
_TlpAtsOutputPowerFactor_Type = Integer32
_TlpAtsOutputPowerFactor_Object = MibTableColumn
tlpAtsOutputPowerFactor = _TlpAtsOutputPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 2, 1, 1, 9),
    _TlpAtsOutputPowerFactor_Type()
)
tlpAtsOutputPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsOutputPowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsOutputPowerFactor.setUnits("0.01")


class _TlpAtsOutputSource_Type(Integer32):
    """Custom type tlpAtsOutputSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("normal", 1))
    )


_TlpAtsOutputSource_Type.__name__ = "Integer32"
_TlpAtsOutputSource_Object = MibTableColumn
tlpAtsOutputSource = _TlpAtsOutputSource_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 2, 1, 1, 10),
    _TlpAtsOutputSource_Type()
)
tlpAtsOutputSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsOutputSource.setStatus("current")
_TlpAtsOutputFrequency_Type = Unsigned32
_TlpAtsOutputFrequency_Object = MibTableColumn
tlpAtsOutputFrequency = _TlpAtsOutputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 2, 1, 1, 11),
    _TlpAtsOutputFrequency_Type()
)
tlpAtsOutputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsOutputFrequency.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsOutputFrequency.setUnits("0.1 Hertz")
_TlpAtsOutputPowerKVA_Type = Unsigned32
_TlpAtsOutputPowerKVA_Object = MibTableColumn
tlpAtsOutputPowerKVA = _TlpAtsOutputPowerKVA_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 2, 1, 1, 12),
    _TlpAtsOutputPowerKVA_Type()
)
tlpAtsOutputPowerKVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsOutputPowerKVA.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsOutputPowerKVA.setUnits("0.01 KVA")
_TlpAtsOutputPowerKW_Type = Unsigned32
_TlpAtsOutputPowerKW_Object = MibTableColumn
tlpAtsOutputPowerKW = _TlpAtsOutputPowerKW_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 2, 1, 1, 13),
    _TlpAtsOutputPowerKW_Type()
)
tlpAtsOutputPowerKW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsOutputPowerKW.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsOutputPowerKW.setUnits("0.01 KW")
_TlpAtsOutput24hrEnergy_Type = Unsigned32
_TlpAtsOutput24hrEnergy_Object = MibTableColumn
tlpAtsOutput24hrEnergy = _TlpAtsOutput24hrEnergy_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 2, 1, 1, 14),
    _TlpAtsOutput24hrEnergy_Type()
)
tlpAtsOutput24hrEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsOutput24hrEnergy.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsOutput24hrEnergy.setUnits("0.01 KWH")
_TlpAtsOutputApparentPower_Type = Unsigned32
_TlpAtsOutputApparentPower_Object = MibTableColumn
tlpAtsOutputApparentPower = _TlpAtsOutputApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 2, 1, 1, 15),
    _TlpAtsOutputApparentPower_Type()
)
tlpAtsOutputApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsOutputApparentPower.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsOutputApparentPower.setUnits("VA")
_TlpAtsOutputReactivePower_Type = Integer32
_TlpAtsOutputReactivePower_Object = MibTableColumn
tlpAtsOutputReactivePower = _TlpAtsOutputReactivePower_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 2, 1, 1, 16),
    _TlpAtsOutputReactivePower_Type()
)
tlpAtsOutputReactivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsOutputReactivePower.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsOutputReactivePower.setUnits("VAR")
_TlpAtsOutputUtilization_Type = Unsigned32
_TlpAtsOutputUtilization_Object = MibTableColumn
tlpAtsOutputUtilization = _TlpAtsOutputUtilization_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 2, 1, 1, 17),
    _TlpAtsOutputUtilization_Type()
)
tlpAtsOutputUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsOutputUtilization.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsOutputUtilization.setUnits("0.01 percent")
_TlpAtsOutputWattHours_Type = Unsigned32
_TlpAtsOutputWattHours_Object = MibTableColumn
tlpAtsOutputWattHours = _TlpAtsOutputWattHours_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 2, 1, 1, 18),
    _TlpAtsOutputWattHours_Type()
)
tlpAtsOutputWattHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsOutputWattHours.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsOutputWattHours.setUnits("WH")
_TlpAtsOutputPeakPower_Type = Unsigned32
_TlpAtsOutputPeakPower_Object = MibTableColumn
tlpAtsOutputPeakPower = _TlpAtsOutputPeakPower_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 2, 1, 1, 19),
    _TlpAtsOutputPeakPower_Type()
)
tlpAtsOutputPeakPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsOutputPeakPower.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsOutputPeakPower.setUnits("Watts")
_TlpAtsOutlet_ObjectIdentity = ObjectIdentity
tlpAtsOutlet = _TlpAtsOutlet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 3)
)
_TlpAtsOutletTable_Object = MibTable
tlpAtsOutletTable = _TlpAtsOutletTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 3, 1)
)
if mibBuilder.loadTexts:
    tlpAtsOutletTable.setStatus("current")
_TlpAtsOutletEntry_Object = MibTableRow
tlpAtsOutletEntry = _TlpAtsOutletEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 3, 1, 1)
)
tlpAtsOutletEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpAtsOutletIndex"),
)
if mibBuilder.loadTexts:
    tlpAtsOutletEntry.setStatus("current")
_TlpAtsOutletIndex_Type = Unsigned32
_TlpAtsOutletIndex_Object = MibTableColumn
tlpAtsOutletIndex = _TlpAtsOutletIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 3, 1, 1, 1),
    _TlpAtsOutletIndex_Type()
)
tlpAtsOutletIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsOutletIndex.setStatus("current")
_TlpAtsOutletName_Type = DisplayString
_TlpAtsOutletName_Object = MibTableColumn
tlpAtsOutletName = _TlpAtsOutletName_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 3, 1, 1, 2),
    _TlpAtsOutletName_Type()
)
tlpAtsOutletName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsOutletName.setStatus("current")
_TlpAtsOutletDescription_Type = DisplayString
_TlpAtsOutletDescription_Object = MibTableColumn
tlpAtsOutletDescription = _TlpAtsOutletDescription_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 3, 1, 1, 3),
    _TlpAtsOutletDescription_Type()
)
tlpAtsOutletDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsOutletDescription.setStatus("current")


class _TlpAtsOutletState_Type(Integer32):
    """Custom type tlpAtsOutletState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("off", 1),
          ("on", 2))
    )


_TlpAtsOutletState_Type.__name__ = "Integer32"
_TlpAtsOutletState_Object = MibTableColumn
tlpAtsOutletState = _TlpAtsOutletState_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 3, 1, 1, 4),
    _TlpAtsOutletState_Type()
)
tlpAtsOutletState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsOutletState.setStatus("current")
_TlpAtsOutletControllable_Type = TruthValue
_TlpAtsOutletControllable_Object = MibTableColumn
tlpAtsOutletControllable = _TlpAtsOutletControllable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 3, 1, 1, 5),
    _TlpAtsOutletControllable_Type()
)
tlpAtsOutletControllable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsOutletControllable.setStatus("current")


class _TlpAtsOutletCommand_Type(Integer32):
    """Custom type tlpAtsOutletCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("turnOff", 1),
          ("turnOn", 2),
          ("cycle", 3))
    )


_TlpAtsOutletCommand_Type.__name__ = "Integer32"
_TlpAtsOutletCommand_Object = MibTableColumn
tlpAtsOutletCommand = _TlpAtsOutletCommand_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 3, 1, 1, 6),
    _TlpAtsOutletCommand_Type()
)
tlpAtsOutletCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsOutletCommand.setStatus("current")
_TlpAtsOutletVoltage_Type = Unsigned32
_TlpAtsOutletVoltage_Object = MibTableColumn
tlpAtsOutletVoltage = _TlpAtsOutletVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 3, 1, 1, 7),
    _TlpAtsOutletVoltage_Type()
)
tlpAtsOutletVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsOutletVoltage.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsOutletVoltage.setUnits("0.1 Volts")
_TlpAtsOutletCurrent_Type = Unsigned32
_TlpAtsOutletCurrent_Object = MibTableColumn
tlpAtsOutletCurrent = _TlpAtsOutletCurrent_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 3, 1, 1, 8),
    _TlpAtsOutletCurrent_Type()
)
tlpAtsOutletCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsOutletCurrent.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsOutletCurrent.setUnits("0.01 Amps")
_TlpAtsOutletActivePower_Type = Unsigned32
_TlpAtsOutletActivePower_Object = MibTableColumn
tlpAtsOutletActivePower = _TlpAtsOutletActivePower_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 3, 1, 1, 9),
    _TlpAtsOutletActivePower_Type()
)
tlpAtsOutletActivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsOutletActivePower.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsOutletActivePower.setUnits("Watts")


class _TlpAtsOutletRampAction_Type(Integer32):
    """Custom type tlpAtsOutletRampAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("remainOff", 0),
          ("turnOnAfterDelay", 1))
    )


_TlpAtsOutletRampAction_Type.__name__ = "Integer32"
_TlpAtsOutletRampAction_Object = MibTableColumn
tlpAtsOutletRampAction = _TlpAtsOutletRampAction_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 3, 1, 1, 10),
    _TlpAtsOutletRampAction_Type()
)
tlpAtsOutletRampAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsOutletRampAction.setStatus("current")
_TlpAtsOutletRampDelay_Type = Integer32
_TlpAtsOutletRampDelay_Object = MibTableColumn
tlpAtsOutletRampDelay = _TlpAtsOutletRampDelay_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 3, 1, 1, 11),
    _TlpAtsOutletRampDelay_Type()
)
tlpAtsOutletRampDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsOutletRampDelay.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsOutletRampDelay.setUnits("seconds")


class _TlpAtsOutletShedAction_Type(Integer32):
    """Custom type tlpAtsOutletShedAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("remainOn", 0),
          ("turnOffAfterDelay", 1))
    )


_TlpAtsOutletShedAction_Type.__name__ = "Integer32"
_TlpAtsOutletShedAction_Object = MibTableColumn
tlpAtsOutletShedAction = _TlpAtsOutletShedAction_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 3, 1, 1, 12),
    _TlpAtsOutletShedAction_Type()
)
tlpAtsOutletShedAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsOutletShedAction.setStatus("current")
_TlpAtsOutletShedDelay_Type = Integer32
_TlpAtsOutletShedDelay_Object = MibTableColumn
tlpAtsOutletShedDelay = _TlpAtsOutletShedDelay_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 3, 1, 1, 13),
    _TlpAtsOutletShedDelay_Type()
)
tlpAtsOutletShedDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsOutletShedDelay.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsOutletShedDelay.setUnits("seconds")
_TlpAtsOutletGroup_Type = Integer32
_TlpAtsOutletGroup_Object = MibTableColumn
tlpAtsOutletGroup = _TlpAtsOutletGroup_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 3, 1, 1, 14),
    _TlpAtsOutletGroup_Type()
)
tlpAtsOutletGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsOutletGroup.setStatus("current")
_TlpAtsOutletBank_Type = Integer32
_TlpAtsOutletBank_Object = MibTableColumn
tlpAtsOutletBank = _TlpAtsOutletBank_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 3, 1, 1, 15),
    _TlpAtsOutletBank_Type()
)
tlpAtsOutletBank.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsOutletBank.setStatus("deprecated")
_TlpAtsOutletCircuit_Type = Integer32
_TlpAtsOutletCircuit_Object = MibTableColumn
tlpAtsOutletCircuit = _TlpAtsOutletCircuit_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 3, 1, 1, 16),
    _TlpAtsOutletCircuit_Type()
)
tlpAtsOutletCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsOutletCircuit.setStatus("current")


class _TlpAtsOutletPhase_Type(Integer32):
    """Custom type tlpAtsOutletPhase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("phase1", 1),
          ("phase2", 2),
          ("phase3", 3),
          ("phase1-2", 4),
          ("phase2-3", 5),
          ("phase3-1", 6))
    )


_TlpAtsOutletPhase_Type.__name__ = "Integer32"
_TlpAtsOutletPhase_Object = MibTableColumn
tlpAtsOutletPhase = _TlpAtsOutletPhase_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 3, 1, 1, 17),
    _TlpAtsOutletPhase_Type()
)
tlpAtsOutletPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsOutletPhase.setStatus("current")


class _TlpAtsOutletReceptacleType_Type(Integer32):
    """Custom type tlpAtsOutletReceptacleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("nema-515R", 1),
          ("nema-520R", 2),
          ("nema-530R", 3),
          ("nema-L515R", 4),
          ("nema-L520R", 5),
          ("nema-L530R", 6),
          ("nema-L615R", 7),
          ("nema-L620R", 8),
          ("nema-L630R", 9),
          ("nema-L1430R", 10),
          ("nema-L1520R", 11),
          ("nema-L1530R", 12),
          ("nema-L2120R", 13),
          ("nema-L2130R", 14),
          ("nema-L2230R", 15),
          ("iec-309-1620", 16),
          ("iec-309-3032", 17),
          ("iec-309-6063", 18),
          ("iec-320-C13", 19),
          ("iec-320-C14", 20),
          ("iec-320-C15", 21),
          ("iec-320-C17", 22),
          ("iec-320-C19", 23),
          ("iec-320-C20", 24))
    )


_TlpAtsOutletReceptacleType_Type.__name__ = "Integer32"
_TlpAtsOutletReceptacleType_Object = MibTableColumn
tlpAtsOutletReceptacleType = _TlpAtsOutletReceptacleType_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 3, 1, 1, 18),
    _TlpAtsOutletReceptacleType_Type()
)
tlpAtsOutletReceptacleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsOutletReceptacleType.setStatus("current")
_TlpAtsOutletPowerFactor_Type = Integer32
_TlpAtsOutletPowerFactor_Object = MibTableColumn
tlpAtsOutletPowerFactor = _TlpAtsOutletPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 3, 1, 1, 19),
    _TlpAtsOutletPowerFactor_Type()
)
tlpAtsOutletPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsOutletPowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsOutletPowerFactor.setUnits("0.01")
_TlpAtsOutletApparentPower_Type = Unsigned32
_TlpAtsOutletApparentPower_Object = MibTableColumn
tlpAtsOutletApparentPower = _TlpAtsOutletApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 3, 1, 1, 20),
    _TlpAtsOutletApparentPower_Type()
)
tlpAtsOutletApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsOutletApparentPower.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsOutletApparentPower.setUnits("VA")
_TlpAtsOutletReactivePower_Type = Integer32
_TlpAtsOutletReactivePower_Object = MibTableColumn
tlpAtsOutletReactivePower = _TlpAtsOutletReactivePower_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 3, 1, 1, 21),
    _TlpAtsOutletReactivePower_Type()
)
tlpAtsOutletReactivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsOutletReactivePower.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsOutletReactivePower.setUnits("VAR")
_TlpAtsOutletFrequency_Type = Unsigned32
_TlpAtsOutletFrequency_Object = MibTableColumn
tlpAtsOutletFrequency = _TlpAtsOutletFrequency_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 3, 1, 1, 22),
    _TlpAtsOutletFrequency_Type()
)
tlpAtsOutletFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsOutletFrequency.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsOutletFrequency.setUnits("0.1 Hertz")
_TlpAtsOutletUtilization_Type = Unsigned32
_TlpAtsOutletUtilization_Object = MibTableColumn
tlpAtsOutletUtilization = _TlpAtsOutletUtilization_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 3, 1, 1, 23),
    _TlpAtsOutletUtilization_Type()
)
tlpAtsOutletUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsOutletUtilization.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsOutletUtilization.setUnits("0.01 percent")
_TlpAtsOutlet24hrEnergy_Type = Unsigned32
_TlpAtsOutlet24hrEnergy_Object = MibTableColumn
tlpAtsOutlet24hrEnergy = _TlpAtsOutlet24hrEnergy_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 3, 1, 1, 24),
    _TlpAtsOutlet24hrEnergy_Type()
)
tlpAtsOutlet24hrEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsOutlet24hrEnergy.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsOutlet24hrEnergy.setUnits("0.01 KWH")
_TlpAtsOutletOvercurrent_Type = TruthValue
_TlpAtsOutletOvercurrent_Object = MibTableColumn
tlpAtsOutletOvercurrent = _TlpAtsOutletOvercurrent_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 3, 1, 1, 25),
    _TlpAtsOutletOvercurrent_Type()
)
tlpAtsOutletOvercurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsOutletOvercurrent.setStatus("current")
_TlpAtsOutletGroupTable_Object = MibTable
tlpAtsOutletGroupTable = _TlpAtsOutletGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 3, 2)
)
if mibBuilder.loadTexts:
    tlpAtsOutletGroupTable.setStatus("current")
_TlpAtsOutletGroupEntry_Object = MibTableRow
tlpAtsOutletGroupEntry = _TlpAtsOutletGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 3, 2, 1)
)
tlpAtsOutletGroupEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpAtsOutletGroupIndex"),
)
if mibBuilder.loadTexts:
    tlpAtsOutletGroupEntry.setStatus("current")
_TlpAtsOutletGroupIndex_Type = Unsigned32
_TlpAtsOutletGroupIndex_Object = MibTableColumn
tlpAtsOutletGroupIndex = _TlpAtsOutletGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 3, 2, 1, 1),
    _TlpAtsOutletGroupIndex_Type()
)
tlpAtsOutletGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsOutletGroupIndex.setStatus("current")
_TlpAtsOutletGroupRowStatus_Type = RowStatus
_TlpAtsOutletGroupRowStatus_Object = MibTableColumn
tlpAtsOutletGroupRowStatus = _TlpAtsOutletGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 3, 2, 1, 2),
    _TlpAtsOutletGroupRowStatus_Type()
)
tlpAtsOutletGroupRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsOutletGroupRowStatus.setStatus("current")
_TlpAtsOutletGroupName_Type = DisplayString
_TlpAtsOutletGroupName_Object = MibTableColumn
tlpAtsOutletGroupName = _TlpAtsOutletGroupName_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 3, 2, 1, 3),
    _TlpAtsOutletGroupName_Type()
)
tlpAtsOutletGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsOutletGroupName.setStatus("current")
_TlpAtsOutletGroupDescription_Type = DisplayString
_TlpAtsOutletGroupDescription_Object = MibTableColumn
tlpAtsOutletGroupDescription = _TlpAtsOutletGroupDescription_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 3, 2, 1, 4),
    _TlpAtsOutletGroupDescription_Type()
)
tlpAtsOutletGroupDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsOutletGroupDescription.setStatus("current")


class _TlpAtsOutletGroupState_Type(Integer32):
    """Custom type tlpAtsOutletGroupState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("off", 1),
          ("on", 2),
          ("mixed", 3))
    )


_TlpAtsOutletGroupState_Type.__name__ = "Integer32"
_TlpAtsOutletGroupState_Object = MibTableColumn
tlpAtsOutletGroupState = _TlpAtsOutletGroupState_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 3, 2, 1, 5),
    _TlpAtsOutletGroupState_Type()
)
tlpAtsOutletGroupState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsOutletGroupState.setStatus("current")


class _TlpAtsOutletGroupCommand_Type(Integer32):
    """Custom type tlpAtsOutletGroupCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("turnOff", 1),
          ("turnOn", 2),
          ("cycle", 3))
    )


_TlpAtsOutletGroupCommand_Type.__name__ = "Integer32"
_TlpAtsOutletGroupCommand_Object = MibTableColumn
tlpAtsOutletGroupCommand = _TlpAtsOutletGroupCommand_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 3, 2, 1, 6),
    _TlpAtsOutletGroupCommand_Type()
)
tlpAtsOutletGroupCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsOutletGroupCommand.setStatus("current")
_TlpAtsCircuit_ObjectIdentity = ObjectIdentity
tlpAtsCircuit = _TlpAtsCircuit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 4)
)
_TlpAtsCircuitTable_Object = MibTable
tlpAtsCircuitTable = _TlpAtsCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 4, 1)
)
if mibBuilder.loadTexts:
    tlpAtsCircuitTable.setStatus("current")
_TlpAtsCircuitEntry_Object = MibTableRow
tlpAtsCircuitEntry = _TlpAtsCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 4, 1, 1)
)
tlpAtsCircuitEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpAtsCircuitIndex"),
)
if mibBuilder.loadTexts:
    tlpAtsCircuitEntry.setStatus("current")
_TlpAtsCircuitIndex_Type = Unsigned32
_TlpAtsCircuitIndex_Object = MibTableColumn
tlpAtsCircuitIndex = _TlpAtsCircuitIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 4, 1, 1, 1),
    _TlpAtsCircuitIndex_Type()
)
tlpAtsCircuitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsCircuitIndex.setStatus("current")


class _TlpAtsCircuitPhase_Type(Integer32):
    """Custom type tlpAtsCircuitPhase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("phase1", 1),
          ("phase2", 2),
          ("phase3", 3),
          ("phase1-2", 4),
          ("phase2-3", 5),
          ("phase3-1", 6))
    )


_TlpAtsCircuitPhase_Type.__name__ = "Integer32"
_TlpAtsCircuitPhase_Object = MibTableColumn
tlpAtsCircuitPhase = _TlpAtsCircuitPhase_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 4, 1, 1, 2),
    _TlpAtsCircuitPhase_Type()
)
tlpAtsCircuitPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsCircuitPhase.setStatus("current")
_TlpAtsCircuitInputVoltage_Type = Integer32
_TlpAtsCircuitInputVoltage_Object = MibTableColumn
tlpAtsCircuitInputVoltage = _TlpAtsCircuitInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 4, 1, 1, 3),
    _TlpAtsCircuitInputVoltage_Type()
)
tlpAtsCircuitInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsCircuitInputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsCircuitInputVoltage.setUnits("0.1 Volts")
_TlpAtsCircuitTotalCurrent_Type = Integer32
_TlpAtsCircuitTotalCurrent_Object = MibTableColumn
tlpAtsCircuitTotalCurrent = _TlpAtsCircuitTotalCurrent_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 4, 1, 1, 4),
    _TlpAtsCircuitTotalCurrent_Type()
)
tlpAtsCircuitTotalCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsCircuitTotalCurrent.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsCircuitTotalCurrent.setUnits("0.01 Amps")
_TlpAtsCircuitCurrentLimit_Type = Integer32
_TlpAtsCircuitCurrentLimit_Object = MibTableColumn
tlpAtsCircuitCurrentLimit = _TlpAtsCircuitCurrentLimit_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 4, 1, 1, 5),
    _TlpAtsCircuitCurrentLimit_Type()
)
tlpAtsCircuitCurrentLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsCircuitCurrentLimit.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsCircuitCurrentLimit.setUnits("0.01 Amps")
_TlpAtsCircuitCurrentMin_Type = Integer32
_TlpAtsCircuitCurrentMin_Object = MibTableColumn
tlpAtsCircuitCurrentMin = _TlpAtsCircuitCurrentMin_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 4, 1, 1, 6),
    _TlpAtsCircuitCurrentMin_Type()
)
tlpAtsCircuitCurrentMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsCircuitCurrentMin.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsCircuitCurrentMin.setUnits("0.01 Amps")
_TlpAtsCircuitCurrentMax_Type = Integer32
_TlpAtsCircuitCurrentMax_Object = MibTableColumn
tlpAtsCircuitCurrentMax = _TlpAtsCircuitCurrentMax_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 4, 1, 1, 7),
    _TlpAtsCircuitCurrentMax_Type()
)
tlpAtsCircuitCurrentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsCircuitCurrentMax.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsCircuitCurrentMax.setUnits("0.01 Amps")
_TlpAtsCircuitTotalPower_Type = Integer32
_TlpAtsCircuitTotalPower_Object = MibTableColumn
tlpAtsCircuitTotalPower = _TlpAtsCircuitTotalPower_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 4, 1, 1, 8),
    _TlpAtsCircuitTotalPower_Type()
)
tlpAtsCircuitTotalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsCircuitTotalPower.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsCircuitTotalPower.setUnits("Watts")
_TlpAtsCircuitPowerFactor_Type = Integer32
_TlpAtsCircuitPowerFactor_Object = MibTableColumn
tlpAtsCircuitPowerFactor = _TlpAtsCircuitPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 4, 1, 1, 9),
    _TlpAtsCircuitPowerFactor_Type()
)
tlpAtsCircuitPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsCircuitPowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsCircuitPowerFactor.setUnits("0.01")
_TlpAtsCircuitUtilization_Type = Unsigned32
_TlpAtsCircuitUtilization_Object = MibTableColumn
tlpAtsCircuitUtilization = _TlpAtsCircuitUtilization_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 4, 1, 1, 10),
    _TlpAtsCircuitUtilization_Type()
)
tlpAtsCircuitUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsCircuitUtilization.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsCircuitUtilization.setUnits("0.01 percent")
_TlpAtsCircuitApparentPower_Type = Unsigned32
_TlpAtsCircuitApparentPower_Object = MibTableColumn
tlpAtsCircuitApparentPower = _TlpAtsCircuitApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 4, 1, 1, 11),
    _TlpAtsCircuitApparentPower_Type()
)
tlpAtsCircuitApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsCircuitApparentPower.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsCircuitApparentPower.setUnits("VA")
_TlpAtsCircuitReactivePower_Type = Integer32
_TlpAtsCircuitReactivePower_Object = MibTableColumn
tlpAtsCircuitReactivePower = _TlpAtsCircuitReactivePower_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 4, 1, 1, 12),
    _TlpAtsCircuitReactivePower_Type()
)
tlpAtsCircuitReactivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsCircuitReactivePower.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsCircuitReactivePower.setUnits("VAR")
_TlpAtsCircuitFrequency_Type = Unsigned32
_TlpAtsCircuitFrequency_Object = MibTableColumn
tlpAtsCircuitFrequency = _TlpAtsCircuitFrequency_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 4, 1, 1, 13),
    _TlpAtsCircuitFrequency_Type()
)
tlpAtsCircuitFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsCircuitFrequency.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsCircuitFrequency.setUnits("0.1 Hertz")
_TlpAtsCircuitWattHours_Type = Unsigned32
_TlpAtsCircuitWattHours_Object = MibTableColumn
tlpAtsCircuitWattHours = _TlpAtsCircuitWattHours_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 4, 1, 1, 14),
    _TlpAtsCircuitWattHours_Type()
)
tlpAtsCircuitWattHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsCircuitWattHours.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsCircuitWattHours.setUnits("WH")
_TlpAtsCircuitPeakPower_Type = Unsigned32
_TlpAtsCircuitPeakPower_Object = MibTableColumn
tlpAtsCircuitPeakPower = _TlpAtsCircuitPeakPower_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 4, 1, 1, 15),
    _TlpAtsCircuitPeakPower_Type()
)
tlpAtsCircuitPeakPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsCircuitPeakPower.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsCircuitPeakPower.setUnits("Watts")
_TlpAtsBreaker_ObjectIdentity = ObjectIdentity
tlpAtsBreaker = _TlpAtsBreaker_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 5)
)
_TlpAtsBreakerTable_Object = MibTable
tlpAtsBreakerTable = _TlpAtsBreakerTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 5, 1)
)
if mibBuilder.loadTexts:
    tlpAtsBreakerTable.setStatus("current")
_TlpAtsBreakerEntry_Object = MibTableRow
tlpAtsBreakerEntry = _TlpAtsBreakerEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 5, 1, 1)
)
tlpAtsBreakerEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpAtsBreakerIndex"),
)
if mibBuilder.loadTexts:
    tlpAtsBreakerEntry.setStatus("current")
_TlpAtsBreakerIndex_Type = Unsigned32
_TlpAtsBreakerIndex_Object = MibTableColumn
tlpAtsBreakerIndex = _TlpAtsBreakerIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 5, 1, 1, 1),
    _TlpAtsBreakerIndex_Type()
)
tlpAtsBreakerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsBreakerIndex.setStatus("current")


class _TlpAtsBreakerStatus_Type(Integer32):
    """Custom type tlpAtsBreakerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 0),
          ("closed", 1),
          ("notInstalled", 2))
    )


_TlpAtsBreakerStatus_Type.__name__ = "Integer32"
_TlpAtsBreakerStatus_Object = MibTableColumn
tlpAtsBreakerStatus = _TlpAtsBreakerStatus_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 5, 1, 1, 2),
    _TlpAtsBreakerStatus_Type()
)
tlpAtsBreakerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsBreakerStatus.setStatus("current")
_TlpAtsHeatsink_ObjectIdentity = ObjectIdentity
tlpAtsHeatsink = _TlpAtsHeatsink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 6)
)
_TlpAtsHeatsinkTable_Object = MibTable
tlpAtsHeatsinkTable = _TlpAtsHeatsinkTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 6, 1)
)
if mibBuilder.loadTexts:
    tlpAtsHeatsinkTable.setStatus("current")
_TlpAtsHeatsinkEntry_Object = MibTableRow
tlpAtsHeatsinkEntry = _TlpAtsHeatsinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 6, 1, 1)
)
tlpAtsHeatsinkEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpAtsHeatsinkIndex"),
)
if mibBuilder.loadTexts:
    tlpAtsHeatsinkEntry.setStatus("current")
_TlpAtsHeatsinkIndex_Type = Unsigned32
_TlpAtsHeatsinkIndex_Object = MibTableColumn
tlpAtsHeatsinkIndex = _TlpAtsHeatsinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 6, 1, 1, 1),
    _TlpAtsHeatsinkIndex_Type()
)
tlpAtsHeatsinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsHeatsinkIndex.setStatus("current")


class _TlpAtsHeatsinkStatus_Type(Integer32):
    """Custom type tlpAtsHeatsinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("available", 1))
    )


_TlpAtsHeatsinkStatus_Type.__name__ = "Integer32"
_TlpAtsHeatsinkStatus_Object = MibTableColumn
tlpAtsHeatsinkStatus = _TlpAtsHeatsinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 6, 1, 1, 2),
    _TlpAtsHeatsinkStatus_Type()
)
tlpAtsHeatsinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsHeatsinkStatus.setStatus("current")
_TlpAtsHeatsinkTemperatureC_Type = Integer32
_TlpAtsHeatsinkTemperatureC_Object = MibTableColumn
tlpAtsHeatsinkTemperatureC = _TlpAtsHeatsinkTemperatureC_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 6, 1, 1, 3),
    _TlpAtsHeatsinkTemperatureC_Type()
)
tlpAtsHeatsinkTemperatureC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsHeatsinkTemperatureC.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsHeatsinkTemperatureC.setUnits("0.1 degrees Celsius")
_TlpAtsHeatsinkTemperatureF_Type = Integer32
_TlpAtsHeatsinkTemperatureF_Object = MibTableColumn
tlpAtsHeatsinkTemperatureF = _TlpAtsHeatsinkTemperatureF_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 6, 1, 1, 4),
    _TlpAtsHeatsinkTemperatureF_Type()
)
tlpAtsHeatsinkTemperatureF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsHeatsinkTemperatureF.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsHeatsinkTemperatureF.setUnits("0.1 degrees Fahrenheit")
_TlpAtsControl_ObjectIdentity = ObjectIdentity
tlpAtsControl = _TlpAtsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 4)
)
_TlpAtsControlTable_Object = MibTable
tlpAtsControlTable = _TlpAtsControlTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 4, 1)
)
if mibBuilder.loadTexts:
    tlpAtsControlTable.setStatus("current")
_TlpAtsControlEntry_Object = MibTableRow
tlpAtsControlEntry = _TlpAtsControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 4, 1, 1)
)
tlpAtsControlEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpAtsControlEntry.setStatus("current")
_TlpAtsControlRamp_Type = TruthValue
_TlpAtsControlRamp_Object = MibTableColumn
tlpAtsControlRamp = _TlpAtsControlRamp_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 4, 1, 1, 1),
    _TlpAtsControlRamp_Type()
)
tlpAtsControlRamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsControlRamp.setStatus("current")
_TlpAtsControlShed_Type = TruthValue
_TlpAtsControlShed_Object = MibTableColumn
tlpAtsControlShed = _TlpAtsControlShed_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 4, 1, 1, 2),
    _TlpAtsControlShed_Type()
)
tlpAtsControlShed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsControlShed.setStatus("current")
_TlpAtsControlOn_Type = TruthValue
_TlpAtsControlOn_Object = MibTableColumn
tlpAtsControlOn = _TlpAtsControlOn_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 4, 1, 1, 3),
    _TlpAtsControlOn_Type()
)
tlpAtsControlOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsControlOn.setStatus("current")
_TlpAtsControlOff_Type = TruthValue
_TlpAtsControlOff_Object = MibTableColumn
tlpAtsControlOff = _TlpAtsControlOff_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 4, 1, 1, 4),
    _TlpAtsControlOff_Type()
)
tlpAtsControlOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsControlOff.setStatus("current")
_TlpAtsControlRestart_Type = TruthValue
_TlpAtsControlRestart_Object = MibTableColumn
tlpAtsControlRestart = _TlpAtsControlRestart_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 4, 1, 1, 5),
    _TlpAtsControlRestart_Type()
)
tlpAtsControlRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsControlRestart.setStatus("current")
_TlpAtsControlResetGeneralFault_Type = TruthValue
_TlpAtsControlResetGeneralFault_Object = MibTableColumn
tlpAtsControlResetGeneralFault = _TlpAtsControlResetGeneralFault_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 4, 1, 1, 6),
    _TlpAtsControlResetGeneralFault_Type()
)
tlpAtsControlResetGeneralFault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsControlResetGeneralFault.setStatus("current")
_TlpAtsControlResetWattHours_Type = TruthValue
_TlpAtsControlResetWattHours_Object = MibTableColumn
tlpAtsControlResetWattHours = _TlpAtsControlResetWattHours_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 4, 1, 1, 7),
    _TlpAtsControlResetWattHours_Type()
)
tlpAtsControlResetWattHours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsControlResetWattHours.setStatus("current")
_TlpAtsControlResetPeakPower_Type = TruthValue
_TlpAtsControlResetPeakPower_Object = MibTableColumn
tlpAtsControlResetPeakPower = _TlpAtsControlResetPeakPower_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 4, 1, 1, 8),
    _TlpAtsControlResetPeakPower_Type()
)
tlpAtsControlResetPeakPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsControlResetPeakPower.setStatus("current")
_TlpAtsControlClearEventLog_Type = TruthValue
_TlpAtsControlClearEventLog_Object = MibTableColumn
tlpAtsControlClearEventLog = _TlpAtsControlClearEventLog_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 4, 1, 1, 9),
    _TlpAtsControlClearEventLog_Type()
)
tlpAtsControlClearEventLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsControlClearEventLog.setStatus("current")
_TlpAtsControlOutputPhaseTable_Object = MibTable
tlpAtsControlOutputPhaseTable = _TlpAtsControlOutputPhaseTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 4, 2)
)
if mibBuilder.loadTexts:
    tlpAtsControlOutputPhaseTable.setStatus("current")
_TlpAtsControlOutputPhaseEntry_Object = MibTableRow
tlpAtsControlOutputPhaseEntry = _TlpAtsControlOutputPhaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 4, 2, 1)
)
tlpAtsControlOutputPhaseEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpAtsOutputIndex"),
)
if mibBuilder.loadTexts:
    tlpAtsControlOutputPhaseEntry.setStatus("current")
_TlpAtsControlResetOutputCurrentMinMax_Type = TruthValue
_TlpAtsControlResetOutputCurrentMinMax_Object = MibTableColumn
tlpAtsControlResetOutputCurrentMinMax = _TlpAtsControlResetOutputCurrentMinMax_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 4, 2, 1, 1),
    _TlpAtsControlResetOutputCurrentMinMax_Type()
)
tlpAtsControlResetOutputCurrentMinMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsControlResetOutputCurrentMinMax.setStatus("current")
_TlpAtsControlInputPhaseTable_Object = MibTable
tlpAtsControlInputPhaseTable = _TlpAtsControlInputPhaseTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 4, 3)
)
if mibBuilder.loadTexts:
    tlpAtsControlInputPhaseTable.setStatus("current")
_TlpAtsControlInputPhaseEntry_Object = MibTableRow
tlpAtsControlInputPhaseEntry = _TlpAtsControlInputPhaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 4, 3, 1)
)
tlpAtsControlInputPhaseEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpAtsInputPhaseIndex"),
)
if mibBuilder.loadTexts:
    tlpAtsControlInputPhaseEntry.setStatus("current")
_TlpAtsControlResetInputVoltageMinMax_Type = TruthValue
_TlpAtsControlResetInputVoltageMinMax_Object = MibTableColumn
tlpAtsControlResetInputVoltageMinMax = _TlpAtsControlResetInputVoltageMinMax_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 4, 3, 1, 1),
    _TlpAtsControlResetInputVoltageMinMax_Type()
)
tlpAtsControlResetInputVoltageMinMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsControlResetInputVoltageMinMax.setStatus("current")
_TlpAtsConfig_ObjectIdentity = ObjectIdentity
tlpAtsConfig = _TlpAtsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5)
)
_TlpAtsConfigTable_Object = MibTable
tlpAtsConfigTable = _TlpAtsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 1)
)
if mibBuilder.loadTexts:
    tlpAtsConfigTable.setStatus("current")
_TlpAtsConfigEntry_Object = MibTableRow
tlpAtsConfigEntry = _TlpAtsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 1, 1)
)
tlpAtsConfigEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpAtsConfigEntry.setStatus("current")
_TlpAtsConfigInputVoltage_Type = Unsigned32
_TlpAtsConfigInputVoltage_Object = MibTableColumn
tlpAtsConfigInputVoltage = _TlpAtsConfigInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 1, 1, 1),
    _TlpAtsConfigInputVoltage_Type()
)
tlpAtsConfigInputVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigInputVoltage.setStatus("current")


class _TlpAtsConfigSourceSelect_Type(Integer32):
    """Custom type tlpAtsConfigSourceSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inputSourceA", 1),
          ("inputSourceB", 2))
    )


_TlpAtsConfigSourceSelect_Type.__name__ = "Integer32"
_TlpAtsConfigSourceSelect_Object = MibTableColumn
tlpAtsConfigSourceSelect = _TlpAtsConfigSourceSelect_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 1, 1, 2),
    _TlpAtsConfigSourceSelect_Type()
)
tlpAtsConfigSourceSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigSourceSelect.setStatus("current")
_TlpAtsConfigSource1ReturnTime_Type = Unsigned32
_TlpAtsConfigSource1ReturnTime_Object = MibTableColumn
tlpAtsConfigSource1ReturnTime = _TlpAtsConfigSource1ReturnTime_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 1, 1, 3),
    _TlpAtsConfigSource1ReturnTime_Type()
)
tlpAtsConfigSource1ReturnTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigSource1ReturnTime.setStatus("current")
_TlpAtsConfigSource2ReturnTime_Type = Unsigned32
_TlpAtsConfigSource2ReturnTime_Object = MibTableColumn
tlpAtsConfigSource2ReturnTime = _TlpAtsConfigSource2ReturnTime_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 1, 1, 4),
    _TlpAtsConfigSource2ReturnTime_Type()
)
tlpAtsConfigSource2ReturnTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigSource2ReturnTime.setStatus("current")


class _TlpAtsConfigAutoRampOnTransition_Type(Integer32):
    """Custom type tlpAtsConfigAutoRampOnTransition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TlpAtsConfigAutoRampOnTransition_Type.__name__ = "Integer32"
_TlpAtsConfigAutoRampOnTransition_Object = MibTableColumn
tlpAtsConfigAutoRampOnTransition = _TlpAtsConfigAutoRampOnTransition_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 1, 1, 5),
    _TlpAtsConfigAutoRampOnTransition_Type()
)
tlpAtsConfigAutoRampOnTransition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigAutoRampOnTransition.setStatus("current")


class _TlpAtsConfigAutoShedOnTransition_Type(Integer32):
    """Custom type tlpAtsConfigAutoShedOnTransition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TlpAtsConfigAutoShedOnTransition_Type.__name__ = "Integer32"
_TlpAtsConfigAutoShedOnTransition_Object = MibTableColumn
tlpAtsConfigAutoShedOnTransition = _TlpAtsConfigAutoShedOnTransition_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 1, 1, 6),
    _TlpAtsConfigAutoShedOnTransition_Type()
)
tlpAtsConfigAutoShedOnTransition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigAutoShedOnTransition.setStatus("current")


class _TlpAtsConfigIsoBreakerSetting_Type(Integer32):
    """Custom type tlpAtsConfigIsoBreakerSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 4))
    )


_TlpAtsConfigIsoBreakerSetting_Type.__name__ = "Integer32"
_TlpAtsConfigIsoBreakerSetting_Object = MibTableColumn
tlpAtsConfigIsoBreakerSetting = _TlpAtsConfigIsoBreakerSetting_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 1, 1, 7),
    _TlpAtsConfigIsoBreakerSetting_Type()
)
tlpAtsConfigIsoBreakerSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigIsoBreakerSetting.setStatus("current")


class _TlpAtsConfigRelayCalibrationSetting_Type(Integer32):
    """Custom type tlpAtsConfigRelayCalibrationSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TlpAtsConfigRelayCalibrationSetting_Type.__name__ = "Integer32"
_TlpAtsConfigRelayCalibrationSetting_Object = MibTableColumn
tlpAtsConfigRelayCalibrationSetting = _TlpAtsConfigRelayCalibrationSetting_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 1, 1, 8),
    _TlpAtsConfigRelayCalibrationSetting_Type()
)
tlpAtsConfigRelayCalibrationSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigRelayCalibrationSetting.setStatus("current")


class _TlpAtsConfigThdSetting_Type(Integer32):
    """Custom type tlpAtsConfigThdSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TlpAtsConfigThdSetting_Type.__name__ = "Integer32"
_TlpAtsConfigThdSetting_Object = MibTableColumn
tlpAtsConfigThdSetting = _TlpAtsConfigThdSetting_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 1, 1, 9),
    _TlpAtsConfigThdSetting_Type()
)
tlpAtsConfigThdSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigThdSetting.setStatus("current")


class _TlpAtsConfigWaveformCaptureSetting_Type(Integer32):
    """Custom type tlpAtsConfigWaveformCaptureSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TlpAtsConfigWaveformCaptureSetting_Type.__name__ = "Integer32"
_TlpAtsConfigWaveformCaptureSetting_Object = MibTableColumn
tlpAtsConfigWaveformCaptureSetting = _TlpAtsConfigWaveformCaptureSetting_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 1, 1, 10),
    _TlpAtsConfigWaveformCaptureSetting_Type()
)
tlpAtsConfigWaveformCaptureSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigWaveformCaptureSetting.setStatus("current")


class _TlpAtsConfigRemoteResetSetting_Type(Integer32):
    """Custom type tlpAtsConfigRemoteResetSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TlpAtsConfigRemoteResetSetting_Type.__name__ = "Integer32"
_TlpAtsConfigRemoteResetSetting_Object = MibTableColumn
tlpAtsConfigRemoteResetSetting = _TlpAtsConfigRemoteResetSetting_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 1, 1, 11),
    _TlpAtsConfigRemoteResetSetting_Type()
)
tlpAtsConfigRemoteResetSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigRemoteResetSetting.setStatus("current")
_TlpAtsConfigVoltageRangeOldTable_Object = MibTable
tlpAtsConfigVoltageRangeOldTable = _TlpAtsConfigVoltageRangeOldTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 2)
)
if mibBuilder.loadTexts:
    tlpAtsConfigVoltageRangeOldTable.setStatus("obsolete")
_TlpAtsConfigVoltageRangeOldEntry_Object = MibTableRow
tlpAtsConfigVoltageRangeOldEntry = _TlpAtsConfigVoltageRangeOldEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 2, 1)
)
tlpAtsConfigVoltageRangeOldEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpAtsConfigVoltageRangeOldEntry.setStatus("obsolete")
_TlpAtsConfigHighVoltageTransferOld_Type = Unsigned32
_TlpAtsConfigHighVoltageTransferOld_Object = MibTableColumn
tlpAtsConfigHighVoltageTransferOld = _TlpAtsConfigHighVoltageTransferOld_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 2, 1, 1),
    _TlpAtsConfigHighVoltageTransferOld_Type()
)
tlpAtsConfigHighVoltageTransferOld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigHighVoltageTransferOld.setStatus("obsolete")
if mibBuilder.loadTexts:
    tlpAtsConfigHighVoltageTransferOld.setUnits("0.1 Volts")
_TlpAtsConfigHighVoltageResetOld_Type = Unsigned32
_TlpAtsConfigHighVoltageResetOld_Object = MibTableColumn
tlpAtsConfigHighVoltageResetOld = _TlpAtsConfigHighVoltageResetOld_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 2, 1, 2),
    _TlpAtsConfigHighVoltageResetOld_Type()
)
tlpAtsConfigHighVoltageResetOld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigHighVoltageResetOld.setStatus("obsolete")
if mibBuilder.loadTexts:
    tlpAtsConfigHighVoltageResetOld.setUnits("0.1 Volts")
_TlpAtsConfigSource1TransferResetOld_Type = Unsigned32
_TlpAtsConfigSource1TransferResetOld_Object = MibTableColumn
tlpAtsConfigSource1TransferResetOld = _TlpAtsConfigSource1TransferResetOld_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 2, 1, 3),
    _TlpAtsConfigSource1TransferResetOld_Type()
)
tlpAtsConfigSource1TransferResetOld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigSource1TransferResetOld.setStatus("obsolete")
if mibBuilder.loadTexts:
    tlpAtsConfigSource1TransferResetOld.setUnits("0.1 Volts")
_TlpAtsConfigSource1BrownoutSetOld_Type = Unsigned32
_TlpAtsConfigSource1BrownoutSetOld_Object = MibTableColumn
tlpAtsConfigSource1BrownoutSetOld = _TlpAtsConfigSource1BrownoutSetOld_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 2, 1, 4),
    _TlpAtsConfigSource1BrownoutSetOld_Type()
)
tlpAtsConfigSource1BrownoutSetOld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigSource1BrownoutSetOld.setStatus("obsolete")
if mibBuilder.loadTexts:
    tlpAtsConfigSource1BrownoutSetOld.setUnits("0.1 Volts")
_TlpAtsConfigSource1TransferSetOld_Type = Unsigned32
_TlpAtsConfigSource1TransferSetOld_Object = MibTableColumn
tlpAtsConfigSource1TransferSetOld = _TlpAtsConfigSource1TransferSetOld_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 2, 1, 5),
    _TlpAtsConfigSource1TransferSetOld_Type()
)
tlpAtsConfigSource1TransferSetOld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigSource1TransferSetOld.setStatus("obsolete")
if mibBuilder.loadTexts:
    tlpAtsConfigSource1TransferSetOld.setUnits("0.1 Volts")
_TlpAtsConfigSource2TransferResetOld_Type = Unsigned32
_TlpAtsConfigSource2TransferResetOld_Object = MibTableColumn
tlpAtsConfigSource2TransferResetOld = _TlpAtsConfigSource2TransferResetOld_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 2, 1, 6),
    _TlpAtsConfigSource2TransferResetOld_Type()
)
tlpAtsConfigSource2TransferResetOld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigSource2TransferResetOld.setStatus("obsolete")
if mibBuilder.loadTexts:
    tlpAtsConfigSource2TransferResetOld.setUnits("0.1 Volts")
_TlpAtsConfigSource2BrownoutSetOld_Type = Unsigned32
_TlpAtsConfigSource2BrownoutSetOld_Object = MibTableColumn
tlpAtsConfigSource2BrownoutSetOld = _TlpAtsConfigSource2BrownoutSetOld_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 2, 1, 7),
    _TlpAtsConfigSource2BrownoutSetOld_Type()
)
tlpAtsConfigSource2BrownoutSetOld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigSource2BrownoutSetOld.setStatus("obsolete")
if mibBuilder.loadTexts:
    tlpAtsConfigSource2BrownoutSetOld.setUnits("0.1 Volts")
_TlpAtsConfigSource2TransferSetOld_Type = Unsigned32
_TlpAtsConfigSource2TransferSetOld_Object = MibTableColumn
tlpAtsConfigSource2TransferSetOld = _TlpAtsConfigSource2TransferSetOld_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 2, 1, 8),
    _TlpAtsConfigSource2TransferSetOld_Type()
)
tlpAtsConfigSource2TransferSetOld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigSource2TransferSetOld.setStatus("obsolete")
if mibBuilder.loadTexts:
    tlpAtsConfigSource2TransferSetOld.setUnits("0.1 Volts")
_TlpAtsConfigLowVoltageResetOld_Type = Unsigned32
_TlpAtsConfigLowVoltageResetOld_Object = MibTableColumn
tlpAtsConfigLowVoltageResetOld = _TlpAtsConfigLowVoltageResetOld_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 2, 1, 9),
    _TlpAtsConfigLowVoltageResetOld_Type()
)
tlpAtsConfigLowVoltageResetOld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigLowVoltageResetOld.setStatus("obsolete")
if mibBuilder.loadTexts:
    tlpAtsConfigLowVoltageResetOld.setUnits("0.1 Volts")
_TlpAtsConfigLowVoltageTransferOld_Type = Unsigned32
_TlpAtsConfigLowVoltageTransferOld_Object = MibTableColumn
tlpAtsConfigLowVoltageTransferOld = _TlpAtsConfigLowVoltageTransferOld_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 2, 1, 10),
    _TlpAtsConfigLowVoltageTransferOld_Type()
)
tlpAtsConfigLowVoltageTransferOld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigLowVoltageTransferOld.setStatus("obsolete")
if mibBuilder.loadTexts:
    tlpAtsConfigLowVoltageTransferOld.setUnits("0.1 Volts")
_TlpAtsConfigVoltageRangeLimitsTable_Object = MibTable
tlpAtsConfigVoltageRangeLimitsTable = _TlpAtsConfigVoltageRangeLimitsTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 3)
)
if mibBuilder.loadTexts:
    tlpAtsConfigVoltageRangeLimitsTable.setStatus("current")
_TlpAtsConfigVoltageRangeLimitsEntry_Object = MibTableRow
tlpAtsConfigVoltageRangeLimitsEntry = _TlpAtsConfigVoltageRangeLimitsEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 3, 1)
)
tlpAtsConfigVoltageRangeLimitsEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpAtsConfigVoltageRangeLimitsEntry.setStatus("current")
_TlpAtsConfigSourceBrownoutSetMinimum_Type = Unsigned32
_TlpAtsConfigSourceBrownoutSetMinimum_Object = MibTableColumn
tlpAtsConfigSourceBrownoutSetMinimum = _TlpAtsConfigSourceBrownoutSetMinimum_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 3, 1, 1),
    _TlpAtsConfigSourceBrownoutSetMinimum_Type()
)
tlpAtsConfigSourceBrownoutSetMinimum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigSourceBrownoutSetMinimum.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsConfigSourceBrownoutSetMinimum.setUnits("0.1 Volts")
_TlpAtsConfigSourceBrownoutSetMaximum_Type = Unsigned32
_TlpAtsConfigSourceBrownoutSetMaximum_Object = MibTableColumn
tlpAtsConfigSourceBrownoutSetMaximum = _TlpAtsConfigSourceBrownoutSetMaximum_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 3, 1, 2),
    _TlpAtsConfigSourceBrownoutSetMaximum_Type()
)
tlpAtsConfigSourceBrownoutSetMaximum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigSourceBrownoutSetMaximum.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsConfigSourceBrownoutSetMaximum.setUnits("0.1 Volts")
_TlpAtsConfigSourceTransferSetMinimum_Type = Unsigned32
_TlpAtsConfigSourceTransferSetMinimum_Object = MibTableColumn
tlpAtsConfigSourceTransferSetMinimum = _TlpAtsConfigSourceTransferSetMinimum_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 3, 1, 3),
    _TlpAtsConfigSourceTransferSetMinimum_Type()
)
tlpAtsConfigSourceTransferSetMinimum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigSourceTransferSetMinimum.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsConfigSourceTransferSetMinimum.setUnits("0.1 Volts")
_TlpAtsConfigSourceTransferSetMaximum_Type = Unsigned32
_TlpAtsConfigSourceTransferSetMaximum_Object = MibTableColumn
tlpAtsConfigSourceTransferSetMaximum = _TlpAtsConfigSourceTransferSetMaximum_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 3, 1, 4),
    _TlpAtsConfigSourceTransferSetMaximum_Type()
)
tlpAtsConfigSourceTransferSetMaximum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigSourceTransferSetMaximum.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsConfigSourceTransferSetMaximum.setUnits("0.1 Volts")
_TlpAtsConfigThresholdTable_Object = MibTable
tlpAtsConfigThresholdTable = _TlpAtsConfigThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 4)
)
if mibBuilder.loadTexts:
    tlpAtsConfigThresholdTable.setStatus("current")
_TlpAtsConfigThresholdEntry_Object = MibTableRow
tlpAtsConfigThresholdEntry = _TlpAtsConfigThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 4, 1)
)
tlpAtsConfigThresholdEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpAtsConfigThresholdEntry.setStatus("current")
_TlpAtsConfigOutputCurrentThreshold_Type = Unsigned32
_TlpAtsConfigOutputCurrentThreshold_Object = MibTableColumn
tlpAtsConfigOutputCurrentThreshold = _TlpAtsConfigOutputCurrentThreshold_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 4, 1, 1),
    _TlpAtsConfigOutputCurrentThreshold_Type()
)
tlpAtsConfigOutputCurrentThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigOutputCurrentThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsConfigOutputCurrentThreshold.setUnits("0.1 Amps")
_TlpAtsConfigOverTemperatureThreshold_Type = Unsigned32
_TlpAtsConfigOverTemperatureThreshold_Object = MibTableColumn
tlpAtsConfigOverTemperatureThreshold = _TlpAtsConfigOverTemperatureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 4, 1, 2),
    _TlpAtsConfigOverTemperatureThreshold_Type()
)
tlpAtsConfigOverTemperatureThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigOverTemperatureThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsConfigOverTemperatureThreshold.setUnits("0.1 Celsius")
_TlpAtsConfigOverVoltageThreshold_Type = Unsigned32
_TlpAtsConfigOverVoltageThreshold_Object = MibTableColumn
tlpAtsConfigOverVoltageThreshold = _TlpAtsConfigOverVoltageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 4, 1, 3),
    _TlpAtsConfigOverVoltageThreshold_Type()
)
tlpAtsConfigOverVoltageThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigOverVoltageThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsConfigOverVoltageThreshold.setUnits("0.1 Volts")
_TlpAtsConfigOverLoadThreshold_Type = Unsigned32
_TlpAtsConfigOverLoadThreshold_Object = MibTableColumn
tlpAtsConfigOverLoadThreshold = _TlpAtsConfigOverLoadThreshold_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 4, 1, 4),
    _TlpAtsConfigOverLoadThreshold_Type()
)
tlpAtsConfigOverLoadThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigOverLoadThreshold.setStatus("current")


class _TlpAtsConfigThdOutOfRangeThreshold_Type(Unsigned32):
    """Custom type tlpAtsConfigThdOutOfRangeThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_TlpAtsConfigThdOutOfRangeThreshold_Type.__name__ = "Unsigned32"
_TlpAtsConfigThdOutOfRangeThreshold_Object = MibTableColumn
tlpAtsConfigThdOutOfRangeThreshold = _TlpAtsConfigThdOutOfRangeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 4, 1, 5),
    _TlpAtsConfigThdOutOfRangeThreshold_Type()
)
tlpAtsConfigThdOutOfRangeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigThdOutOfRangeThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsConfigThdOutOfRangeThreshold.setUnits("0.01 percent")
_TlpAtsConfigVoltageRangeTable_Object = MibTable
tlpAtsConfigVoltageRangeTable = _TlpAtsConfigVoltageRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 5)
)
if mibBuilder.loadTexts:
    tlpAtsConfigVoltageRangeTable.setStatus("current")
_TlpAtsConfigVoltageRangeEntry_Object = MibTableRow
tlpAtsConfigVoltageRangeEntry = _TlpAtsConfigVoltageRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 5, 1)
)
tlpAtsConfigVoltageRangeEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpAtsInputLineIndex"),
)
if mibBuilder.loadTexts:
    tlpAtsConfigVoltageRangeEntry.setStatus("current")
_TlpAtsConfigHighVoltageTransfer_Type = Unsigned32
_TlpAtsConfigHighVoltageTransfer_Object = MibTableColumn
tlpAtsConfigHighVoltageTransfer = _TlpAtsConfigHighVoltageTransfer_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 5, 1, 1),
    _TlpAtsConfigHighVoltageTransfer_Type()
)
tlpAtsConfigHighVoltageTransfer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigHighVoltageTransfer.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsConfigHighVoltageTransfer.setUnits("0.1 Volts")
_TlpAtsConfigHighVoltageReset_Type = Unsigned32
_TlpAtsConfigHighVoltageReset_Object = MibTableColumn
tlpAtsConfigHighVoltageReset = _TlpAtsConfigHighVoltageReset_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 5, 1, 2),
    _TlpAtsConfigHighVoltageReset_Type()
)
tlpAtsConfigHighVoltageReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigHighVoltageReset.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsConfigHighVoltageReset.setUnits("0.1 Volts")
_TlpAtsConfigTransferReset_Type = Unsigned32
_TlpAtsConfigTransferReset_Object = MibTableColumn
tlpAtsConfigTransferReset = _TlpAtsConfigTransferReset_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 5, 1, 3),
    _TlpAtsConfigTransferReset_Type()
)
tlpAtsConfigTransferReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigTransferReset.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsConfigTransferReset.setUnits("0.1 Volts")
_TlpAtsConfigBrownoutSet_Type = Unsigned32
_TlpAtsConfigBrownoutSet_Object = MibTableColumn
tlpAtsConfigBrownoutSet = _TlpAtsConfigBrownoutSet_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 5, 1, 4),
    _TlpAtsConfigBrownoutSet_Type()
)
tlpAtsConfigBrownoutSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigBrownoutSet.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsConfigBrownoutSet.setUnits("0.1 Volts")
_TlpAtsConfigTransferSet_Type = Unsigned32
_TlpAtsConfigTransferSet_Object = MibTableColumn
tlpAtsConfigTransferSet = _TlpAtsConfigTransferSet_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 5, 1, 5),
    _TlpAtsConfigTransferSet_Type()
)
tlpAtsConfigTransferSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigTransferSet.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsConfigTransferSet.setUnits("0.1 Volts")
_TlpAtsConfigLowVoltageReset_Type = Unsigned32
_TlpAtsConfigLowVoltageReset_Object = MibTableColumn
tlpAtsConfigLowVoltageReset = _TlpAtsConfigLowVoltageReset_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 5, 1, 6),
    _TlpAtsConfigLowVoltageReset_Type()
)
tlpAtsConfigLowVoltageReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigLowVoltageReset.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsConfigLowVoltageReset.setUnits("0.1 Volts")
_TlpAtsConfigLowVoltageTransfer_Type = Unsigned32
_TlpAtsConfigLowVoltageTransfer_Object = MibTableColumn
tlpAtsConfigLowVoltageTransfer = _TlpAtsConfigLowVoltageTransfer_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 5, 1, 7),
    _TlpAtsConfigLowVoltageTransfer_Type()
)
tlpAtsConfigLowVoltageTransfer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigLowVoltageTransfer.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsConfigLowVoltageTransfer.setUnits("0.1 Volts")
_TlpAtsConfigOutputPhaseThresholdTable_Object = MibTable
tlpAtsConfigOutputPhaseThresholdTable = _TlpAtsConfigOutputPhaseThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 6)
)
if mibBuilder.loadTexts:
    tlpAtsConfigOutputPhaseThresholdTable.setStatus("current")
_TlpAtsConfigOutputPhaseThresholdEntry_Object = MibTableRow
tlpAtsConfigOutputPhaseThresholdEntry = _TlpAtsConfigOutputPhaseThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 6, 1)
)
tlpAtsConfigOutputPhaseThresholdEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpAtsOutputIndex"),
)
if mibBuilder.loadTexts:
    tlpAtsConfigOutputPhaseThresholdEntry.setStatus("current")
_TlpAtsConfigOutputCurrentThresholdTolerance_Type = Unsigned32
_TlpAtsConfigOutputCurrentThresholdTolerance_Object = MibTableColumn
tlpAtsConfigOutputCurrentThresholdTolerance = _TlpAtsConfigOutputCurrentThresholdTolerance_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 6, 1, 1),
    _TlpAtsConfigOutputCurrentThresholdTolerance_Type()
)
tlpAtsConfigOutputCurrentThresholdTolerance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigOutputCurrentThresholdTolerance.setStatus("deprecated")
if mibBuilder.loadTexts:
    tlpAtsConfigOutputCurrentThresholdTolerance.setUnits("0.1 Amps")
_TlpAtsConfigOutputCurrentHighThreshold_Type = Unsigned32
_TlpAtsConfigOutputCurrentHighThreshold_Object = MibTableColumn
tlpAtsConfigOutputCurrentHighThreshold = _TlpAtsConfigOutputCurrentHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 6, 1, 2),
    _TlpAtsConfigOutputCurrentHighThreshold_Type()
)
tlpAtsConfigOutputCurrentHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigOutputCurrentHighThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsConfigOutputCurrentHighThreshold.setUnits("0.1 Amps")
_TlpAtsConfigOutputCurrentLowThreshold_Type = Unsigned32
_TlpAtsConfigOutputCurrentLowThreshold_Object = MibTableColumn
tlpAtsConfigOutputCurrentLowThreshold = _TlpAtsConfigOutputCurrentLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 6, 1, 3),
    _TlpAtsConfigOutputCurrentLowThreshold_Type()
)
tlpAtsConfigOutputCurrentLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigOutputCurrentLowThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsConfigOutputCurrentLowThreshold.setUnits("0.1 Amps")
_TlpAtsConfigOutputVoltageThresholdTolerance_Type = Unsigned32
_TlpAtsConfigOutputVoltageThresholdTolerance_Object = MibTableColumn
tlpAtsConfigOutputVoltageThresholdTolerance = _TlpAtsConfigOutputVoltageThresholdTolerance_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 6, 1, 4),
    _TlpAtsConfigOutputVoltageThresholdTolerance_Type()
)
tlpAtsConfigOutputVoltageThresholdTolerance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigOutputVoltageThresholdTolerance.setStatus("deprecated")
if mibBuilder.loadTexts:
    tlpAtsConfigOutputVoltageThresholdTolerance.setUnits("0.1 Amps")
_TlpAtsConfigOutputVoltageHighCriticalThreshold_Type = Unsigned32
_TlpAtsConfigOutputVoltageHighCriticalThreshold_Object = MibTableColumn
tlpAtsConfigOutputVoltageHighCriticalThreshold = _TlpAtsConfigOutputVoltageHighCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 6, 1, 5),
    _TlpAtsConfigOutputVoltageHighCriticalThreshold_Type()
)
tlpAtsConfigOutputVoltageHighCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigOutputVoltageHighCriticalThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsConfigOutputVoltageHighCriticalThreshold.setUnits("0.1 Volts")
_TlpAtsConfigOutputVoltageHighWarningThreshold_Type = Unsigned32
_TlpAtsConfigOutputVoltageHighWarningThreshold_Object = MibTableColumn
tlpAtsConfigOutputVoltageHighWarningThreshold = _TlpAtsConfigOutputVoltageHighWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 6, 1, 6),
    _TlpAtsConfigOutputVoltageHighWarningThreshold_Type()
)
tlpAtsConfigOutputVoltageHighWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigOutputVoltageHighWarningThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsConfigOutputVoltageHighWarningThreshold.setUnits("0.1 Volts")
_TlpAtsConfigOutputVoltageLowWarningThreshold_Type = Unsigned32
_TlpAtsConfigOutputVoltageLowWarningThreshold_Object = MibTableColumn
tlpAtsConfigOutputVoltageLowWarningThreshold = _TlpAtsConfigOutputVoltageLowWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 6, 1, 7),
    _TlpAtsConfigOutputVoltageLowWarningThreshold_Type()
)
tlpAtsConfigOutputVoltageLowWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigOutputVoltageLowWarningThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsConfigOutputVoltageLowWarningThreshold.setUnits("0.1 Volts")
_TlpAtsConfigOutputVoltageLowCriticalThreshold_Type = Unsigned32
_TlpAtsConfigOutputVoltageLowCriticalThreshold_Object = MibTableColumn
tlpAtsConfigOutputVoltageLowCriticalThreshold = _TlpAtsConfigOutputVoltageLowCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 6, 1, 8),
    _TlpAtsConfigOutputVoltageLowCriticalThreshold_Type()
)
tlpAtsConfigOutputVoltageLowCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigOutputVoltageLowCriticalThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsConfigOutputVoltageLowCriticalThreshold.setUnits("0.1 Volts")
_TlpAtsConfigInputPhaseThresholdTable_Object = MibTable
tlpAtsConfigInputPhaseThresholdTable = _TlpAtsConfigInputPhaseThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 7)
)
if mibBuilder.loadTexts:
    tlpAtsConfigInputPhaseThresholdTable.setStatus("current")
_TlpAtsConfigInputPhaseThresholdEntry_Object = MibTableRow
tlpAtsConfigInputPhaseThresholdEntry = _TlpAtsConfigInputPhaseThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 7, 1)
)
tlpAtsConfigInputPhaseThresholdEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpAtsInputLineIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpAtsInputPhaseIndex"),
)
if mibBuilder.loadTexts:
    tlpAtsConfigInputPhaseThresholdEntry.setStatus("current")
_TlpAtsConfigInputVoltageThresholdTolerance_Type = Unsigned32
_TlpAtsConfigInputVoltageThresholdTolerance_Object = MibTableColumn
tlpAtsConfigInputVoltageThresholdTolerance = _TlpAtsConfigInputVoltageThresholdTolerance_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 7, 1, 1),
    _TlpAtsConfigInputVoltageThresholdTolerance_Type()
)
tlpAtsConfigInputVoltageThresholdTolerance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigInputVoltageThresholdTolerance.setStatus("deprecated")
if mibBuilder.loadTexts:
    tlpAtsConfigInputVoltageThresholdTolerance.setUnits("0.1 Amps")
_TlpAtsConfigInputVoltageHighCriticalThreshold_Type = Unsigned32
_TlpAtsConfigInputVoltageHighCriticalThreshold_Object = MibTableColumn
tlpAtsConfigInputVoltageHighCriticalThreshold = _TlpAtsConfigInputVoltageHighCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 7, 1, 2),
    _TlpAtsConfigInputVoltageHighCriticalThreshold_Type()
)
tlpAtsConfigInputVoltageHighCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigInputVoltageHighCriticalThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsConfigInputVoltageHighCriticalThreshold.setUnits("0.1 Volts")
_TlpAtsConfigInputVoltageHighWarningThreshold_Type = Unsigned32
_TlpAtsConfigInputVoltageHighWarningThreshold_Object = MibTableColumn
tlpAtsConfigInputVoltageHighWarningThreshold = _TlpAtsConfigInputVoltageHighWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 7, 1, 3),
    _TlpAtsConfigInputVoltageHighWarningThreshold_Type()
)
tlpAtsConfigInputVoltageHighWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigInputVoltageHighWarningThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsConfigInputVoltageHighWarningThreshold.setUnits("0.1 Volts")
_TlpAtsConfigInputVoltageLowWarningThreshold_Type = Unsigned32
_TlpAtsConfigInputVoltageLowWarningThreshold_Object = MibTableColumn
tlpAtsConfigInputVoltageLowWarningThreshold = _TlpAtsConfigInputVoltageLowWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 7, 1, 4),
    _TlpAtsConfigInputVoltageLowWarningThreshold_Type()
)
tlpAtsConfigInputVoltageLowWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigInputVoltageLowWarningThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsConfigInputVoltageLowWarningThreshold.setUnits("0.1 Volts")
_TlpAtsConfigInputVoltageLowCriticalThreshold_Type = Unsigned32
_TlpAtsConfigInputVoltageLowCriticalThreshold_Object = MibTableColumn
tlpAtsConfigInputVoltageLowCriticalThreshold = _TlpAtsConfigInputVoltageLowCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 7, 1, 5),
    _TlpAtsConfigInputVoltageLowCriticalThreshold_Type()
)
tlpAtsConfigInputVoltageLowCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigInputVoltageLowCriticalThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsConfigInputVoltageLowCriticalThreshold.setUnits("0.1 Volts")
_TlpCooling_ObjectIdentity = ObjectIdentity
tlpCooling = _TlpCooling_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5)
)
_TlpCoolingIdent_ObjectIdentity = ObjectIdentity
tlpCoolingIdent = _TlpCoolingIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 1)
)
_TlpCoolingIdentNumCooling_Type = Unsigned32
_TlpCoolingIdentNumCooling_Object = MibScalar
tlpCoolingIdentNumCooling = _TlpCoolingIdentNumCooling_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 1, 1),
    _TlpCoolingIdentNumCooling_Type()
)
tlpCoolingIdentNumCooling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpCoolingIdentNumCooling.setStatus("current")
_TlpCoolingDevice_ObjectIdentity = ObjectIdentity
tlpCoolingDevice = _TlpCoolingDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 2)
)
_TlpCoolingDetail_ObjectIdentity = ObjectIdentity
tlpCoolingDetail = _TlpCoolingDetail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 3)
)
_TlpCoolingTemperature_ObjectIdentity = ObjectIdentity
tlpCoolingTemperature = _TlpCoolingTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 3, 1)
)
_TlpCoolingTemperatureFahrenheitTable_Object = MibTable
tlpCoolingTemperatureFahrenheitTable = _TlpCoolingTemperatureFahrenheitTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 3, 1, 1)
)
if mibBuilder.loadTexts:
    tlpCoolingTemperatureFahrenheitTable.setStatus("current")
_TlpCoolingTemperatureFahrenheitEntry_Object = MibTableRow
tlpCoolingTemperatureFahrenheitEntry = _TlpCoolingTemperatureFahrenheitEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 3, 1, 1, 1)
)
tlpCoolingTemperatureFahrenheitEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpCoolingTemperatureFahrenheitEntry.setStatus("current")
_TlpCoolingAmbientDegF_Type = Integer32
_TlpCoolingAmbientDegF_Object = MibTableColumn
tlpCoolingAmbientDegF = _TlpCoolingAmbientDegF_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 3, 1, 1, 1, 1),
    _TlpCoolingAmbientDegF_Type()
)
tlpCoolingAmbientDegF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpCoolingAmbientDegF.setStatus("current")
if mibBuilder.loadTexts:
    tlpCoolingAmbientDegF.setUnits("0.1 degrees Fahrenheit")
_TlpCoolingSupplyAirDegF_Type = Integer32
_TlpCoolingSupplyAirDegF_Object = MibTableColumn
tlpCoolingSupplyAirDegF = _TlpCoolingSupplyAirDegF_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 3, 1, 1, 1, 2),
    _TlpCoolingSupplyAirDegF_Type()
)
tlpCoolingSupplyAirDegF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpCoolingSupplyAirDegF.setStatus("current")
if mibBuilder.loadTexts:
    tlpCoolingSupplyAirDegF.setUnits("0.1 degrees Fahrenheit")
_TlpCoolingReturnAirDegF_Type = Integer32
_TlpCoolingReturnAirDegF_Object = MibTableColumn
tlpCoolingReturnAirDegF = _TlpCoolingReturnAirDegF_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 3, 1, 1, 1, 3),
    _TlpCoolingReturnAirDegF_Type()
)
tlpCoolingReturnAirDegF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpCoolingReturnAirDegF.setStatus("current")
if mibBuilder.loadTexts:
    tlpCoolingReturnAirDegF.setUnits("0.1 degrees Fahrenheit")
_TlpCoolingCondenserInletDegF_Type = Integer32
_TlpCoolingCondenserInletDegF_Object = MibTableColumn
tlpCoolingCondenserInletDegF = _TlpCoolingCondenserInletDegF_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 3, 1, 1, 1, 4),
    _TlpCoolingCondenserInletDegF_Type()
)
tlpCoolingCondenserInletDegF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpCoolingCondenserInletDegF.setStatus("current")
if mibBuilder.loadTexts:
    tlpCoolingCondenserInletDegF.setUnits("0.1 degrees Fahrenheit")
_TlpCoolingEvaporatorDegF_Type = Integer32
_TlpCoolingEvaporatorDegF_Object = MibTableColumn
tlpCoolingEvaporatorDegF = _TlpCoolingEvaporatorDegF_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 3, 1, 1, 1, 5),
    _TlpCoolingEvaporatorDegF_Type()
)
tlpCoolingEvaporatorDegF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpCoolingEvaporatorDegF.setStatus("current")
if mibBuilder.loadTexts:
    tlpCoolingEvaporatorDegF.setUnits("0.1 degrees Fahrenheit")
_TlpCoolingSuctionDegF_Type = Integer32
_TlpCoolingSuctionDegF_Object = MibTableColumn
tlpCoolingSuctionDegF = _TlpCoolingSuctionDegF_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 3, 1, 1, 1, 6),
    _TlpCoolingSuctionDegF_Type()
)
tlpCoolingSuctionDegF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpCoolingSuctionDegF.setStatus("current")
if mibBuilder.loadTexts:
    tlpCoolingSuctionDegF.setUnits("0.1 degrees Fahrenheit")
_TlpCoolingRemoteDegF_Type = Integer32
_TlpCoolingRemoteDegF_Object = MibTableColumn
tlpCoolingRemoteDegF = _TlpCoolingRemoteDegF_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 3, 1, 1, 1, 7),
    _TlpCoolingRemoteDegF_Type()
)
tlpCoolingRemoteDegF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpCoolingRemoteDegF.setStatus("current")
if mibBuilder.loadTexts:
    tlpCoolingRemoteDegF.setUnits("0.1 degrees Fahrenheit")
_TlpCoolingCondenserOutletDegF_Type = Integer32
_TlpCoolingCondenserOutletDegF_Object = MibTableColumn
tlpCoolingCondenserOutletDegF = _TlpCoolingCondenserOutletDegF_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 3, 1, 1, 1, 8),
    _TlpCoolingCondenserOutletDegF_Type()
)
tlpCoolingCondenserOutletDegF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpCoolingCondenserOutletDegF.setStatus("current")
if mibBuilder.loadTexts:
    tlpCoolingCondenserOutletDegF.setUnits("0.1 degrees Fahrenheit")
_TlpCoolingTemperatureCelsiusTable_Object = MibTable
tlpCoolingTemperatureCelsiusTable = _TlpCoolingTemperatureCelsiusTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 3, 1, 2)
)
if mibBuilder.loadTexts:
    tlpCoolingTemperatureCelsiusTable.setStatus("current")
_TlpCoolingTemperatureCelsiusEntry_Object = MibTableRow
tlpCoolingTemperatureCelsiusEntry = _TlpCoolingTemperatureCelsiusEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 3, 1, 2, 1)
)
tlpCoolingTemperatureCelsiusEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpCoolingTemperatureCelsiusEntry.setStatus("current")
_TlpCoolingAmbientDegC_Type = Integer32
_TlpCoolingAmbientDegC_Object = MibTableColumn
tlpCoolingAmbientDegC = _TlpCoolingAmbientDegC_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 3, 1, 2, 1, 1),
    _TlpCoolingAmbientDegC_Type()
)
tlpCoolingAmbientDegC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpCoolingAmbientDegC.setStatus("deprecated")
if mibBuilder.loadTexts:
    tlpCoolingAmbientDegC.setUnits("0.1 degrees Celsius")
_TlpCoolingSupplyAirDegC_Type = Integer32
_TlpCoolingSupplyAirDegC_Object = MibTableColumn
tlpCoolingSupplyAirDegC = _TlpCoolingSupplyAirDegC_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 3, 1, 2, 1, 2),
    _TlpCoolingSupplyAirDegC_Type()
)
tlpCoolingSupplyAirDegC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpCoolingSupplyAirDegC.setStatus("current")
if mibBuilder.loadTexts:
    tlpCoolingSupplyAirDegC.setUnits("0.1 degrees Celsius")
_TlpCoolingReturnAirDegC_Type = Integer32
_TlpCoolingReturnAirDegC_Object = MibTableColumn
tlpCoolingReturnAirDegC = _TlpCoolingReturnAirDegC_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 3, 1, 2, 1, 3),
    _TlpCoolingReturnAirDegC_Type()
)
tlpCoolingReturnAirDegC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpCoolingReturnAirDegC.setStatus("current")
if mibBuilder.loadTexts:
    tlpCoolingReturnAirDegC.setUnits("0.1 degrees Celsius")
_TlpCoolingCondenserInletDegC_Type = Integer32
_TlpCoolingCondenserInletDegC_Object = MibTableColumn
tlpCoolingCondenserInletDegC = _TlpCoolingCondenserInletDegC_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 3, 1, 2, 1, 4),
    _TlpCoolingCondenserInletDegC_Type()
)
tlpCoolingCondenserInletDegC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpCoolingCondenserInletDegC.setStatus("current")
if mibBuilder.loadTexts:
    tlpCoolingCondenserInletDegC.setUnits("0.1 degrees Celsius")
_TlpCoolingEvaporatorDegC_Type = Integer32
_TlpCoolingEvaporatorDegC_Object = MibTableColumn
tlpCoolingEvaporatorDegC = _TlpCoolingEvaporatorDegC_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 3, 1, 2, 1, 5),
    _TlpCoolingEvaporatorDegC_Type()
)
tlpCoolingEvaporatorDegC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpCoolingEvaporatorDegC.setStatus("current")
if mibBuilder.loadTexts:
    tlpCoolingEvaporatorDegC.setUnits("0.1 degrees Celsius")
_TlpCoolingSuctionDegC_Type = Integer32
_TlpCoolingSuctionDegC_Object = MibTableColumn
tlpCoolingSuctionDegC = _TlpCoolingSuctionDegC_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 3, 1, 2, 1, 6),
    _TlpCoolingSuctionDegC_Type()
)
tlpCoolingSuctionDegC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpCoolingSuctionDegC.setStatus("current")
if mibBuilder.loadTexts:
    tlpCoolingSuctionDegC.setUnits("0.1 degrees Celsius")
_TlpCoolingRemoteDegC_Type = Integer32
_TlpCoolingRemoteDegC_Object = MibTableColumn
tlpCoolingRemoteDegC = _TlpCoolingRemoteDegC_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 3, 1, 2, 1, 7),
    _TlpCoolingRemoteDegC_Type()
)
tlpCoolingRemoteDegC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpCoolingRemoteDegC.setStatus("current")
if mibBuilder.loadTexts:
    tlpCoolingRemoteDegC.setUnits("0.1 degrees Celsius")
_TlpCoolingCondenserOutletDegC_Type = Integer32
_TlpCoolingCondenserOutletDegC_Object = MibTableColumn
tlpCoolingCondenserOutletDegC = _TlpCoolingCondenserOutletDegC_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 3, 1, 2, 1, 8),
    _TlpCoolingCondenserOutletDegC_Type()
)
tlpCoolingCondenserOutletDegC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpCoolingCondenserOutletDegC.setStatus("current")
if mibBuilder.loadTexts:
    tlpCoolingCondenserOutletDegC.setUnits("0.1 degrees Celsius")
_TlpCoolingPressure_ObjectIdentity = ObjectIdentity
tlpCoolingPressure = _TlpCoolingPressure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 3, 2)
)
_TlpCoolingPressureMpaTable_Object = MibTable
tlpCoolingPressureMpaTable = _TlpCoolingPressureMpaTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 3, 2, 1)
)
if mibBuilder.loadTexts:
    tlpCoolingPressureMpaTable.setStatus("current")
_TlpCoolingPressureMpaEntry_Object = MibTableRow
tlpCoolingPressureMpaEntry = _TlpCoolingPressureMpaEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 3, 2, 1, 1)
)
tlpCoolingPressureMpaEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpCoolingPressureMpaEntry.setStatus("current")
_TlpCoolingSuctionPressureMpa_Type = Unsigned32
_TlpCoolingSuctionPressureMpa_Object = MibTableColumn
tlpCoolingSuctionPressureMpa = _TlpCoolingSuctionPressureMpa_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 3, 2, 1, 1, 1),
    _TlpCoolingSuctionPressureMpa_Type()
)
tlpCoolingSuctionPressureMpa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpCoolingSuctionPressureMpa.setStatus("current")
if mibBuilder.loadTexts:
    tlpCoolingSuctionPressureMpa.setUnits("0.1 Mpa")
_TlpCoolingDischargePressureMpa_Type = Unsigned32
_TlpCoolingDischargePressureMpa_Object = MibTableColumn
tlpCoolingDischargePressureMpa = _TlpCoolingDischargePressureMpa_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 3, 2, 1, 1, 2),
    _TlpCoolingDischargePressureMpa_Type()
)
tlpCoolingDischargePressureMpa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpCoolingDischargePressureMpa.setStatus("current")
if mibBuilder.loadTexts:
    tlpCoolingDischargePressureMpa.setUnits("0.1 Mpa")
_TlpCoolingPressurePsiTable_Object = MibTable
tlpCoolingPressurePsiTable = _TlpCoolingPressurePsiTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 3, 2, 2)
)
if mibBuilder.loadTexts:
    tlpCoolingPressurePsiTable.setStatus("current")
_TlpCoolingPressurePsiEntry_Object = MibTableRow
tlpCoolingPressurePsiEntry = _TlpCoolingPressurePsiEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 3, 2, 2, 1)
)
tlpCoolingPressurePsiEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpCoolingPressurePsiEntry.setStatus("current")
_TlpCoolingSuctionPressurePsi_Type = Unsigned32
_TlpCoolingSuctionPressurePsi_Object = MibTableColumn
tlpCoolingSuctionPressurePsi = _TlpCoolingSuctionPressurePsi_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 3, 2, 2, 1, 1),
    _TlpCoolingSuctionPressurePsi_Type()
)
tlpCoolingSuctionPressurePsi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpCoolingSuctionPressurePsi.setStatus("current")
if mibBuilder.loadTexts:
    tlpCoolingSuctionPressurePsi.setUnits("0.1 Psi")
_TlpCoolingDischargePressurePsi_Type = Unsigned32
_TlpCoolingDischargePressurePsi_Object = MibTableColumn
tlpCoolingDischargePressurePsi = _TlpCoolingDischargePressurePsi_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 3, 2, 2, 1, 2),
    _TlpCoolingDischargePressurePsi_Type()
)
tlpCoolingDischargePressurePsi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpCoolingDischargePressurePsi.setStatus("current")
if mibBuilder.loadTexts:
    tlpCoolingDischargePressurePsi.setUnits("0.1 Psi")
_TlpCoolingCurrentTable_Object = MibTable
tlpCoolingCurrentTable = _TlpCoolingCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 3, 3)
)
if mibBuilder.loadTexts:
    tlpCoolingCurrentTable.setStatus("current")
_TlpCoolingCurrentEntry_Object = MibTableRow
tlpCoolingCurrentEntry = _TlpCoolingCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 3, 3, 1)
)
tlpCoolingCurrentEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpCoolingCurrentEntry.setStatus("current")
_TlpCoolingUnitCurrent_Type = Unsigned32
_TlpCoolingUnitCurrent_Object = MibTableColumn
tlpCoolingUnitCurrent = _TlpCoolingUnitCurrent_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 3, 3, 1, 1),
    _TlpCoolingUnitCurrent_Type()
)
tlpCoolingUnitCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpCoolingUnitCurrent.setStatus("current")
if mibBuilder.loadTexts:
    tlpCoolingUnitCurrent.setUnits("0.1 Amps")
_TlpCoolingCompressorCurrent_Type = Unsigned32
_TlpCoolingCompressorCurrent_Object = MibTableColumn
tlpCoolingCompressorCurrent = _TlpCoolingCompressorCurrent_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 3, 3, 1, 2),
    _TlpCoolingCompressorCurrent_Type()
)
tlpCoolingCompressorCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpCoolingCompressorCurrent.setStatus("current")
if mibBuilder.loadTexts:
    tlpCoolingCompressorCurrent.setUnits("0.1 Amps")
_TlpCoolingEvaporatorFanCurrent_Type = Unsigned32
_TlpCoolingEvaporatorFanCurrent_Object = MibTableColumn
tlpCoolingEvaporatorFanCurrent = _TlpCoolingEvaporatorFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 3, 3, 1, 3),
    _TlpCoolingEvaporatorFanCurrent_Type()
)
tlpCoolingEvaporatorFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpCoolingEvaporatorFanCurrent.setStatus("current")
if mibBuilder.loadTexts:
    tlpCoolingEvaporatorFanCurrent.setUnits("0.1 Amps")
_TlpCoolingCondenserFanCurrent_Type = Unsigned32
_TlpCoolingCondenserFanCurrent_Object = MibTableColumn
tlpCoolingCondenserFanCurrent = _TlpCoolingCondenserFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 3, 3, 1, 4),
    _TlpCoolingCondenserFanCurrent_Type()
)
tlpCoolingCondenserFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpCoolingCondenserFanCurrent.setStatus("current")
if mibBuilder.loadTexts:
    tlpCoolingCondenserFanCurrent.setUnits("0.1 Amps")
_TlpCoolingDynamicTable_Object = MibTable
tlpCoolingDynamicTable = _TlpCoolingDynamicTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 3, 4)
)
if mibBuilder.loadTexts:
    tlpCoolingDynamicTable.setStatus("current")
_TlpCoolingDynamicEntry_Object = MibTableRow
tlpCoolingDynamicEntry = _TlpCoolingDynamicEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 3, 4, 1)
)
tlpCoolingDynamicEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpCoolingDynamicEntry.setStatus("current")


class _TlpCoolingEvaporatorFanSpeed_Type(Integer32):
    """Custom type tlpCoolingEvaporatorFanSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("low", 1),
          ("mediumLow", 2),
          ("medium", 3),
          ("mediumHigh", 4),
          ("high", 5),
          ("auto", 6))
    )


_TlpCoolingEvaporatorFanSpeed_Type.__name__ = "Integer32"
_TlpCoolingEvaporatorFanSpeed_Object = MibTableColumn
tlpCoolingEvaporatorFanSpeed = _TlpCoolingEvaporatorFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 3, 4, 1, 1),
    _TlpCoolingEvaporatorFanSpeed_Type()
)
tlpCoolingEvaporatorFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpCoolingEvaporatorFanSpeed.setStatus("current")


class _TlpCoolingCondenserFanSpeed_Type(Integer32):
    """Custom type tlpCoolingCondenserFanSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("low", 1),
          ("mediumLow", 2),
          ("medium", 3),
          ("mediumHigh", 4),
          ("high", 5),
          ("auto", 6))
    )


_TlpCoolingCondenserFanSpeed_Type.__name__ = "Integer32"
_TlpCoolingCondenserFanSpeed_Object = MibTableColumn
tlpCoolingCondenserFanSpeed = _TlpCoolingCondenserFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 3, 4, 1, 2),
    _TlpCoolingCondenserFanSpeed_Type()
)
tlpCoolingCondenserFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpCoolingCondenserFanSpeed.setStatus("current")
_TlpCoolingCompressorFrequency_Type = Unsigned32
_TlpCoolingCompressorFrequency_Object = MibTableColumn
tlpCoolingCompressorFrequency = _TlpCoolingCompressorFrequency_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 3, 4, 1, 3),
    _TlpCoolingCompressorFrequency_Type()
)
tlpCoolingCompressorFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpCoolingCompressorFrequency.setStatus("current")
if mibBuilder.loadTexts:
    tlpCoolingCompressorFrequency.setUnits("Hertz")
_TlpCoolingEEVSteps_Type = Integer32
_TlpCoolingEEVSteps_Object = MibTableColumn
tlpCoolingEEVSteps = _TlpCoolingEEVSteps_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 3, 4, 1, 4),
    _TlpCoolingEEVSteps_Type()
)
tlpCoolingEEVSteps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpCoolingEEVSteps.setStatus("current")
_TlpCoolingRuntimeTable_Object = MibTable
tlpCoolingRuntimeTable = _TlpCoolingRuntimeTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 3, 5)
)
if mibBuilder.loadTexts:
    tlpCoolingRuntimeTable.setStatus("current")
_TlpCoolingRuntimeEntry_Object = MibTableRow
tlpCoolingRuntimeEntry = _TlpCoolingRuntimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 3, 5, 1)
)
tlpCoolingRuntimeEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpCoolingRuntimeEntry.setStatus("current")
_TlpCoolingCompressorRunDays_Type = Unsigned32
_TlpCoolingCompressorRunDays_Object = MibTableColumn
tlpCoolingCompressorRunDays = _TlpCoolingCompressorRunDays_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 3, 5, 1, 1),
    _TlpCoolingCompressorRunDays_Type()
)
tlpCoolingCompressorRunDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpCoolingCompressorRunDays.setStatus("current")
if mibBuilder.loadTexts:
    tlpCoolingCompressorRunDays.setUnits("days")
_TlpCoolingCondensatePumpRunDays_Type = Unsigned32
_TlpCoolingCondensatePumpRunDays_Object = MibTableColumn
tlpCoolingCondensatePumpRunDays = _TlpCoolingCondensatePumpRunDays_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 3, 5, 1, 2),
    _TlpCoolingCondensatePumpRunDays_Type()
)
tlpCoolingCondensatePumpRunDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpCoolingCondensatePumpRunDays.setStatus("current")
if mibBuilder.loadTexts:
    tlpCoolingCondensatePumpRunDays.setUnits("days")
_TlpCoolingAirFilterRunHours_Type = Unsigned32
_TlpCoolingAirFilterRunHours_Object = MibTableColumn
tlpCoolingAirFilterRunHours = _TlpCoolingAirFilterRunHours_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 3, 5, 1, 3),
    _TlpCoolingAirFilterRunHours_Type()
)
tlpCoolingAirFilterRunHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpCoolingAirFilterRunHours.setStatus("current")
if mibBuilder.loadTexts:
    tlpCoolingAirFilterRunHours.setUnits("hours")
_TlpCoolingEvaporatorFanRunDays_Type = Unsigned32
_TlpCoolingEvaporatorFanRunDays_Object = MibTableColumn
tlpCoolingEvaporatorFanRunDays = _TlpCoolingEvaporatorFanRunDays_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 3, 5, 1, 4),
    _TlpCoolingEvaporatorFanRunDays_Type()
)
tlpCoolingEvaporatorFanRunDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpCoolingEvaporatorFanRunDays.setStatus("current")
if mibBuilder.loadTexts:
    tlpCoolingEvaporatorFanRunDays.setUnits("days")
_TlpCoolingCondenserFanRunDays_Type = Unsigned32
_TlpCoolingCondenserFanRunDays_Object = MibTableColumn
tlpCoolingCondenserFanRunDays = _TlpCoolingCondenserFanRunDays_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 3, 5, 1, 5),
    _TlpCoolingCondenserFanRunDays_Type()
)
tlpCoolingCondenserFanRunDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpCoolingCondenserFanRunDays.setStatus("current")
if mibBuilder.loadTexts:
    tlpCoolingCondenserFanRunDays.setUnits("days")
_TlpCoolingAtomizerRunDays_Type = Unsigned32
_TlpCoolingAtomizerRunDays_Object = MibTableColumn
tlpCoolingAtomizerRunDays = _TlpCoolingAtomizerRunDays_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 3, 5, 1, 6),
    _TlpCoolingAtomizerRunDays_Type()
)
tlpCoolingAtomizerRunDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpCoolingAtomizerRunDays.setStatus("current")
if mibBuilder.loadTexts:
    tlpCoolingAtomizerRunDays.setUnits("days")
_TlpCoolingStatusTable_Object = MibTable
tlpCoolingStatusTable = _TlpCoolingStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 3, 6)
)
if mibBuilder.loadTexts:
    tlpCoolingStatusTable.setStatus("current")
_TlpCoolingStatusEntry_Object = MibTableRow
tlpCoolingStatusEntry = _TlpCoolingStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 3, 6, 1)
)
tlpCoolingStatusEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpCoolingStatusEntry.setStatus("current")


class _TlpCoolingOperatingMode_Type(Integer32):
    """Custom type tlpCoolingOperatingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("idle", 1),
          ("cooling", 2),
          ("shuttingDown", 3),
          ("dehumidifying", 4),
          ("defrosting", 5),
          ("notConnected", 6))
    )


_TlpCoolingOperatingMode_Type.__name__ = "Integer32"
_TlpCoolingOperatingMode_Object = MibTableColumn
tlpCoolingOperatingMode = _TlpCoolingOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 3, 6, 1, 1),
    _TlpCoolingOperatingMode_Type()
)
tlpCoolingOperatingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpCoolingOperatingMode.setStatus("current")
_TlpCoolingCoolOutput_Type = Unsigned32
_TlpCoolingCoolOutput_Object = MibTableColumn
tlpCoolingCoolOutput = _TlpCoolingCoolOutput_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 3, 6, 1, 2),
    _TlpCoolingCoolOutput_Type()
)
tlpCoolingCoolOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpCoolingCoolOutput.setStatus("current")
if mibBuilder.loadTexts:
    tlpCoolingCoolOutput.setUnits("0.1 kilowatts")


class _TlpCoolingAlarmStatus_Type(Integer32):
    """Custom type tlpCoolingAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAlarm", 0),
          ("warning", 1),
          ("critical", 2))
    )


_TlpCoolingAlarmStatus_Type.__name__ = "Integer32"
_TlpCoolingAlarmStatus_Object = MibTableColumn
tlpCoolingAlarmStatus = _TlpCoolingAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 3, 6, 1, 3),
    _TlpCoolingAlarmStatus_Type()
)
tlpCoolingAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpCoolingAlarmStatus.setStatus("current")


class _TlpCoolingCompressorStatus_Type(Integer32):
    """Custom type tlpCoolingCompressorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_TlpCoolingCompressorStatus_Type.__name__ = "Integer32"
_TlpCoolingCompressorStatus_Object = MibTableColumn
tlpCoolingCompressorStatus = _TlpCoolingCompressorStatus_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 3, 6, 1, 4),
    _TlpCoolingCompressorStatus_Type()
)
tlpCoolingCompressorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpCoolingCompressorStatus.setStatus("current")


class _TlpCoolingWaterStatus_Type(Integer32):
    """Custom type tlpCoolingWaterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notFull", 0),
          ("full", 1))
    )


_TlpCoolingWaterStatus_Type.__name__ = "Integer32"
_TlpCoolingWaterStatus_Object = MibTableColumn
tlpCoolingWaterStatus = _TlpCoolingWaterStatus_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 3, 6, 1, 5),
    _TlpCoolingWaterStatus_Type()
)
tlpCoolingWaterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpCoolingWaterStatus.setStatus("current")


class _TlpCoolingDefrostMode_Type(Integer32):
    """Custom type tlpCoolingDefrostMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TlpCoolingDefrostMode_Type.__name__ = "Integer32"
_TlpCoolingDefrostMode_Object = MibTableColumn
tlpCoolingDefrostMode = _TlpCoolingDefrostMode_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 3, 6, 1, 6),
    _TlpCoolingDefrostMode_Type()
)
tlpCoolingDefrostMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpCoolingDefrostMode.setStatus("current")


class _TlpCoolingQuietMode_Type(Integer32):
    """Custom type tlpCoolingQuietMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TlpCoolingQuietMode_Type.__name__ = "Integer32"
_TlpCoolingQuietMode_Object = MibTableColumn
tlpCoolingQuietMode = _TlpCoolingQuietMode_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 3, 6, 1, 7),
    _TlpCoolingQuietMode_Type()
)
tlpCoolingQuietMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpCoolingQuietMode.setStatus("current")


class _TlpCoolingHotGasBypass_Type(Integer32):
    """Custom type tlpCoolingHotGasBypass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TlpCoolingHotGasBypass_Type.__name__ = "Integer32"
_TlpCoolingHotGasBypass_Object = MibTableColumn
tlpCoolingHotGasBypass = _TlpCoolingHotGasBypass_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 3, 6, 1, 8),
    _TlpCoolingHotGasBypass_Type()
)
tlpCoolingHotGasBypass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpCoolingHotGasBypass.setStatus("current")


class _TlpCoolingAutoFanSpeed_Type(Integer32):
    """Custom type tlpCoolingAutoFanSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TlpCoolingAutoFanSpeed_Type.__name__ = "Integer32"
_TlpCoolingAutoFanSpeed_Object = MibTableColumn
tlpCoolingAutoFanSpeed = _TlpCoolingAutoFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 3, 6, 1, 9),
    _TlpCoolingAutoFanSpeed_Type()
)
tlpCoolingAutoFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpCoolingAutoFanSpeed.setStatus("current")
_TlpCoolingControl_ObjectIdentity = ObjectIdentity
tlpCoolingControl = _TlpCoolingControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 4)
)
_TlpCoolingControlTable_Object = MibTable
tlpCoolingControlTable = _TlpCoolingControlTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 4, 1)
)
if mibBuilder.loadTexts:
    tlpCoolingControlTable.setStatus("current")
_TlpCoolingControlEntry_Object = MibTableRow
tlpCoolingControlEntry = _TlpCoolingControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 4, 1, 1)
)
tlpCoolingControlEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpCoolingControlEntry.setStatus("current")


class _TlpCoolingMode_Type(Integer32):
    """Custom type tlpCoolingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("turnOffUnit", 0),
          ("turnOnUnit", 1))
    )


_TlpCoolingMode_Type.__name__ = "Integer32"
_TlpCoolingMode_Object = MibTableColumn
tlpCoolingMode = _TlpCoolingMode_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 4, 1, 1, 1),
    _TlpCoolingMode_Type()
)
tlpCoolingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpCoolingMode.setStatus("deprecated")
_TlpCoolingControlOn_Type = TruthValue
_TlpCoolingControlOn_Object = MibTableColumn
tlpCoolingControlOn = _TlpCoolingControlOn_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 4, 1, 1, 2),
    _TlpCoolingControlOn_Type()
)
tlpCoolingControlOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpCoolingControlOn.setStatus("current")
_TlpCoolingControlOff_Type = TruthValue
_TlpCoolingControlOff_Object = MibTableColumn
tlpCoolingControlOff = _TlpCoolingControlOff_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 4, 1, 1, 3),
    _TlpCoolingControlOff_Type()
)
tlpCoolingControlOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpCoolingControlOff.setStatus("current")
_TlpCoolingConfig_ObjectIdentity = ObjectIdentity
tlpCoolingConfig = _TlpCoolingConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 5)
)
_TlpCoolingConfigTable_Object = MibTable
tlpCoolingConfigTable = _TlpCoolingConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 5, 1)
)
if mibBuilder.loadTexts:
    tlpCoolingConfigTable.setStatus("current")
_TlpCoolingConfigEntry_Object = MibTableRow
tlpCoolingConfigEntry = _TlpCoolingConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 5, 1, 1)
)
tlpCoolingConfigEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpCoolingConfigEntry.setStatus("current")


class _TlpCoolingConfigAutoStart_Type(Integer32):
    """Custom type tlpCoolingConfigAutoStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TlpCoolingConfigAutoStart_Type.__name__ = "Integer32"
_TlpCoolingConfigAutoStart_Object = MibTableColumn
tlpCoolingConfigAutoStart = _TlpCoolingConfigAutoStart_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 5, 1, 1, 1),
    _TlpCoolingConfigAutoStart_Type()
)
tlpCoolingConfigAutoStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpCoolingConfigAutoStart.setStatus("deprecated")


class _TlpCoolingConfigFanSpeed_Type(Integer32):
    """Custom type tlpCoolingConfigFanSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("low", 1),
          ("mediumLow", 2),
          ("medium", 3),
          ("mediumHigh", 4),
          ("high", 5),
          ("auto", 6))
    )


_TlpCoolingConfigFanSpeed_Type.__name__ = "Integer32"
_TlpCoolingConfigFanSpeed_Object = MibTableColumn
tlpCoolingConfigFanSpeed = _TlpCoolingConfigFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 5, 1, 1, 2),
    _TlpCoolingConfigFanSpeed_Type()
)
tlpCoolingConfigFanSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpCoolingConfigFanSpeed.setStatus("current")


class _TlpCoolingConfigControlType_Type(Integer32):
    """Custom type tlpCoolingConfigControlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("returnAirTemperature", 0),
          ("remoteTemperature", 1))
    )


_TlpCoolingConfigControlType_Type.__name__ = "Integer32"
_TlpCoolingConfigControlType_Object = MibTableColumn
tlpCoolingConfigControlType = _TlpCoolingConfigControlType_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 5, 1, 1, 3),
    _TlpCoolingConfigControlType_Type()
)
tlpCoolingConfigControlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpCoolingConfigControlType.setStatus("obsolete")


class _TlpCoolingConfigDisplayUnits_Type(Integer32):
    """Custom type tlpCoolingConfigDisplayUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("metric", 0),
          ("english", 1))
    )


_TlpCoolingConfigDisplayUnits_Type.__name__ = "Integer32"
_TlpCoolingConfigDisplayUnits_Object = MibTableColumn
tlpCoolingConfigDisplayUnits = _TlpCoolingConfigDisplayUnits_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 5, 1, 1, 4),
    _TlpCoolingConfigDisplayUnits_Type()
)
tlpCoolingConfigDisplayUnits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpCoolingConfigDisplayUnits.setStatus("current")


class _TlpCoolingConfigBeepOnKey_Type(Integer32):
    """Custom type tlpCoolingConfigBeepOnKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noBeep", 0),
          ("beepOn", 1))
    )


_TlpCoolingConfigBeepOnKey_Type.__name__ = "Integer32"
_TlpCoolingConfigBeepOnKey_Object = MibTableColumn
tlpCoolingConfigBeepOnKey = _TlpCoolingConfigBeepOnKey_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 5, 1, 1, 5),
    _TlpCoolingConfigBeepOnKey_Type()
)
tlpCoolingConfigBeepOnKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpCoolingConfigBeepOnKey.setStatus("obsolete")


class _TlpCoolingConfigInputContactType_Type(Integer32):
    """Custom type tlpCoolingConfigInputContactType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normallyClosed", 0),
          ("normallyOpen", 1))
    )


_TlpCoolingConfigInputContactType_Type.__name__ = "Integer32"
_TlpCoolingConfigInputContactType_Object = MibTableColumn
tlpCoolingConfigInputContactType = _TlpCoolingConfigInputContactType_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 5, 1, 1, 6),
    _TlpCoolingConfigInputContactType_Type()
)
tlpCoolingConfigInputContactType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpCoolingConfigInputContactType.setStatus("deprecated")


class _TlpCoolingConfigOutputContactType_Type(Integer32):
    """Custom type tlpCoolingConfigOutputContactType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normallyClosed", 0),
          ("normallyOpen", 1))
    )


_TlpCoolingConfigOutputContactType_Type.__name__ = "Integer32"
_TlpCoolingConfigOutputContactType_Object = MibTableColumn
tlpCoolingConfigOutputContactType = _TlpCoolingConfigOutputContactType_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 5, 1, 1, 7),
    _TlpCoolingConfigOutputContactType_Type()
)
tlpCoolingConfigOutputContactType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpCoolingConfigOutputContactType.setStatus("deprecated")


class _TlpCoolingConfigOutputRelaySource_Type(Integer32):
    """Custom type tlpCoolingConfigOutputRelaySource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("allAlarmsAndWarnings", 1),
          ("criticalAlarmsOnly", 2))
    )


_TlpCoolingConfigOutputRelaySource_Type.__name__ = "Integer32"
_TlpCoolingConfigOutputRelaySource_Object = MibTableColumn
tlpCoolingConfigOutputRelaySource = _TlpCoolingConfigOutputRelaySource_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 5, 1, 1, 8),
    _TlpCoolingConfigOutputRelaySource_Type()
)
tlpCoolingConfigOutputRelaySource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpCoolingConfigOutputRelaySource.setStatus("deprecated")


class _TlpCoolingConfigOutputRelayDefault_Type(Integer32):
    """Custom type tlpCoolingConfigOutputRelayDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normallyClosed", 0),
          ("normallyOpen", 1))
    )


_TlpCoolingConfigOutputRelayDefault_Type.__name__ = "Integer32"
_TlpCoolingConfigOutputRelayDefault_Object = MibTableColumn
tlpCoolingConfigOutputRelayDefault = _TlpCoolingConfigOutputRelayDefault_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 5, 1, 1, 9),
    _TlpCoolingConfigOutputRelayDefault_Type()
)
tlpCoolingConfigOutputRelayDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpCoolingConfigOutputRelayDefault.setStatus("deprecated")


class _TlpCoolingConfigOffOnInputContact_Type(Integer32):
    """Custom type tlpCoolingConfigOffOnInputContact based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("turnOff", 0),
          ("alarmOnly", 1))
    )


_TlpCoolingConfigOffOnInputContact_Type.__name__ = "Integer32"
_TlpCoolingConfigOffOnInputContact_Object = MibTableColumn
tlpCoolingConfigOffOnInputContact = _TlpCoolingConfigOffOnInputContact_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 5, 1, 1, 10),
    _TlpCoolingConfigOffOnInputContact_Type()
)
tlpCoolingConfigOffOnInputContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpCoolingConfigOffOnInputContact.setStatus("deprecated")


class _TlpCoolingConfigOffOnLeak_Type(Integer32):
    """Custom type tlpCoolingConfigOffOnLeak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("turnOff", 0),
          ("alarmOnly", 1))
    )


_TlpCoolingConfigOffOnLeak_Type.__name__ = "Integer32"
_TlpCoolingConfigOffOnLeak_Object = MibTableColumn
tlpCoolingConfigOffOnLeak = _TlpCoolingConfigOffOnLeak_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 5, 1, 1, 11),
    _TlpCoolingConfigOffOnLeak_Type()
)
tlpCoolingConfigOffOnLeak.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpCoolingConfigOffOnLeak.setStatus("deprecated")


class _TlpCoolingConfigWaterLeakContactType_Type(Integer32):
    """Custom type tlpCoolingConfigWaterLeakContactType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normallyClosed", 0),
          ("normallyOpen", 1))
    )


_TlpCoolingConfigWaterLeakContactType_Type.__name__ = "Integer32"
_TlpCoolingConfigWaterLeakContactType_Object = MibTableColumn
tlpCoolingConfigWaterLeakContactType = _TlpCoolingConfigWaterLeakContactType_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 5, 1, 1, 12),
    _TlpCoolingConfigWaterLeakContactType_Type()
)
tlpCoolingConfigWaterLeakContactType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpCoolingConfigWaterLeakContactType.setStatus("deprecated")
_TlpCoolingConfigAirFilterInterval_Type = Unsigned32
_TlpCoolingConfigAirFilterInterval_Object = MibTableColumn
tlpCoolingConfigAirFilterInterval = _TlpCoolingConfigAirFilterInterval_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 5, 1, 1, 13),
    _TlpCoolingConfigAirFilterInterval_Type()
)
tlpCoolingConfigAirFilterInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpCoolingConfigAirFilterInterval.setStatus("deprecated")
if mibBuilder.loadTexts:
    tlpCoolingConfigAirFilterInterval.setUnits("weeks")


class _TlpCoolingConfigAirFilterAlarm_Type(Integer32):
    """Custom type tlpCoolingConfigAirFilterAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TlpCoolingConfigAirFilterAlarm_Type.__name__ = "Integer32"
_TlpCoolingConfigAirFilterAlarm_Object = MibTableColumn
tlpCoolingConfigAirFilterAlarm = _TlpCoolingConfigAirFilterAlarm_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 5, 1, 1, 14),
    _TlpCoolingConfigAirFilterAlarm_Type()
)
tlpCoolingConfigAirFilterAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpCoolingConfigAirFilterAlarm.setStatus("deprecated")
if mibBuilder.loadTexts:
    tlpCoolingConfigAirFilterAlarm.setUnits("hours")
_TlpCoolingConfigMaxAirFilterRunHours_Type = Unsigned32
_TlpCoolingConfigMaxAirFilterRunHours_Object = MibTableColumn
tlpCoolingConfigMaxAirFilterRunHours = _TlpCoolingConfigMaxAirFilterRunHours_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 5, 1, 1, 15),
    _TlpCoolingConfigMaxAirFilterRunHours_Type()
)
tlpCoolingConfigMaxAirFilterRunHours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpCoolingConfigMaxAirFilterRunHours.setStatus("deprecated")
if mibBuilder.loadTexts:
    tlpCoolingConfigMaxAirFilterRunHours.setUnits("hours")
_TlpCoolingConfigStartTimer_Type = Unsigned32
_TlpCoolingConfigStartTimer_Object = MibTableColumn
tlpCoolingConfigStartTimer = _TlpCoolingConfigStartTimer_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 5, 1, 1, 16),
    _TlpCoolingConfigStartTimer_Type()
)
tlpCoolingConfigStartTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpCoolingConfigStartTimer.setStatus("deprecated")
if mibBuilder.loadTexts:
    tlpCoolingConfigStartTimer.setUnits("minutes")
_TlpCoolingConfigStopTimer_Type = Unsigned32
_TlpCoolingConfigStopTimer_Object = MibTableColumn
tlpCoolingConfigStopTimer = _TlpCoolingConfigStopTimer_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 5, 1, 1, 17),
    _TlpCoolingConfigStopTimer_Type()
)
tlpCoolingConfigStopTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpCoolingConfigStopTimer.setStatus("deprecated")
if mibBuilder.loadTexts:
    tlpCoolingConfigStopTimer.setUnits("minutes")


class _TlpCoolingConfigEnergyMode_Type(Integer32):
    """Custom type tlpCoolingConfigEnergyMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normalCooling", 0),
          ("energySaving", 1))
    )


_TlpCoolingConfigEnergyMode_Type.__name__ = "Integer32"
_TlpCoolingConfigEnergyMode_Object = MibTableColumn
tlpCoolingConfigEnergyMode = _TlpCoolingConfigEnergyMode_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 5, 1, 1, 18),
    _TlpCoolingConfigEnergyMode_Type()
)
tlpCoolingConfigEnergyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpCoolingConfigEnergyMode.setStatus("current")


class _TlpCoolingConfigDefrostMode_Type(Integer32):
    """Custom type tlpCoolingConfigDefrostMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TlpCoolingConfigDefrostMode_Type.__name__ = "Integer32"
_TlpCoolingConfigDefrostMode_Object = MibTableColumn
tlpCoolingConfigDefrostMode = _TlpCoolingConfigDefrostMode_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 5, 1, 1, 19),
    _TlpCoolingConfigDefrostMode_Type()
)
tlpCoolingConfigDefrostMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpCoolingConfigDefrostMode.setStatus("deprecated")


class _TlpCoolingConfigRemoteTemperatureSensor_Type(Integer32):
    """Custom type tlpCoolingConfigRemoteTemperatureSensor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TlpCoolingConfigRemoteTemperatureSensor_Type.__name__ = "Integer32"
_TlpCoolingConfigRemoteTemperatureSensor_Object = MibTableColumn
tlpCoolingConfigRemoteTemperatureSensor = _TlpCoolingConfigRemoteTemperatureSensor_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 5, 1, 1, 20),
    _TlpCoolingConfigRemoteTemperatureSensor_Type()
)
tlpCoolingConfigRemoteTemperatureSensor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpCoolingConfigRemoteTemperatureSensor.setStatus("current")


class _TlpCoolingConfigDehumidifyingMode_Type(Integer32):
    """Custom type tlpCoolingConfigDehumidifyingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TlpCoolingConfigDehumidifyingMode_Type.__name__ = "Integer32"
_TlpCoolingConfigDehumidifyingMode_Object = MibTableColumn
tlpCoolingConfigDehumidifyingMode = _TlpCoolingConfigDehumidifyingMode_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 5, 1, 1, 21),
    _TlpCoolingConfigDehumidifyingMode_Type()
)
tlpCoolingConfigDehumidifyingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpCoolingConfigDehumidifyingMode.setStatus("current")


class _TlpCoolingConfigFanAlwaysOn_Type(Integer32):
    """Custom type tlpCoolingConfigFanAlwaysOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TlpCoolingConfigFanAlwaysOn_Type.__name__ = "Integer32"
_TlpCoolingConfigFanAlwaysOn_Object = MibTableColumn
tlpCoolingConfigFanAlwaysOn = _TlpCoolingConfigFanAlwaysOn_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 5, 1, 1, 22),
    _TlpCoolingConfigFanAlwaysOn_Type()
)
tlpCoolingConfigFanAlwaysOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpCoolingConfigFanAlwaysOn.setStatus("current")


class _TlpCoolingConfigQuietMode_Type(Integer32):
    """Custom type tlpCoolingConfigQuietMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TlpCoolingConfigQuietMode_Type.__name__ = "Integer32"
_TlpCoolingConfigQuietMode_Object = MibTableColumn
tlpCoolingConfigQuietMode = _TlpCoolingConfigQuietMode_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 5, 1, 1, 23),
    _TlpCoolingConfigQuietMode_Type()
)
tlpCoolingConfigQuietMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpCoolingConfigQuietMode.setStatus("obsolete")


class _TlpCoolingConfigHotGasBypass_Type(Integer32):
    """Custom type tlpCoolingConfigHotGasBypass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TlpCoolingConfigHotGasBypass_Type.__name__ = "Integer32"
_TlpCoolingConfigHotGasBypass_Object = MibTableColumn
tlpCoolingConfigHotGasBypass = _TlpCoolingConfigHotGasBypass_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 5, 1, 1, 24),
    _TlpCoolingConfigHotGasBypass_Type()
)
tlpCoolingConfigHotGasBypass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpCoolingConfigHotGasBypass.setStatus("deprecated")


class _TlpCoolingConfigAutoFanSpeed_Type(Integer32):
    """Custom type tlpCoolingConfigAutoFanSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TlpCoolingConfigAutoFanSpeed_Type.__name__ = "Integer32"
_TlpCoolingConfigAutoFanSpeed_Object = MibTableColumn
tlpCoolingConfigAutoFanSpeed = _TlpCoolingConfigAutoFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 5, 1, 1, 25),
    _TlpCoolingConfigAutoFanSpeed_Type()
)
tlpCoolingConfigAutoFanSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpCoolingConfigAutoFanSpeed.setStatus("deprecated")
_TlpCoolingConfigTemperatureFahrenheitTable_Object = MibTable
tlpCoolingConfigTemperatureFahrenheitTable = _TlpCoolingConfigTemperatureFahrenheitTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 5, 2)
)
if mibBuilder.loadTexts:
    tlpCoolingConfigTemperatureFahrenheitTable.setStatus("current")
_TlpCoolingConfigTemperatureFahrenheitEntry_Object = MibTableRow
tlpCoolingConfigTemperatureFahrenheitEntry = _TlpCoolingConfigTemperatureFahrenheitEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 5, 2, 1)
)
tlpCoolingConfigTemperatureFahrenheitEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpCoolingConfigTemperatureFahrenheitEntry.setStatus("current")
_TlpCoolingSetPointDegF_Type = Integer32
_TlpCoolingSetPointDegF_Object = MibTableColumn
tlpCoolingSetPointDegF = _TlpCoolingSetPointDegF_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 5, 2, 1, 1),
    _TlpCoolingSetPointDegF_Type()
)
tlpCoolingSetPointDegF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpCoolingSetPointDegF.setStatus("current")
if mibBuilder.loadTexts:
    tlpCoolingSetPointDegF.setUnits("0.1 degrees Fahrenheit")
_TlpCoolingSupplyAirHighLimitDegF_Type = Integer32
_TlpCoolingSupplyAirHighLimitDegF_Object = MibTableColumn
tlpCoolingSupplyAirHighLimitDegF = _TlpCoolingSupplyAirHighLimitDegF_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 5, 2, 1, 2),
    _TlpCoolingSupplyAirHighLimitDegF_Type()
)
tlpCoolingSupplyAirHighLimitDegF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpCoolingSupplyAirHighLimitDegF.setStatus("current")
if mibBuilder.loadTexts:
    tlpCoolingSupplyAirHighLimitDegF.setUnits("0.1 degrees Fahrenheit")
_TlpCoolingSupplyAirLowLimitDegF_Type = Integer32
_TlpCoolingSupplyAirLowLimitDegF_Object = MibTableColumn
tlpCoolingSupplyAirLowLimitDegF = _TlpCoolingSupplyAirLowLimitDegF_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 5, 2, 1, 3),
    _TlpCoolingSupplyAirLowLimitDegF_Type()
)
tlpCoolingSupplyAirLowLimitDegF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpCoolingSupplyAirLowLimitDegF.setStatus("current")
if mibBuilder.loadTexts:
    tlpCoolingSupplyAirLowLimitDegF.setUnits("0.1 degrees Fahrenheit")
_TlpCoolingMaxDeviationLimitDegF_Type = Integer32
_TlpCoolingMaxDeviationLimitDegF_Object = MibTableColumn
tlpCoolingMaxDeviationLimitDegF = _TlpCoolingMaxDeviationLimitDegF_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 5, 2, 1, 4),
    _TlpCoolingMaxDeviationLimitDegF_Type()
)
tlpCoolingMaxDeviationLimitDegF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpCoolingMaxDeviationLimitDegF.setStatus("current")
if mibBuilder.loadTexts:
    tlpCoolingMaxDeviationLimitDegF.setUnits("0.1 degrees Fahrenheit")
_TlpCoolingReturnAirHighLimitDegF_Type = Integer32
_TlpCoolingReturnAirHighLimitDegF_Object = MibTableColumn
tlpCoolingReturnAirHighLimitDegF = _TlpCoolingReturnAirHighLimitDegF_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 5, 2, 1, 5),
    _TlpCoolingReturnAirHighLimitDegF_Type()
)
tlpCoolingReturnAirHighLimitDegF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpCoolingReturnAirHighLimitDegF.setStatus("current")
if mibBuilder.loadTexts:
    tlpCoolingReturnAirHighLimitDegF.setUnits("0.1 degrees Fahrenheit")
_TlpCoolingReturnAirLowLimitDegF_Type = Integer32
_TlpCoolingReturnAirLowLimitDegF_Object = MibTableColumn
tlpCoolingReturnAirLowLimitDegF = _TlpCoolingReturnAirLowLimitDegF_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 5, 2, 1, 6),
    _TlpCoolingReturnAirLowLimitDegF_Type()
)
tlpCoolingReturnAirLowLimitDegF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpCoolingReturnAirLowLimitDegF.setStatus("current")
if mibBuilder.loadTexts:
    tlpCoolingReturnAirLowLimitDegF.setUnits("0.1 degrees Fahrenheit")
_TlpCoolingRemoteSetPointDegF_Type = Integer32
_TlpCoolingRemoteSetPointDegF_Object = MibTableColumn
tlpCoolingRemoteSetPointDegF = _TlpCoolingRemoteSetPointDegF_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 5, 2, 1, 7),
    _TlpCoolingRemoteSetPointDegF_Type()
)
tlpCoolingRemoteSetPointDegF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpCoolingRemoteSetPointDegF.setStatus("current")
if mibBuilder.loadTexts:
    tlpCoolingRemoteSetPointDegF.setUnits("0.1 degrees Fahrenheit")
_TlpCoolingConfigTemperatureCelsiusTable_Object = MibTable
tlpCoolingConfigTemperatureCelsiusTable = _TlpCoolingConfigTemperatureCelsiusTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 5, 3)
)
if mibBuilder.loadTexts:
    tlpCoolingConfigTemperatureCelsiusTable.setStatus("current")
_TlpCoolingConfigTemperatureCelsiusEntry_Object = MibTableRow
tlpCoolingConfigTemperatureCelsiusEntry = _TlpCoolingConfigTemperatureCelsiusEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 5, 3, 1)
)
tlpCoolingConfigTemperatureCelsiusEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpCoolingConfigTemperatureCelsiusEntry.setStatus("current")
_TlpCoolingSetPointDegC_Type = Integer32
_TlpCoolingSetPointDegC_Object = MibTableColumn
tlpCoolingSetPointDegC = _TlpCoolingSetPointDegC_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 5, 3, 1, 1),
    _TlpCoolingSetPointDegC_Type()
)
tlpCoolingSetPointDegC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpCoolingSetPointDegC.setStatus("current")
if mibBuilder.loadTexts:
    tlpCoolingSetPointDegC.setUnits("0.1 degrees Celsius")
_TlpCoolingSupplyAirHighLimitDegC_Type = Integer32
_TlpCoolingSupplyAirHighLimitDegC_Object = MibTableColumn
tlpCoolingSupplyAirHighLimitDegC = _TlpCoolingSupplyAirHighLimitDegC_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 5, 3, 1, 2),
    _TlpCoolingSupplyAirHighLimitDegC_Type()
)
tlpCoolingSupplyAirHighLimitDegC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpCoolingSupplyAirHighLimitDegC.setStatus("current")
if mibBuilder.loadTexts:
    tlpCoolingSupplyAirHighLimitDegC.setUnits("0.1 degrees Celsius")
_TlpCoolingSupplyAirLowLimitDegC_Type = Integer32
_TlpCoolingSupplyAirLowLimitDegC_Object = MibTableColumn
tlpCoolingSupplyAirLowLimitDegC = _TlpCoolingSupplyAirLowLimitDegC_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 5, 3, 1, 3),
    _TlpCoolingSupplyAirLowLimitDegC_Type()
)
tlpCoolingSupplyAirLowLimitDegC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpCoolingSupplyAirLowLimitDegC.setStatus("current")
if mibBuilder.loadTexts:
    tlpCoolingSupplyAirLowLimitDegC.setUnits("0.1 degrees Celsius")
_TlpCoolingMaxDeviationLimitDegC_Type = Integer32
_TlpCoolingMaxDeviationLimitDegC_Object = MibTableColumn
tlpCoolingMaxDeviationLimitDegC = _TlpCoolingMaxDeviationLimitDegC_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 5, 3, 1, 4),
    _TlpCoolingMaxDeviationLimitDegC_Type()
)
tlpCoolingMaxDeviationLimitDegC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpCoolingMaxDeviationLimitDegC.setStatus("current")
if mibBuilder.loadTexts:
    tlpCoolingMaxDeviationLimitDegC.setUnits("0.1 degrees Celsius")
_TlpCoolingReturnAirHighLimitDegC_Type = Integer32
_TlpCoolingReturnAirHighLimitDegC_Object = MibTableColumn
tlpCoolingReturnAirHighLimitDegC = _TlpCoolingReturnAirHighLimitDegC_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 5, 3, 1, 5),
    _TlpCoolingReturnAirHighLimitDegC_Type()
)
tlpCoolingReturnAirHighLimitDegC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpCoolingReturnAirHighLimitDegC.setStatus("current")
if mibBuilder.loadTexts:
    tlpCoolingReturnAirHighLimitDegC.setUnits("0.1 degrees Celsius")
_TlpCoolingReturnAirLowLimitDegC_Type = Integer32
_TlpCoolingReturnAirLowLimitDegC_Object = MibTableColumn
tlpCoolingReturnAirLowLimitDegC = _TlpCoolingReturnAirLowLimitDegC_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 5, 3, 1, 6),
    _TlpCoolingReturnAirLowLimitDegC_Type()
)
tlpCoolingReturnAirLowLimitDegC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpCoolingReturnAirLowLimitDegC.setStatus("current")
if mibBuilder.loadTexts:
    tlpCoolingReturnAirLowLimitDegC.setUnits("0.1 degrees Celsius")
_TlpCoolingRemoteSetPointDegC_Type = Integer32
_TlpCoolingRemoteSetPointDegC_Object = MibTableColumn
tlpCoolingRemoteSetPointDegC = _TlpCoolingRemoteSetPointDegC_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 5, 3, 1, 7),
    _TlpCoolingRemoteSetPointDegC_Type()
)
tlpCoolingRemoteSetPointDegC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpCoolingRemoteSetPointDegC.setStatus("current")
if mibBuilder.loadTexts:
    tlpCoolingRemoteSetPointDegC.setUnits("0.1 degrees Celsius")
_TlpKvm_ObjectIdentity = ObjectIdentity
tlpKvm = _TlpKvm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 6)
)
_TlpKvmIdent_ObjectIdentity = ObjectIdentity
tlpKvmIdent = _TlpKvmIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 6, 1)
)
_TlpKvmIdentNumKvm_Type = Unsigned32
_TlpKvmIdentNumKvm_Object = MibScalar
tlpKvmIdentNumKvm = _TlpKvmIdentNumKvm_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 6, 1, 1),
    _TlpKvmIdentNumKvm_Type()
)
tlpKvmIdentNumKvm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpKvmIdentNumKvm.setStatus("current")
_TlpKvmDevice_ObjectIdentity = ObjectIdentity
tlpKvmDevice = _TlpKvmDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 6, 2)
)
_TlpKvmDetail_ObjectIdentity = ObjectIdentity
tlpKvmDetail = _TlpKvmDetail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 6, 3)
)
_TlpKvmControl_ObjectIdentity = ObjectIdentity
tlpKvmControl = _TlpKvmControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 6, 4)
)
_TlpKvmConfig_ObjectIdentity = ObjectIdentity
tlpKvmConfig = _TlpKvmConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 6, 5)
)
_TlpRackTrack_ObjectIdentity = ObjectIdentity
tlpRackTrack = _TlpRackTrack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 7)
)
_TlpRackTrackIdent_ObjectIdentity = ObjectIdentity
tlpRackTrackIdent = _TlpRackTrackIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 7, 1)
)
_TlpRackTrackIdentNumRackTrack_Type = Unsigned32
_TlpRackTrackIdentNumRackTrack_Object = MibScalar
tlpRackTrackIdentNumRackTrack = _TlpRackTrackIdentNumRackTrack_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 7, 1, 1),
    _TlpRackTrackIdentNumRackTrack_Type()
)
tlpRackTrackIdentNumRackTrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpRackTrackIdentNumRackTrack.setStatus("current")
_TlpRackTrackDevice_ObjectIdentity = ObjectIdentity
tlpRackTrackDevice = _TlpRackTrackDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 7, 2)
)
_TlpRackTrackDetail_ObjectIdentity = ObjectIdentity
tlpRackTrackDetail = _TlpRackTrackDetail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 7, 3)
)
_TlpRackTrackControl_ObjectIdentity = ObjectIdentity
tlpRackTrackControl = _TlpRackTrackControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 7, 4)
)
_TlpRackTrackConfig_ObjectIdentity = ObjectIdentity
tlpRackTrackConfig = _TlpRackTrackConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 7, 5)
)
_TlpSwitch_ObjectIdentity = ObjectIdentity
tlpSwitch = _TlpSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 8)
)
_TlpSwitchIdent_ObjectIdentity = ObjectIdentity
tlpSwitchIdent = _TlpSwitchIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 8, 1)
)
_TlpSwitchIdentNumSwitch_Type = Unsigned32
_TlpSwitchIdentNumSwitch_Object = MibScalar
tlpSwitchIdentNumSwitch = _TlpSwitchIdentNumSwitch_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 8, 1, 1),
    _TlpSwitchIdentNumSwitch_Type()
)
tlpSwitchIdentNumSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpSwitchIdentNumSwitch.setStatus("current")
_TlpSwitchDevice_ObjectIdentity = ObjectIdentity
tlpSwitchDevice = _TlpSwitchDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 8, 2)
)
_TlpSwitchDetail_ObjectIdentity = ObjectIdentity
tlpSwitchDetail = _TlpSwitchDetail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 8, 3)
)
_TlpSwitchControl_ObjectIdentity = ObjectIdentity
tlpSwitchControl = _TlpSwitchControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 8, 4)
)
_TlpSwitchConfig_ObjectIdentity = ObjectIdentity
tlpSwitchConfig = _TlpSwitchConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 8, 5)
)
_TlpSoftware_ObjectIdentity = ObjectIdentity
tlpSoftware = _TlpSoftware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 2)
)
_TlpAgentDetails_ObjectIdentity = ObjectIdentity
tlpAgentDetails = _TlpAgentDetails_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1)
)
_TlpAgentIdent_ObjectIdentity = ObjectIdentity
tlpAgentIdent = _TlpAgentIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 1)
)


class _TlpAgentType_Type(Integer32):
    """Custom type tlpAgentType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("pal", 1),
          ("pansa", 2),
          ("delta", 3),
          ("sinetica", 4),
          ("netos6", 5),
          ("netos7", 6),
          ("panms", 7),
          ("nmc5", 8))
    )


_TlpAgentType_Type.__name__ = "Integer32"
_TlpAgentType_Object = MibScalar
tlpAgentType = _TlpAgentType_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 1, 1),
    _TlpAgentType_Type()
)
tlpAgentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentType.setStatus("current")
_TlpAgentVersion_Type = DisplayString
_TlpAgentVersion_Object = MibScalar
tlpAgentVersion = _TlpAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 1, 2),
    _TlpAgentVersion_Type()
)
tlpAgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentVersion.setStatus("current")
_TlpAgentDriverVersion_Type = DisplayString
_TlpAgentDriverVersion_Object = MibScalar
tlpAgentDriverVersion = _TlpAgentDriverVersion_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 1, 3),
    _TlpAgentDriverVersion_Type()
)
tlpAgentDriverVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentDriverVersion.setStatus("deprecated")
_TlpAgentMAC_Type = DisplayString
_TlpAgentMAC_Object = MibScalar
tlpAgentMAC = _TlpAgentMAC_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 1, 4),
    _TlpAgentMAC_Type()
)
tlpAgentMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentMAC.setStatus("current")
_TlpAgentSerialNum_Type = DisplayString
_TlpAgentSerialNum_Object = MibScalar
tlpAgentSerialNum = _TlpAgentSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 1, 5),
    _TlpAgentSerialNum_Type()
)
tlpAgentSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentSerialNum.setStatus("current")
_TlpAgentUuid_Type = DisplayString
_TlpAgentUuid_Object = MibScalar
tlpAgentUuid = _TlpAgentUuid_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 1, 6),
    _TlpAgentUuid_Type()
)
tlpAgentUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentUuid.setStatus("current")
_TlpAgentAttributes_ObjectIdentity = ObjectIdentity
tlpAgentAttributes = _TlpAgentAttributes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 2)
)
_TlpAgentAttributesSupports_ObjectIdentity = ObjectIdentity
tlpAgentAttributesSupports = _TlpAgentAttributesSupports_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 2, 1)
)
_TlpAgentAttributesSupportsHTTP_Type = TruthValue
_TlpAgentAttributesSupportsHTTP_Object = MibScalar
tlpAgentAttributesSupportsHTTP = _TlpAgentAttributesSupportsHTTP_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 2, 1, 1),
    _TlpAgentAttributesSupportsHTTP_Type()
)
tlpAgentAttributesSupportsHTTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAttributesSupportsHTTP.setStatus("current")
_TlpAgentAttributesSupportsHTTPS_Type = TruthValue
_TlpAgentAttributesSupportsHTTPS_Object = MibScalar
tlpAgentAttributesSupportsHTTPS = _TlpAgentAttributesSupportsHTTPS_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 2, 1, 2),
    _TlpAgentAttributesSupportsHTTPS_Type()
)
tlpAgentAttributesSupportsHTTPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAttributesSupportsHTTPS.setStatus("current")
_TlpAgentAttributesSupportsFTP_Type = TruthValue
_TlpAgentAttributesSupportsFTP_Object = MibScalar
tlpAgentAttributesSupportsFTP = _TlpAgentAttributesSupportsFTP_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 2, 1, 3),
    _TlpAgentAttributesSupportsFTP_Type()
)
tlpAgentAttributesSupportsFTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAttributesSupportsFTP.setStatus("current")
_TlpAgentAttributesSupportsTelnet_Type = TruthValue
_TlpAgentAttributesSupportsTelnet_Object = MibScalar
tlpAgentAttributesSupportsTelnet = _TlpAgentAttributesSupportsTelnet_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 2, 1, 4),
    _TlpAgentAttributesSupportsTelnet_Type()
)
tlpAgentAttributesSupportsTelnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAttributesSupportsTelnet.setStatus("current")
_TlpAgentAttributesSupportsObsolete1_Type = TruthValue
_TlpAgentAttributesSupportsObsolete1_Object = MibScalar
tlpAgentAttributesSupportsObsolete1 = _TlpAgentAttributesSupportsObsolete1_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 2, 1, 5),
    _TlpAgentAttributesSupportsObsolete1_Type()
)
tlpAgentAttributesSupportsObsolete1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAttributesSupportsObsolete1.setStatus("deprecated")
_TlpAgentAttributesSupportsSSH_Type = TruthValue
_TlpAgentAttributesSupportsSSH_Object = MibScalar
tlpAgentAttributesSupportsSSH = _TlpAgentAttributesSupportsSSH_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 2, 1, 6),
    _TlpAgentAttributesSupportsSSH_Type()
)
tlpAgentAttributesSupportsSSH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAttributesSupportsSSH.setStatus("current")
_TlpAgentAttributesSupportsObsolete2_Type = TruthValue
_TlpAgentAttributesSupportsObsolete2_Object = MibScalar
tlpAgentAttributesSupportsObsolete2 = _TlpAgentAttributesSupportsObsolete2_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 2, 1, 7),
    _TlpAgentAttributesSupportsObsolete2_Type()
)
tlpAgentAttributesSupportsObsolete2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAttributesSupportsObsolete2.setStatus("deprecated")
_TlpAgentAttributesSupportsSNMP_Type = TruthValue
_TlpAgentAttributesSupportsSNMP_Object = MibScalar
tlpAgentAttributesSupportsSNMP = _TlpAgentAttributesSupportsSNMP_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 2, 1, 8),
    _TlpAgentAttributesSupportsSNMP_Type()
)
tlpAgentAttributesSupportsSNMP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAttributesSupportsSNMP.setStatus("current")
_TlpAgentAttributesSupportsSNMPTrap_Type = TruthValue
_TlpAgentAttributesSupportsSNMPTrap_Object = MibScalar
tlpAgentAttributesSupportsSNMPTrap = _TlpAgentAttributesSupportsSNMPTrap_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 2, 1, 9),
    _TlpAgentAttributesSupportsSNMPTrap_Type()
)
tlpAgentAttributesSupportsSNMPTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAttributesSupportsSNMPTrap.setStatus("current")
_TlpAgentAttributesEnabled_ObjectIdentity = ObjectIdentity
tlpAgentAttributesEnabled = _TlpAgentAttributesEnabled_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 2, 2)
)
_TlpAgentAttributesHTTPEnabled_Type = TruthValue
_TlpAgentAttributesHTTPEnabled_Object = MibScalar
tlpAgentAttributesHTTPEnabled = _TlpAgentAttributesHTTPEnabled_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 2, 2, 1),
    _TlpAgentAttributesHTTPEnabled_Type()
)
tlpAgentAttributesHTTPEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAttributesHTTPEnabled.setStatus("current")
_TlpAgentAttributesHTTPSEnabled_Type = TruthValue
_TlpAgentAttributesHTTPSEnabled_Object = MibScalar
tlpAgentAttributesHTTPSEnabled = _TlpAgentAttributesHTTPSEnabled_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 2, 2, 2),
    _TlpAgentAttributesHTTPSEnabled_Type()
)
tlpAgentAttributesHTTPSEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAttributesHTTPSEnabled.setStatus("current")
_TlpAgentAttributesFTPEnabled_Type = TruthValue
_TlpAgentAttributesFTPEnabled_Object = MibScalar
tlpAgentAttributesFTPEnabled = _TlpAgentAttributesFTPEnabled_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 2, 2, 3),
    _TlpAgentAttributesFTPEnabled_Type()
)
tlpAgentAttributesFTPEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAttributesFTPEnabled.setStatus("deprecated")
_TlpAgentAttributesTelnetEnabled_Type = TruthValue
_TlpAgentAttributesTelnetEnabled_Object = MibScalar
tlpAgentAttributesTelnetEnabled = _TlpAgentAttributesTelnetEnabled_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 2, 2, 4),
    _TlpAgentAttributesTelnetEnabled_Type()
)
tlpAgentAttributesTelnetEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAttributesTelnetEnabled.setStatus("current")
_TlpAgentAttributesObsolete1Enabled_Type = TruthValue
_TlpAgentAttributesObsolete1Enabled_Object = MibScalar
tlpAgentAttributesObsolete1Enabled = _TlpAgentAttributesObsolete1Enabled_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 2, 2, 5),
    _TlpAgentAttributesObsolete1Enabled_Type()
)
tlpAgentAttributesObsolete1Enabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAttributesObsolete1Enabled.setStatus("deprecated")
_TlpAgentAttributesSSHEnabled_Type = TruthValue
_TlpAgentAttributesSSHEnabled_Object = MibScalar
tlpAgentAttributesSSHEnabled = _TlpAgentAttributesSSHEnabled_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 2, 2, 6),
    _TlpAgentAttributesSSHEnabled_Type()
)
tlpAgentAttributesSSHEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAttributesSSHEnabled.setStatus("current")
_TlpAgentAttributesSFTPEnabled_Type = TruthValue
_TlpAgentAttributesSFTPEnabled_Object = MibScalar
tlpAgentAttributesSFTPEnabled = _TlpAgentAttributesSFTPEnabled_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 2, 2, 7),
    _TlpAgentAttributesSFTPEnabled_Type()
)
tlpAgentAttributesSFTPEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAttributesSFTPEnabled.setStatus("deprecated")
_TlpAgentAttributesObsolete2Enabled_Type = TruthValue
_TlpAgentAttributesObsolete2Enabled_Object = MibScalar
tlpAgentAttributesObsolete2Enabled = _TlpAgentAttributesObsolete2Enabled_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 2, 2, 8),
    _TlpAgentAttributesObsolete2Enabled_Type()
)
tlpAgentAttributesObsolete2Enabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAttributesObsolete2Enabled.setStatus("deprecated")
_TlpAgentAttributesSnmp_ObjectIdentity = ObjectIdentity
tlpAgentAttributesSnmp = _TlpAgentAttributesSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 2, 3)
)
_TlpAgentAttributesSNMPv1Enabled_Type = TruthValue
_TlpAgentAttributesSNMPv1Enabled_Object = MibScalar
tlpAgentAttributesSNMPv1Enabled = _TlpAgentAttributesSNMPv1Enabled_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 2, 3, 1),
    _TlpAgentAttributesSNMPv1Enabled_Type()
)
tlpAgentAttributesSNMPv1Enabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAttributesSNMPv1Enabled.setStatus("current")
_TlpAgentAttributesSNMPv2cEnabled_Type = TruthValue
_TlpAgentAttributesSNMPv2cEnabled_Object = MibScalar
tlpAgentAttributesSNMPv2cEnabled = _TlpAgentAttributesSNMPv2cEnabled_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 2, 3, 2),
    _TlpAgentAttributesSNMPv2cEnabled_Type()
)
tlpAgentAttributesSNMPv2cEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAttributesSNMPv2cEnabled.setStatus("current")
_TlpAgentAttributesSNMPv3Enabled_Type = TruthValue
_TlpAgentAttributesSNMPv3Enabled_Object = MibScalar
tlpAgentAttributesSNMPv3Enabled = _TlpAgentAttributesSNMPv3Enabled_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 2, 3, 3),
    _TlpAgentAttributesSNMPv3Enabled_Type()
)
tlpAgentAttributesSNMPv3Enabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAttributesSNMPv3Enabled.setStatus("current")
_TlpAgentAttributesPorts_ObjectIdentity = ObjectIdentity
tlpAgentAttributesPorts = _TlpAgentAttributesPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 2, 4)
)
_TlpAgentAttributesHTTPPort_Type = Unsigned32
_TlpAgentAttributesHTTPPort_Object = MibScalar
tlpAgentAttributesHTTPPort = _TlpAgentAttributesHTTPPort_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 2, 4, 1),
    _TlpAgentAttributesHTTPPort_Type()
)
tlpAgentAttributesHTTPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAttributesHTTPPort.setStatus("current")
_TlpAgentAttributesHTTPSPort_Type = Unsigned32
_TlpAgentAttributesHTTPSPort_Object = MibScalar
tlpAgentAttributesHTTPSPort = _TlpAgentAttributesHTTPSPort_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 2, 4, 2),
    _TlpAgentAttributesHTTPSPort_Type()
)
tlpAgentAttributesHTTPSPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAttributesHTTPSPort.setStatus("current")
_TlpAgentAttributesFTPPort_Type = Unsigned32
_TlpAgentAttributesFTPPort_Object = MibScalar
tlpAgentAttributesFTPPort = _TlpAgentAttributesFTPPort_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 2, 4, 3),
    _TlpAgentAttributesFTPPort_Type()
)
tlpAgentAttributesFTPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAttributesFTPPort.setStatus("deprecated")
_TlpAgentAttributesTelnetPort_Type = Unsigned32
_TlpAgentAttributesTelnetPort_Object = MibScalar
tlpAgentAttributesTelnetPort = _TlpAgentAttributesTelnetPort_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 2, 4, 4),
    _TlpAgentAttributesTelnetPort_Type()
)
tlpAgentAttributesTelnetPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAttributesTelnetPort.setStatus("current")
_TlpAgentAttributesObsolete1Port_Type = Unsigned32
_TlpAgentAttributesObsolete1Port_Object = MibScalar
tlpAgentAttributesObsolete1Port = _TlpAgentAttributesObsolete1Port_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 2, 4, 5),
    _TlpAgentAttributesObsolete1Port_Type()
)
tlpAgentAttributesObsolete1Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAttributesObsolete1Port.setStatus("deprecated")
_TlpAgentAttributesSSHPort_Type = Unsigned32
_TlpAgentAttributesSSHPort_Object = MibScalar
tlpAgentAttributesSSHPort = _TlpAgentAttributesSSHPort_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 2, 4, 6),
    _TlpAgentAttributesSSHPort_Type()
)
tlpAgentAttributesSSHPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAttributesSSHPort.setStatus("current")
_TlpAgentAttributesObsolete2Port_Type = Unsigned32
_TlpAgentAttributesObsolete2Port_Object = MibScalar
tlpAgentAttributesObsolete2Port = _TlpAgentAttributesObsolete2Port_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 2, 4, 7),
    _TlpAgentAttributesObsolete2Port_Type()
)
tlpAgentAttributesObsolete2Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAttributesObsolete2Port.setStatus("deprecated")
_TlpAgentAttributesSNMPPort_Type = Unsigned32
_TlpAgentAttributesSNMPPort_Object = MibScalar
tlpAgentAttributesSNMPPort = _TlpAgentAttributesSNMPPort_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 2, 4, 8),
    _TlpAgentAttributesSNMPPort_Type()
)
tlpAgentAttributesSNMPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAttributesSNMPPort.setStatus("current")
_TlpAgentAttributesSNMPTrapPort_Type = Unsigned32
_TlpAgentAttributesSNMPTrapPort_Object = MibScalar
tlpAgentAttributesSNMPTrapPort = _TlpAgentAttributesSNMPTrapPort_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 2, 4, 9),
    _TlpAgentAttributesSNMPTrapPort_Type()
)
tlpAgentAttributesSNMPTrapPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAttributesSNMPTrapPort.setStatus("current")
_TlpAgentAttributesOptions_ObjectIdentity = ObjectIdentity
tlpAgentAttributesOptions = _TlpAgentAttributesOptions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 2, 5)
)
_TlpAgentAttributesHTTPRedirected_Type = TruthValue
_TlpAgentAttributesHTTPRedirected_Object = MibScalar
tlpAgentAttributesHTTPRedirected = _TlpAgentAttributesHTTPRedirected_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 2, 5, 1),
    _TlpAgentAttributesHTTPRedirected_Type()
)
tlpAgentAttributesHTTPRedirected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAttributesHTTPRedirected.setStatus("current")
_TlpAgentAddresses_ObjectIdentity = ObjectIdentity
tlpAgentAddresses = _TlpAgentAddresses_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 3)
)
_TlpAgentAddressIPv4_Type = DisplayString
_TlpAgentAddressIPv4_Object = MibScalar
tlpAgentAddressIPv4 = _TlpAgentAddressIPv4_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 3, 1),
    _TlpAgentAddressIPv4_Type()
)
tlpAgentAddressIPv4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAddressIPv4.setStatus("current")
_TlpAgentAddressIPv6_Type = DisplayString
_TlpAgentAddressIPv6_Object = MibScalar
tlpAgentAddressIPv6 = _TlpAgentAddressIPv6_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 3, 2),
    _TlpAgentAddressIPv6_Type()
)
tlpAgentAddressIPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAddressIPv6.setStatus("current")
_TlpAgentSettings_ObjectIdentity = ObjectIdentity
tlpAgentSettings = _TlpAgentSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 2)
)
_TlpAgentConfig_ObjectIdentity = ObjectIdentity
tlpAgentConfig = _TlpAgentConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 2, 1)
)
_TlpAgentConfigRemoteRegistration_Type = DisplayString
_TlpAgentConfigRemoteRegistration_Object = MibScalar
tlpAgentConfigRemoteRegistration = _TlpAgentConfigRemoteRegistration_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 2, 1, 1),
    _TlpAgentConfigRemoteRegistration_Type()
)
tlpAgentConfigRemoteRegistration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAgentConfigRemoteRegistration.setStatus("current")
_TlpAgentConfigCurrentTime_Type = DisplayString
_TlpAgentConfigCurrentTime_Object = MibScalar
tlpAgentConfigCurrentTime = _TlpAgentConfigCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 2, 1, 2),
    _TlpAgentConfigCurrentTime_Type()
)
tlpAgentConfigCurrentTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAgentConfigCurrentTime.setStatus("current")
_TlpAgentContacts_ObjectIdentity = ObjectIdentity
tlpAgentContacts = _TlpAgentContacts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 3)
)
_TlpAgentEmailContacts_ObjectIdentity = ObjectIdentity
tlpAgentEmailContacts = _TlpAgentEmailContacts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 3, 1)
)
_TlpAgentNumEmailContacts_Type = Unsigned32
_TlpAgentNumEmailContacts_Object = MibScalar
tlpAgentNumEmailContacts = _TlpAgentNumEmailContacts_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 3, 1, 1),
    _TlpAgentNumEmailContacts_Type()
)
tlpAgentNumEmailContacts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentNumEmailContacts.setStatus("current")
_TlpAgentEmailContactTable_Object = MibTable
tlpAgentEmailContactTable = _TlpAgentEmailContactTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 3, 1, 2)
)
if mibBuilder.loadTexts:
    tlpAgentEmailContactTable.setStatus("current")
_TlpAgentEmailContactEntry_Object = MibTableRow
tlpAgentEmailContactEntry = _TlpAgentEmailContactEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 3, 1, 2, 1)
)
tlpAgentEmailContactEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpAgentEmailContactIndex"),
)
if mibBuilder.loadTexts:
    tlpAgentEmailContactEntry.setStatus("current")
_TlpAgentEmailContactIndex_Type = Unsigned32
_TlpAgentEmailContactIndex_Object = MibTableColumn
tlpAgentEmailContactIndex = _TlpAgentEmailContactIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 3, 1, 2, 1, 1),
    _TlpAgentEmailContactIndex_Type()
)
tlpAgentEmailContactIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentEmailContactIndex.setStatus("current")
_TlpAgentEmailContactRowStatus_Type = RowStatus
_TlpAgentEmailContactRowStatus_Object = MibTableColumn
tlpAgentEmailContactRowStatus = _TlpAgentEmailContactRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 3, 1, 2, 1, 2),
    _TlpAgentEmailContactRowStatus_Type()
)
tlpAgentEmailContactRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAgentEmailContactRowStatus.setStatus("current")
_TlpAgentEmailContactName_Type = DisplayString
_TlpAgentEmailContactName_Object = MibTableColumn
tlpAgentEmailContactName = _TlpAgentEmailContactName_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 3, 1, 2, 1, 3),
    _TlpAgentEmailContactName_Type()
)
tlpAgentEmailContactName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAgentEmailContactName.setStatus("current")
_TlpAgentEmailContactAddress_Type = DisplayString
_TlpAgentEmailContactAddress_Object = MibTableColumn
tlpAgentEmailContactAddress = _TlpAgentEmailContactAddress_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 3, 1, 2, 1, 4),
    _TlpAgentEmailContactAddress_Type()
)
tlpAgentEmailContactAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAgentEmailContactAddress.setStatus("current")
_TlpAgentEmailContactTest_Type = TruthValue
_TlpAgentEmailContactTest_Object = MibTableColumn
tlpAgentEmailContactTest = _TlpAgentEmailContactTest_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 3, 1, 2, 1, 5),
    _TlpAgentEmailContactTest_Type()
)
tlpAgentEmailContactTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAgentEmailContactTest.setStatus("current")
_TlpAgentSnmpContacts_ObjectIdentity = ObjectIdentity
tlpAgentSnmpContacts = _TlpAgentSnmpContacts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 3, 2)
)
_TlpAgentNumSnmpContacts_Type = Unsigned32
_TlpAgentNumSnmpContacts_Object = MibScalar
tlpAgentNumSnmpContacts = _TlpAgentNumSnmpContacts_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 3, 2, 1),
    _TlpAgentNumSnmpContacts_Type()
)
tlpAgentNumSnmpContacts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentNumSnmpContacts.setStatus("current")
_TlpAgentSnmpContactTable_Object = MibTable
tlpAgentSnmpContactTable = _TlpAgentSnmpContactTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 3, 2, 2)
)
if mibBuilder.loadTexts:
    tlpAgentSnmpContactTable.setStatus("current")
_TlpAgentSnmpContactEntry_Object = MibTableRow
tlpAgentSnmpContactEntry = _TlpAgentSnmpContactEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 3, 2, 2, 1)
)
tlpAgentSnmpContactEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpAgentSnmpContactIndex"),
)
if mibBuilder.loadTexts:
    tlpAgentSnmpContactEntry.setStatus("current")
_TlpAgentSnmpContactIndex_Type = Unsigned32
_TlpAgentSnmpContactIndex_Object = MibTableColumn
tlpAgentSnmpContactIndex = _TlpAgentSnmpContactIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 3, 2, 2, 1, 1),
    _TlpAgentSnmpContactIndex_Type()
)
tlpAgentSnmpContactIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentSnmpContactIndex.setStatus("current")
_TlpAgentSnmpContactRowStatus_Type = RowStatus
_TlpAgentSnmpContactRowStatus_Object = MibTableColumn
tlpAgentSnmpContactRowStatus = _TlpAgentSnmpContactRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 3, 2, 2, 1, 2),
    _TlpAgentSnmpContactRowStatus_Type()
)
tlpAgentSnmpContactRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAgentSnmpContactRowStatus.setStatus("current")
_TlpAgentSnmpContactName_Type = DisplayString
_TlpAgentSnmpContactName_Object = MibTableColumn
tlpAgentSnmpContactName = _TlpAgentSnmpContactName_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 3, 2, 2, 1, 3),
    _TlpAgentSnmpContactName_Type()
)
tlpAgentSnmpContactName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAgentSnmpContactName.setStatus("current")
_TlpAgentSnmpContactIpAddress_Type = DisplayString
_TlpAgentSnmpContactIpAddress_Object = MibTableColumn
tlpAgentSnmpContactIpAddress = _TlpAgentSnmpContactIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 3, 2, 2, 1, 4),
    _TlpAgentSnmpContactIpAddress_Type()
)
tlpAgentSnmpContactIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAgentSnmpContactIpAddress.setStatus("current")
_TlpAgentSnmpContactTrapPort_Type = Unsigned32
_TlpAgentSnmpContactTrapPort_Object = MibTableColumn
tlpAgentSnmpContactTrapPort = _TlpAgentSnmpContactTrapPort_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 3, 2, 2, 1, 5),
    _TlpAgentSnmpContactTrapPort_Type()
)
tlpAgentSnmpContactTrapPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAgentSnmpContactTrapPort.setStatus("current")


class _TlpAgentSnmpContactSnmpVersion_Type(Integer32):
    """Custom type tlpAgentSnmpContactSnmpVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("snmpv1", 1),
          ("snmpv2c", 2),
          ("snmpv3", 3))
    )


_TlpAgentSnmpContactSnmpVersion_Type.__name__ = "Integer32"
_TlpAgentSnmpContactSnmpVersion_Object = MibTableColumn
tlpAgentSnmpContactSnmpVersion = _TlpAgentSnmpContactSnmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 3, 2, 2, 1, 6),
    _TlpAgentSnmpContactSnmpVersion_Type()
)
tlpAgentSnmpContactSnmpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAgentSnmpContactSnmpVersion.setStatus("current")
_TlpAgentSnmpContactSecurityName_Type = DisplayString
_TlpAgentSnmpContactSecurityName_Object = MibTableColumn
tlpAgentSnmpContactSecurityName = _TlpAgentSnmpContactSecurityName_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 3, 2, 2, 1, 7),
    _TlpAgentSnmpContactSecurityName_Type()
)
tlpAgentSnmpContactSecurityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAgentSnmpContactSecurityName.setStatus("deprecated")
_TlpAgentSnmpContactPrivPassword_Type = DisplayString
_TlpAgentSnmpContactPrivPassword_Object = MibTableColumn
tlpAgentSnmpContactPrivPassword = _TlpAgentSnmpContactPrivPassword_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 3, 2, 2, 1, 8),
    _TlpAgentSnmpContactPrivPassword_Type()
)
tlpAgentSnmpContactPrivPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAgentSnmpContactPrivPassword.setStatus("obsolete")
_TlpAgentSnmpContactAuthPassword_Type = DisplayString
_TlpAgentSnmpContactAuthPassword_Object = MibTableColumn
tlpAgentSnmpContactAuthPassword = _TlpAgentSnmpContactAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 3, 2, 2, 1, 9),
    _TlpAgentSnmpContactAuthPassword_Type()
)
tlpAgentSnmpContactAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAgentSnmpContactAuthPassword.setStatus("obsolete")


class _TlpAgentSnmpContactTrapType_Type(Integer32):
    """Custom type tlpAgentSnmpContactTrapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("trap", 0),
          ("inform", 1))
    )


_TlpAgentSnmpContactTrapType_Type.__name__ = "Integer32"
_TlpAgentSnmpContactTrapType_Object = MibTableColumn
tlpAgentSnmpContactTrapType = _TlpAgentSnmpContactTrapType_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 3, 2, 2, 1, 10),
    _TlpAgentSnmpContactTrapType_Type()
)
tlpAgentSnmpContactTrapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAgentSnmpContactTrapType.setStatus("current")
_TlpAgentSnmpContactSetPort_Type = Unsigned32
_TlpAgentSnmpContactSetPort_Object = MibTableColumn
tlpAgentSnmpContactSetPort = _TlpAgentSnmpContactSetPort_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 3, 2, 2, 1, 11),
    _TlpAgentSnmpContactSetPort_Type()
)
tlpAgentSnmpContactSetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAgentSnmpContactSetPort.setStatus("current")
_TlpAgentSnmpContactSupportsTrap_Type = TruthValue
_TlpAgentSnmpContactSupportsTrap_Object = MibTableColumn
tlpAgentSnmpContactSupportsTrap = _TlpAgentSnmpContactSupportsTrap_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 3, 2, 2, 1, 12),
    _TlpAgentSnmpContactSupportsTrap_Type()
)
tlpAgentSnmpContactSupportsTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAgentSnmpContactSupportsTrap.setStatus("current")
_TlpAgentSnmpContactSupportsSet_Type = TruthValue
_TlpAgentSnmpContactSupportsSet_Object = MibTableColumn
tlpAgentSnmpContactSupportsSet = _TlpAgentSnmpContactSupportsSet_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 3, 2, 2, 1, 13),
    _TlpAgentSnmpContactSupportsSet_Type()
)
tlpAgentSnmpContactSupportsSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAgentSnmpContactSupportsSet.setStatus("current")
_TlpAgentSnmpContactTestTrap_Type = TruthValue
_TlpAgentSnmpContactTestTrap_Object = MibTableColumn
tlpAgentSnmpContactTestTrap = _TlpAgentSnmpContactTestTrap_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 3, 2, 2, 1, 14),
    _TlpAgentSnmpContactTestTrap_Type()
)
tlpAgentSnmpContactTestTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAgentSnmpContactTestTrap.setStatus("current")
_TlpAgentSmsContacts_ObjectIdentity = ObjectIdentity
tlpAgentSmsContacts = _TlpAgentSmsContacts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 3, 3)
)
_TlpAgentSmsNumSmsContacts_Type = Unsigned32
_TlpAgentSmsNumSmsContacts_Object = MibScalar
tlpAgentSmsNumSmsContacts = _TlpAgentSmsNumSmsContacts_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 3, 3, 1),
    _TlpAgentSmsNumSmsContacts_Type()
)
tlpAgentSmsNumSmsContacts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentSmsNumSmsContacts.setStatus("current")
_TlpAgentSmsContactTable_Object = MibTable
tlpAgentSmsContactTable = _TlpAgentSmsContactTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 3, 3, 2)
)
if mibBuilder.loadTexts:
    tlpAgentSmsContactTable.setStatus("current")
_TlpAgentSmsContactEntry_Object = MibTableRow
tlpAgentSmsContactEntry = _TlpAgentSmsContactEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 3, 3, 2, 1)
)
tlpAgentSmsContactEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpAgentSmsContactIndex"),
)
if mibBuilder.loadTexts:
    tlpAgentSmsContactEntry.setStatus("current")
_TlpAgentSmsContactIndex_Type = Unsigned32
_TlpAgentSmsContactIndex_Object = MibTableColumn
tlpAgentSmsContactIndex = _TlpAgentSmsContactIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 3, 3, 2, 1, 1),
    _TlpAgentSmsContactIndex_Type()
)
tlpAgentSmsContactIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentSmsContactIndex.setStatus("current")
_TlpAgentSmsContactRowStatus_Type = RowStatus
_TlpAgentSmsContactRowStatus_Object = MibTableColumn
tlpAgentSmsContactRowStatus = _TlpAgentSmsContactRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 3, 3, 2, 1, 2),
    _TlpAgentSmsContactRowStatus_Type()
)
tlpAgentSmsContactRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAgentSmsContactRowStatus.setStatus("current")
_TlpAgentSmsContactName_Type = DisplayString
_TlpAgentSmsContactName_Object = MibTableColumn
tlpAgentSmsContactName = _TlpAgentSmsContactName_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 3, 3, 2, 1, 3),
    _TlpAgentSmsContactName_Type()
)
tlpAgentSmsContactName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAgentSmsContactName.setStatus("current")
_TlpAgentSmsContactNumber_Type = DisplayString
_TlpAgentSmsContactNumber_Object = MibTableColumn
tlpAgentSmsContactNumber = _TlpAgentSmsContactNumber_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 3, 3, 2, 1, 4),
    _TlpAgentSmsContactNumber_Type()
)
tlpAgentSmsContactNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAgentSmsContactNumber.setStatus("current")
_TlpAgentSmsContactTest_Type = TruthValue
_TlpAgentSmsContactTest_Object = MibTableColumn
tlpAgentSmsContactTest = _TlpAgentSmsContactTest_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 3, 3, 2, 1, 5),
    _TlpAgentSmsContactTest_Type()
)
tlpAgentSmsContactTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAgentSmsContactTest.setStatus("current")
_TlpAgentAutoProbe_ObjectIdentity = ObjectIdentity
tlpAgentAutoProbe = _TlpAgentAutoProbe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 4)
)
_TlpAgentAutoProbeNumProbes_Type = Unsigned32
_TlpAgentAutoProbeNumProbes_Object = MibScalar
tlpAgentAutoProbeNumProbes = _TlpAgentAutoProbeNumProbes_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 4, 1),
    _TlpAgentAutoProbeNumProbes_Type()
)
tlpAgentAutoProbeNumProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAutoProbeNumProbes.setStatus("current")
_TlpAgentAutoProbeTable_Object = MibTable
tlpAgentAutoProbeTable = _TlpAgentAutoProbeTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 4, 2)
)
if mibBuilder.loadTexts:
    tlpAgentAutoProbeTable.setStatus("current")
_TlpAgentAutoProbeEntry_Object = MibTableRow
tlpAgentAutoProbeEntry = _TlpAgentAutoProbeEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 4, 2, 1)
)
tlpAgentAutoProbeEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpAgentAutoProbeIndex"),
)
if mibBuilder.loadTexts:
    tlpAgentAutoProbeEntry.setStatus("current")
_TlpAgentAutoProbeIndex_Type = Unsigned32
_TlpAgentAutoProbeIndex_Object = MibTableColumn
tlpAgentAutoProbeIndex = _TlpAgentAutoProbeIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 4, 2, 1, 1),
    _TlpAgentAutoProbeIndex_Type()
)
tlpAgentAutoProbeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAutoProbeIndex.setStatus("current")
_TlpAgentAutoProbeRowStatus_Type = RowStatus
_TlpAgentAutoProbeRowStatus_Object = MibTableColumn
tlpAgentAutoProbeRowStatus = _TlpAgentAutoProbeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 4, 2, 1, 2),
    _TlpAgentAutoProbeRowStatus_Type()
)
tlpAgentAutoProbeRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAutoProbeRowStatus.setStatus("current")
_TlpAgentAutoProbeName_Type = DisplayString
_TlpAgentAutoProbeName_Object = MibTableColumn
tlpAgentAutoProbeName = _TlpAgentAutoProbeName_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 4, 2, 1, 3),
    _TlpAgentAutoProbeName_Type()
)
tlpAgentAutoProbeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAutoProbeName.setStatus("current")
_TlpAgentAutoProbeDescription_Type = DisplayString
_TlpAgentAutoProbeDescription_Object = MibTableColumn
tlpAgentAutoProbeDescription = _TlpAgentAutoProbeDescription_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 4, 2, 1, 4),
    _TlpAgentAutoProbeDescription_Type()
)
tlpAgentAutoProbeDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAutoProbeDescription.setStatus("current")


class _TlpAgentAutoProbeType_Type(Integer32):
    """Custom type tlpAgentAutoProbeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ntp", 1),
          ("ping", 2),
          ("snmp", 3),
          ("http", 4),
          ("https", 5))
    )


_TlpAgentAutoProbeType_Type.__name__ = "Integer32"
_TlpAgentAutoProbeType_Object = MibTableColumn
tlpAgentAutoProbeType = _TlpAgentAutoProbeType_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 4, 2, 1, 5),
    _TlpAgentAutoProbeType_Type()
)
tlpAgentAutoProbeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAutoProbeType.setStatus("current")


class _TlpAgentAutoProbeStatus_Type(Integer32):
    """Custom type tlpAgentAutoProbeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unspecified", 0),
          ("unknown", 1),
          ("ok", 2),
          ("failed", 3),
          ("initFailed", 4))
    )


_TlpAgentAutoProbeStatus_Type.__name__ = "Integer32"
_TlpAgentAutoProbeStatus_Object = MibTableColumn
tlpAgentAutoProbeStatus = _TlpAgentAutoProbeStatus_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 4, 2, 1, 6),
    _TlpAgentAutoProbeStatus_Type()
)
tlpAgentAutoProbeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAutoProbeStatus.setStatus("current")
_TlpAgentAutoProbeInterval_Type = Unsigned32
_TlpAgentAutoProbeInterval_Object = MibTableColumn
tlpAgentAutoProbeInterval = _TlpAgentAutoProbeInterval_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 4, 2, 1, 7),
    _TlpAgentAutoProbeInterval_Type()
)
tlpAgentAutoProbeInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAutoProbeInterval.setStatus("current")
_TlpAgentAutoProbeRetryCount_Type = Unsigned32
_TlpAgentAutoProbeRetryCount_Object = MibTableColumn
tlpAgentAutoProbeRetryCount = _TlpAgentAutoProbeRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 4, 2, 1, 8),
    _TlpAgentAutoProbeRetryCount_Type()
)
tlpAgentAutoProbeRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAutoProbeRetryCount.setStatus("current")
_TlpAgentAutoProbePrimaryAddress_Type = DisplayString
_TlpAgentAutoProbePrimaryAddress_Object = MibTableColumn
tlpAgentAutoProbePrimaryAddress = _TlpAgentAutoProbePrimaryAddress_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 4, 2, 1, 9),
    _TlpAgentAutoProbePrimaryAddress_Type()
)
tlpAgentAutoProbePrimaryAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAutoProbePrimaryAddress.setStatus("current")
_TlpAgentAutoProbePrimaryPort_Type = Unsigned32
_TlpAgentAutoProbePrimaryPort_Object = MibTableColumn
tlpAgentAutoProbePrimaryPort = _TlpAgentAutoProbePrimaryPort_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 4, 2, 1, 10),
    _TlpAgentAutoProbePrimaryPort_Type()
)
tlpAgentAutoProbePrimaryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAutoProbePrimaryPort.setStatus("current")
_TlpAgentAutoProbeSecondaryAddress_Type = DisplayString
_TlpAgentAutoProbeSecondaryAddress_Object = MibTableColumn
tlpAgentAutoProbeSecondaryAddress = _TlpAgentAutoProbeSecondaryAddress_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 4, 2, 1, 11),
    _TlpAgentAutoProbeSecondaryAddress_Type()
)
tlpAgentAutoProbeSecondaryAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAutoProbeSecondaryAddress.setStatus("current")
_TlpAgentAutoProbeSecondaryPort_Type = Unsigned32
_TlpAgentAutoProbeSecondaryPort_Object = MibTableColumn
tlpAgentAutoProbeSecondaryPort = _TlpAgentAutoProbeSecondaryPort_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 4, 2, 1, 12),
    _TlpAgentAutoProbeSecondaryPort_Type()
)
tlpAgentAutoProbeSecondaryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAutoProbeSecondaryPort.setStatus("current")
_TlpAlarms_ObjectIdentity = ObjectIdentity
tlpAlarms = _TlpAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3)
)
_TlpAlarmsPresent_Type = Unsigned32
_TlpAlarmsPresent_Object = MibScalar
tlpAlarmsPresent = _TlpAlarmsPresent_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 1),
    _TlpAlarmsPresent_Type()
)
tlpAlarmsPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAlarmsPresent.setStatus("current")
_TlpAlarmTable_Object = MibTable
tlpAlarmTable = _TlpAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 2)
)
if mibBuilder.loadTexts:
    tlpAlarmTable.setStatus("current")
_TlpAlarmEntry_Object = MibTableRow
tlpAlarmEntry = _TlpAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 2, 1)
)
tlpAlarmEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpAlarmId"),
)
if mibBuilder.loadTexts:
    tlpAlarmEntry.setStatus("current")
_TlpAlarmId_Type = Unsigned32
_TlpAlarmId_Object = MibTableColumn
tlpAlarmId = _TlpAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 2, 1, 1),
    _TlpAlarmId_Type()
)
tlpAlarmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAlarmId.setStatus("current")
_TlpAlarmDescr_Type = ObjectIdentifier
_TlpAlarmDescr_Object = MibTableColumn
tlpAlarmDescr = _TlpAlarmDescr_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 2, 1, 2),
    _TlpAlarmDescr_Type()
)
tlpAlarmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAlarmDescr.setStatus("current")
_TlpAlarmTime_Type = TimeStamp
_TlpAlarmTime_Object = MibTableColumn
tlpAlarmTime = _TlpAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 2, 1, 3),
    _TlpAlarmTime_Type()
)
tlpAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAlarmTime.setStatus("current")
_TlpAlarmTableRef_Type = ObjectIdentifier
_TlpAlarmTableRef_Object = MibTableColumn
tlpAlarmTableRef = _TlpAlarmTableRef_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 2, 1, 4),
    _TlpAlarmTableRef_Type()
)
tlpAlarmTableRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAlarmTableRef.setStatus("current")
_TlpAlarmTableRowRef_Type = ObjectIdentifier
_TlpAlarmTableRowRef_Object = MibTableColumn
tlpAlarmTableRowRef = _TlpAlarmTableRowRef_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 2, 1, 5),
    _TlpAlarmTableRowRef_Type()
)
tlpAlarmTableRowRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAlarmTableRowRef.setStatus("current")
_TlpAlarmDetail_Type = DisplayString
_TlpAlarmDetail_Object = MibTableColumn
tlpAlarmDetail = _TlpAlarmDetail_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 2, 1, 6),
    _TlpAlarmDetail_Type()
)
tlpAlarmDetail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAlarmDetail.setStatus("current")


class _TlpAlarmType_Type(Integer32):
    """Custom type tlpAlarmType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("warning", 2),
          ("info", 3),
          ("status", 4),
          ("offline", 5),
          ("custom", 6))
    )


_TlpAlarmType_Type.__name__ = "Integer32"
_TlpAlarmType_Object = MibTableColumn
tlpAlarmType = _TlpAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 2, 1, 7),
    _TlpAlarmType_Type()
)
tlpAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAlarmType.setStatus("deprecated")


class _TlpAlarmState_Type(Integer32):
    """Custom type tlpAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_TlpAlarmState_Type.__name__ = "Integer32"
_TlpAlarmState_Object = MibTableColumn
tlpAlarmState = _TlpAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 2, 1, 8),
    _TlpAlarmState_Type()
)
tlpAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAlarmState.setStatus("current")


class _TlpAlarmAcknowledged_Type(Integer32):
    """Custom type tlpAlarmAcknowledged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notAcknowledged", 1),
          ("acknowledged", 2))
    )


_TlpAlarmAcknowledged_Type.__name__ = "Integer32"
_TlpAlarmAcknowledged_Object = MibTableColumn
tlpAlarmAcknowledged = _TlpAlarmAcknowledged_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 2, 1, 9),
    _TlpAlarmAcknowledged_Type()
)
tlpAlarmAcknowledged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAlarmAcknowledged.setStatus("current")


class _TlpAlarmSeverity_Type(Integer32):
    """Custom type tlpAlarmSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("emergency", 0),
          ("alert", 1),
          ("critical", 2),
          ("error", 3),
          ("warning", 4),
          ("notice", 5),
          ("information", 6))
    )


_TlpAlarmSeverity_Type.__name__ = "Integer32"
_TlpAlarmSeverity_Object = MibTableColumn
tlpAlarmSeverity = _TlpAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 2, 1, 10),
    _TlpAlarmSeverity_Type()
)
tlpAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAlarmSeverity.setStatus("current")
_TlpAlarmsWellKnown_ObjectIdentity = ObjectIdentity
tlpAlarmsWellKnown = _TlpAlarmsWellKnown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3)
)
_TlpAgentAlarms_ObjectIdentity = ObjectIdentity
tlpAgentAlarms = _TlpAgentAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1)
)
_TlpAutoProbeAlarms_ObjectIdentity = ObjectIdentity
tlpAutoProbeAlarms = _TlpAutoProbeAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 1)
)
_TlpAutoProbeAlarm01_ObjectIdentity = ObjectIdentity
tlpAutoProbeAlarm01 = _TlpAutoProbeAlarm01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tlpAutoProbeAlarm01.setStatus("current")
_TlpAutoProbeAlarm02_ObjectIdentity = ObjectIdentity
tlpAutoProbeAlarm02 = _TlpAutoProbeAlarm02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    tlpAutoProbeAlarm02.setStatus("current")
_TlpAutoProbeAlarm03_ObjectIdentity = ObjectIdentity
tlpAutoProbeAlarm03 = _TlpAutoProbeAlarm03_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 1, 3)
)
if mibBuilder.loadTexts:
    tlpAutoProbeAlarm03.setStatus("current")
_TlpAutoProbeAlarm04_ObjectIdentity = ObjectIdentity
tlpAutoProbeAlarm04 = _TlpAutoProbeAlarm04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 1, 4)
)
if mibBuilder.loadTexts:
    tlpAutoProbeAlarm04.setStatus("current")
_TlpAutoProbeAlarm05_ObjectIdentity = ObjectIdentity
tlpAutoProbeAlarm05 = _TlpAutoProbeAlarm05_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 1, 5)
)
if mibBuilder.loadTexts:
    tlpAutoProbeAlarm05.setStatus("current")
_TlpAutoProbeAlarm06_ObjectIdentity = ObjectIdentity
tlpAutoProbeAlarm06 = _TlpAutoProbeAlarm06_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 1, 6)
)
if mibBuilder.loadTexts:
    tlpAutoProbeAlarm06.setStatus("current")
_TlpAutoProbeAlarm07_ObjectIdentity = ObjectIdentity
tlpAutoProbeAlarm07 = _TlpAutoProbeAlarm07_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 1, 7)
)
if mibBuilder.loadTexts:
    tlpAutoProbeAlarm07.setStatus("current")
_TlpAutoProbeAlarm08_ObjectIdentity = ObjectIdentity
tlpAutoProbeAlarm08 = _TlpAutoProbeAlarm08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 1, 8)
)
if mibBuilder.loadTexts:
    tlpAutoProbeAlarm08.setStatus("current")
_TlpAutoProbeAlarm09_ObjectIdentity = ObjectIdentity
tlpAutoProbeAlarm09 = _TlpAutoProbeAlarm09_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 1, 9)
)
if mibBuilder.loadTexts:
    tlpAutoProbeAlarm09.setStatus("current")
_TlpAutoProbeAlarm10_ObjectIdentity = ObjectIdentity
tlpAutoProbeAlarm10 = _TlpAutoProbeAlarm10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 1, 10)
)
if mibBuilder.loadTexts:
    tlpAutoProbeAlarm10.setStatus("current")
_TlpAutoProbeAlarm11_ObjectIdentity = ObjectIdentity
tlpAutoProbeAlarm11 = _TlpAutoProbeAlarm11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 1, 11)
)
if mibBuilder.loadTexts:
    tlpAutoProbeAlarm11.setStatus("current")
_TlpAutoProbeAlarm12_ObjectIdentity = ObjectIdentity
tlpAutoProbeAlarm12 = _TlpAutoProbeAlarm12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 1, 12)
)
if mibBuilder.loadTexts:
    tlpAutoProbeAlarm12.setStatus("current")
_TlpAutoProbeAlarm13_ObjectIdentity = ObjectIdentity
tlpAutoProbeAlarm13 = _TlpAutoProbeAlarm13_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 1, 13)
)
if mibBuilder.loadTexts:
    tlpAutoProbeAlarm13.setStatus("current")
_TlpAutoProbeAlarm14_ObjectIdentity = ObjectIdentity
tlpAutoProbeAlarm14 = _TlpAutoProbeAlarm14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 1, 14)
)
if mibBuilder.loadTexts:
    tlpAutoProbeAlarm14.setStatus("current")
_TlpAutoProbeAlarm15_ObjectIdentity = ObjectIdentity
tlpAutoProbeAlarm15 = _TlpAutoProbeAlarm15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 1, 15)
)
if mibBuilder.loadTexts:
    tlpAutoProbeAlarm15.setStatus("current")
_TlpAutoProbeAlarm16_ObjectIdentity = ObjectIdentity
tlpAutoProbeAlarm16 = _TlpAutoProbeAlarm16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 1, 16)
)
if mibBuilder.loadTexts:
    tlpAutoProbeAlarm16.setStatus("current")
_TlpAutoProbeAlarm17_ObjectIdentity = ObjectIdentity
tlpAutoProbeAlarm17 = _TlpAutoProbeAlarm17_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 1, 17)
)
if mibBuilder.loadTexts:
    tlpAutoProbeAlarm17.setStatus("current")
_TlpAutoProbeAlarm18_ObjectIdentity = ObjectIdentity
tlpAutoProbeAlarm18 = _TlpAutoProbeAlarm18_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 1, 18)
)
if mibBuilder.loadTexts:
    tlpAutoProbeAlarm18.setStatus("current")
_TlpAutoProbeAlarm19_ObjectIdentity = ObjectIdentity
tlpAutoProbeAlarm19 = _TlpAutoProbeAlarm19_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 1, 19)
)
if mibBuilder.loadTexts:
    tlpAutoProbeAlarm19.setStatus("current")
_TlpAutoProbeAlarm20_ObjectIdentity = ObjectIdentity
tlpAutoProbeAlarm20 = _TlpAutoProbeAlarm20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 1, 20)
)
if mibBuilder.loadTexts:
    tlpAutoProbeAlarm20.setStatus("current")
_TlpAutoProbeAlarm21_ObjectIdentity = ObjectIdentity
tlpAutoProbeAlarm21 = _TlpAutoProbeAlarm21_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 1, 21)
)
if mibBuilder.loadTexts:
    tlpAutoProbeAlarm21.setStatus("current")
_TlpAutoProbeAlarm22_ObjectIdentity = ObjectIdentity
tlpAutoProbeAlarm22 = _TlpAutoProbeAlarm22_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 1, 22)
)
if mibBuilder.loadTexts:
    tlpAutoProbeAlarm22.setStatus("current")
_TlpAutoProbeAlarm23_ObjectIdentity = ObjectIdentity
tlpAutoProbeAlarm23 = _TlpAutoProbeAlarm23_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 1, 23)
)
if mibBuilder.loadTexts:
    tlpAutoProbeAlarm23.setStatus("current")
_TlpAutoProbeAlarm24_ObjectIdentity = ObjectIdentity
tlpAutoProbeAlarm24 = _TlpAutoProbeAlarm24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 1, 24)
)
if mibBuilder.loadTexts:
    tlpAutoProbeAlarm24.setStatus("current")
_TlpAutoProbeAlarm25_ObjectIdentity = ObjectIdentity
tlpAutoProbeAlarm25 = _TlpAutoProbeAlarm25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 1, 25)
)
if mibBuilder.loadTexts:
    tlpAutoProbeAlarm25.setStatus("current")
_TlpAutoProbeAlarm26_ObjectIdentity = ObjectIdentity
tlpAutoProbeAlarm26 = _TlpAutoProbeAlarm26_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 1, 26)
)
if mibBuilder.loadTexts:
    tlpAutoProbeAlarm26.setStatus("current")
_TlpAutoProbeAlarm27_ObjectIdentity = ObjectIdentity
tlpAutoProbeAlarm27 = _TlpAutoProbeAlarm27_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 1, 27)
)
if mibBuilder.loadTexts:
    tlpAutoProbeAlarm27.setStatus("current")
_TlpAutoProbeAlarm28_ObjectIdentity = ObjectIdentity
tlpAutoProbeAlarm28 = _TlpAutoProbeAlarm28_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 1, 28)
)
if mibBuilder.loadTexts:
    tlpAutoProbeAlarm28.setStatus("current")
_TlpAutoProbeAlarm29_ObjectIdentity = ObjectIdentity
tlpAutoProbeAlarm29 = _TlpAutoProbeAlarm29_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 1, 29)
)
if mibBuilder.loadTexts:
    tlpAutoProbeAlarm29.setStatus("current")
_TlpAutoProbeAlarm30_ObjectIdentity = ObjectIdentity
tlpAutoProbeAlarm30 = _TlpAutoProbeAlarm30_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 1, 30)
)
if mibBuilder.loadTexts:
    tlpAutoProbeAlarm30.setStatus("current")
_TlpAutoProbeAlarm31_ObjectIdentity = ObjectIdentity
tlpAutoProbeAlarm31 = _TlpAutoProbeAlarm31_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 1, 31)
)
if mibBuilder.loadTexts:
    tlpAutoProbeAlarm31.setStatus("current")
_TlpAutoProbeAlarm32_ObjectIdentity = ObjectIdentity
tlpAutoProbeAlarm32 = _TlpAutoProbeAlarm32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 1, 32)
)
if mibBuilder.loadTexts:
    tlpAutoProbeAlarm32.setStatus("current")
_TlpAutoProbeAlarm33_ObjectIdentity = ObjectIdentity
tlpAutoProbeAlarm33 = _TlpAutoProbeAlarm33_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 1, 33)
)
if mibBuilder.loadTexts:
    tlpAutoProbeAlarm33.setStatus("current")
_TlpAutoProbeAlarm34_ObjectIdentity = ObjectIdentity
tlpAutoProbeAlarm34 = _TlpAutoProbeAlarm34_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 1, 34)
)
if mibBuilder.loadTexts:
    tlpAutoProbeAlarm34.setStatus("current")
_TlpAutoProbeAlarm35_ObjectIdentity = ObjectIdentity
tlpAutoProbeAlarm35 = _TlpAutoProbeAlarm35_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 1, 35)
)
if mibBuilder.loadTexts:
    tlpAutoProbeAlarm35.setStatus("current")
_TlpAutoProbeAlarm36_ObjectIdentity = ObjectIdentity
tlpAutoProbeAlarm36 = _TlpAutoProbeAlarm36_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 1, 36)
)
if mibBuilder.loadTexts:
    tlpAutoProbeAlarm36.setStatus("current")
_TlpAutoProbeAlarm37_ObjectIdentity = ObjectIdentity
tlpAutoProbeAlarm37 = _TlpAutoProbeAlarm37_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 1, 37)
)
if mibBuilder.loadTexts:
    tlpAutoProbeAlarm37.setStatus("current")
_TlpAutoProbeAlarm38_ObjectIdentity = ObjectIdentity
tlpAutoProbeAlarm38 = _TlpAutoProbeAlarm38_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 1, 38)
)
if mibBuilder.loadTexts:
    tlpAutoProbeAlarm38.setStatus("current")
_TlpAutoProbeAlarm39_ObjectIdentity = ObjectIdentity
tlpAutoProbeAlarm39 = _TlpAutoProbeAlarm39_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 1, 39)
)
if mibBuilder.loadTexts:
    tlpAutoProbeAlarm39.setStatus("current")
_TlpAutoProbeAlarm40_ObjectIdentity = ObjectIdentity
tlpAutoProbeAlarm40 = _TlpAutoProbeAlarm40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 1, 40)
)
if mibBuilder.loadTexts:
    tlpAutoProbeAlarm40.setStatus("current")
_TlpAutoProbeAlarm41_ObjectIdentity = ObjectIdentity
tlpAutoProbeAlarm41 = _TlpAutoProbeAlarm41_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 1, 41)
)
if mibBuilder.loadTexts:
    tlpAutoProbeAlarm41.setStatus("current")
_TlpAutoProbeAlarm42_ObjectIdentity = ObjectIdentity
tlpAutoProbeAlarm42 = _TlpAutoProbeAlarm42_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 1, 42)
)
if mibBuilder.loadTexts:
    tlpAutoProbeAlarm42.setStatus("current")
_TlpAutoProbeAlarm43_ObjectIdentity = ObjectIdentity
tlpAutoProbeAlarm43 = _TlpAutoProbeAlarm43_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 1, 43)
)
if mibBuilder.loadTexts:
    tlpAutoProbeAlarm43.setStatus("current")
_TlpAutoProbeAlarm44_ObjectIdentity = ObjectIdentity
tlpAutoProbeAlarm44 = _TlpAutoProbeAlarm44_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 1, 44)
)
if mibBuilder.loadTexts:
    tlpAutoProbeAlarm44.setStatus("current")
_TlpAutoProbeAlarm45_ObjectIdentity = ObjectIdentity
tlpAutoProbeAlarm45 = _TlpAutoProbeAlarm45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 1, 45)
)
if mibBuilder.loadTexts:
    tlpAutoProbeAlarm45.setStatus("current")
_TlpAutoProbeAlarm46_ObjectIdentity = ObjectIdentity
tlpAutoProbeAlarm46 = _TlpAutoProbeAlarm46_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 1, 46)
)
if mibBuilder.loadTexts:
    tlpAutoProbeAlarm46.setStatus("current")
_TlpAutoProbeAlarm47_ObjectIdentity = ObjectIdentity
tlpAutoProbeAlarm47 = _TlpAutoProbeAlarm47_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 1, 47)
)
if mibBuilder.loadTexts:
    tlpAutoProbeAlarm47.setStatus("current")
_TlpAutoProbeAlarm48_ObjectIdentity = ObjectIdentity
tlpAutoProbeAlarm48 = _TlpAutoProbeAlarm48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 1, 48)
)
if mibBuilder.loadTexts:
    tlpAutoProbeAlarm48.setStatus("current")
_TlpAutoProbeAlarm49_ObjectIdentity = ObjectIdentity
tlpAutoProbeAlarm49 = _TlpAutoProbeAlarm49_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 1, 49)
)
if mibBuilder.loadTexts:
    tlpAutoProbeAlarm49.setStatus("current")
_TlpAutoProbeAlarm50_ObjectIdentity = ObjectIdentity
tlpAutoProbeAlarm50 = _TlpAutoProbeAlarm50_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 1, 50)
)
if mibBuilder.loadTexts:
    tlpAutoProbeAlarm50.setStatus("current")
_TlpAutoProbeAlarm51_ObjectIdentity = ObjectIdentity
tlpAutoProbeAlarm51 = _TlpAutoProbeAlarm51_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 1, 51)
)
if mibBuilder.loadTexts:
    tlpAutoProbeAlarm51.setStatus("current")
_TlpAutoProbeAlarm52_ObjectIdentity = ObjectIdentity
tlpAutoProbeAlarm52 = _TlpAutoProbeAlarm52_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 1, 52)
)
if mibBuilder.loadTexts:
    tlpAutoProbeAlarm52.setStatus("current")
_TlpAutoProbeAlarm53_ObjectIdentity = ObjectIdentity
tlpAutoProbeAlarm53 = _TlpAutoProbeAlarm53_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 1, 53)
)
if mibBuilder.loadTexts:
    tlpAutoProbeAlarm53.setStatus("current")
_TlpAutoProbeAlarm54_ObjectIdentity = ObjectIdentity
tlpAutoProbeAlarm54 = _TlpAutoProbeAlarm54_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 1, 54)
)
if mibBuilder.loadTexts:
    tlpAutoProbeAlarm54.setStatus("current")
_TlpAutoProbeAlarm55_ObjectIdentity = ObjectIdentity
tlpAutoProbeAlarm55 = _TlpAutoProbeAlarm55_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 1, 55)
)
if mibBuilder.loadTexts:
    tlpAutoProbeAlarm55.setStatus("current")
_TlpAutoProbeAlarm56_ObjectIdentity = ObjectIdentity
tlpAutoProbeAlarm56 = _TlpAutoProbeAlarm56_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 1, 56)
)
if mibBuilder.loadTexts:
    tlpAutoProbeAlarm56.setStatus("current")
_TlpAutoProbeAlarm57_ObjectIdentity = ObjectIdentity
tlpAutoProbeAlarm57 = _TlpAutoProbeAlarm57_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 1, 57)
)
if mibBuilder.loadTexts:
    tlpAutoProbeAlarm57.setStatus("current")
_TlpAutoProbeAlarm58_ObjectIdentity = ObjectIdentity
tlpAutoProbeAlarm58 = _TlpAutoProbeAlarm58_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 1, 58)
)
if mibBuilder.loadTexts:
    tlpAutoProbeAlarm58.setStatus("current")
_TlpAutoProbeAlarm59_ObjectIdentity = ObjectIdentity
tlpAutoProbeAlarm59 = _TlpAutoProbeAlarm59_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 1, 59)
)
if mibBuilder.loadTexts:
    tlpAutoProbeAlarm59.setStatus("current")
_TlpAutoProbeAlarm60_ObjectIdentity = ObjectIdentity
tlpAutoProbeAlarm60 = _TlpAutoProbeAlarm60_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 1, 60)
)
if mibBuilder.loadTexts:
    tlpAutoProbeAlarm60.setStatus("current")
_TlpAutoProbeAlarm61_ObjectIdentity = ObjectIdentity
tlpAutoProbeAlarm61 = _TlpAutoProbeAlarm61_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 1, 61)
)
if mibBuilder.loadTexts:
    tlpAutoProbeAlarm61.setStatus("current")
_TlpAutoProbeAlarm62_ObjectIdentity = ObjectIdentity
tlpAutoProbeAlarm62 = _TlpAutoProbeAlarm62_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 1, 62)
)
if mibBuilder.loadTexts:
    tlpAutoProbeAlarm62.setStatus("current")
_TlpAutoProbeAlarm63_ObjectIdentity = ObjectIdentity
tlpAutoProbeAlarm63 = _TlpAutoProbeAlarm63_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 1, 63)
)
if mibBuilder.loadTexts:
    tlpAutoProbeAlarm63.setStatus("current")
_TlpAutoProbeAlarm64_ObjectIdentity = ObjectIdentity
tlpAutoProbeAlarm64 = _TlpAutoProbeAlarm64_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 1, 64)
)
if mibBuilder.loadTexts:
    tlpAutoProbeAlarm64.setStatus("current")
_TlpAutoProbeUserDefinedAlarms_ObjectIdentity = ObjectIdentity
tlpAutoProbeUserDefinedAlarms = _TlpAutoProbeUserDefinedAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 2)
)
_TlpAutoProbeUserDefinedAlarm01_ObjectIdentity = ObjectIdentity
tlpAutoProbeUserDefinedAlarm01 = _TlpAutoProbeUserDefinedAlarm01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tlpAutoProbeUserDefinedAlarm01.setStatus("current")
_TlpAutoProbeUserDefinedAlarm02_ObjectIdentity = ObjectIdentity
tlpAutoProbeUserDefinedAlarm02 = _TlpAutoProbeUserDefinedAlarm02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 2, 2)
)
if mibBuilder.loadTexts:
    tlpAutoProbeUserDefinedAlarm02.setStatus("current")
_TlpAutoProbeUserDefinedAlarm03_ObjectIdentity = ObjectIdentity
tlpAutoProbeUserDefinedAlarm03 = _TlpAutoProbeUserDefinedAlarm03_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 2, 3)
)
if mibBuilder.loadTexts:
    tlpAutoProbeUserDefinedAlarm03.setStatus("current")
_TlpAutoProbeUserDefinedAlarm04_ObjectIdentity = ObjectIdentity
tlpAutoProbeUserDefinedAlarm04 = _TlpAutoProbeUserDefinedAlarm04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 2, 4)
)
if mibBuilder.loadTexts:
    tlpAutoProbeUserDefinedAlarm04.setStatus("current")
_TlpAutoProbeUserDefinedAlarm05_ObjectIdentity = ObjectIdentity
tlpAutoProbeUserDefinedAlarm05 = _TlpAutoProbeUserDefinedAlarm05_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 2, 5)
)
if mibBuilder.loadTexts:
    tlpAutoProbeUserDefinedAlarm05.setStatus("current")
_TlpAutoProbeUserDefinedAlarm06_ObjectIdentity = ObjectIdentity
tlpAutoProbeUserDefinedAlarm06 = _TlpAutoProbeUserDefinedAlarm06_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 2, 6)
)
if mibBuilder.loadTexts:
    tlpAutoProbeUserDefinedAlarm06.setStatus("current")
_TlpAutoProbeUserDefinedAlarm07_ObjectIdentity = ObjectIdentity
tlpAutoProbeUserDefinedAlarm07 = _TlpAutoProbeUserDefinedAlarm07_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 2, 7)
)
if mibBuilder.loadTexts:
    tlpAutoProbeUserDefinedAlarm07.setStatus("current")
_TlpAutoProbeUserDefinedAlarm08_ObjectIdentity = ObjectIdentity
tlpAutoProbeUserDefinedAlarm08 = _TlpAutoProbeUserDefinedAlarm08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 2, 8)
)
if mibBuilder.loadTexts:
    tlpAutoProbeUserDefinedAlarm08.setStatus("current")
_TlpAutoProbeUserDefinedAlarm09_ObjectIdentity = ObjectIdentity
tlpAutoProbeUserDefinedAlarm09 = _TlpAutoProbeUserDefinedAlarm09_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 2, 9)
)
if mibBuilder.loadTexts:
    tlpAutoProbeUserDefinedAlarm09.setStatus("current")
_TlpAutoProbeUserDefinedAlarm10_ObjectIdentity = ObjectIdentity
tlpAutoProbeUserDefinedAlarm10 = _TlpAutoProbeUserDefinedAlarm10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 2, 10)
)
if mibBuilder.loadTexts:
    tlpAutoProbeUserDefinedAlarm10.setStatus("current")
_TlpAutoProbeUserDefinedAlarm11_ObjectIdentity = ObjectIdentity
tlpAutoProbeUserDefinedAlarm11 = _TlpAutoProbeUserDefinedAlarm11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 2, 11)
)
if mibBuilder.loadTexts:
    tlpAutoProbeUserDefinedAlarm11.setStatus("current")
_TlpAutoProbeUserDefinedAlarm12_ObjectIdentity = ObjectIdentity
tlpAutoProbeUserDefinedAlarm12 = _TlpAutoProbeUserDefinedAlarm12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 2, 12)
)
if mibBuilder.loadTexts:
    tlpAutoProbeUserDefinedAlarm12.setStatus("current")
_TlpAutoProbeUserDefinedAlarm13_ObjectIdentity = ObjectIdentity
tlpAutoProbeUserDefinedAlarm13 = _TlpAutoProbeUserDefinedAlarm13_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 2, 13)
)
if mibBuilder.loadTexts:
    tlpAutoProbeUserDefinedAlarm13.setStatus("current")
_TlpAutoProbeUserDefinedAlarm14_ObjectIdentity = ObjectIdentity
tlpAutoProbeUserDefinedAlarm14 = _TlpAutoProbeUserDefinedAlarm14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 2, 14)
)
if mibBuilder.loadTexts:
    tlpAutoProbeUserDefinedAlarm14.setStatus("current")
_TlpAutoProbeUserDefinedAlarm15_ObjectIdentity = ObjectIdentity
tlpAutoProbeUserDefinedAlarm15 = _TlpAutoProbeUserDefinedAlarm15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 2, 15)
)
if mibBuilder.loadTexts:
    tlpAutoProbeUserDefinedAlarm15.setStatus("current")
_TlpAutoProbeUserDefinedAlarm16_ObjectIdentity = ObjectIdentity
tlpAutoProbeUserDefinedAlarm16 = _TlpAutoProbeUserDefinedAlarm16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 2, 16)
)
if mibBuilder.loadTexts:
    tlpAutoProbeUserDefinedAlarm16.setStatus("current")
_TlpAutoProbeUserDefinedAlarm17_ObjectIdentity = ObjectIdentity
tlpAutoProbeUserDefinedAlarm17 = _TlpAutoProbeUserDefinedAlarm17_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 2, 17)
)
if mibBuilder.loadTexts:
    tlpAutoProbeUserDefinedAlarm17.setStatus("current")
_TlpAutoProbeUserDefinedAlarm18_ObjectIdentity = ObjectIdentity
tlpAutoProbeUserDefinedAlarm18 = _TlpAutoProbeUserDefinedAlarm18_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 2, 18)
)
if mibBuilder.loadTexts:
    tlpAutoProbeUserDefinedAlarm18.setStatus("current")
_TlpAutoProbeUserDefinedAlarm19_ObjectIdentity = ObjectIdentity
tlpAutoProbeUserDefinedAlarm19 = _TlpAutoProbeUserDefinedAlarm19_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 2, 19)
)
if mibBuilder.loadTexts:
    tlpAutoProbeUserDefinedAlarm19.setStatus("current")
_TlpAutoProbeUserDefinedAlarm20_ObjectIdentity = ObjectIdentity
tlpAutoProbeUserDefinedAlarm20 = _TlpAutoProbeUserDefinedAlarm20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 2, 20)
)
if mibBuilder.loadTexts:
    tlpAutoProbeUserDefinedAlarm20.setStatus("current")
_TlpAutoProbeUserDefinedAlarm21_ObjectIdentity = ObjectIdentity
tlpAutoProbeUserDefinedAlarm21 = _TlpAutoProbeUserDefinedAlarm21_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 2, 21)
)
if mibBuilder.loadTexts:
    tlpAutoProbeUserDefinedAlarm21.setStatus("current")
_TlpAutoProbeUserDefinedAlarm22_ObjectIdentity = ObjectIdentity
tlpAutoProbeUserDefinedAlarm22 = _TlpAutoProbeUserDefinedAlarm22_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 2, 22)
)
if mibBuilder.loadTexts:
    tlpAutoProbeUserDefinedAlarm22.setStatus("current")
_TlpAutoProbeUserDefinedAlarm23_ObjectIdentity = ObjectIdentity
tlpAutoProbeUserDefinedAlarm23 = _TlpAutoProbeUserDefinedAlarm23_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 2, 23)
)
if mibBuilder.loadTexts:
    tlpAutoProbeUserDefinedAlarm23.setStatus("current")
_TlpAutoProbeUserDefinedAlarm24_ObjectIdentity = ObjectIdentity
tlpAutoProbeUserDefinedAlarm24 = _TlpAutoProbeUserDefinedAlarm24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 2, 24)
)
if mibBuilder.loadTexts:
    tlpAutoProbeUserDefinedAlarm24.setStatus("current")
_TlpAutoProbeUserDefinedAlarm25_ObjectIdentity = ObjectIdentity
tlpAutoProbeUserDefinedAlarm25 = _TlpAutoProbeUserDefinedAlarm25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 2, 25)
)
if mibBuilder.loadTexts:
    tlpAutoProbeUserDefinedAlarm25.setStatus("current")
_TlpAutoProbeUserDefinedAlarm26_ObjectIdentity = ObjectIdentity
tlpAutoProbeUserDefinedAlarm26 = _TlpAutoProbeUserDefinedAlarm26_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 2, 26)
)
if mibBuilder.loadTexts:
    tlpAutoProbeUserDefinedAlarm26.setStatus("current")
_TlpAutoProbeUserDefinedAlarm27_ObjectIdentity = ObjectIdentity
tlpAutoProbeUserDefinedAlarm27 = _TlpAutoProbeUserDefinedAlarm27_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 2, 27)
)
if mibBuilder.loadTexts:
    tlpAutoProbeUserDefinedAlarm27.setStatus("current")
_TlpAutoProbeUserDefinedAlarm28_ObjectIdentity = ObjectIdentity
tlpAutoProbeUserDefinedAlarm28 = _TlpAutoProbeUserDefinedAlarm28_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 2, 28)
)
if mibBuilder.loadTexts:
    tlpAutoProbeUserDefinedAlarm28.setStatus("current")
_TlpAutoProbeUserDefinedAlarm29_ObjectIdentity = ObjectIdentity
tlpAutoProbeUserDefinedAlarm29 = _TlpAutoProbeUserDefinedAlarm29_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 2, 29)
)
if mibBuilder.loadTexts:
    tlpAutoProbeUserDefinedAlarm29.setStatus("current")
_TlpAutoProbeUserDefinedAlarm30_ObjectIdentity = ObjectIdentity
tlpAutoProbeUserDefinedAlarm30 = _TlpAutoProbeUserDefinedAlarm30_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 2, 30)
)
if mibBuilder.loadTexts:
    tlpAutoProbeUserDefinedAlarm30.setStatus("current")
_TlpAutoProbeUserDefinedAlarm31_ObjectIdentity = ObjectIdentity
tlpAutoProbeUserDefinedAlarm31 = _TlpAutoProbeUserDefinedAlarm31_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 2, 31)
)
if mibBuilder.loadTexts:
    tlpAutoProbeUserDefinedAlarm31.setStatus("current")
_TlpAutoProbeUserDefinedAlarm32_ObjectIdentity = ObjectIdentity
tlpAutoProbeUserDefinedAlarm32 = _TlpAutoProbeUserDefinedAlarm32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 2, 32)
)
if mibBuilder.loadTexts:
    tlpAutoProbeUserDefinedAlarm32.setStatus("current")
_TlpAutoProbeUserDefinedAlarm33_ObjectIdentity = ObjectIdentity
tlpAutoProbeUserDefinedAlarm33 = _TlpAutoProbeUserDefinedAlarm33_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 2, 33)
)
if mibBuilder.loadTexts:
    tlpAutoProbeUserDefinedAlarm33.setStatus("current")
_TlpAutoProbeUserDefinedAlarm34_ObjectIdentity = ObjectIdentity
tlpAutoProbeUserDefinedAlarm34 = _TlpAutoProbeUserDefinedAlarm34_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 2, 34)
)
if mibBuilder.loadTexts:
    tlpAutoProbeUserDefinedAlarm34.setStatus("current")
_TlpAutoProbeUserDefinedAlarm35_ObjectIdentity = ObjectIdentity
tlpAutoProbeUserDefinedAlarm35 = _TlpAutoProbeUserDefinedAlarm35_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 2, 35)
)
if mibBuilder.loadTexts:
    tlpAutoProbeUserDefinedAlarm35.setStatus("current")
_TlpAutoProbeUserDefinedAlarm36_ObjectIdentity = ObjectIdentity
tlpAutoProbeUserDefinedAlarm36 = _TlpAutoProbeUserDefinedAlarm36_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 2, 36)
)
if mibBuilder.loadTexts:
    tlpAutoProbeUserDefinedAlarm36.setStatus("current")
_TlpAutoProbeUserDefinedAlarm37_ObjectIdentity = ObjectIdentity
tlpAutoProbeUserDefinedAlarm37 = _TlpAutoProbeUserDefinedAlarm37_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 2, 37)
)
if mibBuilder.loadTexts:
    tlpAutoProbeUserDefinedAlarm37.setStatus("current")
_TlpAutoProbeUserDefinedAlarm38_ObjectIdentity = ObjectIdentity
tlpAutoProbeUserDefinedAlarm38 = _TlpAutoProbeUserDefinedAlarm38_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 2, 38)
)
if mibBuilder.loadTexts:
    tlpAutoProbeUserDefinedAlarm38.setStatus("current")
_TlpAutoProbeUserDefinedAlarm39_ObjectIdentity = ObjectIdentity
tlpAutoProbeUserDefinedAlarm39 = _TlpAutoProbeUserDefinedAlarm39_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 2, 39)
)
if mibBuilder.loadTexts:
    tlpAutoProbeUserDefinedAlarm39.setStatus("current")
_TlpAutoProbeUserDefinedAlarm40_ObjectIdentity = ObjectIdentity
tlpAutoProbeUserDefinedAlarm40 = _TlpAutoProbeUserDefinedAlarm40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 2, 40)
)
if mibBuilder.loadTexts:
    tlpAutoProbeUserDefinedAlarm40.setStatus("current")
_TlpAutoProbeUserDefinedAlarm41_ObjectIdentity = ObjectIdentity
tlpAutoProbeUserDefinedAlarm41 = _TlpAutoProbeUserDefinedAlarm41_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 2, 41)
)
if mibBuilder.loadTexts:
    tlpAutoProbeUserDefinedAlarm41.setStatus("current")
_TlpAutoProbeUserDefinedAlarm42_ObjectIdentity = ObjectIdentity
tlpAutoProbeUserDefinedAlarm42 = _TlpAutoProbeUserDefinedAlarm42_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 2, 42)
)
if mibBuilder.loadTexts:
    tlpAutoProbeUserDefinedAlarm42.setStatus("current")
_TlpAutoProbeUserDefinedAlarm43_ObjectIdentity = ObjectIdentity
tlpAutoProbeUserDefinedAlarm43 = _TlpAutoProbeUserDefinedAlarm43_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 2, 43)
)
if mibBuilder.loadTexts:
    tlpAutoProbeUserDefinedAlarm43.setStatus("current")
_TlpAutoProbeUserDefinedAlarm44_ObjectIdentity = ObjectIdentity
tlpAutoProbeUserDefinedAlarm44 = _TlpAutoProbeUserDefinedAlarm44_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 2, 44)
)
if mibBuilder.loadTexts:
    tlpAutoProbeUserDefinedAlarm44.setStatus("current")
_TlpAutoProbeUserDefinedAlarm45_ObjectIdentity = ObjectIdentity
tlpAutoProbeUserDefinedAlarm45 = _TlpAutoProbeUserDefinedAlarm45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 2, 45)
)
if mibBuilder.loadTexts:
    tlpAutoProbeUserDefinedAlarm45.setStatus("current")
_TlpAutoProbeUserDefinedAlarm46_ObjectIdentity = ObjectIdentity
tlpAutoProbeUserDefinedAlarm46 = _TlpAutoProbeUserDefinedAlarm46_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 2, 46)
)
if mibBuilder.loadTexts:
    tlpAutoProbeUserDefinedAlarm46.setStatus("current")
_TlpAutoProbeUserDefinedAlarm47_ObjectIdentity = ObjectIdentity
tlpAutoProbeUserDefinedAlarm47 = _TlpAutoProbeUserDefinedAlarm47_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 2, 47)
)
if mibBuilder.loadTexts:
    tlpAutoProbeUserDefinedAlarm47.setStatus("current")
_TlpAutoProbeUserDefinedAlarm48_ObjectIdentity = ObjectIdentity
tlpAutoProbeUserDefinedAlarm48 = _TlpAutoProbeUserDefinedAlarm48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 2, 48)
)
if mibBuilder.loadTexts:
    tlpAutoProbeUserDefinedAlarm48.setStatus("current")
_TlpAutoProbeUserDefinedAlarm49_ObjectIdentity = ObjectIdentity
tlpAutoProbeUserDefinedAlarm49 = _TlpAutoProbeUserDefinedAlarm49_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 2, 49)
)
if mibBuilder.loadTexts:
    tlpAutoProbeUserDefinedAlarm49.setStatus("current")
_TlpAutoProbeUserDefinedAlarm50_ObjectIdentity = ObjectIdentity
tlpAutoProbeUserDefinedAlarm50 = _TlpAutoProbeUserDefinedAlarm50_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 2, 50)
)
if mibBuilder.loadTexts:
    tlpAutoProbeUserDefinedAlarm50.setStatus("current")
_TlpAutoProbeUserDefinedAlarm51_ObjectIdentity = ObjectIdentity
tlpAutoProbeUserDefinedAlarm51 = _TlpAutoProbeUserDefinedAlarm51_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 2, 51)
)
if mibBuilder.loadTexts:
    tlpAutoProbeUserDefinedAlarm51.setStatus("current")
_TlpAutoProbeUserDefinedAlarm52_ObjectIdentity = ObjectIdentity
tlpAutoProbeUserDefinedAlarm52 = _TlpAutoProbeUserDefinedAlarm52_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 2, 52)
)
if mibBuilder.loadTexts:
    tlpAutoProbeUserDefinedAlarm52.setStatus("current")
_TlpAutoProbeUserDefinedAlarm53_ObjectIdentity = ObjectIdentity
tlpAutoProbeUserDefinedAlarm53 = _TlpAutoProbeUserDefinedAlarm53_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 2, 53)
)
if mibBuilder.loadTexts:
    tlpAutoProbeUserDefinedAlarm53.setStatus("current")
_TlpAutoProbeUserDefinedAlarm54_ObjectIdentity = ObjectIdentity
tlpAutoProbeUserDefinedAlarm54 = _TlpAutoProbeUserDefinedAlarm54_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 2, 54)
)
if mibBuilder.loadTexts:
    tlpAutoProbeUserDefinedAlarm54.setStatus("current")
_TlpAutoProbeUserDefinedAlarm55_ObjectIdentity = ObjectIdentity
tlpAutoProbeUserDefinedAlarm55 = _TlpAutoProbeUserDefinedAlarm55_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 2, 55)
)
if mibBuilder.loadTexts:
    tlpAutoProbeUserDefinedAlarm55.setStatus("current")
_TlpAutoProbeUserDefinedAlarm56_ObjectIdentity = ObjectIdentity
tlpAutoProbeUserDefinedAlarm56 = _TlpAutoProbeUserDefinedAlarm56_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 2, 56)
)
if mibBuilder.loadTexts:
    tlpAutoProbeUserDefinedAlarm56.setStatus("current")
_TlpAutoProbeUserDefinedAlarm57_ObjectIdentity = ObjectIdentity
tlpAutoProbeUserDefinedAlarm57 = _TlpAutoProbeUserDefinedAlarm57_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 2, 57)
)
if mibBuilder.loadTexts:
    tlpAutoProbeUserDefinedAlarm57.setStatus("current")
_TlpAutoProbeUserDefinedAlarm58_ObjectIdentity = ObjectIdentity
tlpAutoProbeUserDefinedAlarm58 = _TlpAutoProbeUserDefinedAlarm58_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 2, 58)
)
if mibBuilder.loadTexts:
    tlpAutoProbeUserDefinedAlarm58.setStatus("current")
_TlpAutoProbeUserDefinedAlarm59_ObjectIdentity = ObjectIdentity
tlpAutoProbeUserDefinedAlarm59 = _TlpAutoProbeUserDefinedAlarm59_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 2, 59)
)
if mibBuilder.loadTexts:
    tlpAutoProbeUserDefinedAlarm59.setStatus("current")
_TlpAutoProbeUserDefinedAlarm60_ObjectIdentity = ObjectIdentity
tlpAutoProbeUserDefinedAlarm60 = _TlpAutoProbeUserDefinedAlarm60_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 2, 60)
)
if mibBuilder.loadTexts:
    tlpAutoProbeUserDefinedAlarm60.setStatus("current")
_TlpAutoProbeUserDefinedAlarm61_ObjectIdentity = ObjectIdentity
tlpAutoProbeUserDefinedAlarm61 = _TlpAutoProbeUserDefinedAlarm61_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 2, 61)
)
if mibBuilder.loadTexts:
    tlpAutoProbeUserDefinedAlarm61.setStatus("current")
_TlpAutoProbeUserDefinedAlarm62_ObjectIdentity = ObjectIdentity
tlpAutoProbeUserDefinedAlarm62 = _TlpAutoProbeUserDefinedAlarm62_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 2, 62)
)
if mibBuilder.loadTexts:
    tlpAutoProbeUserDefinedAlarm62.setStatus("current")
_TlpAutoProbeUserDefinedAlarm63_ObjectIdentity = ObjectIdentity
tlpAutoProbeUserDefinedAlarm63 = _TlpAutoProbeUserDefinedAlarm63_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 2, 63)
)
if mibBuilder.loadTexts:
    tlpAutoProbeUserDefinedAlarm63.setStatus("current")
_TlpAutoProbeUserDefinedAlarm64_ObjectIdentity = ObjectIdentity
tlpAutoProbeUserDefinedAlarm64 = _TlpAutoProbeUserDefinedAlarm64_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 2, 64)
)
if mibBuilder.loadTexts:
    tlpAutoProbeUserDefinedAlarm64.setStatus("current")
_TlpAgentDiagnosticAlarms_ObjectIdentity = ObjectIdentity
tlpAgentDiagnosticAlarms = _TlpAgentDiagnosticAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 3)
)
_TlpAgentDiagnosticCPUUsageHigh_ObjectIdentity = ObjectIdentity
tlpAgentDiagnosticCPUUsageHigh = _TlpAgentDiagnosticCPUUsageHigh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    tlpAgentDiagnosticCPUUsageHigh.setStatus("current")
_TlpAgentDiagnosticMemoryUsageHigh_ObjectIdentity = ObjectIdentity
tlpAgentDiagnosticMemoryUsageHigh = _TlpAgentDiagnosticMemoryUsageHigh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 3, 2)
)
if mibBuilder.loadTexts:
    tlpAgentDiagnosticMemoryUsageHigh.setStatus("current")
_TlpAgentDiagnosticServiceFailed_ObjectIdentity = ObjectIdentity
tlpAgentDiagnosticServiceFailed = _TlpAgentDiagnosticServiceFailed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 3, 3)
)
if mibBuilder.loadTexts:
    tlpAgentDiagnosticServiceFailed.setStatus("current")
_TlpAgentConfigurationAlarms_ObjectIdentity = ObjectIdentity
tlpAgentConfigurationAlarms = _TlpAgentConfigurationAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 4)
)
_TlpAgentConfigurationBackedUp_ObjectIdentity = ObjectIdentity
tlpAgentConfigurationBackedUp = _TlpAgentConfigurationBackedUp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 4, 1)
)
if mibBuilder.loadTexts:
    tlpAgentConfigurationBackedUp.setStatus("current")
_TlpAgentConfigurationImported_ObjectIdentity = ObjectIdentity
tlpAgentConfigurationImported = _TlpAgentConfigurationImported_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 4, 2)
)
if mibBuilder.loadTexts:
    tlpAgentConfigurationImported.setStatus("current")
_TlpAgentConfigurationRestored_ObjectIdentity = ObjectIdentity
tlpAgentConfigurationRestored = _TlpAgentConfigurationRestored_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 4, 3)
)
if mibBuilder.loadTexts:
    tlpAgentConfigurationRestored.setStatus("current")
_TlpAgentMaintenanceAlarms_ObjectIdentity = ObjectIdentity
tlpAgentMaintenanceAlarms = _TlpAgentMaintenanceAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 5)
)
_TlpAgentStarted_ObjectIdentity = ObjectIdentity
tlpAgentStarted = _TlpAgentStarted_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 5, 1)
)
if mibBuilder.loadTexts:
    tlpAgentStarted.setStatus("current")
_TlpAgentStopped_ObjectIdentity = ObjectIdentity
tlpAgentStopped = _TlpAgentStopped_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 5, 2)
)
if mibBuilder.loadTexts:
    tlpAgentStopped.setStatus("current")
_TlpAgentRebootInitiated_ObjectIdentity = ObjectIdentity
tlpAgentRebootInitiated = _TlpAgentRebootInitiated_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 5, 3)
)
if mibBuilder.loadTexts:
    tlpAgentRebootInitiated.setStatus("current")
_TlpAgentFirmwareUpdated_ObjectIdentity = ObjectIdentity
tlpAgentFirmwareUpdated = _TlpAgentFirmwareUpdated_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 5, 4)
)
if mibBuilder.loadTexts:
    tlpAgentFirmwareUpdated.setStatus("current")
_TlpAgentRestoreFactoryDefaults_ObjectIdentity = ObjectIdentity
tlpAgentRestoreFactoryDefaults = _TlpAgentRestoreFactoryDefaults_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 5, 5)
)
if mibBuilder.loadTexts:
    tlpAgentRestoreFactoryDefaults.setStatus("current")
_TlpAgentUserManagementAlarms_ObjectIdentity = ObjectIdentity
tlpAgentUserManagementAlarms = _TlpAgentUserManagementAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 6)
)
_TlpAgentUserPasswordChanged_ObjectIdentity = ObjectIdentity
tlpAgentUserPasswordChanged = _TlpAgentUserPasswordChanged_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 6, 1)
)
if mibBuilder.loadTexts:
    tlpAgentUserPasswordChanged.setStatus("current")
_TlpAgentUserAdded_ObjectIdentity = ObjectIdentity
tlpAgentUserAdded = _TlpAgentUserAdded_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 6, 2)
)
if mibBuilder.loadTexts:
    tlpAgentUserAdded.setStatus("current")
_TlpAgentUserModified_ObjectIdentity = ObjectIdentity
tlpAgentUserModified = _TlpAgentUserModified_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 6, 3)
)
if mibBuilder.loadTexts:
    tlpAgentUserModified.setStatus("current")
_TlpAgentUserDeleted_ObjectIdentity = ObjectIdentity
tlpAgentUserDeleted = _TlpAgentUserDeleted_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 6, 4)
)
if mibBuilder.loadTexts:
    tlpAgentUserDeleted.setStatus("current")
_TlpAgentUserConditionOccurred_ObjectIdentity = ObjectIdentity
tlpAgentUserConditionOccurred = _TlpAgentUserConditionOccurred_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 6, 5)
)
if mibBuilder.loadTexts:
    tlpAgentUserConditionOccurred.setStatus("current")
_TlpAgentRoleAdded_ObjectIdentity = ObjectIdentity
tlpAgentRoleAdded = _TlpAgentRoleAdded_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 6, 6)
)
if mibBuilder.loadTexts:
    tlpAgentRoleAdded.setStatus("current")
_TlpAgentRoleModified_ObjectIdentity = ObjectIdentity
tlpAgentRoleModified = _TlpAgentRoleModified_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 6, 7)
)
if mibBuilder.loadTexts:
    tlpAgentRoleModified.setStatus("current")
_TlpAgentRoleDeleted_ObjectIdentity = ObjectIdentity
tlpAgentRoleDeleted = _TlpAgentRoleDeleted_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1, 6, 8)
)
if mibBuilder.loadTexts:
    tlpAgentRoleDeleted.setStatus("current")
_TlpDeviceAlarms_ObjectIdentity = ObjectIdentity
tlpDeviceAlarms = _TlpDeviceAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2)
)
_TlpAlarmCommunicationsLost_ObjectIdentity = ObjectIdentity
tlpAlarmCommunicationsLost = _TlpAlarmCommunicationsLost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 1)
)
if mibBuilder.loadTexts:
    tlpAlarmCommunicationsLost.setStatus("current")
_TlpAlarmUserDefined_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined = _TlpAlarmUserDefined_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2)
)
_TlpAlarmUserDefined01_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined01 = _TlpAlarmUserDefined01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined01.setStatus("current")
_TlpAlarmUserDefined02_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined02 = _TlpAlarmUserDefined02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 2)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined02.setStatus("current")
_TlpAlarmUserDefined03_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined03 = _TlpAlarmUserDefined03_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 3)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined03.setStatus("current")
_TlpAlarmUserDefined04_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined04 = _TlpAlarmUserDefined04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 4)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined04.setStatus("current")
_TlpAlarmUserDefined05_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined05 = _TlpAlarmUserDefined05_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 5)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined05.setStatus("current")
_TlpAlarmUserDefined06_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined06 = _TlpAlarmUserDefined06_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 6)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined06.setStatus("current")
_TlpAlarmUserDefined07_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined07 = _TlpAlarmUserDefined07_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 7)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined07.setStatus("current")
_TlpAlarmUserDefined08_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined08 = _TlpAlarmUserDefined08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 8)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined08.setStatus("current")
_TlpAlarmUserDefined09_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined09 = _TlpAlarmUserDefined09_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 9)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined09.setStatus("current")
_TlpAlarmUserDefined10_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined10 = _TlpAlarmUserDefined10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 10)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined10.setStatus("current")
_TlpAlarmUserDefined11_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined11 = _TlpAlarmUserDefined11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 11)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined11.setStatus("current")
_TlpAlarmUserDefined12_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined12 = _TlpAlarmUserDefined12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 12)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined12.setStatus("current")
_TlpAlarmUserDefined13_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined13 = _TlpAlarmUserDefined13_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 13)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined13.setStatus("current")
_TlpAlarmUserDefined14_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined14 = _TlpAlarmUserDefined14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 14)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined14.setStatus("current")
_TlpAlarmUserDefined15_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined15 = _TlpAlarmUserDefined15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 15)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined15.setStatus("current")
_TlpAlarmUserDefined16_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined16 = _TlpAlarmUserDefined16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 16)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined16.setStatus("current")
_TlpAlarmUserDefined17_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined17 = _TlpAlarmUserDefined17_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 17)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined17.setStatus("current")
_TlpAlarmUserDefined18_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined18 = _TlpAlarmUserDefined18_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 18)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined18.setStatus("current")
_TlpAlarmUserDefined19_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined19 = _TlpAlarmUserDefined19_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 19)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined19.setStatus("current")
_TlpAlarmUserDefined20_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined20 = _TlpAlarmUserDefined20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 20)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined20.setStatus("current")
_TlpAlarmUserDefined21_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined21 = _TlpAlarmUserDefined21_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 21)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined21.setStatus("current")
_TlpAlarmUserDefined22_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined22 = _TlpAlarmUserDefined22_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 22)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined22.setStatus("current")
_TlpAlarmUserDefined23_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined23 = _TlpAlarmUserDefined23_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 23)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined23.setStatus("current")
_TlpAlarmUserDefined24_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined24 = _TlpAlarmUserDefined24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 24)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined24.setStatus("current")
_TlpAlarmUserDefined25_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined25 = _TlpAlarmUserDefined25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 25)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined25.setStatus("current")
_TlpAlarmUserDefined26_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined26 = _TlpAlarmUserDefined26_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 26)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined26.setStatus("current")
_TlpAlarmUserDefined27_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined27 = _TlpAlarmUserDefined27_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 27)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined27.setStatus("current")
_TlpAlarmUserDefined28_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined28 = _TlpAlarmUserDefined28_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 28)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined28.setStatus("current")
_TlpAlarmUserDefined29_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined29 = _TlpAlarmUserDefined29_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 29)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined29.setStatus("current")
_TlpAlarmUserDefined30_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined30 = _TlpAlarmUserDefined30_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 30)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined30.setStatus("current")
_TlpAlarmUserDefined31_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined31 = _TlpAlarmUserDefined31_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 31)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined31.setStatus("current")
_TlpAlarmUserDefined32_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined32 = _TlpAlarmUserDefined32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 32)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined32.setStatus("current")
_TlpAlarmUserDefined33_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined33 = _TlpAlarmUserDefined33_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 33)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined33.setStatus("current")
_TlpAlarmUserDefined34_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined34 = _TlpAlarmUserDefined34_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 34)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined34.setStatus("current")
_TlpAlarmUserDefined35_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined35 = _TlpAlarmUserDefined35_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 35)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined35.setStatus("current")
_TlpAlarmUserDefined36_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined36 = _TlpAlarmUserDefined36_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 36)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined36.setStatus("current")
_TlpAlarmUserDefined37_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined37 = _TlpAlarmUserDefined37_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 37)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined37.setStatus("current")
_TlpAlarmUserDefined38_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined38 = _TlpAlarmUserDefined38_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 38)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined38.setStatus("current")
_TlpAlarmUserDefined39_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined39 = _TlpAlarmUserDefined39_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 39)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined39.setStatus("current")
_TlpAlarmUserDefined40_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined40 = _TlpAlarmUserDefined40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 40)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined40.setStatus("current")
_TlpAlarmUserDefined41_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined41 = _TlpAlarmUserDefined41_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 41)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined41.setStatus("current")
_TlpAlarmUserDefined42_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined42 = _TlpAlarmUserDefined42_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 42)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined42.setStatus("current")
_TlpAlarmUserDefined43_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined43 = _TlpAlarmUserDefined43_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 43)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined43.setStatus("current")
_TlpAlarmUserDefined44_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined44 = _TlpAlarmUserDefined44_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 44)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined44.setStatus("current")
_TlpAlarmUserDefined45_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined45 = _TlpAlarmUserDefined45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 45)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined45.setStatus("current")
_TlpAlarmUserDefined46_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined46 = _TlpAlarmUserDefined46_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 46)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined46.setStatus("current")
_TlpAlarmUserDefined47_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined47 = _TlpAlarmUserDefined47_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 47)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined47.setStatus("current")
_TlpAlarmUserDefined48_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined48 = _TlpAlarmUserDefined48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 48)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined48.setStatus("current")
_TlpAlarmUserDefined49_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined49 = _TlpAlarmUserDefined49_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 49)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined49.setStatus("current")
_TlpAlarmUserDefined50_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined50 = _TlpAlarmUserDefined50_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 50)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined50.setStatus("current")
_TlpAlarmUserDefined51_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined51 = _TlpAlarmUserDefined51_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 51)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined51.setStatus("current")
_TlpAlarmUserDefined52_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined52 = _TlpAlarmUserDefined52_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 52)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined52.setStatus("current")
_TlpAlarmUserDefined53_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined53 = _TlpAlarmUserDefined53_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 53)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined53.setStatus("current")
_TlpAlarmUserDefined54_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined54 = _TlpAlarmUserDefined54_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 54)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined54.setStatus("current")
_TlpAlarmUserDefined55_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined55 = _TlpAlarmUserDefined55_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 55)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined55.setStatus("current")
_TlpAlarmUserDefined56_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined56 = _TlpAlarmUserDefined56_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 56)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined56.setStatus("current")
_TlpAlarmUserDefined57_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined57 = _TlpAlarmUserDefined57_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 57)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined57.setStatus("current")
_TlpAlarmUserDefined58_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined58 = _TlpAlarmUserDefined58_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 58)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined58.setStatus("current")
_TlpAlarmUserDefined59_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined59 = _TlpAlarmUserDefined59_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 59)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined59.setStatus("current")
_TlpAlarmUserDefined60_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined60 = _TlpAlarmUserDefined60_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 60)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined60.setStatus("current")
_TlpAlarmUserDefined61_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined61 = _TlpAlarmUserDefined61_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 61)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined61.setStatus("current")
_TlpAlarmUserDefined62_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined62 = _TlpAlarmUserDefined62_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 62)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined62.setStatus("current")
_TlpAlarmUserDefined63_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined63 = _TlpAlarmUserDefined63_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 63)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined63.setStatus("current")
_TlpAlarmUserDefined64_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined64 = _TlpAlarmUserDefined64_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 64)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined64.setStatus("current")
_TlpAlarmInternalFirmwareError_ObjectIdentity = ObjectIdentity
tlpAlarmInternalFirmwareError = _TlpAlarmInternalFirmwareError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 3)
)
if mibBuilder.loadTexts:
    tlpAlarmInternalFirmwareError.setStatus("current")
_TlpAlarmDeviceEEPROMFault_ObjectIdentity = ObjectIdentity
tlpAlarmDeviceEEPROMFault = _TlpAlarmDeviceEEPROMFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 4)
)
if mibBuilder.loadTexts:
    tlpAlarmDeviceEEPROMFault.setStatus("current")
_TlpUpsAlarms_ObjectIdentity = ObjectIdentity
tlpUpsAlarms = _TlpUpsAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3)
)
_TlpUpsAlarmBatteryBad_ObjectIdentity = ObjectIdentity
tlpUpsAlarmBatteryBad = _TlpUpsAlarmBatteryBad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 1)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmBatteryBad.setStatus("current")
_TlpUpsAlarmOnBattery_ObjectIdentity = ObjectIdentity
tlpUpsAlarmOnBattery = _TlpUpsAlarmOnBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 2)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmOnBattery.setStatus("current")
_TlpUpsAlarmLowBattery_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLowBattery = _TlpUpsAlarmLowBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 3)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLowBattery.setStatus("current")
_TlpUpsAlarmDepletedBattery_ObjectIdentity = ObjectIdentity
tlpUpsAlarmDepletedBattery = _TlpUpsAlarmDepletedBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 4)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmDepletedBattery.setStatus("current")
_TlpUpsAlarmTempBad_ObjectIdentity = ObjectIdentity
tlpUpsAlarmTempBad = _TlpUpsAlarmTempBad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 5)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmTempBad.setStatus("current")
_TlpUpsAlarmInputBad_ObjectIdentity = ObjectIdentity
tlpUpsAlarmInputBad = _TlpUpsAlarmInputBad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 6)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmInputBad.setStatus("current")
_TlpUpsAlarmOutputBad_ObjectIdentity = ObjectIdentity
tlpUpsAlarmOutputBad = _TlpUpsAlarmOutputBad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 7)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmOutputBad.setStatus("current")
_TlpUpsAlarmOutputOverload_ObjectIdentity = ObjectIdentity
tlpUpsAlarmOutputOverload = _TlpUpsAlarmOutputOverload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 8)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmOutputOverload.setStatus("current")
_TlpUpsAlarmOnBypass_ObjectIdentity = ObjectIdentity
tlpUpsAlarmOnBypass = _TlpUpsAlarmOnBypass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 9)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmOnBypass.setStatus("current")
_TlpUpsAlarmBypassBad_ObjectIdentity = ObjectIdentity
tlpUpsAlarmBypassBad = _TlpUpsAlarmBypassBad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 10)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmBypassBad.setStatus("current")
_TlpUpsAlarmOutputOffAsRequested_ObjectIdentity = ObjectIdentity
tlpUpsAlarmOutputOffAsRequested = _TlpUpsAlarmOutputOffAsRequested_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 11)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmOutputOffAsRequested.setStatus("current")
_TlpUpsAlarmUpsOffAsRequested_ObjectIdentity = ObjectIdentity
tlpUpsAlarmUpsOffAsRequested = _TlpUpsAlarmUpsOffAsRequested_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 12)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmUpsOffAsRequested.setStatus("current")
_TlpUpsAlarmChargerFailed_ObjectIdentity = ObjectIdentity
tlpUpsAlarmChargerFailed = _TlpUpsAlarmChargerFailed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 13)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmChargerFailed.setStatus("current")
_TlpUpsAlarmOutputOff_ObjectIdentity = ObjectIdentity
tlpUpsAlarmOutputOff = _TlpUpsAlarmOutputOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 14)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmOutputOff.setStatus("current")
_TlpUpsAlarmUpsOff_ObjectIdentity = ObjectIdentity
tlpUpsAlarmUpsOff = _TlpUpsAlarmUpsOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 15)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmUpsOff.setStatus("current")
_TlpUpsAlarmFanFailure_ObjectIdentity = ObjectIdentity
tlpUpsAlarmFanFailure = _TlpUpsAlarmFanFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 16)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmFanFailure.setStatus("current")
_TlpUpsAlarmFuseFailure_ObjectIdentity = ObjectIdentity
tlpUpsAlarmFuseFailure = _TlpUpsAlarmFuseFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 17)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmFuseFailure.setStatus("current")
_TlpUpsAlarmGeneralFault_ObjectIdentity = ObjectIdentity
tlpUpsAlarmGeneralFault = _TlpUpsAlarmGeneralFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 18)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmGeneralFault.setStatus("current")
_TlpUpsAlarmDiagnosticTestFailed_ObjectIdentity = ObjectIdentity
tlpUpsAlarmDiagnosticTestFailed = _TlpUpsAlarmDiagnosticTestFailed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 19)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmDiagnosticTestFailed.setStatus("current")
_TlpUpsAlarmAwaitingPower_ObjectIdentity = ObjectIdentity
tlpUpsAlarmAwaitingPower = _TlpUpsAlarmAwaitingPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 20)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmAwaitingPower.setStatus("current")
_TlpUpsAlarmShutdownPending_ObjectIdentity = ObjectIdentity
tlpUpsAlarmShutdownPending = _TlpUpsAlarmShutdownPending_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 21)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmShutdownPending.setStatus("current")
_TlpUpsAlarmShutdownImminent_ObjectIdentity = ObjectIdentity
tlpUpsAlarmShutdownImminent = _TlpUpsAlarmShutdownImminent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 22)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmShutdownImminent.setStatus("current")
_TlpUpsAlarmLoadLevelAboveThreshold_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadLevelAboveThreshold = _TlpUpsAlarmLoadLevelAboveThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 23)
)
_TlpUpsAlarmLoadLevelAboveThresholdTotal_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadLevelAboveThresholdTotal = _TlpUpsAlarmLoadLevelAboveThresholdTotal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 23, 1)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadLevelAboveThresholdTotal.setStatus("current")
_TlpUpsAlarmLoadLevelAboveThresholdPhase1_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadLevelAboveThresholdPhase1 = _TlpUpsAlarmLoadLevelAboveThresholdPhase1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 23, 2)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadLevelAboveThresholdPhase1.setStatus("current")
_TlpUpsAlarmLoadLevelAboveThresholdPhase2_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadLevelAboveThresholdPhase2 = _TlpUpsAlarmLoadLevelAboveThresholdPhase2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 23, 3)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadLevelAboveThresholdPhase2.setStatus("current")
_TlpUpsAlarmLoadLevelAboveThresholdPhase3_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadLevelAboveThresholdPhase3 = _TlpUpsAlarmLoadLevelAboveThresholdPhase3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 23, 4)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadLevelAboveThresholdPhase3.setStatus("current")
_TlpUpsAlarmOutputCurrentChanged_ObjectIdentity = ObjectIdentity
tlpUpsAlarmOutputCurrentChanged = _TlpUpsAlarmOutputCurrentChanged_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 24)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmOutputCurrentChanged.setStatus("deprecated")
_TlpUpsAlarmBatteryAgeAboveThreshold_ObjectIdentity = ObjectIdentity
tlpUpsAlarmBatteryAgeAboveThreshold = _TlpUpsAlarmBatteryAgeAboveThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 25)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmBatteryAgeAboveThreshold.setStatus("current")
_TlpUpsAlarmLoadOff_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff = _TlpUpsAlarmLoadOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26)
)
_TlpUpsAlarmLoadOff01_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff01 = _TlpUpsAlarmLoadOff01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 1)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff01.setStatus("current")
_TlpUpsAlarmLoadOff02_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff02 = _TlpUpsAlarmLoadOff02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 2)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff02.setStatus("current")
_TlpUpsAlarmLoadOff03_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff03 = _TlpUpsAlarmLoadOff03_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 3)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff03.setStatus("current")
_TlpUpsAlarmLoadOff04_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff04 = _TlpUpsAlarmLoadOff04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 4)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff04.setStatus("current")
_TlpUpsAlarmLoadOff05_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff05 = _TlpUpsAlarmLoadOff05_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 5)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff05.setStatus("current")
_TlpUpsAlarmLoadOff06_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff06 = _TlpUpsAlarmLoadOff06_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 6)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff06.setStatus("current")
_TlpUpsAlarmLoadOff07_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff07 = _TlpUpsAlarmLoadOff07_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 7)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff07.setStatus("current")
_TlpUpsAlarmLoadOff08_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff08 = _TlpUpsAlarmLoadOff08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 8)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff08.setStatus("current")
_TlpUpsAlarmLoadOff09_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff09 = _TlpUpsAlarmLoadOff09_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 9)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff09.setStatus("current")
_TlpUpsAlarmLoadOff10_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff10 = _TlpUpsAlarmLoadOff10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 10)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff10.setStatus("current")
_TlpUpsAlarmLoadOff11_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff11 = _TlpUpsAlarmLoadOff11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 11)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff11.setStatus("current")
_TlpUpsAlarmLoadOff12_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff12 = _TlpUpsAlarmLoadOff12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 12)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff12.setStatus("current")
_TlpUpsAlarmLoadOff13_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff13 = _TlpUpsAlarmLoadOff13_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 13)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff13.setStatus("current")
_TlpUpsAlarmLoadOff14_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff14 = _TlpUpsAlarmLoadOff14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 14)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff14.setStatus("current")
_TlpUpsAlarmLoadOff15_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff15 = _TlpUpsAlarmLoadOff15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 15)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff15.setStatus("current")
_TlpUpsAlarmLoadOff16_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff16 = _TlpUpsAlarmLoadOff16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 16)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff16.setStatus("current")
_TlpUpsAlarmLoadOff17_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff17 = _TlpUpsAlarmLoadOff17_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 17)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff17.setStatus("current")
_TlpUpsAlarmLoadOff18_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff18 = _TlpUpsAlarmLoadOff18_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 18)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff18.setStatus("current")
_TlpUpsAlarmLoadOff19_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff19 = _TlpUpsAlarmLoadOff19_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 19)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff19.setStatus("current")
_TlpUpsAlarmLoadOff20_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff20 = _TlpUpsAlarmLoadOff20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 20)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff20.setStatus("current")
_TlpUpsAlarmLoadOff21_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff21 = _TlpUpsAlarmLoadOff21_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 21)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff21.setStatus("current")
_TlpUpsAlarmLoadOff22_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff22 = _TlpUpsAlarmLoadOff22_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 22)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff22.setStatus("current")
_TlpUpsAlarmLoadOff23_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff23 = _TlpUpsAlarmLoadOff23_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 23)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff23.setStatus("current")
_TlpUpsAlarmLoadOff24_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff24 = _TlpUpsAlarmLoadOff24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 24)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff24.setStatus("current")
_TlpUpsAlarmLoadOff25_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff25 = _TlpUpsAlarmLoadOff25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 25)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff25.setStatus("current")
_TlpUpsAlarmLoadOff26_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff26 = _TlpUpsAlarmLoadOff26_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 26)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff26.setStatus("current")
_TlpUpsAlarmLoadOff27_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff27 = _TlpUpsAlarmLoadOff27_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 27)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff27.setStatus("current")
_TlpUpsAlarmLoadOff28_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff28 = _TlpUpsAlarmLoadOff28_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 28)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff28.setStatus("current")
_TlpUpsAlarmLoadOff29_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff29 = _TlpUpsAlarmLoadOff29_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 29)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff29.setStatus("current")
_TlpUpsAlarmLoadOff30_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff30 = _TlpUpsAlarmLoadOff30_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 30)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff30.setStatus("current")
_TlpUpsAlarmLoadOff31_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff31 = _TlpUpsAlarmLoadOff31_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 31)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff31.setStatus("current")
_TlpUpsAlarmLoadOff32_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff32 = _TlpUpsAlarmLoadOff32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 32)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff32.setStatus("current")
_TlpUpsAlarmLoadOff33_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff33 = _TlpUpsAlarmLoadOff33_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 33)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff33.setStatus("current")
_TlpUpsAlarmLoadOff34_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff34 = _TlpUpsAlarmLoadOff34_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 34)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff34.setStatus("current")
_TlpUpsAlarmLoadOff35_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff35 = _TlpUpsAlarmLoadOff35_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 35)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff35.setStatus("current")
_TlpUpsAlarmLoadOff36_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff36 = _TlpUpsAlarmLoadOff36_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 36)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff36.setStatus("current")
_TlpUpsAlarmLoadOff37_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff37 = _TlpUpsAlarmLoadOff37_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 37)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff37.setStatus("current")
_TlpUpsAlarmLoadOff38_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff38 = _TlpUpsAlarmLoadOff38_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 38)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff38.setStatus("current")
_TlpUpsAlarmLoadOff39_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff39 = _TlpUpsAlarmLoadOff39_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 39)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff39.setStatus("current")
_TlpUpsAlarmLoadOff40_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff40 = _TlpUpsAlarmLoadOff40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 40)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff40.setStatus("current")
_TlpUpsAlarmLoadOff41_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff41 = _TlpUpsAlarmLoadOff41_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 41)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff41.setStatus("current")
_TlpUpsAlarmLoadOff42_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff42 = _TlpUpsAlarmLoadOff42_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 42)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff42.setStatus("current")
_TlpUpsAlarmLoadOff43_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff43 = _TlpUpsAlarmLoadOff43_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 43)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff43.setStatus("current")
_TlpUpsAlarmLoadOff44_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff44 = _TlpUpsAlarmLoadOff44_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 44)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff44.setStatus("current")
_TlpUpsAlarmLoadOff45_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff45 = _TlpUpsAlarmLoadOff45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 45)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff45.setStatus("current")
_TlpUpsAlarmLoadOff46_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff46 = _TlpUpsAlarmLoadOff46_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 46)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff46.setStatus("current")
_TlpUpsAlarmLoadOff47_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff47 = _TlpUpsAlarmLoadOff47_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 47)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff47.setStatus("current")
_TlpUpsAlarmLoadOff48_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff48 = _TlpUpsAlarmLoadOff48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 48)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff48.setStatus("current")
_TlpUpsAlarmCurrentAboveThreshold_ObjectIdentity = ObjectIdentity
tlpUpsAlarmCurrentAboveThreshold = _TlpUpsAlarmCurrentAboveThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 27)
)
_TlpUpsAlarmCurrentAboveThreshold1_ObjectIdentity = ObjectIdentity
tlpUpsAlarmCurrentAboveThreshold1 = _TlpUpsAlarmCurrentAboveThreshold1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 27, 1)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmCurrentAboveThreshold1.setStatus("current")
_TlpUpsAlarmCurrentAboveThreshold2_ObjectIdentity = ObjectIdentity
tlpUpsAlarmCurrentAboveThreshold2 = _TlpUpsAlarmCurrentAboveThreshold2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 27, 2)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmCurrentAboveThreshold2.setStatus("current")
_TlpUpsAlarmCurrentAboveThreshold3_ObjectIdentity = ObjectIdentity
tlpUpsAlarmCurrentAboveThreshold3 = _TlpUpsAlarmCurrentAboveThreshold3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 27, 3)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmCurrentAboveThreshold3.setStatus("current")
_TlpUpsAlarmCurrentAboveThreshold4_ObjectIdentity = ObjectIdentity
tlpUpsAlarmCurrentAboveThreshold4 = _TlpUpsAlarmCurrentAboveThreshold4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 27, 4)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmCurrentAboveThreshold4.setStatus("current")
_TlpUpsAlarmCurrentAboveThreshold5_ObjectIdentity = ObjectIdentity
tlpUpsAlarmCurrentAboveThreshold5 = _TlpUpsAlarmCurrentAboveThreshold5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 27, 5)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmCurrentAboveThreshold5.setStatus("current")
_TlpUpsAlarmCurrentAboveThreshold6_ObjectIdentity = ObjectIdentity
tlpUpsAlarmCurrentAboveThreshold6 = _TlpUpsAlarmCurrentAboveThreshold6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 27, 6)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmCurrentAboveThreshold6.setStatus("current")
_TlpUpsAlarmRuntimeBelowWarningLevel_ObjectIdentity = ObjectIdentity
tlpUpsAlarmRuntimeBelowWarningLevel = _TlpUpsAlarmRuntimeBelowWarningLevel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 28)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmRuntimeBelowWarningLevel.setStatus("current")
_TlpUpsAlarmBusStartVoltageLow_ObjectIdentity = ObjectIdentity
tlpUpsAlarmBusStartVoltageLow = _TlpUpsAlarmBusStartVoltageLow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 29)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmBusStartVoltageLow.setStatus("current")
_TlpUpsAlarmBusOverVoltage_ObjectIdentity = ObjectIdentity
tlpUpsAlarmBusOverVoltage = _TlpUpsAlarmBusOverVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 30)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmBusOverVoltage.setStatus("current")
_TlpUpsAlarmBusUnderVoltage_ObjectIdentity = ObjectIdentity
tlpUpsAlarmBusUnderVoltage = _TlpUpsAlarmBusUnderVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 31)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmBusUnderVoltage.setStatus("current")
_TlpUpsAlarmBusVoltageUnbalanced_ObjectIdentity = ObjectIdentity
tlpUpsAlarmBusVoltageUnbalanced = _TlpUpsAlarmBusVoltageUnbalanced_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 32)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmBusVoltageUnbalanced.setStatus("current")
_TlpUpsAlarmInverterSoftStartBad_ObjectIdentity = ObjectIdentity
tlpUpsAlarmInverterSoftStartBad = _TlpUpsAlarmInverterSoftStartBad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 33)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmInverterSoftStartBad.setStatus("current")
_TlpUpsAlarmInverterOverVoltage_ObjectIdentity = ObjectIdentity
tlpUpsAlarmInverterOverVoltage = _TlpUpsAlarmInverterOverVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 34)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmInverterOverVoltage.setStatus("current")
_TlpUpsAlarmInverterUnderVoltage_ObjectIdentity = ObjectIdentity
tlpUpsAlarmInverterUnderVoltage = _TlpUpsAlarmInverterUnderVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 35)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmInverterUnderVoltage.setStatus("current")
_TlpUpsAlarmInverterCircuitBad_ObjectIdentity = ObjectIdentity
tlpUpsAlarmInverterCircuitBad = _TlpUpsAlarmInverterCircuitBad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 36)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmInverterCircuitBad.setStatus("current")
_TlpUpsAlarmBatteryOverVoltage_ObjectIdentity = ObjectIdentity
tlpUpsAlarmBatteryOverVoltage = _TlpUpsAlarmBatteryOverVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 37)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmBatteryOverVoltage.setStatus("current")
_TlpUpsAlarmBatteryUnderVoltage_ObjectIdentity = ObjectIdentity
tlpUpsAlarmBatteryUnderVoltage = _TlpUpsAlarmBatteryUnderVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 38)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmBatteryUnderVoltage.setStatus("current")
_TlpUpsAlarmSiteWiringFault_ObjectIdentity = ObjectIdentity
tlpUpsAlarmSiteWiringFault = _TlpUpsAlarmSiteWiringFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 39)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmSiteWiringFault.setStatus("current")
_TlpUpsAlarmOverTemperatureProtection_ObjectIdentity = ObjectIdentity
tlpUpsAlarmOverTemperatureProtection = _TlpUpsAlarmOverTemperatureProtection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 40)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmOverTemperatureProtection.setStatus("current")
_TlpUpsAlarmOverCharged_ObjectIdentity = ObjectIdentity
tlpUpsAlarmOverCharged = _TlpUpsAlarmOverCharged_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 41)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmOverCharged.setStatus("current")
_TlpUpsAlarmEPOActive_ObjectIdentity = ObjectIdentity
tlpUpsAlarmEPOActive = _TlpUpsAlarmEPOActive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 42)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmEPOActive.setStatus("current")
_TlpUpsAlarmBypassFrequencyBad_ObjectIdentity = ObjectIdentity
tlpUpsAlarmBypassFrequencyBad = _TlpUpsAlarmBypassFrequencyBad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 43)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmBypassFrequencyBad.setStatus("current")
_TlpUpsAlarmExternalSmartBatteryAgeAboveThreshold_ObjectIdentity = ObjectIdentity
tlpUpsAlarmExternalSmartBatteryAgeAboveThreshold = _TlpUpsAlarmExternalSmartBatteryAgeAboveThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 44)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmExternalSmartBatteryAgeAboveThreshold.setStatus("current")
_TlpUpsAlarmExternalNonSmartBatteryAgeAboveThreshold_ObjectIdentity = ObjectIdentity
tlpUpsAlarmExternalNonSmartBatteryAgeAboveThreshold = _TlpUpsAlarmExternalNonSmartBatteryAgeAboveThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 45)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmExternalNonSmartBatteryAgeAboveThreshold.setStatus("current")
_TlpUpsAlarmInternalSmartBatteryCommLost_ObjectIdentity = ObjectIdentity
tlpUpsAlarmInternalSmartBatteryCommLost = _TlpUpsAlarmInternalSmartBatteryCommLost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 46)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmInternalSmartBatteryCommLost.setStatus("current")
_TlpUpsAlarmLoadsNotAllOn_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadsNotAllOn = _TlpUpsAlarmLoadsNotAllOn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 47)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadsNotAllOn.setStatus("current")
_TlpUpsAlarmBatteryTemperatureHigh_ObjectIdentity = ObjectIdentity
tlpUpsAlarmBatteryTemperatureHigh = _TlpUpsAlarmBatteryTemperatureHigh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 48)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmBatteryTemperatureHigh.setStatus("current")
_TlpUpsAlarmBatteryTemperatureLow_ObjectIdentity = ObjectIdentity
tlpUpsAlarmBatteryTemperatureLow = _TlpUpsAlarmBatteryTemperatureLow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 49)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmBatteryTemperatureLow.setStatus("current")
_TlpUpsAlarmBatteryDisconnected_ObjectIdentity = ObjectIdentity
tlpUpsAlarmBatteryDisconnected = _TlpUpsAlarmBatteryDisconnected_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 50)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmBatteryDisconnected.setStatus("current")
_TlpUpsAlarmBatteryTemperatureSensorDisconnected_ObjectIdentity = ObjectIdentity
tlpUpsAlarmBatteryTemperatureSensorDisconnected = _TlpUpsAlarmBatteryTemperatureSensorDisconnected_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 51)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmBatteryTemperatureSensorDisconnected.setStatus("current")
_TlpUpsAlarmTemperatureDerating_ObjectIdentity = ObjectIdentity
tlpUpsAlarmTemperatureDerating = _TlpUpsAlarmTemperatureDerating_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 52)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmTemperatureDerating.setStatus("current")
_TlpUpsAlarmInputContact_ObjectIdentity = ObjectIdentity
tlpUpsAlarmInputContact = _TlpUpsAlarmInputContact_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 53)
)
_TlpUpsAlarmInputContact1_ObjectIdentity = ObjectIdentity
tlpUpsAlarmInputContact1 = _TlpUpsAlarmInputContact1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 53, 1)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmInputContact1.setStatus("current")
_TlpUpsAlarmOutputContact_ObjectIdentity = ObjectIdentity
tlpUpsAlarmOutputContact = _TlpUpsAlarmOutputContact_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 54)
)
_TlpUpsAlarmOutputContact1_ObjectIdentity = ObjectIdentity
tlpUpsAlarmOutputContact1 = _TlpUpsAlarmOutputContact1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 54, 1)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmOutputContact1.setStatus("current")
_TlpUpsAlarmOutputContact2_ObjectIdentity = ObjectIdentity
tlpUpsAlarmOutputContact2 = _TlpUpsAlarmOutputContact2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 54, 2)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmOutputContact2.setStatus("current")
_TlpUpsAlarmOutputContact3_ObjectIdentity = ObjectIdentity
tlpUpsAlarmOutputContact3 = _TlpUpsAlarmOutputContact3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 54, 3)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmOutputContact3.setStatus("current")
_TlpUpsAlarmOutputContact4_ObjectIdentity = ObjectIdentity
tlpUpsAlarmOutputContact4 = _TlpUpsAlarmOutputContact4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 54, 4)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmOutputContact4.setStatus("current")
_TlpUpsAlarmOutputContact5_ObjectIdentity = ObjectIdentity
tlpUpsAlarmOutputContact5 = _TlpUpsAlarmOutputContact5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 54, 5)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmOutputContact5.setStatus("current")
_TlpUpsAlarmOutputContact6_ObjectIdentity = ObjectIdentity
tlpUpsAlarmOutputContact6 = _TlpUpsAlarmOutputContact6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 54, 6)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmOutputContact6.setStatus("current")
_TlpUpsAlarmCurrentBelowThreshold_ObjectIdentity = ObjectIdentity
tlpUpsAlarmCurrentBelowThreshold = _TlpUpsAlarmCurrentBelowThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 55)
)
_TlpUpsAlarmCurrentBelowThreshold1_ObjectIdentity = ObjectIdentity
tlpUpsAlarmCurrentBelowThreshold1 = _TlpUpsAlarmCurrentBelowThreshold1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 55, 1)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmCurrentBelowThreshold1.setStatus("current")
_TlpUpsAlarmCurrentBelowThreshold2_ObjectIdentity = ObjectIdentity
tlpUpsAlarmCurrentBelowThreshold2 = _TlpUpsAlarmCurrentBelowThreshold2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 55, 2)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmCurrentBelowThreshold2.setStatus("current")
_TlpUpsAlarmCurrentBelowThreshold3_ObjectIdentity = ObjectIdentity
tlpUpsAlarmCurrentBelowThreshold3 = _TlpUpsAlarmCurrentBelowThreshold3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 55, 3)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmCurrentBelowThreshold3.setStatus("current")
_TlpUpsAlarmCurrentBelowThreshold4_ObjectIdentity = ObjectIdentity
tlpUpsAlarmCurrentBelowThreshold4 = _TlpUpsAlarmCurrentBelowThreshold4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 55, 4)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmCurrentBelowThreshold4.setStatus("current")
_TlpUpsAlarmCurrentBelowThreshold5_ObjectIdentity = ObjectIdentity
tlpUpsAlarmCurrentBelowThreshold5 = _TlpUpsAlarmCurrentBelowThreshold5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 55, 5)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmCurrentBelowThreshold5.setStatus("current")
_TlpUpsAlarmCurrentBelowThreshold6_ObjectIdentity = ObjectIdentity
tlpUpsAlarmCurrentBelowThreshold6 = _TlpUpsAlarmCurrentBelowThreshold6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 55, 6)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmCurrentBelowThreshold6.setStatus("current")
_TlpPduAlarms_ObjectIdentity = ObjectIdentity
tlpPduAlarms = _TlpPduAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4)
)
_TlpPduAlarmLoadLevelAboveThreshold_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadLevelAboveThreshold = _TlpPduAlarmLoadLevelAboveThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 1)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadLevelAboveThreshold.setStatus("current")
_TlpPduAlarmInputBad_ObjectIdentity = ObjectIdentity
tlpPduAlarmInputBad = _TlpPduAlarmInputBad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 2)
)
if mibBuilder.loadTexts:
    tlpPduAlarmInputBad.setStatus("current")
_TlpPduAlarmOutputBad_ObjectIdentity = ObjectIdentity
tlpPduAlarmOutputBad = _TlpPduAlarmOutputBad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 3)
)
if mibBuilder.loadTexts:
    tlpPduAlarmOutputBad.setStatus("current")
_TlpPduAlarmOutputOverload_ObjectIdentity = ObjectIdentity
tlpPduAlarmOutputOverload = _TlpPduAlarmOutputOverload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 4)
)
if mibBuilder.loadTexts:
    tlpPduAlarmOutputOverload.setStatus("current")
_TlpPduAlarmOutputOff_ObjectIdentity = ObjectIdentity
tlpPduAlarmOutputOff = _TlpPduAlarmOutputOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 5)
)
if mibBuilder.loadTexts:
    tlpPduAlarmOutputOff.setStatus("current")
_TlpPduAlarmLoadOff_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff = _TlpPduAlarmLoadOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6)
)
_TlpPduAlarmLoadOff01_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff01 = _TlpPduAlarmLoadOff01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 1)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff01.setStatus("current")
_TlpPduAlarmLoadOff02_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff02 = _TlpPduAlarmLoadOff02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 2)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff02.setStatus("current")
_TlpPduAlarmLoadOff03_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff03 = _TlpPduAlarmLoadOff03_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 3)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff03.setStatus("current")
_TlpPduAlarmLoadOff04_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff04 = _TlpPduAlarmLoadOff04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 4)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff04.setStatus("current")
_TlpPduAlarmLoadOff05_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff05 = _TlpPduAlarmLoadOff05_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 5)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff05.setStatus("current")
_TlpPduAlarmLoadOff06_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff06 = _TlpPduAlarmLoadOff06_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 6)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff06.setStatus("current")
_TlpPduAlarmLoadOff07_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff07 = _TlpPduAlarmLoadOff07_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 7)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff07.setStatus("current")
_TlpPduAlarmLoadOff08_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff08 = _TlpPduAlarmLoadOff08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 8)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff08.setStatus("current")
_TlpPduAlarmLoadOff09_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff09 = _TlpPduAlarmLoadOff09_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 9)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff09.setStatus("current")
_TlpPduAlarmLoadOff10_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff10 = _TlpPduAlarmLoadOff10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 10)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff10.setStatus("current")
_TlpPduAlarmLoadOff11_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff11 = _TlpPduAlarmLoadOff11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 11)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff11.setStatus("current")
_TlpPduAlarmLoadOff12_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff12 = _TlpPduAlarmLoadOff12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 12)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff12.setStatus("current")
_TlpPduAlarmLoadOff13_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff13 = _TlpPduAlarmLoadOff13_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 13)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff13.setStatus("current")
_TlpPduAlarmLoadOff14_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff14 = _TlpPduAlarmLoadOff14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 14)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff14.setStatus("current")
_TlpPduAlarmLoadOff15_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff15 = _TlpPduAlarmLoadOff15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 15)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff15.setStatus("current")
_TlpPduAlarmLoadOff16_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff16 = _TlpPduAlarmLoadOff16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 16)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff16.setStatus("current")
_TlpPduAlarmLoadOff17_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff17 = _TlpPduAlarmLoadOff17_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 17)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff17.setStatus("current")
_TlpPduAlarmLoadOff18_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff18 = _TlpPduAlarmLoadOff18_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 18)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff18.setStatus("current")
_TlpPduAlarmLoadOff19_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff19 = _TlpPduAlarmLoadOff19_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 19)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff19.setStatus("current")
_TlpPduAlarmLoadOff20_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff20 = _TlpPduAlarmLoadOff20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 20)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff20.setStatus("current")
_TlpPduAlarmLoadOff21_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff21 = _TlpPduAlarmLoadOff21_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 21)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff21.setStatus("current")
_TlpPduAlarmLoadOff22_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff22 = _TlpPduAlarmLoadOff22_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 22)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff22.setStatus("current")
_TlpPduAlarmLoadOff23_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff23 = _TlpPduAlarmLoadOff23_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 23)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff23.setStatus("current")
_TlpPduAlarmLoadOff24_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff24 = _TlpPduAlarmLoadOff24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 24)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff24.setStatus("current")
_TlpPduAlarmLoadOff25_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff25 = _TlpPduAlarmLoadOff25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 25)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff25.setStatus("current")
_TlpPduAlarmLoadOff26_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff26 = _TlpPduAlarmLoadOff26_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 26)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff26.setStatus("current")
_TlpPduAlarmLoadOff27_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff27 = _TlpPduAlarmLoadOff27_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 27)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff27.setStatus("current")
_TlpPduAlarmLoadOff28_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff28 = _TlpPduAlarmLoadOff28_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 28)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff28.setStatus("current")
_TlpPduAlarmLoadOff29_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff29 = _TlpPduAlarmLoadOff29_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 29)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff29.setStatus("current")
_TlpPduAlarmLoadOff30_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff30 = _TlpPduAlarmLoadOff30_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 30)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff30.setStatus("current")
_TlpPduAlarmLoadOff31_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff31 = _TlpPduAlarmLoadOff31_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 31)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff31.setStatus("current")
_TlpPduAlarmLoadOff32_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff32 = _TlpPduAlarmLoadOff32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 32)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff32.setStatus("current")
_TlpPduAlarmLoadOff33_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff33 = _TlpPduAlarmLoadOff33_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 33)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff33.setStatus("current")
_TlpPduAlarmLoadOff34_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff34 = _TlpPduAlarmLoadOff34_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 34)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff34.setStatus("current")
_TlpPduAlarmLoadOff35_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff35 = _TlpPduAlarmLoadOff35_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 35)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff35.setStatus("current")
_TlpPduAlarmLoadOff36_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff36 = _TlpPduAlarmLoadOff36_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 36)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff36.setStatus("current")
_TlpPduAlarmLoadOff37_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff37 = _TlpPduAlarmLoadOff37_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 37)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff37.setStatus("current")
_TlpPduAlarmLoadOff38_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff38 = _TlpPduAlarmLoadOff38_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 38)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff38.setStatus("current")
_TlpPduAlarmLoadOff39_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff39 = _TlpPduAlarmLoadOff39_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 39)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff39.setStatus("current")
_TlpPduAlarmLoadOff40_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff40 = _TlpPduAlarmLoadOff40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 40)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff40.setStatus("current")
_TlpPduAlarmLoadOff41_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff41 = _TlpPduAlarmLoadOff41_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 41)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff41.setStatus("current")
_TlpPduAlarmLoadOff42_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff42 = _TlpPduAlarmLoadOff42_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 42)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff42.setStatus("current")
_TlpPduAlarmLoadOff43_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff43 = _TlpPduAlarmLoadOff43_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 43)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff43.setStatus("current")
_TlpPduAlarmLoadOff44_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff44 = _TlpPduAlarmLoadOff44_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 44)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff44.setStatus("current")
_TlpPduAlarmLoadOff45_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff45 = _TlpPduAlarmLoadOff45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 45)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff45.setStatus("current")
_TlpPduAlarmLoadOff46_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff46 = _TlpPduAlarmLoadOff46_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 46)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff46.setStatus("current")
_TlpPduAlarmLoadOff47_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff47 = _TlpPduAlarmLoadOff47_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 47)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff47.setStatus("current")
_TlpPduAlarmLoadOff48_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff48 = _TlpPduAlarmLoadOff48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 48)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff48.setStatus("current")
_TlpPduAlarmCircuitBreakerOpen_ObjectIdentity = ObjectIdentity
tlpPduAlarmCircuitBreakerOpen = _TlpPduAlarmCircuitBreakerOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 7)
)
_TlpPduAlarmCircuitBreakerOpen01_ObjectIdentity = ObjectIdentity
tlpPduAlarmCircuitBreakerOpen01 = _TlpPduAlarmCircuitBreakerOpen01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 7, 1)
)
if mibBuilder.loadTexts:
    tlpPduAlarmCircuitBreakerOpen01.setStatus("current")
_TlpPduAlarmCircuitBreakerOpen02_ObjectIdentity = ObjectIdentity
tlpPduAlarmCircuitBreakerOpen02 = _TlpPduAlarmCircuitBreakerOpen02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 7, 2)
)
if mibBuilder.loadTexts:
    tlpPduAlarmCircuitBreakerOpen02.setStatus("current")
_TlpPduAlarmCircuitBreakerOpen03_ObjectIdentity = ObjectIdentity
tlpPduAlarmCircuitBreakerOpen03 = _TlpPduAlarmCircuitBreakerOpen03_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 7, 3)
)
if mibBuilder.loadTexts:
    tlpPduAlarmCircuitBreakerOpen03.setStatus("current")
_TlpPduAlarmCircuitBreakerOpen04_ObjectIdentity = ObjectIdentity
tlpPduAlarmCircuitBreakerOpen04 = _TlpPduAlarmCircuitBreakerOpen04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 7, 4)
)
if mibBuilder.loadTexts:
    tlpPduAlarmCircuitBreakerOpen04.setStatus("current")
_TlpPduAlarmCircuitBreakerOpen05_ObjectIdentity = ObjectIdentity
tlpPduAlarmCircuitBreakerOpen05 = _TlpPduAlarmCircuitBreakerOpen05_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 7, 5)
)
if mibBuilder.loadTexts:
    tlpPduAlarmCircuitBreakerOpen05.setStatus("current")
_TlpPduAlarmCircuitBreakerOpen06_ObjectIdentity = ObjectIdentity
tlpPduAlarmCircuitBreakerOpen06 = _TlpPduAlarmCircuitBreakerOpen06_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 7, 6)
)
if mibBuilder.loadTexts:
    tlpPduAlarmCircuitBreakerOpen06.setStatus("current")
_TlpPduAlarmCurrentAboveThreshold_ObjectIdentity = ObjectIdentity
tlpPduAlarmCurrentAboveThreshold = _TlpPduAlarmCurrentAboveThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 8)
)
_TlpPduAlarmCurrentAboveThreshold1_ObjectIdentity = ObjectIdentity
tlpPduAlarmCurrentAboveThreshold1 = _TlpPduAlarmCurrentAboveThreshold1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 8, 1)
)
if mibBuilder.loadTexts:
    tlpPduAlarmCurrentAboveThreshold1.setStatus("current")
_TlpPduAlarmCurrentAboveThreshold2_ObjectIdentity = ObjectIdentity
tlpPduAlarmCurrentAboveThreshold2 = _TlpPduAlarmCurrentAboveThreshold2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 8, 2)
)
if mibBuilder.loadTexts:
    tlpPduAlarmCurrentAboveThreshold2.setStatus("current")
_TlpPduAlarmCurrentAboveThreshold3_ObjectIdentity = ObjectIdentity
tlpPduAlarmCurrentAboveThreshold3 = _TlpPduAlarmCurrentAboveThreshold3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 8, 3)
)
if mibBuilder.loadTexts:
    tlpPduAlarmCurrentAboveThreshold3.setStatus("current")
_TlpPduAlarmCurrentAboveThreshold4_ObjectIdentity = ObjectIdentity
tlpPduAlarmCurrentAboveThreshold4 = _TlpPduAlarmCurrentAboveThreshold4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 8, 4)
)
if mibBuilder.loadTexts:
    tlpPduAlarmCurrentAboveThreshold4.setStatus("current")
_TlpPduAlarmCurrentAboveThreshold5_ObjectIdentity = ObjectIdentity
tlpPduAlarmCurrentAboveThreshold5 = _TlpPduAlarmCurrentAboveThreshold5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 8, 5)
)
if mibBuilder.loadTexts:
    tlpPduAlarmCurrentAboveThreshold5.setStatus("current")
_TlpPduAlarmCurrentAboveThreshold6_ObjectIdentity = ObjectIdentity
tlpPduAlarmCurrentAboveThreshold6 = _TlpPduAlarmCurrentAboveThreshold6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 8, 6)
)
if mibBuilder.loadTexts:
    tlpPduAlarmCurrentAboveThreshold6.setStatus("current")
_TlpPduAlarmLoadsNotAllOn_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadsNotAllOn = _TlpPduAlarmLoadsNotAllOn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 9)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadsNotAllOn.setStatus("current")
_TlpPduAlarmLoadLevelBelowThreshold_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadLevelBelowThreshold = _TlpPduAlarmLoadLevelBelowThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 10)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadLevelBelowThreshold.setStatus("current")
_TlpPduAlarmCurrentBelowThreshold_ObjectIdentity = ObjectIdentity
tlpPduAlarmCurrentBelowThreshold = _TlpPduAlarmCurrentBelowThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 11)
)
_TlpPduAlarmCurrentBelowThreshold1_ObjectIdentity = ObjectIdentity
tlpPduAlarmCurrentBelowThreshold1 = _TlpPduAlarmCurrentBelowThreshold1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 11, 1)
)
if mibBuilder.loadTexts:
    tlpPduAlarmCurrentBelowThreshold1.setStatus("current")
_TlpPduAlarmCurrentBelowThreshold2_ObjectIdentity = ObjectIdentity
tlpPduAlarmCurrentBelowThreshold2 = _TlpPduAlarmCurrentBelowThreshold2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 11, 2)
)
if mibBuilder.loadTexts:
    tlpPduAlarmCurrentBelowThreshold2.setStatus("current")
_TlpPduAlarmCurrentBelowThreshold3_ObjectIdentity = ObjectIdentity
tlpPduAlarmCurrentBelowThreshold3 = _TlpPduAlarmCurrentBelowThreshold3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 11, 3)
)
if mibBuilder.loadTexts:
    tlpPduAlarmCurrentBelowThreshold3.setStatus("current")
_TlpPduAlarmCurrentBelowThreshold4_ObjectIdentity = ObjectIdentity
tlpPduAlarmCurrentBelowThreshold4 = _TlpPduAlarmCurrentBelowThreshold4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 11, 4)
)
if mibBuilder.loadTexts:
    tlpPduAlarmCurrentBelowThreshold4.setStatus("current")
_TlpPduAlarmCurrentBelowThreshold5_ObjectIdentity = ObjectIdentity
tlpPduAlarmCurrentBelowThreshold5 = _TlpPduAlarmCurrentBelowThreshold5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 11, 5)
)
if mibBuilder.loadTexts:
    tlpPduAlarmCurrentBelowThreshold5.setStatus("current")
_TlpPduAlarmCurrentBelowThreshold6_ObjectIdentity = ObjectIdentity
tlpPduAlarmCurrentBelowThreshold6 = _TlpPduAlarmCurrentBelowThreshold6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 11, 6)
)
if mibBuilder.loadTexts:
    tlpPduAlarmCurrentBelowThreshold6.setStatus("current")
_TlpPduAlarmThdOutOfRange_ObjectIdentity = ObjectIdentity
tlpPduAlarmThdOutOfRange = _TlpPduAlarmThdOutOfRange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 12)
)
if mibBuilder.loadTexts:
    tlpPduAlarmThdOutOfRange.setStatus("current")
_TlpPduAlarmGeneralFault_ObjectIdentity = ObjectIdentity
tlpPduAlarmGeneralFault = _TlpPduAlarmGeneralFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 13)
)
if mibBuilder.loadTexts:
    tlpPduAlarmGeneralFault.setStatus("current")
_TlpPduAlarmOutletOverCurrent_ObjectIdentity = ObjectIdentity
tlpPduAlarmOutletOverCurrent = _TlpPduAlarmOutletOverCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 14)
)
if mibBuilder.loadTexts:
    tlpPduAlarmOutletOverCurrent.setStatus("current")
_TlpEnvAlarms_ObjectIdentity = ObjectIdentity
tlpEnvAlarms = _TlpEnvAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 5)
)
_TlpEnvAlarmTemperatureBeyondLimits_ObjectIdentity = ObjectIdentity
tlpEnvAlarmTemperatureBeyondLimits = _TlpEnvAlarmTemperatureBeyondLimits_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 5, 1)
)
if mibBuilder.loadTexts:
    tlpEnvAlarmTemperatureBeyondLimits.setStatus("current")
_TlpEnvAlarmHumidityBeyondLimits_ObjectIdentity = ObjectIdentity
tlpEnvAlarmHumidityBeyondLimits = _TlpEnvAlarmHumidityBeyondLimits_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 5, 2)
)
if mibBuilder.loadTexts:
    tlpEnvAlarmHumidityBeyondLimits.setStatus("current")
_TlpEnvAlarmInputContact_ObjectIdentity = ObjectIdentity
tlpEnvAlarmInputContact = _TlpEnvAlarmInputContact_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 5, 3)
)
_TlpEnvAlarmInputContact01_ObjectIdentity = ObjectIdentity
tlpEnvAlarmInputContact01 = _TlpEnvAlarmInputContact01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 5, 3, 1)
)
if mibBuilder.loadTexts:
    tlpEnvAlarmInputContact01.setStatus("current")
_TlpEnvAlarmInputContact02_ObjectIdentity = ObjectIdentity
tlpEnvAlarmInputContact02 = _TlpEnvAlarmInputContact02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 5, 3, 2)
)
if mibBuilder.loadTexts:
    tlpEnvAlarmInputContact02.setStatus("current")
_TlpEnvAlarmInputContact03_ObjectIdentity = ObjectIdentity
tlpEnvAlarmInputContact03 = _TlpEnvAlarmInputContact03_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 5, 3, 3)
)
if mibBuilder.loadTexts:
    tlpEnvAlarmInputContact03.setStatus("current")
_TlpEnvAlarmInputContact04_ObjectIdentity = ObjectIdentity
tlpEnvAlarmInputContact04 = _TlpEnvAlarmInputContact04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 5, 3, 4)
)
if mibBuilder.loadTexts:
    tlpEnvAlarmInputContact04.setStatus("current")
_TlpEnvAlarmOutputContact_ObjectIdentity = ObjectIdentity
tlpEnvAlarmOutputContact = _TlpEnvAlarmOutputContact_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 5, 4)
)
_TlpEnvAlarmOutputContact01_ObjectIdentity = ObjectIdentity
tlpEnvAlarmOutputContact01 = _TlpEnvAlarmOutputContact01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 5, 4, 1)
)
if mibBuilder.loadTexts:
    tlpEnvAlarmOutputContact01.setStatus("current")
_TlpEnvAlarmOutputContact02_ObjectIdentity = ObjectIdentity
tlpEnvAlarmOutputContact02 = _TlpEnvAlarmOutputContact02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 5, 4, 2)
)
if mibBuilder.loadTexts:
    tlpEnvAlarmOutputContact02.setStatus("current")
_TlpEnvAlarmOutputContact03_ObjectIdentity = ObjectIdentity
tlpEnvAlarmOutputContact03 = _TlpEnvAlarmOutputContact03_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 5, 4, 3)
)
if mibBuilder.loadTexts:
    tlpEnvAlarmOutputContact03.setStatus("current")
_TlpEnvAlarmOutputContact04_ObjectIdentity = ObjectIdentity
tlpEnvAlarmOutputContact04 = _TlpEnvAlarmOutputContact04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 5, 4, 4)
)
if mibBuilder.loadTexts:
    tlpEnvAlarmOutputContact04.setStatus("current")
_TlpAtsAlarms_ObjectIdentity = ObjectIdentity
tlpAtsAlarms = _TlpAtsAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6)
)
_TlpAtsAlarmOutage_ObjectIdentity = ObjectIdentity
tlpAtsAlarmOutage = _TlpAtsAlarmOutage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 1)
)
_TlpAtsAlarmSource1Outage_ObjectIdentity = ObjectIdentity
tlpAtsAlarmSource1Outage = _TlpAtsAlarmSource1Outage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 1, 1)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmSource1Outage.setStatus("current")
_TlpAtsAlarmSource2Outage_ObjectIdentity = ObjectIdentity
tlpAtsAlarmSource2Outage = _TlpAtsAlarmSource2Outage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 1, 2)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmSource2Outage.setStatus("current")
_TlpAtsAlarmTemperature_ObjectIdentity = ObjectIdentity
tlpAtsAlarmTemperature = _TlpAtsAlarmTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 2)
)
_TlpAtsAlarmDeviceTemperature_ObjectIdentity = ObjectIdentity
tlpAtsAlarmDeviceTemperature = _TlpAtsAlarmDeviceTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 2, 1)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmDeviceTemperature.setStatus("current")
_TlpAtsAlarmSource1Temperature_ObjectIdentity = ObjectIdentity
tlpAtsAlarmSource1Temperature = _TlpAtsAlarmSource1Temperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 2, 2)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmSource1Temperature.setStatus("current")
_TlpAtsAlarmSource2Temperature_ObjectIdentity = ObjectIdentity
tlpAtsAlarmSource2Temperature = _TlpAtsAlarmSource2Temperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 2, 3)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmSource2Temperature.setStatus("current")
_TlpAtsAlarmLoadLevelAboveThreshold_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadLevelAboveThreshold = _TlpAtsAlarmLoadLevelAboveThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 3)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadLevelAboveThreshold.setStatus("current")
_TlpAtsAlarmInputBad_ObjectIdentity = ObjectIdentity
tlpAtsAlarmInputBad = _TlpAtsAlarmInputBad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 4)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmInputBad.setStatus("current")
_TlpAtsAlarmOutputBad_ObjectIdentity = ObjectIdentity
tlpAtsAlarmOutputBad = _TlpAtsAlarmOutputBad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 5)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmOutputBad.setStatus("current")
_TlpAtsAlarmOutputOverload_ObjectIdentity = ObjectIdentity
tlpAtsAlarmOutputOverload = _TlpAtsAlarmOutputOverload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 6)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmOutputOverload.setStatus("current")
_TlpAtsAlarmOutputOff_ObjectIdentity = ObjectIdentity
tlpAtsAlarmOutputOff = _TlpAtsAlarmOutputOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 7)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmOutputOff.setStatus("current")
_TlpAtsAlarmLoadOff_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff = _TlpAtsAlarmLoadOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8)
)
_TlpAtsAlarmLoadOff01_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff01 = _TlpAtsAlarmLoadOff01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 1)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff01.setStatus("current")
_TlpAtsAlarmLoadOff02_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff02 = _TlpAtsAlarmLoadOff02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 2)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff02.setStatus("current")
_TlpAtsAlarmLoadOff03_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff03 = _TlpAtsAlarmLoadOff03_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 3)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff03.setStatus("current")
_TlpAtsAlarmLoadOff04_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff04 = _TlpAtsAlarmLoadOff04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 4)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff04.setStatus("current")
_TlpAtsAlarmLoadOff05_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff05 = _TlpAtsAlarmLoadOff05_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 5)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff05.setStatus("current")
_TlpAtsAlarmLoadOff06_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff06 = _TlpAtsAlarmLoadOff06_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 6)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff06.setStatus("current")
_TlpAtsAlarmLoadOff07_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff07 = _TlpAtsAlarmLoadOff07_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 7)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff07.setStatus("current")
_TlpAtsAlarmLoadOff08_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff08 = _TlpAtsAlarmLoadOff08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 8)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff08.setStatus("current")
_TlpAtsAlarmLoadOff09_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff09 = _TlpAtsAlarmLoadOff09_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 9)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff09.setStatus("current")
_TlpAtsAlarmLoadOff10_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff10 = _TlpAtsAlarmLoadOff10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 10)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff10.setStatus("current")
_TlpAtsAlarmLoadOff11_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff11 = _TlpAtsAlarmLoadOff11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 11)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff11.setStatus("current")
_TlpAtsAlarmLoadOff12_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff12 = _TlpAtsAlarmLoadOff12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 12)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff12.setStatus("current")
_TlpAtsAlarmLoadOff13_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff13 = _TlpAtsAlarmLoadOff13_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 13)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff13.setStatus("current")
_TlpAtsAlarmLoadOff14_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff14 = _TlpAtsAlarmLoadOff14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 14)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff14.setStatus("current")
_TlpAtsAlarmLoadOff15_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff15 = _TlpAtsAlarmLoadOff15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 15)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff15.setStatus("current")
_TlpAtsAlarmLoadOff16_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff16 = _TlpAtsAlarmLoadOff16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 16)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff16.setStatus("current")
_TlpAtsAlarmLoadOff17_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff17 = _TlpAtsAlarmLoadOff17_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 17)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff17.setStatus("current")
_TlpAtsAlarmLoadOff18_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff18 = _TlpAtsAlarmLoadOff18_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 18)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff18.setStatus("current")
_TlpAtsAlarmLoadOff19_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff19 = _TlpAtsAlarmLoadOff19_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 19)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff19.setStatus("current")
_TlpAtsAlarmLoadOff20_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff20 = _TlpAtsAlarmLoadOff20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 20)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff20.setStatus("current")
_TlpAtsAlarmLoadOff21_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff21 = _TlpAtsAlarmLoadOff21_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 21)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff21.setStatus("current")
_TlpAtsAlarmLoadOff22_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff22 = _TlpAtsAlarmLoadOff22_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 22)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff22.setStatus("current")
_TlpAtsAlarmLoadOff23_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff23 = _TlpAtsAlarmLoadOff23_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 23)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff23.setStatus("current")
_TlpAtsAlarmLoadOff24_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff24 = _TlpAtsAlarmLoadOff24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 24)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff24.setStatus("current")
_TlpAtsAlarmLoadOff25_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff25 = _TlpAtsAlarmLoadOff25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 25)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff25.setStatus("current")
_TlpAtsAlarmLoadOff26_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff26 = _TlpAtsAlarmLoadOff26_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 26)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff26.setStatus("current")
_TlpAtsAlarmLoadOff27_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff27 = _TlpAtsAlarmLoadOff27_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 27)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff27.setStatus("current")
_TlpAtsAlarmLoadOff28_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff28 = _TlpAtsAlarmLoadOff28_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 28)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff28.setStatus("current")
_TlpAtsAlarmLoadOff29_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff29 = _TlpAtsAlarmLoadOff29_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 29)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff29.setStatus("current")
_TlpAtsAlarmLoadOff30_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff30 = _TlpAtsAlarmLoadOff30_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 30)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff30.setStatus("current")
_TlpAtsAlarmLoadOff31_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff31 = _TlpAtsAlarmLoadOff31_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 31)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff31.setStatus("current")
_TlpAtsAlarmLoadOff32_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff32 = _TlpAtsAlarmLoadOff32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 32)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff32.setStatus("current")
_TlpAtsAlarmLoadOff33_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff33 = _TlpAtsAlarmLoadOff33_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 33)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff33.setStatus("current")
_TlpAtsAlarmLoadOff34_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff34 = _TlpAtsAlarmLoadOff34_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 34)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff34.setStatus("current")
_TlpAtsAlarmLoadOff35_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff35 = _TlpAtsAlarmLoadOff35_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 35)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff35.setStatus("current")
_TlpAtsAlarmLoadOff36_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff36 = _TlpAtsAlarmLoadOff36_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 36)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff36.setStatus("current")
_TlpAtsAlarmLoadOff37_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff37 = _TlpAtsAlarmLoadOff37_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 37)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff37.setStatus("current")
_TlpAtsAlarmLoadOff38_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff38 = _TlpAtsAlarmLoadOff38_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 38)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff38.setStatus("current")
_TlpAtsAlarmLoadOff39_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff39 = _TlpAtsAlarmLoadOff39_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 39)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff39.setStatus("current")
_TlpAtsAlarmLoadOff40_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff40 = _TlpAtsAlarmLoadOff40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 40)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff40.setStatus("current")
_TlpAtsAlarmLoadOff41_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff41 = _TlpAtsAlarmLoadOff41_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 41)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff41.setStatus("current")
_TlpAtsAlarmLoadOff42_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff42 = _TlpAtsAlarmLoadOff42_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 42)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff42.setStatus("current")
_TlpAtsAlarmLoadOff43_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff43 = _TlpAtsAlarmLoadOff43_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 43)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff43.setStatus("current")
_TlpAtsAlarmLoadOff44_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff44 = _TlpAtsAlarmLoadOff44_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 44)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff44.setStatus("current")
_TlpAtsAlarmLoadOff45_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff45 = _TlpAtsAlarmLoadOff45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 45)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff45.setStatus("current")
_TlpAtsAlarmLoadOff46_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff46 = _TlpAtsAlarmLoadOff46_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 46)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff46.setStatus("current")
_TlpAtsAlarmLoadOff47_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff47 = _TlpAtsAlarmLoadOff47_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 47)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff47.setStatus("current")
_TlpAtsAlarmLoadOff48_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff48 = _TlpAtsAlarmLoadOff48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 48)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff48.setStatus("current")
_TlpAtsAlarmCircuitBreakerOpen_ObjectIdentity = ObjectIdentity
tlpAtsAlarmCircuitBreakerOpen = _TlpAtsAlarmCircuitBreakerOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 9)
)
_TlpAtsAlarmCircuitBreakerOpen01_ObjectIdentity = ObjectIdentity
tlpAtsAlarmCircuitBreakerOpen01 = _TlpAtsAlarmCircuitBreakerOpen01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 9, 1)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmCircuitBreakerOpen01.setStatus("current")
_TlpAtsAlarmCircuitBreakerOpen02_ObjectIdentity = ObjectIdentity
tlpAtsAlarmCircuitBreakerOpen02 = _TlpAtsAlarmCircuitBreakerOpen02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 9, 2)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmCircuitBreakerOpen02.setStatus("current")
_TlpAtsAlarmCircuitBreakerOpen03_ObjectIdentity = ObjectIdentity
tlpAtsAlarmCircuitBreakerOpen03 = _TlpAtsAlarmCircuitBreakerOpen03_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 9, 3)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmCircuitBreakerOpen03.setStatus("current")
_TlpAtsAlarmCircuitBreakerOpen04_ObjectIdentity = ObjectIdentity
tlpAtsAlarmCircuitBreakerOpen04 = _TlpAtsAlarmCircuitBreakerOpen04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 9, 4)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmCircuitBreakerOpen04.setStatus("current")
_TlpAtsAlarmCircuitBreakerOpen05_ObjectIdentity = ObjectIdentity
tlpAtsAlarmCircuitBreakerOpen05 = _TlpAtsAlarmCircuitBreakerOpen05_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 9, 5)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmCircuitBreakerOpen05.setStatus("current")
_TlpAtsAlarmCircuitBreakerOpen06_ObjectIdentity = ObjectIdentity
tlpAtsAlarmCircuitBreakerOpen06 = _TlpAtsAlarmCircuitBreakerOpen06_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 9, 6)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmCircuitBreakerOpen06.setStatus("current")
_TlpAtsAlarmCurrentAboveThreshold_ObjectIdentity = ObjectIdentity
tlpAtsAlarmCurrentAboveThreshold = _TlpAtsAlarmCurrentAboveThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 10)
)
_TlpAtsAlarmCurrentAboveThreshold1_ObjectIdentity = ObjectIdentity
tlpAtsAlarmCurrentAboveThreshold1 = _TlpAtsAlarmCurrentAboveThreshold1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 10, 1)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmCurrentAboveThreshold1.setStatus("current")
_TlpAtsAlarmCurrentAboveThreshold2_ObjectIdentity = ObjectIdentity
tlpAtsAlarmCurrentAboveThreshold2 = _TlpAtsAlarmCurrentAboveThreshold2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 10, 2)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmCurrentAboveThreshold2.setStatus("current")
_TlpAtsAlarmCurrentAboveThreshold3_ObjectIdentity = ObjectIdentity
tlpAtsAlarmCurrentAboveThreshold3 = _TlpAtsAlarmCurrentAboveThreshold3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 10, 3)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmCurrentAboveThreshold3.setStatus("current")
_TlpAtsAlarmCurrentAboveThreshold4_ObjectIdentity = ObjectIdentity
tlpAtsAlarmCurrentAboveThreshold4 = _TlpAtsAlarmCurrentAboveThreshold4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 10, 4)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmCurrentAboveThreshold4.setStatus("current")
_TlpAtsAlarmCurrentAboveThreshold5_ObjectIdentity = ObjectIdentity
tlpAtsAlarmCurrentAboveThreshold5 = _TlpAtsAlarmCurrentAboveThreshold5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 10, 5)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmCurrentAboveThreshold5.setStatus("current")
_TlpAtsAlarmCurrentAboveThreshold6_ObjectIdentity = ObjectIdentity
tlpAtsAlarmCurrentAboveThreshold6 = _TlpAtsAlarmCurrentAboveThreshold6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 10, 6)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmCurrentAboveThreshold6.setStatus("current")
_TlpAtsAlarmLoadsNotAllOn_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadsNotAllOn = _TlpAtsAlarmLoadsNotAllOn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 11)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadsNotAllOn.setStatus("current")
_TlpAtsAlarmGeneralFault_ObjectIdentity = ObjectIdentity
tlpAtsAlarmGeneralFault = _TlpAtsAlarmGeneralFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 12)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmGeneralFault.setStatus("current")
_TlpAtsAlarmVoltage_ObjectIdentity = ObjectIdentity
tlpAtsAlarmVoltage = _TlpAtsAlarmVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 13)
)
_TlpAtsAlarmOverVoltage_ObjectIdentity = ObjectIdentity
tlpAtsAlarmOverVoltage = _TlpAtsAlarmOverVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 13, 1)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmOverVoltage.setStatus("current")
_TlpAtsAlarmSource1OverVoltage_ObjectIdentity = ObjectIdentity
tlpAtsAlarmSource1OverVoltage = _TlpAtsAlarmSource1OverVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 13, 2)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmSource1OverVoltage.setStatus("current")
_TlpAtsAlarmSource2OverVoltage_ObjectIdentity = ObjectIdentity
tlpAtsAlarmSource2OverVoltage = _TlpAtsAlarmSource2OverVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 13, 3)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmSource2OverVoltage.setStatus("current")
_TlpAtsAlarmFrequency_ObjectIdentity = ObjectIdentity
tlpAtsAlarmFrequency = _TlpAtsAlarmFrequency_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 14)
)
_TlpAtsAlarmSource1InvalidFrequency_ObjectIdentity = ObjectIdentity
tlpAtsAlarmSource1InvalidFrequency = _TlpAtsAlarmSource1InvalidFrequency_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 14, 1)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmSource1InvalidFrequency.setStatus("current")
_TlpAtsAlarmSource2InvalidFrequency_ObjectIdentity = ObjectIdentity
tlpAtsAlarmSource2InvalidFrequency = _TlpAtsAlarmSource2InvalidFrequency_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 14, 2)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmSource2InvalidFrequency.setStatus("current")
_TlpAtsAlarmLoadLevelBelowThreshold_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadLevelBelowThreshold = _TlpAtsAlarmLoadLevelBelowThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 15)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadLevelBelowThreshold.setStatus("current")
_TlpAtsAlarmCurrentBelowThreshold_ObjectIdentity = ObjectIdentity
tlpAtsAlarmCurrentBelowThreshold = _TlpAtsAlarmCurrentBelowThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 16)
)
_TlpAtsAlarmCurrentBelowThreshold1_ObjectIdentity = ObjectIdentity
tlpAtsAlarmCurrentBelowThreshold1 = _TlpAtsAlarmCurrentBelowThreshold1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 16, 1)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmCurrentBelowThreshold1.setStatus("current")
_TlpAtsAlarmCurrentBelowThreshold2_ObjectIdentity = ObjectIdentity
tlpAtsAlarmCurrentBelowThreshold2 = _TlpAtsAlarmCurrentBelowThreshold2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 16, 2)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmCurrentBelowThreshold2.setStatus("current")
_TlpAtsAlarmCurrentBelowThreshold3_ObjectIdentity = ObjectIdentity
tlpAtsAlarmCurrentBelowThreshold3 = _TlpAtsAlarmCurrentBelowThreshold3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 16, 3)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmCurrentBelowThreshold3.setStatus("current")
_TlpAtsAlarmCurrentBelowThreshold4_ObjectIdentity = ObjectIdentity
tlpAtsAlarmCurrentBelowThreshold4 = _TlpAtsAlarmCurrentBelowThreshold4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 16, 4)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmCurrentBelowThreshold4.setStatus("current")
_TlpAtsAlarmCurrentBelowThreshold5_ObjectIdentity = ObjectIdentity
tlpAtsAlarmCurrentBelowThreshold5 = _TlpAtsAlarmCurrentBelowThreshold5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 16, 5)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmCurrentBelowThreshold5.setStatus("current")
_TlpAtsAlarmCurrentBelowThreshold6_ObjectIdentity = ObjectIdentity
tlpAtsAlarmCurrentBelowThreshold6 = _TlpAtsAlarmCurrentBelowThreshold6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 16, 6)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmCurrentBelowThreshold6.setStatus("current")
_TlpAtsAlarmThdOutOfRange_ObjectIdentity = ObjectIdentity
tlpAtsAlarmThdOutOfRange = _TlpAtsAlarmThdOutOfRange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 17)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmThdOutOfRange.setStatus("current")
_TlpAtsAlarmOutletOverCurrent_ObjectIdentity = ObjectIdentity
tlpAtsAlarmOutletOverCurrent = _TlpAtsAlarmOutletOverCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 18)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmOutletOverCurrent.setStatus("current")
_TlpCoolingAlarms_ObjectIdentity = ObjectIdentity
tlpCoolingAlarms = _TlpCoolingAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7)
)
_TlpCoolingAlarmSupplyAirSensorFault_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmSupplyAirSensorFault = _TlpCoolingAlarmSupplyAirSensorFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 1)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmSupplyAirSensorFault.setStatus("current")
_TlpCoolingAlarmReturnAirSensorFault_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmReturnAirSensorFault = _TlpCoolingAlarmReturnAirSensorFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 2)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmReturnAirSensorFault.setStatus("current")
_TlpCoolingAlarmCondenserInletAirSensorFault_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmCondenserInletAirSensorFault = _TlpCoolingAlarmCondenserInletAirSensorFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 3)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmCondenserInletAirSensorFault.setStatus("current")
_TlpCoolingAlarmCondenserOutletAirSensorFault_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmCondenserOutletAirSensorFault = _TlpCoolingAlarmCondenserOutletAirSensorFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 4)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmCondenserOutletAirSensorFault.setStatus("current")
_TlpCoolingAlarmSuctionTemperatureSensorFault_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmSuctionTemperatureSensorFault = _TlpCoolingAlarmSuctionTemperatureSensorFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 5)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmSuctionTemperatureSensorFault.setStatus("current")
_TlpCoolingAlarmEvaporatorTemperatureSensorFault_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmEvaporatorTemperatureSensorFault = _TlpCoolingAlarmEvaporatorTemperatureSensorFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 6)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmEvaporatorTemperatureSensorFault.setStatus("current")
_TlpCoolingAlarmAirFilterClogged_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmAirFilterClogged = _TlpCoolingAlarmAirFilterClogged_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 7)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmAirFilterClogged.setStatus("current")
_TlpCoolingAlarmAirFilterRunHoursViolation_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmAirFilterRunHoursViolation = _TlpCoolingAlarmAirFilterRunHoursViolation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 8)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmAirFilterRunHoursViolation.setStatus("current")
_TlpCoolingAlarmSuctionPressureSensorFault_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmSuctionPressureSensorFault = _TlpCoolingAlarmSuctionPressureSensorFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 9)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmSuctionPressureSensorFault.setStatus("current")
_TlpCoolingAlarmInverterCommunicationsFault_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmInverterCommunicationsFault = _TlpCoolingAlarmInverterCommunicationsFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 10)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmInverterCommunicationsFault.setStatus("current")
_TlpCoolingAlarmRemoteShutdownViaInputContact_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmRemoteShutdownViaInputContact = _TlpCoolingAlarmRemoteShutdownViaInputContact_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 11)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmRemoteShutdownViaInputContact.setStatus("current")
_TlpCoolingAlarmCondensatePumpFault_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmCondensatePumpFault = _TlpCoolingAlarmCondensatePumpFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 12)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmCondensatePumpFault.setStatus("current")
_TlpCoolingAlarmLowRefrigerantStartupFault_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmLowRefrigerantStartupFault = _TlpCoolingAlarmLowRefrigerantStartupFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 13)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmLowRefrigerantStartupFault.setStatus("current")
_TlpCoolingAlarmCondenserFanFault_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmCondenserFanFault = _TlpCoolingAlarmCondenserFanFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 14)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmCondenserFanFault.setStatus("current")
_TlpCoolingAlarmCondenserFailure_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmCondenserFailure = _TlpCoolingAlarmCondenserFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 15)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmCondenserFailure.setStatus("current")
_TlpCoolingAlarmEvaporatorCoolingFailure_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmEvaporatorCoolingFailure = _TlpCoolingAlarmEvaporatorCoolingFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 16)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmEvaporatorCoolingFailure.setStatus("current")
_TlpCoolingAlarmReturnAirTempHigh_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmReturnAirTempHigh = _TlpCoolingAlarmReturnAirTempHigh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 17)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmReturnAirTempHigh.setStatus("current")
_TlpCoolingAlarmSupplyAirTempHigh_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmSupplyAirTempHigh = _TlpCoolingAlarmSupplyAirTempHigh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 18)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmSupplyAirTempHigh.setStatus("current")
_TlpCoolingAlarmEvaporatorFailure_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmEvaporatorFailure = _TlpCoolingAlarmEvaporatorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 19)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmEvaporatorFailure.setStatus("current")
_TlpCoolingAlarmEvaporatorFreezeUp_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmEvaporatorFreezeUp = _TlpCoolingAlarmEvaporatorFreezeUp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 20)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmEvaporatorFreezeUp.setStatus("current")
_TlpCoolingAlarmDischargePressureHigh_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmDischargePressureHigh = _TlpCoolingAlarmDischargePressureHigh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 21)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmDischargePressureHigh.setStatus("current")
_TlpCoolingAlarmPressureGaugeFailure_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmPressureGaugeFailure = _TlpCoolingAlarmPressureGaugeFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 22)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmPressureGaugeFailure.setStatus("current")
_TlpCoolingAlarmDischargePressurePersistentHigh_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmDischargePressurePersistentHigh = _TlpCoolingAlarmDischargePressurePersistentHigh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 23)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmDischargePressurePersistentHigh.setStatus("current")
_TlpCoolingAlarmSuctionPressureLowStartFailure_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmSuctionPressureLowStartFailure = _TlpCoolingAlarmSuctionPressureLowStartFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 24)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmSuctionPressureLowStartFailure.setStatus("current")
_TlpCoolingAlarmSuctionPressureLow_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmSuctionPressureLow = _TlpCoolingAlarmSuctionPressureLow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 25)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmSuctionPressureLow.setStatus("current")
_TlpCoolingAlarmSuctionPressurePersistentLow_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmSuctionPressurePersistentLow = _TlpCoolingAlarmSuctionPressurePersistentLow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 26)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmSuctionPressurePersistentLow.setStatus("current")
_TlpCoolingAlarmStartupLinePressureImbalance_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmStartupLinePressureImbalance = _TlpCoolingAlarmStartupLinePressureImbalance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 27)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmStartupLinePressureImbalance.setStatus("current")
_TlpCoolingAlarmCompressorFailure_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmCompressorFailure = _TlpCoolingAlarmCompressorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 28)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmCompressorFailure.setStatus("current")
_TlpCoolingAlarmCurrentLimit_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmCurrentLimit = _TlpCoolingAlarmCurrentLimit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 29)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmCurrentLimit.setStatus("current")
_TlpCoolingAlarmWaterLeak_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmWaterLeak = _TlpCoolingAlarmWaterLeak_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 30)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmWaterLeak.setStatus("current")
_TlpCoolingAlarmFanUnderCurrent_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmFanUnderCurrent = _TlpCoolingAlarmFanUnderCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 31)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmFanUnderCurrent.setStatus("current")
_TlpCoolingAlarmFanOverCurrent_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmFanOverCurrent = _TlpCoolingAlarmFanOverCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 32)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmFanOverCurrent.setStatus("current")
_TlpCoolingAlarmDischargePressureSensorFault_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmDischargePressureSensorFault = _TlpCoolingAlarmDischargePressureSensorFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 33)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmDischargePressureSensorFault.setStatus("current")
_TlpCoolingAlarmWaterFull_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmWaterFull = _TlpCoolingAlarmWaterFull_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 34)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmWaterFull.setStatus("current")
_TlpCoolingAlarmAutoCoolingOn_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmAutoCoolingOn = _TlpCoolingAlarmAutoCoolingOn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 35)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmAutoCoolingOn.setStatus("current")
_TlpCoolingAlarmPowerButtonPressed_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmPowerButtonPressed = _TlpCoolingAlarmPowerButtonPressed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 36)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmPowerButtonPressed.setStatus("current")
_TlpCoolingAlarmDisconnectedFromDevice_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmDisconnectedFromDevice = _TlpCoolingAlarmDisconnectedFromDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 37)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmDisconnectedFromDevice.setStatus("current")
_TlpCoolingAlarmReturnAirTemperatureSensorFault_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmReturnAirTemperatureSensorFault = _TlpCoolingAlarmReturnAirTemperatureSensorFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 38)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmReturnAirTemperatureSensorFault.setStatus("current")
_TlpCoolingAlarmRemoteTemperatureSensorFault_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmRemoteTemperatureSensorFault = _TlpCoolingAlarmRemoteTemperatureSensorFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 39)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmRemoteTemperatureSensorFault.setStatus("current")
_TlpCoolingAlarmLowPressureSensorFault_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmLowPressureSensorFault = _TlpCoolingAlarmLowPressureSensorFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 40)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmLowPressureSensorFault.setStatus("current")
_TlpCoolingAlarmHighPressureSensorFault_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmHighPressureSensorFault = _TlpCoolingAlarmHighPressureSensorFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 41)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmHighPressureSensorFault.setStatus("current")
_TlpCoolingAlarmSentrytimerTimeout_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmSentrytimerTimeout = _TlpCoolingAlarmSentrytimerTimeout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 42)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmSentrytimerTimeout.setStatus("current")
_TlpKvmAlarms_ObjectIdentity = ObjectIdentity
tlpKvmAlarms = _TlpKvmAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 8)
)
_TlpRackTrackAlarms_ObjectIdentity = ObjectIdentity
tlpRackTrackAlarms = _TlpRackTrackAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 9)
)
_TlpSwitchAlarms_ObjectIdentity = ObjectIdentity
tlpSwitchAlarms = _TlpSwitchAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 10)
)
_TlpAlarmControl_ObjectIdentity = ObjectIdentity
tlpAlarmControl = _TlpAlarmControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 4)
)
_TlpAlarmControlTable_Object = MibTable
tlpAlarmControlTable = _TlpAlarmControlTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 4, 1)
)
if mibBuilder.loadTexts:
    tlpAlarmControlTable.setStatus("current")
_TlpAlarmControlEntry_Object = MibTableRow
tlpAlarmControlEntry = _TlpAlarmControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 4, 1, 1)
)
tlpAlarmControlEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpAlarmControlIndex"),
)
if mibBuilder.loadTexts:
    tlpAlarmControlEntry.setStatus("current")
_TlpAlarmControlIndex_Type = Unsigned32
_TlpAlarmControlIndex_Object = MibTableColumn
tlpAlarmControlIndex = _TlpAlarmControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 4, 1, 1, 1),
    _TlpAlarmControlIndex_Type()
)
tlpAlarmControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAlarmControlIndex.setStatus("current")
_TlpAlarmControlDescr_Type = ObjectIdentifier
_TlpAlarmControlDescr_Object = MibTableColumn
tlpAlarmControlDescr = _TlpAlarmControlDescr_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 4, 1, 1, 2),
    _TlpAlarmControlDescr_Type()
)
tlpAlarmControlDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAlarmControlDescr.setStatus("current")
_TlpAlarmControlDetail_Type = DisplayString
_TlpAlarmControlDetail_Object = MibTableColumn
tlpAlarmControlDetail = _TlpAlarmControlDetail_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 4, 1, 1, 3),
    _TlpAlarmControlDetail_Type()
)
tlpAlarmControlDetail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAlarmControlDetail.setStatus("current")


class _TlpAlarmControlSeverity_Type(Integer32):
    """Custom type tlpAlarmControlSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("warning", 2),
          ("info", 3))
    )


_TlpAlarmControlSeverity_Type.__name__ = "Integer32"
_TlpAlarmControlSeverity_Object = MibTableColumn
tlpAlarmControlSeverity = _TlpAlarmControlSeverity_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 4, 1, 1, 4),
    _TlpAlarmControlSeverity_Type()
)
tlpAlarmControlSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAlarmControlSeverity.setStatus("current")
_TlpNotify_ObjectIdentity = ObjectIdentity
tlpNotify = _TlpNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 4)
)
_TlpNotifications_ObjectIdentity = ObjectIdentity
tlpNotifications = _TlpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 1)
)
_TlpNotificationsEvent_ObjectIdentity = ObjectIdentity
tlpNotificationsEvent = _TlpNotificationsEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2)
)
_TlpNotificationsAgent_ObjectIdentity = ObjectIdentity
tlpNotificationsAgent = _TlpNotificationsAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 1)
)
_TlpNotificationsDevice_ObjectIdentity = ObjectIdentity
tlpNotificationsDevice = _TlpNotificationsDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 2)
)
_TlpNotificationsUps_ObjectIdentity = ObjectIdentity
tlpNotificationsUps = _TlpNotificationsUps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 3)
)
_TlpNotificationsPdu_ObjectIdentity = ObjectIdentity
tlpNotificationsPdu = _TlpNotificationsPdu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 4)
)
_TlpNotificationsEnvirosense_ObjectIdentity = ObjectIdentity
tlpNotificationsEnvirosense = _TlpNotificationsEnvirosense_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 5)
)
_TlpNotificationsAts_ObjectIdentity = ObjectIdentity
tlpNotificationsAts = _TlpNotificationsAts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 6)
)
_TlpNotificationsCooling_ObjectIdentity = ObjectIdentity
tlpNotificationsCooling = _TlpNotificationsCooling_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 7)
)
_TlpNotificationsKvm_ObjectIdentity = ObjectIdentity
tlpNotificationsKvm = _TlpNotificationsKvm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 8)
)
_TlpNotificationsRackTrack_ObjectIdentity = ObjectIdentity
tlpNotificationsRackTrack = _TlpNotificationsRackTrack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 9)
)
_TlpNotificationsSwitch_ObjectIdentity = ObjectIdentity
tlpNotificationsSwitch = _TlpNotificationsSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 10)
)
_TlpNotificationsEventParameters_ObjectIdentity = ObjectIdentity
tlpNotificationsEventParameters = _TlpNotificationsEventParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 3)
)
_TlpNotifyEventTableRef_Type = ObjectIdentifier
_TlpNotifyEventTableRef_Object = MibScalar
tlpNotifyEventTableRef = _TlpNotifyEventTableRef_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 3, 1),
    _TlpNotifyEventTableRef_Type()
)
tlpNotifyEventTableRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpNotifyEventTableRef.setStatus("current")
_TlpNotifyEventTableRowRef_Type = ObjectIdentifier
_TlpNotifyEventTableRowRef_Object = MibScalar
tlpNotifyEventTableRowRef = _TlpNotifyEventTableRowRef_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 3, 2),
    _TlpNotifyEventTableRowRef_Type()
)
tlpNotifyEventTableRowRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpNotifyEventTableRowRef.setStatus("current")

# Managed Objects groups


# Notification objects

tlpNotificationsAlarmEntryAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 1, 1)
)
tlpNotificationsAlarmEntryAdded.setObjects(
      *(("TRIPPLITE-PRODUCTS", "tlpAlarmId"),
        ("TRIPPLITE-PRODUCTS", "tlpAlarmDescr"),
        ("TRIPPLITE-PRODUCTS", "tlpAlarmTime"),
        ("TRIPPLITE-PRODUCTS", "tlpAlarmTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpAlarmTableRowRef"),
        ("TRIPPLITE-PRODUCTS", "tlpAlarmDetail"),
        ("TRIPPLITE-PRODUCTS", "tlpAlarmType"))
)
if mibBuilder.loadTexts:
    tlpNotificationsAlarmEntryAdded.setStatus(
        "current"
    )

tlpNotificationsAlarmEntryRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 1, 2)
)
tlpNotificationsAlarmEntryRemoved.setObjects(
      *(("TRIPPLITE-PRODUCTS", "tlpAlarmId"),
        ("TRIPPLITE-PRODUCTS", "tlpAlarmDescr"),
        ("TRIPPLITE-PRODUCTS", "tlpAlarmTime"),
        ("TRIPPLITE-PRODUCTS", "tlpAlarmTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpAlarmTableRowRef"),
        ("TRIPPLITE-PRODUCTS", "tlpAlarmDetail"),
        ("TRIPPLITE-PRODUCTS", "tlpAlarmType"))
)
if mibBuilder.loadTexts:
    tlpNotificationsAlarmEntryRemoved.setStatus(
        "current"
    )

tlpNotifySystemStartup = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 1, 3)
)
if mibBuilder.loadTexts:
    tlpNotifySystemStartup.setStatus(
        "current"
    )

tlpNotifySystemShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 1, 4)
)
if mibBuilder.loadTexts:
    tlpNotifySystemShutdown.setStatus(
        "current"
    )

tlpNotifySystemUpdate = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 1, 5)
)
if mibBuilder.loadTexts:
    tlpNotifySystemUpdate.setStatus(
        "current"
    )

tlpNotifyTest = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 1, 6)
)
if mibBuilder.loadTexts:
    tlpNotifyTest.setStatus(
        "current"
    )

tlpNotificationsDeviceInternalFirmwareFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 2, 1)
)
tlpNotificationsDeviceInternalFirmwareFault.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsDeviceInternalFirmwareFault.setStatus(
        "current"
    )

tlpNotificationsDeviceInternalHardwareFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 2, 2)
)
tlpNotificationsDeviceInternalHardwareFault.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsDeviceInternalHardwareFault.setStatus(
        "current"
    )

tlpNotificationsDeviceConfigurationChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 2, 3)
)
tlpNotificationsDeviceConfigurationChange.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsDeviceConfigurationChange.setStatus(
        "current"
    )

tlpNotificationsDeviceFirmwareUpdate = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 2, 4)
)
tlpNotificationsDeviceFirmwareUpdate.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsDeviceFirmwareUpdate.setStatus(
        "current"
    )

tlpNotificationsDeviceMicrocontrollerReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 2, 5)
)
tlpNotificationsDeviceMicrocontrollerReset.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsDeviceMicrocontrollerReset.setStatus(
        "current"
    )

tlpNotificationsDeviceSystemInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 2, 6)
)
tlpNotificationsDeviceSystemInformation.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsDeviceSystemInformation.setStatus(
        "current"
    )

tlpNotificationsDeviceNvrChecksumMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 2, 7)
)
tlpNotificationsDeviceNvrChecksumMismatch.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsDeviceNvrChecksumMismatch.setStatus(
        "current"
    )

tlpNotificationsDeviceUsbCommunicationsEstablished = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 2, 8)
)
tlpNotificationsDeviceUsbCommunicationsEstablished.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsDeviceUsbCommunicationsEstablished.setStatus(
        "current"
    )

tlpNotificationsDeviceUsbCommunicationsLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 2, 9)
)
tlpNotificationsDeviceUsbCommunicationsLost.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsDeviceUsbCommunicationsLost.setStatus(
        "current"
    )

tlpNotificationsDevicePowerSupplyShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 2, 10)
)
tlpNotificationsDevicePowerSupplyShutdown.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsDevicePowerSupplyShutdown.setStatus(
        "current"
    )

tlpNotificationsDeviceOverLoadShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 2, 11)
)
tlpNotificationsDeviceOverLoadShutdown.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsDeviceOverLoadShutdown.setStatus(
        "current"
    )

tlpNotificationsDeviceCurrentLimitShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 2, 12)
)
tlpNotificationsDeviceCurrentLimitShutdown.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsDeviceCurrentLimitShutdown.setStatus(
        "current"
    )

tlpNotificationsDeviceOverTemperatureShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 2, 13)
)
tlpNotificationsDeviceOverTemperatureShutdown.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsDeviceOverTemperatureShutdown.setStatus(
        "current"
    )

tlpNotificationsDeviceModeTransitionTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 2, 14)
)
tlpNotificationsDeviceModeTransitionTimeout.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsDeviceModeTransitionTimeout.setStatus(
        "current"
    )

tlpNotificationsDeviceFailedModeTransitionToIdle = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 2, 15)
)
tlpNotificationsDeviceFailedModeTransitionToIdle.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsDeviceFailedModeTransitionToIdle.setStatus(
        "current"
    )

tlpNotificationsDeviceInternalCommunicationsLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 2, 16)
)
tlpNotificationsDeviceInternalCommunicationsLost.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsDeviceInternalCommunicationsLost.setStatus(
        "current"
    )

tlpNotificationsDeviceAcknowledgeFaults = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 2, 17)
)
tlpNotificationsDeviceAcknowledgeFaults.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsDeviceAcknowledgeFaults.setStatus(
        "current"
    )

tlpNotificationsDeviceTransferToRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 2, 18)
)
tlpNotificationsDeviceTransferToRestart.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsDeviceTransferToRestart.setStatus(
        "current"
    )

tlpNotificationsDeviceTransferToWatchdogRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 2, 19)
)
tlpNotificationsDeviceTransferToWatchdogRestart.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsDeviceTransferToWatchdogRestart.setStatus(
        "current"
    )

tlpNotificationsDeviceTransferToLatchedIdle = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 2, 20)
)
tlpNotificationsDeviceTransferToLatchedIdle.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsDeviceTransferToLatchedIdle.setStatus(
        "current"
    )

tlpNotificationsDeviceTransferToLatchedStandby = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 2, 21)
)
tlpNotificationsDeviceTransferToLatchedStandby.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsDeviceTransferToLatchedStandby.setStatus(
        "current"
    )

tlpNotificationsDeviceTransferToLatchedLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 2, 22)
)
tlpNotificationsDeviceTransferToLatchedLine.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsDeviceTransferToLatchedLine.setStatus(
        "current"
    )

tlpNotificationsDeviceFailSafeClockMonitorEngaged = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 2, 23)
)
tlpNotificationsDeviceFailSafeClockMonitorEngaged.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsDeviceFailSafeClockMonitorEngaged.setStatus(
        "current"
    )

tlpNotificationsDeviceTransferToIdle = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 2, 24)
)
tlpNotificationsDeviceTransferToIdle.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsDeviceTransferToIdle.setStatus(
        "current"
    )

tlpNotificationsDeviceVoutUnderVoltageShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 2, 25)
)
tlpNotificationsDeviceVoutUnderVoltageShutdown.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsDeviceVoutUnderVoltageShutdown.setStatus(
        "current"
    )

tlpNotificationsDeviceVoutOverVoltageShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 2, 26)
)
tlpNotificationsDeviceVoutOverVoltageShutdown.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsDeviceVoutOverVoltageShutdown.setStatus(
        "current"
    )

tlpNotificationsDeviceRtosFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 2, 27)
)
tlpNotificationsDeviceRtosFault.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsDeviceRtosFault.setStatus(
        "current"
    )

tlpNotificationsDeviceCriticalNvrValuesBlank = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 2, 28)
)
tlpNotificationsDeviceCriticalNvrValuesBlank.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsDeviceCriticalNvrValuesBlank.setStatus(
        "current"
    )

tlpNotificationsDeviceOutputOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 2, 29)
)
tlpNotificationsDeviceOutputOff.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsDeviceOutputOff.setStatus(
        "current"
    )

tlpNotificationsDeviceStartup = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 2, 30)
)
tlpNotificationsDeviceStartup.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsDeviceStartup.setStatus(
        "current"
    )

tlpNotificationsDeviceEpo = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 2, 31)
)
tlpNotificationsDeviceEpo.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsDeviceEpo.setStatus(
        "current"
    )

tlpNotificationsDeviceFirmwareMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 2, 32)
)
tlpNotificationsDeviceFirmwareMismatch.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsDeviceFirmwareMismatch.setStatus(
        "current"
    )

tlpNotificationsDeviceOverloadRelease = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 2, 33)
)
tlpNotificationsDeviceOverloadRelease.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsDeviceOverloadRelease.setStatus(
        "current"
    )

tlpNotificationsDeviceTransferToLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 2, 34)
)
tlpNotificationsDeviceTransferToLine.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsDeviceTransferToLine.setStatus(
        "current"
    )

tlpNotificationsDeviceAcFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 2, 35)
)
tlpNotificationsDeviceAcFailure.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsDeviceAcFailure.setStatus(
        "current"
    )

tlpNotificationsDeviceSiteWiringFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 2, 36)
)
tlpNotificationsDeviceSiteWiringFault.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsDeviceSiteWiringFault.setStatus(
        "current"
    )

tlpNotificationsDeviceEmergencyShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 2, 37)
)
tlpNotificationsDeviceEmergencyShutdown.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsDeviceEmergencyShutdown.setStatus(
        "current"
    )

tlpNotificationsDeviceCircuitBreakerOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 2, 38)
)
tlpNotificationsDeviceCircuitBreakerOpen.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsDeviceCircuitBreakerOpen.setStatus(
        "current"
    )

tlpNotificationsDeviceSupplyMonitorInterrupt = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 2, 39)
)
tlpNotificationsDeviceSupplyMonitorInterrupt.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsDeviceSupplyMonitorInterrupt.setStatus(
        "current"
    )

tlpNotificationsDeviceSystemTickTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 2, 40)
)
tlpNotificationsDeviceSystemTickTimeout.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsDeviceSystemTickTimeout.setStatus(
        "current"
    )

tlpNotificationsDeviceRelayInUnexpectedState = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 2, 41)
)
tlpNotificationsDeviceRelayInUnexpectedState.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsDeviceRelayInUnexpectedState.setStatus(
        "current"
    )

tlpNotificationsDeviceEepromQueueOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 2, 42)
)
tlpNotificationsDeviceEepromQueueOverflow.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsDeviceEepromQueueOverflow.setStatus(
        "current"
    )

tlpNotificationsDeviceEepromWriteFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 2, 43)
)
tlpNotificationsDeviceEepromWriteFault.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsDeviceEepromWriteFault.setStatus(
        "current"
    )

tlpNotificationsDeviceEepromOperationTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 2, 44)
)
tlpNotificationsDeviceEepromOperationTimeout.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsDeviceEepromOperationTimeout.setStatus(
        "current"
    )

tlpNotificationsDeviceI2cWriteDelayed = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 2, 45)
)
tlpNotificationsDeviceI2cWriteDelayed.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsDeviceI2cWriteDelayed.setStatus(
        "current"
    )

tlpNotificationsDeviceRampShedNvrWriteFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 2, 46)
)
tlpNotificationsDeviceRampShedNvrWriteFailed.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsDeviceRampShedNvrWriteFailed.setStatus(
        "current"
    )

tlpNotificationsDeviceFactoryRestoreFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 2, 47)
)
tlpNotificationsDeviceFactoryRestoreFault.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsDeviceFactoryRestoreFault.setStatus(
        "current"
    )

tlpNotificationsDeviceRelaySetTimeOutOfRange = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 2, 48)
)
tlpNotificationsDeviceRelaySetTimeOutOfRange.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsDeviceRelaySetTimeOutOfRange.setStatus(
        "current"
    )

tlpNotificationsDeviceRelayResetTimeOutOfRange = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 2, 49)
)
tlpNotificationsDeviceRelayResetTimeOutOfRange.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsDeviceRelayResetTimeOutOfRange.setStatus(
        "current"
    )

tlpNotificationsUpsBatteryLowVoltageShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 3, 1)
)
tlpNotificationsUpsBatteryLowVoltageShutdown.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsUpsBatteryLowVoltageShutdown.setStatus(
        "current"
    )

tlpNotificationsUpsBatteryLowPercentageShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 3, 2)
)
tlpNotificationsUpsBatteryLowPercentageShutdown.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsUpsBatteryLowPercentageShutdown.setStatus(
        "current"
    )

tlpNotificationsUpsBatteryOverVoltageShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 3, 3)
)
tlpNotificationsUpsBatteryOverVoltageShutdown.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsUpsBatteryOverVoltageShutdown.setStatus(
        "current"
    )

tlpNotificationsUpsBatteryOverCurrentShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 3, 4)
)
tlpNotificationsUpsBatteryOverCurrentShutdown.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsUpsBatteryOverCurrentShutdown.setStatus(
        "current"
    )

tlpNotificationsUpsBatteryUnknownTypeShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 3, 5)
)
tlpNotificationsUpsBatteryUnknownTypeShutdown.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsUpsBatteryUnknownTypeShutdown.setStatus(
        "current"
    )

tlpNotificationsUpsBatteryConfigurationMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 3, 6)
)
tlpNotificationsUpsBatteryConfigurationMismatch.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsUpsBatteryConfigurationMismatch.setStatus(
        "current"
    )

tlpNotificationsUpsBatteryUnderVoltageShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 3, 7)
)
tlpNotificationsUpsBatteryUnderVoltageShutdown.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsUpsBatteryUnderVoltageShutdown.setStatus(
        "current"
    )

tlpNotificationsUpsSlaBatteryOverTemperatureShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 3, 8)
)
tlpNotificationsUpsSlaBatteryOverTemperatureShutdown.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsUpsSlaBatteryOverTemperatureShutdown.setStatus(
        "current"
    )

tlpNotificationsUpsBatteryInstallation = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 3, 9)
)
tlpNotificationsUpsBatteryInstallation.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsUpsBatteryInstallation.setStatus(
        "current"
    )

tlpNotificationsUpsChargerBulkToAcceptance = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 3, 10)
)
tlpNotificationsUpsChargerBulkToAcceptance.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsUpsChargerBulkToAcceptance.setStatus(
        "current"
    )

tlpNotificationsUpsChargerAcceptanceToFloat = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 3, 11)
)
tlpNotificationsUpsChargerAcceptanceToFloat.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsUpsChargerAcceptanceToFloat.setStatus(
        "current"
    )

tlpNotificationsUpsChargerFloatToBulk = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 3, 12)
)
tlpNotificationsUpsChargerFloatToBulk.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsUpsChargerFloatToBulk.setStatus(
        "current"
    )

tlpNotificationsUpsTransferToSelftest = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 3, 13)
)
tlpNotificationsUpsTransferToSelftest.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsUpsTransferToSelftest.setStatus(
        "current"
    )

tlpNotificationsUpsTransferToEconomy = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 3, 14)
)
tlpNotificationsUpsTransferToEconomy.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsUpsTransferToEconomy.setStatus(
        "current"
    )

tlpNotificationsUpsLineConnectRelayFaultShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 3, 15)
)
tlpNotificationsUpsLineConnectRelayFaultShutdown.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsUpsLineConnectRelayFaultShutdown.setStatus(
        "current"
    )

tlpNotificationsUpsTransferToFaultBypass = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 3, 16)
)
tlpNotificationsUpsTransferToFaultBypass.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsUpsTransferToFaultBypass.setStatus(
        "current"
    )

tlpNotificationsUpsBypassPowerDistributionModuleDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 3, 17)
)
tlpNotificationsUpsBypassPowerDistributionModuleDisconnected.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsUpsBypassPowerDistributionModuleDisconnected.setStatus(
        "current"
    )

tlpNotificationsUpsManualBypassActivatedFromUnsupportedMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 3, 18)
)
tlpNotificationsUpsManualBypassActivatedFromUnsupportedMode.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsUpsManualBypassActivatedFromUnsupportedMode.setStatus(
        "current"
    )

tlpNotificationsUpsOnBatteryTimeoutShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 3, 19)
)
tlpNotificationsUpsOnBatteryTimeoutShutdown.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsUpsOnBatteryTimeoutShutdown.setStatus(
        "current"
    )

tlpNotificationsUpsLowBatteryPercentageShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 3, 20)
)
tlpNotificationsUpsLowBatteryPercentageShutdown.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsUpsLowBatteryPercentageShutdown.setStatus(
        "current"
    )

tlpNotificationsUpsBatteryCommunicationsLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 3, 21)
)
tlpNotificationsUpsBatteryCommunicationsLost.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsUpsBatteryCommunicationsLost.setStatus(
        "current"
    )

tlpNotificationsUpsBatteryCommunicationsEstablished = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 3, 22)
)
tlpNotificationsUpsBatteryCommunicationsEstablished.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsUpsBatteryCommunicationsEstablished.setStatus(
        "current"
    )

tlpNotificationsUpsBatteryOtaShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 3, 23)
)
tlpNotificationsUpsBatteryOtaShutdown.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsUpsBatteryOtaShutdown.setStatus(
        "current"
    )

tlpNotificationsUpsCartInstallation = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 3, 24)
)
tlpNotificationsUpsCartInstallation.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsUpsCartInstallation.setStatus(
        "current"
    )

tlpNotificationsUpsDeadBatteryRecoveryShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 3, 25)
)
tlpNotificationsUpsDeadBatteryRecoveryShutdown.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsUpsDeadBatteryRecoveryShutdown.setStatus(
        "current"
    )

tlpNotificationsUpsFullBridgeNotSteadyShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 3, 26)
)
tlpNotificationsUpsFullBridgeNotSteadyShutdown.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsUpsFullBridgeNotSteadyShutdown.setStatus(
        "current"
    )

tlpNotificationsUpsFullBridgeCurrentLimitShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 3, 27)
)
tlpNotificationsUpsFullBridgeCurrentLimitShutdown.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsUpsFullBridgeCurrentLimitShutdown.setStatus(
        "current"
    )

tlpNotificationsUpsTransitionFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 3, 28)
)
tlpNotificationsUpsTransitionFailed.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsUpsTransitionFailed.setStatus(
        "current"
    )

tlpNotificationsUpsInverterOcp = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 3, 29)
)
tlpNotificationsUpsInverterOcp.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsUpsInverterOcp.setStatus(
        "current"
    )

tlpNotificationsUpsInverterVbusShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 3, 30)
)
tlpNotificationsUpsInverterVbusShutdown.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsUpsInverterVbusShutdown.setStatus(
        "current"
    )

tlpNotificationsUpsTransferToFaultStandby = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 3, 31)
)
tlpNotificationsUpsTransferToFaultStandby.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsUpsTransferToFaultStandby.setStatus(
        "current"
    )

tlpNotificationsUpsModbusBatteryStatusShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 3, 32)
)
tlpNotificationsUpsModbusBatteryStatusShutdown.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsUpsModbusBatteryStatusShutdown.setStatus(
        "current"
    )

tlpNotificationsUpsBatteryPackCountChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 3, 33)
)
tlpNotificationsUpsBatteryPackCountChange.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsUpsBatteryPackCountChange.setStatus(
        "current"
    )

tlpNotificationsUpsTransferToBattery = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 3, 34)
)
tlpNotificationsUpsTransferToBattery.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsUpsTransferToBattery.setStatus(
        "current"
    )

tlpNotificationsUpsTransferToBypass = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 3, 35)
)
tlpNotificationsUpsTransferToBypass.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsUpsTransferToBypass.setStatus(
        "current"
    )

tlpNotificationsUpsTransferToDbrLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 3, 36)
)
tlpNotificationsUpsTransferToDbrLine.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsUpsTransferToDbrLine.setStatus(
        "current"
    )

tlpNotificationsUpsTransferToDbrStandby = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 3, 37)
)
tlpNotificationsUpsTransferToDbrStandby.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsUpsTransferToDbrStandby.setStatus(
        "current"
    )

tlpNotificationsUpsTransferToStandby = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 3, 38)
)
tlpNotificationsUpsTransferToStandby.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsUpsTransferToStandby.setStatus(
        "current"
    )

tlpNotificationsUpsTransferToOnline = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 3, 39)
)
tlpNotificationsUpsTransferToOnline.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsUpsTransferToOnline.setStatus(
        "current"
    )

tlpNotificationsUpsV20BusNotSteadyShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 3, 40)
)
tlpNotificationsUpsV20BusNotSteadyShutdown.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsUpsV20BusNotSteadyShutdown.setStatus(
        "current"
    )

tlpNotificationsUpsV20BusOverVoltageShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 3, 41)
)
tlpNotificationsUpsV20BusOverVoltageShutdown.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsUpsV20BusOverVoltageShutdown.setStatus(
        "current"
    )

tlpNotificationsUpsV20BusUnderVoltageShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 3, 42)
)
tlpNotificationsUpsV20BusUnderVoltageShutdown.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsUpsV20BusUnderVoltageShutdown.setStatus(
        "current"
    )

tlpNotificationsUpsBypassOutOfRange = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 3, 43)
)
tlpNotificationsUpsBypassOutOfRange.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsUpsBypassOutOfRange.setStatus(
        "current"
    )

tlpNotificationsUpsEnergySavingShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 3, 44)
)
tlpNotificationsUpsEnergySavingShutdown.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsUpsEnergySavingShutdown.setStatus(
        "current"
    )

tlpNotificationsUpsDryContactShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 3, 45)
)
tlpNotificationsUpsDryContactShutdown.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsUpsDryContactShutdown.setStatus(
        "current"
    )

tlpNotificationsUpsInverterOverCurrentShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 3, 46)
)
tlpNotificationsUpsInverterOverCurrentShutdown.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsUpsInverterOverCurrentShutdown.setStatus(
        "current"
    )

tlpNotificationsUpsPfcPrechargeFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 3, 47)
)
tlpNotificationsUpsPfcPrechargeFault.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsUpsPfcPrechargeFault.setStatus(
        "current"
    )

tlpNotificationsUpsPfcOverVoltageFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 3, 48)
)
tlpNotificationsUpsPfcOverVoltageFault.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsUpsPfcOverVoltageFault.setStatus(
        "current"
    )

tlpNotificationsUpsPfcUnderVoltageFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 3, 49)
)
tlpNotificationsUpsPfcUnderVoltageFault.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsUpsPfcUnderVoltageFault.setStatus(
        "current"
    )

tlpNotificationsUpsPfcOverCurrentFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 3, 50)
)
tlpNotificationsUpsPfcOverCurrentFault.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsUpsPfcOverCurrentFault.setStatus(
        "current"
    )

tlpNotificationsPduCrestFactorOutOfRange = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 4, 1)
)
tlpNotificationsPduCrestFactorOutOfRange.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsPduCrestFactorOutOfRange.setStatus(
        "current"
    )

tlpNotificationsPduTransferToForceLineMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 4, 2)
)
tlpNotificationsPduTransferToForceLineMode.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsPduTransferToForceLineMode.setStatus(
        "current"
    )

tlpNotificationsPduLineInRange = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 4, 3)
)
tlpNotificationsPduLineInRange.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsPduLineInRange.setStatus(
        "current"
    )

tlpNotificationsPduLineOutOfRange = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 4, 4)
)
tlpNotificationsPduLineOutOfRange.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsPduLineOutOfRange.setStatus(
        "current"
    )

tlpNotificationsPduNotableRelayResponseTimes = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 4, 5)
)
tlpNotificationsPduNotableRelayResponseTimes.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsPduNotableRelayResponseTimes.setStatus(
        "current"
    )

tlpNotificationsPduOutletNearMaxRating = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 4, 6)
)
tlpNotificationsPduOutletNearMaxRating.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsPduOutletNearMaxRating.setStatus(
        "current"
    )

tlpNotificationsPduLineModeTransferToLinePartialPowerup = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 4, 7)
)
tlpNotificationsPduLineModeTransferToLinePartialPowerup.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsPduLineModeTransferToLinePartialPowerup.setStatus(
        "current"
    )

tlpNotificationsPduSinglePhasing = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 4, 8)
)
tlpNotificationsPduSinglePhasing.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsPduSinglePhasing.setStatus(
        "current"
    )

tlpNotificationsAtsSource1NotAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 6, 1)
)
tlpNotificationsAtsSource1NotAvailable.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsAtsSource1NotAvailable.setStatus(
        "current"
    )

tlpNotificationsAtsSource2NotAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 6, 2)
)
tlpNotificationsAtsSource2NotAvailable.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsAtsSource2NotAvailable.setStatus(
        "current"
    )

tlpNotificationsAtsLockdownToSource1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 6, 3)
)
tlpNotificationsAtsLockdownToSource1.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsAtsLockdownToSource1.setStatus(
        "current"
    )

tlpNotificationsAtsLockdownToSource2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 6, 4)
)
tlpNotificationsAtsLockdownToSource2.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsAtsLockdownToSource2.setStatus(
        "current"
    )

tlpNotificationsAtsSource1Available = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 6, 5)
)
tlpNotificationsAtsSource1Available.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsAtsSource1Available.setStatus(
        "current"
    )

tlpNotificationsAtsSource2Available = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 6, 6)
)
tlpNotificationsAtsSource2Available.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsAtsSource2Available.setStatus(
        "current"
    )

tlpNotificationsAtsSource1Brownout = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 6, 7)
)
tlpNotificationsAtsSource1Brownout.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsAtsSource1Brownout.setStatus(
        "current"
    )

tlpNotificationsAtsSource2Brownout = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 6, 8)
)
tlpNotificationsAtsSource2Brownout.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsAtsSource2Brownout.setStatus(
        "current"
    )

tlpNotificationsAtsSource1VoltageDrop = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 6, 9)
)
tlpNotificationsAtsSource1VoltageDrop.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsAtsSource1VoltageDrop.setStatus(
        "current"
    )

tlpNotificationsAtsSource2VoltageDrop = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 6, 10)
)
tlpNotificationsAtsSource2VoltageDrop.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsAtsSource2VoltageDrop.setStatus(
        "current"
    )

tlpNotificationsAtsTimedReturnToSource1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 6, 11)
)
tlpNotificationsAtsTimedReturnToSource1.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsAtsTimedReturnToSource1.setStatus(
        "current"
    )

tlpNotificationsAtsTimedReturnToSource2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 6, 12)
)
tlpNotificationsAtsTimedReturnToSource2.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsAtsTimedReturnToSource2.setStatus(
        "current"
    )

tlpNotificationsAtsTransferToSource1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 6, 13)
)
tlpNotificationsAtsTransferToSource1.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsAtsTransferToSource1.setStatus(
        "current"
    )

tlpNotificationsAtsTransferToSource2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 2, 6, 14)
)
tlpNotificationsAtsTransferToSource2.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpNotifyEventTableRowRef"))
)
if mibBuilder.loadTexts:
    tlpNotificationsAtsTransferToSource2.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TRIPPLITE-PRODUCTS",
    **{"tlpProducts": tlpProducts,
       "tlpHardware": tlpHardware,
       "tlpDevice": tlpDevice,
       "tlpDeviceNumDevices": tlpDeviceNumDevices,
       "tlpDeviceTable": tlpDeviceTable,
       "tlpDeviceEntry": tlpDeviceEntry,
       "tlpDeviceIndex": tlpDeviceIndex,
       "tlpDeviceRowStatus": tlpDeviceRowStatus,
       "tlpDeviceType": tlpDeviceType,
       "tlpDeviceManufacturer": tlpDeviceManufacturer,
       "tlpDeviceModel": tlpDeviceModel,
       "tlpDeviceName": tlpDeviceName,
       "tlpDeviceID": tlpDeviceID,
       "tlpDeviceLocation": tlpDeviceLocation,
       "tlpDeviceRegion": tlpDeviceRegion,
       "tlpDeviceStatus": tlpDeviceStatus,
       "tlpDeviceAssetTag": tlpDeviceAssetTag,
       "tlpDeviceDetail": tlpDeviceDetail,
       "tlpDeviceIdentTable": tlpDeviceIdentTable,
       "tlpDeviceIdentEntry": tlpDeviceIdentEntry,
       "tlpDeviceIdentProtocol": tlpDeviceIdentProtocol,
       "tlpDeviceIdentCommPortType": tlpDeviceIdentCommPortType,
       "tlpDeviceIdentCommPortName": tlpDeviceIdentCommPortName,
       "tlpDeviceIdentFirmwareVersion": tlpDeviceIdentFirmwareVersion,
       "tlpDeviceIdentSerialNum": tlpDeviceIdentSerialNum,
       "tlpDeviceIdentDateInstalled": tlpDeviceIdentDateInstalled,
       "tlpDeviceIdentHardwareVersion": tlpDeviceIdentHardwareVersion,
       "tlpDeviceIdentCurrentUptime": tlpDeviceIdentCurrentUptime,
       "tlpDeviceIdentTotalUptime": tlpDeviceIdentTotalUptime,
       "tlpDeviceIdentFirmwareVersion2": tlpDeviceIdentFirmwareVersion2,
       "tlpDeviceIdentFirmwareVersion3": tlpDeviceIdentFirmwareVersion3,
       "tlpDeviceIdentNvrID": tlpDeviceIdentNvrID,
       "tlpDeviceTypes": tlpDeviceTypes,
       "tlpUps": tlpUps,
       "tlpUpsIdent": tlpUpsIdent,
       "tlpUpsIdentNumUps": tlpUpsIdentNumUps,
       "tlpUpsIdentTable": tlpUpsIdentTable,
       "tlpUpsIdentEntry": tlpUpsIdentEntry,
       "tlpUpsIdentNumInputs": tlpUpsIdentNumInputs,
       "tlpUpsIdentNumOutputs": tlpUpsIdentNumOutputs,
       "tlpUpsIdentNumBypass": tlpUpsIdentNumBypass,
       "tlpUpsIdentNumPhases": tlpUpsIdentNumPhases,
       "tlpUpsIdentNumOutlets": tlpUpsIdentNumOutlets,
       "tlpUpsIdentNumOutletGroups": tlpUpsIdentNumOutletGroups,
       "tlpUpsIdentNumBatteries": tlpUpsIdentNumBatteries,
       "tlpUpsIdentNumFans": tlpUpsIdentNumFans,
       "tlpUpsIdentNumHeatsinks": tlpUpsIdentNumHeatsinks,
       "tlpUpsIdentNumInputContacts": tlpUpsIdentNumInputContacts,
       "tlpUpsIdentNumOutputContacts": tlpUpsIdentNumOutputContacts,
       "tlpUpsIdentNumActiveControlModules": tlpUpsIdentNumActiveControlModules,
       "tlpUpsIdentNumRedundantControlModules": tlpUpsIdentNumRedundantControlModules,
       "tlpUpsSupportsTable": tlpUpsSupportsTable,
       "tlpUpsSupportsEntry": tlpUpsSupportsEntry,
       "tlpUpsSupportsEnergywise": tlpUpsSupportsEnergywise,
       "tlpUpsSupportsRampShed": tlpUpsSupportsRampShed,
       "tlpUpsSupportsOutletGroup": tlpUpsSupportsOutletGroup,
       "tlpUpsSupportsOutletCurrent": tlpUpsSupportsOutletCurrent,
       "tlpUpsSupportsOutletVoltage": tlpUpsSupportsOutletVoltage,
       "tlpUpsSupportsOutletActivePower": tlpUpsSupportsOutletActivePower,
       "tlpUpsDevice": tlpUpsDevice,
       "tlpUpsDeviceTable": tlpUpsDeviceTable,
       "tlpUpsDeviceEntry": tlpUpsDeviceEntry,
       "tlpUpsDeviceMainLoadState": tlpUpsDeviceMainLoadState,
       "tlpUpsDeviceMainLoadControllable": tlpUpsDeviceMainLoadControllable,
       "tlpUpsDeviceMainLoadCommand": tlpUpsDeviceMainLoadCommand,
       "tlpUpsDevicePowerOnDelay": tlpUpsDevicePowerOnDelay,
       "tlpUpsDeviceTestDate": tlpUpsDeviceTestDate,
       "tlpUpsDeviceTestResultsStatus": tlpUpsDeviceTestResultsStatus,
       "tlpUpsDeviceTemperatureC": tlpUpsDeviceTemperatureC,
       "tlpUpsDeviceTemperatureF": tlpUpsDeviceTemperatureF,
       "tlpUpsDeviceLastACFailureReason": tlpUpsDeviceLastACFailureReason,
       "tlpUpsDeviceLastShutdownReason": tlpUpsDeviceLastShutdownReason,
       "tlpUpsDeviceOutputCurrentPrecision": tlpUpsDeviceOutputCurrentPrecision,
       "tlpUpsDeviceOutputActivePowerTotal": tlpUpsDeviceOutputActivePowerTotal,
       "tlpUpsDeviceAggregatePowerFactor": tlpUpsDeviceAggregatePowerFactor,
       "tlpUpsDeviceGeneralFault": tlpUpsDeviceGeneralFault,
       "tlpUpsDeviceUpsType": tlpUpsDeviceUpsType,
       "tlpUpsDeviceLastBypassReason": tlpUpsDeviceLastBypassReason,
       "tlpUpsDeviceBuzzerStatus": tlpUpsDeviceBuzzerStatus,
       "tlpUpsDetail": tlpUpsDetail,
       "tlpUpsBattery": tlpUpsBattery,
       "tlpUpsBatterySummaryTable": tlpUpsBatterySummaryTable,
       "tlpUpsBatterySummaryEntry": tlpUpsBatterySummaryEntry,
       "tlpUpsBatteryStatus": tlpUpsBatteryStatus,
       "tlpUpsSecondsOnBattery": tlpUpsSecondsOnBattery,
       "tlpUpsEstimatedMinutesRemaining": tlpUpsEstimatedMinutesRemaining,
       "tlpUpsEstimatedChargeRemaining": tlpUpsEstimatedChargeRemaining,
       "tlpUpsBatteryRunTimeRemaining": tlpUpsBatteryRunTimeRemaining,
       "tlpUpsBatteryTotalMinutesOnBattery": tlpUpsBatteryTotalMinutesOnBattery,
       "tlpUpsBatteryDetailTable": tlpUpsBatteryDetailTable,
       "tlpUpsBatteryDetailEntry": tlpUpsBatteryDetailEntry,
       "tlpUpsBatteryDetailVoltage": tlpUpsBatteryDetailVoltage,
       "tlpUpsBatteryDetailCurrent": tlpUpsBatteryDetailCurrent,
       "tlpUpsBatteryDetailCapacity": tlpUpsBatteryDetailCapacity,
       "tlpUpsBatteryDetailCharge": tlpUpsBatteryDetailCharge,
       "tlpUpsBatteryDetailChargerStatus": tlpUpsBatteryDetailChargerStatus,
       "tlpUpsBatteryDetailNominalVoltage": tlpUpsBatteryDetailNominalVoltage,
       "tlpUpsBatteryDetailFullyCharged": tlpUpsBatteryDetailFullyCharged,
       "tlpUpsBatteryDetailOvercharged": tlpUpsBatteryDetailOvercharged,
       "tlpUpsBatteryDetailVoltageNegative": tlpUpsBatteryDetailVoltageNegative,
       "tlpUpsBatteryDetailVoltagePositive": tlpUpsBatteryDetailVoltagePositive,
       "tlpUpsBatteryDetailMaxChargerCurrent": tlpUpsBatteryDetailMaxChargerCurrent,
       "tlpUpsBatteryPackIdentTable": tlpUpsBatteryPackIdentTable,
       "tlpUpsBatteryPackIdentEntry": tlpUpsBatteryPackIdentEntry,
       "tlpUpsBatteryPackIdentIndex": tlpUpsBatteryPackIdentIndex,
       "tlpUpsBatteryPackIdentManufacturer": tlpUpsBatteryPackIdentManufacturer,
       "tlpUpsBatteryPackIdentModel": tlpUpsBatteryPackIdentModel,
       "tlpUpsBatteryPackIdentSerialNum": tlpUpsBatteryPackIdentSerialNum,
       "tlpUpsBatteryPackIdentFirmware": tlpUpsBatteryPackIdentFirmware,
       "tlpUpsBatteryPackIdentSKU": tlpUpsBatteryPackIdentSKU,
       "tlpUpsBatteryPackConfigTable": tlpUpsBatteryPackConfigTable,
       "tlpUpsBatteryPackConfigEntry": tlpUpsBatteryPackConfigEntry,
       "tlpUpsBatteryPackConfigChemistry": tlpUpsBatteryPackConfigChemistry,
       "tlpUpsBatteryPackConfigStyle": tlpUpsBatteryPackConfigStyle,
       "tlpUpsBatteryPackConfigLocation": tlpUpsBatteryPackConfigLocation,
       "tlpUpsBatteryPackConfigStrings": tlpUpsBatteryPackConfigStrings,
       "tlpUpsBatteryPackConfigBatteriesPerString": tlpUpsBatteryPackConfigBatteriesPerString,
       "tlpUpsBatteryPackConfigCellsPerBattery": tlpUpsBatteryPackConfigCellsPerBattery,
       "tlpUpsBatteryPackConfigNumBatteries": tlpUpsBatteryPackConfigNumBatteries,
       "tlpUpsBatteryPackConfigCapacityUnits": tlpUpsBatteryPackConfigCapacityUnits,
       "tlpUpsBatteryPackConfigDesignCapacity": tlpUpsBatteryPackConfigDesignCapacity,
       "tlpUpsBatteryPackConfigCellCapacity": tlpUpsBatteryPackConfigCellCapacity,
       "tlpUpsBatteryPackConfigMinCellVoltage": tlpUpsBatteryPackConfigMinCellVoltage,
       "tlpUpsBatteryPackConfigMaxCellVoltage": tlpUpsBatteryPackConfigMaxCellVoltage,
       "tlpUpsBatteryPackConfigRechargeable": tlpUpsBatteryPackConfigRechargeable,
       "tlpUpsBatteryPackConfigFullChargeCapacity": tlpUpsBatteryPackConfigFullChargeCapacity,
       "tlpUpsBatteryPackDetailTable": tlpUpsBatteryPackDetailTable,
       "tlpUpsBatteryPackDetailEntry": tlpUpsBatteryPackDetailEntry,
       "tlpUpsBatteryPackDetailCondition": tlpUpsBatteryPackDetailCondition,
       "tlpUpsBatteryPackDetailTemperatureC": tlpUpsBatteryPackDetailTemperatureC,
       "tlpUpsBatteryPackDetailTemperatureF": tlpUpsBatteryPackDetailTemperatureF,
       "tlpUpsBatteryPackDetailAge": tlpUpsBatteryPackDetailAge,
       "tlpUpsBatteryPackDetailLastReplaceDate": tlpUpsBatteryPackDetailLastReplaceDate,
       "tlpUpsBatteryPackDetailNextReplaceDate": tlpUpsBatteryPackDetailNextReplaceDate,
       "tlpUpsBatteryPackDetailCycleCount": tlpUpsBatteryPackDetailCycleCount,
       "tlpUpsInput": tlpUpsInput,
       "tlpUpsInputTable": tlpUpsInputTable,
       "tlpUpsInputEntry": tlpUpsInputEntry,
       "tlpUpsInputLineBads": tlpUpsInputLineBads,
       "tlpUpsInputNominalVoltage": tlpUpsInputNominalVoltage,
       "tlpUpsInputNominalFrequency": tlpUpsInputNominalFrequency,
       "tlpUpsInputLowTransferVoltage": tlpUpsInputLowTransferVoltage,
       "tlpUpsInputLowTransferVoltageLowerBound": tlpUpsInputLowTransferVoltageLowerBound,
       "tlpUpsInputLowTransferVoltageUpperBound": tlpUpsInputLowTransferVoltageUpperBound,
       "tlpUpsInputHighTransferVoltage": tlpUpsInputHighTransferVoltage,
       "tlpUpsInputHighTransferVoltageLowerBound": tlpUpsInputHighTransferVoltageLowerBound,
       "tlpUpsInputHighTransferVoltageUpperBound": tlpUpsInputHighTransferVoltageUpperBound,
       "tlpUpsInputCurrentTotal": tlpUpsInputCurrentTotal,
       "tlpUpsInputLowTransferVoltageResetTolerance": tlpUpsInputLowTransferVoltageResetTolerance,
       "tlpUpsInputHighTransferVoltageResetTolerance": tlpUpsInputHighTransferVoltageResetTolerance,
       "tlpUpsInputTransformerStatus": tlpUpsInputTransformerStatus,
       "tlpUpsInputAvrTransitionCount": tlpUpsInputAvrTransitionCount,
       "tlpUpsInputSource": tlpUpsInputSource,
       "tlpUpsInputPhaseTable": tlpUpsInputPhaseTable,
       "tlpUpsInputPhaseEntry": tlpUpsInputPhaseEntry,
       "tlpUpsInputPhaseIndex": tlpUpsInputPhaseIndex,
       "tlpUpsInputPhaseFrequency": tlpUpsInputPhaseFrequency,
       "tlpUpsInputPhaseVoltage": tlpUpsInputPhaseVoltage,
       "tlpUpsInputPhaseVoltageMin": tlpUpsInputPhaseVoltageMin,
       "tlpUpsInputPhaseVoltageMax": tlpUpsInputPhaseVoltageMax,
       "tlpUpsInputPhaseCurrent": tlpUpsInputPhaseCurrent,
       "tlpUpsInputPhasePower": tlpUpsInputPhasePower,
       "tlpUpsOutput": tlpUpsOutput,
       "tlpUpsOutputTable": tlpUpsOutputTable,
       "tlpUpsOutputEntry": tlpUpsOutputEntry,
       "tlpUpsOutputSource": tlpUpsOutputSource,
       "tlpUpsOutputNominalVoltage": tlpUpsOutputNominalVoltage,
       "tlpUpsOutputFrequency": tlpUpsOutputFrequency,
       "tlpUpsOutputVARating": tlpUpsOutputVARating,
       "tlpUpsOutputPowerFactor": tlpUpsOutputPowerFactor,
       "tlpUpsOutputTotalUtilization": tlpUpsOutputTotalUtilization,
       "tlpUpsOutputPowerRating": tlpUpsOutputPowerRating,
       "tlpUpsOutputChargerCurrent": tlpUpsOutputChargerCurrent,
       "tlpUpsOutputCurrentRating": tlpUpsOutputCurrentRating,
       "tlpUpsOutputEfficiency": tlpUpsOutputEfficiency,
       "tlpUpsOutputLineTable": tlpUpsOutputLineTable,
       "tlpUpsOutputLineEntry": tlpUpsOutputLineEntry,
       "tlpUpsOutputLineIndex": tlpUpsOutputLineIndex,
       "tlpUpsOutputLineVoltage": tlpUpsOutputLineVoltage,
       "tlpUpsOutputLineCurrent": tlpUpsOutputLineCurrent,
       "tlpUpsOutputLineActivePower": tlpUpsOutputLineActivePower,
       "tlpUpsOutputLineUtilization": tlpUpsOutputLineUtilization,
       "tlpUpsOutputLineFrequency": tlpUpsOutputLineFrequency,
       "tlpUpsOutputLineCurrentMin": tlpUpsOutputLineCurrentMin,
       "tlpUpsOutputLineCurrentMax": tlpUpsOutputLineCurrentMax,
       "tlpUpsOutputLineApparentPower": tlpUpsOutputLineApparentPower,
       "tlpUpsOutputLinePowerKVA": tlpUpsOutputLinePowerKVA,
       "tlpUpsOutputLinePowerKW": tlpUpsOutputLinePowerKW,
       "tlpUpsOutputLine24hrEnergy": tlpUpsOutputLine24hrEnergy,
       "tlpUpsOutputLineWattHours": tlpUpsOutputLineWattHours,
       "tlpUpsOutputLinePeakPower": tlpUpsOutputLinePeakPower,
       "tlpUpsBypass": tlpUpsBypass,
       "tlpUpsBypassTable": tlpUpsBypassTable,
       "tlpUpsBypassEntry": tlpUpsBypassEntry,
       "tlpUpsBypassFrequency": tlpUpsBypassFrequency,
       "tlpUpsBypassNominalFrequency": tlpUpsBypassNominalFrequency,
       "tlpUpsBypassLineTable": tlpUpsBypassLineTable,
       "tlpUpsBypassLineEntry": tlpUpsBypassLineEntry,
       "tlpUpsBypassLineIndex": tlpUpsBypassLineIndex,
       "tlpUpsBypassLineVoltage": tlpUpsBypassLineVoltage,
       "tlpUpsBypassLineCurrent": tlpUpsBypassLineCurrent,
       "tlpUpsBypassLinePower": tlpUpsBypassLinePower,
       "tlpUpsOutlet": tlpUpsOutlet,
       "tlpUpsOutletTable": tlpUpsOutletTable,
       "tlpUpsOutletEntry": tlpUpsOutletEntry,
       "tlpUpsOutletIndex": tlpUpsOutletIndex,
       "tlpUpsOutletName": tlpUpsOutletName,
       "tlpUpsOutletDescription": tlpUpsOutletDescription,
       "tlpUpsOutletState": tlpUpsOutletState,
       "tlpUpsOutletControllable": tlpUpsOutletControllable,
       "tlpUpsOutletCommand": tlpUpsOutletCommand,
       "tlpUpsOutletVoltage": tlpUpsOutletVoltage,
       "tlpUpsOutletCurrent": tlpUpsOutletCurrent,
       "tlpUpsOutletActivePower": tlpUpsOutletActivePower,
       "tlpUpsOutletRampAction": tlpUpsOutletRampAction,
       "tlpUpsOutletRampDelay": tlpUpsOutletRampDelay,
       "tlpUpsOutletShedAction": tlpUpsOutletShedAction,
       "tlpUpsOutletShedDelay": tlpUpsOutletShedDelay,
       "tlpUpsOutletGroup": tlpUpsOutletGroup,
       "tlpUpsOutletBank": tlpUpsOutletBank,
       "tlpUpsOutletCircuit": tlpUpsOutletCircuit,
       "tlpUpsOutletPhase": tlpUpsOutletPhase,
       "tlpUpsOutletReceptacleType": tlpUpsOutletReceptacleType,
       "tlpUpsOutletPowerFactor": tlpUpsOutletPowerFactor,
       "tlpUpsOutletApparentPower": tlpUpsOutletApparentPower,
       "tlpUpsOutletReactivePower": tlpUpsOutletReactivePower,
       "tlpUpsOutletFrequency": tlpUpsOutletFrequency,
       "tlpUpsOutletUtilization": tlpUpsOutletUtilization,
       "tlpUpsOutlet24hrEnergy": tlpUpsOutlet24hrEnergy,
       "tlpUpsOutletOvercurrent": tlpUpsOutletOvercurrent,
       "tlpUpsOutletGroupTable": tlpUpsOutletGroupTable,
       "tlpUpsOutletGroupEntry": tlpUpsOutletGroupEntry,
       "tlpUpsOutletGroupIndex": tlpUpsOutletGroupIndex,
       "tlpUpsOutletGroupRowStatus": tlpUpsOutletGroupRowStatus,
       "tlpUpsOutletGroupName": tlpUpsOutletGroupName,
       "tlpUpsOutletGroupDescription": tlpUpsOutletGroupDescription,
       "tlpUpsOutletGroupState": tlpUpsOutletGroupState,
       "tlpUpsOutletGroupCommand": tlpUpsOutletGroupCommand,
       "tlpUpsWatchdog": tlpUpsWatchdog,
       "tlpUpsWatchdogTable": tlpUpsWatchdogTable,
       "tlpUpsWatchdogEntry": tlpUpsWatchdogEntry,
       "tlpUpsWatchdogSupported": tlpUpsWatchdogSupported,
       "tlpUpsWatchdogSecsBeforeRestart": tlpUpsWatchdogSecsBeforeRestart,
       "tlpUpsWatchdogRestartAlarm": tlpUpsWatchdogRestartAlarm,
       "tlpUpsWatchdogStatus": tlpUpsWatchdogStatus,
       "tlpUpsWatchdogRetry": tlpUpsWatchdogRetry,
       "tlpUpsFan": tlpUpsFan,
       "tlpUpsFanTable": tlpUpsFanTable,
       "tlpUpsFanEntry": tlpUpsFanEntry,
       "tlpUpsFanIndex": tlpUpsFanIndex,
       "tlpUpsFanLocation": tlpUpsFanLocation,
       "tlpUpsFanStatus": tlpUpsFanStatus,
       "tlpUpsFanSpeed": tlpUpsFanSpeed,
       "tlpUpsFanActivationTemperatureDegF": tlpUpsFanActivationTemperatureDegF,
       "tlpUpsFanActivationTemperatureDegC": tlpUpsFanActivationTemperatureDegC,
       "tlpUpsHeatsink": tlpUpsHeatsink,
       "tlpUpsHeatsinkTable": tlpUpsHeatsinkTable,
       "tlpUpsHeatsinkEntry": tlpUpsHeatsinkEntry,
       "tlpUpsHeatsinkIndex": tlpUpsHeatsinkIndex,
       "tlpUpsHeatsinkTemperatureC": tlpUpsHeatsinkTemperatureC,
       "tlpUpsHeatsinkTemperatureF": tlpUpsHeatsinkTemperatureF,
       "tlpUpsContact": tlpUpsContact,
       "tlpUpsInputContact": tlpUpsInputContact,
       "tlpUpsInputContactTable": tlpUpsInputContactTable,
       "tlpUpsInputContactEntry": tlpUpsInputContactEntry,
       "tlpUpsInputContactIndex": tlpUpsInputContactIndex,
       "tlpUpsInputContactInAlarm": tlpUpsInputContactInAlarm,
       "tlpUpsOutputContact": tlpUpsOutputContact,
       "tlpUpsOutputContactTable": tlpUpsOutputContactTable,
       "tlpUpsOutputContactEntry": tlpUpsOutputContactEntry,
       "tlpUpsOutputContactIndex": tlpUpsOutputContactIndex,
       "tlpUpsOutputContactInAlarm": tlpUpsOutputContactInAlarm,
       "tlpUpsControl": tlpUpsControl,
       "tlpUpsControlTable": tlpUpsControlTable,
       "tlpUpsControlEntry": tlpUpsControlEntry,
       "tlpUpsControlSelfTest": tlpUpsControlSelfTest,
       "tlpUpsControlRamp": tlpUpsControlRamp,
       "tlpUpsControlShed": tlpUpsControlShed,
       "tlpUpsControlUpsOn": tlpUpsControlUpsOn,
       "tlpUpsControlUpsOff": tlpUpsControlUpsOff,
       "tlpUpsControlUpsRestart": tlpUpsControlUpsRestart,
       "tlpUpsControlBypass": tlpUpsControlBypass,
       "tlpUpsControlResetWattHours": tlpUpsControlResetWattHours,
       "tlpUpsControlCancelSelfTest": tlpUpsControlCancelSelfTest,
       "tlpUpsControlResetAllParameters": tlpUpsControlResetAllParameters,
       "tlpUpsControlMuteBuzzer": tlpUpsControlMuteBuzzer,
       "tlpUpsControlResetBatteryTransitionCount": tlpUpsControlResetBatteryTransitionCount,
       "tlpUpsControlResetLastReasonForBypass": tlpUpsControlResetLastReasonForBypass,
       "tlpUpsControlResetLastReasonStats": tlpUpsControlResetLastReasonStats,
       "tlpUpsControlResetAvrTransitionCount": tlpUpsControlResetAvrTransitionCount,
       "tlpUpsControlResetPeakPower": tlpUpsControlResetPeakPower,
       "tlpUpsControlClearEventLog": tlpUpsControlClearEventLog,
       "tlpUpsControlOutputPhaseTable": tlpUpsControlOutputPhaseTable,
       "tlpUpsControlOutputPhaseEntry": tlpUpsControlOutputPhaseEntry,
       "tlpUpsControlResetOutputCurrentMinMax": tlpUpsControlResetOutputCurrentMinMax,
       "tlpUpsControlInputPhaseTable": tlpUpsControlInputPhaseTable,
       "tlpUpsControlInputPhaseEntry": tlpUpsControlInputPhaseEntry,
       "tlpUpsControlResetInputVoltageMinMax": tlpUpsControlResetInputVoltageMinMax,
       "tlpUpsConfig": tlpUpsConfig,
       "tlpUpsConfigTable": tlpUpsConfigTable,
       "tlpUpsConfigEntry": tlpUpsConfigEntry,
       "tlpUpsConfigInputVoltage": tlpUpsConfigInputVoltage,
       "tlpUpsConfigInputFrequency": tlpUpsConfigInputFrequency,
       "tlpUpsConfigOutputVoltage": tlpUpsConfigOutputVoltage,
       "tlpUpsConfigOutputFrequency": tlpUpsConfigOutputFrequency,
       "tlpUpsConfigAudibleStatus": tlpUpsConfigAudibleStatus,
       "tlpUpsConfigAutoBatteryTest": tlpUpsConfigAutoBatteryTest,
       "tlpUpsConfigAutoRestartAfterShutdown": tlpUpsConfigAutoRestartAfterShutdown,
       "tlpUpsConfigAutoRampOnTransition": tlpUpsConfigAutoRampOnTransition,
       "tlpUpsConfigAutoShedOnTransition": tlpUpsConfigAutoShedOnTransition,
       "tlpUpsConfigBypassLowerLimitPercent": tlpUpsConfigBypassLowerLimitPercent,
       "tlpUpsConfigBypassUpperLimitPercent": tlpUpsConfigBypassUpperLimitPercent,
       "tlpUpsConfigBypassLowerLimitVoltage": tlpUpsConfigBypassLowerLimitVoltage,
       "tlpUpsConfigBypassUpperLimitVoltage": tlpUpsConfigBypassUpperLimitVoltage,
       "tlpUpsConfigColdStart": tlpUpsConfigColdStart,
       "tlpUpsConfigPowerStrategy": tlpUpsConfigPowerStrategy,
       "tlpUpsConfigFaultAction": tlpUpsConfigFaultAction,
       "tlpUpsConfigOffMode": tlpUpsConfigOffMode,
       "tlpUpsConfigLineSensitivity": tlpUpsConfigLineSensitivity,
       "tlpUpsConfigLineQualifyTime": tlpUpsConfigLineQualifyTime,
       "tlpUpsConfigACPowerSenseType": tlpUpsConfigACPowerSenseType,
       "tlpUpsConfigAcPresentStartMode": tlpUpsConfigAcPresentStartMode,
       "tlpUpsConfigBatteryCapacityCoefficient": tlpUpsConfigBatteryCapacityCoefficient,
       "tlpUpsConfigBatteryTemperatureCompensation": tlpUpsConfigBatteryTemperatureCompensation,
       "tlpUpsConfigBatteryTimedShutdownStatus": tlpUpsConfigBatteryTimedShutdownStatus,
       "tlpUpsConfigBatteryTimedShutdownSeconds": tlpUpsConfigBatteryTimedShutdownSeconds,
       "tlpUpsConfigBatteryMinCapacityToRestart": tlpUpsConfigBatteryMinCapacityToRestart,
       "tlpUpsConfigShutdownCompletionBehavior": tlpUpsConfigShutdownCompletionBehavior,
       "tlpUpsConfigEmergencyPowerOff": tlpUpsConfigEmergencyPowerOff,
       "tlpUpsConfigEnergySavingSetting": tlpUpsConfigEnergySavingSetting,
       "tlpUpsConfigFrequencyConvertMode": tlpUpsConfigFrequencyConvertMode,
       "tlpUpsConfigBatteryCapacityConfiguration": tlpUpsConfigBatteryCapacityConfiguration,
       "tlpUpsConfigAutoBatteryTestMinutes": tlpUpsConfigAutoBatteryTestMinutes,
       "tlpUpsConfigMaxBatteryChargerCurrent": tlpUpsConfigMaxBatteryChargerCurrent,
       "tlpUpsConfigAutoRestartTable": tlpUpsConfigAutoRestartTable,
       "tlpUpsConfigAutoRestartEntry": tlpUpsConfigAutoRestartEntry,
       "tlpUpsConfigAutoRestartInverterShutdown": tlpUpsConfigAutoRestartInverterShutdown,
       "tlpUpsConfigAutoRestartDelayedWakeup": tlpUpsConfigAutoRestartDelayedWakeup,
       "tlpUpsConfigAutoRestartLowVoltageCutoff": tlpUpsConfigAutoRestartLowVoltageCutoff,
       "tlpUpsConfigAutoRestartOverLoad": tlpUpsConfigAutoRestartOverLoad,
       "tlpUpsConfigAutoRestartOverTemperature": tlpUpsConfigAutoRestartOverTemperature,
       "tlpUpsConfigThresholdTable": tlpUpsConfigThresholdTable,
       "tlpUpsConfigThresholdEntry": tlpUpsConfigThresholdEntry,
       "tlpUpsConfigBatteryAgeThreshold": tlpUpsConfigBatteryAgeThreshold,
       "tlpUpsConfigLowBatteryThreshold": tlpUpsConfigLowBatteryThreshold,
       "tlpUpsConfigLowBatteryTime": tlpUpsConfigLowBatteryTime,
       "tlpUpsConfigOverLoadThreshold": tlpUpsConfigOverLoadThreshold,
       "tlpUpsConfigLowBatteryCriticalThreshold": tlpUpsConfigLowBatteryCriticalThreshold,
       "tlpUpsConfigBatteryAgeWarningThreshold": tlpUpsConfigBatteryAgeWarningThreshold,
       "tlpUpsConfigBatteryAgeCriticalThreshold": tlpUpsConfigBatteryAgeCriticalThreshold,
       "tlpUpsConfigLowBatteryRuntimeWarningThreshold": tlpUpsConfigLowBatteryRuntimeWarningThreshold,
       "tlpUpsConfigLowBatteryRuntimeCriticalThreshold": tlpUpsConfigLowBatteryRuntimeCriticalThreshold,
       "tlpUpsConfigVoltageTable": tlpUpsConfigVoltageTable,
       "tlpUpsConfigVoltageEntry": tlpUpsConfigVoltageEntry,
       "tlpUpsConfigHighVoltageTransfer": tlpUpsConfigHighVoltageTransfer,
       "tlpUpsConfigHighVoltageResetTolerance": tlpUpsConfigHighVoltageResetTolerance,
       "tlpUpsConfigHighVoltageReset": tlpUpsConfigHighVoltageReset,
       "tlpUpsConfigLowVoltageTransfer": tlpUpsConfigLowVoltageTransfer,
       "tlpUpsConfigLowVoltageResetTolerance": tlpUpsConfigLowVoltageResetTolerance,
       "tlpUpsConfigLowVoltageReset": tlpUpsConfigLowVoltageReset,
       "tlpUpsConfigContact": tlpUpsConfigContact,
       "tlpUpsConfigContactTable": tlpUpsConfigContactTable,
       "tlpUpsConfigContactEntry": tlpUpsConfigContactEntry,
       "tlpUpsConfigOutputContactBackupTimer": tlpUpsConfigOutputContactBackupTimer,
       "tlpUpsConfigInputContactTable": tlpUpsConfigInputContactTable,
       "tlpUpsConfigInputContactEntry": tlpUpsConfigInputContactEntry,
       "tlpUpsConfigInputContactIndex": tlpUpsConfigInputContactIndex,
       "tlpUpsConfigInputContactSetup": tlpUpsConfigInputContactSetup,
       "tlpUpsConfigOutputContactTable": tlpUpsConfigOutputContactTable,
       "tlpUpsConfigOutputContactEntry": tlpUpsConfigOutputContactEntry,
       "tlpUpsConfigOutputContactIndex": tlpUpsConfigOutputContactIndex,
       "tlpUpsConfigOutputContactSetup": tlpUpsConfigOutputContactSetup,
       "tlpUpsConfigDb9": tlpUpsConfigDb9,
       "tlpUpsConfigDb9InputTable": tlpUpsConfigDb9InputTable,
       "tlpUpsConfigDb9InputEntry": tlpUpsConfigDb9InputEntry,
       "tlpUpsConfigDb9InputPins3and9": tlpUpsConfigDb9InputPins3and9,
       "tlpUpsConfigDb9OutputTable": tlpUpsConfigDb9OutputTable,
       "tlpUpsConfigDb9OutputEntry": tlpUpsConfigDb9OutputEntry,
       "tlpUpsConfigDb9OutputPins1and5": tlpUpsConfigDb9OutputPins1and5,
       "tlpUpsConfigDb9OutputPins8and5": tlpUpsConfigDb9OutputPins8and5,
       "tlpUpsConfigOutputPhaseThresholdTable": tlpUpsConfigOutputPhaseThresholdTable,
       "tlpUpsConfigOutputPhaseThresholdEntry": tlpUpsConfigOutputPhaseThresholdEntry,
       "tlpUpsConfigOutputCurrentThresholdTolerance": tlpUpsConfigOutputCurrentThresholdTolerance,
       "tlpUpsConfigOutputCurrentHighThreshold": tlpUpsConfigOutputCurrentHighThreshold,
       "tlpUpsConfigOutputCurrentLowThreshold": tlpUpsConfigOutputCurrentLowThreshold,
       "tlpUpsConfigOutputVoltageThresholdTolerance": tlpUpsConfigOutputVoltageThresholdTolerance,
       "tlpUpsConfigOutputVoltageHighCriticalThreshold": tlpUpsConfigOutputVoltageHighCriticalThreshold,
       "tlpUpsConfigOutputVoltageHighWarningThreshold": tlpUpsConfigOutputVoltageHighWarningThreshold,
       "tlpUpsConfigOutputVoltageLowWarningThreshold": tlpUpsConfigOutputVoltageLowWarningThreshold,
       "tlpUpsConfigOutputVoltageLowCriticalThreshold": tlpUpsConfigOutputVoltageLowCriticalThreshold,
       "tlpUpsConfigOutputUtilizationThresholdTolerance": tlpUpsConfigOutputUtilizationThresholdTolerance,
       "tlpUpsConfigOutputUtilizationWarningThreshold": tlpUpsConfigOutputUtilizationWarningThreshold,
       "tlpUpsConfigInputPhaseThresholdTable": tlpUpsConfigInputPhaseThresholdTable,
       "tlpUpsConfigInputPhaseThresholdEntry": tlpUpsConfigInputPhaseThresholdEntry,
       "tlpUpsConfigInputVoltageThresholdTolerance": tlpUpsConfigInputVoltageThresholdTolerance,
       "tlpUpsConfigInputVoltageHighCriticalThreshold": tlpUpsConfigInputVoltageHighCriticalThreshold,
       "tlpUpsConfigInputVoltageHighWarningThreshold": tlpUpsConfigInputVoltageHighWarningThreshold,
       "tlpUpsConfigInputVoltageLowWarningThreshold": tlpUpsConfigInputVoltageLowWarningThreshold,
       "tlpUpsConfigInputVoltageLowCriticalThreshold": tlpUpsConfigInputVoltageLowCriticalThreshold,
       "tlpUpsConfigTemperatureFahrenheitTable": tlpUpsConfigTemperatureFahrenheitTable,
       "tlpUpsConfigTemperatureFahrenheitEntry": tlpUpsConfigTemperatureFahrenheitEntry,
       "tlpUpsConfigExternalFanActivationTemperatureDegF": tlpUpsConfigExternalFanActivationTemperatureDegF,
       "tlpUpsConfigTemperatureCelsiusTable": tlpUpsConfigTemperatureCelsiusTable,
       "tlpUpsConfigTemperatureCelsiusEntry": tlpUpsConfigTemperatureCelsiusEntry,
       "tlpUpsConfigExternalFanActivationTemperatureDegC": tlpUpsConfigExternalFanActivationTemperatureDegC,
       "tlpPdu": tlpPdu,
       "tlpPduIdent": tlpPduIdent,
       "tlpPduIdentNumPdu": tlpPduIdentNumPdu,
       "tlpPduIdentTable": tlpPduIdentTable,
       "tlpPduIdentEntry": tlpPduIdentEntry,
       "tlpPduIdentNumInputs": tlpPduIdentNumInputs,
       "tlpPduIdentNumOutputs": tlpPduIdentNumOutputs,
       "tlpPduIdentNumPhases": tlpPduIdentNumPhases,
       "tlpPduIdentNumOutlets": tlpPduIdentNumOutlets,
       "tlpPduIdentNumOutletGroups": tlpPduIdentNumOutletGroups,
       "tlpPduIdentNumCircuits": tlpPduIdentNumCircuits,
       "tlpPduIdentNumBreakers": tlpPduIdentNumBreakers,
       "tlpPduIdentNumHeatsinks": tlpPduIdentNumHeatsinks,
       "tlpPduSupportsTable": tlpPduSupportsTable,
       "tlpPduSupportsEntry": tlpPduSupportsEntry,
       "tlpPduSupportsEnergywise": tlpPduSupportsEnergywise,
       "tlpPduSupportsRampShed": tlpPduSupportsRampShed,
       "tlpPduSupportsOutletGroup": tlpPduSupportsOutletGroup,
       "tlpPduSupportsOutletCurrent": tlpPduSupportsOutletCurrent,
       "tlpPduSupportsOutletVoltage": tlpPduSupportsOutletVoltage,
       "tlpPduSupportsOutletActivePower": tlpPduSupportsOutletActivePower,
       "tlpPduDisplayTable": tlpPduDisplayTable,
       "tlpPduDisplayEntry": tlpPduDisplayEntry,
       "tlpPduDisplayScheme": tlpPduDisplayScheme,
       "tlpPduDisplayOrientation": tlpPduDisplayOrientation,
       "tlpPduDisplayAutoScroll": tlpPduDisplayAutoScroll,
       "tlpPduDisplayIntensity": tlpPduDisplayIntensity,
       "tlpPduDisplayUnits": tlpPduDisplayUnits,
       "tlpPduDevice": tlpPduDevice,
       "tlpPduDeviceTable": tlpPduDeviceTable,
       "tlpPduDeviceEntry": tlpPduDeviceEntry,
       "tlpPduDeviceMainLoadState": tlpPduDeviceMainLoadState,
       "tlpPduDeviceMainLoadControllable": tlpPduDeviceMainLoadControllable,
       "tlpPduDeviceMainLoadCommand": tlpPduDeviceMainLoadCommand,
       "tlpPduDevicePowerOnDelay": tlpPduDevicePowerOnDelay,
       "tlpPduDeviceTotalInputPowerRating": tlpPduDeviceTotalInputPowerRating,
       "tlpPduDeviceTemperatureC": tlpPduDeviceTemperatureC,
       "tlpPduDeviceTemperatureF": tlpPduDeviceTemperatureF,
       "tlpPduDevicePhaseImbalance": tlpPduDevicePhaseImbalance,
       "tlpPduDeviceOutputActivePowerTotal": tlpPduDeviceOutputActivePowerTotal,
       "tlpPduDeviceAggregatePowerFactor": tlpPduDeviceAggregatePowerFactor,
       "tlpPduDeviceOutputCurrentPrecision": tlpPduDeviceOutputCurrentPrecision,
       "tlpPduDeviceGeneralFault": tlpPduDeviceGeneralFault,
       "tlpPduDeviceTotalOutputUtilization": tlpPduDeviceTotalOutputUtilization,
       "tlpPduDeviceOutputApparentPowerTotal": tlpPduDeviceOutputApparentPowerTotal,
       "tlpPduDeviceOutputReactivePowerTotal": tlpPduDeviceOutputReactivePowerTotal,
       "tlpPduDeviceOutputCurrentTotal": tlpPduDeviceOutputCurrentTotal,
       "tlpPduDeviceWattHoursTotal": tlpPduDeviceWattHoursTotal,
       "tlpPduDevicePeakPowerTotal": tlpPduDevicePeakPowerTotal,
       "tlpPduDevice24hrEnergyTotal": tlpPduDevice24hrEnergyTotal,
       "tlpPduDetail": tlpPduDetail,
       "tlpPduInput": tlpPduInput,
       "tlpPduInputTable": tlpPduInputTable,
       "tlpPduInputEntry": tlpPduInputEntry,
       "tlpPduInputNominalVoltage": tlpPduInputNominalVoltage,
       "tlpPduInputNominalVoltagePhaseToPhase": tlpPduInputNominalVoltagePhaseToPhase,
       "tlpPduInputNominalVoltagePhaseToNeutral": tlpPduInputNominalVoltagePhaseToNeutral,
       "tlpPduInputLowTransferVoltage": tlpPduInputLowTransferVoltage,
       "tlpPduInputLowTransferVoltageLowerBound": tlpPduInputLowTransferVoltageLowerBound,
       "tlpPduInputLowTransferVoltageUpperBound": tlpPduInputLowTransferVoltageUpperBound,
       "tlpPduInputHighTransferVoltage": tlpPduInputHighTransferVoltage,
       "tlpPduInputHighTransferVoltageLowerBound": tlpPduInputHighTransferVoltageLowerBound,
       "tlpPduInputHighTransferVoltageUpperBound": tlpPduInputHighTransferVoltageUpperBound,
       "tlpPduInputCurrentLimit": tlpPduInputCurrentLimit,
       "tlpPduInputCurrentTotal": tlpPduInputCurrentTotal,
       "tlpPduInputPhaseTable": tlpPduInputPhaseTable,
       "tlpPduInputPhaseEntry": tlpPduInputPhaseEntry,
       "tlpPduInputPhaseIndex": tlpPduInputPhaseIndex,
       "tlpPduInputPhasePhaseType": tlpPduInputPhasePhaseType,
       "tlpPduInputPhaseFrequency": tlpPduInputPhaseFrequency,
       "tlpPduInputPhaseVoltage": tlpPduInputPhaseVoltage,
       "tlpPduInputPhaseVoltageMin": tlpPduInputPhaseVoltageMin,
       "tlpPduInputPhaseVoltageMax": tlpPduInputPhaseVoltageMax,
       "tlpPduInputPhaseCurrent": tlpPduInputPhaseCurrent,
       "tlpPduInputPhasePower": tlpPduInputPhasePower,
       "tlpPduInputPhaseThdVoltage": tlpPduInputPhaseThdVoltage,
       "tlpPduOutput": tlpPduOutput,
       "tlpPduOutputTable": tlpPduOutputTable,
       "tlpPduOutputEntry": tlpPduOutputEntry,
       "tlpPduOutputIndex": tlpPduOutputIndex,
       "tlpPduOutputPhase": tlpPduOutputPhase,
       "tlpPduOutputPhaseType": tlpPduOutputPhaseType,
       "tlpPduOutputVoltage": tlpPduOutputVoltage,
       "tlpPduOutputCurrent": tlpPduOutputCurrent,
       "tlpPduOutputCurrentMin": tlpPduOutputCurrentMin,
       "tlpPduOutputCurrentMax": tlpPduOutputCurrentMax,
       "tlpPduOutputActivePower": tlpPduOutputActivePower,
       "tlpPduOutputPowerFactor": tlpPduOutputPowerFactor,
       "tlpPduOutputSource": tlpPduOutputSource,
       "tlpPduOutputFrequency": tlpPduOutputFrequency,
       "tlpPduOutputPowerKVA": tlpPduOutputPowerKVA,
       "tlpPduOutputPowerKW": tlpPduOutputPowerKW,
       "tlpPduOutput24hrEnergy": tlpPduOutput24hrEnergy,
       "tlpPduOutputApparentPower": tlpPduOutputApparentPower,
       "tlpPduOutputReactivePower": tlpPduOutputReactivePower,
       "tlpPduOutputUtilization": tlpPduOutputUtilization,
       "tlpPduOutputWattHours": tlpPduOutputWattHours,
       "tlpPduOutputPeakPower": tlpPduOutputPeakPower,
       "tlpPduOutlet": tlpPduOutlet,
       "tlpPduOutletTable": tlpPduOutletTable,
       "tlpPduOutletEntry": tlpPduOutletEntry,
       "tlpPduOutletIndex": tlpPduOutletIndex,
       "tlpPduOutletName": tlpPduOutletName,
       "tlpPduOutletDescription": tlpPduOutletDescription,
       "tlpPduOutletState": tlpPduOutletState,
       "tlpPduOutletControllable": tlpPduOutletControllable,
       "tlpPduOutletCommand": tlpPduOutletCommand,
       "tlpPduOutletVoltage": tlpPduOutletVoltage,
       "tlpPduOutletCurrent": tlpPduOutletCurrent,
       "tlpPduOutletActivePower": tlpPduOutletActivePower,
       "tlpPduOutletRampAction": tlpPduOutletRampAction,
       "tlpPduOutletRampDelay": tlpPduOutletRampDelay,
       "tlpPduOutletShedAction": tlpPduOutletShedAction,
       "tlpPduOutletShedDelay": tlpPduOutletShedDelay,
       "tlpPduOutletGroup": tlpPduOutletGroup,
       "tlpPduOutletBank": tlpPduOutletBank,
       "tlpPduOutletCircuit": tlpPduOutletCircuit,
       "tlpPduOutletPhase": tlpPduOutletPhase,
       "tlpPduOutletReceptacleType": tlpPduOutletReceptacleType,
       "tlpPduOutletPowerFactor": tlpPduOutletPowerFactor,
       "tlpPduOutletApparentPower": tlpPduOutletApparentPower,
       "tlpPduOutletReactivePower": tlpPduOutletReactivePower,
       "tlpPduOutletFrequency": tlpPduOutletFrequency,
       "tlpPduOutletUtilization": tlpPduOutletUtilization,
       "tlpPduOutlet24hrEnergy": tlpPduOutlet24hrEnergy,
       "tlpPduOutletOvercurrent": tlpPduOutletOvercurrent,
       "tlpPduOutletGroupTable": tlpPduOutletGroupTable,
       "tlpPduOutletGroupEntry": tlpPduOutletGroupEntry,
       "tlpPduOutletGroupIndex": tlpPduOutletGroupIndex,
       "tlpPduOutletGroupRowStatus": tlpPduOutletGroupRowStatus,
       "tlpPduOutletGroupName": tlpPduOutletGroupName,
       "tlpPduOutletGroupDescription": tlpPduOutletGroupDescription,
       "tlpPduOutletGroupState": tlpPduOutletGroupState,
       "tlpPduOutletGroupCommand": tlpPduOutletGroupCommand,
       "tlpPduCircuit": tlpPduCircuit,
       "tlpPduCircuitTable": tlpPduCircuitTable,
       "tlpPduCircuitEntry": tlpPduCircuitEntry,
       "tlpPduCircuitIndex": tlpPduCircuitIndex,
       "tlpPduCircuitPhase": tlpPduCircuitPhase,
       "tlpPduCircuitInputVoltage": tlpPduCircuitInputVoltage,
       "tlpPduCircuitTotalCurrent": tlpPduCircuitTotalCurrent,
       "tlpPduCircuitCurrentLimit": tlpPduCircuitCurrentLimit,
       "tlpPduCircuitCurrentMin": tlpPduCircuitCurrentMin,
       "tlpPduCircuitCurrentMax": tlpPduCircuitCurrentMax,
       "tlpPduCircuitTotalPower": tlpPduCircuitTotalPower,
       "tlpPduCircuitPowerFactor": tlpPduCircuitPowerFactor,
       "tlpPduCircuitUtilization": tlpPduCircuitUtilization,
       "tlpPduCircuitApparentPower": tlpPduCircuitApparentPower,
       "tlpPduCircuitReactivePower": tlpPduCircuitReactivePower,
       "tlpPduCircuitFrequency": tlpPduCircuitFrequency,
       "tlpPduCircuitWattHours": tlpPduCircuitWattHours,
       "tlpPduCircuitPeakPower": tlpPduCircuitPeakPower,
       "tlpPduBreaker": tlpPduBreaker,
       "tlpPduBreakerTable": tlpPduBreakerTable,
       "tlpPduBreakerEntry": tlpPduBreakerEntry,
       "tlpPduBreakerIndex": tlpPduBreakerIndex,
       "tlpPduBreakerStatus": tlpPduBreakerStatus,
       "tlpPduHeatsink": tlpPduHeatsink,
       "tlpPduHeatsinkTable": tlpPduHeatsinkTable,
       "tlpPduHeatsinkEntry": tlpPduHeatsinkEntry,
       "tlpPduHeatsinkIndex": tlpPduHeatsinkIndex,
       "tlpPduHeatsinkStatus": tlpPduHeatsinkStatus,
       "tlpPduHeatsinkTemperatureC": tlpPduHeatsinkTemperatureC,
       "tlpPduHeatsinkTemperatureF": tlpPduHeatsinkTemperatureF,
       "tlpPduControl": tlpPduControl,
       "tlpPduControlTable": tlpPduControlTable,
       "tlpPduControlEntry": tlpPduControlEntry,
       "tlpPduControlRamp": tlpPduControlRamp,
       "tlpPduControlShed": tlpPduControlShed,
       "tlpPduControlPduOn": tlpPduControlPduOn,
       "tlpPduControlPduOff": tlpPduControlPduOff,
       "tlpPduControlPduRestart": tlpPduControlPduRestart,
       "tlpPduControlResetGeneralFault": tlpPduControlResetGeneralFault,
       "tlpPduControlResetWattHours": tlpPduControlResetWattHours,
       "tlpPduControlResetPeakPower": tlpPduControlResetPeakPower,
       "tlpPduControlClearEventLog": tlpPduControlClearEventLog,
       "tlpPduControlOutputPhaseTable": tlpPduControlOutputPhaseTable,
       "tlpPduControlOutputPhaseEntry": tlpPduControlOutputPhaseEntry,
       "tlpPduControlResetOutputCurrentMinMax": tlpPduControlResetOutputCurrentMinMax,
       "tlpPduControlInputPhaseTable": tlpPduControlInputPhaseTable,
       "tlpPduControlInputPhaseEntry": tlpPduControlInputPhaseEntry,
       "tlpPduControlResetInputVoltageMinMax": tlpPduControlResetInputVoltageMinMax,
       "tlpPduConfig": tlpPduConfig,
       "tlpPduConfigTable": tlpPduConfigTable,
       "tlpPduConfigEntry": tlpPduConfigEntry,
       "tlpPduConfigInputVoltage": tlpPduConfigInputVoltage,
       "tlpPduConfigIsoBreakerSetting": tlpPduConfigIsoBreakerSetting,
       "tlpPduConfigRelayCalibrationSetting": tlpPduConfigRelayCalibrationSetting,
       "tlpPduConfigThdSetting": tlpPduConfigThdSetting,
       "tlpPduConfigWaveformCaptureSetting": tlpPduConfigWaveformCaptureSetting,
       "tlpPduConfigRemoteResetSetting": tlpPduConfigRemoteResetSetting,
       "tlpPduConfigOutputPhaseThresholdTable": tlpPduConfigOutputPhaseThresholdTable,
       "tlpPduConfigOutputPhaseThresholdEntry": tlpPduConfigOutputPhaseThresholdEntry,
       "tlpPduConfigOutputCurrentThresholdTolerance": tlpPduConfigOutputCurrentThresholdTolerance,
       "tlpPduConfigOutputCurrentHighThreshold": tlpPduConfigOutputCurrentHighThreshold,
       "tlpPduConfigOutputCurrentLowThreshold": tlpPduConfigOutputCurrentLowThreshold,
       "tlpPduConfigOutputVoltageThresholdTolerance": tlpPduConfigOutputVoltageThresholdTolerance,
       "tlpPduConfigOutputVoltageHighCriticalThreshold": tlpPduConfigOutputVoltageHighCriticalThreshold,
       "tlpPduConfigOutputVoltageHighWarningThreshold": tlpPduConfigOutputVoltageHighWarningThreshold,
       "tlpPduConfigOutputVoltageLowWarningThreshold": tlpPduConfigOutputVoltageLowWarningThreshold,
       "tlpPduConfigOutputVoltageLowCriticalThreshold": tlpPduConfigOutputVoltageLowCriticalThreshold,
       "tlpPduConfigInputPhaseThresholdTable": tlpPduConfigInputPhaseThresholdTable,
       "tlpPduConfigInputPhaseThresholdEntry": tlpPduConfigInputPhaseThresholdEntry,
       "tlpPduConfigInputVoltageThresholdTolerance": tlpPduConfigInputVoltageThresholdTolerance,
       "tlpPduConfigInputVoltageHighCriticalThreshold": tlpPduConfigInputVoltageHighCriticalThreshold,
       "tlpPduConfigInputVoltageHighWarningThreshold": tlpPduConfigInputVoltageHighWarningThreshold,
       "tlpPduConfigInputVoltageLowWarningThreshold": tlpPduConfigInputVoltageLowWarningThreshold,
       "tlpPduConfigInputVoltageLowCriticalThreshold": tlpPduConfigInputVoltageLowCriticalThreshold,
       "tlpPduConfigThresholdTable": tlpPduConfigThresholdTable,
       "tlpPduConfigThresholdEntry": tlpPduConfigThresholdEntry,
       "tlpPduConfigThdOutOfRangeThreshold": tlpPduConfigThdOutOfRangeThreshold,
       "tlpEnvirosense": tlpEnvirosense,
       "tlpEnvIdent": tlpEnvIdent,
       "tlpEnvIdentNumEnvirosense": tlpEnvIdentNumEnvirosense,
       "tlpEnvIdentTable": tlpEnvIdentTable,
       "tlpEnvIdentEntry": tlpEnvIdentEntry,
       "tlpEnvIdentTempSupported": tlpEnvIdentTempSupported,
       "tlpEnvIdentHumiditySupported": tlpEnvIdentHumiditySupported,
       "tlpEnvNumInputContacts": tlpEnvNumInputContacts,
       "tlpEnvNumOutputContacts": tlpEnvNumOutputContacts,
       "tlpEnvDetail": tlpEnvDetail,
       "tlpEnvTemperatureTable": tlpEnvTemperatureTable,
       "tlpEnvTemperatureEntry": tlpEnvTemperatureEntry,
       "tlpEnvTemperatureC": tlpEnvTemperatureC,
       "tlpEnvTemperatureF": tlpEnvTemperatureF,
       "tlpEnvTemperatureInAlarm": tlpEnvTemperatureInAlarm,
       "tlpEnvHumidityTable": tlpEnvHumidityTable,
       "tlpEnvHumidityEntry": tlpEnvHumidityEntry,
       "tlpEnvHumidityHumidity": tlpEnvHumidityHumidity,
       "tlpEnvHumidityInAlarm": tlpEnvHumidityInAlarm,
       "tlpEnvInputContactTable": tlpEnvInputContactTable,
       "tlpEnvInputContactEntry": tlpEnvInputContactEntry,
       "tlpEnvInputContactIndex": tlpEnvInputContactIndex,
       "tlpEnvInputContactName": tlpEnvInputContactName,
       "tlpEnvInputContactNormalState": tlpEnvInputContactNormalState,
       "tlpEnvInputContactCurrentState": tlpEnvInputContactCurrentState,
       "tlpEnvInputContactInAlarm": tlpEnvInputContactInAlarm,
       "tlpEnvOutputContactTable": tlpEnvOutputContactTable,
       "tlpEnvOutputContactEntry": tlpEnvOutputContactEntry,
       "tlpEnvOutputContactIndex": tlpEnvOutputContactIndex,
       "tlpEnvOutputContactName": tlpEnvOutputContactName,
       "tlpEnvOutputContactNormalState": tlpEnvOutputContactNormalState,
       "tlpEnvOutputContactCurrentState": tlpEnvOutputContactCurrentState,
       "tlpEnvOutputContactInAlarm": tlpEnvOutputContactInAlarm,
       "tlpEnvControl": tlpEnvControl,
       "tlpEnvControlOutputContactTable": tlpEnvControlOutputContactTable,
       "tlpEnvControlOutputContactEntry": tlpEnvControlOutputContactEntry,
       "tlpEnvControlOutputContactOpen": tlpEnvControlOutputContactOpen,
       "tlpEnvControlOutputContactClose": tlpEnvControlOutputContactClose,
       "tlpEnvConfig": tlpEnvConfig,
       "tlpEnvConfigTable": tlpEnvConfigTable,
       "tlpEnvConfigEntry": tlpEnvConfigEntry,
       "tlpEnvTemperatureLowLimit": tlpEnvTemperatureLowLimit,
       "tlpEnvTemperatureHighLimit": tlpEnvTemperatureHighLimit,
       "tlpEnvHumidityLowLimit": tlpEnvHumidityLowLimit,
       "tlpEnvHumidityHighLimit": tlpEnvHumidityHighLimit,
       "tlpAts": tlpAts,
       "tlpAtsIdent": tlpAtsIdent,
       "tlpAtsIdentNumAts": tlpAtsIdentNumAts,
       "tlpAtsIdentTable": tlpAtsIdentTable,
       "tlpAtsIdentEntry": tlpAtsIdentEntry,
       "tlpAtsIdentNumInputs": tlpAtsIdentNumInputs,
       "tlpAtsIdentNumOutputs": tlpAtsIdentNumOutputs,
       "tlpAtsIdentNumPhases": tlpAtsIdentNumPhases,
       "tlpAtsIdentNumOutlets": tlpAtsIdentNumOutlets,
       "tlpAtsIdentNumOutletGroups": tlpAtsIdentNumOutletGroups,
       "tlpAtsIdentNumCircuits": tlpAtsIdentNumCircuits,
       "tlpAtsIdentNumBreakers": tlpAtsIdentNumBreakers,
       "tlpAtsIdentNumHeatsinks": tlpAtsIdentNumHeatsinks,
       "tlpAtsSupportsTable": tlpAtsSupportsTable,
       "tlpAtsSupportsEntry": tlpAtsSupportsEntry,
       "tlpAtsSupportsEnergywise": tlpAtsSupportsEnergywise,
       "tlpAtsSupportsRampShed": tlpAtsSupportsRampShed,
       "tlpAtsSupportsOutletGroup": tlpAtsSupportsOutletGroup,
       "tlpAtsSupportsOutletCurrent": tlpAtsSupportsOutletCurrent,
       "tlpAtsSupportsOutletVoltage": tlpAtsSupportsOutletVoltage,
       "tlpAtsSupportsOutletActivePower": tlpAtsSupportsOutletActivePower,
       "tlpAtsDisplayTable": tlpAtsDisplayTable,
       "tlpAtsDisplayEntry": tlpAtsDisplayEntry,
       "tlpAtsDisplayScheme": tlpAtsDisplayScheme,
       "tlpAtsDisplayOrientation": tlpAtsDisplayOrientation,
       "tlpAtsDisplayAutoScroll": tlpAtsDisplayAutoScroll,
       "tlpAtsDisplayIntensity": tlpAtsDisplayIntensity,
       "tlpAtsDisplayUnits": tlpAtsDisplayUnits,
       "tlpAtsDevice": tlpAtsDevice,
       "tlpAtsDeviceTable": tlpAtsDeviceTable,
       "tlpAtsDeviceEntry": tlpAtsDeviceEntry,
       "tlpAtsDeviceMainLoadState": tlpAtsDeviceMainLoadState,
       "tlpAtsDeviceMainLoadControllable": tlpAtsDeviceMainLoadControllable,
       "tlpAtsDeviceMainLoadCommand": tlpAtsDeviceMainLoadCommand,
       "tlpAtsDevicePowerOnDelay": tlpAtsDevicePowerOnDelay,
       "tlpAtsDeviceTotalInputPowerRating": tlpAtsDeviceTotalInputPowerRating,
       "tlpAtsDeviceTemperatureC": tlpAtsDeviceTemperatureC,
       "tlpAtsDeviceTemperatureF": tlpAtsDeviceTemperatureF,
       "tlpAtsDevicePhaseImbalance": tlpAtsDevicePhaseImbalance,
       "tlpAtsDeviceOutputActivePowerTotal": tlpAtsDeviceOutputActivePowerTotal,
       "tlpAtsDeviceAggregatePowerFactor": tlpAtsDeviceAggregatePowerFactor,
       "tlpAtsDeviceOutputCurrentPrecision": tlpAtsDeviceOutputCurrentPrecision,
       "tlpAtsDeviceGeneralFault": tlpAtsDeviceGeneralFault,
       "tlpAtsDeviceTotalOutputUtilization": tlpAtsDeviceTotalOutputUtilization,
       "tlpAtsDeviceOutputApparentPowerTotal": tlpAtsDeviceOutputApparentPowerTotal,
       "tlpAtsDeviceOutputReactivePowerTotal": tlpAtsDeviceOutputReactivePowerTotal,
       "tlpAtsDeviceOutputCurrentTotal": tlpAtsDeviceOutputCurrentTotal,
       "tlpAtsDeviceWattHoursTotal": tlpAtsDeviceWattHoursTotal,
       "tlpAtsDevicePeakPowerTotal": tlpAtsDevicePeakPowerTotal,
       "tlpAtsDevice24hrEnergyTotal": tlpAtsDevice24hrEnergyTotal,
       "tlpAtsDetail": tlpAtsDetail,
       "tlpAtsInput": tlpAtsInput,
       "tlpAtsInputTable": tlpAtsInputTable,
       "tlpAtsInputEntry": tlpAtsInputEntry,
       "tlpAtsInputNominalVoltage": tlpAtsInputNominalVoltage,
       "tlpAtsInputNominalVoltagePhaseToPhase": tlpAtsInputNominalVoltagePhaseToPhase,
       "tlpAtsInputNominalVoltagePhaseToNeutral": tlpAtsInputNominalVoltagePhaseToNeutral,
       "tlpAtsInputLowTransferVoltage": tlpAtsInputLowTransferVoltage,
       "tlpAtsInputLowTransferVoltageLowerBound": tlpAtsInputLowTransferVoltageLowerBound,
       "tlpAtsInputLowTransferVoltageUpperBound": tlpAtsInputLowTransferVoltageUpperBound,
       "tlpAtsInputHighTransferVoltage": tlpAtsInputHighTransferVoltage,
       "tlpAtsInputHighTransferVoltageLowerBound": tlpAtsInputHighTransferVoltageLowerBound,
       "tlpAtsInputHighTransferVoltageUpperBound": tlpAtsInputHighTransferVoltageUpperBound,
       "tlpAtsInputFairVoltageThreshold": tlpAtsInputFairVoltageThreshold,
       "tlpAtsInputBadVoltageThreshold": tlpAtsInputBadVoltageThreshold,
       "tlpAtsInputSourceAvailability": tlpAtsInputSourceAvailability,
       "tlpAtsInputSourceInUse": tlpAtsInputSourceInUse,
       "tlpAtsInputSourceTransitionCount": tlpAtsInputSourceTransitionCount,
       "tlpAtsInputCurrentLimit": tlpAtsInputCurrentLimit,
       "tlpAtsInputCurrentTotal": tlpAtsInputCurrentTotal,
       "tlpAtsInputPhaseTable": tlpAtsInputPhaseTable,
       "tlpAtsInputPhaseEntry": tlpAtsInputPhaseEntry,
       "tlpAtsInputLineIndex": tlpAtsInputLineIndex,
       "tlpAtsInputPhaseIndex": tlpAtsInputPhaseIndex,
       "tlpAtsInputPhaseType": tlpAtsInputPhaseType,
       "tlpAtsInputPhaseFrequency": tlpAtsInputPhaseFrequency,
       "tlpAtsInputPhaseVoltage": tlpAtsInputPhaseVoltage,
       "tlpAtsInputPhaseVoltageMin": tlpAtsInputPhaseVoltageMin,
       "tlpAtsInputPhaseVoltageMax": tlpAtsInputPhaseVoltageMax,
       "tlpAtsInputPhaseCurrent": tlpAtsInputPhaseCurrent,
       "tlpAtsInputPhasePower": tlpAtsInputPhasePower,
       "tlpAtsInputPhaseThdVoltage": tlpAtsInputPhaseThdVoltage,
       "tlpAtsOutput": tlpAtsOutput,
       "tlpAtsOutputTable": tlpAtsOutputTable,
       "tlpAtsOutputEntry": tlpAtsOutputEntry,
       "tlpAtsOutputIndex": tlpAtsOutputIndex,
       "tlpAtsOutputPhase": tlpAtsOutputPhase,
       "tlpAtsOutputPhaseType": tlpAtsOutputPhaseType,
       "tlpAtsOutputVoltage": tlpAtsOutputVoltage,
       "tlpAtsOutputCurrent": tlpAtsOutputCurrent,
       "tlpAtsOutputCurrentMin": tlpAtsOutputCurrentMin,
       "tlpAtsOutputCurrentMax": tlpAtsOutputCurrentMax,
       "tlpAtsOutputActivePower": tlpAtsOutputActivePower,
       "tlpAtsOutputPowerFactor": tlpAtsOutputPowerFactor,
       "tlpAtsOutputSource": tlpAtsOutputSource,
       "tlpAtsOutputFrequency": tlpAtsOutputFrequency,
       "tlpAtsOutputPowerKVA": tlpAtsOutputPowerKVA,
       "tlpAtsOutputPowerKW": tlpAtsOutputPowerKW,
       "tlpAtsOutput24hrEnergy": tlpAtsOutput24hrEnergy,
       "tlpAtsOutputApparentPower": tlpAtsOutputApparentPower,
       "tlpAtsOutputReactivePower": tlpAtsOutputReactivePower,
       "tlpAtsOutputUtilization": tlpAtsOutputUtilization,
       "tlpAtsOutputWattHours": tlpAtsOutputWattHours,
       "tlpAtsOutputPeakPower": tlpAtsOutputPeakPower,
       "tlpAtsOutlet": tlpAtsOutlet,
       "tlpAtsOutletTable": tlpAtsOutletTable,
       "tlpAtsOutletEntry": tlpAtsOutletEntry,
       "tlpAtsOutletIndex": tlpAtsOutletIndex,
       "tlpAtsOutletName": tlpAtsOutletName,
       "tlpAtsOutletDescription": tlpAtsOutletDescription,
       "tlpAtsOutletState": tlpAtsOutletState,
       "tlpAtsOutletControllable": tlpAtsOutletControllable,
       "tlpAtsOutletCommand": tlpAtsOutletCommand,
       "tlpAtsOutletVoltage": tlpAtsOutletVoltage,
       "tlpAtsOutletCurrent": tlpAtsOutletCurrent,
       "tlpAtsOutletActivePower": tlpAtsOutletActivePower,
       "tlpAtsOutletRampAction": tlpAtsOutletRampAction,
       "tlpAtsOutletRampDelay": tlpAtsOutletRampDelay,
       "tlpAtsOutletShedAction": tlpAtsOutletShedAction,
       "tlpAtsOutletShedDelay": tlpAtsOutletShedDelay,
       "tlpAtsOutletGroup": tlpAtsOutletGroup,
       "tlpAtsOutletBank": tlpAtsOutletBank,
       "tlpAtsOutletCircuit": tlpAtsOutletCircuit,
       "tlpAtsOutletPhase": tlpAtsOutletPhase,
       "tlpAtsOutletReceptacleType": tlpAtsOutletReceptacleType,
       "tlpAtsOutletPowerFactor": tlpAtsOutletPowerFactor,
       "tlpAtsOutletApparentPower": tlpAtsOutletApparentPower,
       "tlpAtsOutletReactivePower": tlpAtsOutletReactivePower,
       "tlpAtsOutletFrequency": tlpAtsOutletFrequency,
       "tlpAtsOutletUtilization": tlpAtsOutletUtilization,
       "tlpAtsOutlet24hrEnergy": tlpAtsOutlet24hrEnergy,
       "tlpAtsOutletOvercurrent": tlpAtsOutletOvercurrent,
       "tlpAtsOutletGroupTable": tlpAtsOutletGroupTable,
       "tlpAtsOutletGroupEntry": tlpAtsOutletGroupEntry,
       "tlpAtsOutletGroupIndex": tlpAtsOutletGroupIndex,
       "tlpAtsOutletGroupRowStatus": tlpAtsOutletGroupRowStatus,
       "tlpAtsOutletGroupName": tlpAtsOutletGroupName,
       "tlpAtsOutletGroupDescription": tlpAtsOutletGroupDescription,
       "tlpAtsOutletGroupState": tlpAtsOutletGroupState,
       "tlpAtsOutletGroupCommand": tlpAtsOutletGroupCommand,
       "tlpAtsCircuit": tlpAtsCircuit,
       "tlpAtsCircuitTable": tlpAtsCircuitTable,
       "tlpAtsCircuitEntry": tlpAtsCircuitEntry,
       "tlpAtsCircuitIndex": tlpAtsCircuitIndex,
       "tlpAtsCircuitPhase": tlpAtsCircuitPhase,
       "tlpAtsCircuitInputVoltage": tlpAtsCircuitInputVoltage,
       "tlpAtsCircuitTotalCurrent": tlpAtsCircuitTotalCurrent,
       "tlpAtsCircuitCurrentLimit": tlpAtsCircuitCurrentLimit,
       "tlpAtsCircuitCurrentMin": tlpAtsCircuitCurrentMin,
       "tlpAtsCircuitCurrentMax": tlpAtsCircuitCurrentMax,
       "tlpAtsCircuitTotalPower": tlpAtsCircuitTotalPower,
       "tlpAtsCircuitPowerFactor": tlpAtsCircuitPowerFactor,
       "tlpAtsCircuitUtilization": tlpAtsCircuitUtilization,
       "tlpAtsCircuitApparentPower": tlpAtsCircuitApparentPower,
       "tlpAtsCircuitReactivePower": tlpAtsCircuitReactivePower,
       "tlpAtsCircuitFrequency": tlpAtsCircuitFrequency,
       "tlpAtsCircuitWattHours": tlpAtsCircuitWattHours,
       "tlpAtsCircuitPeakPower": tlpAtsCircuitPeakPower,
       "tlpAtsBreaker": tlpAtsBreaker,
       "tlpAtsBreakerTable": tlpAtsBreakerTable,
       "tlpAtsBreakerEntry": tlpAtsBreakerEntry,
       "tlpAtsBreakerIndex": tlpAtsBreakerIndex,
       "tlpAtsBreakerStatus": tlpAtsBreakerStatus,
       "tlpAtsHeatsink": tlpAtsHeatsink,
       "tlpAtsHeatsinkTable": tlpAtsHeatsinkTable,
       "tlpAtsHeatsinkEntry": tlpAtsHeatsinkEntry,
       "tlpAtsHeatsinkIndex": tlpAtsHeatsinkIndex,
       "tlpAtsHeatsinkStatus": tlpAtsHeatsinkStatus,
       "tlpAtsHeatsinkTemperatureC": tlpAtsHeatsinkTemperatureC,
       "tlpAtsHeatsinkTemperatureF": tlpAtsHeatsinkTemperatureF,
       "tlpAtsControl": tlpAtsControl,
       "tlpAtsControlTable": tlpAtsControlTable,
       "tlpAtsControlEntry": tlpAtsControlEntry,
       "tlpAtsControlRamp": tlpAtsControlRamp,
       "tlpAtsControlShed": tlpAtsControlShed,
       "tlpAtsControlOn": tlpAtsControlOn,
       "tlpAtsControlOff": tlpAtsControlOff,
       "tlpAtsControlRestart": tlpAtsControlRestart,
       "tlpAtsControlResetGeneralFault": tlpAtsControlResetGeneralFault,
       "tlpAtsControlResetWattHours": tlpAtsControlResetWattHours,
       "tlpAtsControlResetPeakPower": tlpAtsControlResetPeakPower,
       "tlpAtsControlClearEventLog": tlpAtsControlClearEventLog,
       "tlpAtsControlOutputPhaseTable": tlpAtsControlOutputPhaseTable,
       "tlpAtsControlOutputPhaseEntry": tlpAtsControlOutputPhaseEntry,
       "tlpAtsControlResetOutputCurrentMinMax": tlpAtsControlResetOutputCurrentMinMax,
       "tlpAtsControlInputPhaseTable": tlpAtsControlInputPhaseTable,
       "tlpAtsControlInputPhaseEntry": tlpAtsControlInputPhaseEntry,
       "tlpAtsControlResetInputVoltageMinMax": tlpAtsControlResetInputVoltageMinMax,
       "tlpAtsConfig": tlpAtsConfig,
       "tlpAtsConfigTable": tlpAtsConfigTable,
       "tlpAtsConfigEntry": tlpAtsConfigEntry,
       "tlpAtsConfigInputVoltage": tlpAtsConfigInputVoltage,
       "tlpAtsConfigSourceSelect": tlpAtsConfigSourceSelect,
       "tlpAtsConfigSource1ReturnTime": tlpAtsConfigSource1ReturnTime,
       "tlpAtsConfigSource2ReturnTime": tlpAtsConfigSource2ReturnTime,
       "tlpAtsConfigAutoRampOnTransition": tlpAtsConfigAutoRampOnTransition,
       "tlpAtsConfigAutoShedOnTransition": tlpAtsConfigAutoShedOnTransition,
       "tlpAtsConfigIsoBreakerSetting": tlpAtsConfigIsoBreakerSetting,
       "tlpAtsConfigRelayCalibrationSetting": tlpAtsConfigRelayCalibrationSetting,
       "tlpAtsConfigThdSetting": tlpAtsConfigThdSetting,
       "tlpAtsConfigWaveformCaptureSetting": tlpAtsConfigWaveformCaptureSetting,
       "tlpAtsConfigRemoteResetSetting": tlpAtsConfigRemoteResetSetting,
       "tlpAtsConfigVoltageRangeOldTable": tlpAtsConfigVoltageRangeOldTable,
       "tlpAtsConfigVoltageRangeOldEntry": tlpAtsConfigVoltageRangeOldEntry,
       "tlpAtsConfigHighVoltageTransferOld": tlpAtsConfigHighVoltageTransferOld,
       "tlpAtsConfigHighVoltageResetOld": tlpAtsConfigHighVoltageResetOld,
       "tlpAtsConfigSource1TransferResetOld": tlpAtsConfigSource1TransferResetOld,
       "tlpAtsConfigSource1BrownoutSetOld": tlpAtsConfigSource1BrownoutSetOld,
       "tlpAtsConfigSource1TransferSetOld": tlpAtsConfigSource1TransferSetOld,
       "tlpAtsConfigSource2TransferResetOld": tlpAtsConfigSource2TransferResetOld,
       "tlpAtsConfigSource2BrownoutSetOld": tlpAtsConfigSource2BrownoutSetOld,
       "tlpAtsConfigSource2TransferSetOld": tlpAtsConfigSource2TransferSetOld,
       "tlpAtsConfigLowVoltageResetOld": tlpAtsConfigLowVoltageResetOld,
       "tlpAtsConfigLowVoltageTransferOld": tlpAtsConfigLowVoltageTransferOld,
       "tlpAtsConfigVoltageRangeLimitsTable": tlpAtsConfigVoltageRangeLimitsTable,
       "tlpAtsConfigVoltageRangeLimitsEntry": tlpAtsConfigVoltageRangeLimitsEntry,
       "tlpAtsConfigSourceBrownoutSetMinimum": tlpAtsConfigSourceBrownoutSetMinimum,
       "tlpAtsConfigSourceBrownoutSetMaximum": tlpAtsConfigSourceBrownoutSetMaximum,
       "tlpAtsConfigSourceTransferSetMinimum": tlpAtsConfigSourceTransferSetMinimum,
       "tlpAtsConfigSourceTransferSetMaximum": tlpAtsConfigSourceTransferSetMaximum,
       "tlpAtsConfigThresholdTable": tlpAtsConfigThresholdTable,
       "tlpAtsConfigThresholdEntry": tlpAtsConfigThresholdEntry,
       "tlpAtsConfigOutputCurrentThreshold": tlpAtsConfigOutputCurrentThreshold,
       "tlpAtsConfigOverTemperatureThreshold": tlpAtsConfigOverTemperatureThreshold,
       "tlpAtsConfigOverVoltageThreshold": tlpAtsConfigOverVoltageThreshold,
       "tlpAtsConfigOverLoadThreshold": tlpAtsConfigOverLoadThreshold,
       "tlpAtsConfigThdOutOfRangeThreshold": tlpAtsConfigThdOutOfRangeThreshold,
       "tlpAtsConfigVoltageRangeTable": tlpAtsConfigVoltageRangeTable,
       "tlpAtsConfigVoltageRangeEntry": tlpAtsConfigVoltageRangeEntry,
       "tlpAtsConfigHighVoltageTransfer": tlpAtsConfigHighVoltageTransfer,
       "tlpAtsConfigHighVoltageReset": tlpAtsConfigHighVoltageReset,
       "tlpAtsConfigTransferReset": tlpAtsConfigTransferReset,
       "tlpAtsConfigBrownoutSet": tlpAtsConfigBrownoutSet,
       "tlpAtsConfigTransferSet": tlpAtsConfigTransferSet,
       "tlpAtsConfigLowVoltageReset": tlpAtsConfigLowVoltageReset,
       "tlpAtsConfigLowVoltageTransfer": tlpAtsConfigLowVoltageTransfer,
       "tlpAtsConfigOutputPhaseThresholdTable": tlpAtsConfigOutputPhaseThresholdTable,
       "tlpAtsConfigOutputPhaseThresholdEntry": tlpAtsConfigOutputPhaseThresholdEntry,
       "tlpAtsConfigOutputCurrentThresholdTolerance": tlpAtsConfigOutputCurrentThresholdTolerance,
       "tlpAtsConfigOutputCurrentHighThreshold": tlpAtsConfigOutputCurrentHighThreshold,
       "tlpAtsConfigOutputCurrentLowThreshold": tlpAtsConfigOutputCurrentLowThreshold,
       "tlpAtsConfigOutputVoltageThresholdTolerance": tlpAtsConfigOutputVoltageThresholdTolerance,
       "tlpAtsConfigOutputVoltageHighCriticalThreshold": tlpAtsConfigOutputVoltageHighCriticalThreshold,
       "tlpAtsConfigOutputVoltageHighWarningThreshold": tlpAtsConfigOutputVoltageHighWarningThreshold,
       "tlpAtsConfigOutputVoltageLowWarningThreshold": tlpAtsConfigOutputVoltageLowWarningThreshold,
       "tlpAtsConfigOutputVoltageLowCriticalThreshold": tlpAtsConfigOutputVoltageLowCriticalThreshold,
       "tlpAtsConfigInputPhaseThresholdTable": tlpAtsConfigInputPhaseThresholdTable,
       "tlpAtsConfigInputPhaseThresholdEntry": tlpAtsConfigInputPhaseThresholdEntry,
       "tlpAtsConfigInputVoltageThresholdTolerance": tlpAtsConfigInputVoltageThresholdTolerance,
       "tlpAtsConfigInputVoltageHighCriticalThreshold": tlpAtsConfigInputVoltageHighCriticalThreshold,
       "tlpAtsConfigInputVoltageHighWarningThreshold": tlpAtsConfigInputVoltageHighWarningThreshold,
       "tlpAtsConfigInputVoltageLowWarningThreshold": tlpAtsConfigInputVoltageLowWarningThreshold,
       "tlpAtsConfigInputVoltageLowCriticalThreshold": tlpAtsConfigInputVoltageLowCriticalThreshold,
       "tlpCooling": tlpCooling,
       "tlpCoolingIdent": tlpCoolingIdent,
       "tlpCoolingIdentNumCooling": tlpCoolingIdentNumCooling,
       "tlpCoolingDevice": tlpCoolingDevice,
       "tlpCoolingDetail": tlpCoolingDetail,
       "tlpCoolingTemperature": tlpCoolingTemperature,
       "tlpCoolingTemperatureFahrenheitTable": tlpCoolingTemperatureFahrenheitTable,
       "tlpCoolingTemperatureFahrenheitEntry": tlpCoolingTemperatureFahrenheitEntry,
       "tlpCoolingAmbientDegF": tlpCoolingAmbientDegF,
       "tlpCoolingSupplyAirDegF": tlpCoolingSupplyAirDegF,
       "tlpCoolingReturnAirDegF": tlpCoolingReturnAirDegF,
       "tlpCoolingCondenserInletDegF": tlpCoolingCondenserInletDegF,
       "tlpCoolingEvaporatorDegF": tlpCoolingEvaporatorDegF,
       "tlpCoolingSuctionDegF": tlpCoolingSuctionDegF,
       "tlpCoolingRemoteDegF": tlpCoolingRemoteDegF,
       "tlpCoolingCondenserOutletDegF": tlpCoolingCondenserOutletDegF,
       "tlpCoolingTemperatureCelsiusTable": tlpCoolingTemperatureCelsiusTable,
       "tlpCoolingTemperatureCelsiusEntry": tlpCoolingTemperatureCelsiusEntry,
       "tlpCoolingAmbientDegC": tlpCoolingAmbientDegC,
       "tlpCoolingSupplyAirDegC": tlpCoolingSupplyAirDegC,
       "tlpCoolingReturnAirDegC": tlpCoolingReturnAirDegC,
       "tlpCoolingCondenserInletDegC": tlpCoolingCondenserInletDegC,
       "tlpCoolingEvaporatorDegC": tlpCoolingEvaporatorDegC,
       "tlpCoolingSuctionDegC": tlpCoolingSuctionDegC,
       "tlpCoolingRemoteDegC": tlpCoolingRemoteDegC,
       "tlpCoolingCondenserOutletDegC": tlpCoolingCondenserOutletDegC,
       "tlpCoolingPressure": tlpCoolingPressure,
       "tlpCoolingPressureMpaTable": tlpCoolingPressureMpaTable,
       "tlpCoolingPressureMpaEntry": tlpCoolingPressureMpaEntry,
       "tlpCoolingSuctionPressureMpa": tlpCoolingSuctionPressureMpa,
       "tlpCoolingDischargePressureMpa": tlpCoolingDischargePressureMpa,
       "tlpCoolingPressurePsiTable": tlpCoolingPressurePsiTable,
       "tlpCoolingPressurePsiEntry": tlpCoolingPressurePsiEntry,
       "tlpCoolingSuctionPressurePsi": tlpCoolingSuctionPressurePsi,
       "tlpCoolingDischargePressurePsi": tlpCoolingDischargePressurePsi,
       "tlpCoolingCurrentTable": tlpCoolingCurrentTable,
       "tlpCoolingCurrentEntry": tlpCoolingCurrentEntry,
       "tlpCoolingUnitCurrent": tlpCoolingUnitCurrent,
       "tlpCoolingCompressorCurrent": tlpCoolingCompressorCurrent,
       "tlpCoolingEvaporatorFanCurrent": tlpCoolingEvaporatorFanCurrent,
       "tlpCoolingCondenserFanCurrent": tlpCoolingCondenserFanCurrent,
       "tlpCoolingDynamicTable": tlpCoolingDynamicTable,
       "tlpCoolingDynamicEntry": tlpCoolingDynamicEntry,
       "tlpCoolingEvaporatorFanSpeed": tlpCoolingEvaporatorFanSpeed,
       "tlpCoolingCondenserFanSpeed": tlpCoolingCondenserFanSpeed,
       "tlpCoolingCompressorFrequency": tlpCoolingCompressorFrequency,
       "tlpCoolingEEVSteps": tlpCoolingEEVSteps,
       "tlpCoolingRuntimeTable": tlpCoolingRuntimeTable,
       "tlpCoolingRuntimeEntry": tlpCoolingRuntimeEntry,
       "tlpCoolingCompressorRunDays": tlpCoolingCompressorRunDays,
       "tlpCoolingCondensatePumpRunDays": tlpCoolingCondensatePumpRunDays,
       "tlpCoolingAirFilterRunHours": tlpCoolingAirFilterRunHours,
       "tlpCoolingEvaporatorFanRunDays": tlpCoolingEvaporatorFanRunDays,
       "tlpCoolingCondenserFanRunDays": tlpCoolingCondenserFanRunDays,
       "tlpCoolingAtomizerRunDays": tlpCoolingAtomizerRunDays,
       "tlpCoolingStatusTable": tlpCoolingStatusTable,
       "tlpCoolingStatusEntry": tlpCoolingStatusEntry,
       "tlpCoolingOperatingMode": tlpCoolingOperatingMode,
       "tlpCoolingCoolOutput": tlpCoolingCoolOutput,
       "tlpCoolingAlarmStatus": tlpCoolingAlarmStatus,
       "tlpCoolingCompressorStatus": tlpCoolingCompressorStatus,
       "tlpCoolingWaterStatus": tlpCoolingWaterStatus,
       "tlpCoolingDefrostMode": tlpCoolingDefrostMode,
       "tlpCoolingQuietMode": tlpCoolingQuietMode,
       "tlpCoolingHotGasBypass": tlpCoolingHotGasBypass,
       "tlpCoolingAutoFanSpeed": tlpCoolingAutoFanSpeed,
       "tlpCoolingControl": tlpCoolingControl,
       "tlpCoolingControlTable": tlpCoolingControlTable,
       "tlpCoolingControlEntry": tlpCoolingControlEntry,
       "tlpCoolingMode": tlpCoolingMode,
       "tlpCoolingControlOn": tlpCoolingControlOn,
       "tlpCoolingControlOff": tlpCoolingControlOff,
       "tlpCoolingConfig": tlpCoolingConfig,
       "tlpCoolingConfigTable": tlpCoolingConfigTable,
       "tlpCoolingConfigEntry": tlpCoolingConfigEntry,
       "tlpCoolingConfigAutoStart": tlpCoolingConfigAutoStart,
       "tlpCoolingConfigFanSpeed": tlpCoolingConfigFanSpeed,
       "tlpCoolingConfigControlType": tlpCoolingConfigControlType,
       "tlpCoolingConfigDisplayUnits": tlpCoolingConfigDisplayUnits,
       "tlpCoolingConfigBeepOnKey": tlpCoolingConfigBeepOnKey,
       "tlpCoolingConfigInputContactType": tlpCoolingConfigInputContactType,
       "tlpCoolingConfigOutputContactType": tlpCoolingConfigOutputContactType,
       "tlpCoolingConfigOutputRelaySource": tlpCoolingConfigOutputRelaySource,
       "tlpCoolingConfigOutputRelayDefault": tlpCoolingConfigOutputRelayDefault,
       "tlpCoolingConfigOffOnInputContact": tlpCoolingConfigOffOnInputContact,
       "tlpCoolingConfigOffOnLeak": tlpCoolingConfigOffOnLeak,
       "tlpCoolingConfigWaterLeakContactType": tlpCoolingConfigWaterLeakContactType,
       "tlpCoolingConfigAirFilterInterval": tlpCoolingConfigAirFilterInterval,
       "tlpCoolingConfigAirFilterAlarm": tlpCoolingConfigAirFilterAlarm,
       "tlpCoolingConfigMaxAirFilterRunHours": tlpCoolingConfigMaxAirFilterRunHours,
       "tlpCoolingConfigStartTimer": tlpCoolingConfigStartTimer,
       "tlpCoolingConfigStopTimer": tlpCoolingConfigStopTimer,
       "tlpCoolingConfigEnergyMode": tlpCoolingConfigEnergyMode,
       "tlpCoolingConfigDefrostMode": tlpCoolingConfigDefrostMode,
       "tlpCoolingConfigRemoteTemperatureSensor": tlpCoolingConfigRemoteTemperatureSensor,
       "tlpCoolingConfigDehumidifyingMode": tlpCoolingConfigDehumidifyingMode,
       "tlpCoolingConfigFanAlwaysOn": tlpCoolingConfigFanAlwaysOn,
       "tlpCoolingConfigQuietMode": tlpCoolingConfigQuietMode,
       "tlpCoolingConfigHotGasBypass": tlpCoolingConfigHotGasBypass,
       "tlpCoolingConfigAutoFanSpeed": tlpCoolingConfigAutoFanSpeed,
       "tlpCoolingConfigTemperatureFahrenheitTable": tlpCoolingConfigTemperatureFahrenheitTable,
       "tlpCoolingConfigTemperatureFahrenheitEntry": tlpCoolingConfigTemperatureFahrenheitEntry,
       "tlpCoolingSetPointDegF": tlpCoolingSetPointDegF,
       "tlpCoolingSupplyAirHighLimitDegF": tlpCoolingSupplyAirHighLimitDegF,
       "tlpCoolingSupplyAirLowLimitDegF": tlpCoolingSupplyAirLowLimitDegF,
       "tlpCoolingMaxDeviationLimitDegF": tlpCoolingMaxDeviationLimitDegF,
       "tlpCoolingReturnAirHighLimitDegF": tlpCoolingReturnAirHighLimitDegF,
       "tlpCoolingReturnAirLowLimitDegF": tlpCoolingReturnAirLowLimitDegF,
       "tlpCoolingRemoteSetPointDegF": tlpCoolingRemoteSetPointDegF,
       "tlpCoolingConfigTemperatureCelsiusTable": tlpCoolingConfigTemperatureCelsiusTable,
       "tlpCoolingConfigTemperatureCelsiusEntry": tlpCoolingConfigTemperatureCelsiusEntry,
       "tlpCoolingSetPointDegC": tlpCoolingSetPointDegC,
       "tlpCoolingSupplyAirHighLimitDegC": tlpCoolingSupplyAirHighLimitDegC,
       "tlpCoolingSupplyAirLowLimitDegC": tlpCoolingSupplyAirLowLimitDegC,
       "tlpCoolingMaxDeviationLimitDegC": tlpCoolingMaxDeviationLimitDegC,
       "tlpCoolingReturnAirHighLimitDegC": tlpCoolingReturnAirHighLimitDegC,
       "tlpCoolingReturnAirLowLimitDegC": tlpCoolingReturnAirLowLimitDegC,
       "tlpCoolingRemoteSetPointDegC": tlpCoolingRemoteSetPointDegC,
       "tlpKvm": tlpKvm,
       "tlpKvmIdent": tlpKvmIdent,
       "tlpKvmIdentNumKvm": tlpKvmIdentNumKvm,
       "tlpKvmDevice": tlpKvmDevice,
       "tlpKvmDetail": tlpKvmDetail,
       "tlpKvmControl": tlpKvmControl,
       "tlpKvmConfig": tlpKvmConfig,
       "tlpRackTrack": tlpRackTrack,
       "tlpRackTrackIdent": tlpRackTrackIdent,
       "tlpRackTrackIdentNumRackTrack": tlpRackTrackIdentNumRackTrack,
       "tlpRackTrackDevice": tlpRackTrackDevice,
       "tlpRackTrackDetail": tlpRackTrackDetail,
       "tlpRackTrackControl": tlpRackTrackControl,
       "tlpRackTrackConfig": tlpRackTrackConfig,
       "tlpSwitch": tlpSwitch,
       "tlpSwitchIdent": tlpSwitchIdent,
       "tlpSwitchIdentNumSwitch": tlpSwitchIdentNumSwitch,
       "tlpSwitchDevice": tlpSwitchDevice,
       "tlpSwitchDetail": tlpSwitchDetail,
       "tlpSwitchControl": tlpSwitchControl,
       "tlpSwitchConfig": tlpSwitchConfig,
       "tlpSoftware": tlpSoftware,
       "tlpAgentDetails": tlpAgentDetails,
       "tlpAgentIdent": tlpAgentIdent,
       "tlpAgentType": tlpAgentType,
       "tlpAgentVersion": tlpAgentVersion,
       "tlpAgentDriverVersion": tlpAgentDriverVersion,
       "tlpAgentMAC": tlpAgentMAC,
       "tlpAgentSerialNum": tlpAgentSerialNum,
       "tlpAgentUuid": tlpAgentUuid,
       "tlpAgentAttributes": tlpAgentAttributes,
       "tlpAgentAttributesSupports": tlpAgentAttributesSupports,
       "tlpAgentAttributesSupportsHTTP": tlpAgentAttributesSupportsHTTP,
       "tlpAgentAttributesSupportsHTTPS": tlpAgentAttributesSupportsHTTPS,
       "tlpAgentAttributesSupportsFTP": tlpAgentAttributesSupportsFTP,
       "tlpAgentAttributesSupportsTelnet": tlpAgentAttributesSupportsTelnet,
       "tlpAgentAttributesSupportsObsolete1": tlpAgentAttributesSupportsObsolete1,
       "tlpAgentAttributesSupportsSSH": tlpAgentAttributesSupportsSSH,
       "tlpAgentAttributesSupportsObsolete2": tlpAgentAttributesSupportsObsolete2,
       "tlpAgentAttributesSupportsSNMP": tlpAgentAttributesSupportsSNMP,
       "tlpAgentAttributesSupportsSNMPTrap": tlpAgentAttributesSupportsSNMPTrap,
       "tlpAgentAttributesEnabled": tlpAgentAttributesEnabled,
       "tlpAgentAttributesHTTPEnabled": tlpAgentAttributesHTTPEnabled,
       "tlpAgentAttributesHTTPSEnabled": tlpAgentAttributesHTTPSEnabled,
       "tlpAgentAttributesFTPEnabled": tlpAgentAttributesFTPEnabled,
       "tlpAgentAttributesTelnetEnabled": tlpAgentAttributesTelnetEnabled,
       "tlpAgentAttributesObsolete1Enabled": tlpAgentAttributesObsolete1Enabled,
       "tlpAgentAttributesSSHEnabled": tlpAgentAttributesSSHEnabled,
       "tlpAgentAttributesSFTPEnabled": tlpAgentAttributesSFTPEnabled,
       "tlpAgentAttributesObsolete2Enabled": tlpAgentAttributesObsolete2Enabled,
       "tlpAgentAttributesSnmp": tlpAgentAttributesSnmp,
       "tlpAgentAttributesSNMPv1Enabled": tlpAgentAttributesSNMPv1Enabled,
       "tlpAgentAttributesSNMPv2cEnabled": tlpAgentAttributesSNMPv2cEnabled,
       "tlpAgentAttributesSNMPv3Enabled": tlpAgentAttributesSNMPv3Enabled,
       "tlpAgentAttributesPorts": tlpAgentAttributesPorts,
       "tlpAgentAttributesHTTPPort": tlpAgentAttributesHTTPPort,
       "tlpAgentAttributesHTTPSPort": tlpAgentAttributesHTTPSPort,
       "tlpAgentAttributesFTPPort": tlpAgentAttributesFTPPort,
       "tlpAgentAttributesTelnetPort": tlpAgentAttributesTelnetPort,
       "tlpAgentAttributesObsolete1Port": tlpAgentAttributesObsolete1Port,
       "tlpAgentAttributesSSHPort": tlpAgentAttributesSSHPort,
       "tlpAgentAttributesObsolete2Port": tlpAgentAttributesObsolete2Port,
       "tlpAgentAttributesSNMPPort": tlpAgentAttributesSNMPPort,
       "tlpAgentAttributesSNMPTrapPort": tlpAgentAttributesSNMPTrapPort,
       "tlpAgentAttributesOptions": tlpAgentAttributesOptions,
       "tlpAgentAttributesHTTPRedirected": tlpAgentAttributesHTTPRedirected,
       "tlpAgentAddresses": tlpAgentAddresses,
       "tlpAgentAddressIPv4": tlpAgentAddressIPv4,
       "tlpAgentAddressIPv6": tlpAgentAddressIPv6,
       "tlpAgentSettings": tlpAgentSettings,
       "tlpAgentConfig": tlpAgentConfig,
       "tlpAgentConfigRemoteRegistration": tlpAgentConfigRemoteRegistration,
       "tlpAgentConfigCurrentTime": tlpAgentConfigCurrentTime,
       "tlpAgentContacts": tlpAgentContacts,
       "tlpAgentEmailContacts": tlpAgentEmailContacts,
       "tlpAgentNumEmailContacts": tlpAgentNumEmailContacts,
       "tlpAgentEmailContactTable": tlpAgentEmailContactTable,
       "tlpAgentEmailContactEntry": tlpAgentEmailContactEntry,
       "tlpAgentEmailContactIndex": tlpAgentEmailContactIndex,
       "tlpAgentEmailContactRowStatus": tlpAgentEmailContactRowStatus,
       "tlpAgentEmailContactName": tlpAgentEmailContactName,
       "tlpAgentEmailContactAddress": tlpAgentEmailContactAddress,
       "tlpAgentEmailContactTest": tlpAgentEmailContactTest,
       "tlpAgentSnmpContacts": tlpAgentSnmpContacts,
       "tlpAgentNumSnmpContacts": tlpAgentNumSnmpContacts,
       "tlpAgentSnmpContactTable": tlpAgentSnmpContactTable,
       "tlpAgentSnmpContactEntry": tlpAgentSnmpContactEntry,
       "tlpAgentSnmpContactIndex": tlpAgentSnmpContactIndex,
       "tlpAgentSnmpContactRowStatus": tlpAgentSnmpContactRowStatus,
       "tlpAgentSnmpContactName": tlpAgentSnmpContactName,
       "tlpAgentSnmpContactIpAddress": tlpAgentSnmpContactIpAddress,
       "tlpAgentSnmpContactTrapPort": tlpAgentSnmpContactTrapPort,
       "tlpAgentSnmpContactSnmpVersion": tlpAgentSnmpContactSnmpVersion,
       "tlpAgentSnmpContactSecurityName": tlpAgentSnmpContactSecurityName,
       "tlpAgentSnmpContactPrivPassword": tlpAgentSnmpContactPrivPassword,
       "tlpAgentSnmpContactAuthPassword": tlpAgentSnmpContactAuthPassword,
       "tlpAgentSnmpContactTrapType": tlpAgentSnmpContactTrapType,
       "tlpAgentSnmpContactSetPort": tlpAgentSnmpContactSetPort,
       "tlpAgentSnmpContactSupportsTrap": tlpAgentSnmpContactSupportsTrap,
       "tlpAgentSnmpContactSupportsSet": tlpAgentSnmpContactSupportsSet,
       "tlpAgentSnmpContactTestTrap": tlpAgentSnmpContactTestTrap,
       "tlpAgentSmsContacts": tlpAgentSmsContacts,
       "tlpAgentSmsNumSmsContacts": tlpAgentSmsNumSmsContacts,
       "tlpAgentSmsContactTable": tlpAgentSmsContactTable,
       "tlpAgentSmsContactEntry": tlpAgentSmsContactEntry,
       "tlpAgentSmsContactIndex": tlpAgentSmsContactIndex,
       "tlpAgentSmsContactRowStatus": tlpAgentSmsContactRowStatus,
       "tlpAgentSmsContactName": tlpAgentSmsContactName,
       "tlpAgentSmsContactNumber": tlpAgentSmsContactNumber,
       "tlpAgentSmsContactTest": tlpAgentSmsContactTest,
       "tlpAgentAutoProbe": tlpAgentAutoProbe,
       "tlpAgentAutoProbeNumProbes": tlpAgentAutoProbeNumProbes,
       "tlpAgentAutoProbeTable": tlpAgentAutoProbeTable,
       "tlpAgentAutoProbeEntry": tlpAgentAutoProbeEntry,
       "tlpAgentAutoProbeIndex": tlpAgentAutoProbeIndex,
       "tlpAgentAutoProbeRowStatus": tlpAgentAutoProbeRowStatus,
       "tlpAgentAutoProbeName": tlpAgentAutoProbeName,
       "tlpAgentAutoProbeDescription": tlpAgentAutoProbeDescription,
       "tlpAgentAutoProbeType": tlpAgentAutoProbeType,
       "tlpAgentAutoProbeStatus": tlpAgentAutoProbeStatus,
       "tlpAgentAutoProbeInterval": tlpAgentAutoProbeInterval,
       "tlpAgentAutoProbeRetryCount": tlpAgentAutoProbeRetryCount,
       "tlpAgentAutoProbePrimaryAddress": tlpAgentAutoProbePrimaryAddress,
       "tlpAgentAutoProbePrimaryPort": tlpAgentAutoProbePrimaryPort,
       "tlpAgentAutoProbeSecondaryAddress": tlpAgentAutoProbeSecondaryAddress,
       "tlpAgentAutoProbeSecondaryPort": tlpAgentAutoProbeSecondaryPort,
       "tlpAlarms": tlpAlarms,
       "tlpAlarmsPresent": tlpAlarmsPresent,
       "tlpAlarmTable": tlpAlarmTable,
       "tlpAlarmEntry": tlpAlarmEntry,
       "tlpAlarmId": tlpAlarmId,
       "tlpAlarmDescr": tlpAlarmDescr,
       "tlpAlarmTime": tlpAlarmTime,
       "tlpAlarmTableRef": tlpAlarmTableRef,
       "tlpAlarmTableRowRef": tlpAlarmTableRowRef,
       "tlpAlarmDetail": tlpAlarmDetail,
       "tlpAlarmType": tlpAlarmType,
       "tlpAlarmState": tlpAlarmState,
       "tlpAlarmAcknowledged": tlpAlarmAcknowledged,
       "tlpAlarmSeverity": tlpAlarmSeverity,
       "tlpAlarmsWellKnown": tlpAlarmsWellKnown,
       "tlpAgentAlarms": tlpAgentAlarms,
       "tlpAutoProbeAlarms": tlpAutoProbeAlarms,
       "tlpAutoProbeAlarm01": tlpAutoProbeAlarm01,
       "tlpAutoProbeAlarm02": tlpAutoProbeAlarm02,
       "tlpAutoProbeAlarm03": tlpAutoProbeAlarm03,
       "tlpAutoProbeAlarm04": tlpAutoProbeAlarm04,
       "tlpAutoProbeAlarm05": tlpAutoProbeAlarm05,
       "tlpAutoProbeAlarm06": tlpAutoProbeAlarm06,
       "tlpAutoProbeAlarm07": tlpAutoProbeAlarm07,
       "tlpAutoProbeAlarm08": tlpAutoProbeAlarm08,
       "tlpAutoProbeAlarm09": tlpAutoProbeAlarm09,
       "tlpAutoProbeAlarm10": tlpAutoProbeAlarm10,
       "tlpAutoProbeAlarm11": tlpAutoProbeAlarm11,
       "tlpAutoProbeAlarm12": tlpAutoProbeAlarm12,
       "tlpAutoProbeAlarm13": tlpAutoProbeAlarm13,
       "tlpAutoProbeAlarm14": tlpAutoProbeAlarm14,
       "tlpAutoProbeAlarm15": tlpAutoProbeAlarm15,
       "tlpAutoProbeAlarm16": tlpAutoProbeAlarm16,
       "tlpAutoProbeAlarm17": tlpAutoProbeAlarm17,
       "tlpAutoProbeAlarm18": tlpAutoProbeAlarm18,
       "tlpAutoProbeAlarm19": tlpAutoProbeAlarm19,
       "tlpAutoProbeAlarm20": tlpAutoProbeAlarm20,
       "tlpAutoProbeAlarm21": tlpAutoProbeAlarm21,
       "tlpAutoProbeAlarm22": tlpAutoProbeAlarm22,
       "tlpAutoProbeAlarm23": tlpAutoProbeAlarm23,
       "tlpAutoProbeAlarm24": tlpAutoProbeAlarm24,
       "tlpAutoProbeAlarm25": tlpAutoProbeAlarm25,
       "tlpAutoProbeAlarm26": tlpAutoProbeAlarm26,
       "tlpAutoProbeAlarm27": tlpAutoProbeAlarm27,
       "tlpAutoProbeAlarm28": tlpAutoProbeAlarm28,
       "tlpAutoProbeAlarm29": tlpAutoProbeAlarm29,
       "tlpAutoProbeAlarm30": tlpAutoProbeAlarm30,
       "tlpAutoProbeAlarm31": tlpAutoProbeAlarm31,
       "tlpAutoProbeAlarm32": tlpAutoProbeAlarm32,
       "tlpAutoProbeAlarm33": tlpAutoProbeAlarm33,
       "tlpAutoProbeAlarm34": tlpAutoProbeAlarm34,
       "tlpAutoProbeAlarm35": tlpAutoProbeAlarm35,
       "tlpAutoProbeAlarm36": tlpAutoProbeAlarm36,
       "tlpAutoProbeAlarm37": tlpAutoProbeAlarm37,
       "tlpAutoProbeAlarm38": tlpAutoProbeAlarm38,
       "tlpAutoProbeAlarm39": tlpAutoProbeAlarm39,
       "tlpAutoProbeAlarm40": tlpAutoProbeAlarm40,
       "tlpAutoProbeAlarm41": tlpAutoProbeAlarm41,
       "tlpAutoProbeAlarm42": tlpAutoProbeAlarm42,
       "tlpAutoProbeAlarm43": tlpAutoProbeAlarm43,
       "tlpAutoProbeAlarm44": tlpAutoProbeAlarm44,
       "tlpAutoProbeAlarm45": tlpAutoProbeAlarm45,
       "tlpAutoProbeAlarm46": tlpAutoProbeAlarm46,
       "tlpAutoProbeAlarm47": tlpAutoProbeAlarm47,
       "tlpAutoProbeAlarm48": tlpAutoProbeAlarm48,
       "tlpAutoProbeAlarm49": tlpAutoProbeAlarm49,
       "tlpAutoProbeAlarm50": tlpAutoProbeAlarm50,
       "tlpAutoProbeAlarm51": tlpAutoProbeAlarm51,
       "tlpAutoProbeAlarm52": tlpAutoProbeAlarm52,
       "tlpAutoProbeAlarm53": tlpAutoProbeAlarm53,
       "tlpAutoProbeAlarm54": tlpAutoProbeAlarm54,
       "tlpAutoProbeAlarm55": tlpAutoProbeAlarm55,
       "tlpAutoProbeAlarm56": tlpAutoProbeAlarm56,
       "tlpAutoProbeAlarm57": tlpAutoProbeAlarm57,
       "tlpAutoProbeAlarm58": tlpAutoProbeAlarm58,
       "tlpAutoProbeAlarm59": tlpAutoProbeAlarm59,
       "tlpAutoProbeAlarm60": tlpAutoProbeAlarm60,
       "tlpAutoProbeAlarm61": tlpAutoProbeAlarm61,
       "tlpAutoProbeAlarm62": tlpAutoProbeAlarm62,
       "tlpAutoProbeAlarm63": tlpAutoProbeAlarm63,
       "tlpAutoProbeAlarm64": tlpAutoProbeAlarm64,
       "tlpAutoProbeUserDefinedAlarms": tlpAutoProbeUserDefinedAlarms,
       "tlpAutoProbeUserDefinedAlarm01": tlpAutoProbeUserDefinedAlarm01,
       "tlpAutoProbeUserDefinedAlarm02": tlpAutoProbeUserDefinedAlarm02,
       "tlpAutoProbeUserDefinedAlarm03": tlpAutoProbeUserDefinedAlarm03,
       "tlpAutoProbeUserDefinedAlarm04": tlpAutoProbeUserDefinedAlarm04,
       "tlpAutoProbeUserDefinedAlarm05": tlpAutoProbeUserDefinedAlarm05,
       "tlpAutoProbeUserDefinedAlarm06": tlpAutoProbeUserDefinedAlarm06,
       "tlpAutoProbeUserDefinedAlarm07": tlpAutoProbeUserDefinedAlarm07,
       "tlpAutoProbeUserDefinedAlarm08": tlpAutoProbeUserDefinedAlarm08,
       "tlpAutoProbeUserDefinedAlarm09": tlpAutoProbeUserDefinedAlarm09,
       "tlpAutoProbeUserDefinedAlarm10": tlpAutoProbeUserDefinedAlarm10,
       "tlpAutoProbeUserDefinedAlarm11": tlpAutoProbeUserDefinedAlarm11,
       "tlpAutoProbeUserDefinedAlarm12": tlpAutoProbeUserDefinedAlarm12,
       "tlpAutoProbeUserDefinedAlarm13": tlpAutoProbeUserDefinedAlarm13,
       "tlpAutoProbeUserDefinedAlarm14": tlpAutoProbeUserDefinedAlarm14,
       "tlpAutoProbeUserDefinedAlarm15": tlpAutoProbeUserDefinedAlarm15,
       "tlpAutoProbeUserDefinedAlarm16": tlpAutoProbeUserDefinedAlarm16,
       "tlpAutoProbeUserDefinedAlarm17": tlpAutoProbeUserDefinedAlarm17,
       "tlpAutoProbeUserDefinedAlarm18": tlpAutoProbeUserDefinedAlarm18,
       "tlpAutoProbeUserDefinedAlarm19": tlpAutoProbeUserDefinedAlarm19,
       "tlpAutoProbeUserDefinedAlarm20": tlpAutoProbeUserDefinedAlarm20,
       "tlpAutoProbeUserDefinedAlarm21": tlpAutoProbeUserDefinedAlarm21,
       "tlpAutoProbeUserDefinedAlarm22": tlpAutoProbeUserDefinedAlarm22,
       "tlpAutoProbeUserDefinedAlarm23": tlpAutoProbeUserDefinedAlarm23,
       "tlpAutoProbeUserDefinedAlarm24": tlpAutoProbeUserDefinedAlarm24,
       "tlpAutoProbeUserDefinedAlarm25": tlpAutoProbeUserDefinedAlarm25,
       "tlpAutoProbeUserDefinedAlarm26": tlpAutoProbeUserDefinedAlarm26,
       "tlpAutoProbeUserDefinedAlarm27": tlpAutoProbeUserDefinedAlarm27,
       "tlpAutoProbeUserDefinedAlarm28": tlpAutoProbeUserDefinedAlarm28,
       "tlpAutoProbeUserDefinedAlarm29": tlpAutoProbeUserDefinedAlarm29,
       "tlpAutoProbeUserDefinedAlarm30": tlpAutoProbeUserDefinedAlarm30,
       "tlpAutoProbeUserDefinedAlarm31": tlpAutoProbeUserDefinedAlarm31,
       "tlpAutoProbeUserDefinedAlarm32": tlpAutoProbeUserDefinedAlarm32,
       "tlpAutoProbeUserDefinedAlarm33": tlpAutoProbeUserDefinedAlarm33,
       "tlpAutoProbeUserDefinedAlarm34": tlpAutoProbeUserDefinedAlarm34,
       "tlpAutoProbeUserDefinedAlarm35": tlpAutoProbeUserDefinedAlarm35,
       "tlpAutoProbeUserDefinedAlarm36": tlpAutoProbeUserDefinedAlarm36,
       "tlpAutoProbeUserDefinedAlarm37": tlpAutoProbeUserDefinedAlarm37,
       "tlpAutoProbeUserDefinedAlarm38": tlpAutoProbeUserDefinedAlarm38,
       "tlpAutoProbeUserDefinedAlarm39": tlpAutoProbeUserDefinedAlarm39,
       "tlpAutoProbeUserDefinedAlarm40": tlpAutoProbeUserDefinedAlarm40,
       "tlpAutoProbeUserDefinedAlarm41": tlpAutoProbeUserDefinedAlarm41,
       "tlpAutoProbeUserDefinedAlarm42": tlpAutoProbeUserDefinedAlarm42,
       "tlpAutoProbeUserDefinedAlarm43": tlpAutoProbeUserDefinedAlarm43,
       "tlpAutoProbeUserDefinedAlarm44": tlpAutoProbeUserDefinedAlarm44,
       "tlpAutoProbeUserDefinedAlarm45": tlpAutoProbeUserDefinedAlarm45,
       "tlpAutoProbeUserDefinedAlarm46": tlpAutoProbeUserDefinedAlarm46,
       "tlpAutoProbeUserDefinedAlarm47": tlpAutoProbeUserDefinedAlarm47,
       "tlpAutoProbeUserDefinedAlarm48": tlpAutoProbeUserDefinedAlarm48,
       "tlpAutoProbeUserDefinedAlarm49": tlpAutoProbeUserDefinedAlarm49,
       "tlpAutoProbeUserDefinedAlarm50": tlpAutoProbeUserDefinedAlarm50,
       "tlpAutoProbeUserDefinedAlarm51": tlpAutoProbeUserDefinedAlarm51,
       "tlpAutoProbeUserDefinedAlarm52": tlpAutoProbeUserDefinedAlarm52,
       "tlpAutoProbeUserDefinedAlarm53": tlpAutoProbeUserDefinedAlarm53,
       "tlpAutoProbeUserDefinedAlarm54": tlpAutoProbeUserDefinedAlarm54,
       "tlpAutoProbeUserDefinedAlarm55": tlpAutoProbeUserDefinedAlarm55,
       "tlpAutoProbeUserDefinedAlarm56": tlpAutoProbeUserDefinedAlarm56,
       "tlpAutoProbeUserDefinedAlarm57": tlpAutoProbeUserDefinedAlarm57,
       "tlpAutoProbeUserDefinedAlarm58": tlpAutoProbeUserDefinedAlarm58,
       "tlpAutoProbeUserDefinedAlarm59": tlpAutoProbeUserDefinedAlarm59,
       "tlpAutoProbeUserDefinedAlarm60": tlpAutoProbeUserDefinedAlarm60,
       "tlpAutoProbeUserDefinedAlarm61": tlpAutoProbeUserDefinedAlarm61,
       "tlpAutoProbeUserDefinedAlarm62": tlpAutoProbeUserDefinedAlarm62,
       "tlpAutoProbeUserDefinedAlarm63": tlpAutoProbeUserDefinedAlarm63,
       "tlpAutoProbeUserDefinedAlarm64": tlpAutoProbeUserDefinedAlarm64,
       "tlpAgentDiagnosticAlarms": tlpAgentDiagnosticAlarms,
       "tlpAgentDiagnosticCPUUsageHigh": tlpAgentDiagnosticCPUUsageHigh,
       "tlpAgentDiagnosticMemoryUsageHigh": tlpAgentDiagnosticMemoryUsageHigh,
       "tlpAgentDiagnosticServiceFailed": tlpAgentDiagnosticServiceFailed,
       "tlpAgentConfigurationAlarms": tlpAgentConfigurationAlarms,
       "tlpAgentConfigurationBackedUp": tlpAgentConfigurationBackedUp,
       "tlpAgentConfigurationImported": tlpAgentConfigurationImported,
       "tlpAgentConfigurationRestored": tlpAgentConfigurationRestored,
       "tlpAgentMaintenanceAlarms": tlpAgentMaintenanceAlarms,
       "tlpAgentStarted": tlpAgentStarted,
       "tlpAgentStopped": tlpAgentStopped,
       "tlpAgentRebootInitiated": tlpAgentRebootInitiated,
       "tlpAgentFirmwareUpdated": tlpAgentFirmwareUpdated,
       "tlpAgentRestoreFactoryDefaults": tlpAgentRestoreFactoryDefaults,
       "tlpAgentUserManagementAlarms": tlpAgentUserManagementAlarms,
       "tlpAgentUserPasswordChanged": tlpAgentUserPasswordChanged,
       "tlpAgentUserAdded": tlpAgentUserAdded,
       "tlpAgentUserModified": tlpAgentUserModified,
       "tlpAgentUserDeleted": tlpAgentUserDeleted,
       "tlpAgentUserConditionOccurred": tlpAgentUserConditionOccurred,
       "tlpAgentRoleAdded": tlpAgentRoleAdded,
       "tlpAgentRoleModified": tlpAgentRoleModified,
       "tlpAgentRoleDeleted": tlpAgentRoleDeleted,
       "tlpDeviceAlarms": tlpDeviceAlarms,
       "tlpAlarmCommunicationsLost": tlpAlarmCommunicationsLost,
       "tlpAlarmUserDefined": tlpAlarmUserDefined,
       "tlpAlarmUserDefined01": tlpAlarmUserDefined01,
       "tlpAlarmUserDefined02": tlpAlarmUserDefined02,
       "tlpAlarmUserDefined03": tlpAlarmUserDefined03,
       "tlpAlarmUserDefined04": tlpAlarmUserDefined04,
       "tlpAlarmUserDefined05": tlpAlarmUserDefined05,
       "tlpAlarmUserDefined06": tlpAlarmUserDefined06,
       "tlpAlarmUserDefined07": tlpAlarmUserDefined07,
       "tlpAlarmUserDefined08": tlpAlarmUserDefined08,
       "tlpAlarmUserDefined09": tlpAlarmUserDefined09,
       "tlpAlarmUserDefined10": tlpAlarmUserDefined10,
       "tlpAlarmUserDefined11": tlpAlarmUserDefined11,
       "tlpAlarmUserDefined12": tlpAlarmUserDefined12,
       "tlpAlarmUserDefined13": tlpAlarmUserDefined13,
       "tlpAlarmUserDefined14": tlpAlarmUserDefined14,
       "tlpAlarmUserDefined15": tlpAlarmUserDefined15,
       "tlpAlarmUserDefined16": tlpAlarmUserDefined16,
       "tlpAlarmUserDefined17": tlpAlarmUserDefined17,
       "tlpAlarmUserDefined18": tlpAlarmUserDefined18,
       "tlpAlarmUserDefined19": tlpAlarmUserDefined19,
       "tlpAlarmUserDefined20": tlpAlarmUserDefined20,
       "tlpAlarmUserDefined21": tlpAlarmUserDefined21,
       "tlpAlarmUserDefined22": tlpAlarmUserDefined22,
       "tlpAlarmUserDefined23": tlpAlarmUserDefined23,
       "tlpAlarmUserDefined24": tlpAlarmUserDefined24,
       "tlpAlarmUserDefined25": tlpAlarmUserDefined25,
       "tlpAlarmUserDefined26": tlpAlarmUserDefined26,
       "tlpAlarmUserDefined27": tlpAlarmUserDefined27,
       "tlpAlarmUserDefined28": tlpAlarmUserDefined28,
       "tlpAlarmUserDefined29": tlpAlarmUserDefined29,
       "tlpAlarmUserDefined30": tlpAlarmUserDefined30,
       "tlpAlarmUserDefined31": tlpAlarmUserDefined31,
       "tlpAlarmUserDefined32": tlpAlarmUserDefined32,
       "tlpAlarmUserDefined33": tlpAlarmUserDefined33,
       "tlpAlarmUserDefined34": tlpAlarmUserDefined34,
       "tlpAlarmUserDefined35": tlpAlarmUserDefined35,
       "tlpAlarmUserDefined36": tlpAlarmUserDefined36,
       "tlpAlarmUserDefined37": tlpAlarmUserDefined37,
       "tlpAlarmUserDefined38": tlpAlarmUserDefined38,
       "tlpAlarmUserDefined39": tlpAlarmUserDefined39,
       "tlpAlarmUserDefined40": tlpAlarmUserDefined40,
       "tlpAlarmUserDefined41": tlpAlarmUserDefined41,
       "tlpAlarmUserDefined42": tlpAlarmUserDefined42,
       "tlpAlarmUserDefined43": tlpAlarmUserDefined43,
       "tlpAlarmUserDefined44": tlpAlarmUserDefined44,
       "tlpAlarmUserDefined45": tlpAlarmUserDefined45,
       "tlpAlarmUserDefined46": tlpAlarmUserDefined46,
       "tlpAlarmUserDefined47": tlpAlarmUserDefined47,
       "tlpAlarmUserDefined48": tlpAlarmUserDefined48,
       "tlpAlarmUserDefined49": tlpAlarmUserDefined49,
       "tlpAlarmUserDefined50": tlpAlarmUserDefined50,
       "tlpAlarmUserDefined51": tlpAlarmUserDefined51,
       "tlpAlarmUserDefined52": tlpAlarmUserDefined52,
       "tlpAlarmUserDefined53": tlpAlarmUserDefined53,
       "tlpAlarmUserDefined54": tlpAlarmUserDefined54,
       "tlpAlarmUserDefined55": tlpAlarmUserDefined55,
       "tlpAlarmUserDefined56": tlpAlarmUserDefined56,
       "tlpAlarmUserDefined57": tlpAlarmUserDefined57,
       "tlpAlarmUserDefined58": tlpAlarmUserDefined58,
       "tlpAlarmUserDefined59": tlpAlarmUserDefined59,
       "tlpAlarmUserDefined60": tlpAlarmUserDefined60,
       "tlpAlarmUserDefined61": tlpAlarmUserDefined61,
       "tlpAlarmUserDefined62": tlpAlarmUserDefined62,
       "tlpAlarmUserDefined63": tlpAlarmUserDefined63,
       "tlpAlarmUserDefined64": tlpAlarmUserDefined64,
       "tlpAlarmInternalFirmwareError": tlpAlarmInternalFirmwareError,
       "tlpAlarmDeviceEEPROMFault": tlpAlarmDeviceEEPROMFault,
       "tlpUpsAlarms": tlpUpsAlarms,
       "tlpUpsAlarmBatteryBad": tlpUpsAlarmBatteryBad,
       "tlpUpsAlarmOnBattery": tlpUpsAlarmOnBattery,
       "tlpUpsAlarmLowBattery": tlpUpsAlarmLowBattery,
       "tlpUpsAlarmDepletedBattery": tlpUpsAlarmDepletedBattery,
       "tlpUpsAlarmTempBad": tlpUpsAlarmTempBad,
       "tlpUpsAlarmInputBad": tlpUpsAlarmInputBad,
       "tlpUpsAlarmOutputBad": tlpUpsAlarmOutputBad,
       "tlpUpsAlarmOutputOverload": tlpUpsAlarmOutputOverload,
       "tlpUpsAlarmOnBypass": tlpUpsAlarmOnBypass,
       "tlpUpsAlarmBypassBad": tlpUpsAlarmBypassBad,
       "tlpUpsAlarmOutputOffAsRequested": tlpUpsAlarmOutputOffAsRequested,
       "tlpUpsAlarmUpsOffAsRequested": tlpUpsAlarmUpsOffAsRequested,
       "tlpUpsAlarmChargerFailed": tlpUpsAlarmChargerFailed,
       "tlpUpsAlarmOutputOff": tlpUpsAlarmOutputOff,
       "tlpUpsAlarmUpsOff": tlpUpsAlarmUpsOff,
       "tlpUpsAlarmFanFailure": tlpUpsAlarmFanFailure,
       "tlpUpsAlarmFuseFailure": tlpUpsAlarmFuseFailure,
       "tlpUpsAlarmGeneralFault": tlpUpsAlarmGeneralFault,
       "tlpUpsAlarmDiagnosticTestFailed": tlpUpsAlarmDiagnosticTestFailed,
       "tlpUpsAlarmAwaitingPower": tlpUpsAlarmAwaitingPower,
       "tlpUpsAlarmShutdownPending": tlpUpsAlarmShutdownPending,
       "tlpUpsAlarmShutdownImminent": tlpUpsAlarmShutdownImminent,
       "tlpUpsAlarmLoadLevelAboveThreshold": tlpUpsAlarmLoadLevelAboveThreshold,
       "tlpUpsAlarmLoadLevelAboveThresholdTotal": tlpUpsAlarmLoadLevelAboveThresholdTotal,
       "tlpUpsAlarmLoadLevelAboveThresholdPhase1": tlpUpsAlarmLoadLevelAboveThresholdPhase1,
       "tlpUpsAlarmLoadLevelAboveThresholdPhase2": tlpUpsAlarmLoadLevelAboveThresholdPhase2,
       "tlpUpsAlarmLoadLevelAboveThresholdPhase3": tlpUpsAlarmLoadLevelAboveThresholdPhase3,
       "tlpUpsAlarmOutputCurrentChanged": tlpUpsAlarmOutputCurrentChanged,
       "tlpUpsAlarmBatteryAgeAboveThreshold": tlpUpsAlarmBatteryAgeAboveThreshold,
       "tlpUpsAlarmLoadOff": tlpUpsAlarmLoadOff,
       "tlpUpsAlarmLoadOff01": tlpUpsAlarmLoadOff01,
       "tlpUpsAlarmLoadOff02": tlpUpsAlarmLoadOff02,
       "tlpUpsAlarmLoadOff03": tlpUpsAlarmLoadOff03,
       "tlpUpsAlarmLoadOff04": tlpUpsAlarmLoadOff04,
       "tlpUpsAlarmLoadOff05": tlpUpsAlarmLoadOff05,
       "tlpUpsAlarmLoadOff06": tlpUpsAlarmLoadOff06,
       "tlpUpsAlarmLoadOff07": tlpUpsAlarmLoadOff07,
       "tlpUpsAlarmLoadOff08": tlpUpsAlarmLoadOff08,
       "tlpUpsAlarmLoadOff09": tlpUpsAlarmLoadOff09,
       "tlpUpsAlarmLoadOff10": tlpUpsAlarmLoadOff10,
       "tlpUpsAlarmLoadOff11": tlpUpsAlarmLoadOff11,
       "tlpUpsAlarmLoadOff12": tlpUpsAlarmLoadOff12,
       "tlpUpsAlarmLoadOff13": tlpUpsAlarmLoadOff13,
       "tlpUpsAlarmLoadOff14": tlpUpsAlarmLoadOff14,
       "tlpUpsAlarmLoadOff15": tlpUpsAlarmLoadOff15,
       "tlpUpsAlarmLoadOff16": tlpUpsAlarmLoadOff16,
       "tlpUpsAlarmLoadOff17": tlpUpsAlarmLoadOff17,
       "tlpUpsAlarmLoadOff18": tlpUpsAlarmLoadOff18,
       "tlpUpsAlarmLoadOff19": tlpUpsAlarmLoadOff19,
       "tlpUpsAlarmLoadOff20": tlpUpsAlarmLoadOff20,
       "tlpUpsAlarmLoadOff21": tlpUpsAlarmLoadOff21,
       "tlpUpsAlarmLoadOff22": tlpUpsAlarmLoadOff22,
       "tlpUpsAlarmLoadOff23": tlpUpsAlarmLoadOff23,
       "tlpUpsAlarmLoadOff24": tlpUpsAlarmLoadOff24,
       "tlpUpsAlarmLoadOff25": tlpUpsAlarmLoadOff25,
       "tlpUpsAlarmLoadOff26": tlpUpsAlarmLoadOff26,
       "tlpUpsAlarmLoadOff27": tlpUpsAlarmLoadOff27,
       "tlpUpsAlarmLoadOff28": tlpUpsAlarmLoadOff28,
       "tlpUpsAlarmLoadOff29": tlpUpsAlarmLoadOff29,
       "tlpUpsAlarmLoadOff30": tlpUpsAlarmLoadOff30,
       "tlpUpsAlarmLoadOff31": tlpUpsAlarmLoadOff31,
       "tlpUpsAlarmLoadOff32": tlpUpsAlarmLoadOff32,
       "tlpUpsAlarmLoadOff33": tlpUpsAlarmLoadOff33,
       "tlpUpsAlarmLoadOff34": tlpUpsAlarmLoadOff34,
       "tlpUpsAlarmLoadOff35": tlpUpsAlarmLoadOff35,
       "tlpUpsAlarmLoadOff36": tlpUpsAlarmLoadOff36,
       "tlpUpsAlarmLoadOff37": tlpUpsAlarmLoadOff37,
       "tlpUpsAlarmLoadOff38": tlpUpsAlarmLoadOff38,
       "tlpUpsAlarmLoadOff39": tlpUpsAlarmLoadOff39,
       "tlpUpsAlarmLoadOff40": tlpUpsAlarmLoadOff40,
       "tlpUpsAlarmLoadOff41": tlpUpsAlarmLoadOff41,
       "tlpUpsAlarmLoadOff42": tlpUpsAlarmLoadOff42,
       "tlpUpsAlarmLoadOff43": tlpUpsAlarmLoadOff43,
       "tlpUpsAlarmLoadOff44": tlpUpsAlarmLoadOff44,
       "tlpUpsAlarmLoadOff45": tlpUpsAlarmLoadOff45,
       "tlpUpsAlarmLoadOff46": tlpUpsAlarmLoadOff46,
       "tlpUpsAlarmLoadOff47": tlpUpsAlarmLoadOff47,
       "tlpUpsAlarmLoadOff48": tlpUpsAlarmLoadOff48,
       "tlpUpsAlarmCurrentAboveThreshold": tlpUpsAlarmCurrentAboveThreshold,
       "tlpUpsAlarmCurrentAboveThreshold1": tlpUpsAlarmCurrentAboveThreshold1,
       "tlpUpsAlarmCurrentAboveThreshold2": tlpUpsAlarmCurrentAboveThreshold2,
       "tlpUpsAlarmCurrentAboveThreshold3": tlpUpsAlarmCurrentAboveThreshold3,
       "tlpUpsAlarmCurrentAboveThreshold4": tlpUpsAlarmCurrentAboveThreshold4,
       "tlpUpsAlarmCurrentAboveThreshold5": tlpUpsAlarmCurrentAboveThreshold5,
       "tlpUpsAlarmCurrentAboveThreshold6": tlpUpsAlarmCurrentAboveThreshold6,
       "tlpUpsAlarmRuntimeBelowWarningLevel": tlpUpsAlarmRuntimeBelowWarningLevel,
       "tlpUpsAlarmBusStartVoltageLow": tlpUpsAlarmBusStartVoltageLow,
       "tlpUpsAlarmBusOverVoltage": tlpUpsAlarmBusOverVoltage,
       "tlpUpsAlarmBusUnderVoltage": tlpUpsAlarmBusUnderVoltage,
       "tlpUpsAlarmBusVoltageUnbalanced": tlpUpsAlarmBusVoltageUnbalanced,
       "tlpUpsAlarmInverterSoftStartBad": tlpUpsAlarmInverterSoftStartBad,
       "tlpUpsAlarmInverterOverVoltage": tlpUpsAlarmInverterOverVoltage,
       "tlpUpsAlarmInverterUnderVoltage": tlpUpsAlarmInverterUnderVoltage,
       "tlpUpsAlarmInverterCircuitBad": tlpUpsAlarmInverterCircuitBad,
       "tlpUpsAlarmBatteryOverVoltage": tlpUpsAlarmBatteryOverVoltage,
       "tlpUpsAlarmBatteryUnderVoltage": tlpUpsAlarmBatteryUnderVoltage,
       "tlpUpsAlarmSiteWiringFault": tlpUpsAlarmSiteWiringFault,
       "tlpUpsAlarmOverTemperatureProtection": tlpUpsAlarmOverTemperatureProtection,
       "tlpUpsAlarmOverCharged": tlpUpsAlarmOverCharged,
       "tlpUpsAlarmEPOActive": tlpUpsAlarmEPOActive,
       "tlpUpsAlarmBypassFrequencyBad": tlpUpsAlarmBypassFrequencyBad,
       "tlpUpsAlarmExternalSmartBatteryAgeAboveThreshold": tlpUpsAlarmExternalSmartBatteryAgeAboveThreshold,
       "tlpUpsAlarmExternalNonSmartBatteryAgeAboveThreshold": tlpUpsAlarmExternalNonSmartBatteryAgeAboveThreshold,
       "tlpUpsAlarmInternalSmartBatteryCommLost": tlpUpsAlarmInternalSmartBatteryCommLost,
       "tlpUpsAlarmLoadsNotAllOn": tlpUpsAlarmLoadsNotAllOn,
       "tlpUpsAlarmBatteryTemperatureHigh": tlpUpsAlarmBatteryTemperatureHigh,
       "tlpUpsAlarmBatteryTemperatureLow": tlpUpsAlarmBatteryTemperatureLow,
       "tlpUpsAlarmBatteryDisconnected": tlpUpsAlarmBatteryDisconnected,
       "tlpUpsAlarmBatteryTemperatureSensorDisconnected": tlpUpsAlarmBatteryTemperatureSensorDisconnected,
       "tlpUpsAlarmTemperatureDerating": tlpUpsAlarmTemperatureDerating,
       "tlpUpsAlarmInputContact": tlpUpsAlarmInputContact,
       "tlpUpsAlarmInputContact1": tlpUpsAlarmInputContact1,
       "tlpUpsAlarmOutputContact": tlpUpsAlarmOutputContact,
       "tlpUpsAlarmOutputContact1": tlpUpsAlarmOutputContact1,
       "tlpUpsAlarmOutputContact2": tlpUpsAlarmOutputContact2,
       "tlpUpsAlarmOutputContact3": tlpUpsAlarmOutputContact3,
       "tlpUpsAlarmOutputContact4": tlpUpsAlarmOutputContact4,
       "tlpUpsAlarmOutputContact5": tlpUpsAlarmOutputContact5,
       "tlpUpsAlarmOutputContact6": tlpUpsAlarmOutputContact6,
       "tlpUpsAlarmCurrentBelowThreshold": tlpUpsAlarmCurrentBelowThreshold,
       "tlpUpsAlarmCurrentBelowThreshold1": tlpUpsAlarmCurrentBelowThreshold1,
       "tlpUpsAlarmCurrentBelowThreshold2": tlpUpsAlarmCurrentBelowThreshold2,
       "tlpUpsAlarmCurrentBelowThreshold3": tlpUpsAlarmCurrentBelowThreshold3,
       "tlpUpsAlarmCurrentBelowThreshold4": tlpUpsAlarmCurrentBelowThreshold4,
       "tlpUpsAlarmCurrentBelowThreshold5": tlpUpsAlarmCurrentBelowThreshold5,
       "tlpUpsAlarmCurrentBelowThreshold6": tlpUpsAlarmCurrentBelowThreshold6,
       "tlpPduAlarms": tlpPduAlarms,
       "tlpPduAlarmLoadLevelAboveThreshold": tlpPduAlarmLoadLevelAboveThreshold,
       "tlpPduAlarmInputBad": tlpPduAlarmInputBad,
       "tlpPduAlarmOutputBad": tlpPduAlarmOutputBad,
       "tlpPduAlarmOutputOverload": tlpPduAlarmOutputOverload,
       "tlpPduAlarmOutputOff": tlpPduAlarmOutputOff,
       "tlpPduAlarmLoadOff": tlpPduAlarmLoadOff,
       "tlpPduAlarmLoadOff01": tlpPduAlarmLoadOff01,
       "tlpPduAlarmLoadOff02": tlpPduAlarmLoadOff02,
       "tlpPduAlarmLoadOff03": tlpPduAlarmLoadOff03,
       "tlpPduAlarmLoadOff04": tlpPduAlarmLoadOff04,
       "tlpPduAlarmLoadOff05": tlpPduAlarmLoadOff05,
       "tlpPduAlarmLoadOff06": tlpPduAlarmLoadOff06,
       "tlpPduAlarmLoadOff07": tlpPduAlarmLoadOff07,
       "tlpPduAlarmLoadOff08": tlpPduAlarmLoadOff08,
       "tlpPduAlarmLoadOff09": tlpPduAlarmLoadOff09,
       "tlpPduAlarmLoadOff10": tlpPduAlarmLoadOff10,
       "tlpPduAlarmLoadOff11": tlpPduAlarmLoadOff11,
       "tlpPduAlarmLoadOff12": tlpPduAlarmLoadOff12,
       "tlpPduAlarmLoadOff13": tlpPduAlarmLoadOff13,
       "tlpPduAlarmLoadOff14": tlpPduAlarmLoadOff14,
       "tlpPduAlarmLoadOff15": tlpPduAlarmLoadOff15,
       "tlpPduAlarmLoadOff16": tlpPduAlarmLoadOff16,
       "tlpPduAlarmLoadOff17": tlpPduAlarmLoadOff17,
       "tlpPduAlarmLoadOff18": tlpPduAlarmLoadOff18,
       "tlpPduAlarmLoadOff19": tlpPduAlarmLoadOff19,
       "tlpPduAlarmLoadOff20": tlpPduAlarmLoadOff20,
       "tlpPduAlarmLoadOff21": tlpPduAlarmLoadOff21,
       "tlpPduAlarmLoadOff22": tlpPduAlarmLoadOff22,
       "tlpPduAlarmLoadOff23": tlpPduAlarmLoadOff23,
       "tlpPduAlarmLoadOff24": tlpPduAlarmLoadOff24,
       "tlpPduAlarmLoadOff25": tlpPduAlarmLoadOff25,
       "tlpPduAlarmLoadOff26": tlpPduAlarmLoadOff26,
       "tlpPduAlarmLoadOff27": tlpPduAlarmLoadOff27,
       "tlpPduAlarmLoadOff28": tlpPduAlarmLoadOff28,
       "tlpPduAlarmLoadOff29": tlpPduAlarmLoadOff29,
       "tlpPduAlarmLoadOff30": tlpPduAlarmLoadOff30,
       "tlpPduAlarmLoadOff31": tlpPduAlarmLoadOff31,
       "tlpPduAlarmLoadOff32": tlpPduAlarmLoadOff32,
       "tlpPduAlarmLoadOff33": tlpPduAlarmLoadOff33,
       "tlpPduAlarmLoadOff34": tlpPduAlarmLoadOff34,
       "tlpPduAlarmLoadOff35": tlpPduAlarmLoadOff35,
       "tlpPduAlarmLoadOff36": tlpPduAlarmLoadOff36,
       "tlpPduAlarmLoadOff37": tlpPduAlarmLoadOff37,
       "tlpPduAlarmLoadOff38": tlpPduAlarmLoadOff38,
       "tlpPduAlarmLoadOff39": tlpPduAlarmLoadOff39,
       "tlpPduAlarmLoadOff40": tlpPduAlarmLoadOff40,
       "tlpPduAlarmLoadOff41": tlpPduAlarmLoadOff41,
       "tlpPduAlarmLoadOff42": tlpPduAlarmLoadOff42,
       "tlpPduAlarmLoadOff43": tlpPduAlarmLoadOff43,
       "tlpPduAlarmLoadOff44": tlpPduAlarmLoadOff44,
       "tlpPduAlarmLoadOff45": tlpPduAlarmLoadOff45,
       "tlpPduAlarmLoadOff46": tlpPduAlarmLoadOff46,
       "tlpPduAlarmLoadOff47": tlpPduAlarmLoadOff47,
       "tlpPduAlarmLoadOff48": tlpPduAlarmLoadOff48,
       "tlpPduAlarmCircuitBreakerOpen": tlpPduAlarmCircuitBreakerOpen,
       "tlpPduAlarmCircuitBreakerOpen01": tlpPduAlarmCircuitBreakerOpen01,
       "tlpPduAlarmCircuitBreakerOpen02": tlpPduAlarmCircuitBreakerOpen02,
       "tlpPduAlarmCircuitBreakerOpen03": tlpPduAlarmCircuitBreakerOpen03,
       "tlpPduAlarmCircuitBreakerOpen04": tlpPduAlarmCircuitBreakerOpen04,
       "tlpPduAlarmCircuitBreakerOpen05": tlpPduAlarmCircuitBreakerOpen05,
       "tlpPduAlarmCircuitBreakerOpen06": tlpPduAlarmCircuitBreakerOpen06,
       "tlpPduAlarmCurrentAboveThreshold": tlpPduAlarmCurrentAboveThreshold,
       "tlpPduAlarmCurrentAboveThreshold1": tlpPduAlarmCurrentAboveThreshold1,
       "tlpPduAlarmCurrentAboveThreshold2": tlpPduAlarmCurrentAboveThreshold2,
       "tlpPduAlarmCurrentAboveThreshold3": tlpPduAlarmCurrentAboveThreshold3,
       "tlpPduAlarmCurrentAboveThreshold4": tlpPduAlarmCurrentAboveThreshold4,
       "tlpPduAlarmCurrentAboveThreshold5": tlpPduAlarmCurrentAboveThreshold5,
       "tlpPduAlarmCurrentAboveThreshold6": tlpPduAlarmCurrentAboveThreshold6,
       "tlpPduAlarmLoadsNotAllOn": tlpPduAlarmLoadsNotAllOn,
       "tlpPduAlarmLoadLevelBelowThreshold": tlpPduAlarmLoadLevelBelowThreshold,
       "tlpPduAlarmCurrentBelowThreshold": tlpPduAlarmCurrentBelowThreshold,
       "tlpPduAlarmCurrentBelowThreshold1": tlpPduAlarmCurrentBelowThreshold1,
       "tlpPduAlarmCurrentBelowThreshold2": tlpPduAlarmCurrentBelowThreshold2,
       "tlpPduAlarmCurrentBelowThreshold3": tlpPduAlarmCurrentBelowThreshold3,
       "tlpPduAlarmCurrentBelowThreshold4": tlpPduAlarmCurrentBelowThreshold4,
       "tlpPduAlarmCurrentBelowThreshold5": tlpPduAlarmCurrentBelowThreshold5,
       "tlpPduAlarmCurrentBelowThreshold6": tlpPduAlarmCurrentBelowThreshold6,
       "tlpPduAlarmThdOutOfRange": tlpPduAlarmThdOutOfRange,
       "tlpPduAlarmGeneralFault": tlpPduAlarmGeneralFault,
       "tlpPduAlarmOutletOverCurrent": tlpPduAlarmOutletOverCurrent,
       "tlpEnvAlarms": tlpEnvAlarms,
       "tlpEnvAlarmTemperatureBeyondLimits": tlpEnvAlarmTemperatureBeyondLimits,
       "tlpEnvAlarmHumidityBeyondLimits": tlpEnvAlarmHumidityBeyondLimits,
       "tlpEnvAlarmInputContact": tlpEnvAlarmInputContact,
       "tlpEnvAlarmInputContact01": tlpEnvAlarmInputContact01,
       "tlpEnvAlarmInputContact02": tlpEnvAlarmInputContact02,
       "tlpEnvAlarmInputContact03": tlpEnvAlarmInputContact03,
       "tlpEnvAlarmInputContact04": tlpEnvAlarmInputContact04,
       "tlpEnvAlarmOutputContact": tlpEnvAlarmOutputContact,
       "tlpEnvAlarmOutputContact01": tlpEnvAlarmOutputContact01,
       "tlpEnvAlarmOutputContact02": tlpEnvAlarmOutputContact02,
       "tlpEnvAlarmOutputContact03": tlpEnvAlarmOutputContact03,
       "tlpEnvAlarmOutputContact04": tlpEnvAlarmOutputContact04,
       "tlpAtsAlarms": tlpAtsAlarms,
       "tlpAtsAlarmOutage": tlpAtsAlarmOutage,
       "tlpAtsAlarmSource1Outage": tlpAtsAlarmSource1Outage,
       "tlpAtsAlarmSource2Outage": tlpAtsAlarmSource2Outage,
       "tlpAtsAlarmTemperature": tlpAtsAlarmTemperature,
       "tlpAtsAlarmDeviceTemperature": tlpAtsAlarmDeviceTemperature,
       "tlpAtsAlarmSource1Temperature": tlpAtsAlarmSource1Temperature,
       "tlpAtsAlarmSource2Temperature": tlpAtsAlarmSource2Temperature,
       "tlpAtsAlarmLoadLevelAboveThreshold": tlpAtsAlarmLoadLevelAboveThreshold,
       "tlpAtsAlarmInputBad": tlpAtsAlarmInputBad,
       "tlpAtsAlarmOutputBad": tlpAtsAlarmOutputBad,
       "tlpAtsAlarmOutputOverload": tlpAtsAlarmOutputOverload,
       "tlpAtsAlarmOutputOff": tlpAtsAlarmOutputOff,
       "tlpAtsAlarmLoadOff": tlpAtsAlarmLoadOff,
       "tlpAtsAlarmLoadOff01": tlpAtsAlarmLoadOff01,
       "tlpAtsAlarmLoadOff02": tlpAtsAlarmLoadOff02,
       "tlpAtsAlarmLoadOff03": tlpAtsAlarmLoadOff03,
       "tlpAtsAlarmLoadOff04": tlpAtsAlarmLoadOff04,
       "tlpAtsAlarmLoadOff05": tlpAtsAlarmLoadOff05,
       "tlpAtsAlarmLoadOff06": tlpAtsAlarmLoadOff06,
       "tlpAtsAlarmLoadOff07": tlpAtsAlarmLoadOff07,
       "tlpAtsAlarmLoadOff08": tlpAtsAlarmLoadOff08,
       "tlpAtsAlarmLoadOff09": tlpAtsAlarmLoadOff09,
       "tlpAtsAlarmLoadOff10": tlpAtsAlarmLoadOff10,
       "tlpAtsAlarmLoadOff11": tlpAtsAlarmLoadOff11,
       "tlpAtsAlarmLoadOff12": tlpAtsAlarmLoadOff12,
       "tlpAtsAlarmLoadOff13": tlpAtsAlarmLoadOff13,
       "tlpAtsAlarmLoadOff14": tlpAtsAlarmLoadOff14,
       "tlpAtsAlarmLoadOff15": tlpAtsAlarmLoadOff15,
       "tlpAtsAlarmLoadOff16": tlpAtsAlarmLoadOff16,
       "tlpAtsAlarmLoadOff17": tlpAtsAlarmLoadOff17,
       "tlpAtsAlarmLoadOff18": tlpAtsAlarmLoadOff18,
       "tlpAtsAlarmLoadOff19": tlpAtsAlarmLoadOff19,
       "tlpAtsAlarmLoadOff20": tlpAtsAlarmLoadOff20,
       "tlpAtsAlarmLoadOff21": tlpAtsAlarmLoadOff21,
       "tlpAtsAlarmLoadOff22": tlpAtsAlarmLoadOff22,
       "tlpAtsAlarmLoadOff23": tlpAtsAlarmLoadOff23,
       "tlpAtsAlarmLoadOff24": tlpAtsAlarmLoadOff24,
       "tlpAtsAlarmLoadOff25": tlpAtsAlarmLoadOff25,
       "tlpAtsAlarmLoadOff26": tlpAtsAlarmLoadOff26,
       "tlpAtsAlarmLoadOff27": tlpAtsAlarmLoadOff27,
       "tlpAtsAlarmLoadOff28": tlpAtsAlarmLoadOff28,
       "tlpAtsAlarmLoadOff29": tlpAtsAlarmLoadOff29,
       "tlpAtsAlarmLoadOff30": tlpAtsAlarmLoadOff30,
       "tlpAtsAlarmLoadOff31": tlpAtsAlarmLoadOff31,
       "tlpAtsAlarmLoadOff32": tlpAtsAlarmLoadOff32,
       "tlpAtsAlarmLoadOff33": tlpAtsAlarmLoadOff33,
       "tlpAtsAlarmLoadOff34": tlpAtsAlarmLoadOff34,
       "tlpAtsAlarmLoadOff35": tlpAtsAlarmLoadOff35,
       "tlpAtsAlarmLoadOff36": tlpAtsAlarmLoadOff36,
       "tlpAtsAlarmLoadOff37": tlpAtsAlarmLoadOff37,
       "tlpAtsAlarmLoadOff38": tlpAtsAlarmLoadOff38,
       "tlpAtsAlarmLoadOff39": tlpAtsAlarmLoadOff39,
       "tlpAtsAlarmLoadOff40": tlpAtsAlarmLoadOff40,
       "tlpAtsAlarmLoadOff41": tlpAtsAlarmLoadOff41,
       "tlpAtsAlarmLoadOff42": tlpAtsAlarmLoadOff42,
       "tlpAtsAlarmLoadOff43": tlpAtsAlarmLoadOff43,
       "tlpAtsAlarmLoadOff44": tlpAtsAlarmLoadOff44,
       "tlpAtsAlarmLoadOff45": tlpAtsAlarmLoadOff45,
       "tlpAtsAlarmLoadOff46": tlpAtsAlarmLoadOff46,
       "tlpAtsAlarmLoadOff47": tlpAtsAlarmLoadOff47,
       "tlpAtsAlarmLoadOff48": tlpAtsAlarmLoadOff48,
       "tlpAtsAlarmCircuitBreakerOpen": tlpAtsAlarmCircuitBreakerOpen,
       "tlpAtsAlarmCircuitBreakerOpen01": tlpAtsAlarmCircuitBreakerOpen01,
       "tlpAtsAlarmCircuitBreakerOpen02": tlpAtsAlarmCircuitBreakerOpen02,
       "tlpAtsAlarmCircuitBreakerOpen03": tlpAtsAlarmCircuitBreakerOpen03,
       "tlpAtsAlarmCircuitBreakerOpen04": tlpAtsAlarmCircuitBreakerOpen04,
       "tlpAtsAlarmCircuitBreakerOpen05": tlpAtsAlarmCircuitBreakerOpen05,
       "tlpAtsAlarmCircuitBreakerOpen06": tlpAtsAlarmCircuitBreakerOpen06,
       "tlpAtsAlarmCurrentAboveThreshold": tlpAtsAlarmCurrentAboveThreshold,
       "tlpAtsAlarmCurrentAboveThreshold1": tlpAtsAlarmCurrentAboveThreshold1,
       "tlpAtsAlarmCurrentAboveThreshold2": tlpAtsAlarmCurrentAboveThreshold2,
       "tlpAtsAlarmCurrentAboveThreshold3": tlpAtsAlarmCurrentAboveThreshold3,
       "tlpAtsAlarmCurrentAboveThreshold4": tlpAtsAlarmCurrentAboveThreshold4,
       "tlpAtsAlarmCurrentAboveThreshold5": tlpAtsAlarmCurrentAboveThreshold5,
       "tlpAtsAlarmCurrentAboveThreshold6": tlpAtsAlarmCurrentAboveThreshold6,
       "tlpAtsAlarmLoadsNotAllOn": tlpAtsAlarmLoadsNotAllOn,
       "tlpAtsAlarmGeneralFault": tlpAtsAlarmGeneralFault,
       "tlpAtsAlarmVoltage": tlpAtsAlarmVoltage,
       "tlpAtsAlarmOverVoltage": tlpAtsAlarmOverVoltage,
       "tlpAtsAlarmSource1OverVoltage": tlpAtsAlarmSource1OverVoltage,
       "tlpAtsAlarmSource2OverVoltage": tlpAtsAlarmSource2OverVoltage,
       "tlpAtsAlarmFrequency": tlpAtsAlarmFrequency,
       "tlpAtsAlarmSource1InvalidFrequency": tlpAtsAlarmSource1InvalidFrequency,
       "tlpAtsAlarmSource2InvalidFrequency": tlpAtsAlarmSource2InvalidFrequency,
       "tlpAtsAlarmLoadLevelBelowThreshold": tlpAtsAlarmLoadLevelBelowThreshold,
       "tlpAtsAlarmCurrentBelowThreshold": tlpAtsAlarmCurrentBelowThreshold,
       "tlpAtsAlarmCurrentBelowThreshold1": tlpAtsAlarmCurrentBelowThreshold1,
       "tlpAtsAlarmCurrentBelowThreshold2": tlpAtsAlarmCurrentBelowThreshold2,
       "tlpAtsAlarmCurrentBelowThreshold3": tlpAtsAlarmCurrentBelowThreshold3,
       "tlpAtsAlarmCurrentBelowThreshold4": tlpAtsAlarmCurrentBelowThreshold4,
       "tlpAtsAlarmCurrentBelowThreshold5": tlpAtsAlarmCurrentBelowThreshold5,
       "tlpAtsAlarmCurrentBelowThreshold6": tlpAtsAlarmCurrentBelowThreshold6,
       "tlpAtsAlarmThdOutOfRange": tlpAtsAlarmThdOutOfRange,
       "tlpAtsAlarmOutletOverCurrent": tlpAtsAlarmOutletOverCurrent,
       "tlpCoolingAlarms": tlpCoolingAlarms,
       "tlpCoolingAlarmSupplyAirSensorFault": tlpCoolingAlarmSupplyAirSensorFault,
       "tlpCoolingAlarmReturnAirSensorFault": tlpCoolingAlarmReturnAirSensorFault,
       "tlpCoolingAlarmCondenserInletAirSensorFault": tlpCoolingAlarmCondenserInletAirSensorFault,
       "tlpCoolingAlarmCondenserOutletAirSensorFault": tlpCoolingAlarmCondenserOutletAirSensorFault,
       "tlpCoolingAlarmSuctionTemperatureSensorFault": tlpCoolingAlarmSuctionTemperatureSensorFault,
       "tlpCoolingAlarmEvaporatorTemperatureSensorFault": tlpCoolingAlarmEvaporatorTemperatureSensorFault,
       "tlpCoolingAlarmAirFilterClogged": tlpCoolingAlarmAirFilterClogged,
       "tlpCoolingAlarmAirFilterRunHoursViolation": tlpCoolingAlarmAirFilterRunHoursViolation,
       "tlpCoolingAlarmSuctionPressureSensorFault": tlpCoolingAlarmSuctionPressureSensorFault,
       "tlpCoolingAlarmInverterCommunicationsFault": tlpCoolingAlarmInverterCommunicationsFault,
       "tlpCoolingAlarmRemoteShutdownViaInputContact": tlpCoolingAlarmRemoteShutdownViaInputContact,
       "tlpCoolingAlarmCondensatePumpFault": tlpCoolingAlarmCondensatePumpFault,
       "tlpCoolingAlarmLowRefrigerantStartupFault": tlpCoolingAlarmLowRefrigerantStartupFault,
       "tlpCoolingAlarmCondenserFanFault": tlpCoolingAlarmCondenserFanFault,
       "tlpCoolingAlarmCondenserFailure": tlpCoolingAlarmCondenserFailure,
       "tlpCoolingAlarmEvaporatorCoolingFailure": tlpCoolingAlarmEvaporatorCoolingFailure,
       "tlpCoolingAlarmReturnAirTempHigh": tlpCoolingAlarmReturnAirTempHigh,
       "tlpCoolingAlarmSupplyAirTempHigh": tlpCoolingAlarmSupplyAirTempHigh,
       "tlpCoolingAlarmEvaporatorFailure": tlpCoolingAlarmEvaporatorFailure,
       "tlpCoolingAlarmEvaporatorFreezeUp": tlpCoolingAlarmEvaporatorFreezeUp,
       "tlpCoolingAlarmDischargePressureHigh": tlpCoolingAlarmDischargePressureHigh,
       "tlpCoolingAlarmPressureGaugeFailure": tlpCoolingAlarmPressureGaugeFailure,
       "tlpCoolingAlarmDischargePressurePersistentHigh": tlpCoolingAlarmDischargePressurePersistentHigh,
       "tlpCoolingAlarmSuctionPressureLowStartFailure": tlpCoolingAlarmSuctionPressureLowStartFailure,
       "tlpCoolingAlarmSuctionPressureLow": tlpCoolingAlarmSuctionPressureLow,
       "tlpCoolingAlarmSuctionPressurePersistentLow": tlpCoolingAlarmSuctionPressurePersistentLow,
       "tlpCoolingAlarmStartupLinePressureImbalance": tlpCoolingAlarmStartupLinePressureImbalance,
       "tlpCoolingAlarmCompressorFailure": tlpCoolingAlarmCompressorFailure,
       "tlpCoolingAlarmCurrentLimit": tlpCoolingAlarmCurrentLimit,
       "tlpCoolingAlarmWaterLeak": tlpCoolingAlarmWaterLeak,
       "tlpCoolingAlarmFanUnderCurrent": tlpCoolingAlarmFanUnderCurrent,
       "tlpCoolingAlarmFanOverCurrent": tlpCoolingAlarmFanOverCurrent,
       "tlpCoolingAlarmDischargePressureSensorFault": tlpCoolingAlarmDischargePressureSensorFault,
       "tlpCoolingAlarmWaterFull": tlpCoolingAlarmWaterFull,
       "tlpCoolingAlarmAutoCoolingOn": tlpCoolingAlarmAutoCoolingOn,
       "tlpCoolingAlarmPowerButtonPressed": tlpCoolingAlarmPowerButtonPressed,
       "tlpCoolingAlarmDisconnectedFromDevice": tlpCoolingAlarmDisconnectedFromDevice,
       "tlpCoolingAlarmReturnAirTemperatureSensorFault": tlpCoolingAlarmReturnAirTemperatureSensorFault,
       "tlpCoolingAlarmRemoteTemperatureSensorFault": tlpCoolingAlarmRemoteTemperatureSensorFault,
       "tlpCoolingAlarmLowPressureSensorFault": tlpCoolingAlarmLowPressureSensorFault,
       "tlpCoolingAlarmHighPressureSensorFault": tlpCoolingAlarmHighPressureSensorFault,
       "tlpCoolingAlarmSentrytimerTimeout": tlpCoolingAlarmSentrytimerTimeout,
       "tlpKvmAlarms": tlpKvmAlarms,
       "tlpRackTrackAlarms": tlpRackTrackAlarms,
       "tlpSwitchAlarms": tlpSwitchAlarms,
       "tlpAlarmControl": tlpAlarmControl,
       "tlpAlarmControlTable": tlpAlarmControlTable,
       "tlpAlarmControlEntry": tlpAlarmControlEntry,
       "tlpAlarmControlIndex": tlpAlarmControlIndex,
       "tlpAlarmControlDescr": tlpAlarmControlDescr,
       "tlpAlarmControlDetail": tlpAlarmControlDetail,
       "tlpAlarmControlSeverity": tlpAlarmControlSeverity,
       "tlpNotify": tlpNotify,
       "tlpNotifications": tlpNotifications,
       "tlpNotificationsAlarmEntryAdded": tlpNotificationsAlarmEntryAdded,
       "tlpNotificationsAlarmEntryRemoved": tlpNotificationsAlarmEntryRemoved,
       "tlpNotifySystemStartup": tlpNotifySystemStartup,
       "tlpNotifySystemShutdown": tlpNotifySystemShutdown,
       "tlpNotifySystemUpdate": tlpNotifySystemUpdate,
       "tlpNotifyTest": tlpNotifyTest,
       "tlpNotificationsEvent": tlpNotificationsEvent,
       "tlpNotificationsAgent": tlpNotificationsAgent,
       "tlpNotificationsDevice": tlpNotificationsDevice,
       "tlpNotificationsDeviceInternalFirmwareFault": tlpNotificationsDeviceInternalFirmwareFault,
       "tlpNotificationsDeviceInternalHardwareFault": tlpNotificationsDeviceInternalHardwareFault,
       "tlpNotificationsDeviceConfigurationChange": tlpNotificationsDeviceConfigurationChange,
       "tlpNotificationsDeviceFirmwareUpdate": tlpNotificationsDeviceFirmwareUpdate,
       "tlpNotificationsDeviceMicrocontrollerReset": tlpNotificationsDeviceMicrocontrollerReset,
       "tlpNotificationsDeviceSystemInformation": tlpNotificationsDeviceSystemInformation,
       "tlpNotificationsDeviceNvrChecksumMismatch": tlpNotificationsDeviceNvrChecksumMismatch,
       "tlpNotificationsDeviceUsbCommunicationsEstablished": tlpNotificationsDeviceUsbCommunicationsEstablished,
       "tlpNotificationsDeviceUsbCommunicationsLost": tlpNotificationsDeviceUsbCommunicationsLost,
       "tlpNotificationsDevicePowerSupplyShutdown": tlpNotificationsDevicePowerSupplyShutdown,
       "tlpNotificationsDeviceOverLoadShutdown": tlpNotificationsDeviceOverLoadShutdown,
       "tlpNotificationsDeviceCurrentLimitShutdown": tlpNotificationsDeviceCurrentLimitShutdown,
       "tlpNotificationsDeviceOverTemperatureShutdown": tlpNotificationsDeviceOverTemperatureShutdown,
       "tlpNotificationsDeviceModeTransitionTimeout": tlpNotificationsDeviceModeTransitionTimeout,
       "tlpNotificationsDeviceFailedModeTransitionToIdle": tlpNotificationsDeviceFailedModeTransitionToIdle,
       "tlpNotificationsDeviceInternalCommunicationsLost": tlpNotificationsDeviceInternalCommunicationsLost,
       "tlpNotificationsDeviceAcknowledgeFaults": tlpNotificationsDeviceAcknowledgeFaults,
       "tlpNotificationsDeviceTransferToRestart": tlpNotificationsDeviceTransferToRestart,
       "tlpNotificationsDeviceTransferToWatchdogRestart": tlpNotificationsDeviceTransferToWatchdogRestart,
       "tlpNotificationsDeviceTransferToLatchedIdle": tlpNotificationsDeviceTransferToLatchedIdle,
       "tlpNotificationsDeviceTransferToLatchedStandby": tlpNotificationsDeviceTransferToLatchedStandby,
       "tlpNotificationsDeviceTransferToLatchedLine": tlpNotificationsDeviceTransferToLatchedLine,
       "tlpNotificationsDeviceFailSafeClockMonitorEngaged": tlpNotificationsDeviceFailSafeClockMonitorEngaged,
       "tlpNotificationsDeviceTransferToIdle": tlpNotificationsDeviceTransferToIdle,
       "tlpNotificationsDeviceVoutUnderVoltageShutdown": tlpNotificationsDeviceVoutUnderVoltageShutdown,
       "tlpNotificationsDeviceVoutOverVoltageShutdown": tlpNotificationsDeviceVoutOverVoltageShutdown,
       "tlpNotificationsDeviceRtosFault": tlpNotificationsDeviceRtosFault,
       "tlpNotificationsDeviceCriticalNvrValuesBlank": tlpNotificationsDeviceCriticalNvrValuesBlank,
       "tlpNotificationsDeviceOutputOff": tlpNotificationsDeviceOutputOff,
       "tlpNotificationsDeviceStartup": tlpNotificationsDeviceStartup,
       "tlpNotificationsDeviceEpo": tlpNotificationsDeviceEpo,
       "tlpNotificationsDeviceFirmwareMismatch": tlpNotificationsDeviceFirmwareMismatch,
       "tlpNotificationsDeviceOverloadRelease": tlpNotificationsDeviceOverloadRelease,
       "tlpNotificationsDeviceTransferToLine": tlpNotificationsDeviceTransferToLine,
       "tlpNotificationsDeviceAcFailure": tlpNotificationsDeviceAcFailure,
       "tlpNotificationsDeviceSiteWiringFault": tlpNotificationsDeviceSiteWiringFault,
       "tlpNotificationsDeviceEmergencyShutdown": tlpNotificationsDeviceEmergencyShutdown,
       "tlpNotificationsDeviceCircuitBreakerOpen": tlpNotificationsDeviceCircuitBreakerOpen,
       "tlpNotificationsDeviceSupplyMonitorInterrupt": tlpNotificationsDeviceSupplyMonitorInterrupt,
       "tlpNotificationsDeviceSystemTickTimeout": tlpNotificationsDeviceSystemTickTimeout,
       "tlpNotificationsDeviceRelayInUnexpectedState": tlpNotificationsDeviceRelayInUnexpectedState,
       "tlpNotificationsDeviceEepromQueueOverflow": tlpNotificationsDeviceEepromQueueOverflow,
       "tlpNotificationsDeviceEepromWriteFault": tlpNotificationsDeviceEepromWriteFault,
       "tlpNotificationsDeviceEepromOperationTimeout": tlpNotificationsDeviceEepromOperationTimeout,
       "tlpNotificationsDeviceI2cWriteDelayed": tlpNotificationsDeviceI2cWriteDelayed,
       "tlpNotificationsDeviceRampShedNvrWriteFailed": tlpNotificationsDeviceRampShedNvrWriteFailed,
       "tlpNotificationsDeviceFactoryRestoreFault": tlpNotificationsDeviceFactoryRestoreFault,
       "tlpNotificationsDeviceRelaySetTimeOutOfRange": tlpNotificationsDeviceRelaySetTimeOutOfRange,
       "tlpNotificationsDeviceRelayResetTimeOutOfRange": tlpNotificationsDeviceRelayResetTimeOutOfRange,
       "tlpNotificationsUps": tlpNotificationsUps,
       "tlpNotificationsUpsBatteryLowVoltageShutdown": tlpNotificationsUpsBatteryLowVoltageShutdown,
       "tlpNotificationsUpsBatteryLowPercentageShutdown": tlpNotificationsUpsBatteryLowPercentageShutdown,
       "tlpNotificationsUpsBatteryOverVoltageShutdown": tlpNotificationsUpsBatteryOverVoltageShutdown,
       "tlpNotificationsUpsBatteryOverCurrentShutdown": tlpNotificationsUpsBatteryOverCurrentShutdown,
       "tlpNotificationsUpsBatteryUnknownTypeShutdown": tlpNotificationsUpsBatteryUnknownTypeShutdown,
       "tlpNotificationsUpsBatteryConfigurationMismatch": tlpNotificationsUpsBatteryConfigurationMismatch,
       "tlpNotificationsUpsBatteryUnderVoltageShutdown": tlpNotificationsUpsBatteryUnderVoltageShutdown,
       "tlpNotificationsUpsSlaBatteryOverTemperatureShutdown": tlpNotificationsUpsSlaBatteryOverTemperatureShutdown,
       "tlpNotificationsUpsBatteryInstallation": tlpNotificationsUpsBatteryInstallation,
       "tlpNotificationsUpsChargerBulkToAcceptance": tlpNotificationsUpsChargerBulkToAcceptance,
       "tlpNotificationsUpsChargerAcceptanceToFloat": tlpNotificationsUpsChargerAcceptanceToFloat,
       "tlpNotificationsUpsChargerFloatToBulk": tlpNotificationsUpsChargerFloatToBulk,
       "tlpNotificationsUpsTransferToSelftest": tlpNotificationsUpsTransferToSelftest,
       "tlpNotificationsUpsTransferToEconomy": tlpNotificationsUpsTransferToEconomy,
       "tlpNotificationsUpsLineConnectRelayFaultShutdown": tlpNotificationsUpsLineConnectRelayFaultShutdown,
       "tlpNotificationsUpsTransferToFaultBypass": tlpNotificationsUpsTransferToFaultBypass,
       "tlpNotificationsUpsBypassPowerDistributionModuleDisconnected": tlpNotificationsUpsBypassPowerDistributionModuleDisconnected,
       "tlpNotificationsUpsManualBypassActivatedFromUnsupportedMode": tlpNotificationsUpsManualBypassActivatedFromUnsupportedMode,
       "tlpNotificationsUpsOnBatteryTimeoutShutdown": tlpNotificationsUpsOnBatteryTimeoutShutdown,
       "tlpNotificationsUpsLowBatteryPercentageShutdown": tlpNotificationsUpsLowBatteryPercentageShutdown,
       "tlpNotificationsUpsBatteryCommunicationsLost": tlpNotificationsUpsBatteryCommunicationsLost,
       "tlpNotificationsUpsBatteryCommunicationsEstablished": tlpNotificationsUpsBatteryCommunicationsEstablished,
       "tlpNotificationsUpsBatteryOtaShutdown": tlpNotificationsUpsBatteryOtaShutdown,
       "tlpNotificationsUpsCartInstallation": tlpNotificationsUpsCartInstallation,
       "tlpNotificationsUpsDeadBatteryRecoveryShutdown": tlpNotificationsUpsDeadBatteryRecoveryShutdown,
       "tlpNotificationsUpsFullBridgeNotSteadyShutdown": tlpNotificationsUpsFullBridgeNotSteadyShutdown,
       "tlpNotificationsUpsFullBridgeCurrentLimitShutdown": tlpNotificationsUpsFullBridgeCurrentLimitShutdown,
       "tlpNotificationsUpsTransitionFailed": tlpNotificationsUpsTransitionFailed,
       "tlpNotificationsUpsInverterOcp": tlpNotificationsUpsInverterOcp,
       "tlpNotificationsUpsInverterVbusShutdown": tlpNotificationsUpsInverterVbusShutdown,
       "tlpNotificationsUpsTransferToFaultStandby": tlpNotificationsUpsTransferToFaultStandby,
       "tlpNotificationsUpsModbusBatteryStatusShutdown": tlpNotificationsUpsModbusBatteryStatusShutdown,
       "tlpNotificationsUpsBatteryPackCountChange": tlpNotificationsUpsBatteryPackCountChange,
       "tlpNotificationsUpsTransferToBattery": tlpNotificationsUpsTransferToBattery,
       "tlpNotificationsUpsTransferToBypass": tlpNotificationsUpsTransferToBypass,
       "tlpNotificationsUpsTransferToDbrLine": tlpNotificationsUpsTransferToDbrLine,
       "tlpNotificationsUpsTransferToDbrStandby": tlpNotificationsUpsTransferToDbrStandby,
       "tlpNotificationsUpsTransferToStandby": tlpNotificationsUpsTransferToStandby,
       "tlpNotificationsUpsTransferToOnline": tlpNotificationsUpsTransferToOnline,
       "tlpNotificationsUpsV20BusNotSteadyShutdown": tlpNotificationsUpsV20BusNotSteadyShutdown,
       "tlpNotificationsUpsV20BusOverVoltageShutdown": tlpNotificationsUpsV20BusOverVoltageShutdown,
       "tlpNotificationsUpsV20BusUnderVoltageShutdown": tlpNotificationsUpsV20BusUnderVoltageShutdown,
       "tlpNotificationsUpsBypassOutOfRange": tlpNotificationsUpsBypassOutOfRange,
       "tlpNotificationsUpsEnergySavingShutdown": tlpNotificationsUpsEnergySavingShutdown,
       "tlpNotificationsUpsDryContactShutdown": tlpNotificationsUpsDryContactShutdown,
       "tlpNotificationsUpsInverterOverCurrentShutdown": tlpNotificationsUpsInverterOverCurrentShutdown,
       "tlpNotificationsUpsPfcPrechargeFault": tlpNotificationsUpsPfcPrechargeFault,
       "tlpNotificationsUpsPfcOverVoltageFault": tlpNotificationsUpsPfcOverVoltageFault,
       "tlpNotificationsUpsPfcUnderVoltageFault": tlpNotificationsUpsPfcUnderVoltageFault,
       "tlpNotificationsUpsPfcOverCurrentFault": tlpNotificationsUpsPfcOverCurrentFault,
       "tlpNotificationsPdu": tlpNotificationsPdu,
       "tlpNotificationsPduCrestFactorOutOfRange": tlpNotificationsPduCrestFactorOutOfRange,
       "tlpNotificationsPduTransferToForceLineMode": tlpNotificationsPduTransferToForceLineMode,
       "tlpNotificationsPduLineInRange": tlpNotificationsPduLineInRange,
       "tlpNotificationsPduLineOutOfRange": tlpNotificationsPduLineOutOfRange,
       "tlpNotificationsPduNotableRelayResponseTimes": tlpNotificationsPduNotableRelayResponseTimes,
       "tlpNotificationsPduOutletNearMaxRating": tlpNotificationsPduOutletNearMaxRating,
       "tlpNotificationsPduLineModeTransferToLinePartialPowerup": tlpNotificationsPduLineModeTransferToLinePartialPowerup,
       "tlpNotificationsPduSinglePhasing": tlpNotificationsPduSinglePhasing,
       "tlpNotificationsEnvirosense": tlpNotificationsEnvirosense,
       "tlpNotificationsAts": tlpNotificationsAts,
       "tlpNotificationsAtsSource1NotAvailable": tlpNotificationsAtsSource1NotAvailable,
       "tlpNotificationsAtsSource2NotAvailable": tlpNotificationsAtsSource2NotAvailable,
       "tlpNotificationsAtsLockdownToSource1": tlpNotificationsAtsLockdownToSource1,
       "tlpNotificationsAtsLockdownToSource2": tlpNotificationsAtsLockdownToSource2,
       "tlpNotificationsAtsSource1Available": tlpNotificationsAtsSource1Available,
       "tlpNotificationsAtsSource2Available": tlpNotificationsAtsSource2Available,
       "tlpNotificationsAtsSource1Brownout": tlpNotificationsAtsSource1Brownout,
       "tlpNotificationsAtsSource2Brownout": tlpNotificationsAtsSource2Brownout,
       "tlpNotificationsAtsSource1VoltageDrop": tlpNotificationsAtsSource1VoltageDrop,
       "tlpNotificationsAtsSource2VoltageDrop": tlpNotificationsAtsSource2VoltageDrop,
       "tlpNotificationsAtsTimedReturnToSource1": tlpNotificationsAtsTimedReturnToSource1,
       "tlpNotificationsAtsTimedReturnToSource2": tlpNotificationsAtsTimedReturnToSource2,
       "tlpNotificationsAtsTransferToSource1": tlpNotificationsAtsTransferToSource1,
       "tlpNotificationsAtsTransferToSource2": tlpNotificationsAtsTransferToSource2,
       "tlpNotificationsCooling": tlpNotificationsCooling,
       "tlpNotificationsKvm": tlpNotificationsKvm,
       "tlpNotificationsRackTrack": tlpNotificationsRackTrack,
       "tlpNotificationsSwitch": tlpNotificationsSwitch,
       "tlpNotificationsEventParameters": tlpNotificationsEventParameters,
       "tlpNotifyEventTableRef": tlpNotifyEventTableRef,
       "tlpNotifyEventTableRowRef": tlpNotifyEventTableRowRef}
)
