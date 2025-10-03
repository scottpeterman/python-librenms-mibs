# SNMP MIB module (IBOOTPDU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dataprobe\IBOOTPDU-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:35:22 2025
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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

iBoot_PDU_Agent = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1418, 6)
)
if mibBuilder.loadTexts:
    iBoot_PDU_Agent.setRevisions(
        ("2017-10-25 13:23",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TC1(TextualConvention, Integer32):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_Dataprobe_ObjectIdentity = ObjectIdentity
dataprobe = _Dataprobe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1418)
)
_Device_ObjectIdentity = ObjectIdentity
device = _Device_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1418, 6, 1)
)
_FirmwareVersion_Type = DisplayString
_FirmwareVersion_Object = MibScalar
firmwareVersion = _FirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 1418, 6, 1, 1),
    _FirmwareVersion_Type()
)
firmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareVersion.setStatus("current")
_DeviceName_Type = DisplayString
_DeviceName_Object = MibScalar
deviceName = _DeviceName_Object(
    (1, 3, 6, 1, 4, 1, 1418, 6, 1, 2),
    _DeviceName_Type()
)
deviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceName.setStatus("current")
_DeviceFamily_Type = DisplayString
_DeviceFamily_Object = MibScalar
deviceFamily = _DeviceFamily_Object(
    (1, 3, 6, 1, 4, 1, 1418, 6, 1, 3),
    _DeviceFamily_Type()
)
deviceFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceFamily.setStatus("current")
_DeviceModelName_Type = DisplayString
_DeviceModelName_Object = MibScalar
deviceModelName = _DeviceModelName_Object(
    (1, 3, 6, 1, 4, 1, 1418, 6, 1, 4),
    _DeviceModelName_Type()
)
deviceModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceModelName.setStatus("current")


class _DeviceConnector_Type(Integer32):
    """Custom type deviceConnector based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nema", 0),
          ("iec", 1))
    )


_DeviceConnector_Type.__name__ = "Integer32"
_DeviceConnector_Object = MibScalar
deviceConnector = _DeviceConnector_Object(
    (1, 3, 6, 1, 4, 1, 1418, 6, 1, 5),
    _DeviceConnector_Type()
)
deviceConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceConnector.setStatus("current")
_DeviceNumberOfOutlets_Type = Integer32
_DeviceNumberOfOutlets_Object = MibScalar
deviceNumberOfOutlets = _DeviceNumberOfOutlets_Object(
    (1, 3, 6, 1, 4, 1, 1418, 6, 1, 6),
    _DeviceNumberOfOutlets_Type()
)
deviceNumberOfOutlets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceNumberOfOutlets.setStatus("current")


class _DeviceNumberOfLineCords_Type(Integer32):
    """Custom type deviceNumberOfLineCords based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("one", 0),
          ("two", 1))
    )


_DeviceNumberOfLineCords_Type.__name__ = "Integer32"
_DeviceNumberOfLineCords_Object = MibScalar
deviceNumberOfLineCords = _DeviceNumberOfLineCords_Object(
    (1, 3, 6, 1, 4, 1, 1418, 6, 1, 7),
    _DeviceNumberOfLineCords_Type()
)
deviceNumberOfLineCords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceNumberOfLineCords.setStatus("current")
_DeviceMaxCurrent_Type = Integer32
_DeviceMaxCurrent_Object = MibScalar
deviceMaxCurrent = _DeviceMaxCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1418, 6, 1, 8),
    _DeviceMaxCurrent_Type()
)
deviceMaxCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceMaxCurrent.setStatus("current")


class _DeviceTemperatureUnit_Type(Integer32):
    """Custom type deviceTemperatureUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fahrenheit", 0),
          ("celsius", 1))
    )


_DeviceTemperatureUnit_Type.__name__ = "Integer32"
_DeviceTemperatureUnit_Object = MibScalar
deviceTemperatureUnit = _DeviceTemperatureUnit_Object(
    (1, 3, 6, 1, 4, 1, 1418, 6, 1, 9),
    _DeviceTemperatureUnit_Type()
)
deviceTemperatureUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceTemperatureUnit.setStatus("current")
_DeviceTimeZone_Type = DisplayString
_DeviceTimeZone_Object = MibScalar
deviceTimeZone = _DeviceTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 1418, 6, 1, 10),
    _DeviceTimeZone_Type()
)
deviceTimeZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceTimeZone.setStatus("current")


class _DeviceCalibrated_Type(Integer32):
    """Custom type deviceCalibrated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_DeviceCalibrated_Type.__name__ = "Integer32"
