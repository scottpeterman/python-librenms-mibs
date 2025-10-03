# SNMP MIB module (RAY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ray\RAY-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:23:14 2025
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

(snmpTraps,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "snmpTraps")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

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

ray = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 33555, 1)
)
if mibBuilder.loadTexts:
    ray.setRevisions(
        ("2016-10-04 00:00",)
    )


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""




class PhysAddress(OctetString):
    """Custom type PhysAddress based on OctetString"""



# TEXTUAL-CONVENTIONS



class ServiceState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("up", 1),
          ("down", 2))
    )



class AlarmState(TextualConvention, Integer32):
    status = "current"
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
        *(("na", 0),
          ("up", 1),
          ("down", 2),
          ("ack", 3))
    )



class OptionSetting(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("on", 1),
          ("off", 2))
    )



class ModulationList(TextualConvention, Integer32):
    status = "current"
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
        *(("na", 0),
          ("qpsk", 1),
          ("qam16", 2),
          ("qam32", 3),
          ("qam64", 4),
          ("qam128", 5),
          ("qam256", 6))
    )



# MIB Managed Objects in the order of their OIDs

_Racom_ObjectIdentity = ObjectIdentity
racom = _Racom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33555)
)
_Station_ObjectIdentity = ObjectIdentity
station = _Station_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33555, 1, 1)
)
_Product_ObjectIdentity = ObjectIdentity
product = _Product_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33555, 1, 1, 1)
)


class _ProductName_Type(DisplayString):
    """Custom type productName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ProductName_Type.__name__ = "DisplayString"
_ProductName_Object = MibScalar
productName = _ProductName_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 1, 1, 1),
    _ProductName_Type()
)
productName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productName.setStatus("current")
_SerialNumber_Type = Gauge32
_SerialNumber_Object = MibScalar
serialNumber = _SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 1, 1, 2),
    _SerialNumber_Type()
)
serialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNumber.setStatus("current")


class _UnitType_Type(DisplayString):
    """Custom type unitType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_UnitType_Type.__name__ = "DisplayString"
_UnitType_Object = MibScalar
unitType = _UnitType_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 1, 1, 3),
    _UnitType_Type()
)
unitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitType.setStatus("current")
_Info_ObjectIdentity = ObjectIdentity
info = _Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33555, 1, 1, 2)
)


class _DeviceName_Type(DisplayString):
    """Custom type deviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_DeviceName_Type.__name__ = "DisplayString"
_DeviceName_Object = MibScalar
deviceName = _DeviceName_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 1, 2, 1),
    _DeviceName_Type()
)
deviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceName.setStatus("current")


class _SwVer_Type(DisplayString):
    """Custom type swVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SwVer_Type.__name__ = "DisplayString"
_SwVer_Object = MibScalar
swVer = _SwVer_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 1, 2, 2),
    _SwVer_Type()
)
swVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swVer.setStatus("current")


class _SwVerRadio_Type(DisplayString):
    """Custom type swVerRadio based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SwVerRadio_Type.__name__ = "DisplayString"
_SwVerRadio_Object = MibScalar
swVerRadio = _SwVerRadio_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 1, 2, 3),
    _SwVerRadio_Type()
)
swVerRadio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swVerRadio.setStatus("current")
_Status_ObjectIdentity = ObjectIdentity
status = _Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33555, 1, 1, 3)
)


class _SystemStatus_Type(Integer32):
    """Custom type systemStatus based on Integer32"""
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
        *(("na", 0),
          ("ok", 1),
          ("warning", 2),
          ("alarm", 3))
    )


_SystemStatus_Type.__name__ = "Integer32"
_SystemStatus_Object = MibScalar
systemStatus = _SystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 1, 3, 1),
    _SystemStatus_Type()
)
systemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatus.setStatus("current")


class _LineStatus_Type(Integer32):
    """Custom type lineStatus based on Integer32"""
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
        *(("na", 0),
          ("ok", 1),
          ("analyzer", 2),
          ("connecting", 3),
          ("searching", 4))
    )


_LineStatus_Type.__name__ = "Integer32"
_LineStatus_Object = MibScalar
lineStatus = _LineStatus_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 1, 3, 2),
    _LineStatus_Type()
)
lineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineStatus.setStatus("current")
_PeerNumber_Type = Gauge32
_PeerNumber_Object = MibScalar
peerNumber = _PeerNumber_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 1, 3, 3),
    _PeerNumber_Type()
)
peerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peerNumber.setStatus("current")


class _RfPowerStatus_Type(Integer32):
    """Custom type rfPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("ok", 1),
          ("fail", 2))
    )


_RfPowerStatus_Type.__name__ = "Integer32"
_RfPowerStatus_Object = MibScalar
rfPowerStatus = _RfPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 1, 3, 4),
    _RfPowerStatus_Type()
)
rfPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfPowerStatus.setStatus("current")
_SearchModeDisabled_Type = OptionSetting
_SearchModeDisabled_Object = MibScalar
searchModeDisabled = _SearchModeDisabled_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 1, 3, 5),
    _SearchModeDisabled_Type()
)
searchModeDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    searchModeDisabled.setStatus("current")
_EthPeer_Type = ServiceState
_EthPeer_Object = MibScalar
ethPeer = _EthPeer_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 1, 3, 6),
    _EthPeer_Type()
)
ethPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethPeer.setStatus("current")
_SecurePeerMode_Type = OptionSetting
_SecurePeerMode_Object = MibScalar
securePeerMode = _SecurePeerMode_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 1, 3, 7),
    _SecurePeerMode_Type()
)
securePeerMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securePeerMode.setStatus("current")


class _LineStatusII_Type(Integer32):
    """Custom type lineStatusII based on Integer32"""
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
        *(("na", 0),
          ("setup", 1),
          ("single", 2),
          ("connecting", 3),
          ("authorizing", 4),
          ("ok", 5),
          ("analyzer", 6))
    )


