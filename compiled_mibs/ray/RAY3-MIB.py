# SNMP MIB module (RAY3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ray\RAY3-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:23:15 2025
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

racom = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 33555)
)
if mibBuilder.loadTexts:
    racom.setRevisions(
        ("2019-10-21 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Tenths(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-1"


class Hundredths(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-2"


class Thousandths(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-3"


class DisplayStringRaw(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class PhysAddressRaw(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x"


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
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("qpskS", 1),
          ("qpsk", 2),
          ("qam16", 3),
          ("qam32", 4),
          ("qam64", 5),
          ("qam128", 6),
          ("qam256", 7),
          ("qam512", 8),
          ("qam1024", 9),
          ("qam2048", 10),
          ("qam4096", 11))
    )



# MIB Managed Objects in the order of their OIDs

_Ray3_ObjectIdentity = ObjectIdentity
ray3 = _Ray3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33555, 4)
)
_Station_ObjectIdentity = ObjectIdentity
station = _Station_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33555, 4, 1)
)
_Product_ObjectIdentity = ObjectIdentity
product = _Product_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33555, 4, 1, 1)
)


class _ProductName_Type(DisplayStringRaw):
    """Custom type productName based on DisplayStringRaw"""
    subtypeSpec = DisplayStringRaw.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ProductName_Type.__name__ = "DisplayStringRaw"
_ProductName_Object = MibScalar
productName = _ProductName_Object(
    (1, 3, 6, 1, 4, 1, 33555, 4, 1, 1, 1),
    _ProductName_Type()
)
productName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productName.setStatus("current")
_SerialNumber_Type = Gauge32
_SerialNumber_Object = MibScalar
serialNumber = _SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 33555, 4, 1, 1, 2),
    _SerialNumber_Type()
)
serialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNumber.setStatus("current")


class _UnitType_Type(DisplayStringRaw):
    """Custom type unitType based on DisplayStringRaw"""
    subtypeSpec = DisplayStringRaw.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_UnitType_Type.__name__ = "DisplayStringRaw"
_UnitType_Object = MibScalar
unitType = _UnitType_Object(
    (1, 3, 6, 1, 4, 1, 33555, 4, 1, 1, 3),
    _UnitType_Type()
)
unitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitType.setStatus("current")
_Info_ObjectIdentity = ObjectIdentity
info = _Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33555, 4, 1, 2)
)


class _DeviceName_Type(DisplayStringRaw):
    """Custom type deviceName based on DisplayStringRaw"""
    subtypeSpec = DisplayStringRaw.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_DeviceName_Type.__name__ = "DisplayStringRaw"
_DeviceName_Object = MibScalar
deviceName = _DeviceName_Object(
    (1, 3, 6, 1, 4, 1, 33555, 4, 1, 2, 1),
    _DeviceName_Type()
)
deviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceName.setStatus("current")


class _SwVer_Type(DisplayStringRaw):
    """Custom type swVer based on DisplayStringRaw"""
    subtypeSpec = DisplayStringRaw.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SwVer_Type.__name__ = "DisplayStringRaw"
_SwVer_Object = MibScalar
swVer = _SwVer_Object(
    (1, 3, 6, 1, 4, 1, 33555, 4, 1, 2, 2),
    _SwVer_Type()
)
swVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swVer.setStatus("current")


class _SwVerRadio_Type(DisplayStringRaw):
    """Custom type swVerRadio based on DisplayStringRaw"""
    subtypeSpec = DisplayStringRaw.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SwVerRadio_Type.__name__ = "DisplayStringRaw"
_SwVerRadio_Object = MibScalar
swVerRadio = _SwVerRadio_Object(
    (1, 3, 6, 1, 4, 1, 33555, 4, 1, 2, 3),
    _SwVerRadio_Type()
)
swVerRadio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swVerRadio.setStatus("current")
_Status_ObjectIdentity = ObjectIdentity
status = _Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33555, 4, 1, 3)
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
    (1, 3, 6, 1, 4, 1, 33555, 4, 1, 3, 1),
    _SystemStatus_Type()
)
systemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatus.setStatus("current")
_PeerNumber_Type = Gauge32
_PeerNumber_Object = MibScalar
peerNumber = _PeerNumber_Object(
    (1, 3, 6, 1, 4, 1, 33555, 4, 1, 3, 3),
    _PeerNumber_Type()
)
peerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peerNumber.setStatus("current")
_SecurePeerMode_Type = OptionSetting
_SecurePeerMode_Object = MibScalar
securePeerMode = _SecurePeerMode_Object(
    (1, 3, 6, 1, 4, 1, 33555, 4, 1, 3, 7),
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
    (1, 3, 6, 1, 4, 1, 33555, 4, 1, 3, 8),
    _LineStatusII_Type()
)
lineStatusII.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineStatusII.setStatus("current")
_Eth1Link_Type = ServiceState
_Eth1Link_Object = MibScalar
eth1Link = _Eth1Link_Object(
    (1, 3, 6, 1, 4, 1, 33555, 4, 1, 3, 9),
    _Eth1Link_Type()
)
eth1Link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth1Link.setStatus("current")
_Eth2Link_Type = ServiceState
_Eth2Link_Object = MibScalar
eth2Link = _Eth2Link_Object(
    (1, 3, 6, 1, 4, 1, 33555, 4, 1, 3, 10),
    _Eth2Link_Type()
)
eth2Link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth2Link.setStatus("current")
_Chassis_ObjectIdentity = ObjectIdentity
chassis = _Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33555, 4, 1, 4)
)