_DeviceCalibrated_Object = MibScalar
deviceCalibrated = _DeviceCalibrated_Object(
    (1, 3, 6, 1, 4, 1, 1418, 6, 1, 11),
    _DeviceCalibrated_Type()
)
deviceCalibrated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceCalibrated.setStatus("current")
_ModemCountryCode_Type = Integer32
_ModemCountryCode_Object = MibScalar
modemCountryCode = _ModemCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 1418, 6, 1, 12),
    _ModemCountryCode_Type()
)
modemCountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCountryCode.setStatus("current")
_OutletDelayTime_Type = Integer32
_OutletDelayTime_Object = MibScalar
outletDelayTime = _OutletDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 1418, 6, 1, 13),
    _OutletDelayTime_Type()
)
outletDelayTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletDelayTime.setStatus("current")


class _CloudServiceEnabled_Type(Integer32):
    """Custom type cloudServiceEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_CloudServiceEnabled_Type.__name__ = "Integer32"
_CloudServiceEnabled_Object = MibScalar
cloudServiceEnabled = _CloudServiceEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1418, 6, 1, 14),
    _CloudServiceEnabled_Type()
)
cloudServiceEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cloudServiceEnabled.setStatus("current")


class _CloudServerAddress_Type(DisplayString):
    """Custom type cloudServerAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )
    fixed_length = 128


_CloudServerAddress_Type.__name__ = "DisplayString"
_CloudServerAddress_Object = MibScalar
cloudServerAddress = _CloudServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 1418, 6, 1, 15),
    _CloudServerAddress_Type()
)
cloudServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cloudServerAddress.setStatus("current")
_CloudActivationCode_Type = DisplayString
_CloudActivationCode_Object = MibScalar
cloudActivationCode = _CloudActivationCode_Object(
    (1, 3, 6, 1, 4, 1, 1418, 6, 1, 16),
    _CloudActivationCode_Type()
)
cloudActivationCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cloudActivationCode.setStatus("current")
_CloudUUID_Type = DisplayString
_CloudUUID_Object = MibScalar
cloudUUID = _CloudUUID_Object(
    (1, 3, 6, 1, 4, 1, 1418, 6, 1, 17),
    _CloudUUID_Type()
)
cloudUUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cloudUUID.setStatus("current")


class _SetFactoryDefaults_Type(Integer32):
    """Custom type setFactoryDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_SetFactoryDefaults_Type.__name__ = "Integer32"
_SetFactoryDefaults_Object = MibScalar
setFactoryDefaults = _SetFactoryDefaults_Object(
    (1, 3, 6, 1, 4, 1, 1418, 6, 1, 18),
    _SetFactoryDefaults_Type()
)
setFactoryDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setFactoryDefaults.setStatus("current")


class _RebootSystem_Type(Integer32):
    """Custom type rebootSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_RebootSystem_Type.__name__ = "Integer32"
_RebootSystem_Object = MibScalar
rebootSystem = _RebootSystem_Object(
    (1, 3, 6, 1, 4, 1, 1418, 6, 1, 19),
    _RebootSystem_Type()
)
rebootSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rebootSystem.setStatus("current")


class _RebootRequired_Type(Integer32):
    """Custom type rebootRequired based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_RebootRequired_Type.__name__ = "Integer32"
_RebootRequired_Object = MibScalar
rebootRequired = _RebootRequired_Object(
    (1, 3, 6, 1, 4, 1, 1418, 6, 1, 20),
    _RebootRequired_Type()
)
rebootRequired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rebootRequired.setStatus("current")
_Console_ObjectIdentity = ObjectIdentity
console = _Console_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1418, 6, 2)
)


class _SerialPortEnabled_Type(Integer32):
    """Custom type serialPortEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_SerialPortEnabled_Type.__name__ = "Integer32"
_SerialPortEnabled_Object = MibScalar
serialPortEnabled = _SerialPortEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1418, 6, 2, 1),
    _SerialPortEnabled_Type()
)
serialPortEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialPortEnabled.setStatus("current")