_LineStatusII_Type.__name__ = "Integer32"
_LineStatusII_Object = MibScalar
lineStatusII = _LineStatusII_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 1, 3, 8),
    _LineStatusII_Type()
)
lineStatusII.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineStatusII.setStatus("current")
_Eth1Link_Type = ServiceState
_Eth1Link_Object = MibScalar
eth1Link = _Eth1Link_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 1, 3, 9),
    _Eth1Link_Type()
)
eth1Link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth1Link.setStatus("current")
_Eth2Link_Type = ServiceState
_Eth2Link_Object = MibScalar
eth2Link = _Eth2Link_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 1, 3, 10),
    _Eth2Link_Type()
)
eth2Link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth2Link.setStatus("current")
_Chassis_ObjectIdentity = ObjectIdentity
chassis = _Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33555, 1, 1, 4)
)
_TemperatureModem_Type = Integer32
_TemperatureModem_Object = MibScalar
temperatureModem = _TemperatureModem_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 1, 4, 1),
    _TemperatureModem_Type()
)
temperatureModem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureModem.setStatus("current")
_TemperatureRadio_Type = Integer32
_TemperatureRadio_Object = MibScalar
temperatureRadio = _TemperatureRadio_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 1, 4, 2),
    _TemperatureRadio_Type()
)
temperatureRadio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureRadio.setStatus("current")
_VoltageUnit_Type = Integer32
_VoltageUnit_Object = MibScalar
voltageUnit = _VoltageUnit_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 1, 4, 3),
    _VoltageUnit_Type()
)
voltageUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageUnit.setStatus("current")


class _VoltageSource_Type(Integer32):
    """Custom type voltageSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("aux", 1),
          ("poe", 2))
    )


_VoltageSource_Type.__name__ = "Integer32"
_VoltageSource_Object = MibScalar
voltageSource = _VoltageSource_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 1, 4, 4),
    _VoltageSource_Type()
)
voltageSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageSource.setStatus("current")
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33555, 1, 1, 5)
)
_UseCpu_Type = Integer32
_UseCpu_Object = MibScalar
useCpu = _UseCpu_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 1, 5, 1),
    _UseCpu_Type()
)
useCpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    useCpu.setStatus("current")
_UseMemory_Type = Integer32
_UseMemory_Object = MibScalar
useMemory = _UseMemory_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 1, 5, 2),
    _UseMemory_Type()
)
useMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    useMemory.setStatus("current")
_UseLogStorage_Type = Integer32
_UseLogStorage_Object = MibScalar
useLogStorage = _UseLogStorage_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 1, 5, 3),
    _UseLogStorage_Type()
)
useLogStorage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    useLogStorage.setStatus("current")
_Access_ObjectIdentity = ObjectIdentity
access = _Access_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33555, 1, 1, 6)
)


class _Sshd_Type(Integer32):
    """Custom type sshd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("onlykey", 2),
          ("off", 3))
    )


_Sshd_Type.__name__ = "Integer32"
_Sshd_Object = MibScalar
sshd = _Sshd_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 1, 6, 1),
    _Sshd_Type()
)
sshd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshd.setStatus("current")
_Telnetd_Type = OptionSetting
_Telnetd_Object = MibScalar
telnetd = _Telnetd_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 1, 6, 2),
    _Telnetd_Type()
)
telnetd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telnetd.setStatus("current")
_Httpd_Type = OptionSetting
_Httpd_Object = MibScalar
httpd = _Httpd_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 1, 6, 3),
    _Httpd_Type()
)
httpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpd.setStatus("current")
_Ip_Type = IpAddress
_Ip_Object = MibScalar
ip = _Ip_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 1, 6, 4),
    _Ip_Type()
)
ip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip.setStatus("current")
_Mac_Type = PhysAddress
_Mac_Object = MibScalar
mac = _Mac_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 1, 6, 5),
    _Mac_Type()
)
mac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mac.setStatus("current")
_ManagementVlan_Type = OptionSetting
_ManagementVlan_Object = MibScalar
managementVlan = _ManagementVlan_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 1, 6, 6),
    _ManagementVlan_Type()
)
managementVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    managementVlan.setStatus("current")
_ManagementVlanId_Type = Integer32
_ManagementVlanId_Object = MibScalar
managementVlanId = _ManagementVlanId_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 1, 6, 7),
    _ManagementVlanId_Type()
)
managementVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    managementVlanId.setStatus("current")
_WifiHAP_Type = OptionSetting
_WifiHAP_Object = MibScalar
wifiHAP = _WifiHAP_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 1, 6, 8),
    _WifiHAP_Type()
)
wifiHAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wifiHAP.setStatus("current")
_Authorization_ObjectIdentity = ObjectIdentity
authorization = _Authorization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33555, 1, 1, 7)
)
_KeyTable_Object = MibTable
keyTable = _KeyTable_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 1, 7, 1)
)
if mibBuilder.loadTexts:
    keyTable.setStatus("current")
_KeyEntry_Object = MibTableRow
keyEntry = _KeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 1, 7, 1, 1)
)
keyEntry.setIndexNames(
    (0, "RAY-MIB", "keyName"),
)
if mibBuilder.loadTexts:
    keyEntry.setStatus("current")