class _TemperatureModem_Type(Hundredths):
    """Custom type temperatureModem based on Hundredths"""
    subtypeSpec = Hundredths.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10000, 10000),
    )


_TemperatureModem_Type.__name__ = "Hundredths"
_TemperatureModem_Object = MibScalar
temperatureModem = _TemperatureModem_Object(
    (1, 3, 6, 1, 4, 1, 33555, 4, 1, 4, 1),
    _TemperatureModem_Type()
)
temperatureModem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureModem.setStatus("current")
if mibBuilder.loadTexts:
    temperatureModem.setUnits("deg C")


class _TemperatureRadio_Type(Hundredths):
    """Custom type temperatureRadio based on Hundredths"""
    subtypeSpec = Hundredths.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10000, 10000),
    )


_TemperatureRadio_Type.__name__ = "Hundredths"
_TemperatureRadio_Object = MibScalar
temperatureRadio = _TemperatureRadio_Object(
    (1, 3, 6, 1, 4, 1, 33555, 4, 1, 4, 2),
    _TemperatureRadio_Type()
)
temperatureRadio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureRadio.setStatus("current")
if mibBuilder.loadTexts:
    temperatureRadio.setUnits("deg C")


class _VoltageUnit_Type(Tenths):
    """Custom type voltageUnit based on Tenths"""
    subtypeSpec = Tenths.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_VoltageUnit_Type.__name__ = "Tenths"
_VoltageUnit_Object = MibScalar
voltageUnit = _VoltageUnit_Object(
    (1, 3, 6, 1, 4, 1, 33555, 4, 1, 4, 3),
    _VoltageUnit_Type()
)
voltageUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageUnit.setStatus("current")
if mibBuilder.loadTexts:
    voltageUnit.setUnits("V")


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
    (1, 3, 6, 1, 4, 1, 33555, 4, 1, 4, 4),
    _VoltageSource_Type()
)
voltageSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageSource.setStatus("current")
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33555, 4, 1, 5)
)
_UseCpu_Type = Integer32
_UseCpu_Object = MibScalar
useCpu = _UseCpu_Object(
    (1, 3, 6, 1, 4, 1, 33555, 4, 1, 5, 1),
    _UseCpu_Type()
)
useCpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    useCpu.setStatus("current")
if mibBuilder.loadTexts:
    useCpu.setUnits("%")
_UseMemory_Type = Integer32
_UseMemory_Object = MibScalar
useMemory = _UseMemory_Object(
    (1, 3, 6, 1, 4, 1, 33555, 4, 1, 5, 2),
    _UseMemory_Type()
)
useMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    useMemory.setStatus("current")
if mibBuilder.loadTexts:
    useMemory.setUnits("%")
_UseLogStorage_Type = Integer32
_UseLogStorage_Object = MibScalar
useLogStorage = _UseLogStorage_Object(
    (1, 3, 6, 1, 4, 1, 33555, 4, 1, 5, 3),
    _UseLogStorage_Type()
)
useLogStorage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    useLogStorage.setStatus("current")
if mibBuilder.loadTexts:
    useLogStorage.setUnits("%")