class _ConsoleTimeout_Type(Integer32):
    """Custom type consoleTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_ConsoleTimeout_Type.__name__ = "Integer32"
_ConsoleTimeout_Object = MibScalar
consoleTimeout = _ConsoleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1418, 6, 2, 2),
    _ConsoleTimeout_Type()
)
consoleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consoleTimeout.setStatus("current")


class _TelnetEnabled_Type(Integer32):
    """Custom type telnetEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_TelnetEnabled_Type.__name__ = "Integer32"
_TelnetEnabled_Object = MibScalar
telnetEnabled = _TelnetEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1418, 6, 2, 3),
    _TelnetEnabled_Type()
)
telnetEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetEnabled.setStatus("current")


class _TelnetPort_Type(Integer32):
    """Custom type telnetPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TelnetPort_Type.__name__ = "Integer32"
_TelnetPort_Object = MibScalar
telnetPort = _TelnetPort_Object(
    (1, 3, 6, 1, 4, 1, 1418, 6, 2, 4),
    _TelnetPort_Type()
)
telnetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetPort.setStatus("current")


class _SshEnabled_Type(Integer32):
    """Custom type sshEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_SshEnabled_Type.__name__ = "Integer32"
_SshEnabled_Object = MibScalar
sshEnabled = _SshEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1418, 6, 2, 5),
    _SshEnabled_Type()
)
sshEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshEnabled.setStatus("current")


class _SshPort_Type(Integer32):
    """Custom type sshPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SshPort_Type.__name__ = "Integer32"
_SshPort_Object = MibScalar
sshPort = _SshPort_Object(
    (1, 3, 6, 1, 4, 1, 1418, 6, 2, 6),
    _SshPort_Type()
)
sshPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshPort.setStatus("current")
_Network_ObjectIdentity = ObjectIdentity
network = _Network_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1418, 6, 3)
)
_MacAddress_Type = MacAddress
_MacAddress_Object = MibScalar
macAddress = _MacAddress_Object(
    (1, 3, 6, 1, 4, 1, 1418, 6, 3, 1),
    _MacAddress_Type()
)
macAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macAddress.setStatus("current")


class _IpMode_Type(Integer32):
    """Custom type ipMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("static", 0),
          ("dhcp", 1))
    )


_IpMode_Type.__name__ = "Integer32"
_IpMode_Object = MibScalar
ipMode = _IpMode_Object(
    (1, 3, 6, 1, 4, 1, 1418, 6, 3, 2),
    _IpMode_Type()
)
ipMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipMode.setStatus("current")
_IpAddress_Type = IpAddress
_IpAddress_Object = MibScalar
ipAddress = _IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1418, 6, 3, 3),
    _IpAddress_Type()
)
ipAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAddress.setStatus("current")
_SubnetMask_Type = IpAddress
_SubnetMask_Object = MibScalar
subnetMask = _SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 1418, 6, 3, 4),
    _SubnetMask_Type()
)
subnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subnetMask.setStatus("current")
_Gateway_Type = IpAddress
_Gateway_Object = MibScalar
gateway = _Gateway_Object(
    (1, 3, 6, 1, 4, 1, 1418, 6, 3, 5),
    _Gateway_Type()
)
gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gateway.setStatus("current")
_DnsServer1_Type = IpAddress
_DnsServer1_Object = MibScalar
dnsServer1 = _DnsServer1_Object(
    (1, 3, 6, 1, 4, 1, 1418, 6, 3, 6),
    _DnsServer1_Type()
)
dnsServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsServer1.setStatus("current")
_DnsServer2_Type = IpAddress
_DnsServer2_Object = MibScalar
dnsServer2 = _DnsServer2_Object(
    (1, 3, 6, 1, 4, 1, 1418, 6, 3, 7),
    _DnsServer2_Type()
)
dnsServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsServer2.setStatus("current")


class _SslEnabled_Type(Integer32):
    """Custom type sslEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_SslEnabled_Type.__name__ = "Integer32"
_SslEnabled_Object = MibScalar
sslEnabled = _SslEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1418, 6, 3, 8),
    _SslEnabled_Type()
)
sslEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslEnabled.setStatus("current")


class _SslPort_Type(Integer32):
    """Custom type sslPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SslPort_Type.__name__ = "Integer32"
_SslPort_Object = MibScalar
sslPort = _SslPort_Object(
    (1, 3, 6, 1, 4, 1, 1418, 6, 3, 9),
    _SslPort_Type()
)
sslPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslPort.setStatus("current")