class _KeyName_Type(DisplayString):
    """Custom type keyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_KeyName_Type.__name__ = "DisplayString"
_KeyName_Object = MibTableColumn
keyName = _KeyName_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 1, 7, 1, 1, 1),
    _KeyName_Type()
)
keyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keyName.setStatus("current")
_Alarm_ObjectIdentity = ObjectIdentity
alarm = _Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33555, 1, 1, 8)
)
_AlarmTemperature_Type = AlarmState
_AlarmTemperature_Object = MibScalar
alarmTemperature = _AlarmTemperature_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 1, 8, 1),
    _AlarmTemperature_Type()
)
alarmTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmTemperature.setStatus("current")
_AlarmVoltageLow_Type = AlarmState
_AlarmVoltageLow_Object = MibScalar
alarmVoltageLow = _AlarmVoltageLow_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 1, 8, 2),
    _AlarmVoltageLow_Type()
)
alarmVoltageLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmVoltageLow.setStatus("current")
_AlarmVoltageHigh_Type = AlarmState
_AlarmVoltageHigh_Object = MibScalar
alarmVoltageHigh = _AlarmVoltageHigh_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 1, 8, 3),
    _AlarmVoltageHigh_Type()
)
alarmVoltageHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmVoltageHigh.setStatus("current")
_AlarmRss_Type = AlarmState
_AlarmRss_Object = MibScalar
alarmRss = _AlarmRss_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 1, 8, 4),
    _AlarmRss_Type()
)
alarmRss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmRss.setStatus("current")
_AlarmSnr_Type = AlarmState
_AlarmSnr_Object = MibScalar
alarmSnr = _AlarmSnr_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 1, 8, 5),
    _AlarmSnr_Type()
)
alarmSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmSnr.setStatus("current")
_AlarmBer_Type = AlarmState
_AlarmBer_Object = MibScalar
alarmBer = _AlarmBer_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 1, 8, 6),
    _AlarmBer_Type()
)
alarmBer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmBer.setStatus("current")
_AlarmPeerDisconnected_Type = AlarmState
_AlarmPeerDisconnected_Object = MibScalar
alarmPeerDisconnected = _AlarmPeerDisconnected_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 1, 8, 7),
    _AlarmPeerDisconnected_Type()
)
alarmPeerDisconnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmPeerDisconnected.setStatus("current")
_AlarmEth1Down_Type = AlarmState
_AlarmEth1Down_Object = MibScalar
alarmEth1Down = _AlarmEth1Down_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 1, 8, 8),
    _AlarmEth1Down_Type()
)
alarmEth1Down.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmEth1Down.setStatus("current")
_AlarmEth2Down_Type = AlarmState
_AlarmEth2Down_Object = MibScalar
alarmEth2Down = _AlarmEth2Down_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 1, 8, 9),
    _AlarmEth2Down_Type()
)
alarmEth2Down.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmEth2Down.setStatus("current")
_AlarmRfPowerFail_Type = AlarmState
_AlarmRfPowerFail_Object = MibScalar
alarmRfPowerFail = _AlarmRfPowerFail_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 1, 8, 10),
    _AlarmRfPowerFail_Type()
)
alarmRfPowerFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmRfPowerFail.setStatus("current")
_AlarmNetBitrate_Type = AlarmState
_AlarmNetBitrate_Object = MibScalar
alarmNetBitrate = _AlarmNetBitrate_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 1, 8, 11),
    _AlarmNetBitrate_Type()
)
alarmNetBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmNetBitrate.setStatus("current")
_AlarmWifiOn_Type = AlarmState
_AlarmWifiOn_Object = MibScalar
alarmWifiOn = _AlarmWifiOn_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 1, 8, 12),
    _AlarmWifiOn_Type()
)
alarmWifiOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmWifiOn.setStatus("current")
_Interface_ObjectIdentity = ObjectIdentity
interface = _Interface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33555, 1, 2)
)
_IfRadio_ObjectIdentity = ObjectIdentity
ifRadio = _IfRadio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33555, 1, 2, 1)
)


class _RxChannel_Type(DisplayString):
    """Custom type rxChannel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_RxChannel_Type.__name__ = "DisplayString"
_RxChannel_Object = MibScalar
rxChannel = _RxChannel_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 2, 1, 1),
    _RxChannel_Type()
)
rxChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxChannel.setStatus("current")


class _TxChannel_Type(DisplayString):
    """Custom type txChannel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_TxChannel_Type.__name__ = "DisplayString"
_TxChannel_Object = MibScalar
txChannel = _TxChannel_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 2, 1, 2),
    _TxChannel_Type()
)
txChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txChannel.setStatus("current")
_RxFreq_Type = Gauge32
_RxFreq_Object = MibScalar
rxFreq = _RxFreq_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 2, 1, 3),
    _RxFreq_Type()
)
rxFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxFreq.setStatus("current")
_TxFreq_Type = Gauge32
_TxFreq_Object = MibScalar
txFreq = _TxFreq_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 2, 1, 4),
    _TxFreq_Type()
)
txFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txFreq.setStatus("current")
_RxModulation_Type = DisplayString
_RxModulation_Object = MibScalar
rxModulation = _RxModulation_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 2, 1, 5),
    _RxModulation_Type()
)
rxModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxModulation.setStatus("current")
_TxModulation_Type = DisplayString
_TxModulation_Object = MibScalar
txModulation = _TxModulation_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 2, 1, 6),
    _TxModulation_Type()
)
txModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txModulation.setStatus("current")
_RxModulationIndex_Type = ModulationList
_RxModulationIndex_Object = MibScalar
rxModulationIndex = _RxModulationIndex_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 2, 1, 7),
    _RxModulationIndex_Type()
)
rxModulationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxModulationIndex.setStatus("current")
_TxModulationIndex_Type = ModulationList
_TxModulationIndex_Object = MibScalar
txModulationIndex = _TxModulationIndex_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 2, 1, 8),
    _TxModulationIndex_Type()
)
txModulationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txModulationIndex.setStatus("current")


class _Bandwidth_Type(Integer32):
    """Custom type bandwidth based on Integer32"""
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
        *(("na", 0),
          ("bw-28MHz", 1),
          ("bw-14MHz", 2),
          ("bw-7MHz", 3))
    )


_Bandwidth_Type.__name__ = "Integer32"
_Bandwidth_Object = MibScalar
bandwidth = _Bandwidth_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 2, 1, 9),
    _Bandwidth_Type()
)
bandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandwidth.setStatus("current")


class _Coding_Type(Integer32):
    """Custom type coding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("low", 1),
          ("hi", 2))
    )