_Access_ObjectIdentity = ObjectIdentity
access = _Access_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33555, 4, 1, 6)
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
    (1, 3, 6, 1, 4, 1, 33555, 4, 1, 6, 1),
    _Sshd_Type()
)
sshd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshd.setStatus("current")
_Telnetd_Type = OptionSetting
_Telnetd_Object = MibScalar
telnetd = _Telnetd_Object(
    (1, 3, 6, 1, 4, 1, 33555, 4, 1, 6, 2),
    _Telnetd_Type()
)
telnetd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telnetd.setStatus("current")
_Httpd_Type = OptionSetting
_Httpd_Object = MibScalar
httpd = _Httpd_Object(
    (1, 3, 6, 1, 4, 1, 33555, 4, 1, 6, 3),
    _Httpd_Type()
)
httpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpd.setStatus("current")
_Ip_Type = IpAddress
_Ip_Object = MibScalar
ip = _Ip_Object(
    (1, 3, 6, 1, 4, 1, 33555, 4, 1, 6, 4),
    _Ip_Type()
)
ip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip.setStatus("current")
_Mac_Type = PhysAddressRaw
_Mac_Object = MibScalar
mac = _Mac_Object(
    (1, 3, 6, 1, 4, 1, 33555, 4, 1, 6, 5),
    _Mac_Type()
)
mac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mac.setStatus("current")
_ManagementVlan_Type = OptionSetting
_ManagementVlan_Object = MibScalar
managementVlan = _ManagementVlan_Object(
    (1, 3, 6, 1, 4, 1, 33555, 4, 1, 6, 6),
    _ManagementVlan_Type()
)
managementVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    managementVlan.setStatus("current")
_ManagementVlanId_Type = Integer32
_ManagementVlanId_Object = MibScalar
managementVlanId = _ManagementVlanId_Object(
    (1, 3, 6, 1, 4, 1, 33555, 4, 1, 6, 7),
    _ManagementVlanId_Type()
)
managementVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    managementVlanId.setStatus("current")


class _WifiHAP_Type(Integer32):
    """Custom type wifiHAP based on Integer32"""
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
          ("disabled", 1),
          ("enabled-on-air-link-loss", 2),
          ("force-enabled", 3))
    )


_WifiHAP_Type.__name__ = "Integer32"
_WifiHAP_Object = MibScalar
wifiHAP = _WifiHAP_Object(
    (1, 3, 6, 1, 4, 1, 33555, 4, 1, 6, 8),
    _WifiHAP_Type()
)
wifiHAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wifiHAP.setStatus("current")
_Alarm_ObjectIdentity = ObjectIdentity
alarm = _Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33555, 4, 1, 8)
)
_AlarmTemperature_Type = AlarmState
_AlarmTemperature_Object = MibScalar
alarmTemperature = _AlarmTemperature_Object(
    (1, 3, 6, 1, 4, 1, 33555, 4, 1, 8, 1),
    _AlarmTemperature_Type()
)
alarmTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmTemperature.setStatus("current")
_AlarmVoltageLow_Type = AlarmState
_AlarmVoltageLow_Object = MibScalar
alarmVoltageLow = _AlarmVoltageLow_Object(
    (1, 3, 6, 1, 4, 1, 33555, 4, 1, 8, 2),
    _AlarmVoltageLow_Type()
)
alarmVoltageLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmVoltageLow.setStatus("current")
_AlarmVoltageHigh_Type = AlarmState
_AlarmVoltageHigh_Object = MibScalar
alarmVoltageHigh = _AlarmVoltageHigh_Object(
    (1, 3, 6, 1, 4, 1, 33555, 4, 1, 8, 3),
    _AlarmVoltageHigh_Type()
)
alarmVoltageHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmVoltageHigh.setStatus("current")
_AlarmRss_Type = AlarmState
_AlarmRss_Object = MibScalar
alarmRss = _AlarmRss_Object(
    (1, 3, 6, 1, 4, 1, 33555, 4, 1, 8, 4),
    _AlarmRss_Type()
)
alarmRss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmRss.setStatus("current")
_AlarmBer_Type = AlarmState
_AlarmBer_Object = MibScalar
alarmBer = _AlarmBer_Object(
    (1, 3, 6, 1, 4, 1, 33555, 4, 1, 8, 6),
    _AlarmBer_Type()
)
alarmBer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmBer.setStatus("current")
_AlarmPeerDisconnected_Type = AlarmState
_AlarmPeerDisconnected_Object = MibScalar
alarmPeerDisconnected = _AlarmPeerDisconnected_Object(
    (1, 3, 6, 1, 4, 1, 33555, 4, 1, 8, 7),
    _AlarmPeerDisconnected_Type()
)
alarmPeerDisconnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmPeerDisconnected.setStatus("current")
_AlarmEth1Down_Type = AlarmState
_AlarmEth1Down_Object = MibScalar
alarmEth1Down = _AlarmEth1Down_Object(
    (1, 3, 6, 1, 4, 1, 33555, 4, 1, 8, 8),
    _AlarmEth1Down_Type()
)
alarmEth1Down.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmEth1Down.setStatus("current")
_AlarmEth2Down_Type = AlarmState
_AlarmEth2Down_Object = MibScalar
alarmEth2Down = _AlarmEth2Down_Object(
    (1, 3, 6, 1, 4, 1, 33555, 4, 1, 8, 9),
    _AlarmEth2Down_Type()
)
alarmEth2Down.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmEth2Down.setStatus("current")
_AlarmNetBitrate_Type = AlarmState
_AlarmNetBitrate_Object = MibScalar
alarmNetBitrate = _AlarmNetBitrate_Object(
    (1, 3, 6, 1, 4, 1, 33555, 4, 1, 8, 11),
    _AlarmNetBitrate_Type()
)
alarmNetBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmNetBitrate.setStatus("current")
_AlarmWifiOn_Type = AlarmState
_AlarmWifiOn_Object = MibScalar
alarmWifiOn = _AlarmWifiOn_Object(
    (1, 3, 6, 1, 4, 1, 33555, 4, 1, 8, 12),
    _AlarmWifiOn_Type()
)
alarmWifiOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmWifiOn.setStatus("current")
_AlarmMse_Type = AlarmState
_AlarmMse_Object = MibScalar
alarmMse = _AlarmMse_Object(
    (1, 3, 6, 1, 4, 1, 33555, 4, 1, 8, 13),
    _AlarmMse_Type()
)
alarmMse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmMse.setStatus("current")
_Interface_ObjectIdentity = ObjectIdentity
interface = _Interface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33555, 4, 2)
)
_IfRadio_ObjectIdentity = ObjectIdentity
ifRadio = _IfRadio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33555, 4, 2, 1)
)