class _WebEnabled_Type(Integer32):
    """Custom type webEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_WebEnabled_Type.__name__ = "Integer32"
_WebEnabled_Object = MibScalar
webEnabled = _WebEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1418, 6, 3, 10),
    _WebEnabled_Type()
)
webEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webEnabled.setStatus("current")


class _WebPort_Type(Integer32):
    """Custom type webPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WebPort_Type.__name__ = "Integer32"
_WebPort_Object = MibScalar
webPort = _WebPort_Object(
    (1, 3, 6, 1, 4, 1, 1418, 6, 3, 11),
    _WebPort_Type()
)
webPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webPort.setStatus("current")
_Snmp_ObjectIdentity = ObjectIdentity
snmp = _Snmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1418, 6, 4)
)


class _SnmpEnabled_Type(Integer32):
    """Custom type snmpEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_SnmpEnabled_Type.__name__ = "Integer32"
_SnmpEnabled_Object = MibScalar
snmpEnabled = _SnmpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1418, 6, 4, 1),
    _SnmpEnabled_Type()
)
snmpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpEnabled.setStatus("current")
_SnmpReadCommunity_Type = DisplayString
_SnmpReadCommunity_Object = MibScalar
snmpReadCommunity = _SnmpReadCommunity_Object(
    (1, 3, 6, 1, 4, 1, 1418, 6, 4, 2),
    _SnmpReadCommunity_Type()
)
snmpReadCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpReadCommunity.setStatus("current")
_SnmpWriteCommunity_Type = DisplayString
_SnmpWriteCommunity_Object = MibScalar
snmpWriteCommunity = _SnmpWriteCommunity_Object(
    (1, 3, 6, 1, 4, 1, 1418, 6, 4, 3),
    _SnmpWriteCommunity_Type()
)
snmpWriteCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpWriteCommunity.setStatus("current")
_SnmpManagerTable_Object = MibTable
snmpManagerTable = _SnmpManagerTable_Object(
    (1, 3, 6, 1, 4, 1, 1418, 6, 4, 4)
)
if mibBuilder.loadTexts:
    snmpManagerTable.setStatus("current")
_SnmpManagerEntry_Object = MibTableRow
snmpManagerEntry = _SnmpManagerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1418, 6, 4, 4, 1)
)
snmpManagerEntry.setIndexNames(
    (0, "IBOOTPDU-MIB", "snmpManagerIndex"),
)
if mibBuilder.loadTexts:
    snmpManagerEntry.setStatus("current")


class _SnmpManagerIndex_Type(Integer32):
    """Custom type snmpManagerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SnmpManagerIndex_Type.__name__ = "Integer32"
_SnmpManagerIndex_Object = MibTableColumn
snmpManagerIndex = _SnmpManagerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1418, 6, 4, 4, 1, 1),
    _SnmpManagerIndex_Type()
)
snmpManagerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpManagerIndex.setStatus("current")


class _SnmpManagerAddress_Type(DisplayString):
    """Custom type snmpManagerAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_SnmpManagerAddress_Type.__name__ = "DisplayString"
_SnmpManagerAddress_Object = MibTableColumn
snmpManagerAddress = _SnmpManagerAddress_Object(
    (1, 3, 6, 1, 4, 1, 1418, 6, 4, 4, 1, 2),
    _SnmpManagerAddress_Type()
)
snmpManagerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpManagerAddress.setStatus("current")
_SnmpManagerName_Type = DisplayString
_SnmpManagerName_Object = MibTableColumn
snmpManagerName = _SnmpManagerName_Object(
    (1, 3, 6, 1, 4, 1, 1418, 6, 4, 4, 1, 3),
    _SnmpManagerName_Type()
)
snmpManagerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpManagerName.setStatus("current")
_SnmpTrapCommunity_Type = DisplayString
_SnmpTrapCommunity_Object = MibTableColumn
snmpTrapCommunity = _SnmpTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 1418, 6, 4, 4, 1, 4),
    _SnmpTrapCommunity_Type()
)
snmpTrapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapCommunity.setStatus("current")
_OutletTable_Object = MibTable
outletTable = _OutletTable_Object(
    (1, 3, 6, 1, 4, 1, 1418, 6, 5)
)
if mibBuilder.loadTexts:
    outletTable.setStatus("current")
_OutletEntry_Object = MibTableRow
outletEntry = _OutletEntry_Object(
    (1, 3, 6, 1, 4, 1, 1418, 6, 5, 1)
)
outletEntry.setIndexNames(
    (0, "IBOOTPDU-MIB", "outletIndex"),
)
if mibBuilder.loadTexts:
    outletEntry.setStatus("current")


class _OutletIndex_Type(Integer32):
    """Custom type outletIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_OutletIndex_Type.__name__ = "Integer32"