_Coding_Type.__name__ = "Integer32"
_Coding_Object = MibScalar
coding = _Coding_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 2, 1, 10),
    _Coding_Type()
)
coding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coding.setStatus("current")
_Matching_Type = OptionSetting
_Matching_Object = MibScalar
matching = _Matching_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 2, 1, 11),
    _Matching_Type()
)
matching.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matching.setStatus("current")
_RfPowerConfigured_Type = Integer32
_RfPowerConfigured_Object = MibScalar
rfPowerConfigured = _RfPowerConfigured_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 2, 1, 12),
    _RfPowerConfigured_Type()
)
rfPowerConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfPowerConfigured.setStatus("current")
_NetBitrate_Type = Integer32
_NetBitrate_Object = MibScalar
netBitrate = _NetBitrate_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 2, 1, 13),
    _NetBitrate_Type()
)
netBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBitrate.setStatus("current")
_MaxNetBitrate_Type = Integer32
_MaxNetBitrate_Object = MibScalar
maxNetBitrate = _MaxNetBitrate_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 2, 1, 14),
    _MaxNetBitrate_Type()
)
maxNetBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNetBitrate.setStatus("current")
_BandwidthKHz_Type = Integer32
_BandwidthKHz_Object = MibScalar
bandwidthKHz = _BandwidthKHz_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 2, 1, 15),
    _BandwidthKHz_Type()
)
bandwidthKHz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandwidthKHz.setStatus("current")


class _ChannelArrangement_Type(Integer32):
    """Custom type channelArrangement based on Integer32"""
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
        *(("na", 0),
          ("accp", 1),
          ("acap", 2),
          ("ccdp", 3))
    )


_ChannelArrangement_Type.__name__ = "Integer32"
_ChannelArrangement_Object = MibScalar
channelArrangement = _ChannelArrangement_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 2, 1, 16),
    _ChannelArrangement_Type()
)
channelArrangement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelArrangement.setStatus("current")
_RfPowerCurrent_Type = Integer32
_RfPowerCurrent_Object = MibScalar
rfPowerCurrent = _RfPowerCurrent_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 2, 1, 17),
    _RfPowerCurrent_Type()
)
rfPowerCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfPowerCurrent.setStatus("current")
_IfEth_ObjectIdentity = ObjectIdentity
ifEth = _IfEth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33555, 1, 2, 2)
)
_IfEthTable_Object = MibTable
ifEthTable = _IfEthTable_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ifEthTable.setStatus("current")
_IfEthEntry_Object = MibTableRow
ifEthEntry = _IfEthEntry_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 2, 2, 1, 1)
)
ifEthEntry.setIndexNames(
    (0, "RAY-MIB", "speed"),
)
if mibBuilder.loadTexts:
    ifEthEntry.setStatus("current")


class _Speed_Type(Integer32):
    """Custom type speed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000000),
    )


_Speed_Type.__name__ = "Integer32"
_Speed_Object = MibTableColumn
speed = _Speed_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 2, 2, 1, 1, 1),
    _Speed_Type()
)
speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speed.setStatus("current")


class _Duplex_Type(Integer32):
    """Custom type duplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("full", 1),
          ("half", 2))
    )


_Duplex_Type.__name__ = "Integer32"
_Duplex_Object = MibTableColumn
duplex = _Duplex_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 2, 2, 1, 1, 2),
    _Duplex_Type()
)
duplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    duplex.setStatus("current")