class _RxChannel_Type(DisplayStringRaw):
    """Custom type rxChannel based on DisplayStringRaw"""
    subtypeSpec = DisplayStringRaw.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_RxChannel_Type.__name__ = "DisplayStringRaw"
_RxChannel_Object = MibScalar
rxChannel = _RxChannel_Object(
    (1, 3, 6, 1, 4, 1, 33555, 4, 2, 1, 1),
    _RxChannel_Type()
)
rxChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxChannel.setStatus("current")


class _TxChannel_Type(DisplayStringRaw):
    """Custom type txChannel based on DisplayStringRaw"""
    subtypeSpec = DisplayStringRaw.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_TxChannel_Type.__name__ = "DisplayStringRaw"
_TxChannel_Object = MibScalar
txChannel = _TxChannel_Object(
    (1, 3, 6, 1, 4, 1, 33555, 4, 2, 1, 2),
    _TxChannel_Type()
)
txChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txChannel.setStatus("current")
_RxFreq_Type = Gauge32
_RxFreq_Object = MibScalar
rxFreq = _RxFreq_Object(
    (1, 3, 6, 1, 4, 1, 33555, 4, 2, 1, 3),
    _RxFreq_Type()
)
rxFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxFreq.setStatus("current")
if mibBuilder.loadTexts:
    rxFreq.setUnits("kHz")
_TxFreq_Type = Gauge32
_TxFreq_Object = MibScalar
txFreq = _TxFreq_Object(
    (1, 3, 6, 1, 4, 1, 33555, 4, 2, 1, 4),
    _TxFreq_Type()
)
txFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txFreq.setStatus("current")
if mibBuilder.loadTexts:
    txFreq.setUnits("kHz")
_RxModulation_Type = DisplayStringRaw
_RxModulation_Object = MibScalar
rxModulation = _RxModulation_Object(
    (1, 3, 6, 1, 4, 1, 33555, 4, 2, 1, 5),
    _RxModulation_Type()
)
rxModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxModulation.setStatus("current")
_TxModulation_Type = DisplayStringRaw
_TxModulation_Object = MibScalar
txModulation = _TxModulation_Object(
    (1, 3, 6, 1, 4, 1, 33555, 4, 2, 1, 6),
    _TxModulation_Type()
)
txModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txModulation.setStatus("current")
_RxModulationIndex_Type = ModulationList
_RxModulationIndex_Object = MibScalar
rxModulationIndex = _RxModulationIndex_Object(
    (1, 3, 6, 1, 4, 1, 33555, 4, 2, 1, 7),
    _RxModulationIndex_Type()
)
rxModulationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxModulationIndex.setStatus("current")
_TxModulationIndex_Type = ModulationList
_TxModulationIndex_Object = MibScalar
txModulationIndex = _TxModulationIndex_Object(
    (1, 3, 6, 1, 4, 1, 33555, 4, 2, 1, 8),
    _TxModulationIndex_Type()
)
txModulationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txModulationIndex.setStatus("current")
_Matching_Type = OptionSetting
_Matching_Object = MibScalar
matching = _Matching_Object(
    (1, 3, 6, 1, 4, 1, 33555, 4, 2, 1, 11),
    _Matching_Type()
)
matching.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matching.setStatus("current")
_RfPowerConfigured_Type = Integer32
_RfPowerConfigured_Object = MibScalar
rfPowerConfigured = _RfPowerConfigured_Object(
    (1, 3, 6, 1, 4, 1, 33555, 4, 2, 1, 12),
    _RfPowerConfigured_Type()
)
rfPowerConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfPowerConfigured.setStatus("current")
if mibBuilder.loadTexts:
    rfPowerConfigured.setUnits("dBm")