_OutletIndex_Object = MibTableColumn
outletIndex = _OutletIndex_Object(
    (1, 3, 6, 1, 4, 1, 1418, 6, 5, 1, 1),
    _OutletIndex_Type()
)
outletIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletIndex.setStatus("current")
_OutletName_Type = DisplayString
_OutletName_Object = MibTableColumn
outletName = _OutletName_Object(
    (1, 3, 6, 1, 4, 1, 1418, 6, 5, 1, 2),
    _OutletName_Type()
)
outletName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletName.setStatus("current")


class _OutletInitialState_Type(Integer32):
    """Custom type outletInitialState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1),
          ("last", 2))
    )


_OutletInitialState_Type.__name__ = "Integer32"
_OutletInitialState_Object = MibTableColumn
outletInitialState = _OutletInitialState_Object(
    (1, 3, 6, 1, 4, 1, 1418, 6, 5, 1, 3),
    _OutletInitialState_Type()
)
outletInitialState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletInitialState.setStatus("current")
_OutletCycleTime_Type = Integer32
_OutletCycleTime_Object = MibTableColumn
outletCycleTime = _OutletCycleTime_Object(
    (1, 3, 6, 1, 4, 1, 1418, 6, 5, 1, 4),
    _OutletCycleTime_Type()
)
outletCycleTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCycleTime.setStatus("current")


class _OutletControl_Type(Integer32):
    """Custom type outletControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1),
          ("cycle", 2))
    )


_OutletControl_Type.__name__ = "Integer32"
_OutletControl_Object = MibTableColumn
outletControl = _OutletControl_Object(
    (1, 3, 6, 1, 4, 1, 1418, 6, 5, 1, 5),
    _OutletControl_Type()
)
outletControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletControl.setStatus("current")


class _OutletStatus_Type(Integer32):
    """Custom type outletStatus based on Integer32"""
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
        *(("off", 0),
          ("on", 1),
          ("cycle", 2),
          ("reboot", 3),
          ("pend-on", 4))
    )


_OutletStatus_Type.__name__ = "Integer32"
_OutletStatus_Object = MibTableColumn
outletStatus = _OutletStatus_Object(
    (1, 3, 6, 1, 4, 1, 1418, 6, 5, 1, 6),
    _OutletStatus_Type()
)
outletStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletStatus.setStatus("current")


class _OutletActualStatus_Type(Integer32):
    """Custom type outletActualStatus based on Integer32"""
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


_OutletActualStatus_Type.__name__ = "Integer32"
_OutletActualStatus_Object = MibTableColumn
outletActualStatus = _OutletActualStatus_Object(
    (1, 3, 6, 1, 4, 1, 1418, 6, 5, 1, 7),
    _OutletActualStatus_Type()
)
outletActualStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletActualStatus.setStatus("current")
_Sensors_ObjectIdentity = ObjectIdentity
sensors = _Sensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1418, 6, 6)
)
_VoltageLC1_Type = Integer32
_VoltageLC1_Object = MibScalar
voltageLC1 = _VoltageLC1_Object(
    (1, 3, 6, 1, 4, 1, 1418, 6, 6, 1),
    _VoltageLC1_Type()
)
voltageLC1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageLC1.setStatus("current")
_CurrentLC1_Type = Integer32
_CurrentLC1_Object = MibScalar
currentLC1 = _CurrentLC1_Object(
    (1, 3, 6, 1, 4, 1, 1418, 6, 6, 2),
    _CurrentLC1_Type()
)
currentLC1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentLC1.setStatus("current")
_VoltageLC2_Type = Integer32
_VoltageLC2_Object = MibScalar
voltageLC2 = _VoltageLC2_Object(
    (1, 3, 6, 1, 4, 1, 1418, 6, 6, 3),
    _VoltageLC2_Type()
)
voltageLC2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageLC2.setStatus("current")
_CurrentLC2_Type = Integer32
_CurrentLC2_Object = MibScalar
currentLC2 = _CurrentLC2_Object(
    (1, 3, 6, 1, 4, 1, 1418, 6, 6, 4),
    _CurrentLC2_Type()
)
currentLC2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentLC2.setStatus("current")
_Temperature1_Type = Integer32
_Temperature1_Object = MibScalar
temperature1 = _Temperature1_Object(
    (1, 3, 6, 1, 4, 1, 1418, 6, 6, 5),
    _Temperature1_Type()
)
temperature1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature1.setStatus("current")
_Temperature2_Type = Integer32
_Temperature2_Object = MibScalar
temperature2 = _Temperature2_Object(
    (1, 3, 6, 1, 4, 1, 1418, 6, 6, 6),
    _Temperature2_Type()
)
temperature2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature2.setStatus("current")
_Notifications_ObjectIdentity = ObjectIdentity
notifications = _Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1418, 6, 7)
)