class _Mdix_Type(Integer32):
    """Custom type mdix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("mdi", 1),
          ("mdi-x", 2))
    )


_Mdix_Type.__name__ = "Integer32"
_Mdix_Object = MibTableColumn
mdix = _Mdix_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 2, 2, 1, 1, 3),
    _Mdix_Type()
)
mdix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdix.setStatus("current")
_Autonego_Type = OptionSetting
_Autonego_Object = MibTableColumn
autonego = _Autonego_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 2, 2, 1, 1, 4),
    _Autonego_Type()
)
autonego.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autonego.setStatus("current")
_Pause_Type = OptionSetting
_Pause_Object = MibTableColumn
pause = _Pause_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 2, 2, 1, 1, 5),
    _Pause_Type()
)
pause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pause.setStatus("current")
_AsymPause_Type = OptionSetting
_AsymPause_Object = MibTableColumn
asymPause = _AsymPause_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 2, 2, 1, 1, 6),
    _AsymPause_Type()
)
asymPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asymPause.setStatus("current")
_Prioritized_Type = OptionSetting
_Prioritized_Object = MibScalar
prioritized = _Prioritized_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 2, 2, 2),
    _Prioritized_Type()
)
prioritized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prioritized.setStatus("current")
_VlanId_Type = Integer32
_VlanId_Object = MibScalar
vlanId = _VlanId_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 2, 2, 3),
    _VlanId_Type()
)
vlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanId.setStatus("current")
_ServiceVlanId_Type = Integer32
_ServiceVlanId_Object = MibScalar
serviceVlanId = _ServiceVlanId_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 2, 2, 4),
    _ServiceVlanId_Type()
)
serviceVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceVlanId.setStatus("current")
_Statistic_ObjectIdentity = ObjectIdentity
statistic = _Statistic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33555, 1, 3)
)
_ModemR_ObjectIdentity = ObjectIdentity
modemR = _ModemR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33555, 1, 3, 1)
)
_RxPauseFrames_Type = Counter32
_RxPauseFrames_Object = MibScalar
rxPauseFrames = _RxPauseFrames_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 3, 1, 1),
    _RxPauseFrames_Type()
)
rxPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxPauseFrames.setStatus("current")
_RxControlFrames_Type = Counter32
_RxControlFrames_Object = MibScalar
rxControlFrames = _RxControlFrames_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 3, 1, 2),
    _RxControlFrames_Type()
)
rxControlFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxControlFrames.setStatus("current")
_RxBroadcast_Type = Counter32
_RxBroadcast_Object = MibScalar
rxBroadcast = _RxBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 3, 1, 3),
    _RxBroadcast_Type()
)
rxBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxBroadcast.setStatus("current")
_RxMulticast_Type = Counter32
_RxMulticast_Object = MibScalar
rxMulticast = _RxMulticast_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 3, 1, 4),
    _RxMulticast_Type()
)
rxMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxMulticast.setStatus("current")
_RxDones_Type = Counter32
_RxDones_Object = MibScalar
rxDones = _RxDones_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 3, 1, 5),
    _RxDones_Type()
)
rxDones.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxDones.setStatus("current")
_RxOutOfRangeErrors_Type = Counter32
_RxOutOfRangeErrors_Object = MibScalar
rxOutOfRangeErrors = _RxOutOfRangeErrors_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 3, 1, 6),
    _RxOutOfRangeErrors_Type()
)
rxOutOfRangeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxOutOfRangeErrors.setStatus("current")
_RxCrcErrors_Type = Counter32
_RxCrcErrors_Object = MibScalar
rxCrcErrors = _RxCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 3, 1, 7),
    _RxCrcErrors_Type()
)
rxCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxCrcErrors.setStatus("current")
_RxCodeErrors_Type = Counter32
_RxCodeErrors_Object = MibScalar
rxCodeErrors = _RxCodeErrors_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 3, 1, 8),
    _RxCodeErrors_Type()
)
rxCodeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxCodeErrors.setStatus("current")
_RxFalseCarrierErrors_Type = Counter32
_RxFalseCarrierErrors_Object = MibScalar
rxFalseCarrierErrors = _RxFalseCarrierErrors_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 3, 1, 9),
    _RxFalseCarrierErrors_Type()
)
rxFalseCarrierErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxFalseCarrierErrors.setStatus("current")
_RxDroppedPkts_Type = Counter32
_RxDroppedPkts_Object = MibScalar
rxDroppedPkts = _RxDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 3, 1, 10),
    _RxDroppedPkts_Type()
)
rxDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxDroppedPkts.setStatus("current")
_RxHCBytes_Type = Counter64
_RxHCBytes_Object = MibScalar
rxHCBytes = _RxHCBytes_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 3, 1, 11),
    _RxHCBytes_Type()
)
rxHCBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxHCBytes.setStatus("current")
_TxPauseFrames_Type = Counter32
_TxPauseFrames_Object = MibScalar
txPauseFrames = _TxPauseFrames_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 3, 1, 12),
    _TxPauseFrames_Type()
)
txPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txPauseFrames.setStatus("current")
_TxControlFrames_Type = Counter32
_TxControlFrames_Object = MibScalar
txControlFrames = _TxControlFrames_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 3, 1, 13),
    _TxControlFrames_Type()
)
txControlFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txControlFrames.setStatus("current")
_TxBroadcast_Type = Counter32
_TxBroadcast_Object = MibScalar
txBroadcast = _TxBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 3, 1, 14),
    _TxBroadcast_Type()
)
txBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txBroadcast.setStatus("current")
_TxMulticast_Type = Counter32
_TxMulticast_Object = MibScalar
txMulticast = _TxMulticast_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 3, 1, 15),
    _TxMulticast_Type()
)
txMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txMulticast.setStatus("current")
_TxDones_Type = Counter32
_TxDones_Object = MibScalar
txDones = _TxDones_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 3, 1, 16),
    _TxDones_Type()
)
txDones.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txDones.setStatus("current")
_TxLengthCheckErrors_Type = Counter32
_TxLengthCheckErrors_Object = MibScalar
txLengthCheckErrors = _TxLengthCheckErrors_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 3, 1, 17),
    _TxLengthCheckErrors_Type()
)
txLengthCheckErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txLengthCheckErrors.setStatus("current")
_TxCrcErrors_Type = Counter32
_TxCrcErrors_Object = MibScalar
txCrcErrors = _TxCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 3, 1, 18),
    _TxCrcErrors_Type()
)
txCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txCrcErrors.setStatus("current")
_TxCollisions_Type = Counter32
_TxCollisions_Object = MibScalar
txCollisions = _TxCollisions_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 3, 1, 19),
    _TxCollisions_Type()
)
txCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txCollisions.setStatus("current")
_TxHCBytes_Type = Counter64
_TxHCBytes_Object = MibScalar
txHCBytes = _TxHCBytes_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 3, 1, 20),
    _TxHCBytes_Type()
)
txHCBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txHCBytes.setStatus("current")
_Radio_ObjectIdentity = ObjectIdentity
radio = _Radio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33555, 1, 3, 2)
)
_Rss_Type = Integer32
_Rss_Object = MibScalar
rss = _Rss_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 3, 2, 1),
    _Rss_Type()
)
rss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rss.setStatus("current")
_Snr_Type = Integer32
_Snr_Object = MibScalar
snr = _Snr_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 3, 2, 2),
    _Snr_Type()
)
snr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snr.setStatus("current")
_FecBlockCounter_Type = Counter32
_FecBlockCounter_Object = MibScalar
fecBlockCounter = _FecBlockCounter_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 3, 2, 3),
    _FecBlockCounter_Type()
)
fecBlockCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fecBlockCounter.setStatus("current")
_FecUncorrectBlockCounter_Type = Counter32
_FecUncorrectBlockCounter_Object = MibScalar
fecUncorrectBlockCounter = _FecUncorrectBlockCounter_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 3, 2, 4),
    _FecUncorrectBlockCounter_Type()
)
fecUncorrectBlockCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fecUncorrectBlockCounter.setStatus("current")
_TimeAllConnect_Type = TimeTicks
_TimeAllConnect_Object = MibScalar
timeAllConnect = _TimeAllConnect_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 3, 2, 5),
    _TimeAllConnect_Type()
)
timeAllConnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeAllConnect.setStatus("current")
_TimeAllDisconnect_Type = TimeTicks
_TimeAllDisconnect_Object = MibScalar
timeAllDisconnect = _TimeAllDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 3, 2, 6),
    _TimeAllDisconnect_Type()
)
timeAllDisconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeAllDisconnect.setStatus("current")
_TimeMaxDisconnect_Type = TimeTicks
_TimeMaxDisconnect_Object = MibScalar
timeMaxDisconnect = _TimeMaxDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 3, 2, 7),
    _TimeMaxDisconnect_Type()
)
timeMaxDisconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeMaxDisconnect.setStatus("current")
_NumDisconnect_Type = Counter32
_NumDisconnect_Object = MibScalar
numDisconnect = _NumDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 3, 2, 8),
    _NumDisconnect_Type()
)
numDisconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numDisconnect.setStatus("current")
_Reliability_Type = Integer32
_Reliability_Object = MibScalar
reliability = _Reliability_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 3, 2, 9),
    _Reliability_Type()
)
reliability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reliability.setStatus("current")
_LinkUptime_Type = TimeTicks
_LinkUptime_Object = MibScalar
linkUptime = _LinkUptime_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 3, 2, 10),
    _LinkUptime_Type()
)
linkUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkUptime.setStatus("current")
_Ber_Type = Integer32
_Ber_Object = MibScalar
ber = _Ber_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 3, 2, 11),
    _Ber_Type()
)
ber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ber.setStatus("current")
_Ethernet_ObjectIdentity = ObjectIdentity
ethernet = _Ethernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33555, 1, 3, 3)
)
_EthInThroughput_Type = Integer32
_EthInThroughput_Object = MibScalar
ethInThroughput = _EthInThroughput_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 3, 3, 1),
    _EthInThroughput_Type()
)
ethInThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethInThroughput.setStatus("current")
_EthOutThroughput_Type = Integer32
_EthOutThroughput_Object = MibScalar
ethOutThroughput = _EthOutThroughput_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 3, 3, 2),
    _EthOutThroughput_Type()
)
ethOutThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOutThroughput.setStatus("current")
_Eth2InThroughput_Type = Integer32
_Eth2InThroughput_Object = MibScalar
eth2InThroughput = _Eth2InThroughput_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 3, 3, 3),
    _Eth2InThroughput_Type()
)
eth2InThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth2InThroughput.setStatus("current")
_Eth2OutThroughput_Type = Integer32
_Eth2OutThroughput_Object = MibScalar
eth2OutThroughput = _Eth2OutThroughput_Object(
    (1, 3, 6, 1, 4, 1, 33555, 1, 3, 3, 4),
    _Eth2OutThroughput_Type()
)
eth2OutThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth2OutThroughput.setStatus("current")
_RayTraps_ObjectIdentity = ObjectIdentity
rayTraps = _RayTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33555, 1, 10)
)
_Ray2Traps_ObjectIdentity = ObjectIdentity
ray2Traps = _Ray2Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33555, 1, 11)
)

# Managed Objects groups


# Notification objects

airDisconnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 33555, 1, 10, 1)
)
airDisconnect.setObjects(
    ("RAY-MIB", "lineStatus")
)
if mibBuilder.loadTexts:
    airDisconnect.setStatus(
        "current"
    )

airConnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 33555, 1, 10, 2)
)
airConnect.setObjects(
    ("RAY-MIB", "lineStatus")
)
if mibBuilder.loadTexts:
    airConnect.setStatus(
        "current"
    )

airWdog = NotificationType(
    (1, 3, 6, 1, 4, 1, 33555, 1, 10, 3)
)
airWdog.setObjects(
    ("RAY-MIB", "lineStatus")
)
if mibBuilder.loadTexts:
    airWdog.setStatus(
        "current"
    )

tempAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33555, 1, 10, 4)
)
tempAlarm.setObjects(
    ("RAY-MIB", "temperatureModem")
)
if mibBuilder.loadTexts:
    tempAlarm.setStatus(
        "current"
    )

powerAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33555, 1, 10, 5)
)
powerAlarm.setObjects(
    ("RAY-MIB", "voltageUnit")
)
if mibBuilder.loadTexts:
    powerAlarm.setStatus(
        "current"
    )

memoryAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33555, 1, 10, 6)
)
memoryAlarm.setObjects(
    ("RAY-MIB", "useMemory")
)
if mibBuilder.loadTexts:
    memoryAlarm.setStatus(
        "current"
    )

rssAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33555, 1, 10, 7)
)
rssAlarm.setObjects(
    ("RAY-MIB", "rss")
)
if mibBuilder.loadTexts:
    rssAlarm.setStatus(
        "current"
    )

snrAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33555, 1, 10, 8)
)
snrAlarm.setObjects(
    ("RAY-MIB", "snr")
)
if mibBuilder.loadTexts:
    snrAlarm.setStatus(
        "current"
    )

berAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33555, 1, 10, 9)
)
berAlarm.setObjects(
      *(("RAY-MIB", "fecUncorrectBlockCounter"),
        ("RAY-MIB", "fecBlockCounter"))
)
if mibBuilder.loadTexts:
    berAlarm.setStatus(
        "current"
    )

rfPowerFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 33555, 1, 10, 10)
)
rfPowerFail.setObjects(
    ("RAY-MIB", "rfPowerStatus")
)
if mibBuilder.loadTexts:
    rfPowerFail.setStatus(
        "current"
    )

peerEthLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 33555, 1, 10, 11)
)
peerEthLinkDown.setObjects(
    ("RAY-MIB", "ethPeer")
)
if mibBuilder.loadTexts:
    peerEthLinkDown.setStatus(
        "current"
    )

tr2TemperatureAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33555, 1, 11, 1)
)
tr2TemperatureAlarm.setObjects(
      *(("RAY-MIB", "temperatureModem"),
        ("RAY-MIB", "alarmTemperature"))
)
if mibBuilder.loadTexts:
    tr2TemperatureAlarm.setStatus(
        "current"
    )

tr2VoltageLowAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33555, 1, 11, 2)
)
tr2VoltageLowAlarm.setObjects(
      *(("RAY-MIB", "voltageUnit"),
        ("RAY-MIB", "alarmVoltageLow"))
)
if mibBuilder.loadTexts:
    tr2VoltageLowAlarm.setStatus(
        "current"
    )

tr2VoltageHighAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33555, 1, 11, 3)
)
tr2VoltageHighAlarm.setObjects(
      *(("RAY-MIB", "voltageUnit"),
        ("RAY-MIB", "alarmVoltageHigh"))
)
if mibBuilder.loadTexts:
    tr2VoltageHighAlarm.setStatus(
        "current"
    )

tr2RssAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33555, 1, 11, 4)
)
tr2RssAlarm.setObjects(
      *(("RAY-MIB", "rss"),
        ("RAY-MIB", "alarmRss"))
)
if mibBuilder.loadTexts:
    tr2RssAlarm.setStatus(
        "current"
    )

tr2SnrAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33555, 1, 11, 5)
)
tr2SnrAlarm.setObjects(
      *(("RAY-MIB", "snr"),
        ("RAY-MIB", "alarmSnr"))
)
if mibBuilder.loadTexts:
    tr2SnrAlarm.setStatus(
        "current"
    )

tr2BerAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33555, 1, 11, 6)
)
tr2BerAlarm.setObjects(
      *(("RAY-MIB", "ber"),
        ("RAY-MIB", "alarmBer"))
)
if mibBuilder.loadTexts:
    tr2BerAlarm.setStatus(
        "current"
    )

tr2AirDisconnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 33555, 1, 11, 7)
)
tr2AirDisconnect.setObjects(
      *(("RAY-MIB", "lineStatusII"),
        ("RAY-MIB", "alarmPeerDisconnected"))
)
if mibBuilder.loadTexts:
    tr2AirDisconnect.setStatus(
        "current"
    )

tr2AirConnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 33555, 1, 11, 8)
)
tr2AirConnect.setObjects(
      *(("RAY-MIB", "lineStatusII"),
        ("RAY-MIB", "alarmPeerDisconnected"))
)
if mibBuilder.loadTexts:
    tr2AirConnect.setStatus(
        "current"
    )

tr2Eth1LinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 33555, 1, 11, 9)
)
tr2Eth1LinkDown.setObjects(
      *(("RAY-MIB", "eth1Link"),
        ("RAY-MIB", "alarmEth1Down"))
)
if mibBuilder.loadTexts:
    tr2Eth1LinkDown.setStatus(
        "current"
    )

tr2Eth21LinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 33555, 1, 11, 10)
)
tr2Eth21LinkDown.setObjects(
      *(("RAY-MIB", "eth2Link"),
        ("RAY-MIB", "alarmEth2Down"))
)
if mibBuilder.loadTexts:
    tr2Eth21LinkDown.setStatus(
        "current"
    )

tr2RfPowerFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 33555, 1, 11, 11)
)
tr2RfPowerFail.setObjects(
      *(("RAY-MIB", "rfPowerStatus"),
        ("RAY-MIB", "alarmRfPowerFail"))
)
if mibBuilder.loadTexts:
    tr2RfPowerFail.setStatus(
        "current"
    )

tr2NetBitrate = NotificationType(
    (1, 3, 6, 1, 4, 1, 33555, 1, 11, 12)
)
tr2NetBitrate.setObjects(
      *(("RAY-MIB", "netBitrate"),
        ("RAY-MIB", "alarmNetBitrate"))
)
if mibBuilder.loadTexts:
    tr2NetBitrate.setStatus(
        "current"
    )

tr2WifiOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 33555, 1, 11, 13)
)
tr2WifiOn.setObjects(
      *(("RAY-MIB", "wifiHAP"),
        ("RAY-MIB", "alarmWifiOn"))
)
if mibBuilder.loadTexts:
    tr2WifiOn.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAY-MIB",
    **{"DisplayString": DisplayString,
       "PhysAddress": PhysAddress,
       "ServiceState": ServiceState,
       "AlarmState": AlarmState,
       "OptionSetting": OptionSetting,
       "ModulationList": ModulationList,
       "racom": racom,
       "ray": ray,
       "station": station,
       "product": product,
       "productName": productName,
       "serialNumber": serialNumber,
       "unitType": unitType,
       "info": info,
       "deviceName": deviceName,
       "swVer": swVer,
       "swVerRadio": swVerRadio,
       "status": status,
       "systemStatus": systemStatus,
       "lineStatus": lineStatus,
       "peerNumber": peerNumber,
       "rfPowerStatus": rfPowerStatus,
       "searchModeDisabled": searchModeDisabled,
       "ethPeer": ethPeer,
       "securePeerMode": securePeerMode,
       "lineStatusII": lineStatusII,
       "eth1Link": eth1Link,
       "eth2Link": eth2Link,
       "chassis": chassis,
       "temperatureModem": temperatureModem,
       "temperatureRadio": temperatureRadio,
       "voltageUnit": voltageUnit,
       "voltageSource": voltageSource,
       "system": system,
       "useCpu": useCpu,
       "useMemory": useMemory,
       "useLogStorage": useLogStorage,
       "access": access,
       "sshd": sshd,
       "telnetd": telnetd,
       "httpd": httpd,
       "ip": ip,
       "mac": mac,
       "managementVlan": managementVlan,
       "managementVlanId": managementVlanId,
       "wifiHAP": wifiHAP,
       "authorization": authorization,
       "keyTable": keyTable,
       "keyEntry": keyEntry,
       "keyName": keyName,
       "alarm": alarm,
       "alarmTemperature": alarmTemperature,
       "alarmVoltageLow": alarmVoltageLow,
       "alarmVoltageHigh": alarmVoltageHigh,
       "alarmRss": alarmRss,
       "alarmSnr": alarmSnr,
       "alarmBer": alarmBer,
       "alarmPeerDisconnected": alarmPeerDisconnected,
       "alarmEth1Down": alarmEth1Down,
       "alarmEth2Down": alarmEth2Down,
       "alarmRfPowerFail": alarmRfPowerFail,
       "alarmNetBitrate": alarmNetBitrate,
       "alarmWifiOn": alarmWifiOn,
       "interface": interface,
       "ifRadio": ifRadio,
       "rxChannel": rxChannel,
       "txChannel": txChannel,
       "rxFreq": rxFreq,
       "txFreq": txFreq,
       "rxModulation": rxModulation,
       "txModulation": txModulation,
       "rxModulationIndex": rxModulationIndex,
       "txModulationIndex": txModulationIndex,
       "bandwidth": bandwidth,
       "coding": coding,
       "matching": matching,
       "rfPowerConfigured": rfPowerConfigured,
       "netBitrate": netBitrate,
       "maxNetBitrate": maxNetBitrate,
       "bandwidthKHz": bandwidthKHz,
       "channelArrangement": channelArrangement,
       "rfPowerCurrent": rfPowerCurrent,
       "ifEth": ifEth,
       "ifEthTable": ifEthTable,
       "ifEthEntry": ifEthEntry,
       "speed": speed,
       "duplex": duplex,
       "mdix": mdix,
       "autonego": autonego,
       "pause": pause,
       "asymPause": asymPause,
       "prioritized": prioritized,
       "vlanId": vlanId,
       "serviceVlanId": serviceVlanId,
       "statistic": statistic,
       "modemR": modemR,
       "rxPauseFrames": rxPauseFrames,
       "rxControlFrames": rxControlFrames,
       "rxBroadcast": rxBroadcast,
       "rxMulticast": rxMulticast,
       "rxDones": rxDones,
       "rxOutOfRangeErrors": rxOutOfRangeErrors,
       "rxCrcErrors": rxCrcErrors,
       "rxCodeErrors": rxCodeErrors,
       "rxFalseCarrierErrors": rxFalseCarrierErrors,
       "rxDroppedPkts": rxDroppedPkts,
       "rxHCBytes": rxHCBytes,
       "txPauseFrames": txPauseFrames,
       "txControlFrames": txControlFrames,
       "txBroadcast": txBroadcast,
       "txMulticast": txMulticast,
       "txDones": txDones,
       "txLengthCheckErrors": txLengthCheckErrors,
       "txCrcErrors": txCrcErrors,
       "txCollisions": txCollisions,
       "txHCBytes": txHCBytes,
       "radio": radio,
       "rss": rss,
       "snr": snr,
       "fecBlockCounter": fecBlockCounter,
       "fecUncorrectBlockCounter": fecUncorrectBlockCounter,
       "timeAllConnect": timeAllConnect,
       "timeAllDisconnect": timeAllDisconnect,
       "timeMaxDisconnect": timeMaxDisconnect,
       "numDisconnect": numDisconnect,
       "reliability": reliability,
       "linkUptime": linkUptime,
       "ber": ber,
       "ethernet": ethernet,
       "ethInThroughput": ethInThroughput,
       "ethOutThroughput": ethOutThroughput,
       "eth2InThroughput": eth2InThroughput,
       "eth2OutThroughput": eth2OutThroughput,
       "rayTraps": rayTraps,
       "airDisconnect": airDisconnect,
       "airConnect": airConnect,
       "airWdog": airWdog,
       "tempAlarm": tempAlarm,
       "powerAlarm": powerAlarm,
       "memoryAlarm": memoryAlarm,
       "rssAlarm": rssAlarm,
       "snrAlarm": snrAlarm,
       "berAlarm": berAlarm,
       "rfPowerFail": rfPowerFail,
       "peerEthLinkDown": peerEthLinkDown,
       "ray2Traps": ray2Traps,
       "tr2TemperatureAlarm": tr2TemperatureAlarm,
       "tr2VoltageLowAlarm": tr2VoltageLowAlarm,
       "tr2VoltageHighAlarm": tr2VoltageHighAlarm,
       "tr2RssAlarm": tr2RssAlarm,
       "tr2SnrAlarm": tr2SnrAlarm,
       "tr2BerAlarm": tr2BerAlarm,
       "tr2AirDisconnect": tr2AirDisconnect,
       "tr2AirConnect": tr2AirConnect,
       "tr2Eth1LinkDown": tr2Eth1LinkDown,
       "tr2Eth21LinkDown": tr2Eth21LinkDown,
       "tr2RfPowerFail": tr2RfPowerFail,
       "tr2NetBitrate": tr2NetBitrate,
       "tr2WifiOn": tr2WifiOn}
)