_NetBitrate_Type = Integer32
_NetBitrate_Object = MibScalar
netBitrate = _NetBitrate_Object(
    (1, 3, 6, 1, 4, 1, 33555, 4, 2, 1, 13),
    _NetBitrate_Type()
)
netBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBitrate.setStatus("current")
if mibBuilder.loadTexts:
    netBitrate.setUnits("kbps")
_MaxNetBitrate_Type = Integer32
_MaxNetBitrate_Object = MibScalar
maxNetBitrate = _MaxNetBitrate_Object(
    (1, 3, 6, 1, 4, 1, 33555, 4, 2, 1, 14),
    _MaxNetBitrate_Type()
)
maxNetBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNetBitrate.setStatus("current")
if mibBuilder.loadTexts:
    maxNetBitrate.setUnits("Mbps")
_TxBandwidthKHz_Type = Integer32
_TxBandwidthKHz_Object = MibScalar
txBandwidthKHz = _TxBandwidthKHz_Object(
    (1, 3, 6, 1, 4, 1, 33555, 4, 2, 1, 15),
    _TxBandwidthKHz_Type()
)
txBandwidthKHz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txBandwidthKHz.setStatus("current")
if mibBuilder.loadTexts:
    txBandwidthKHz.setUnits("kHz")


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
    (1, 3, 6, 1, 4, 1, 33555, 4, 2, 1, 16),
    _ChannelArrangement_Type()
)
channelArrangement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelArrangement.setStatus("current")
_RfPowerCurrent_Type = Integer32
_RfPowerCurrent_Object = MibScalar
rfPowerCurrent = _RfPowerCurrent_Object(
    (1, 3, 6, 1, 4, 1, 33555, 4, 2, 1, 17),
    _RfPowerCurrent_Type()
)
rfPowerCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfPowerCurrent.setStatus("current")
if mibBuilder.loadTexts:
    rfPowerCurrent.setUnits("dBm")
_Acm_Type = OptionSetting
_Acm_Object = MibScalar
acm = _Acm_Object(
    (1, 3, 6, 1, 4, 1, 33555, 4, 2, 1, 18),
    _Acm_Type()
)
acm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acm.setStatus("current")
_Atpc_Type = OptionSetting
_Atpc_Object = MibScalar
atpc = _Atpc_Object(
    (1, 3, 6, 1, 4, 1, 33555, 4, 2, 1, 19),
    _Atpc_Type()
)
atpc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atpc.setStatus("current")


class _FrequencyTable_Type(DisplayStringRaw):
    """Custom type frequencyTable based on DisplayStringRaw"""
    subtypeSpec = DisplayStringRaw.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FrequencyTable_Type.__name__ = "DisplayStringRaw"
_FrequencyTable_Object = MibScalar
frequencyTable = _FrequencyTable_Object(
    (1, 3, 6, 1, 4, 1, 33555, 4, 2, 1, 20),
    _FrequencyTable_Type()
)
frequencyTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frequencyTable.setStatus("current")
_RxBandwidthKHz_Type = Integer32
_RxBandwidthKHz_Object = MibScalar
rxBandwidthKHz = _RxBandwidthKHz_Object(
    (1, 3, 6, 1, 4, 1, 33555, 4, 2, 1, 21),
    _RxBandwidthKHz_Type()
)
rxBandwidthKHz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxBandwidthKHz.setStatus("current")
if mibBuilder.loadTexts:
    rxBandwidthKHz.setUnits("kHz")
_IfEth_ObjectIdentity = ObjectIdentity
ifEth = _IfEth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33555, 4, 2, 2)
)
_IfEthTable_Object = MibTable
ifEthTable = _IfEthTable_Object(
    (1, 3, 6, 1, 4, 1, 33555, 4, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ifEthTable.setStatus("current")
_IfEthEntry_Object = MibTableRow
ifEthEntry = _IfEthEntry_Object(
    (1, 3, 6, 1, 4, 1, 33555, 4, 2, 2, 1, 1)
)
ifEthEntry.setIndexNames(
    (0, "RAY3-MIB", "speed"),
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
    (1, 3, 6, 1, 4, 1, 33555, 4, 2, 2, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 33555, 4, 2, 2, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 33555, 4, 2, 2, 1, 1, 3),
    _Mdix_Type()
)
mdix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdix.setStatus("current")
_Autonego_Type = OptionSetting
_Autonego_Object = MibTableColumn
autonego = _Autonego_Object(
    (1, 3, 6, 1, 4, 1, 33555, 4, 2, 2, 1, 1, 4),
    _Autonego_Type()
)
autonego.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autonego.setStatus("current")


class _FlowControl_Type(Integer32):
    """Custom type flowControl based on Integer32"""
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
          ("off", 1),
          ("on", 2),
          ("auto", 3))
    )