# Managed Objects groups


# Notification objects

outletChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1418, 6, 7, 1)
)
outletChange.setObjects(
      *(("IBOOTPDU-MIB", "outletIndex"),
        ("IBOOTPDU-MIB", "outletName"),
        ("IBOOTPDU-MIB", "outletStatus"))
)
if mibBuilder.loadTexts:
    outletChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IBOOTPDU-MIB",
    **{"TC1": TC1,
       "dataprobe": dataprobe,
       "iBoot-PDU-Agent": iBoot_PDU_Agent,
       "device": device,
       "firmwareVersion": firmwareVersion,
       "deviceName": deviceName,
       "deviceFamily": deviceFamily,
       "deviceModelName": deviceModelName,
       "deviceConnector": deviceConnector,
       "deviceNumberOfOutlets": deviceNumberOfOutlets,
       "deviceNumberOfLineCords": deviceNumberOfLineCords,
       "deviceMaxCurrent": deviceMaxCurrent,
       "deviceTemperatureUnit": deviceTemperatureUnit,
       "deviceTimeZone": deviceTimeZone,
       "deviceCalibrated": deviceCalibrated,
       "modemCountryCode": modemCountryCode,
       "outletDelayTime": outletDelayTime,
       "cloudServiceEnabled": cloudServiceEnabled,
       "cloudServerAddress": cloudServerAddress,
       "cloudActivationCode": cloudActivationCode,
       "cloudUUID": cloudUUID,
       "setFactoryDefaults": setFactoryDefaults,
       "rebootSystem": rebootSystem,
       "rebootRequired": rebootRequired,
       "console": console,
       "serialPortEnabled": serialPortEnabled,
       "consoleTimeout": consoleTimeout,
       "telnetEnabled": telnetEnabled,
       "telnetPort": telnetPort,
       "sshEnabled": sshEnabled,
       "sshPort": sshPort,
       "network": network,
       "macAddress": macAddress,
       "ipMode": ipMode,
       "ipAddress": ipAddress,
       "subnetMask": subnetMask,
       "gateway": gateway,
       "dnsServer1": dnsServer1,
       "dnsServer2": dnsServer2,
       "sslEnabled": sslEnabled,
       "sslPort": sslPort,
       "webEnabled": webEnabled,
       "webPort": webPort,
       "snmp": snmp,
       "snmpEnabled": snmpEnabled,
       "snmpReadCommunity": snmpReadCommunity,
       "snmpWriteCommunity": snmpWriteCommunity,
       "snmpManagerTable": snmpManagerTable,
       "snmpManagerEntry": snmpManagerEntry,
       "snmpManagerIndex": snmpManagerIndex,
       "snmpManagerAddress": snmpManagerAddress,
       "snmpManagerName": snmpManagerName,
       "snmpTrapCommunity": snmpTrapCommunity,
       "outletTable": outletTable,
       "outletEntry": outletEntry,
       "outletIndex": outletIndex,
       "outletName": outletName,
       "outletInitialState": outletInitialState,
       "outletCycleTime": outletCycleTime,
       "outletControl": outletControl,
       "outletStatus": outletStatus,
       "outletActualStatus": outletActualStatus,
       "sensors": sensors,
       "voltageLC1": voltageLC1,
       "currentLC1": currentLC1,
       "voltageLC2": voltageLC2,
       "currentLC2": currentLC2,
       "temperature1": temperature1,
       "temperature2": temperature2,
       "notifications": notifications,
       "outletChange": outletChange}
)