_FlowControl_Type.__name__ = "Integer32"
_FlowControl_Object = MibTableColumn
flowControl = _FlowControl_Object(
    (1, 3, 6, 1, 4, 1, 33555, 4, 2, 2, 1, 1, 7),
    _FlowControl_Type()
)
flowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowControl.setStatus("current")
_Statistic_ObjectIdentity = ObjectIdentity
statistic = _Statistic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33555, 4, 3)
)
_Radio_ObjectIdentity = ObjectIdentity
radio = _Radio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33555, 4, 3, 2)
)


class _Rss_Type(Tenths):
    """Custom type rss based on Tenths"""
    subtypeSpec = Tenths.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 0),
    )


_Rss_Type.__name__ = "Tenths"
_Rss_Object = MibScalar
rss = _Rss_Object(
    (1, 3, 6, 1, 4, 1, 33555, 4, 3, 2, 1),
    _Rss_Type()
)
rss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rss.setStatus("current")
_TimeAllConnect_Type = TimeTicks
_TimeAllConnect_Object = MibScalar
timeAllConnect = _TimeAllConnect_Object(
    (1, 3, 6, 1, 4, 1, 33555, 4, 3, 2, 5),
    _TimeAllConnect_Type()
)
timeAllConnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeAllConnect.setStatus("current")
_TimeAllDisconnect_Type = TimeTicks
_TimeAllDisconnect_Object = MibScalar
timeAllDisconnect = _TimeAllDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 33555, 4, 3, 2, 6),
    _TimeAllDisconnect_Type()
)
timeAllDisconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeAllDisconnect.setStatus("current")
_TimeMaxDisconnect_Type = TimeTicks
_TimeMaxDisconnect_Object = MibScalar
timeMaxDisconnect = _TimeMaxDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 33555, 4, 3, 2, 7),
    _TimeMaxDisconnect_Type()
)
timeMaxDisconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeMaxDisconnect.setStatus("current")
_NumDisconnect_Type = Counter32
_NumDisconnect_Object = MibScalar
numDisconnect = _NumDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 33555, 4, 3, 2, 8),
    _NumDisconnect_Type()
)
numDisconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numDisconnect.setStatus("current")


class _Reliability_Type(Thousandths):
    """Custom type reliability based on Thousandths"""
    subtypeSpec = Thousandths.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_Reliability_Type.__name__ = "Thousandths"
_Reliability_Object = MibScalar
reliability = _Reliability_Object(
    (1, 3, 6, 1, 4, 1, 33555, 4, 3, 2, 9),
    _Reliability_Type()
)
reliability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reliability.setStatus("current")
_LinkUptime_Type = TimeTicks
_LinkUptime_Object = MibScalar
linkUptime = _LinkUptime_Object(
    (1, 3, 6, 1, 4, 1, 33555, 4, 3, 2, 10),
    _LinkUptime_Type()
)
linkUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkUptime.setStatus("current")
_Ber_Type = Integer32
_Ber_Object = MibScalar
ber = _Ber_Object(
    (1, 3, 6, 1, 4, 1, 33555, 4, 3, 2, 11),
    _Ber_Type()
)
ber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ber.setStatus("current")


class _Mse_Type(Tenths):
    """Custom type mse based on Tenths"""
    subtypeSpec = Tenths.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-500, 0),
    )


_Mse_Type.__name__ = "Tenths"
_Mse_Object = MibScalar
mse = _Mse_Object(
    (1, 3, 6, 1, 4, 1, 33555, 4, 3, 2, 12),
    _Mse_Type()
)
mse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mse.setStatus("current")
_Ethernet_ObjectIdentity = ObjectIdentity
ethernet = _Ethernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33555, 4, 3, 3)
)
_EthInThroughput_Type = Integer32
_EthInThroughput_Object = MibScalar
ethInThroughput = _EthInThroughput_Object(
    (1, 3, 6, 1, 4, 1, 33555, 4, 3, 3, 1),
    _EthInThroughput_Type()
)
ethInThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethInThroughput.setStatus("current")
if mibBuilder.loadTexts:
    ethInThroughput.setUnits("kbps")
_EthOutThroughput_Type = Integer32
_EthOutThroughput_Object = MibScalar
ethOutThroughput = _EthOutThroughput_Object(
    (1, 3, 6, 1, 4, 1, 33555, 4, 3, 3, 2),
    _EthOutThroughput_Type()
)
ethOutThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOutThroughput.setStatus("current")
if mibBuilder.loadTexts:
    ethOutThroughput.setUnits("kbps")
_Eth2InThroughput_Type = Integer32
_Eth2InThroughput_Object = MibScalar
eth2InThroughput = _Eth2InThroughput_Object(
    (1, 3, 6, 1, 4, 1, 33555, 4, 3, 3, 3),
    _Eth2InThroughput_Type()
)
eth2InThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth2InThroughput.setStatus("current")
if mibBuilder.loadTexts:
    eth2InThroughput.setUnits("kbps")
_Eth2OutThroughput_Type = Integer32
_Eth2OutThroughput_Object = MibScalar
eth2OutThroughput = _Eth2OutThroughput_Object(
    (1, 3, 6, 1, 4, 1, 33555, 4, 3, 3, 4),
    _Eth2OutThroughput_Type()
)
eth2OutThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth2OutThroughput.setStatus("current")
if mibBuilder.loadTexts:
    eth2OutThroughput.setUnits("kbps")
_Switch_ObjectIdentity = ObjectIdentity
switch = _Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33555, 4, 4)
)
_EgressQueue_ObjectIdentity = ObjectIdentity
egressQueue = _EgressQueue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33555, 4, 4, 3)
)
_SpeedGuard_Type = OptionSetting
_SpeedGuard_Object = MibScalar
speedGuard = _SpeedGuard_Object(
    (1, 3, 6, 1, 4, 1, 33555, 4, 4, 3, 2),
    _SpeedGuard_Type()
)
speedGuard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedGuard.setStatus("current")
_Ray3Traps_ObjectIdentity = ObjectIdentity
ray3Traps = _Ray3Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33555, 4, 12)
)
_Ray3TrapsPrefix_ObjectIdentity = ObjectIdentity
ray3TrapsPrefix = _Ray3TrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33555, 4, 12, 0)
)

# Managed Objects groups


# Notification objects

tr3TemperatureAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33555, 4, 12, 0, 1)
)
tr3TemperatureAlarm.setObjects(
      *(("RAY3-MIB", "temperatureModem"),
        ("RAY3-MIB", "alarmTemperature"))
)
if mibBuilder.loadTexts:
    tr3TemperatureAlarm.setStatus(
        "current"
    )

tr3VoltageLowAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33555, 4, 12, 0, 2)
)
tr3VoltageLowAlarm.setObjects(
      *(("RAY3-MIB", "voltageUnit"),
        ("RAY3-MIB", "alarmVoltageLow"))
)
if mibBuilder.loadTexts:
    tr3VoltageLowAlarm.setStatus(
        "current"
    )

tr3VoltageHighAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33555, 4, 12, 0, 3)
)
tr3VoltageHighAlarm.setObjects(
      *(("RAY3-MIB", "voltageUnit"),
        ("RAY3-MIB", "alarmVoltageHigh"))
)
if mibBuilder.loadTexts:
    tr3VoltageHighAlarm.setStatus(
        "current"
    )

tr3RssAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33555, 4, 12, 0, 4)
)
tr3RssAlarm.setObjects(
      *(("RAY3-MIB", "rss"),
        ("RAY3-MIB", "alarmRss"))
)
if mibBuilder.loadTexts:
    tr3RssAlarm.setStatus(
        "current"
    )

tr3MseAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33555, 4, 12, 0, 5)
)
tr3MseAlarm.setObjects(
      *(("RAY3-MIB", "mse"),
        ("RAY3-MIB", "alarmMse"))
)
if mibBuilder.loadTexts:
    tr3MseAlarm.setStatus(
        "current"
    )

tr3BerAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33555, 4, 12, 0, 6)
)
tr3BerAlarm.setObjects(
      *(("RAY3-MIB", "ber"),
        ("RAY3-MIB", "alarmBer"))
)
if mibBuilder.loadTexts:
    tr3BerAlarm.setStatus(
        "current"
    )

tr3AirDisconnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 33555, 4, 12, 0, 7)
)
tr3AirDisconnect.setObjects(
      *(("RAY3-MIB", "lineStatusII"),
        ("RAY3-MIB", "alarmPeerDisconnected"))
)
if mibBuilder.loadTexts:
    tr3AirDisconnect.setStatus(
        "current"
    )

tr3AirConnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 33555, 4, 12, 0, 8)
)
tr3AirConnect.setObjects(
      *(("RAY3-MIB", "lineStatusII"),
        ("RAY3-MIB", "alarmPeerDisconnected"))
)
if mibBuilder.loadTexts:
    tr3AirConnect.setStatus(
        "current"
    )

tr3Eth1LinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 33555, 4, 12, 0, 9)
)
tr3Eth1LinkDown.setObjects(
      *(("RAY3-MIB", "eth1Link"),
        ("RAY3-MIB", "alarmEth1Down"))
)
if mibBuilder.loadTexts:
    tr3Eth1LinkDown.setStatus(
        "current"
    )

tr3Eth21LinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 33555, 4, 12, 0, 10)
)
tr3Eth21LinkDown.setObjects(
      *(("RAY3-MIB", "eth2Link"),
        ("RAY3-MIB", "alarmEth2Down"))
)
if mibBuilder.loadTexts:
    tr3Eth21LinkDown.setStatus(
        "current"
    )

tr3NetBitrate = NotificationType(
    (1, 3, 6, 1, 4, 1, 33555, 4, 12, 0, 11)
)
tr3NetBitrate.setObjects(
      *(("RAY3-MIB", "netBitrate"),
        ("RAY3-MIB", "alarmNetBitrate"))
)
if mibBuilder.loadTexts:
    tr3NetBitrate.setStatus(
        "current"
    )

tr3WifiOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 33555, 4, 12, 0, 12)
)
tr3WifiOn.setObjects(
      *(("RAY3-MIB", "wifiHAP"),
        ("RAY3-MIB", "alarmWifiOn"))
)
if mibBuilder.loadTexts:
    tr3WifiOn.setStatus(
        "current"
    )

tr3EventAirCapacity = NotificationType(
    (1, 3, 6, 1, 4, 1, 33555, 4, 12, 0, 101)
)
tr3EventAirCapacity.setObjects(
    ("RAY3-MIB", "netBitrate")
)
if mibBuilder.loadTexts:
    tr3EventAirCapacity.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAY3-MIB",
    **{"Tenths": Tenths,
       "Hundredths": Hundredths,
       "Thousandths": Thousandths,
       "DisplayStringRaw": DisplayStringRaw,
       "PhysAddressRaw": PhysAddressRaw,
       "ServiceState": ServiceState,
       "AlarmState": AlarmState,
       "OptionSetting": OptionSetting,
       "ModulationList": ModulationList,
       "racom": racom,
       "ray3": ray3,
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
       "peerNumber": peerNumber,
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
       "alarm": alarm,
       "alarmTemperature": alarmTemperature,
       "alarmVoltageLow": alarmVoltageLow,
       "alarmVoltageHigh": alarmVoltageHigh,
       "alarmRss": alarmRss,
       "alarmBer": alarmBer,
       "alarmPeerDisconnected": alarmPeerDisconnected,
       "alarmEth1Down": alarmEth1Down,
       "alarmEth2Down": alarmEth2Down,
       "alarmNetBitrate": alarmNetBitrate,
       "alarmWifiOn": alarmWifiOn,
       "alarmMse": alarmMse,
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
       "matching": matching,
       "rfPowerConfigured": rfPowerConfigured,
       "netBitrate": netBitrate,
       "maxNetBitrate": maxNetBitrate,
       "txBandwidthKHz": txBandwidthKHz,
       "channelArrangement": channelArrangement,
       "rfPowerCurrent": rfPowerCurrent,
       "acm": acm,
       "atpc": atpc,
       "frequencyTable": frequencyTable,
       "rxBandwidthKHz": rxBandwidthKHz,
       "ifEth": ifEth,
       "ifEthTable": ifEthTable,
       "ifEthEntry": ifEthEntry,
       "speed": speed,
       "duplex": duplex,
       "mdix": mdix,
       "autonego": autonego,
       "flowControl": flowControl,
       "statistic": statistic,
       "radio": radio,
       "rss": rss,
       "timeAllConnect": timeAllConnect,
       "timeAllDisconnect": timeAllDisconnect,
       "timeMaxDisconnect": timeMaxDisconnect,
       "numDisconnect": numDisconnect,
       "reliability": reliability,
       "linkUptime": linkUptime,
       "ber": ber,
       "mse": mse,
       "ethernet": ethernet,
       "ethInThroughput": ethInThroughput,
       "ethOutThroughput": ethOutThroughput,
       "eth2InThroughput": eth2InThroughput,
       "eth2OutThroughput": eth2OutThroughput,
       "switch": switch,
       "egressQueue": egressQueue,
       "speedGuard": speedGuard,
       "ray3Traps": ray3Traps,
       "ray3TrapsPrefix": ray3TrapsPrefix,
       "tr3TemperatureAlarm": tr3TemperatureAlarm,
       "tr3VoltageLowAlarm": tr3VoltageLowAlarm,
       "tr3VoltageHighAlarm": tr3VoltageHighAlarm,
       "tr3RssAlarm": tr3RssAlarm,
       "tr3MseAlarm": tr3MseAlarm,
       "tr3BerAlarm": tr3BerAlarm,
       "tr3AirDisconnect": tr3AirDisconnect,
       "tr3AirConnect": tr3AirConnect,
       "tr3Eth1LinkDown": tr3Eth1LinkDown,
       "tr3Eth21LinkDown": tr3Eth21LinkDown,
       "tr3NetBitrate": tr3NetBitrate,
       "tr3WifiOn": tr3WifiOn,
       "tr3EventAirCapacity": tr3EventAirCapacity}
)
