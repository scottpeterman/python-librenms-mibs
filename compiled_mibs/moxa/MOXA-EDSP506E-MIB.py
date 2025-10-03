# SNMP MIB module (MOXA-EDSP506E-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\moxa\MOXA-EDSP506E-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:11:02 2025
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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

edsp506e = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162)
)
if mibBuilder.loadTexts:
    edsp506e.setRevisions(
        ("2017-04-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PortList(TextualConvention, OctetString):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_Moxa_ObjectIdentity = ObjectIdentity
moxa = _Moxa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691)
)
_IndustrialEthernet_ObjectIdentity = ObjectIdentity
industrialEthernet = _IndustrialEthernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7)
)
_MibNotificationsPrefix_ObjectIdentity = ObjectIdentity
mibNotificationsPrefix = _MibNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 0)
)
_SwMgmt_ObjectIdentity = ObjectIdentity
swMgmt = _SwMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1)
)
_NumberOfPorts_Type = Integer32
_NumberOfPorts_Object = MibScalar
numberOfPorts = _NumberOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 1),
    _NumberOfPorts_Type()
)
numberOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfPorts.setStatus("current")
_SwitchModel_Type = DisplayString
_SwitchModel_Object = MibScalar
switchModel = _SwitchModel_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 2),
    _SwitchModel_Type()
)
switchModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchModel.setStatus("current")
_FirmwareVersion_Type = DisplayString
_FirmwareVersion_Object = MibScalar
firmwareVersion = _FirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 4),
    _FirmwareVersion_Type()
)
firmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareVersion.setStatus("current")


class _EnableWebConfig_Type(Integer32):
    """Custom type enableWebConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("httpOrHttps", 1),
          ("httpsOnly", 2))
    )


_EnableWebConfig_Type.__name__ = "Integer32"
_EnableWebConfig_Object = MibScalar
enableWebConfig = _EnableWebConfig_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 5),
    _EnableWebConfig_Type()
)
enableWebConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableWebConfig.setStatus("current")


class _EnableTelnetConsole_Type(Integer32):
    """Custom type enableTelnetConsole based on Integer32"""
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


_EnableTelnetConsole_Type.__name__ = "Integer32"
_EnableTelnetConsole_Object = MibScalar
enableTelnetConsole = _EnableTelnetConsole_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 6),
    _EnableTelnetConsole_Type()
)
enableTelnetConsole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableTelnetConsole.setStatus("current")


class _LineSwapRecovery_Type(Integer32):
    """Custom type lineSwapRecovery based on Integer32"""
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


_LineSwapRecovery_Type.__name__ = "Integer32"
_LineSwapRecovery_Object = MibScalar
lineSwapRecovery = _LineSwapRecovery_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 7),
    _LineSwapRecovery_Type()
)
lineSwapRecovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineSwapRecovery.setStatus("current")
_NetworkSetting_ObjectIdentity = ObjectIdentity
networkSetting = _NetworkSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 8)
)
_SwitchIpAddr_Type = IpAddress
_SwitchIpAddr_Object = MibScalar
switchIpAddr = _SwitchIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 8, 1),
    _SwitchIpAddr_Type()
)
switchIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIpAddr.setStatus("current")
_SwitchIpMask_Type = IpAddress
_SwitchIpMask_Object = MibScalar
switchIpMask = _SwitchIpMask_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 8, 2),
    _SwitchIpMask_Type()
)
switchIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIpMask.setStatus("current")
_DefaultGateway_Type = IpAddress
_DefaultGateway_Object = MibScalar
defaultGateway = _DefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 8, 3),
    _DefaultGateway_Type()
)
defaultGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defaultGateway.setStatus("current")


class _EnableAutoIpConfig_Type(Integer32):
    """Custom type enableAutoIpConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enableDHCP", 1),
          ("enableBOOTP", 2))
    )


_EnableAutoIpConfig_Type.__name__ = "Integer32"
_EnableAutoIpConfig_Object = MibScalar
enableAutoIpConfig = _EnableAutoIpConfig_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 8, 4),
    _EnableAutoIpConfig_Type()
)
enableAutoIpConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableAutoIpConfig.setStatus("current")
_DnsServer1IpAddr_Type = IpAddress
_DnsServer1IpAddr_Object = MibScalar
dnsServer1IpAddr = _DnsServer1IpAddr_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 8, 5),
    _DnsServer1IpAddr_Type()
)
dnsServer1IpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsServer1IpAddr.setStatus("current")
_SnmpTrapCommunity_Type = DisplayString
_SnmpTrapCommunity_Object = MibScalar
snmpTrapCommunity = _SnmpTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 8, 6),
    _SnmpTrapCommunity_Type()
)
snmpTrapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapCommunity.setStatus("current")
_TrapServerAddr_Type = DisplayString
_TrapServerAddr_Object = MibScalar
trapServerAddr = _TrapServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 8, 7),
    _TrapServerAddr_Type()
)
trapServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapServerAddr.setStatus("current")
_DnsServer2IpAddr_Type = IpAddress
_DnsServer2IpAddr_Object = MibScalar
dnsServer2IpAddr = _DnsServer2IpAddr_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 8, 8),
    _DnsServer2IpAddr_Type()
)
dnsServer2IpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsServer2IpAddr.setStatus("current")
_SnmpReadCommunity_Type = DisplayString
_SnmpReadCommunity_Object = MibScalar
snmpReadCommunity = _SnmpReadCommunity_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 8, 9),
    _SnmpReadCommunity_Type()
)
snmpReadCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpReadCommunity.setStatus("current")
_SnmpTrap2Community_Type = DisplayString
_SnmpTrap2Community_Object = MibScalar
snmpTrap2Community = _SnmpTrap2Community_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 8, 11),
    _SnmpTrap2Community_Type()
)
snmpTrap2Community.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrap2Community.setStatus("current")
_Trap2ServerAddr_Type = DisplayString
_Trap2ServerAddr_Object = MibScalar
trap2ServerAddr = _Trap2ServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 8, 12),
    _Trap2ServerAddr_Type()
)
trap2ServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trap2ServerAddr.setStatus("current")


class _SnmpInformEnable_Type(Integer32):
    """Custom type snmpInformEnable based on Integer32"""
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


_SnmpInformEnable_Type.__name__ = "Integer32"
_SnmpInformEnable_Object = MibScalar
snmpInformEnable = _SnmpInformEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 8, 13),
    _SnmpInformEnable_Type()
)
snmpInformEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpInformEnable.setStatus("current")


class _SnmpInformRetries_Type(Integer32):
    """Custom type snmpInformRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_SnmpInformRetries_Type.__name__ = "Integer32"
_SnmpInformRetries_Object = MibScalar
snmpInformRetries = _SnmpInformRetries_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 8, 14),
    _SnmpInformRetries_Type()
)
snmpInformRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpInformRetries.setStatus("current")


class _SnmpInformTimeout_Type(Integer32):
    """Custom type snmpInformTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_SnmpInformTimeout_Type.__name__ = "Integer32"
_SnmpInformTimeout_Object = MibScalar
snmpInformTimeout = _SnmpInformTimeout_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 8, 15),
    _SnmpInformTimeout_Type()
)
snmpInformTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpInformTimeout.setStatus("current")
_DhcpRetryPeriods_Type = Integer32
_DhcpRetryPeriods_Object = MibScalar
dhcpRetryPeriods = _DhcpRetryPeriods_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 8, 16),
    _DhcpRetryPeriods_Type()
)
dhcpRetryPeriods.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRetryPeriods.setStatus("current")
_DhcpRetryTimes_Type = Integer32
_DhcpRetryTimes_Object = MibScalar
dhcpRetryTimes = _DhcpRetryTimes_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 8, 17),
    _DhcpRetryTimes_Type()
)
dhcpRetryTimes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRetryTimes.setStatus("current")


class _TrapVersion_Type(Integer32):
    """Custom type trapVersion based on Integer32"""
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
        *(("snmpv1-Trap", 0),
          ("snmpv2-Notification", 1),
          ("snmpv2-Inform", 2),
          ("snmpv3-Trap", 3),
          ("snmpv3-Inform", 4))
    )


_TrapVersion_Type.__name__ = "Integer32"
_TrapVersion_Object = MibScalar
trapVersion = _TrapVersion_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 8, 18),
    _TrapVersion_Type()
)
trapVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapVersion.setStatus("current")


class _SnmpVersion_Type(Integer32):
    """Custom type snmpVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("snmpv1-v2c-v3", 1),
          ("snmpv1-v2c", 2),
          ("snmpv3", 3))
    )


_SnmpVersion_Type.__name__ = "Integer32"
_SnmpVersion_Object = MibScalar
snmpVersion = _SnmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 8, 21),
    _SnmpVersion_Type()
)
snmpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpVersion.setStatus("current")


class _SnmpAdminSecurityLevel_Type(Integer32):
    """Custom type snmpAdminSecurityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAuthNoPriv", 1),
          ("authNoPriv", 2),
          ("authPriv", 3))
    )


_SnmpAdminSecurityLevel_Type.__name__ = "Integer32"
_SnmpAdminSecurityLevel_Object = MibScalar
snmpAdminSecurityLevel = _SnmpAdminSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 8, 22),
    _SnmpAdminSecurityLevel_Type()
)
snmpAdminSecurityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAdminSecurityLevel.setStatus("current")


class _SnmpUserSecurityLevel_Type(Integer32):
    """Custom type snmpUserSecurityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAuthNoPriv", 1),
          ("authNoPriv", 2),
          ("authPriv", 3))
    )


_SnmpUserSecurityLevel_Type.__name__ = "Integer32"
_SnmpUserSecurityLevel_Object = MibScalar
snmpUserSecurityLevel = _SnmpUserSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 8, 23),
    _SnmpUserSecurityLevel_Type()
)
snmpUserSecurityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpUserSecurityLevel.setStatus("current")
_PortSetting_ObjectIdentity = ObjectIdentity
portSetting = _PortSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 9)
)
_PortTable_Object = MibTable
portTable = _PortTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 9, 1)
)
if mibBuilder.loadTexts:
    portTable.setStatus("current")
_PortEntry_Object = MibTableRow
portEntry = _PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 9, 1, 1)
)
portEntry.setIndexNames(
    (0, "MOXA-EDSP506E-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    portEntry.setStatus("current")
_PortIndex_Type = Integer32
_PortIndex_Object = MibTableColumn
portIndex = _PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 9, 1, 1, 1),
    _PortIndex_Type()
)
portIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portIndex.setStatus("current")
_PortDesc_Type = DisplayString
_PortDesc_Object = MibTableColumn
portDesc = _PortDesc_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 9, 1, 1, 2),
    _PortDesc_Type()
)
portDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDesc.setStatus("current")


class _PortEnable_Type(Integer32):
    """Custom type portEnable based on Integer32"""
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


_PortEnable_Type.__name__ = "Integer32"
_PortEnable_Object = MibTableColumn
portEnable = _PortEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 9, 1, 1, 3),
    _PortEnable_Type()
)
portEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portEnable.setStatus("current")


class _PortSpeed_Type(Integer32):
    """Custom type portSpeed based on Integer32"""
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
        *(("auto", 0),
          ("speed100M-Full", 1),
          ("speed100M-Half", 2),
          ("speed10M-Full", 3),
          ("speed10M-Half", 4),
          ("speed1000M-Full", 5))
    )


_PortSpeed_Type.__name__ = "Integer32"
_PortSpeed_Object = MibTableColumn
portSpeed = _PortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 9, 1, 1, 4),
    _PortSpeed_Type()
)
portSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSpeed.setStatus("current")


class _PortMDI_Type(Integer32):
    """Custom type portMDI based on Integer32"""
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
          ("auto", 1),
          ("mdi", 2),
          ("mdiX", 3))
    )


_PortMDI_Type.__name__ = "Integer32"
_PortMDI_Object = MibTableColumn
portMDI = _PortMDI_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 9, 1, 1, 5),
    _PortMDI_Type()
)
portMDI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portMDI.setStatus("current")


class _PortFDXFlowCtrl_Type(Integer32):
    """Custom type portFDXFlowCtrl based on Integer32"""
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


_PortFDXFlowCtrl_Type.__name__ = "Integer32"
_PortFDXFlowCtrl_Object = MibTableColumn
portFDXFlowCtrl = _PortFDXFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 9, 1, 1, 6),
    _PortFDXFlowCtrl_Type()
)
portFDXFlowCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portFDXFlowCtrl.setStatus("current")
_PortName_Type = DisplayString
_PortName_Object = MibTableColumn
portName = _PortName_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 9, 1, 1, 7),
    _PortName_Type()
)
portName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portName.setStatus("current")
_PortSubdesc_Type = DisplayString
_PortSubdesc_Object = MibTableColumn
portSubdesc = _PortSubdesc_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 9, 1, 1, 8),
    _PortSubdesc_Type()
)
portSubdesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSubdesc.setStatus("current")
_Monitor_ObjectIdentity = ObjectIdentity
monitor = _Monitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 10)
)


class _Power1InputStatus_Type(Integer32):
    """Custom type power1InputStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-present", 0),
          ("present", 1))
    )


_Power1InputStatus_Type.__name__ = "Integer32"
_Power1InputStatus_Object = MibScalar
power1InputStatus = _Power1InputStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 10, 1),
    _Power1InputStatus_Type()
)
power1InputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    power1InputStatus.setStatus("current")


class _Power2InputStatus_Type(Integer32):
    """Custom type power2InputStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-present", 0),
          ("present", 1))
    )


_Power2InputStatus_Type.__name__ = "Integer32"
_Power2InputStatus_Object = MibScalar
power2InputStatus = _Power2InputStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 10, 2),
    _Power2InputStatus_Type()
)
power2InputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    power2InputStatus.setStatus("current")
_MonitorPortTable_Object = MibTable
monitorPortTable = _MonitorPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 10, 3)
)
if mibBuilder.loadTexts:
    monitorPortTable.setStatus("current")
_MonitorPortEntry_Object = MibTableRow
monitorPortEntry = _MonitorPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 10, 3, 1)
)
monitorPortEntry.setIndexNames(
    (0, "MOXA-EDSP506E-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    monitorPortEntry.setStatus("current")


class _MonitorLinkStatus_Type(Integer32):
    """Custom type monitorLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", -1),
          ("off", 0),
          ("on", 1))
    )


_MonitorLinkStatus_Type.__name__ = "Integer32"
_MonitorLinkStatus_Object = MibTableColumn
monitorLinkStatus = _MonitorLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 10, 3, 1, 2),
    _MonitorLinkStatus_Type()
)
monitorLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorLinkStatus.setStatus("current")


class _MonitorSpeed_Type(Integer32):
    """Custom type monitorSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("na", -1),
          ("speed10M-Half", 0),
          ("speed10M-Full", 1),
          ("speed100M-Half", 2),
          ("speed100M-Full", 3),
          ("speed1000M-Half", 4),
          ("speed1000M-Full", 5))
    )


_MonitorSpeed_Type.__name__ = "Integer32"
_MonitorSpeed_Object = MibTableColumn
monitorSpeed = _MonitorSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 10, 3, 1, 3),
    _MonitorSpeed_Type()
)
monitorSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorSpeed.setStatus("current")


class _MonitorAutoMDI_Type(Integer32):
    """Custom type monitorAutoMDI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("na", -1),
          ("mdi", 0),
          ("mdix", 1),
          ("auto", 2))
    )


_MonitorAutoMDI_Type.__name__ = "Integer32"
_MonitorAutoMDI_Object = MibTableColumn
monitorAutoMDI = _MonitorAutoMDI_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 10, 3, 1, 4),
    _MonitorAutoMDI_Type()
)
monitorAutoMDI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorAutoMDI.setStatus("current")
_MonitorTraffic_Type = Integer32
_MonitorTraffic_Object = MibTableColumn
monitorTraffic = _MonitorTraffic_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 10, 3, 1, 5),
    _MonitorTraffic_Type()
)
monitorTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorTraffic.setStatus("current")


class _MonitorFDXFlowCtrl_Type(Integer32):
    """Custom type monitorFDXFlowCtrl based on Integer32"""
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


_MonitorFDXFlowCtrl_Type.__name__ = "Integer32"
_MonitorFDXFlowCtrl_Object = MibTableColumn
monitorFDXFlowCtrl = _MonitorFDXFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 10, 3, 1, 6),
    _MonitorFDXFlowCtrl_Type()
)
monitorFDXFlowCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorFDXFlowCtrl.setStatus("current")
_MonitorTxTraffic_Type = Integer32
_MonitorTxTraffic_Object = MibTableColumn
monitorTxTraffic = _MonitorTxTraffic_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 10, 3, 1, 7),
    _MonitorTxTraffic_Type()
)
monitorTxTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorTxTraffic.setStatus("current")
_MonitorRxTraffic_Type = Integer32
_MonitorRxTraffic_Object = MibTableColumn
monitorRxTraffic = _MonitorRxTraffic_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 10, 3, 1, 8),
    _MonitorRxTraffic_Type()
)
monitorRxTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorRxTraffic.setStatus("current")
_MonitorDiTable_Object = MibTable
monitorDiTable = _MonitorDiTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 10, 4)
)
if mibBuilder.loadTexts:
    monitorDiTable.setStatus("current")
_MonitorDiEntry_Object = MibTableRow
monitorDiEntry = _MonitorDiEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 10, 4, 1)
)
monitorDiEntry.setIndexNames(
    (0, "MOXA-EDSP506E-MIB", "diIndex"),
)
if mibBuilder.loadTexts:
    monitorDiEntry.setStatus("current")


class _DiIndex_Type(Integer32):
    """Custom type diIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_DiIndex_Type.__name__ = "Integer32"
_DiIndex_Object = MibTableColumn
diIndex = _DiIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 10, 4, 1, 1),
    _DiIndex_Type()
)
diIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diIndex.setStatus("current")


class _DiInputStatus_Type(Integer32):
    """Custom type diInputStatus based on Integer32"""
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


_DiInputStatus_Type.__name__ = "Integer32"
_DiInputStatus_Object = MibTableColumn
diInputStatus = _DiInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 10, 4, 1, 2),
    _DiInputStatus_Type()
)
diInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diInputStatus.setStatus("current")
_PowerConsumption_Type = DisplayString
_PowerConsumption_Object = MibScalar
powerConsumption = _PowerConsumption_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 10, 8),
    _PowerConsumption_Type()
)
powerConsumption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerConsumption.setStatus("current")
_MonitorFiberCheckTable_Object = MibTable
monitorFiberCheckTable = _MonitorFiberCheckTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 10, 11)
)
if mibBuilder.loadTexts:
    monitorFiberCheckTable.setStatus("current")
_MonitorFiberCheckEntry_Object = MibTableRow
monitorFiberCheckEntry = _MonitorFiberCheckEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 10, 11, 1)
)
monitorFiberCheckEntry.setIndexNames(
    (0, "MOXA-EDSP506E-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    monitorFiberCheckEntry.setStatus("current")
_FiberPort_Type = DisplayString
_FiberPort_Object = MibTableColumn
fiberPort = _FiberPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 10, 11, 1, 1),
    _FiberPort_Type()
)
fiberPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fiberPort.setStatus("current")
_FiberModelName_Type = DisplayString
_FiberModelName_Object = MibTableColumn
fiberModelName = _FiberModelName_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 10, 11, 1, 2),
    _FiberModelName_Type()
)
fiberModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fiberModelName.setStatus("current")
_FiberWaveLength_Type = DisplayString
_FiberWaveLength_Object = MibTableColumn
fiberWaveLength = _FiberWaveLength_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 10, 11, 1, 3),
    _FiberWaveLength_Type()
)
fiberWaveLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fiberWaveLength.setStatus("current")
_FiberVoltage_Type = DisplayString
_FiberVoltage_Object = MibTableColumn
fiberVoltage = _FiberVoltage_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 10, 11, 1, 4),
    _FiberVoltage_Type()
)
fiberVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fiberVoltage.setStatus("current")
_FiberTemperature_Type = DisplayString
_FiberTemperature_Object = MibTableColumn
fiberTemperature = _FiberTemperature_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 10, 11, 1, 5),
    _FiberTemperature_Type()
)
fiberTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fiberTemperature.setStatus("current")
_FiberTempWarn_Type = DisplayString
_FiberTempWarn_Object = MibTableColumn
fiberTempWarn = _FiberTempWarn_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 10, 11, 1, 6),
    _FiberTempWarn_Type()
)
fiberTempWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fiberTempWarn.setStatus("current")
_FiberTxPower_Type = DisplayString
_FiberTxPower_Object = MibTableColumn
fiberTxPower = _FiberTxPower_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 10, 11, 1, 7),
    _FiberTxPower_Type()
)
fiberTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fiberTxPower.setStatus("current")
_FiberTxPowerWarn_Type = DisplayString
_FiberTxPowerWarn_Object = MibTableColumn
fiberTxPowerWarn = _FiberTxPowerWarn_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 10, 11, 1, 8),
    _FiberTxPowerWarn_Type()
)
fiberTxPowerWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fiberTxPowerWarn.setStatus("current")
_FiberRxPower_Type = DisplayString
_FiberRxPower_Object = MibTableColumn
fiberRxPower = _FiberRxPower_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 10, 11, 1, 9),
    _FiberRxPower_Type()
)
fiberRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fiberRxPower.setStatus("current")
_FiberRxPowerWarn_Type = DisplayString
_FiberRxPowerWarn_Object = MibTableColumn
fiberRxPowerWarn = _FiberRxPowerWarn_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 10, 11, 1, 10),
    _FiberRxPowerWarn_Type()
)
fiberRxPowerWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fiberRxPowerWarn.setStatus("current")
_FiberSN_Type = DisplayString
_FiberSN_Object = MibTableColumn
fiberSN = _FiberSN_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 10, 11, 1, 13),
    _FiberSN_Type()
)
fiberSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fiberSN.setStatus("current")
_MonitorPoEEPSTable_Object = MibTable
monitorPoEEPSTable = _MonitorPoEEPSTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 10, 12)
)
if mibBuilder.loadTexts:
    monitorPoEEPSTable.setStatus("current")
_MonitorPoEEPSEntry_Object = MibTableRow
monitorPoEEPSEntry = _MonitorPoEEPSEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 10, 12, 1)
)
monitorPoEEPSEntry.setIndexNames(
    (0, "MOXA-EDSP506E-MIB", "epsIndex"),
)
if mibBuilder.loadTexts:
    monitorPoEEPSEntry.setStatus("current")
_EpsIndex_Type = Integer32
_EpsIndex_Object = MibTableColumn
epsIndex = _EpsIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 10, 12, 1, 1),
    _EpsIndex_Type()
)
epsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epsIndex.setStatus("current")


class _EpsState_Type(Integer32):
    """Custom type epsState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-present", 0),
          ("present", 1))
    )


_EpsState_Type.__name__ = "Integer32"
_EpsState_Object = MibTableColumn
epsState = _EpsState_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 10, 12, 1, 2),
    _EpsState_Type()
)
epsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epsState.setStatus("current")
_EmailWarning_ObjectIdentity = ObjectIdentity
emailWarning = _EmailWarning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 11)
)
_EmailService_ObjectIdentity = ObjectIdentity
emailService = _EmailService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 11, 1)
)
_EmailWarningSMTPServer_Type = DisplayString
_EmailWarningSMTPServer_Object = MibScalar
emailWarningSMTPServer = _EmailWarningSMTPServer_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 11, 1, 1),
    _EmailWarningSMTPServer_Type()
)
emailWarningSMTPServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailWarningSMTPServer.setStatus("current")
_EmailWarningFirstRecipientEmailAddr_Type = DisplayString
_EmailWarningFirstRecipientEmailAddr_Object = MibScalar
emailWarningFirstRecipientEmailAddr = _EmailWarningFirstRecipientEmailAddr_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 11, 1, 2),
    _EmailWarningFirstRecipientEmailAddr_Type()
)
emailWarningFirstRecipientEmailAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailWarningFirstRecipientEmailAddr.setStatus("current")
_EmailWarningSecondRecipientEmailAddr_Type = DisplayString
_EmailWarningSecondRecipientEmailAddr_Object = MibScalar
emailWarningSecondRecipientEmailAddr = _EmailWarningSecondRecipientEmailAddr_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 11, 1, 3),
    _EmailWarningSecondRecipientEmailAddr_Type()
)
emailWarningSecondRecipientEmailAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailWarningSecondRecipientEmailAddr.setStatus("current")
_EmailWarningThirdRecipientEmailAddr_Type = DisplayString
_EmailWarningThirdRecipientEmailAddr_Object = MibScalar
emailWarningThirdRecipientEmailAddr = _EmailWarningThirdRecipientEmailAddr_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 11, 1, 4),
    _EmailWarningThirdRecipientEmailAddr_Type()
)
emailWarningThirdRecipientEmailAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailWarningThirdRecipientEmailAddr.setStatus("current")
_EmailWarningFourthRecipientEmailAddr_Type = DisplayString
_EmailWarningFourthRecipientEmailAddr_Object = MibScalar
emailWarningFourthRecipientEmailAddr = _EmailWarningFourthRecipientEmailAddr_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 11, 1, 5),
    _EmailWarningFourthRecipientEmailAddr_Type()
)
emailWarningFourthRecipientEmailAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailWarningFourthRecipientEmailAddr.setStatus("current")


class _EmailWarningSMTPPort_Type(Integer32):
    """Custom type emailWarningSMTPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_EmailWarningSMTPPort_Type.__name__ = "Integer32"
_EmailWarningSMTPPort_Object = MibScalar
emailWarningSMTPPort = _EmailWarningSMTPPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 11, 1, 6),
    _EmailWarningSMTPPort_Type()
)
emailWarningSMTPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailWarningSMTPPort.setStatus("current")
_EmailWarningSMTPUser_Type = DisplayString
_EmailWarningSMTPUser_Object = MibScalar
emailWarningSMTPUser = _EmailWarningSMTPUser_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 11, 1, 7),
    _EmailWarningSMTPUser_Type()
)
emailWarningSMTPUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailWarningSMTPUser.setStatus("current")
_EmailWarningSMTPPassword_Type = DisplayString
_EmailWarningSMTPPassword_Object = MibScalar
emailWarningSMTPPassword = _EmailWarningSMTPPassword_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 11, 1, 8),
    _EmailWarningSMTPPassword_Type()
)
emailWarningSMTPPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailWarningSMTPPassword.setStatus("current")


class _EmailWarningSMTPTLS_Type(Integer32):
    """Custom type emailWarningSMTPTLS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_EmailWarningSMTPTLS_Type.__name__ = "Integer32"
_EmailWarningSMTPTLS_Object = MibScalar
emailWarningSMTPTLS = _EmailWarningSMTPTLS_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 11, 1, 9),
    _EmailWarningSMTPTLS_Type()
)
emailWarningSMTPTLS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailWarningSMTPTLS.setStatus("current")


class _EmailWarningSMTPAuthMethod_Type(Integer32):
    """Custom type emailWarningSMTPAuthMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("plain", 0),
          ("login", 1),
          ("cram-md5", 2))
    )


_EmailWarningSMTPAuthMethod_Type.__name__ = "Integer32"
_EmailWarningSMTPAuthMethod_Object = MibScalar
emailWarningSMTPAuthMethod = _EmailWarningSMTPAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 11, 1, 10),
    _EmailWarningSMTPAuthMethod_Type()
)
emailWarningSMTPAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailWarningSMTPAuthMethod.setStatus("current")
_EmailWarningSenderEmailAddr_Type = DisplayString
_EmailWarningSenderEmailAddr_Object = MibScalar
emailWarningSenderEmailAddr = _EmailWarningSenderEmailAddr_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 11, 1, 11),
    _EmailWarningSenderEmailAddr_Type()
)
emailWarningSenderEmailAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailWarningSenderEmailAddr.setStatus("current")
_SetDeviceIp_ObjectIdentity = ObjectIdentity
setDeviceIp = _SetDeviceIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 12)
)
_SetDevIpTable_Object = MibTable
setDevIpTable = _SetDevIpTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 12, 1)
)
if mibBuilder.loadTexts:
    setDevIpTable.setStatus("current")
_SetDevIpEntry_Object = MibTableRow
setDevIpEntry = _SetDevIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 12, 1, 1)
)
setDevIpEntry.setIndexNames(
    (0, "MOXA-EDSP506E-MIB", "setDevIpIndex"),
)
if mibBuilder.loadTexts:
    setDevIpEntry.setStatus("current")
_SetDevIpIndex_Type = Integer32
_SetDevIpIndex_Object = MibTableColumn
setDevIpIndex = _SetDevIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 12, 1, 1, 1),
    _SetDevIpIndex_Type()
)
setDevIpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setDevIpIndex.setStatus("current")
_SetDevIpCurrentIpofDevice_Type = DisplayString
_SetDevIpCurrentIpofDevice_Object = MibTableColumn
setDevIpCurrentIpofDevice = _SetDevIpCurrentIpofDevice_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 12, 1, 1, 2),
    _SetDevIpCurrentIpofDevice_Type()
)
setDevIpCurrentIpofDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setDevIpCurrentIpofDevice.setStatus("current")


class _SetDevIpPresentBy_Type(Integer32):
    """Custom type setDevIpPresentBy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("dhcpClient", 1),
          ("rarp", 2),
          ("bootp", 4))
    )


_SetDevIpPresentBy_Type.__name__ = "Integer32"
_SetDevIpPresentBy_Object = MibTableColumn
setDevIpPresentBy = _SetDevIpPresentBy_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 12, 1, 1, 3),
    _SetDevIpPresentBy_Type()
)
setDevIpPresentBy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setDevIpPresentBy.setStatus("current")
_SetDevIpDedicatedIp_Type = IpAddress
_SetDevIpDedicatedIp_Object = MibTableColumn
setDevIpDedicatedIp = _SetDevIpDedicatedIp_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 12, 1, 1, 4),
    _SetDevIpDedicatedIp_Type()
)
setDevIpDedicatedIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setDevIpDedicatedIp.setStatus("current")
_Mirroring_ObjectIdentity = ObjectIdentity
mirroring = _Mirroring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 13)
)
_TargetPort_Type = Integer32
_TargetPort_Object = MibScalar
targetPort = _TargetPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 13, 1),
    _TargetPort_Type()
)
targetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    targetPort.setStatus("current")
_MirroringPort_Type = Integer32
_MirroringPort_Object = MibScalar
mirroringPort = _MirroringPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 13, 2),
    _MirroringPort_Type()
)
mirroringPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mirroringPort.setStatus("current")


class _MonitorDirection_Type(Integer32):
    """Custom type monitorDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inputDataStream", 0),
          ("outputDataStream", 1),
          ("biDirectional", 2))
    )


_MonitorDirection_Type.__name__ = "Integer32"
_MonitorDirection_Object = MibScalar
monitorDirection = _MonitorDirection_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 13, 3),
    _MonitorDirection_Type()
)
monitorDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    monitorDirection.setStatus("current")
_PortTrunking_ObjectIdentity = ObjectIdentity
portTrunking = _PortTrunking_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 14)
)
_TrunkSettingTable_Object = MibTable
trunkSettingTable = _TrunkSettingTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 14, 1)
)
if mibBuilder.loadTexts:
    trunkSettingTable.setStatus("current")
_TrunkSettingEntry_Object = MibTableRow
trunkSettingEntry = _TrunkSettingEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 14, 1, 1)
)
trunkSettingEntry.setIndexNames(
    (0, "MOXA-EDSP506E-MIB", "trunkSettingIndex"),
)
if mibBuilder.loadTexts:
    trunkSettingEntry.setStatus("current")
_TrunkSettingIndex_Type = Integer32
_TrunkSettingIndex_Object = MibTableColumn
trunkSettingIndex = _TrunkSettingIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 14, 1, 1, 1),
    _TrunkSettingIndex_Type()
)
trunkSettingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkSettingIndex.setStatus("current")


class _TrunkType_Type(Integer32):
    """Custom type trunkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("lacp", 2))
    )


_TrunkType_Type.__name__ = "Integer32"
_TrunkType_Object = MibTableColumn
trunkType = _TrunkType_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 14, 1, 1, 2),
    _TrunkType_Type()
)
trunkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trunkType.setStatus("current")
_TrunkMemberPorts_Type = PortList
_TrunkMemberPorts_Object = MibTableColumn
trunkMemberPorts = _TrunkMemberPorts_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 14, 1, 1, 3),
    _TrunkMemberPorts_Type()
)
trunkMemberPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trunkMemberPorts.setStatus("current")
_TrunkTable_Object = MibTable
trunkTable = _TrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 14, 2)
)
if mibBuilder.loadTexts:
    trunkTable.setStatus("current")
_TrunkEntry_Object = MibTableRow
trunkEntry = _TrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 14, 2, 1)
)
trunkEntry.setIndexNames(
    (0, "MOXA-EDSP506E-MIB", "trunkIndex"),
    (0, "MOXA-EDSP506E-MIB", "trunkPort"),
)
if mibBuilder.loadTexts:
    trunkEntry.setStatus("current")
_TrunkIndex_Type = Integer32
_TrunkIndex_Object = MibTableColumn
trunkIndex = _TrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 14, 2, 1, 1),
    _TrunkIndex_Type()
)
trunkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkIndex.setStatus("current")
_TrunkPort_Type = Integer32
_TrunkPort_Object = MibTableColumn
trunkPort = _TrunkPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 14, 2, 1, 2),
    _TrunkPort_Type()
)
trunkPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkPort.setStatus("current")


class _TrunkStatus_Type(Integer32):
    """Custom type trunkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("success", 1),
          ("fail", 2),
          ("standby", 3))
    )


_TrunkStatus_Type.__name__ = "Integer32"
_TrunkStatus_Object = MibTableColumn
trunkStatus = _TrunkStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 14, 2, 1, 3),
    _TrunkStatus_Type()
)
trunkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkStatus.setStatus("current")
_CommRedundancy_ObjectIdentity = ObjectIdentity
commRedundancy = _CommRedundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16)
)


class _ProtocolOfRedundancySetup_Type(Integer32):
    """Custom type protocolOfRedundancySetup based on Integer32"""
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
        *(("spanningTree", 1),
          ("turboRing", 2),
          ("turboRingV2", 3),
          ("turboChain", 4),
          ("mstp", 5))
    )


_ProtocolOfRedundancySetup_Type.__name__ = "Integer32"
_ProtocolOfRedundancySetup_Object = MibScalar
protocolOfRedundancySetup = _ProtocolOfRedundancySetup_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 1),
    _ProtocolOfRedundancySetup_Type()
)
protocolOfRedundancySetup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protocolOfRedundancySetup.setStatus("current")
_TurboRing_ObjectIdentity = ObjectIdentity
turboRing = _TurboRing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 2)
)


class _TurboRingMaster_Type(Integer32):
    """Custom type turboRingMaster based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_TurboRingMaster_Type.__name__ = "Integer32"
_TurboRingMaster_Object = MibScalar
turboRingMaster = _TurboRingMaster_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 2, 1),
    _TurboRingMaster_Type()
)
turboRingMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    turboRingMaster.setStatus("current")


class _TurboRingMasterSetup_Type(Integer32):
    """Custom type turboRingMasterSetup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_TurboRingMasterSetup_Type.__name__ = "Integer32"
_TurboRingMasterSetup_Object = MibScalar
turboRingMasterSetup = _TurboRingMasterSetup_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 2, 2),
    _TurboRingMasterSetup_Type()
)
turboRingMasterSetup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRingMasterSetup.setStatus("current")
_TurboRingPortTable_Object = MibTable
turboRingPortTable = _TurboRingPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 2, 3)
)
if mibBuilder.loadTexts:
    turboRingPortTable.setStatus("current")
_TurboRingPortEntry_Object = MibTableRow
turboRingPortEntry = _TurboRingPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 2, 3, 1)
)
turboRingPortEntry.setIndexNames(
    (0, "MOXA-EDSP506E-MIB", "turboRingPortIndex"),
)
if mibBuilder.loadTexts:
    turboRingPortEntry.setStatus("current")
_TurboRingPortIndex_Type = Integer32
_TurboRingPortIndex_Object = MibTableColumn
turboRingPortIndex = _TurboRingPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 2, 3, 1, 1),
    _TurboRingPortIndex_Type()
)
turboRingPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    turboRingPortIndex.setStatus("current")


class _TurboRingPortStatus_Type(Integer32):
    """Custom type turboRingPortStatus based on Integer32"""
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
        *(("portDisabled", 0),
          ("notTurboRingPort", 1),
          ("linkDown", 2),
          ("blocked", 3),
          ("learning", 4),
          ("forwarding", 5))
    )


_TurboRingPortStatus_Type.__name__ = "Integer32"
_TurboRingPortStatus_Object = MibTableColumn
turboRingPortStatus = _TurboRingPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 2, 3, 1, 2),
    _TurboRingPortStatus_Type()
)
turboRingPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    turboRingPortStatus.setStatus("current")
_TurboRingPortDesignatedBridge_Type = MacAddress
_TurboRingPortDesignatedBridge_Object = MibTableColumn
turboRingPortDesignatedBridge = _TurboRingPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 2, 3, 1, 3),
    _TurboRingPortDesignatedBridge_Type()
)
turboRingPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    turboRingPortDesignatedBridge.setStatus("current")
_TurboRingPortDesignatedPort_Type = Integer32
_TurboRingPortDesignatedPort_Object = MibTableColumn
turboRingPortDesignatedPort = _TurboRingPortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 2, 3, 1, 4),
    _TurboRingPortDesignatedPort_Type()
)
turboRingPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    turboRingPortDesignatedPort.setStatus("current")
_TurboRingDesignatedMaster_Type = MacAddress
_TurboRingDesignatedMaster_Object = MibScalar
turboRingDesignatedMaster = _TurboRingDesignatedMaster_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 2, 6),
    _TurboRingDesignatedMaster_Type()
)
turboRingDesignatedMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    turboRingDesignatedMaster.setStatus("current")
_TurboRingRdntPort1_Type = Integer32
_TurboRingRdntPort1_Object = MibScalar
turboRingRdntPort1 = _TurboRingRdntPort1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 2, 7),
    _TurboRingRdntPort1_Type()
)
turboRingRdntPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRingRdntPort1.setStatus("current")
_TurboRingRdntPort2_Type = Integer32
_TurboRingRdntPort2_Object = MibScalar
turboRingRdntPort2 = _TurboRingRdntPort2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 2, 8),
    _TurboRingRdntPort2_Type()
)
turboRingRdntPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRingRdntPort2.setStatus("current")


class _TurboRingEnableCoupling_Type(Integer32):
    """Custom type turboRingEnableCoupling based on Integer32"""
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


_TurboRingEnableCoupling_Type.__name__ = "Integer32"
_TurboRingEnableCoupling_Object = MibScalar
turboRingEnableCoupling = _TurboRingEnableCoupling_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 2, 9),
    _TurboRingEnableCoupling_Type()
)
turboRingEnableCoupling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRingEnableCoupling.setStatus("current")
_TurboRingCouplingPort_Type = Integer32
_TurboRingCouplingPort_Object = MibScalar
turboRingCouplingPort = _TurboRingCouplingPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 2, 10),
    _TurboRingCouplingPort_Type()
)
turboRingCouplingPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRingCouplingPort.setStatus("current")


class _TurboRingCouplingPortStatus_Type(Integer32):
    """Custom type turboRingCouplingPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("portDisabled", 0),
          ("notCouplingPort", 1),
          ("linkDown", 2),
          ("blocked", 3),
          ("forwarding", 5))
    )


_TurboRingCouplingPortStatus_Type.__name__ = "Integer32"
_TurboRingCouplingPortStatus_Object = MibScalar
turboRingCouplingPortStatus = _TurboRingCouplingPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 2, 11),
    _TurboRingCouplingPortStatus_Type()
)
turboRingCouplingPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    turboRingCouplingPortStatus.setStatus("current")
_TurboRingControlPort_Type = Integer32
_TurboRingControlPort_Object = MibScalar
turboRingControlPort = _TurboRingControlPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 2, 12),
    _TurboRingControlPort_Type()
)
turboRingControlPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRingControlPort.setStatus("current")


class _TurboRingControlPortStatus_Type(Integer32):
    """Custom type turboRingControlPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("portDisabled", 0),
          ("notControlPort", 1),
          ("linkDown", 2),
          ("blocked", 3),
          ("forwarding", 5),
          ("inactive", 6),
          ("active", 7))
    )


_TurboRingControlPortStatus_Type.__name__ = "Integer32"
_TurboRingControlPortStatus_Object = MibScalar
turboRingControlPortStatus = _TurboRingControlPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 2, 13),
    _TurboRingControlPortStatus_Type()
)
turboRingControlPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    turboRingControlPortStatus.setStatus("current")


class _TurboRingBrokenStatus_Type(Integer32):
    """Custom type turboRingBrokenStatus based on Integer32"""
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
          ("normal", 1),
          ("broken", 2))
    )


_TurboRingBrokenStatus_Type.__name__ = "Integer32"
_TurboRingBrokenStatus_Object = MibScalar
turboRingBrokenStatus = _TurboRingBrokenStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 2, 14),
    _TurboRingBrokenStatus_Type()
)
turboRingBrokenStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    turboRingBrokenStatus.setStatus("current")
_SpanningTree_ObjectIdentity = ObjectIdentity
spanningTree = _SpanningTree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 3)
)


class _SpanningTreeRoot_Type(Integer32):
    """Custom type spanningTreeRoot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_SpanningTreeRoot_Type.__name__ = "Integer32"
_SpanningTreeRoot_Object = MibScalar
spanningTreeRoot = _SpanningTreeRoot_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 3, 1),
    _SpanningTreeRoot_Type()
)
spanningTreeRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spanningTreeRoot.setStatus("current")


class _SpanningTreeBridgePriority_Type(Integer32):
    """Custom type spanningTreeBridgePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4096,
              8192,
              12288,
              16384,
              20480,
              24576,
              28672,
              32768,
              36864,
              40960,
              45056,
              49152,
              53248,
              57344,
              61440)
        )
    )
    namedValues = NamedValues(
        *(("priority0", 0),
          ("priority4096", 4096),
          ("priority8192", 8192),
          ("priority12288", 12288),
          ("priority16384", 16384),
          ("priority20480", 20480),
          ("priority24576", 24576),
          ("priority28672", 28672),
          ("priority32768", 32768),
          ("priority36864", 36864),
          ("priority40960", 40960),
          ("priority45056", 45056),
          ("priority49152", 49152),
          ("priority53248", 53248),
          ("priority57344", 57344),
          ("priority61440", 61440))
    )


_SpanningTreeBridgePriority_Type.__name__ = "Integer32"
_SpanningTreeBridgePriority_Object = MibScalar
spanningTreeBridgePriority = _SpanningTreeBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 3, 2),
    _SpanningTreeBridgePriority_Type()
)
spanningTreeBridgePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spanningTreeBridgePriority.setStatus("current")
_SpanningTreeHelloTime_Type = Integer32
_SpanningTreeHelloTime_Object = MibScalar
spanningTreeHelloTime = _SpanningTreeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 3, 3),
    _SpanningTreeHelloTime_Type()
)
spanningTreeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spanningTreeHelloTime.setStatus("current")
_SpanningTreeMaxAge_Type = Integer32
_SpanningTreeMaxAge_Object = MibScalar
spanningTreeMaxAge = _SpanningTreeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 3, 4),
    _SpanningTreeMaxAge_Type()
)
spanningTreeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spanningTreeMaxAge.setStatus("current")
_SpanningTreeForwardingDelay_Type = Integer32
_SpanningTreeForwardingDelay_Object = MibScalar
spanningTreeForwardingDelay = _SpanningTreeForwardingDelay_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 3, 5),
    _SpanningTreeForwardingDelay_Type()
)
spanningTreeForwardingDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spanningTreeForwardingDelay.setStatus("current")
_SpanningTreeTable_Object = MibTable
spanningTreeTable = _SpanningTreeTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 3, 6)
)
if mibBuilder.loadTexts:
    spanningTreeTable.setStatus("current")
_SpanningTreeEntry_Object = MibTableRow
spanningTreeEntry = _SpanningTreeEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 3, 6, 1)
)
spanningTreeEntry.setIndexNames(
    (0, "MOXA-EDSP506E-MIB", "spanningTreeIndex"),
)
if mibBuilder.loadTexts:
    spanningTreeEntry.setStatus("current")
_SpanningTreeIndex_Type = Integer32
_SpanningTreeIndex_Object = MibTableColumn
spanningTreeIndex = _SpanningTreeIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 3, 6, 1, 1),
    _SpanningTreeIndex_Type()
)
spanningTreeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spanningTreeIndex.setStatus("current")


class _EnableSpanningTree_Type(Integer32):
    """Custom type enableSpanningTree based on Integer32"""
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


_EnableSpanningTree_Type.__name__ = "Integer32"
_EnableSpanningTree_Object = MibTableColumn
enableSpanningTree = _EnableSpanningTree_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 3, 6, 1, 2),
    _EnableSpanningTree_Type()
)
enableSpanningTree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableSpanningTree.setStatus("current")


class _SpanningTreePortPriority_Type(Integer32):
    """Custom type spanningTreePortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              16,
              32,
              48,
              64,
              80,
              96,
              112,
              128,
              144,
              160,
              176,
              192,
              208,
              224,
              240)
        )
    )
    namedValues = NamedValues(
        *(("priority0", 0),
          ("priority16", 16),
          ("priority32", 32),
          ("priority48", 48),
          ("priority64", 64),
          ("priority80", 80),
          ("priority96", 96),
          ("priority112", 112),
          ("priority128", 128),
          ("priority144", 144),
          ("priority160", 160),
          ("priority176", 176),
          ("priority192", 192),
          ("priority208", 208),
          ("priority224", 224),
          ("priority240", 240))
    )


_SpanningTreePortPriority_Type.__name__ = "Integer32"
_SpanningTreePortPriority_Object = MibTableColumn
spanningTreePortPriority = _SpanningTreePortPriority_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 3, 6, 1, 3),
    _SpanningTreePortPriority_Type()
)
spanningTreePortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spanningTreePortPriority.setStatus("current")
_SpanningTreePortCost_Type = Integer32
_SpanningTreePortCost_Object = MibTableColumn
spanningTreePortCost = _SpanningTreePortCost_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 3, 6, 1, 4),
    _SpanningTreePortCost_Type()
)
spanningTreePortCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spanningTreePortCost.setStatus("current")


class _SpanningTreePortStatus_Type(Integer32):
    """Custom type spanningTreePortStatus based on Integer32"""
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
        *(("portDisabled", 0),
          ("notSpanningTreePort", 1),
          ("linkDown", 2),
          ("blocked", 3),
          ("learning", 4),
          ("forwarding", 5))
    )


_SpanningTreePortStatus_Type.__name__ = "Integer32"
_SpanningTreePortStatus_Object = MibTableColumn
spanningTreePortStatus = _SpanningTreePortStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 3, 6, 1, 5),
    _SpanningTreePortStatus_Type()
)
spanningTreePortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spanningTreePortStatus.setStatus("current")


class _SpanningTreePortEdge_Type(Integer32):
    """Custom type spanningTreePortEdge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("true", 1),
          ("false", 2))
    )


_SpanningTreePortEdge_Type.__name__ = "Integer32"
_SpanningTreePortEdge_Object = MibTableColumn
spanningTreePortEdge = _SpanningTreePortEdge_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 3, 6, 1, 6),
    _SpanningTreePortEdge_Type()
)
spanningTreePortEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spanningTreePortEdge.setStatus("current")


class _ActiveProtocolOfRedundancy_Type(Integer32):
    """Custom type activeProtocolOfRedundancy based on Integer32"""
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
        *(("none", 0),
          ("spanningTree", 1),
          ("turboRing", 2),
          ("turboRingV2", 3),
          ("turboChain", 4),
          ("mstp", 5))
    )


_ActiveProtocolOfRedundancy_Type.__name__ = "Integer32"
_ActiveProtocolOfRedundancy_Object = MibScalar
activeProtocolOfRedundancy = _ActiveProtocolOfRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 4),
    _ActiveProtocolOfRedundancy_Type()
)
activeProtocolOfRedundancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeProtocolOfRedundancy.setStatus("current")
_TurboRingV2_ObjectIdentity = ObjectIdentity
turboRingV2 = _TurboRingV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 5)
)
_TurboRingV2Ring1_ObjectIdentity = ObjectIdentity
turboRingV2Ring1 = _TurboRingV2Ring1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 5, 1)
)


class _RingIndexRing1_Type(Integer32):
    """Custom type ringIndexRing1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_RingIndexRing1_Type.__name__ = "Integer32"
_RingIndexRing1_Object = MibScalar
ringIndexRing1 = _RingIndexRing1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 5, 1, 1),
    _RingIndexRing1_Type()
)
ringIndexRing1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringIndexRing1.setStatus("current")


class _RingEnableRing1_Type(Integer32):
    """Custom type ringEnableRing1 based on Integer32"""
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


_RingEnableRing1_Type.__name__ = "Integer32"
_RingEnableRing1_Object = MibScalar
ringEnableRing1 = _RingEnableRing1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 5, 1, 2),
    _RingEnableRing1_Type()
)
ringEnableRing1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringEnableRing1.setStatus("current")


class _MasterSetupRing1_Type(Integer32):
    """Custom type masterSetupRing1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_MasterSetupRing1_Type.__name__ = "Integer32"
_MasterSetupRing1_Object = MibScalar
masterSetupRing1 = _MasterSetupRing1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 5, 1, 3),
    _MasterSetupRing1_Type()
)
masterSetupRing1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    masterSetupRing1.setStatus("current")


class _MasterStatusRing1_Type(Integer32):
    """Custom type masterStatusRing1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_MasterStatusRing1_Type.__name__ = "Integer32"
_MasterStatusRing1_Object = MibScalar
masterStatusRing1 = _MasterStatusRing1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 5, 1, 4),
    _MasterStatusRing1_Type()
)
masterStatusRing1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    masterStatusRing1.setStatus("current")
_DesignatedMasterRing1_Type = MacAddress
_DesignatedMasterRing1_Object = MibScalar
designatedMasterRing1 = _DesignatedMasterRing1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 5, 1, 5),
    _DesignatedMasterRing1_Type()
)
designatedMasterRing1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    designatedMasterRing1.setStatus("current")
_Rdnt1stPortRing1_Type = Integer32
_Rdnt1stPortRing1_Object = MibScalar
rdnt1stPortRing1 = _Rdnt1stPortRing1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 5, 1, 6),
    _Rdnt1stPortRing1_Type()
)
rdnt1stPortRing1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnt1stPortRing1.setStatus("current")


class _Rdnt1stPortStatusRing1_Type(Integer32):
    """Custom type rdnt1stPortStatusRing1 based on Integer32"""
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
        *(("disabled", 0),
          ("notRedundant", 1),
          ("linkdown", 2),
          ("blocking", 3),
          ("learning", 4),
          ("forwarding", 5))
    )


_Rdnt1stPortStatusRing1_Type.__name__ = "Integer32"
_Rdnt1stPortStatusRing1_Object = MibScalar
rdnt1stPortStatusRing1 = _Rdnt1stPortStatusRing1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 5, 1, 7),
    _Rdnt1stPortStatusRing1_Type()
)
rdnt1stPortStatusRing1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnt1stPortStatusRing1.setStatus("current")
_Rdnt2ndPortRing1_Type = Integer32
_Rdnt2ndPortRing1_Object = MibScalar
rdnt2ndPortRing1 = _Rdnt2ndPortRing1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 5, 1, 8),
    _Rdnt2ndPortRing1_Type()
)
rdnt2ndPortRing1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnt2ndPortRing1.setStatus("current")


class _Rdnt2ndPortStatusRing1_Type(Integer32):
    """Custom type rdnt2ndPortStatusRing1 based on Integer32"""
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
        *(("disabled", 0),
          ("notRedundant", 1),
          ("linkdown", 2),
          ("blocking", 3),
          ("learning", 4),
          ("forwarding", 5))
    )


_Rdnt2ndPortStatusRing1_Type.__name__ = "Integer32"
_Rdnt2ndPortStatusRing1_Object = MibScalar
rdnt2ndPortStatusRing1 = _Rdnt2ndPortStatusRing1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 5, 1, 9),
    _Rdnt2ndPortStatusRing1_Type()
)
rdnt2ndPortStatusRing1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnt2ndPortStatusRing1.setStatus("current")


class _BrokenStatusRing1_Type(Integer32):
    """Custom type brokenStatusRing1 based on Integer32"""
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
          ("normal", 1),
          ("broken", 2))
    )


_BrokenStatusRing1_Type.__name__ = "Integer32"
_BrokenStatusRing1_Object = MibScalar
brokenStatusRing1 = _BrokenStatusRing1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 5, 1, 10),
    _BrokenStatusRing1_Type()
)
brokenStatusRing1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brokenStatusRing1.setStatus("current")
_TurboRingV2Ring2_ObjectIdentity = ObjectIdentity
turboRingV2Ring2 = _TurboRingV2Ring2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 5, 2)
)


class _RingIndexRing2_Type(Integer32):
    """Custom type ringIndexRing2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_RingIndexRing2_Type.__name__ = "Integer32"
_RingIndexRing2_Object = MibScalar
ringIndexRing2 = _RingIndexRing2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 5, 2, 1),
    _RingIndexRing2_Type()
)
ringIndexRing2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringIndexRing2.setStatus("current")


class _RingEnableRing2_Type(Integer32):
    """Custom type ringEnableRing2 based on Integer32"""
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


_RingEnableRing2_Type.__name__ = "Integer32"
_RingEnableRing2_Object = MibScalar
ringEnableRing2 = _RingEnableRing2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 5, 2, 2),
    _RingEnableRing2_Type()
)
ringEnableRing2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringEnableRing2.setStatus("current")


class _MasterSetupRing2_Type(Integer32):
    """Custom type masterSetupRing2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_MasterSetupRing2_Type.__name__ = "Integer32"
_MasterSetupRing2_Object = MibScalar
masterSetupRing2 = _MasterSetupRing2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 5, 2, 3),
    _MasterSetupRing2_Type()
)
masterSetupRing2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    masterSetupRing2.setStatus("current")


class _MasterStatusRing2_Type(Integer32):
    """Custom type masterStatusRing2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_MasterStatusRing2_Type.__name__ = "Integer32"
_MasterStatusRing2_Object = MibScalar
masterStatusRing2 = _MasterStatusRing2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 5, 2, 4),
    _MasterStatusRing2_Type()
)
masterStatusRing2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    masterStatusRing2.setStatus("current")
_DesignatedMasterRing2_Type = MacAddress
_DesignatedMasterRing2_Object = MibScalar
designatedMasterRing2 = _DesignatedMasterRing2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 5, 2, 5),
    _DesignatedMasterRing2_Type()
)
designatedMasterRing2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    designatedMasterRing2.setStatus("current")
_Rdnt1stPortRing2_Type = Integer32
_Rdnt1stPortRing2_Object = MibScalar
rdnt1stPortRing2 = _Rdnt1stPortRing2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 5, 2, 6),
    _Rdnt1stPortRing2_Type()
)
rdnt1stPortRing2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnt1stPortRing2.setStatus("current")


class _Rdnt1stPortStatusRing2_Type(Integer32):
    """Custom type rdnt1stPortStatusRing2 based on Integer32"""
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
        *(("disabled", 0),
          ("notRedundant", 1),
          ("linkdown", 2),
          ("blocking", 3),
          ("learning", 4),
          ("forwarding", 5))
    )


_Rdnt1stPortStatusRing2_Type.__name__ = "Integer32"
_Rdnt1stPortStatusRing2_Object = MibScalar
rdnt1stPortStatusRing2 = _Rdnt1stPortStatusRing2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 5, 2, 7),
    _Rdnt1stPortStatusRing2_Type()
)
rdnt1stPortStatusRing2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnt1stPortStatusRing2.setStatus("current")
_Rdnt2ndPortRing2_Type = Integer32
_Rdnt2ndPortRing2_Object = MibScalar
rdnt2ndPortRing2 = _Rdnt2ndPortRing2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 5, 2, 8),
    _Rdnt2ndPortRing2_Type()
)
rdnt2ndPortRing2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnt2ndPortRing2.setStatus("current")


class _Rdnt2ndPortStatusRing2_Type(Integer32):
    """Custom type rdnt2ndPortStatusRing2 based on Integer32"""
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
        *(("disabled", 0),
          ("notRedundant", 1),
          ("linkdown", 2),
          ("blocking", 3),
          ("learning", 4),
          ("forwarding", 5))
    )


_Rdnt2ndPortStatusRing2_Type.__name__ = "Integer32"
_Rdnt2ndPortStatusRing2_Object = MibScalar
rdnt2ndPortStatusRing2 = _Rdnt2ndPortStatusRing2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 5, 2, 9),
    _Rdnt2ndPortStatusRing2_Type()
)
rdnt2ndPortStatusRing2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnt2ndPortStatusRing2.setStatus("current")


class _BrokenStatusRing2_Type(Integer32):
    """Custom type brokenStatusRing2 based on Integer32"""
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
          ("normal", 1),
          ("broken", 2))
    )


_BrokenStatusRing2_Type.__name__ = "Integer32"
_BrokenStatusRing2_Object = MibScalar
brokenStatusRing2 = _BrokenStatusRing2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 5, 2, 10),
    _BrokenStatusRing2_Type()
)
brokenStatusRing2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brokenStatusRing2.setStatus("current")
_TurboRingV2Coupling_ObjectIdentity = ObjectIdentity
turboRingV2Coupling = _TurboRingV2Coupling_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 5, 3)
)


class _CouplingEnable_Type(Integer32):
    """Custom type couplingEnable based on Integer32"""
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


_CouplingEnable_Type.__name__ = "Integer32"
_CouplingEnable_Object = MibScalar
couplingEnable = _CouplingEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 5, 3, 1),
    _CouplingEnable_Type()
)
couplingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    couplingEnable.setStatus("current")


class _CouplingMode_Type(Integer32):
    """Custom type couplingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dualHoming", 1),
          ("couplingBackup", 2),
          ("couplingPrimary", 3))
    )


_CouplingMode_Type.__name__ = "Integer32"
_CouplingMode_Object = MibScalar
couplingMode = _CouplingMode_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 5, 3, 2),
    _CouplingMode_Type()
)
couplingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    couplingMode.setStatus("current")
_Coupling1stPort_Type = Integer32
_Coupling1stPort_Object = MibScalar
coupling1stPort = _Coupling1stPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 5, 3, 3),
    _Coupling1stPort_Type()
)
coupling1stPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coupling1stPort.setStatus("current")


class _Coupling1stPortStatus_Type(Integer32):
    """Custom type coupling1stPortStatus based on Integer32"""
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
        *(("disabled", 0),
          ("notRedundant", 1),
          ("linkdown", 2),
          ("blocking", 3),
          ("learning", 4),
          ("forwarding", 5))
    )


_Coupling1stPortStatus_Type.__name__ = "Integer32"
_Coupling1stPortStatus_Object = MibScalar
coupling1stPortStatus = _Coupling1stPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 5, 3, 4),
    _Coupling1stPortStatus_Type()
)
coupling1stPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coupling1stPortStatus.setStatus("current")
_Coupling2ndPort_Type = Integer32
_Coupling2ndPort_Object = MibScalar
coupling2ndPort = _Coupling2ndPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 5, 3, 5),
    _Coupling2ndPort_Type()
)
coupling2ndPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coupling2ndPort.setStatus("current")


class _Coupling2ndPortStatus_Type(Integer32):
    """Custom type coupling2ndPortStatus based on Integer32"""
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
        *(("disabled", 0),
          ("notRedundant", 1),
          ("linkdown", 2),
          ("blocking", 3),
          ("learning", 4),
          ("forwarding", 5))
    )


_Coupling2ndPortStatus_Type.__name__ = "Integer32"
_Coupling2ndPortStatus_Object = MibScalar
coupling2ndPortStatus = _Coupling2ndPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 5, 3, 6),
    _Coupling2ndPortStatus_Type()
)
coupling2ndPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coupling2ndPortStatus.setStatus("current")
_TurboChain_ObjectIdentity = ObjectIdentity
turboChain = _TurboChain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 6)
)


class _TurboChainRole_Type(Integer32):
    """Custom type turboChainRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("head", 1),
          ("member", 2),
          ("tail", 3))
    )


_TurboChainRole_Type.__name__ = "Integer32"
_TurboChainRole_Object = MibScalar
turboChainRole = _TurboChainRole_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 6, 1),
    _TurboChainRole_Type()
)
turboChainRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboChainRole.setStatus("current")
_TurboChainPort1_Type = Integer32
_TurboChainPort1_Object = MibScalar
turboChainPort1 = _TurboChainPort1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 6, 2),
    _TurboChainPort1_Type()
)
turboChainPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboChainPort1.setStatus("current")
_TurboChainPort2_Type = Integer32
_TurboChainPort2_Object = MibScalar
turboChainPort2 = _TurboChainPort2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 6, 3),
    _TurboChainPort2_Type()
)
turboChainPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboChainPort2.setStatus("current")


class _TurboChainPort1Status_Type(Integer32):
    """Custom type turboChainPort1Status based on Integer32"""
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
        *(("notTurboChainPort", 0),
          ("linkDown", 1),
          ("blocking", 2),
          ("blocked", 3),
          ("forwarding", 4),
          ("na", 5))
    )


_TurboChainPort1Status_Type.__name__ = "Integer32"
_TurboChainPort1Status_Object = MibScalar
turboChainPort1Status = _TurboChainPort1Status_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 6, 4),
    _TurboChainPort1Status_Type()
)
turboChainPort1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    turboChainPort1Status.setStatus("current")


class _TurboChainPort2Status_Type(Integer32):
    """Custom type turboChainPort2Status based on Integer32"""
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
        *(("notTurboChainPort", 0),
          ("linkDown", 1),
          ("blocking", 2),
          ("blocked", 3),
          ("forwarding", 4),
          ("na", 5))
    )


_TurboChainPort2Status_Type.__name__ = "Integer32"
_TurboChainPort2Status_Object = MibScalar
turboChainPort2Status = _TurboChainPort2Status_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 6, 5),
    _TurboChainPort2Status_Type()
)
turboChainPort2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    turboChainPort2Status.setStatus("current")
_TurboChainPort1PartnerBridge_Type = MacAddress
_TurboChainPort1PartnerBridge_Object = MibScalar
turboChainPort1PartnerBridge = _TurboChainPort1PartnerBridge_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 6, 6),
    _TurboChainPort1PartnerBridge_Type()
)
turboChainPort1PartnerBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    turboChainPort1PartnerBridge.setStatus("current")
_TurboChainPort2PartnerBridge_Type = MacAddress
_TurboChainPort2PartnerBridge_Object = MibScalar
turboChainPort2PartnerBridge = _TurboChainPort2PartnerBridge_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 16, 6, 7),
    _TurboChainPort2PartnerBridge_Type()
)
turboChainPort2PartnerBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    turboChainPort2PartnerBridge.setStatus("current")
_RelayWarning_ObjectIdentity = ObjectIdentity
relayWarning = _RelayWarning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 17)
)
_RelayWarningTable_Object = MibTable
relayWarningTable = _RelayWarningTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 17, 11)
)
if mibBuilder.loadTexts:
    relayWarningTable.setStatus("current")
_RelayWarningEntry_Object = MibTableRow
relayWarningEntry = _RelayWarningEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 17, 11, 1)
)
relayWarningEntry.setIndexNames(
    (0, "MOXA-EDSP506E-MIB", "relayAlarmIndex"),
)
if mibBuilder.loadTexts:
    relayWarningEntry.setStatus("current")
_RelayAlarmIndex_Type = Integer32
_RelayAlarmIndex_Object = MibTableColumn
relayAlarmIndex = _RelayAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 17, 11, 1, 1),
    _RelayAlarmIndex_Type()
)
relayAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relayAlarmIndex.setStatus("current")


class _RelayWarningRelayContact_Type(Integer32):
    """Custom type relayWarningRelayContact based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("closed", 0),
          ("opened", 1))
    )


_RelayWarningRelayContact_Type.__name__ = "Integer32"
_RelayWarningRelayContact_Object = MibTableColumn
relayWarningRelayContact = _RelayWarningRelayContact_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 17, 11, 1, 2),
    _RelayWarningRelayContact_Type()
)
relayWarningRelayContact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relayWarningRelayContact.setStatus("current")


class _OverrideRelayWarningSetting_Type(Integer32):
    """Custom type overrideRelayWarningSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_OverrideRelayWarningSetting_Type.__name__ = "Integer32"
_OverrideRelayWarningSetting_Object = MibTableColumn
overrideRelayWarningSetting = _OverrideRelayWarningSetting_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 17, 11, 1, 3),
    _OverrideRelayWarningSetting_Type()
)
overrideRelayWarningSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overrideRelayWarningSetting.setStatus("current")


class _RelayWarningPower1Off_Type(Integer32):
    """Custom type relayWarningPower1Off based on Integer32"""
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


_RelayWarningPower1Off_Type.__name__ = "Integer32"
_RelayWarningPower1Off_Object = MibTableColumn
relayWarningPower1Off = _RelayWarningPower1Off_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 17, 11, 1, 4),
    _RelayWarningPower1Off_Type()
)
relayWarningPower1Off.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayWarningPower1Off.setStatus("current")


class _RelayWarningPower1OffStatus_Type(Integer32):
    """Custom type relayWarningPower1OffStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-triggered", 0),
          ("triggered", 1))
    )


_RelayWarningPower1OffStatus_Type.__name__ = "Integer32"
_RelayWarningPower1OffStatus_Object = MibTableColumn
relayWarningPower1OffStatus = _RelayWarningPower1OffStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 17, 11, 1, 5),
    _RelayWarningPower1OffStatus_Type()
)
relayWarningPower1OffStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relayWarningPower1OffStatus.setStatus("current")


class _RelayWarningPower2Off_Type(Integer32):
    """Custom type relayWarningPower2Off based on Integer32"""
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


_RelayWarningPower2Off_Type.__name__ = "Integer32"
_RelayWarningPower2Off_Object = MibTableColumn
relayWarningPower2Off = _RelayWarningPower2Off_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 17, 11, 1, 6),
    _RelayWarningPower2Off_Type()
)
relayWarningPower2Off.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayWarningPower2Off.setStatus("current")


class _RelayWarningPower2OffStatus_Type(Integer32):
    """Custom type relayWarningPower2OffStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-triggered", 0),
          ("triggered", 1))
    )


_RelayWarningPower2OffStatus_Type.__name__ = "Integer32"
_RelayWarningPower2OffStatus_Object = MibTableColumn
relayWarningPower2OffStatus = _RelayWarningPower2OffStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 17, 11, 1, 7),
    _RelayWarningPower2OffStatus_Type()
)
relayWarningPower2OffStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relayWarningPower2OffStatus.setStatus("current")


class _RelayWarningTurboRingBreak_Type(Integer32):
    """Custom type relayWarningTurboRingBreak based on Integer32"""
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


_RelayWarningTurboRingBreak_Type.__name__ = "Integer32"
_RelayWarningTurboRingBreak_Object = MibTableColumn
relayWarningTurboRingBreak = _RelayWarningTurboRingBreak_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 17, 11, 1, 8),
    _RelayWarningTurboRingBreak_Type()
)
relayWarningTurboRingBreak.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayWarningTurboRingBreak.setStatus("current")


class _RelayWarningTurboRingBreakStatus_Type(Integer32):
    """Custom type relayWarningTurboRingBreakStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-triggered", 0),
          ("triggered", 1))
    )


_RelayWarningTurboRingBreakStatus_Type.__name__ = "Integer32"
_RelayWarningTurboRingBreakStatus_Object = MibTableColumn
relayWarningTurboRingBreakStatus = _RelayWarningTurboRingBreakStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 17, 11, 1, 9),
    _RelayWarningTurboRingBreakStatus_Type()
)
relayWarningTurboRingBreakStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relayWarningTurboRingBreakStatus.setStatus("current")
_PortRelayWarningTable_Object = MibTable
portRelayWarningTable = _PortRelayWarningTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 17, 12)
)
if mibBuilder.loadTexts:
    portRelayWarningTable.setStatus("current")
_PortRelayWarningEntry_Object = MibTableRow
portRelayWarningEntry = _PortRelayWarningEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 17, 12, 1)
)
portRelayWarningEntry.setIndexNames(
    (0, "MOXA-EDSP506E-MIB", "portIndex"),
    (0, "MOXA-EDSP506E-MIB", "relayAlarmIndex"),
)
if mibBuilder.loadTexts:
    portRelayWarningEntry.setStatus("current")


class _RelayWarningLinkChanged_Type(Integer32):
    """Custom type relayWarningLinkChanged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 0),
          ("on2off", 1),
          ("off2on", 2))
    )


_RelayWarningLinkChanged_Type.__name__ = "Integer32"
_RelayWarningLinkChanged_Object = MibTableColumn
relayWarningLinkChanged = _RelayWarningLinkChanged_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 17, 12, 1, 1),
    _RelayWarningLinkChanged_Type()
)
relayWarningLinkChanged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayWarningLinkChanged.setStatus("current")


class _RelayWarningLinkChangedStatus_Type(Integer32):
    """Custom type relayWarningLinkChangedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-triggered", 0),
          ("triggered", 1))
    )


_RelayWarningLinkChangedStatus_Type.__name__ = "Integer32"
_RelayWarningLinkChangedStatus_Object = MibTableColumn
relayWarningLinkChangedStatus = _RelayWarningLinkChangedStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 17, 12, 1, 2),
    _RelayWarningLinkChangedStatus_Type()
)
relayWarningLinkChangedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relayWarningLinkChangedStatus.setStatus("current")


class _RelayWarningTrafficOverload_Type(Integer32):
    """Custom type relayWarningTrafficOverload based on Integer32"""
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


_RelayWarningTrafficOverload_Type.__name__ = "Integer32"
_RelayWarningTrafficOverload_Object = MibTableColumn
relayWarningTrafficOverload = _RelayWarningTrafficOverload_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 17, 12, 1, 3),
    _RelayWarningTrafficOverload_Type()
)
relayWarningTrafficOverload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayWarningTrafficOverload.setStatus("current")


class _RelayWarningTrafficOverloadStatus_Type(Integer32):
    """Custom type relayWarningTrafficOverloadStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-triggered", 0),
          ("triggered", 1))
    )


_RelayWarningTrafficOverloadStatus_Type.__name__ = "Integer32"
_RelayWarningTrafficOverloadStatus_Object = MibTableColumn
relayWarningTrafficOverloadStatus = _RelayWarningTrafficOverloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 17, 12, 1, 4),
    _RelayWarningTrafficOverloadStatus_Type()
)
relayWarningTrafficOverloadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relayWarningTrafficOverloadStatus.setStatus("current")
_RelayWarningRxTrafficThreshold_Type = Integer32
_RelayWarningRxTrafficThreshold_Object = MibTableColumn
relayWarningRxTrafficThreshold = _RelayWarningRxTrafficThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 17, 12, 1, 5),
    _RelayWarningRxTrafficThreshold_Type()
)
relayWarningRxTrafficThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayWarningRxTrafficThreshold.setStatus("current")
_RelayWarningTrafficDuration_Type = Integer32
_RelayWarningTrafficDuration_Object = MibTableColumn
relayWarningTrafficDuration = _RelayWarningTrafficDuration_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 17, 12, 1, 6),
    _RelayWarningTrafficDuration_Type()
)
relayWarningTrafficDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayWarningTrafficDuration.setStatus("current")
_DiRelayWarningTable_Object = MibTable
diRelayWarningTable = _DiRelayWarningTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 17, 13)
)
if mibBuilder.loadTexts:
    diRelayWarningTable.setStatus("current")
_DiRelayWarningEntry_Object = MibTableRow
diRelayWarningEntry = _DiRelayWarningEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 17, 13, 1)
)
diRelayWarningEntry.setIndexNames(
    (0, "MOXA-EDSP506E-MIB", "diIndex"),
    (0, "MOXA-EDSP506E-MIB", "relayAlarmIndex"),
)
if mibBuilder.loadTexts:
    diRelayWarningEntry.setStatus("current")


class _RelayWarningDiInputChanged_Type(Integer32):
    """Custom type relayWarningDiInputChanged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("off", 1),
          ("on", 2))
    )


_RelayWarningDiInputChanged_Type.__name__ = "Integer32"
_RelayWarningDiInputChanged_Object = MibTableColumn
relayWarningDiInputChanged = _RelayWarningDiInputChanged_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 17, 13, 1, 1),
    _RelayWarningDiInputChanged_Type()
)
relayWarningDiInputChanged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayWarningDiInputChanged.setStatus("current")


class _RelayWarningDiInputChangedStatus_Type(Integer32):
    """Custom type relayWarningDiInputChangedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-triggered", 0),
          ("triggered", 1))
    )


_RelayWarningDiInputChangedStatus_Type.__name__ = "Integer32"
_RelayWarningDiInputChangedStatus_Object = MibTableColumn
relayWarningDiInputChangedStatus = _RelayWarningDiInputChangedStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 17, 13, 1, 2),
    _RelayWarningDiInputChangedStatus_Type()
)
relayWarningDiInputChangedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relayWarningDiInputChangedStatus.setStatus("current")
_TrafficPrioritization_ObjectIdentity = ObjectIdentity
trafficPrioritization = _TrafficPrioritization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 18)
)
_QosClassification_ObjectIdentity = ObjectIdentity
qosClassification = _QosClassification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 18, 1)
)


class _SchedulingMechanism_Type(Integer32):
    """Custom type schedulingMechanism based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("schedweightfair", 0),
          ("schedstrict", 1))
    )


_SchedulingMechanism_Type.__name__ = "Integer32"
_SchedulingMechanism_Object = MibScalar
schedulingMechanism = _SchedulingMechanism_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 18, 1, 1),
    _SchedulingMechanism_Type()
)
schedulingMechanism.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schedulingMechanism.setStatus("current")
_QosPortTable_Object = MibTable
qosPortTable = _QosPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 18, 1, 2)
)
if mibBuilder.loadTexts:
    qosPortTable.setStatus("current")
_QosPortEntry_Object = MibTableRow
qosPortEntry = _QosPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 18, 1, 2, 1)
)
qosPortEntry.setIndexNames(
    (0, "MOXA-EDSP506E-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    qosPortEntry.setStatus("current")


class _DscpInspection_Type(Integer32):
    """Custom type dscpInspection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_DscpInspection_Type.__name__ = "Integer32"
_DscpInspection_Object = MibTableColumn
dscpInspection = _DscpInspection_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 18, 1, 2, 1, 1),
    _DscpInspection_Type()
)
dscpInspection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscpInspection.setStatus("current")


class _CosInspection_Type(Integer32):
    """Custom type cosInspection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_CosInspection_Type.__name__ = "Integer32"
_CosInspection_Object = MibTableColumn
cosInspection = _CosInspection_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 18, 1, 2, 1, 2),
    _CosInspection_Type()
)
cosInspection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cosInspection.setStatus("current")


class _PortPriority_Type(Integer32):
    """Custom type portPriority based on Integer32"""
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
        *(("priority0", 0),
          ("priority1", 1),
          ("priority2", 2),
          ("priority3", 3),
          ("priority4", 4),
          ("priority5", 5),
          ("priority6", 6),
          ("priority7", 7))
    )


_PortPriority_Type.__name__ = "Integer32"
_PortPriority_Object = MibTableColumn
portPriority = _PortPriority_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 18, 1, 2, 1, 3),
    _PortPriority_Type()
)
portPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portPriority.setStatus("current")
_PriorityMapping_ObjectIdentity = ObjectIdentity
priorityMapping = _PriorityMapping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 18, 2)
)
_PriorityMappingTable_Object = MibTable
priorityMappingTable = _PriorityMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 18, 2, 1)
)
if mibBuilder.loadTexts:
    priorityMappingTable.setStatus("current")
_PriorityMappingEntry_Object = MibTableRow
priorityMappingEntry = _PriorityMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 18, 2, 1, 1)
)
priorityMappingEntry.setIndexNames(
    (0, "MOXA-EDSP506E-MIB", "priorityTag"),
)
if mibBuilder.loadTexts:
    priorityMappingEntry.setStatus("current")


class _PriorityTag_Type(Integer32):
    """Custom type priorityTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PriorityTag_Type.__name__ = "Integer32"
_PriorityTag_Object = MibTableColumn
priorityTag = _PriorityTag_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 18, 2, 1, 1, 1),
    _PriorityTag_Type()
)
priorityTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    priorityTag.setStatus("current")


class _PriorityMappedQueue_Type(Integer32):
    """Custom type priorityMappedQueue based on Integer32"""
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
        *(("trafficclass0", 0),
          ("trafficclass1", 1),
          ("trafficclass2", 2),
          ("trafficclass3", 3))
    )


_PriorityMappedQueue_Type.__name__ = "Integer32"
_PriorityMappedQueue_Object = MibTableColumn
priorityMappedQueue = _PriorityMappedQueue_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 18, 2, 1, 1, 2),
    _PriorityMappedQueue_Type()
)
priorityMappedQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    priorityMappedQueue.setStatus("current")
_DscpMapping_ObjectIdentity = ObjectIdentity
dscpMapping = _DscpMapping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 18, 3)
)
_DscpMappingTable_Object = MibTable
dscpMappingTable = _DscpMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 18, 3, 1)
)
if mibBuilder.loadTexts:
    dscpMappingTable.setStatus("current")
_DscpMappingEntry_Object = MibTableRow
dscpMappingEntry = _DscpMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 18, 3, 1, 1)
)
dscpMappingEntry.setIndexNames(
    (0, "MOXA-EDSP506E-MIB", "dscpClass"),
)
if mibBuilder.loadTexts:
    dscpMappingEntry.setStatus("current")
_DscpClass_Type = Integer32
_DscpClass_Object = MibTableColumn
dscpClass = _DscpClass_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 18, 3, 1, 1, 1),
    _DscpClass_Type()
)
dscpClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dscpClass.setStatus("current")


class _DscpMappedPriority_Type(Integer32):
    """Custom type dscpMappedPriority based on Integer32"""
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
        *(("priority0", 0),
          ("priority1", 1),
          ("priority2", 2),
          ("priority3", 3),
          ("priority4", 4),
          ("priority5", 5),
          ("priority6", 6),
          ("priority7", 7))
    )


_DscpMappedPriority_Type.__name__ = "Integer32"
_DscpMappedPriority_Object = MibTableColumn
dscpMappedPriority = _DscpMappedPriority_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 18, 3, 1, 1, 2),
    _DscpMappedPriority_Type()
)
dscpMappedPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscpMappedPriority.setStatus("current")
_Vlan_ObjectIdentity = ObjectIdentity
vlan = _Vlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 19)
)
_VlanPortSettingTable_Object = MibTable
vlanPortSettingTable = _VlanPortSettingTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 19, 1)
)
if mibBuilder.loadTexts:
    vlanPortSettingTable.setStatus("current")
_VlanPortSettingEntry_Object = MibTableRow
vlanPortSettingEntry = _VlanPortSettingEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 19, 1, 1)
)
vlanPortSettingEntry.setIndexNames(
    (0, "MOXA-EDSP506E-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    vlanPortSettingEntry.setStatus("current")


class _PortVlanType_Type(Integer32):
    """Custom type portVlanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("access", 0),
          ("trunk", 1),
          ("hybrid", 2))
    )


_PortVlanType_Type.__name__ = "Integer32"
_PortVlanType_Object = MibTableColumn
portVlanType = _PortVlanType_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 19, 1, 1, 1),
    _PortVlanType_Type()
)
portVlanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portVlanType.setStatus("current")


class _PortDefaultVid_Type(Integer32):
    """Custom type portDefaultVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_PortDefaultVid_Type.__name__ = "Integer32"
_PortDefaultVid_Object = MibTableColumn
portDefaultVid = _PortDefaultVid_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 19, 1, 1, 2),
    _PortDefaultVid_Type()
)
portDefaultVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDefaultVid.setStatus("current")
_PortFixedVid_Type = DisplayString
_PortFixedVid_Object = MibTableColumn
portFixedVid = _PortFixedVid_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 19, 1, 1, 3),
    _PortFixedVid_Type()
)
portFixedVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portFixedVid.setStatus("current")
_PortForbiddenVid_Type = DisplayString
_PortForbiddenVid_Object = MibTableColumn
portForbiddenVid = _PortForbiddenVid_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 19, 1, 1, 4),
    _PortForbiddenVid_Type()
)
portForbiddenVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portForbiddenVid.setStatus("current")
_PortFixedVidUntag_Type = DisplayString
_PortFixedVidUntag_Object = MibTableColumn
portFixedVidUntag = _PortFixedVidUntag_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 19, 1, 1, 5),
    _PortFixedVidUntag_Type()
)
portFixedVidUntag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portFixedVidUntag.setStatus("current")
_VlanTable_Object = MibTable
vlanTable = _VlanTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 19, 2)
)
if mibBuilder.loadTexts:
    vlanTable.setStatus("current")
_VlanEntry_Object = MibTableRow
vlanEntry = _VlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 19, 2, 1)
)
vlanEntry.setIndexNames(
    (0, "MOXA-EDSP506E-MIB", "vlanId"),
)
if mibBuilder.loadTexts:
    vlanEntry.setStatus("current")


class _VlanId_Type(Integer32):
    """Custom type vlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_VlanId_Type.__name__ = "Integer32"
_VlanId_Object = MibTableColumn
vlanId = _VlanId_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 19, 2, 1, 1),
    _VlanId_Type()
)
vlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanId.setStatus("current")
_JoinedAccessPorts_Type = PortList
_JoinedAccessPorts_Object = MibTableColumn
joinedAccessPorts = _JoinedAccessPorts_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 19, 2, 1, 2),
    _JoinedAccessPorts_Type()
)
joinedAccessPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    joinedAccessPorts.setStatus("current")
_JoinedTrunkPorts_Type = PortList
_JoinedTrunkPorts_Object = MibTableColumn
joinedTrunkPorts = _JoinedTrunkPorts_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 19, 2, 1, 3),
    _JoinedTrunkPorts_Type()
)
joinedTrunkPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    joinedTrunkPorts.setStatus("current")
_JoinedHybridPorts_Type = PortList
_JoinedHybridPorts_Object = MibTableColumn
joinedHybridPorts = _JoinedHybridPorts_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 19, 2, 1, 4),
    _JoinedHybridPorts_Type()
)
joinedHybridPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    joinedHybridPorts.setStatus("current")
_VlanName_Type = DisplayString
_VlanName_Object = MibTableColumn
vlanName = _VlanName_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 19, 2, 1, 5),
    _VlanName_Type()
)
vlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanName.setStatus("current")
_ManagementVlanId_Type = Integer32
_ManagementVlanId_Object = MibScalar
managementVlanId = _ManagementVlanId_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 19, 3),
    _ManagementVlanId_Type()
)
managementVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managementVlanId.setStatus("current")


class _VlanType_Type(Integer32):
    """Custom type vlanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("tagBased", 0),
          ("portBased", 1))
    )


_VlanType_Type.__name__ = "Integer32"
_VlanType_Object = MibScalar
vlanType = _VlanType_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 19, 4),
    _VlanType_Type()
)
vlanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanType.setStatus("current")
_PortbaseVlanSettingTable_Object = MibTable
portbaseVlanSettingTable = _PortbaseVlanSettingTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 19, 5)
)
if mibBuilder.loadTexts:
    portbaseVlanSettingTable.setStatus("current")
_PortbaseVlanSettingEntry_Object = MibTableRow
portbaseVlanSettingEntry = _PortbaseVlanSettingEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 19, 5, 1)
)
portbaseVlanSettingEntry.setIndexNames(
    (0, "MOXA-EDSP506E-MIB", "portbaseVlanSettingIndex"),
)
if mibBuilder.loadTexts:
    portbaseVlanSettingEntry.setStatus("current")
_PortbaseVlanSettingIndex_Type = Integer32
_PortbaseVlanSettingIndex_Object = MibTableColumn
portbaseVlanSettingIndex = _PortbaseVlanSettingIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 19, 5, 1, 1),
    _PortbaseVlanSettingIndex_Type()
)
portbaseVlanSettingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portbaseVlanSettingIndex.setStatus("current")
_PortbaseVlanMemberPorts_Type = PortList
_PortbaseVlanMemberPorts_Object = MibTableColumn
portbaseVlanMemberPorts = _PortbaseVlanMemberPorts_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 19, 5, 1, 2),
    _PortbaseVlanMemberPorts_Type()
)
portbaseVlanMemberPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portbaseVlanMemberPorts.setStatus("current")


class _EnableGvrp_Type(Integer32):
    """Custom type enableGvrp based on Integer32"""
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


_EnableGvrp_Type.__name__ = "Integer32"
_EnableGvrp_Object = MibScalar
enableGvrp = _EnableGvrp_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 19, 6),
    _EnableGvrp_Type()
)
enableGvrp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableGvrp.setStatus("current")
_MulticastFiltering_ObjectIdentity = ObjectIdentity
multicastFiltering = _MulticastFiltering_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 20)
)
_IgmpSnooping_ObjectIdentity = ObjectIdentity
igmpSnooping = _IgmpSnooping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 20, 1)
)


class _QuerierQueryInterval_Type(Integer32):
    """Custom type querierQueryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 600),
    )


_QuerierQueryInterval_Type.__name__ = "Integer32"
_QuerierQueryInterval_Object = MibScalar
querierQueryInterval = _QuerierQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 20, 1, 1),
    _QuerierQueryInterval_Type()
)
querierQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    querierQueryInterval.setStatus("current")
_IgmpSnoopingSettingTable_Object = MibTable
igmpSnoopingSettingTable = _IgmpSnoopingSettingTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 20, 1, 2)
)
if mibBuilder.loadTexts:
    igmpSnoopingSettingTable.setStatus("current")
_IgmpSnoopingSettingEntry_Object = MibTableRow
igmpSnoopingSettingEntry = _IgmpSnoopingSettingEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 20, 1, 2, 1)
)
igmpSnoopingSettingEntry.setIndexNames(
    (0, "MOXA-EDSP506E-MIB", "vlanId"),
)
if mibBuilder.loadTexts:
    igmpSnoopingSettingEntry.setStatus("current")


class _EnableIgmpSnooping_Type(Integer32):
    """Custom type enableIgmpSnooping based on Integer32"""
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


_EnableIgmpSnooping_Type.__name__ = "Integer32"
_EnableIgmpSnooping_Object = MibTableColumn
enableIgmpSnooping = _EnableIgmpSnooping_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 20, 1, 2, 1, 1),
    _EnableIgmpSnooping_Type()
)
enableIgmpSnooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableIgmpSnooping.setStatus("current")


class _EnableQuerier_Type(Integer32):
    """Custom type enableQuerier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("igmpv2", 1),
          ("igmpv3", 2))
    )


_EnableQuerier_Type.__name__ = "Integer32"
_EnableQuerier_Object = MibTableColumn
enableQuerier = _EnableQuerier_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 20, 1, 2, 1, 2),
    _EnableQuerier_Type()
)
enableQuerier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableQuerier.setStatus("current")
_FixedMulticastQuerierPorts_Type = PortList
_FixedMulticastQuerierPorts_Object = MibTableColumn
fixedMulticastQuerierPorts = _FixedMulticastQuerierPorts_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 20, 1, 2, 1, 3),
    _FixedMulticastQuerierPorts_Type()
)
fixedMulticastQuerierPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fixedMulticastQuerierPorts.setStatus("current")
_LearnedMulticastQuerierPorts_Type = PortList
_LearnedMulticastQuerierPorts_Object = MibTableColumn
learnedMulticastQuerierPorts = _LearnedMulticastQuerierPorts_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 20, 1, 2, 1, 4),
    _LearnedMulticastQuerierPorts_Type()
)
learnedMulticastQuerierPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    learnedMulticastQuerierPorts.setStatus("current")


class _EnableGlobalIgmpSnooping_Type(Integer32):
    """Custom type enableGlobalIgmpSnooping based on Integer32"""
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


_EnableGlobalIgmpSnooping_Type.__name__ = "Integer32"
_EnableGlobalIgmpSnooping_Object = MibScalar
enableGlobalIgmpSnooping = _EnableGlobalIgmpSnooping_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 20, 1, 4),
    _EnableGlobalIgmpSnooping_Type()
)
enableGlobalIgmpSnooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableGlobalIgmpSnooping.setStatus("current")


class _MulticastFastForwarding_Type(Integer32):
    """Custom type multicastFastForwarding based on Integer32"""
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


_MulticastFastForwarding_Type.__name__ = "Integer32"
_MulticastFastForwarding_Object = MibScalar
multicastFastForwarding = _MulticastFastForwarding_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 20, 1, 7),
    _MulticastFastForwarding_Type()
)
multicastFastForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastFastForwarding.setStatus("current")
_StaticMulticast_ObjectIdentity = ObjectIdentity
staticMulticast = _StaticMulticast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 20, 2)
)
_StaticMulticastTable_Object = MibTable
staticMulticastTable = _StaticMulticastTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 20, 2, 1)
)
if mibBuilder.loadTexts:
    staticMulticastTable.setStatus("current")
_StaticMulticastEntry_Object = MibTableRow
staticMulticastEntry = _StaticMulticastEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 20, 2, 1, 1)
)
staticMulticastEntry.setIndexNames(
    (0, "MOXA-EDSP506E-MIB", "staticMulticastAddress"),
)
if mibBuilder.loadTexts:
    staticMulticastEntry.setStatus("current")
_StaticMulticastAddress_Type = MacAddress
_StaticMulticastAddress_Object = MibTableColumn
staticMulticastAddress = _StaticMulticastAddress_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 20, 2, 1, 1, 1),
    _StaticMulticastAddress_Type()
)
staticMulticastAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    staticMulticastAddress.setStatus("current")
_StaticMulticastPorts_Type = PortList
_StaticMulticastPorts_Object = MibTableColumn
staticMulticastPorts = _StaticMulticastPorts_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 20, 2, 1, 1, 2),
    _StaticMulticastPorts_Type()
)
staticMulticastPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    staticMulticastPorts.setStatus("current")


class _StaticMulticastStatus_Type(Integer32):
    """Custom type staticMulticastStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6))
    )


_StaticMulticastStatus_Type.__name__ = "Integer32"
_StaticMulticastStatus_Object = MibTableColumn
staticMulticastStatus = _StaticMulticastStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 20, 2, 1, 1, 3),
    _StaticMulticastStatus_Type()
)
staticMulticastStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    staticMulticastStatus.setStatus("current")
_Gmrp_ObjectIdentity = ObjectIdentity
gmrp = _Gmrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 20, 3)
)
_GmrpSettingTable_Object = MibTable
gmrpSettingTable = _GmrpSettingTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 20, 3, 1)
)
if mibBuilder.loadTexts:
    gmrpSettingTable.setStatus("current")
_GmrpSettingEntry_Object = MibTableRow
gmrpSettingEntry = _GmrpSettingEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 20, 3, 1, 1)
)
gmrpSettingEntry.setIndexNames(
    (0, "MOXA-EDSP506E-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    gmrpSettingEntry.setStatus("current")


class _EnableGMRP_Type(Integer32):
    """Custom type enableGMRP based on Integer32"""
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


_EnableGMRP_Type.__name__ = "Integer32"
_EnableGMRP_Object = MibTableColumn
enableGMRP = _EnableGMRP_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 20, 3, 1, 1, 1),
    _EnableGMRP_Type()
)
enableGMRP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableGMRP.setStatus("current")
_GmrpTable_Object = MibTable
gmrpTable = _GmrpTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 20, 3, 2)
)
if mibBuilder.loadTexts:
    gmrpTable.setStatus("current")
_GmrpEntry_Object = MibTableRow
gmrpEntry = _GmrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 20, 3, 2, 1)
)
gmrpEntry.setIndexNames(
    (0, "MOXA-EDSP506E-MIB", "gmrpMulticastGroup"),
)
if mibBuilder.loadTexts:
    gmrpEntry.setStatus("current")
_GmrpMulticastGroup_Type = MacAddress
_GmrpMulticastGroup_Object = MibTableColumn
gmrpMulticastGroup = _GmrpMulticastGroup_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 20, 3, 2, 1, 1),
    _GmrpMulticastGroup_Type()
)
gmrpMulticastGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmrpMulticastGroup.setStatus("current")
_GmrpFixedPorts_Type = PortList
_GmrpFixedPorts_Object = MibTableColumn
gmrpFixedPorts = _GmrpFixedPorts_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 20, 3, 2, 1, 2),
    _GmrpFixedPorts_Type()
)
gmrpFixedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmrpFixedPorts.setStatus("current")
_GmrpLearnedPorts_Type = PortList
_GmrpLearnedPorts_Object = MibTableColumn
gmrpLearnedPorts = _GmrpLearnedPorts_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 20, 3, 2, 1, 3),
    _GmrpLearnedPorts_Type()
)
gmrpLearnedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmrpLearnedPorts.setStatus("current")
_Mfb_ObjectIdentity = ObjectIdentity
mfb = _Mfb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 20, 4)
)
_MfbSettingTable_Object = MibTable
mfbSettingTable = _MfbSettingTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 20, 4, 1)
)
if mibBuilder.loadTexts:
    mfbSettingTable.setStatus("current")
_MfbSettingEntry_Object = MibTableRow
mfbSettingEntry = _MfbSettingEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 20, 4, 1, 1)
)
mfbSettingEntry.setIndexNames(
    (0, "MOXA-EDSP506E-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    mfbSettingEntry.setStatus("current")


class _FilterBehavior_Type(Integer32):
    """Custom type filterBehavior based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("forwardUnknown", 2),
          ("filterUnknown", 3))
    )


_FilterBehavior_Type.__name__ = "Integer32"
_FilterBehavior_Object = MibTableColumn
filterBehavior = _FilterBehavior_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 20, 4, 1, 1, 1),
    _FilterBehavior_Type()
)
filterBehavior.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterBehavior.setStatus("current")
_RateLimiting_ObjectIdentity = ObjectIdentity
rateLimiting = _RateLimiting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 21)
)
_DroppacketModeRateLimitingIngressTable_Object = MibTable
droppacketModeRateLimitingIngressTable = _DroppacketModeRateLimitingIngressTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 21, 1)
)
if mibBuilder.loadTexts:
    droppacketModeRateLimitingIngressTable.setStatus("current")
_DroppacketModeRateLimitingIngressEntry_Object = MibTableRow
droppacketModeRateLimitingIngressEntry = _DroppacketModeRateLimitingIngressEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 21, 1, 1)
)
droppacketModeRateLimitingIngressEntry.setIndexNames(
    (0, "MOXA-EDSP506E-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    droppacketModeRateLimitingIngressEntry.setStatus("current")


class _IngressLimitRate_Type(Integer32):
    """Custom type ingressLimitRate based on Integer32"""
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
        *(("notlimited", 0),
          ("percentage03", 1),
          ("percentage05", 2),
          ("percentage10", 3),
          ("percentage15", 4),
          ("percentage25", 5),
          ("percentage35", 6),
          ("percentage50", 7),
          ("percentage65", 8),
          ("percentage85", 9))
    )


_IngressLimitRate_Type.__name__ = "Integer32"
_IngressLimitRate_Object = MibTableColumn
ingressLimitRate = _IngressLimitRate_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 21, 1, 1, 1),
    _IngressLimitRate_Type()
)
ingressLimitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ingressLimitRate.setStatus("current")


class _EgressLimitRate_Type(Integer32):
    """Custom type egressLimitRate based on Integer32"""
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
        *(("notlimited", 0),
          ("percentage03", 1),
          ("percentage05", 2),
          ("percentage10", 3),
          ("percentage15", 4),
          ("percentage25", 5),
          ("percentage35", 6),
          ("percentage50", 7),
          ("percentage65", 8),
          ("percentage85", 9))
    )


_EgressLimitRate_Type.__name__ = "Integer32"
_EgressLimitRate_Object = MibTableColumn
egressLimitRate = _EgressLimitRate_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 21, 1, 1, 2),
    _EgressLimitRate_Type()
)
egressLimitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    egressLimitRate.setStatus("current")
_BroadcastStormProtection_ObjectIdentity = ObjectIdentity
broadcastStormProtection = _BroadcastStormProtection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 21, 2)
)


class _BcastStormProtection_Type(Integer32):
    """Custom type bcastStormProtection based on Integer32"""
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


_BcastStormProtection_Type.__name__ = "Integer32"
_BcastStormProtection_Object = MibScalar
bcastStormProtection = _BcastStormProtection_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 21, 2, 1),
    _BcastStormProtection_Type()
)
bcastStormProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcastStormProtection.setStatus("current")


class _BcastStormProtectionIncludeMcast_Type(Integer32):
    """Custom type bcastStormProtectionIncludeMcast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_BcastStormProtectionIncludeMcast_Type.__name__ = "Integer32"
_BcastStormProtectionIncludeMcast_Object = MibScalar
bcastStormProtectionIncludeMcast = _BcastStormProtectionIncludeMcast_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 21, 2, 2),
    _BcastStormProtectionIncludeMcast_Type()
)
bcastStormProtectionIncludeMcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcastStormProtectionIncludeMcast.setStatus("current")


class _BcastStormProtectionIncludeUcast_Type(Integer32):
    """Custom type bcastStormProtectionIncludeUcast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_BcastStormProtectionIncludeUcast_Type.__name__ = "Integer32"
_BcastStormProtectionIncludeUcast_Object = MibScalar
bcastStormProtectionIncludeUcast = _BcastStormProtectionIncludeUcast_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 21, 2, 3),
    _BcastStormProtectionIncludeUcast_Type()
)
bcastStormProtectionIncludeUcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcastStormProtectionIncludeUcast.setStatus("current")
_PortDisableMode_ObjectIdentity = ObjectIdentity
portDisableMode = _PortDisableMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 21, 3)
)


class _PortDisableModePeriod_Type(Integer32):
    """Custom type portDisableModePeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PortDisableModePeriod_Type.__name__ = "Integer32"
_PortDisableModePeriod_Object = MibScalar
portDisableModePeriod = _PortDisableModePeriod_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 21, 3, 1),
    _PortDisableModePeriod_Type()
)
portDisableModePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDisableModePeriod.setStatus("current")
_PortDisableModeTable_Object = MibTable
portDisableModeTable = _PortDisableModeTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 21, 3, 2)
)
if mibBuilder.loadTexts:
    portDisableModeTable.setStatus("current")
_PortDisableModeEntry_Object = MibTableRow
portDisableModeEntry = _PortDisableModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 21, 3, 2, 1)
)
portDisableModeEntry.setIndexNames(
    (0, "MOXA-EDSP506E-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    portDisableModeEntry.setStatus("current")


class _IngressLimit_Type(Integer32):
    """Custom type ingressLimit based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("notlimited", 0),
          ("rateMega1Fps4464", 1),
          ("rateMega2Fps7441", 2),
          ("rateMega3Fps14881", 3),
          ("rateMega4Fps22322", 4),
          ("rateMega5Fps37203", 5),
          ("rateMega6Fps52084", 6),
          ("rateMega7Fps74405", 7),
          ("rateGiga1Fps44640", 8),
          ("rateGiga2Fps74410", 9),
          ("rateGiga3Fps148810", 10),
          ("rateGiga4Fps223220", 11),
          ("rateGiga5Fps372030", 12),
          ("rateGiga6Fps520840", 13),
          ("rateGiga7Fps744050", 14))
    )


_IngressLimit_Type.__name__ = "Integer32"
_IngressLimit_Object = MibTableColumn
ingressLimit = _IngressLimit_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 21, 3, 2, 1, 1),
    _IngressLimit_Type()
)
ingressLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ingressLimit.setStatus("current")


class _RateLimitingAction_Type(Integer32):
    """Custom type rateLimitingAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("droppacket", 0),
          ("portDisable", 1))
    )


_RateLimitingAction_Type.__name__ = "Integer32"
_RateLimitingAction_Object = MibScalar
rateLimitingAction = _RateLimitingAction_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 21, 4),
    _RateLimitingAction_Type()
)
rateLimitingAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rateLimitingAction.setStatus("current")
_Security_ObjectIdentity = ObjectIdentity
security = _Security_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22)
)
_UserLoginSetting_ObjectIdentity = ObjectIdentity
userLoginSetting = _UserLoginSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 1)
)


class _UserLoginServer_Type(Integer32):
    """Custom type userLoginServer based on Integer32"""
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
        *(("tacacsLocal", 1),
          ("radiusLocal", 2),
          ("tacacs", 3),
          ("radius", 4),
          ("local", 5))
    )


_UserLoginServer_Type.__name__ = "Integer32"
_UserLoginServer_Object = MibScalar
userLoginServer = _UserLoginServer_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 1, 1),
    _UserLoginServer_Type()
)
userLoginServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userLoginServer.setStatus("current")
_TacacsServerSetting_ObjectIdentity = ObjectIdentity
tacacsServerSetting = _TacacsServerSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 1, 2)
)
_TacacsLoginAuthServer_Type = DisplayString
_TacacsLoginAuthServer_Object = MibScalar
tacacsLoginAuthServer = _TacacsLoginAuthServer_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 1, 2, 1),
    _TacacsLoginAuthServer_Type()
)
tacacsLoginAuthServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsLoginAuthServer.setStatus("current")


class _TacacsLoginAuthPort_Type(Integer32):
    """Custom type tacacsLoginAuthPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TacacsLoginAuthPort_Type.__name__ = "Integer32"
_TacacsLoginAuthPort_Object = MibScalar
tacacsLoginAuthPort = _TacacsLoginAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 1, 2, 2),
    _TacacsLoginAuthPort_Type()
)
tacacsLoginAuthPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsLoginAuthPort.setStatus("current")
_TacacsLoginAuthSharedKey_Type = DisplayString
_TacacsLoginAuthSharedKey_Object = MibScalar
tacacsLoginAuthSharedKey = _TacacsLoginAuthSharedKey_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 1, 2, 3),
    _TacacsLoginAuthSharedKey_Type()
)
tacacsLoginAuthSharedKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsLoginAuthSharedKey.setStatus("current")


class _TacacsLoginAuthAuthType_Type(Integer32):
    """Custom type tacacsLoginAuthAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 0),
          ("pap", 1),
          ("chap", 2),
          ("mschap", 4))
    )


_TacacsLoginAuthAuthType_Type.__name__ = "Integer32"
_TacacsLoginAuthAuthType_Object = MibScalar
tacacsLoginAuthAuthType = _TacacsLoginAuthAuthType_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 1, 2, 4),
    _TacacsLoginAuthAuthType_Type()
)
tacacsLoginAuthAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsLoginAuthAuthType.setStatus("current")


class _TacacsLoginAuthTimeout_Type(Integer32):
    """Custom type tacacsLoginAuthTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TacacsLoginAuthTimeout_Type.__name__ = "Integer32"
_TacacsLoginAuthTimeout_Object = MibScalar
tacacsLoginAuthTimeout = _TacacsLoginAuthTimeout_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 1, 2, 5),
    _TacacsLoginAuthTimeout_Type()
)
tacacsLoginAuthTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsLoginAuthTimeout.setStatus("current")
_RadiusServerSetting_ObjectIdentity = ObjectIdentity
radiusServerSetting = _RadiusServerSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 1, 3)
)
_RadiusLoginAuthServer_Type = DisplayString
_RadiusLoginAuthServer_Object = MibScalar
radiusLoginAuthServer = _RadiusLoginAuthServer_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 1, 3, 1),
    _RadiusLoginAuthServer_Type()
)
radiusLoginAuthServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusLoginAuthServer.setStatus("current")


class _RadiusLoginAuthPort_Type(Integer32):
    """Custom type radiusLoginAuthPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RadiusLoginAuthPort_Type.__name__ = "Integer32"
_RadiusLoginAuthPort_Object = MibScalar
radiusLoginAuthPort = _RadiusLoginAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 1, 3, 2),
    _RadiusLoginAuthPort_Type()
)
radiusLoginAuthPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusLoginAuthPort.setStatus("current")
_RadiusLoginAuthSharedKey_Type = DisplayString
_RadiusLoginAuthSharedKey_Object = MibScalar
radiusLoginAuthSharedKey = _RadiusLoginAuthSharedKey_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 1, 3, 3),
    _RadiusLoginAuthSharedKey_Type()
)
radiusLoginAuthSharedKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusLoginAuthSharedKey.setStatus("current")


class _RadiusLoginAuthAuthType_Type(Integer32):
    """Custom type radiusLoginAuthAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("pap", 0),
          ("chap", 1))
    )


_RadiusLoginAuthAuthType_Type.__name__ = "Integer32"
_RadiusLoginAuthAuthType_Object = MibScalar
radiusLoginAuthAuthType = _RadiusLoginAuthAuthType_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 1, 3, 4),
    _RadiusLoginAuthAuthType_Type()
)
radiusLoginAuthAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusLoginAuthAuthType.setStatus("current")


class _RadiusLoginAuthTimeout_Type(Integer32):
    """Custom type radiusLoginAuthTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RadiusLoginAuthTimeout_Type.__name__ = "Integer32"
_RadiusLoginAuthTimeout_Object = MibScalar
radiusLoginAuthTimeout = _RadiusLoginAuthTimeout_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 1, 3, 5),
    _RadiusLoginAuthTimeout_Type()
)
radiusLoginAuthTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusLoginAuthTimeout.setStatus("current")
_PortAccessControl_ObjectIdentity = ObjectIdentity
portAccessControl = _PortAccessControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 2)
)
_StaticPortLockLegacy_ObjectIdentity = ObjectIdentity
staticPortLockLegacy = _StaticPortLockLegacy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 2, 1)
)
_StaticPortLockLegacyAddress_Type = MacAddress
_StaticPortLockLegacyAddress_Object = MibScalar
staticPortLockLegacyAddress = _StaticPortLockLegacyAddress_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 2, 1, 1),
    _StaticPortLockLegacyAddress_Type()
)
staticPortLockLegacyAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    staticPortLockLegacyAddress.setStatus("current")
_StaticPortLockLegacyPort_Type = Integer32
_StaticPortLockLegacyPort_Object = MibScalar
staticPortLockLegacyPort = _StaticPortLockLegacyPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 2, 1, 2),
    _StaticPortLockLegacyPort_Type()
)
staticPortLockLegacyPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    staticPortLockLegacyPort.setStatus("current")


class _StaticPortLockLegacyStatus_Type(Integer32):
    """Custom type staticPortLockLegacyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4))
    )


_StaticPortLockLegacyStatus_Type.__name__ = "Integer32"
_StaticPortLockLegacyStatus_Object = MibScalar
staticPortLockLegacyStatus = _StaticPortLockLegacyStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 2, 1, 3),
    _StaticPortLockLegacyStatus_Type()
)
staticPortLockLegacyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    staticPortLockLegacyStatus.setStatus("current")
_Dot1x_ObjectIdentity = ObjectIdentity
dot1x = _Dot1x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 2, 2)
)


class _DataBaseOption_Type(Integer32):
    """Custom type dataBaseOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("radius", 2),
          ("radiuslocal", 3))
    )


_DataBaseOption_Type.__name__ = "Integer32"
_DataBaseOption_Object = MibScalar
dataBaseOption = _DataBaseOption_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 2, 2, 1),
    _DataBaseOption_Type()
)
dataBaseOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataBaseOption.setStatus("current")


class _Dot1xReauthEnable_Type(Integer32):
    """Custom type dot1xReauthEnable based on Integer32"""
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


_Dot1xReauthEnable_Type.__name__ = "Integer32"
_Dot1xReauthEnable_Object = MibScalar
dot1xReauthEnable = _Dot1xReauthEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 2, 2, 5),
    _Dot1xReauthEnable_Type()
)
dot1xReauthEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xReauthEnable.setStatus("current")


class _Dot1xReauthPeriod_Type(Integer32):
    """Custom type dot1xReauthPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_Dot1xReauthPeriod_Type.__name__ = "Integer32"
_Dot1xReauthPeriod_Object = MibScalar
dot1xReauthPeriod = _Dot1xReauthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 2, 2, 6),
    _Dot1xReauthPeriod_Type()
)
dot1xReauthPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xReauthPeriod.setStatus("current")
_Dot1xSettingTable_Object = MibTable
dot1xSettingTable = _Dot1xSettingTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 2, 2, 7)
)
if mibBuilder.loadTexts:
    dot1xSettingTable.setStatus("current")
_Dot1xSettingEntry_Object = MibTableRow
dot1xSettingEntry = _Dot1xSettingEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 2, 2, 7, 1)
)
dot1xSettingEntry.setIndexNames(
    (0, "MOXA-EDSP506E-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    dot1xSettingEntry.setStatus("current")


class _EnableDot1X_Type(Integer32):
    """Custom type enableDot1X based on Integer32"""
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


_EnableDot1X_Type.__name__ = "Integer32"
_EnableDot1X_Object = MibTableColumn
enableDot1X = _EnableDot1X_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 2, 2, 7, 1, 1),
    _EnableDot1X_Type()
)
enableDot1X.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableDot1X.setStatus("current")
_Dot1xReauthTable_Object = MibTable
dot1xReauthTable = _Dot1xReauthTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 2, 2, 8)
)
if mibBuilder.loadTexts:
    dot1xReauthTable.setStatus("current")
_Dot1xReauthEntry_Object = MibTableRow
dot1xReauthEntry = _Dot1xReauthEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 2, 2, 8, 1)
)
dot1xReauthEntry.setIndexNames(
    (0, "MOXA-EDSP506E-MIB", "dot1xReauthPortIndex"),
)
if mibBuilder.loadTexts:
    dot1xReauthEntry.setStatus("current")
_Dot1xReauthPortIndex_Type = Integer32
_Dot1xReauthPortIndex_Object = MibTableColumn
dot1xReauthPortIndex = _Dot1xReauthPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 2, 2, 8, 1, 1),
    _Dot1xReauthPortIndex_Type()
)
dot1xReauthPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xReauthPortIndex.setStatus("current")


class _Dot1xReauth_Type(Integer32):
    """Custom type dot1xReauth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Dot1xReauth_Type.__name__ = "Integer32"
_Dot1xReauth_Object = MibTableColumn
dot1xReauth = _Dot1xReauth_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 2, 2, 8, 1, 2),
    _Dot1xReauth_Type()
)
dot1xReauth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xReauth.setStatus("current")
_Dot1xRadius_ObjectIdentity = ObjectIdentity
dot1xRadius = _Dot1xRadius_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 2, 2, 9)
)


class _Dot1xSameAsAuthServer_Type(Integer32):
    """Custom type dot1xSameAsAuthServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notSame", 0),
          ("same", 1))
    )


_Dot1xSameAsAuthServer_Type.__name__ = "Integer32"
_Dot1xSameAsAuthServer_Object = MibScalar
dot1xSameAsAuthServer = _Dot1xSameAsAuthServer_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 2, 2, 9, 1),
    _Dot1xSameAsAuthServer_Type()
)
dot1xSameAsAuthServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xSameAsAuthServer.setStatus("current")
_Dot1x1stRadiusServer_Type = DisplayString
_Dot1x1stRadiusServer_Object = MibScalar
dot1x1stRadiusServer = _Dot1x1stRadiusServer_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 2, 2, 9, 2),
    _Dot1x1stRadiusServer_Type()
)
dot1x1stRadiusServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1x1stRadiusServer.setStatus("current")


class _Dot1x1stRadiusPort_Type(Integer32):
    """Custom type dot1x1stRadiusPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dot1x1stRadiusPort_Type.__name__ = "Integer32"
_Dot1x1stRadiusPort_Object = MibScalar
dot1x1stRadiusPort = _Dot1x1stRadiusPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 2, 2, 9, 3),
    _Dot1x1stRadiusPort_Type()
)
dot1x1stRadiusPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1x1stRadiusPort.setStatus("current")
_Dot1x1stRadiusSharedKey_Type = DisplayString
_Dot1x1stRadiusSharedKey_Object = MibScalar
dot1x1stRadiusSharedKey = _Dot1x1stRadiusSharedKey_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 2, 2, 9, 4),
    _Dot1x1stRadiusSharedKey_Type()
)
dot1x1stRadiusSharedKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1x1stRadiusSharedKey.setStatus("current")
_Dot1x2ndRadiusServer_Type = DisplayString
_Dot1x2ndRadiusServer_Object = MibScalar
dot1x2ndRadiusServer = _Dot1x2ndRadiusServer_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 2, 2, 9, 5),
    _Dot1x2ndRadiusServer_Type()
)
dot1x2ndRadiusServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1x2ndRadiusServer.setStatus("current")


class _Dot1x2ndRadiusPort_Type(Integer32):
    """Custom type dot1x2ndRadiusPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dot1x2ndRadiusPort_Type.__name__ = "Integer32"
_Dot1x2ndRadiusPort_Object = MibScalar
dot1x2ndRadiusPort = _Dot1x2ndRadiusPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 2, 2, 9, 6),
    _Dot1x2ndRadiusPort_Type()
)
dot1x2ndRadiusPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1x2ndRadiusPort.setStatus("current")
_Dot1x2ndRadiusSharedKey_Type = DisplayString
_Dot1x2ndRadiusSharedKey_Object = MibScalar
dot1x2ndRadiusSharedKey = _Dot1x2ndRadiusSharedKey_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 2, 2, 9, 7),
    _Dot1x2ndRadiusSharedKey_Type()
)
dot1x2ndRadiusSharedKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1x2ndRadiusSharedKey.setStatus("current")
_PortAccessControlTable_Object = MibTable
portAccessControlTable = _PortAccessControlTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 2, 3)
)
if mibBuilder.loadTexts:
    portAccessControlTable.setStatus("current")
_PortAccessControlEntry_Object = MibTableRow
portAccessControlEntry = _PortAccessControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 2, 3, 1)
)
portAccessControlEntry.setIndexNames(
    (0, "MOXA-EDSP506E-MIB", "portAccessControlAddress"),
    (0, "MOXA-EDSP506E-MIB", "portAccessControlVid"),
)
if mibBuilder.loadTexts:
    portAccessControlEntry.setStatus("current")
_PortAccessControlAddress_Type = MacAddress
_PortAccessControlAddress_Object = MibTableColumn
portAccessControlAddress = _PortAccessControlAddress_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 2, 3, 1, 1),
    _PortAccessControlAddress_Type()
)
portAccessControlAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portAccessControlAddress.setStatus("current")
_PortAccessControlPortNo_Type = Integer32
_PortAccessControlPortNo_Object = MibTableColumn
portAccessControlPortNo = _PortAccessControlPortNo_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 2, 3, 1, 2),
    _PortAccessControlPortNo_Type()
)
portAccessControlPortNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portAccessControlPortNo.setStatus("current")


class _PortAccessControlAccessStatus_Type(Integer32):
    """Custom type portAccessControlAccessStatus based on Integer32"""
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
        *(("staticLock", 1),
          ("authorized", 2),
          ("unAuthorized", 3),
          ("authorizing", 4),
          ("macAddrSticky", 5))
    )


_PortAccessControlAccessStatus_Type.__name__ = "Integer32"
_PortAccessControlAccessStatus_Object = MibTableColumn
portAccessControlAccessStatus = _PortAccessControlAccessStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 2, 3, 1, 3),
    _PortAccessControlAccessStatus_Type()
)
portAccessControlAccessStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portAccessControlAccessStatus.setStatus("current")


class _PortAccessControlStatus_Type(Integer32):
    """Custom type portAccessControlStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6))
    )


_PortAccessControlStatus_Type.__name__ = "Integer32"
_PortAccessControlStatus_Object = MibTableColumn
portAccessControlStatus = _PortAccessControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 2, 3, 1, 4),
    _PortAccessControlStatus_Type()
)
portAccessControlStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portAccessControlStatus.setStatus("current")
_PortAccessControlVid_Type = Integer32
_PortAccessControlVid_Object = MibTableColumn
portAccessControlVid = _PortAccessControlVid_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 2, 3, 1, 5),
    _PortAccessControlVid_Type()
)
portAccessControlVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portAccessControlVid.setStatus("current")
_PortSecurity_ObjectIdentity = ObjectIdentity
portSecurity = _PortSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 2, 4)
)
_PortSecurityModeTable_Object = MibTable
portSecurityModeTable = _PortSecurityModeTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 2, 4, 1)
)
if mibBuilder.loadTexts:
    portSecurityModeTable.setStatus("current")
_PortSecurityModeEntry_Object = MibTableRow
portSecurityModeEntry = _PortSecurityModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 2, 4, 1, 1)
)
portSecurityModeEntry.setIndexNames(
    (0, "MOXA-EDSP506E-MIB", "portSecurityModePort"),
)
if mibBuilder.loadTexts:
    portSecurityModeEntry.setStatus("current")
_PortSecurityModePort_Type = Integer32
_PortSecurityModePort_Object = MibTableColumn
portSecurityModePort = _PortSecurityModePort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 2, 4, 1, 1, 1),
    _PortSecurityModePort_Type()
)
portSecurityModePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSecurityModePort.setStatus("current")


class _PortSecurityModeSelect_Type(Integer32):
    """Custom type portSecurityModeSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal-mode", 0),
          ("static-portlock", 1),
          ("mac-address-sticky", 2))
    )


_PortSecurityModeSelect_Type.__name__ = "Integer32"
_PortSecurityModeSelect_Object = MibTableColumn
portSecurityModeSelect = _PortSecurityModeSelect_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 2, 4, 1, 1, 2),
    _PortSecurityModeSelect_Type()
)
portSecurityModeSelect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portSecurityModeSelect.setStatus("current")
_PortSecurityModeLimit_Type = Integer32
_PortSecurityModeLimit_Object = MibTableColumn
portSecurityModeLimit = _PortSecurityModeLimit_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 2, 4, 1, 1, 3),
    _PortSecurityModeLimit_Type()
)
portSecurityModeLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portSecurityModeLimit.setStatus("current")


class _PortSecurityModeViolationPortDisable_Type(Integer32):
    """Custom type portSecurityModeViolationPortDisable based on Integer32"""
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


_PortSecurityModeViolationPortDisable_Type.__name__ = "Integer32"
_PortSecurityModeViolationPortDisable_Object = MibTableColumn
portSecurityModeViolationPortDisable = _PortSecurityModeViolationPortDisable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 2, 4, 1, 1, 4),
    _PortSecurityModeViolationPortDisable_Type()
)
portSecurityModeViolationPortDisable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portSecurityModeViolationPortDisable.setStatus("current")


class _PortSecurityModeStatus_Type(Integer32):
    """Custom type portSecurityModeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4))
    )


_PortSecurityModeStatus_Type.__name__ = "Integer32"
_PortSecurityModeStatus_Object = MibTableColumn
portSecurityModeStatus = _PortSecurityModeStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 2, 4, 1, 1, 5),
    _PortSecurityModeStatus_Type()
)
portSecurityModeStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portSecurityModeStatus.setStatus("current")
_StaticPortLock_ObjectIdentity = ObjectIdentity
staticPortLock = _StaticPortLock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 2, 4, 2)
)
_StaticPortLockAddress_Type = MacAddress
_StaticPortLockAddress_Object = MibScalar
staticPortLockAddress = _StaticPortLockAddress_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 2, 4, 2, 1),
    _StaticPortLockAddress_Type()
)
staticPortLockAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    staticPortLockAddress.setStatus("current")
_StaticPortLockPort_Type = Integer32
_StaticPortLockPort_Object = MibScalar
staticPortLockPort = _StaticPortLockPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 2, 4, 2, 2),
    _StaticPortLockPort_Type()
)
staticPortLockPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    staticPortLockPort.setStatus("current")


class _StaticPortLockStatus_Type(Integer32):
    """Custom type staticPortLockStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4))
    )


_StaticPortLockStatus_Type.__name__ = "Integer32"
_StaticPortLockStatus_Object = MibScalar
staticPortLockStatus = _StaticPortLockStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 2, 4, 2, 3),
    _StaticPortLockStatus_Type()
)
staticPortLockStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    staticPortLockStatus.setStatus("current")
_StaticPortLockVid_Type = Integer32
_StaticPortLockVid_Object = MibScalar
staticPortLockVid = _StaticPortLockVid_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 2, 4, 2, 4),
    _StaticPortLockVid_Type()
)
staticPortLockVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    staticPortLockVid.setStatus("current")
_MacAddressSticky_ObjectIdentity = ObjectIdentity
macAddressSticky = _MacAddressSticky_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 2, 4, 3)
)
_MacAddressStickyAddress_Type = MacAddress
_MacAddressStickyAddress_Object = MibScalar
macAddressStickyAddress = _MacAddressStickyAddress_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 2, 4, 3, 1),
    _MacAddressStickyAddress_Type()
)
macAddressStickyAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macAddressStickyAddress.setStatus("current")
_MacAddressStickyPort_Type = Integer32
_MacAddressStickyPort_Object = MibScalar
macAddressStickyPort = _MacAddressStickyPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 2, 4, 3, 2),
    _MacAddressStickyPort_Type()
)
macAddressStickyPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macAddressStickyPort.setStatus("current")
_MacAddressStickyVid_Type = Integer32
_MacAddressStickyVid_Object = MibScalar
macAddressStickyVid = _MacAddressStickyVid_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 2, 4, 3, 3),
    _MacAddressStickyVid_Type()
)
macAddressStickyVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macAddressStickyVid.setStatus("current")


class _MacAddressStickyStatus_Type(Integer32):
    """Custom type macAddressStickyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4))
    )


_MacAddressStickyStatus_Type.__name__ = "Integer32"
_MacAddressStickyStatus_Object = MibScalar
macAddressStickyStatus = _MacAddressStickyStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 2, 4, 3, 4),
    _MacAddressStickyStatus_Type()
)
macAddressStickyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macAddressStickyStatus.setStatus("current")
_Mab_ObjectIdentity = ObjectIdentity
mab = _Mab_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 2, 5)
)


class _MabDBOption_Type(Integer32):
    """Custom type mabDBOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("radius", 2)
    )


_MabDBOption_Type.__name__ = "Integer32"
_MabDBOption_Object = MibScalar
mabDBOption = _MabDBOption_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 2, 5, 1),
    _MabDBOption_Type()
)
mabDBOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mabDBOption.setStatus("current")


class _MabReauthEnable_Type(Integer32):
    """Custom type mabReauthEnable based on Integer32"""
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


_MabReauthEnable_Type.__name__ = "Integer32"
_MabReauthEnable_Object = MibScalar
mabReauthEnable = _MabReauthEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 2, 5, 2),
    _MabReauthEnable_Type()
)
mabReauthEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mabReauthEnable.setStatus("current")


class _MabReauthPeriod_Type(Integer32):
    """Custom type mabReauthPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 65535),
    )


_MabReauthPeriod_Type.__name__ = "Integer32"
_MabReauthPeriod_Object = MibScalar
mabReauthPeriod = _MabReauthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 2, 5, 3),
    _MabReauthPeriod_Type()
)
mabReauthPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mabReauthPeriod.setStatus("current")


class _MabRestartEnable_Type(Integer32):
    """Custom type mabRestartEnable based on Integer32"""
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


_MabRestartEnable_Type.__name__ = "Integer32"
_MabRestartEnable_Object = MibScalar
mabRestartEnable = _MabRestartEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 2, 5, 4),
    _MabRestartEnable_Type()
)
mabRestartEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mabRestartEnable.setStatus("current")


class _MabRestartPeriod_Type(Integer32):
    """Custom type mabRestartPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 300),
    )


_MabRestartPeriod_Type.__name__ = "Integer32"
_MabRestartPeriod_Object = MibScalar
mabRestartPeriod = _MabRestartPeriod_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 2, 5, 5),
    _MabRestartPeriod_Type()
)
mabRestartPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mabRestartPeriod.setStatus("current")
_MabSettingTable_Object = MibTable
mabSettingTable = _MabSettingTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 2, 5, 6)
)
if mibBuilder.loadTexts:
    mabSettingTable.setStatus("current")
_MabSettingEntry_Object = MibTableRow
mabSettingEntry = _MabSettingEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 2, 5, 6, 1)
)
mabSettingEntry.setIndexNames(
    (0, "MOXA-EDSP506E-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    mabSettingEntry.setStatus("current")


class _EnableMAB_Type(Integer32):
    """Custom type enableMAB based on Integer32"""
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


_EnableMAB_Type.__name__ = "Integer32"
_EnableMAB_Object = MibTableColumn
enableMAB = _EnableMAB_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 22, 2, 5, 6, 1, 1),
    _EnableMAB_Type()
)
enableMAB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableMAB.setStatus("current")
_AccessibleIP_ObjectIdentity = ObjectIdentity
accessibleIP = _AccessibleIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 30)
)


class _EnableAccessibleIP_Type(Integer32):
    """Custom type enableAccessibleIP based on Integer32"""
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


_EnableAccessibleIP_Type.__name__ = "Integer32"
_EnableAccessibleIP_Object = MibScalar
enableAccessibleIP = _EnableAccessibleIP_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 30, 1),
    _EnableAccessibleIP_Type()
)
enableAccessibleIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableAccessibleIP.setStatus("current")
_AccessibleIpTable_Object = MibTable
accessibleIpTable = _AccessibleIpTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 30, 2)
)
if mibBuilder.loadTexts:
    accessibleIpTable.setStatus("current")
_AccessibleIpEntry_Object = MibTableRow
accessibleIpEntry = _AccessibleIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 30, 2, 1)
)
accessibleIpEntry.setIndexNames(
    (0, "MOXA-EDSP506E-MIB", "accessibleIpAddress"),
)
if mibBuilder.loadTexts:
    accessibleIpEntry.setStatus("current")
_AccessibleIpAddress_Type = IpAddress
_AccessibleIpAddress_Object = MibTableColumn
accessibleIpAddress = _AccessibleIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 30, 2, 1, 1),
    _AccessibleIpAddress_Type()
)
accessibleIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accessibleIpAddress.setStatus("current")
_AccessibleIpNetMask_Type = IpAddress
_AccessibleIpNetMask_Object = MibTableColumn
accessibleIpNetMask = _AccessibleIpNetMask_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 30, 2, 1, 2),
    _AccessibleIpNetMask_Type()
)
accessibleIpNetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accessibleIpNetMask.setStatus("current")


class _AccessibleIpStatus_Type(Integer32):
    """Custom type accessibleIpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6))
    )


_AccessibleIpStatus_Type.__name__ = "Integer32"
_AccessibleIpStatus_Object = MibTableColumn
accessibleIpStatus = _AccessibleIpStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 30, 2, 1, 3),
    _AccessibleIpStatus_Type()
)
accessibleIpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accessibleIpStatus.setStatus("current")
_SysFileUpdate_ObjectIdentity = ObjectIdentity
sysFileUpdate = _SysFileUpdate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 31)
)
_TftpServer_Type = DisplayString
_TftpServer_Object = MibScalar
tftpServer = _TftpServer_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 31, 1),
    _TftpServer_Type()
)
tftpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpServer.setStatus("current")
_FirmwarePathName_Type = DisplayString
_FirmwarePathName_Object = MibScalar
firmwarePathName = _FirmwarePathName_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 31, 2),
    _FirmwarePathName_Type()
)
firmwarePathName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firmwarePathName.setStatus("current")
_LogPathName_Type = DisplayString
_LogPathName_Object = MibScalar
logPathName = _LogPathName_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 31, 3),
    _LogPathName_Type()
)
logPathName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logPathName.setStatus("current")
_ConfPathName_Type = DisplayString
_ConfPathName_Object = MibScalar
confPathName = _ConfPathName_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 31, 4),
    _ConfPathName_Type()
)
confPathName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confPathName.setStatus("current")


class _TftpUpdate_Type(Integer32):
    """Custom type tftpUpdate based on Integer32"""
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
        *(("importFirmware", 1),
          ("importConfig", 2),
          ("exportConfig", 3),
          ("exportLog", 4))
    )


_TftpUpdate_Type.__name__ = "Integer32"
_TftpUpdate_Object = MibScalar
tftpUpdate = _TftpUpdate_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 31, 5),
    _TftpUpdate_Type()
)
tftpUpdate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tftpUpdate.setStatus("current")
_TimeSetting_ObjectIdentity = ObjectIdentity
timeSetting = _TimeSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 32)
)
_SysDateTime_Type = DateAndTime
_SysDateTime_Object = MibScalar
sysDateTime = _SysDateTime_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 32, 1),
    _SysDateTime_Type()
)
sysDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDateTime.setStatus("current")
_CalibratePeriod_Type = Integer32
_CalibratePeriod_Object = MibScalar
calibratePeriod = _CalibratePeriod_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 32, 2),
    _CalibratePeriod_Type()
)
calibratePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    calibratePeriod.setStatus("current")
_TimeServer1_Type = DisplayString
_TimeServer1_Object = MibScalar
timeServer1 = _TimeServer1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 32, 3),
    _TimeServer1_Type()
)
timeServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeServer1.setStatus("current")
_TimeServer2_Type = DisplayString
_TimeServer2_Object = MibScalar
timeServer2 = _TimeServer2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 32, 4),
    _TimeServer2_Type()
)
timeServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeServer2.setStatus("current")
_DaylightSaving_ObjectIdentity = ObjectIdentity
daylightSaving = _DaylightSaving_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 32, 5)
)


class _StartMonth_Type(Integer32):
    """Custom type startMonth based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("jan", 1),
          ("feb", 2),
          ("mar", 3),
          ("apr", 4),
          ("may", 5),
          ("jun", 6),
          ("jul", 7),
          ("aug", 8),
          ("sep", 9),
          ("oct", 10),
          ("nov", 11),
          ("dec", 12))
    )


_StartMonth_Type.__name__ = "Integer32"
_StartMonth_Object = MibScalar
startMonth = _StartMonth_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 32, 5, 1),
    _StartMonth_Type()
)
startMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    startMonth.setStatus("current")


class _StartWeek_Type(Integer32):
    """Custom type startWeek based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("week1", 1),
          ("week2", 2),
          ("week3", 3),
          ("week4", 4),
          ("weeklast", 6))
    )


_StartWeek_Type.__name__ = "Integer32"
_StartWeek_Object = MibScalar
startWeek = _StartWeek_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 32, 5, 2),
    _StartWeek_Type()
)
startWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    startWeek.setStatus("current")


class _StartDay_Type(Integer32):
    """Custom type startDay based on Integer32"""
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
        *(("na", 0),
          ("sun", 1),
          ("mon", 2),
          ("tue", 3),
          ("wed", 4),
          ("thu", 5),
          ("fri", 6),
          ("sat", 7))
    )


_StartDay_Type.__name__ = "Integer32"
_StartDay_Object = MibScalar
startDay = _StartDay_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 32, 5, 3),
    _StartDay_Type()
)
startDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    startDay.setStatus("current")
_StartHour_Type = Integer32
_StartHour_Object = MibScalar
startHour = _StartHour_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 32, 5, 4),
    _StartHour_Type()
)
startHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    startHour.setStatus("current")


class _EndMonth_Type(Integer32):
    """Custom type endMonth based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("jan", 1),
          ("feb", 2),
          ("mar", 3),
          ("apr", 4),
          ("may", 5),
          ("jun", 6),
          ("jul", 7),
          ("aug", 8),
          ("sep", 9),
          ("oct", 10),
          ("nov", 11),
          ("dec", 12))
    )


_EndMonth_Type.__name__ = "Integer32"
_EndMonth_Object = MibScalar
endMonth = _EndMonth_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 32, 5, 5),
    _EndMonth_Type()
)
endMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    endMonth.setStatus("current")


class _EndWeek_Type(Integer32):
    """Custom type endWeek based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("week1", 1),
          ("week2", 2),
          ("week3", 3),
          ("week4", 4),
          ("weeklast", 6))
    )


_EndWeek_Type.__name__ = "Integer32"
_EndWeek_Object = MibScalar
endWeek = _EndWeek_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 32, 5, 6),
    _EndWeek_Type()
)
endWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    endWeek.setStatus("current")


class _EndDay_Type(Integer32):
    """Custom type endDay based on Integer32"""
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
        *(("na", 0),
          ("sun", 1),
          ("mon", 2),
          ("tue", 3),
          ("wed", 4),
          ("thu", 5),
          ("fri", 6),
          ("sat", 7))
    )


_EndDay_Type.__name__ = "Integer32"
_EndDay_Object = MibScalar
endDay = _EndDay_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 32, 5, 7),
    _EndDay_Type()
)
endDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    endDay.setStatus("current")
_EndHour_Type = Integer32
_EndHour_Object = MibScalar
endHour = _EndHour_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 32, 5, 8),
    _EndHour_Type()
)
endHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    endHour.setStatus("current")
_OffsetHours_Type = Integer32
_OffsetHours_Object = MibScalar
offsetHours = _OffsetHours_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 32, 5, 9),
    _OffsetHours_Type()
)
offsetHours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    offsetHours.setStatus("current")


class _EnableNTPServer_Type(Integer32):
    """Custom type enableNTPServer based on Integer32"""
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


_EnableNTPServer_Type.__name__ = "Integer32"
_EnableNTPServer_Object = MibScalar
enableNTPServer = _EnableNTPServer_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 32, 6),
    _EnableNTPServer_Type()
)
enableNTPServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableNTPServer.setStatus("current")


class _ClockSource_Type(Integer32):
    """Custom type clockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 0),
          ("sntp", 1),
          ("ntp", 2))
    )


_ClockSource_Type.__name__ = "Integer32"
_ClockSource_Object = MibScalar
clockSource = _ClockSource_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 32, 7),
    _ClockSource_Type()
)
clockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clockSource.setStatus("current")


class _NtpAuthenticate_Type(Integer32):
    """Custom type ntpAuthenticate based on Integer32"""
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


_NtpAuthenticate_Type.__name__ = "Integer32"
_NtpAuthenticate_Object = MibScalar
ntpAuthenticate = _NtpAuthenticate_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 32, 8),
    _NtpAuthenticate_Type()
)
ntpAuthenticate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpAuthenticate.setStatus("current")
_NtpPeerTable_Object = MibTable
ntpPeerTable = _NtpPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 32, 9)
)
if mibBuilder.loadTexts:
    ntpPeerTable.setStatus("current")
_NtpPeerEntry_Object = MibTableRow
ntpPeerEntry = _NtpPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 32, 9, 1)
)
ntpPeerEntry.setIndexNames(
    (0, "MOXA-EDSP506E-MIB", "ntpPeerIndex"),
)
if mibBuilder.loadTexts:
    ntpPeerEntry.setStatus("current")
_NtpPeerIndex_Type = Integer32
_NtpPeerIndex_Object = MibTableColumn
ntpPeerIndex = _NtpPeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 32, 9, 1, 1),
    _NtpPeerIndex_Type()
)
ntpPeerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpPeerIndex.setStatus("current")
_NtpPeerAddress_Type = DisplayString
_NtpPeerAddress_Object = MibTableColumn
ntpPeerAddress = _NtpPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 32, 9, 1, 2),
    _NtpPeerAddress_Type()
)
ntpPeerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpPeerAddress.setStatus("current")


class _NtpPeerAuthenticate_Type(Integer32):
    """Custom type ntpPeerAuthenticate based on Integer32"""
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


_NtpPeerAuthenticate_Type.__name__ = "Integer32"
_NtpPeerAuthenticate_Object = MibTableColumn
ntpPeerAuthenticate = _NtpPeerAuthenticate_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 32, 9, 1, 3),
    _NtpPeerAuthenticate_Type()
)
ntpPeerAuthenticate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpPeerAuthenticate.setStatus("current")
_NtpPeerAuthenticateKeyid_Type = Integer32
_NtpPeerAuthenticateKeyid_Object = MibTableColumn
ntpPeerAuthenticateKeyid = _NtpPeerAuthenticateKeyid_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 32, 9, 1, 4),
    _NtpPeerAuthenticateKeyid_Type()
)
ntpPeerAuthenticateKeyid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpPeerAuthenticateKeyid.setStatus("current")
_NtpAuthenticateKeyTable_Object = MibTable
ntpAuthenticateKeyTable = _NtpAuthenticateKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 32, 10)
)
if mibBuilder.loadTexts:
    ntpAuthenticateKeyTable.setStatus("current")
_NtpAuthenticateKeyEntry_Object = MibTableRow
ntpAuthenticateKeyEntry = _NtpAuthenticateKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 32, 10, 1)
)
ntpAuthenticateKeyEntry.setIndexNames(
    (0, "MOXA-EDSP506E-MIB", "ntpAuthenticateKeyIndex"),
)
if mibBuilder.loadTexts:
    ntpAuthenticateKeyEntry.setStatus("current")
_NtpAuthenticateKeyIndex_Type = Integer32
_NtpAuthenticateKeyIndex_Object = MibTableColumn
ntpAuthenticateKeyIndex = _NtpAuthenticateKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 32, 10, 1, 1),
    _NtpAuthenticateKeyIndex_Type()
)
ntpAuthenticateKeyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpAuthenticateKeyIndex.setStatus("current")
_NtpAuthenticateKeyID_Type = Integer32
_NtpAuthenticateKeyID_Object = MibTableColumn
ntpAuthenticateKeyID = _NtpAuthenticateKeyID_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 32, 10, 1, 2),
    _NtpAuthenticateKeyID_Type()
)
ntpAuthenticateKeyID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpAuthenticateKeyID.setStatus("current")
_NtpAuthenticateKeyString_Type = DisplayString
_NtpAuthenticateKeyString_Object = MibTableColumn
ntpAuthenticateKeyString = _NtpAuthenticateKeyString_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 32, 10, 1, 3),
    _NtpAuthenticateKeyString_Type()
)
ntpAuthenticateKeyString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpAuthenticateKeyString.setStatus("current")


class _NtpAuthenticateKeyTrusted_Type(Integer32):
    """Custom type ntpAuthenticateKeyTrusted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("distrust", 0),
          ("trusted", 1))
    )


_NtpAuthenticateKeyTrusted_Type.__name__ = "Integer32"
_NtpAuthenticateKeyTrusted_Object = MibTableColumn
ntpAuthenticateKeyTrusted = _NtpAuthenticateKeyTrusted_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 32, 10, 1, 4),
    _NtpAuthenticateKeyTrusted_Type()
)
ntpAuthenticateKeyTrusted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpAuthenticateKeyTrusted.setStatus("current")
_DipSwitchSetting_ObjectIdentity = ObjectIdentity
dipSwitchSetting = _DipSwitchSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 34)
)


class _DipSwitchEnableTurboRing_Type(Integer32):
    """Custom type dipSwitchEnableTurboRing based on Integer32"""
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


_DipSwitchEnableTurboRing_Type.__name__ = "Integer32"
_DipSwitchEnableTurboRing_Object = MibScalar
dipSwitchEnableTurboRing = _DipSwitchEnableTurboRing_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 34, 1),
    _DipSwitchEnableTurboRing_Type()
)
dipSwitchEnableTurboRing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dipSwitchEnableTurboRing.setStatus("current")


class _DipSwitchTurboRingPole_Type(Integer32):
    """Custom type dipSwitchTurboRingPole based on Integer32"""
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


_DipSwitchTurboRingPole_Type.__name__ = "Integer32"
_DipSwitchTurboRingPole_Object = MibScalar
dipSwitchTurboRingPole = _DipSwitchTurboRingPole_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 34, 2),
    _DipSwitchTurboRingPole_Type()
)
dipSwitchTurboRingPole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dipSwitchTurboRingPole.setStatus("current")


class _DipSwitchRingCouplingPole_Type(Integer32):
    """Custom type dipSwitchRingCouplingPole based on Integer32"""
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


_DipSwitchRingCouplingPole_Type.__name__ = "Integer32"
_DipSwitchRingCouplingPole_Object = MibScalar
dipSwitchRingCouplingPole = _DipSwitchRingCouplingPole_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 34, 3),
    _DipSwitchRingCouplingPole_Type()
)
dipSwitchRingCouplingPole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dipSwitchRingCouplingPole.setStatus("current")


class _DipSwitchRingMasterPole_Type(Integer32):
    """Custom type dipSwitchRingMasterPole based on Integer32"""
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


_DipSwitchRingMasterPole_Type.__name__ = "Integer32"
_DipSwitchRingMasterPole_Object = MibScalar
dipSwitchRingMasterPole = _DipSwitchRingMasterPole_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 34, 4),
    _DipSwitchRingMasterPole_Type()
)
dipSwitchRingMasterPole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dipSwitchRingMasterPole.setStatus("current")
_BackupMediaSetting_ObjectIdentity = ObjectIdentity
backupMediaSetting = _BackupMediaSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 35)
)


class _Abc02Status_Type(Integer32):
    """Custom type abc02Status based on Integer32"""
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
        *(("device-not-present", 0),
          ("unauthorized-media", 1),
          ("detecting", 2),
          ("working", 3),
          ("ready-and-removable", 4))
    )


_Abc02Status_Type.__name__ = "Integer32"
_Abc02Status_Object = MibScalar
abc02Status = _Abc02Status_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 35, 2),
    _Abc02Status_Type()
)
abc02Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    abc02Status.setStatus("current")


class _Abc02AutoImportConfig_Type(Integer32):
    """Custom type abc02AutoImportConfig based on Integer32"""
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


_Abc02AutoImportConfig_Type.__name__ = "Integer32"
_Abc02AutoImportConfig_Object = MibScalar
abc02AutoImportConfig = _Abc02AutoImportConfig_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 35, 3),
    _Abc02AutoImportConfig_Type()
)
abc02AutoImportConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    abc02AutoImportConfig.setStatus("current")


class _Abc02AutoExportConfig_Type(Integer32):
    """Custom type abc02AutoExportConfig based on Integer32"""
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


_Abc02AutoExportConfig_Type.__name__ = "Integer32"
_Abc02AutoExportConfig_Object = MibScalar
abc02AutoExportConfig = _Abc02AutoExportConfig_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 35, 4),
    _Abc02AutoExportConfig_Type()
)
abc02AutoExportConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    abc02AutoExportConfig.setStatus("current")


class _Abc02AutoExportLog_Type(Integer32):
    """Custom type abc02AutoExportLog based on Integer32"""
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


_Abc02AutoExportLog_Type.__name__ = "Integer32"
_Abc02AutoExportLog_Object = MibScalar
abc02AutoExportLog = _Abc02AutoExportLog_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 35, 5),
    _Abc02AutoExportLog_Type()
)
abc02AutoExportLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    abc02AutoExportLog.setStatus("current")


class _EnableWarmStart_Type(Integer32):
    """Custom type enableWarmStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_EnableWarmStart_Type.__name__ = "Integer32"
_EnableWarmStart_Object = MibScalar
enableWarmStart = _EnableWarmStart_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 36),
    _EnableWarmStart_Type()
)
enableWarmStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableWarmStart.setStatus("current")
_SyslogSetting_ObjectIdentity = ObjectIdentity
syslogSetting = _SyslogSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 37)
)
_SyslogServer1_Type = DisplayString
_SyslogServer1_Object = MibScalar
syslogServer1 = _SyslogServer1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 37, 1),
    _SyslogServer1_Type()
)
syslogServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogServer1.setStatus("current")
_SyslogServer1port_Type = Integer32
_SyslogServer1port_Object = MibScalar
syslogServer1port = _SyslogServer1port_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 37, 2),
    _SyslogServer1port_Type()
)
syslogServer1port.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogServer1port.setStatus("current")
_SyslogServer2_Type = DisplayString
_SyslogServer2_Object = MibScalar
syslogServer2 = _SyslogServer2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 37, 3),
    _SyslogServer2_Type()
)
syslogServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogServer2.setStatus("current")
_SyslogServer2port_Type = Integer32
_SyslogServer2port_Object = MibScalar
syslogServer2port = _SyslogServer2port_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 37, 4),
    _SyslogServer2port_Type()
)
syslogServer2port.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogServer2port.setStatus("current")
_SyslogServer3_Type = DisplayString
_SyslogServer3_Object = MibScalar
syslogServer3 = _SyslogServer3_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 37, 5),
    _SyslogServer3_Type()
)
syslogServer3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogServer3.setStatus("current")
_SyslogServer3port_Type = Integer32
_SyslogServer3port_Object = MibScalar
syslogServer3port = _SyslogServer3port_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 37, 6),
    _SyslogServer3port_Type()
)
syslogServer3port.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogServer3port.setStatus("current")
_DhcpRelayAgentSetting_ObjectIdentity = ObjectIdentity
dhcpRelayAgentSetting = _DhcpRelayAgentSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 39)
)
_DhcpServer1_Type = DisplayString
_DhcpServer1_Object = MibScalar
dhcpServer1 = _DhcpServer1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 39, 1),
    _DhcpServer1_Type()
)
dhcpServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServer1.setStatus("current")
_DhcpServer2_Type = DisplayString
_DhcpServer2_Object = MibScalar
dhcpServer2 = _DhcpServer2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 39, 2),
    _DhcpServer2_Type()
)
dhcpServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServer2.setStatus("current")
_DhcpServer3_Type = DisplayString
_DhcpServer3_Object = MibScalar
dhcpServer3 = _DhcpServer3_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 39, 3),
    _DhcpServer3_Type()
)
dhcpServer3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServer3.setStatus("current")
_DhcpServer4_Type = DisplayString
_DhcpServer4_Object = MibScalar
dhcpServer4 = _DhcpServer4_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 39, 4),
    _DhcpServer4_Type()
)
dhcpServer4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServer4.setStatus("current")
_Option82Setting_ObjectIdentity = ObjectIdentity
option82Setting = _Option82Setting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 39, 5)
)


class _EnableOption82_Type(Integer32):
    """Custom type enableOption82 based on Integer32"""
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


_EnableOption82_Type.__name__ = "Integer32"
_EnableOption82_Object = MibScalar
enableOption82 = _EnableOption82_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 39, 5, 1),
    _EnableOption82_Type()
)
enableOption82.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableOption82.setStatus("current")


class _Option82Type_Type(Integer32):
    """Custom type option82Type based on Integer32"""
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
        *(("ip", 0),
          ("mac", 1),
          ("client-id", 2),
          ("other", 3))
    )


_Option82Type_Type.__name__ = "Integer32"
_Option82Type_Object = MibScalar
option82Type = _Option82Type_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 39, 5, 2),
    _Option82Type_Type()
)
option82Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    option82Type.setStatus("current")
_Option82Value_Type = DisplayString
_Option82Value_Object = MibScalar
option82Value = _Option82Value_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 39, 5, 3),
    _Option82Value_Type()
)
option82Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    option82Value.setStatus("current")
_Option82ValueDisplay_Type = DisplayString
_Option82ValueDisplay_Object = MibScalar
option82ValueDisplay = _Option82ValueDisplay_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 39, 5, 4),
    _Option82ValueDisplay_Type()
)
option82ValueDisplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    option82ValueDisplay.setStatus("current")
_DhcpFunctionTable_Object = MibTable
dhcpFunctionTable = _DhcpFunctionTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 39, 6)
)
if mibBuilder.loadTexts:
    dhcpFunctionTable.setStatus("current")
_DhcpFunctionEntry_Object = MibTableRow
dhcpFunctionEntry = _DhcpFunctionEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 39, 6, 1)
)
dhcpFunctionEntry.setIndexNames(
    (0, "MOXA-EDSP506E-MIB", "dhcpPortIndex"),
)
if mibBuilder.loadTexts:
    dhcpFunctionEntry.setStatus("current")
_DhcpPortIndex_Type = Integer32
_DhcpPortIndex_Object = MibTableColumn
dhcpPortIndex = _DhcpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 39, 6, 1, 1),
    _DhcpPortIndex_Type()
)
dhcpPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpPortIndex.setStatus("current")
_CircuitID_Type = DisplayString
_CircuitID_Object = MibTableColumn
circuitID = _CircuitID_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 39, 6, 1, 2),
    _CircuitID_Type()
)
circuitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitID.setStatus("current")


class _Option82Enable_Type(Integer32):
    """Custom type option82Enable based on Integer32"""
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


_Option82Enable_Type.__name__ = "Integer32"
_Option82Enable_Object = MibTableColumn
option82Enable = _Option82Enable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 39, 6, 1, 3),
    _Option82Enable_Type()
)
option82Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    option82Enable.setStatus("current")
_PoeSetting_ObjectIdentity = ObjectIdentity
poeSetting = _PoeSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 40)
)
_PoePortTable_Object = MibTable
poePortTable = _PoePortTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 40, 3)
)
if mibBuilder.loadTexts:
    poePortTable.setStatus("current")
_PoePortEntry_Object = MibTableRow
poePortEntry = _PoePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 40, 3, 1)
)
poePortEntry.setIndexNames(
    (0, "MOXA-EDSP506E-MIB", "poePortIndex"),
)
if mibBuilder.loadTexts:
    poePortEntry.setStatus("current")
_PoePortIndex_Type = Integer32
_PoePortIndex_Object = MibTableColumn
poePortIndex = _PoePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 40, 3, 1, 1),
    _PoePortIndex_Type()
)
poePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poePortIndex.setStatus("current")


class _PoePortEnable_Type(Integer32):
    """Custom type poePortEnable based on Integer32"""
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


_PoePortEnable_Type.__name__ = "Integer32"
_PoePortEnable_Object = MibTableColumn
poePortEnable = _PoePortEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 40, 3, 1, 2),
    _PoePortEnable_Type()
)
poePortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poePortEnable.setStatus("current")
_PowerLimit_Type = Integer32
_PowerLimit_Object = MibTableColumn
powerLimit = _PowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 40, 3, 1, 4),
    _PowerLimit_Type()
)
powerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerLimit.setStatus("current")


class _Pdfailure_Type(Integer32):
    """Custom type pdfailure based on Integer32"""
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


_Pdfailure_Type.__name__ = "Integer32"
_Pdfailure_Object = MibTableColumn
pdfailure = _Pdfailure_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 40, 3, 1, 5),
    _Pdfailure_Type()
)
pdfailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdfailure.setStatus("current")
_Pdipaddr_Type = DisplayString
_Pdipaddr_Object = MibTableColumn
pdipaddr = _Pdipaddr_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 40, 3, 1, 6),
    _Pdipaddr_Type()
)
pdipaddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdipaddr.setStatus("current")
_PdPollingInterval_Type = Integer32
_PdPollingInterval_Object = MibTableColumn
pdPollingInterval = _PdPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 40, 3, 1, 7),
    _PdPollingInterval_Type()
)
pdPollingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdPollingInterval.setStatus("current")


class _Poeporttimetabling_Type(Integer32):
    """Custom type poeporttimetabling based on Integer32"""
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


_Poeporttimetabling_Type.__name__ = "Integer32"
_Poeporttimetabling_Object = MibTableColumn
poeporttimetabling = _Poeporttimetabling_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 40, 3, 1, 8),
    _Poeporttimetabling_Type()
)
poeporttimetabling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poeporttimetabling.setStatus("current")


class _PoePortLegacyPdDetect_Type(Integer32):
    """Custom type poePortLegacyPdDetect based on Integer32"""
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


_PoePortLegacyPdDetect_Type.__name__ = "Integer32"
_PoePortLegacyPdDetect_Object = MibTableColumn
poePortLegacyPdDetect = _PoePortLegacyPdDetect_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 40, 3, 1, 9),
    _PoePortLegacyPdDetect_Type()
)
poePortLegacyPdDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poePortLegacyPdDetect.setStatus("current")
_PdNoResponseTimeout_Type = Integer32
_PdNoResponseTimeout_Object = MibTableColumn
pdNoResponseTimeout = _PdNoResponseTimeout_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 40, 3, 1, 10),
    _PdNoResponseTimeout_Type()
)
pdNoResponseTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdNoResponseTimeout.setStatus("current")


class _PdNoResponseAction_Type(Integer32):
    """Custom type pdNoResponseAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 0),
          ("rebootPD", 1),
          ("powerOffPD", 2))
    )


_PdNoResponseAction_Type.__name__ = "Integer32"
_PdNoResponseAction_Object = MibTableColumn
pdNoResponseAction = _PdNoResponseAction_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 40, 3, 1, 11),
    _PdNoResponseAction_Type()
)
pdNoResponseAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdNoResponseAction.setStatus("current")


class _PoePowerOutputMode_Type(Integer32):
    """Custom type poePowerOutputMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("highPower", 1),
          ("force", 2))
    )


_PoePowerOutputMode_Type.__name__ = "Integer32"
_PoePowerOutputMode_Object = MibTableColumn
poePowerOutputMode = _PoePowerOutputMode_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 40, 3, 1, 12),
    _PoePowerOutputMode_Type()
)
poePowerOutputMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poePowerOutputMode.setStatus("current")
_PoePortPowerPriority_Type = Integer32
_PoePortPowerPriority_Object = MibTableColumn
poePortPowerPriority = _PoePortPowerPriority_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 40, 3, 1, 13),
    _PoePortPowerPriority_Type()
)
poePortPowerPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poePortPowerPriority.setStatus("current")
_PoeTimeTable_Object = MibTable
poeTimeTable = _PoeTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 40, 5)
)
if mibBuilder.loadTexts:
    poeTimeTable.setStatus("current")
_PoeTimeEntry_Object = MibTableRow
poeTimeEntry = _PoeTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 40, 5, 1)
)
poeTimeEntry.setIndexNames(
    (0, "MOXA-EDSP506E-MIB", "poeTPortIndex"),
    (0, "MOXA-EDSP506E-MIB", "poeWeekDay"),
)
if mibBuilder.loadTexts:
    poeTimeEntry.setStatus("current")
_PoeTPortIndex_Type = Integer32
_PoeTPortIndex_Object = MibTableColumn
poeTPortIndex = _PoeTPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 40, 5, 1, 1),
    _PoeTPortIndex_Type()
)
poeTPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poeTPortIndex.setStatus("current")
_PoeWeekDay_Type = Integer32
_PoeWeekDay_Object = MibTableColumn
poeWeekDay = _PoeWeekDay_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 40, 5, 1, 2),
    _PoeWeekDay_Type()
)
poeWeekDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poeWeekDay.setStatus("current")


class _PoeDayEnable_Type(Integer32):
    """Custom type poeDayEnable based on Integer32"""
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


_PoeDayEnable_Type.__name__ = "Integer32"
_PoeDayEnable_Object = MibTableColumn
poeDayEnable = _PoeDayEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 40, 5, 1, 3),
    _PoeDayEnable_Type()
)
poeDayEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poeDayEnable.setStatus("current")
_PoeDayStart_Type = Integer32
_PoeDayStart_Object = MibTableColumn
poeDayStart = _PoeDayStart_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 40, 5, 1, 4),
    _PoeDayStart_Type()
)
poeDayStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poeDayStart.setStatus("current")
_PoeDayStop_Type = Integer32
_PoeDayStop_Object = MibTableColumn
poeDayStop = _PoeDayStop_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 40, 5, 1, 5),
    _PoeDayStop_Type()
)
poeDayStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poeDayStop.setStatus("current")
_PoeStatusTable_Object = MibTable
poeStatusTable = _PoeStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 40, 6)
)
if mibBuilder.loadTexts:
    poeStatusTable.setStatus("current")
_PoeStatusEntry_Object = MibTableRow
poeStatusEntry = _PoeStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 40, 6, 1)
)
poeStatusEntry.setIndexNames(
    (0, "MOXA-EDSP506E-MIB", "poePortIndex"),
)
if mibBuilder.loadTexts:
    poeStatusEntry.setStatus("current")


class _PoePortStatus_Type(Integer32):
    """Custom type poePortStatus based on Integer32"""
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


_PoePortStatus_Type.__name__ = "Integer32"
_PoePortStatus_Object = MibTableColumn
poePortStatus = _PoePortStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 40, 6, 1, 1),
    _PoePortStatus_Type()
)
poePortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poePortStatus.setStatus("current")


class _PoePortConsumption_Type(Integer32):
    """Custom type poePortConsumption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("na", -1)
    )


_PoePortConsumption_Type.__name__ = "Integer32"
_PoePortConsumption_Object = MibTableColumn
poePortConsumption = _PoePortConsumption_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 40, 6, 1, 2),
    _PoePortConsumption_Type()
)
poePortConsumption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poePortConsumption.setStatus("current")


class _PoePortVoltage_Type(Integer32):
    """Custom type poePortVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("na", -1)
    )


_PoePortVoltage_Type.__name__ = "Integer32"
_PoePortVoltage_Object = MibTableColumn
poePortVoltage = _PoePortVoltage_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 40, 6, 1, 3),
    _PoePortVoltage_Type()
)
poePortVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poePortVoltage.setStatus("current")


class _PoePortCurrent_Type(Integer32):
    """Custom type poePortCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("na", -1)
    )


_PoePortCurrent_Type.__name__ = "Integer32"
_PoePortCurrent_Object = MibTableColumn
poePortCurrent = _PoePortCurrent_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 40, 6, 1, 4),
    _PoePortCurrent_Type()
)
poePortCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poePortCurrent.setStatus("current")


class _PoePortPowerOutput_Type(Integer32):
    """Custom type poePortPowerOutput based on Integer32"""
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


_PoePortPowerOutput_Type.__name__ = "Integer32"
_PoePortPowerOutput_Object = MibTableColumn
poePortPowerOutput = _PoePortPowerOutput_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 40, 6, 1, 5),
    _PoePortPowerOutput_Type()
)
poePortPowerOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poePortPowerOutput.setStatus("current")


class _PoePortClass_Type(Integer32):
    """Custom type poePortClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-2,
              -1)
        )
    )
    namedValues = NamedValues(
        *(("na", -2),
          ("unknown", -1))
    )


_PoePortClass_Type.__name__ = "Integer32"
_PoePortClass_Object = MibTableColumn
poePortClass = _PoePortClass_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 40, 6, 1, 6),
    _PoePortClass_Type()
)
poePortClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poePortClass.setStatus("current")


class _PoePortPdFailCheck_Type(Integer32):
    """Custom type poePortPdFailCheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notAlive", 0),
          ("alive", 1),
          ("disable", 2))
    )


_PoePortPdFailCheck_Type.__name__ = "Integer32"
_PoePortPdFailCheck_Object = MibTableColumn
poePortPdFailCheck = _PoePortPdFailCheck_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 40, 6, 1, 7),
    _PoePortPdFailCheck_Type()
)
poePortPdFailCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poePortPdFailCheck.setStatus("current")


class _PoePortPdStatusDescription_Type(Integer32):
    """Custom type poePortPdStatusDescription based on Integer32"""
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
          ("notPresent", 1),
          ("powered", 2),
          ("nic", 3),
          ("fault", 4),
          ("legacyPowered", 5),
          ("potentialLegacyPD", 6))
    )


_PoePortPdStatusDescription_Type.__name__ = "Integer32"
_PoePortPdStatusDescription_Object = MibTableColumn
poePortPdStatusDescription = _PoePortPdStatusDescription_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 40, 6, 1, 8),
    _PoePortPdStatusDescription_Type()
)
poePortPdStatusDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poePortPdStatusDescription.setStatus("current")
_PoeSystemSetting_ObjectIdentity = ObjectIdentity
poeSystemSetting = _PoeSystemSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 40, 9)
)


class _PoeSysPowerEnable_Type(Integer32):
    """Custom type poeSysPowerEnable based on Integer32"""
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


_PoeSysPowerEnable_Type.__name__ = "Integer32"
_PoeSysPowerEnable_Object = MibScalar
poeSysPowerEnable = _PoeSysPowerEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 40, 9, 1),
    _PoeSysPowerEnable_Type()
)
poeSysPowerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poeSysPowerEnable.setStatus("current")
_PoeSysPowerThreshold_Type = Integer32
_PoeSysPowerThreshold_Object = MibScalar
poeSysPowerThreshold = _PoeSysPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 40, 9, 2),
    _PoeSysPowerThreshold_Type()
)
poeSysPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poeSysPowerThreshold.setStatus("current")


class _PoeSysThresholdCutOff_Type(Integer32):
    """Custom type poeSysThresholdCutOff based on Integer32"""
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


_PoeSysThresholdCutOff_Type.__name__ = "Integer32"
_PoeSysThresholdCutOff_Object = MibScalar
poeSysThresholdCutOff = _PoeSysThresholdCutOff_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 40, 9, 3),
    _PoeSysThresholdCutOff_Type()
)
poeSysThresholdCutOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poeSysThresholdCutOff.setStatus("current")
_PoeSysAllocatedPower_Type = Integer32
_PoeSysAllocatedPower_Object = MibScalar
poeSysAllocatedPower = _PoeSysAllocatedPower_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 40, 9, 4),
    _PoeSysAllocatedPower_Type()
)
poeSysAllocatedPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poeSysAllocatedPower.setStatus("current")
_PoeSysMeasuredPower_Type = Integer32
_PoeSysMeasuredPower_Object = MibScalar
poeSysMeasuredPower = _PoeSysMeasuredPower_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 40, 9, 5),
    _PoeSysMeasuredPower_Type()
)
poeSysMeasuredPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poeSysMeasuredPower.setStatus("current")
_PoeSysPowerBudget_Type = Integer32
_PoeSysPowerBudget_Object = MibScalar
poeSysPowerBudget = _PoeSysPowerBudget_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 40, 9, 7),
    _PoeSysPowerBudget_Type()
)
poeSysPowerBudget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poeSysPowerBudget.setStatus("current")
_Ieee1588Setting_ObjectIdentity = ObjectIdentity
ieee1588Setting = _Ieee1588Setting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 41)
)
_Ptpv1Setting_ObjectIdentity = ObjectIdentity
ptpv1Setting = _Ptpv1Setting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 41, 1)
)


class _EnablePtpv1_Type(Integer32):
    """Custom type enablePtpv1 based on Integer32"""
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


_EnablePtpv1_Type.__name__ = "Integer32"
_EnablePtpv1_Object = MibScalar
enablePtpv1 = _EnablePtpv1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 41, 1, 1),
    _EnablePtpv1_Type()
)
enablePtpv1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enablePtpv1.setStatus("current")


class _ClockModev1_Type(Integer32):
    """Custom type clockModev1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("v1BC", 0),
          ("v2E2E2stepTC", 1),
          ("v2P2PTC", 3),
          ("v2E2EBC", 4),
          ("v2P2PBC", 5))
    )


_ClockModev1_Type.__name__ = "Integer32"
_ClockModev1_Object = MibScalar
clockModev1 = _ClockModev1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 41, 1, 2),
    _ClockModev1_Type()
)
clockModev1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clockModev1.setStatus("current")


class _SyncIntervalv1_Type(Integer32):
    """Custom type syncIntervalv1 based on Integer32"""
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
        *(("oneSec", 0),
          ("twoSec", 1),
          ("fourSec", 2),
          ("eightSec", 3),
          ("sixteenSec", 4))
    )


_SyncIntervalv1_Type.__name__ = "Integer32"
_SyncIntervalv1_Object = MibScalar
syncIntervalv1 = _SyncIntervalv1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 41, 1, 3),
    _SyncIntervalv1_Type()
)
syncIntervalv1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syncIntervalv1.setStatus("current")


class _SubDomainNamev1_Type(Integer32):
    """Custom type subDomainNamev1 based on Integer32"""
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
        *(("dflt", 0),
          ("alt1", 1),
          ("alt2", 2),
          ("alt3", 3))
    )


_SubDomainNamev1_Type.__name__ = "Integer32"
_SubDomainNamev1_Object = MibScalar
subDomainNamev1 = _SubDomainNamev1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 41, 1, 4),
    _SubDomainNamev1_Type()
)
subDomainNamev1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subDomainNamev1.setStatus("current")


class _PreferMasterv1_Type(Integer32):
    """Custom type preferMasterv1 based on Integer32"""
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


_PreferMasterv1_Type.__name__ = "Integer32"
_PreferMasterv1_Object = MibScalar
preferMasterv1 = _PreferMasterv1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 41, 1, 5),
    _PreferMasterv1_Type()
)
preferMasterv1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    preferMasterv1.setStatus("current")
_Ptpv2Setting_ObjectIdentity = ObjectIdentity
ptpv2Setting = _Ptpv2Setting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 41, 2)
)


class _EnablePtp_Type(Integer32):
    """Custom type enablePtp based on Integer32"""
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


_EnablePtp_Type.__name__ = "Integer32"
_EnablePtp_Object = MibScalar
enablePtp = _EnablePtp_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 41, 2, 1),
    _EnablePtp_Type()
)
enablePtp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enablePtp.setStatus("current")


class _ClockMode_Type(Integer32):
    """Custom type clockMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("v1BC", 0),
          ("v2E2E2stepTC", 1),
          ("v2P2PTC", 3),
          ("v2E2EBC", 4),
          ("v2P2PBC", 5))
    )


_ClockMode_Type.__name__ = "Integer32"
_ClockMode_Object = MibScalar
clockMode = _ClockMode_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 41, 2, 2),
    _ClockMode_Type()
)
clockMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clockMode.setStatus("current")


class _Transport_Type(Integer32):
    """Custom type transport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ieee802dot3", 0),
          ("ipv4", 1))
    )


_Transport_Type.__name__ = "Integer32"
_Transport_Object = MibScalar
transport = _Transport_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 41, 2, 3),
    _Transport_Type()
)
transport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transport.setStatus("current")


class _SyncInterval_Type(Integer32):
    """Custom type syncInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-3,
              -2,
              -1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("t128msec", -3),
          ("t256msec", -2),
          ("t512msec", -1),
          ("t1sec", 0),
          ("t2sec", 1))
    )


_SyncInterval_Type.__name__ = "Integer32"
_SyncInterval_Object = MibScalar
syncInterval = _SyncInterval_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 41, 2, 4),
    _SyncInterval_Type()
)
syncInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syncInterval.setStatus("current")


class _LogMinDelayReqInterval_Type(Integer32):
    """Custom type logMinDelayReqInterval based on Integer32"""
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
        *(("t1sec", 0),
          ("t2sec", 1),
          ("t4sec", 2),
          ("t8sec", 3),
          ("t16sec", 4),
          ("t32sec", 5))
    )


_LogMinDelayReqInterval_Type.__name__ = "Integer32"
_LogMinDelayReqInterval_Object = MibScalar
logMinDelayReqInterval = _LogMinDelayReqInterval_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 41, 2, 5),
    _LogMinDelayReqInterval_Type()
)
logMinDelayReqInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logMinDelayReqInterval.setStatus("current")


class _LogMinPdelayReqInterval_Type(Integer32):
    """Custom type logMinPdelayReqInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("t512msec", -1),
          ("t1sec", 0),
          ("t2sec", 1),
          ("t4sec", 2),
          ("t8sec", 3),
          ("t16sec", 4),
          ("t32sec", 5))
    )


_LogMinPdelayReqInterval_Type.__name__ = "Integer32"
_LogMinPdelayReqInterval_Object = MibScalar
logMinPdelayReqInterval = _LogMinPdelayReqInterval_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 41, 2, 6),
    _LogMinPdelayReqInterval_Type()
)
logMinPdelayReqInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logMinPdelayReqInterval.setStatus("current")


class _LogAnnounceInterval_Type(Integer32):
    """Custom type logAnnounceInterval based on Integer32"""
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
        *(("t1sec", 0),
          ("t2sec", 1),
          ("t4sec", 2),
          ("t8sec", 3),
          ("t16sec", 4))
    )


_LogAnnounceInterval_Type.__name__ = "Integer32"
_LogAnnounceInterval_Object = MibScalar
logAnnounceInterval = _LogAnnounceInterval_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 41, 2, 7),
    _LogAnnounceInterval_Type()
)
logAnnounceInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logAnnounceInterval.setStatus("current")


class _AnnounceReceiptTimeout_Type(Integer32):
    """Custom type announceReceiptTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_AnnounceReceiptTimeout_Type.__name__ = "Integer32"
_AnnounceReceiptTimeout_Object = MibScalar
announceReceiptTimeout = _AnnounceReceiptTimeout_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 41, 2, 8),
    _AnnounceReceiptTimeout_Type()
)
announceReceiptTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    announceReceiptTimeout.setStatus("current")
_Priority1_Type = Integer32
_Priority1_Object = MibScalar
priority1 = _Priority1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 41, 2, 9),
    _Priority1_Type()
)
priority1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    priority1.setStatus("current")
_Priority2_Type = Integer32
_Priority2_Object = MibScalar
priority2 = _Priority2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 41, 2, 10),
    _Priority2_Type()
)
priority2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    priority2.setStatus("current")
_ClockClass_Type = Integer32
_ClockClass_Object = MibScalar
clockClass = _ClockClass_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 41, 2, 11),
    _ClockClass_Type()
)
clockClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clockClass.setStatus("current")


class _DomainNumber_Type(Integer32):
    """Custom type domainNumber based on Integer32"""
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
        *(("dflt", 0),
          ("alt1", 1),
          ("alt2", 2),
          ("alt3", 3))
    )


_DomainNumber_Type.__name__ = "Integer32"
_DomainNumber_Object = MibScalar
domainNumber = _DomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 41, 2, 12),
    _DomainNumber_Type()
)
domainNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    domainNumber.setStatus("current")
_LocalUtcOffset_Type = Integer32
_LocalUtcOffset_Object = MibScalar
localUtcOffset = _LocalUtcOffset_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 41, 2, 13),
    _LocalUtcOffset_Type()
)
localUtcOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localUtcOffset.setStatus("current")


class _LocalUtcOffsetValid_Type(Integer32):
    """Custom type localUtcOffsetValid based on Integer32"""
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


_LocalUtcOffsetValid_Type.__name__ = "Integer32"
_LocalUtcOffsetValid_Object = MibScalar
localUtcOffsetValid = _LocalUtcOffsetValid_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 41, 2, 14),
    _LocalUtcOffsetValid_Type()
)
localUtcOffsetValid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localUtcOffsetValid.setStatus("current")


class _LocalLeap59_Type(Integer32):
    """Custom type localLeap59 based on Integer32"""
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


_LocalLeap59_Type.__name__ = "Integer32"
_LocalLeap59_Object = MibScalar
localLeap59 = _LocalLeap59_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 41, 2, 15),
    _LocalLeap59_Type()
)
localLeap59.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localLeap59.setStatus("current")


class _LocalLeap61_Type(Integer32):
    """Custom type localLeap61 based on Integer32"""
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


_LocalLeap61_Type.__name__ = "Integer32"
_LocalLeap61_Object = MibScalar
localLeap61 = _LocalLeap61_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 41, 2, 16),
    _LocalLeap61_Type()
)
localLeap61.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localLeap61.setStatus("current")


class _LocalPtpTimescale_Type(Integer32):
    """Custom type localPtpTimescale based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("arb", 0),
          ("ptp", 1))
    )


_LocalPtpTimescale_Type.__name__ = "Integer32"
_LocalPtpTimescale_Object = MibScalar
localPtpTimescale = _LocalPtpTimescale_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 41, 2, 17),
    _LocalPtpTimescale_Type()
)
localPtpTimescale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localPtpTimescale.setStatus("current")
_LocalArbTime_Type = Integer32
_LocalArbTime_Object = MibScalar
localArbTime = _LocalArbTime_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 41, 2, 18),
    _LocalArbTime_Type()
)
localArbTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localArbTime.setStatus("current")
_Ptpv1Status_ObjectIdentity = ObjectIdentity
ptpv1Status = _Ptpv1Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 41, 3)
)
_OffsetToMasterv1_Type = Integer32
_OffsetToMasterv1_Object = MibScalar
offsetToMasterv1 = _OffsetToMasterv1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 41, 3, 1),
    _OffsetToMasterv1_Type()
)
offsetToMasterv1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    offsetToMasterv1.setStatus("current")
_MeanPathDelayv1_Type = Integer32
_MeanPathDelayv1_Object = MibScalar
meanPathDelayv1 = _MeanPathDelayv1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 41, 3, 2),
    _MeanPathDelayv1_Type()
)
meanPathDelayv1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meanPathDelayv1.setStatus("current")
_GrandMasterUuidv1_Type = MacAddress
_GrandMasterUuidv1_Object = MibScalar
grandMasterUuidv1 = _GrandMasterUuidv1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 41, 3, 3),
    _GrandMasterUuidv1_Type()
)
grandMasterUuidv1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grandMasterUuidv1.setStatus("current")
_ParentUuidv1_Type = MacAddress
_ParentUuidv1_Object = MibScalar
parentUuidv1 = _ParentUuidv1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 41, 3, 4),
    _ParentUuidv1_Type()
)
parentUuidv1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parentUuidv1.setStatus("current")
_ClockStratumv1_Type = Integer32
_ClockStratumv1_Object = MibScalar
clockStratumv1 = _ClockStratumv1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 41, 3, 5),
    _ClockStratumv1_Type()
)
clockStratumv1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clockStratumv1.setStatus("current")
_ClockIdentifierv1_Type = DisplayString
_ClockIdentifierv1_Object = MibScalar
clockIdentifierv1 = _ClockIdentifierv1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 41, 3, 6),
    _ClockIdentifierv1_Type()
)
clockIdentifierv1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clockIdentifierv1.setStatus("current")
_Ptpv2Status_ObjectIdentity = ObjectIdentity
ptpv2Status = _Ptpv2Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 41, 4)
)
_OffsetToMaster_Type = Integer32
_OffsetToMaster_Object = MibScalar
offsetToMaster = _OffsetToMaster_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 41, 4, 1),
    _OffsetToMaster_Type()
)
offsetToMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    offsetToMaster.setStatus("current")
_MeanPathDelay_Type = Integer32
_MeanPathDelay_Object = MibScalar
meanPathDelay = _MeanPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 41, 4, 2),
    _MeanPathDelay_Type()
)
meanPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meanPathDelay.setStatus("current")
_ParentIdentity_Type = DisplayString
_ParentIdentity_Object = MibScalar
parentIdentity = _ParentIdentity_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 41, 4, 3),
    _ParentIdentity_Type()
)
parentIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parentIdentity.setStatus("current")
_GrandmasterIdentity_Type = DisplayString
_GrandmasterIdentity_Object = MibScalar
grandmasterIdentity = _GrandmasterIdentity_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 41, 4, 4),
    _GrandmasterIdentity_Type()
)
grandmasterIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grandmasterIdentity.setStatus("current")
_GrandmasterClockClass_Type = Integer32
_GrandmasterClockClass_Object = MibScalar
grandmasterClockClass = _GrandmasterClockClass_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 41, 4, 5),
    _GrandmasterClockClass_Type()
)
grandmasterClockClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grandmasterClockClass.setStatus("current")
_GrandmasterClockAccuracy_Type = Integer32
_GrandmasterClockAccuracy_Object = MibScalar
grandmasterClockAccuracy = _GrandmasterClockAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 41, 4, 6),
    _GrandmasterClockAccuracy_Type()
)
grandmasterClockAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grandmasterClockAccuracy.setStatus("current")
_GrandmasterPriority1_Type = Integer32
_GrandmasterPriority1_Object = MibScalar
grandmasterPriority1 = _GrandmasterPriority1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 41, 4, 7),
    _GrandmasterPriority1_Type()
)
grandmasterPriority1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grandmasterPriority1.setStatus("current")
_GrandmasterPriority2_Type = Integer32
_GrandmasterPriority2_Object = MibScalar
grandmasterPriority2 = _GrandmasterPriority2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 41, 4, 8),
    _GrandmasterPriority2_Type()
)
grandmasterPriority2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grandmasterPriority2.setStatus("current")
_StepsRemoved_Type = Integer32
_StepsRemoved_Object = MibScalar
stepsRemoved = _StepsRemoved_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 41, 4, 9),
    _StepsRemoved_Type()
)
stepsRemoved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stepsRemoved.setStatus("current")
_CurrentUtcOffset_Type = Integer32
_CurrentUtcOffset_Object = MibScalar
currentUtcOffset = _CurrentUtcOffset_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 41, 4, 10),
    _CurrentUtcOffset_Type()
)
currentUtcOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentUtcOffset.setStatus("current")
_CurrentUtcOffsetValid_Type = DisplayString
_CurrentUtcOffsetValid_Object = MibScalar
currentUtcOffsetValid = _CurrentUtcOffsetValid_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 41, 4, 11),
    _CurrentUtcOffsetValid_Type()
)
currentUtcOffsetValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentUtcOffsetValid.setStatus("current")
_Leap59_Type = DisplayString
_Leap59_Object = MibScalar
leap59 = _Leap59_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 41, 4, 12),
    _Leap59_Type()
)
leap59.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    leap59.setStatus("current")
_Leap61_Type = DisplayString
_Leap61_Object = MibScalar
leap61 = _Leap61_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 41, 4, 13),
    _Leap61_Type()
)
leap61.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    leap61.setStatus("current")
_PtpTimescale_Type = DisplayString
_PtpTimescale_Object = MibScalar
ptpTimescale = _PtpTimescale_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 41, 4, 14),
    _PtpTimescale_Type()
)
ptpTimescale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpTimescale.setStatus("current")
_Timesource_Type = DisplayString
_Timesource_Object = MibScalar
timesource = _Timesource_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 41, 4, 15),
    _Timesource_Type()
)
timesource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timesource.setStatus("current")
_PtpPortTable_Object = MibTable
ptpPortTable = _PtpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 41, 5)
)
if mibBuilder.loadTexts:
    ptpPortTable.setStatus("current")
_PtpPortEntry_Object = MibTableRow
ptpPortEntry = _PtpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 41, 5, 1)
)
ptpPortEntry.setIndexNames(
    (0, "MOXA-EDSP506E-MIB", "ptpPortIndex"),
)
if mibBuilder.loadTexts:
    ptpPortEntry.setStatus("current")
_PtpPortIndex_Type = Integer32
_PtpPortIndex_Object = MibTableColumn
ptpPortIndex = _PtpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 41, 5, 1, 1),
    _PtpPortIndex_Type()
)
ptpPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpPortIndex.setStatus("current")


class _PtpPortEnable_Type(Integer32):
    """Custom type ptpPortEnable based on Integer32"""
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


_PtpPortEnable_Type.__name__ = "Integer32"
_PtpPortEnable_Object = MibTableColumn
ptpPortEnable = _PtpPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 41, 5, 1, 2),
    _PtpPortEnable_Type()
)
ptpPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptpPortEnable.setStatus("current")


class _PtpPortStatus_Type(Integer32):
    """Custom type ptpPortStatus based on Integer32"""
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
        *(("ptpInitializing", 0),
          ("ptpFaulty", 1),
          ("ptpDisabled", 2),
          ("ptpListening", 3),
          ("ptpPreMaster", 4),
          ("ptpMaster", 5),
          ("ptpPassive", 6),
          ("ptpUncalibrated", 7),
          ("ptpSlave", 8))
    )


_PtpPortStatus_Type.__name__ = "Integer32"
_PtpPortStatus_Object = MibTableColumn
ptpPortStatus = _PtpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 41, 5, 1, 3),
    _PtpPortStatus_Type()
)
ptpPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpPortStatus.setStatus("current")
_Diagnosis_ObjectIdentity = ObjectIdentity
diagnosis = _Diagnosis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 42)
)
_LldpSetting_ObjectIdentity = ObjectIdentity
lldpSetting = _LldpSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 42, 1)
)


class _EnableLLDP_Type(Integer32):
    """Custom type enableLLDP based on Integer32"""
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


_EnableLLDP_Type.__name__ = "Integer32"
_EnableLLDP_Object = MibScalar
enableLLDP = _EnableLLDP_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 42, 1, 1),
    _EnableLLDP_Type()
)
enableLLDP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableLLDP.setStatus("current")
_LldpMSGInterval_Type = Integer32
_LldpMSGInterval_Object = MibScalar
lldpMSGInterval = _LldpMSGInterval_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 42, 1, 2),
    _LldpMSGInterval_Type()
)
lldpMSGInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpMSGInterval.setStatus("current")
_AgingTime_Type = Integer32
_AgingTime_Object = MibScalar
agingTime = _AgingTime_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 44),
    _AgingTime_Type()
)
agingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agingTime.setStatus("current")
_GarpSetting_ObjectIdentity = ObjectIdentity
garpSetting = _GarpSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 45)
)
_JoinTime_Type = Integer32
_JoinTime_Object = MibScalar
joinTime = _JoinTime_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 45, 1),
    _JoinTime_Type()
)
joinTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    joinTime.setStatus("current")
_LeaveTime_Type = Integer32
_LeaveTime_Object = MibScalar
leaveTime = _LeaveTime_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 45, 2),
    _LeaveTime_Type()
)
leaveTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    leaveTime.setStatus("current")
_LeaveAllTime_Type = Integer32
_LeaveAllTime_Object = MibScalar
leaveAllTime = _LeaveAllTime_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 45, 3),
    _LeaveAllTime_Type()
)
leaveAllTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    leaveAllTime.setStatus("current")
_Eventlog_ObjectIdentity = ObjectIdentity
eventlog = _Eventlog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 46)
)
_EventlogTable_Object = MibTable
eventlogTable = _EventlogTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 46, 1)
)
if mibBuilder.loadTexts:
    eventlogTable.setStatus("current")
_EventlogEntry_Object = MibTableRow
eventlogEntry = _EventlogEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 46, 1, 1)
)
eventlogEntry.setIndexNames(
    (0, "MOXA-EDSP506E-MIB", "eventlogIndex"),
)
if mibBuilder.loadTexts:
    eventlogEntry.setStatus("current")
_EventlogIndex_Type = Integer32
_EventlogIndex_Object = MibTableColumn
eventlogIndex = _EventlogIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 46, 1, 1, 1),
    _EventlogIndex_Type()
)
eventlogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventlogIndex.setStatus("current")
_EventlogBootup_Type = Integer32
_EventlogBootup_Object = MibTableColumn
eventlogBootup = _EventlogBootup_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 46, 1, 1, 2),
    _EventlogBootup_Type()
)
eventlogBootup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventlogBootup.setStatus("current")
_EventlogDate_Type = DisplayString
_EventlogDate_Object = MibTableColumn
eventlogDate = _EventlogDate_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 46, 1, 1, 3),
    _EventlogDate_Type()
)
eventlogDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventlogDate.setStatus("current")
_EventlogTime_Type = DisplayString
_EventlogTime_Object = MibTableColumn
eventlogTime = _EventlogTime_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 46, 1, 1, 4),
    _EventlogTime_Type()
)
eventlogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventlogTime.setStatus("current")
_EventlogUptime_Type = DisplayString
_EventlogUptime_Object = MibTableColumn
eventlogUptime = _EventlogUptime_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 46, 1, 1, 5),
    _EventlogUptime_Type()
)
eventlogUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventlogUptime.setStatus("current")
_EventlogEvent_Type = DisplayString
_EventlogEvent_Object = MibTableColumn
eventlogEvent = _EventlogEvent_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 46, 1, 1, 6),
    _EventlogEvent_Type()
)
eventlogEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventlogEvent.setStatus("current")


class _EventlogClear_Type(Integer32):
    """Custom type eventlogClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noop", 0),
          ("clear", 1))
    )


_EventlogClear_Type.__name__ = "Integer32"
_EventlogClear_Object = MibScalar
eventlogClear = _EventlogClear_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 46, 2),
    _EventlogClear_Type()
)
eventlogClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventlogClear.setStatus("current")
_IndustrialProtocol_ObjectIdentity = ObjectIdentity
industrialProtocol = _IndustrialProtocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 47)
)
_EipSetting_ObjectIdentity = ObjectIdentity
eipSetting = _EipSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 47, 1)
)


class _EnableEtherNetIP_Type(Integer32):
    """Custom type enableEtherNetIP based on Integer32"""
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


_EnableEtherNetIP_Type.__name__ = "Integer32"
_EnableEtherNetIP_Object = MibScalar
enableEtherNetIP = _EnableEtherNetIP_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 47, 1, 1),
    _EnableEtherNetIP_Type()
)
enableEtherNetIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableEtherNetIP.setStatus("current")
_ModbusSetting_ObjectIdentity = ObjectIdentity
modbusSetting = _ModbusSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 47, 2)
)


class _EnableModbus_Type(Integer32):
    """Custom type enableModbus based on Integer32"""
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


_EnableModbus_Type.__name__ = "Integer32"
_EnableModbus_Object = MibScalar
enableModbus = _EnableModbus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 47, 2, 1),
    _EnableModbus_Type()
)
enableModbus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableModbus.setStatus("current")
_ProfinetioSetting_ObjectIdentity = ObjectIdentity
profinetioSetting = _ProfinetioSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 47, 3)
)


class _EnableProfinetIO_Type(Integer32):
    """Custom type enableProfinetIO based on Integer32"""
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


_EnableProfinetIO_Type.__name__ = "Integer32"
_EnableProfinetIO_Object = MibScalar
enableProfinetIO = _EnableProfinetIO_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 47, 3, 1),
    _EnableProfinetIO_Type()
)
enableProfinetIO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableProfinetIO.setStatus("current")


class _EnableFactoryDefault_Type(Integer32):
    """Custom type enableFactoryDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("activate", 1)
    )


_EnableFactoryDefault_Type.__name__ = "Integer32"
_EnableFactoryDefault_Object = MibScalar
enableFactoryDefault = _EnableFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 48),
    _EnableFactoryDefault_Type()
)
enableFactoryDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableFactoryDefault.setStatus("current")


class _ConsoleLoginMode_Type(Integer32):
    """Custom type consoleLoginMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("menu", 0),
          ("cli", 1))
    )


_ConsoleLoginMode_Type.__name__ = "Integer32"
_ConsoleLoginMode_Object = MibScalar
consoleLoginMode = _ConsoleLoginMode_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 51),
    _ConsoleLoginMode_Type()
)
consoleLoginMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consoleLoginMode.setStatus("current")
_AccessControlList_ObjectIdentity = ObjectIdentity
accessControlList = _AccessControlList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 52)
)
_AccessControlTable_Object = MibTable
accessControlTable = _AccessControlTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 52, 1)
)
if mibBuilder.loadTexts:
    accessControlTable.setStatus("current")
_AccessControlEntry_Object = MibTableRow
accessControlEntry = _AccessControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 52, 1, 1)
)
accessControlEntry.setIndexNames(
    (0, "MOXA-EDSP506E-MIB", "aclRuleIndex"),
)
if mibBuilder.loadTexts:
    accessControlEntry.setStatus("current")
_AclRuleIndex_Type = Integer32
_AclRuleIndex_Object = MibTableColumn
aclRuleIndex = _AclRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 52, 1, 1, 1),
    _AclRuleIndex_Type()
)
aclRuleIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRuleIndex.setStatus("current")
_ListID_Type = Integer32
_ListID_Object = MibTableColumn
listID = _ListID_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 52, 1, 1, 2),
    _ListID_Type()
)
listID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    listID.setStatus("current")


class _FilterType_Type(Integer32):
    """Custom type filterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ipBase", 0),
          ("macBase", 1))
    )


_FilterType_Type.__name__ = "Integer32"
_FilterType_Object = MibTableColumn
filterType = _FilterType_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 52, 1, 1, 3),
    _FilterType_Type()
)
filterType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    filterType.setStatus("current")


class _ActionFlag_Type(Integer32):
    """Custom type actionFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("permit", 0),
          ("deny", 1))
    )


_ActionFlag_Type.__name__ = "Integer32"
_ActionFlag_Object = MibTableColumn
actionFlag = _ActionFlag_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 52, 1, 1, 4),
    _ActionFlag_Type()
)
actionFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    actionFlag.setStatus("current")
_SrcMacAddr_Type = MacAddress
_SrcMacAddr_Object = MibTableColumn
srcMacAddr = _SrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 52, 1, 1, 5),
    _SrcMacAddr_Type()
)
srcMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    srcMacAddr.setStatus("current")
_SrcMacMask_Type = MacAddress
_SrcMacMask_Object = MibTableColumn
srcMacMask = _SrcMacMask_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 52, 1, 1, 6),
    _SrcMacMask_Type()
)
srcMacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    srcMacMask.setStatus("current")
_DstMacAddr_Type = MacAddress
_DstMacAddr_Object = MibTableColumn
dstMacAddr = _DstMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 52, 1, 1, 7),
    _DstMacAddr_Type()
)
dstMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dstMacAddr.setStatus("current")
_DstMacMask_Type = MacAddress
_DstMacMask_Object = MibTableColumn
dstMacMask = _DstMacMask_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 52, 1, 1, 8),
    _DstMacMask_Type()
)
dstMacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dstMacMask.setStatus("current")
_EtherType_Type = Integer32
_EtherType_Object = MibTableColumn
etherType = _EtherType_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 52, 1, 1, 9),
    _EtherType_Type()
)
etherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etherType.setStatus("current")


class _VlanID_Type(Integer32):
    """Custom type vlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_VlanID_Type.__name__ = "Integer32"
_VlanID_Object = MibTableColumn
vlanID = _VlanID_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 52, 1, 1, 10),
    _VlanID_Type()
)
vlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanID.setStatus("current")
_SrcIpAddr_Type = IpAddress
_SrcIpAddr_Object = MibTableColumn
srcIpAddr = _SrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 52, 1, 1, 11),
    _SrcIpAddr_Type()
)
srcIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    srcIpAddr.setStatus("current")
_SrcNetmask_Type = IpAddress
_SrcNetmask_Object = MibTableColumn
srcNetmask = _SrcNetmask_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 52, 1, 1, 12),
    _SrcNetmask_Type()
)
srcNetmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    srcNetmask.setStatus("current")
_DstIpAddr_Type = IpAddress
_DstIpAddr_Object = MibTableColumn
dstIpAddr = _DstIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 52, 1, 1, 13),
    _DstIpAddr_Type()
)
dstIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dstIpAddr.setStatus("current")
_DstNetmask_Type = IpAddress
_DstNetmask_Object = MibTableColumn
dstNetmask = _DstNetmask_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 52, 1, 1, 14),
    _DstNetmask_Type()
)
dstNetmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dstNetmask.setStatus("current")
_ProtocolCode_Type = Integer32
_ProtocolCode_Object = MibTableColumn
protocolCode = _ProtocolCode_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 52, 1, 1, 15),
    _ProtocolCode_Type()
)
protocolCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    protocolCode.setStatus("current")
_SrcsocketPort_Type = Integer32
_SrcsocketPort_Object = MibTableColumn
srcsocketPort = _SrcsocketPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 52, 1, 1, 16),
    _SrcsocketPort_Type()
)
srcsocketPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    srcsocketPort.setStatus("current")
_DstsocketPort_Type = Integer32
_DstsocketPort_Object = MibTableColumn
dstsocketPort = _DstsocketPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 52, 1, 1, 17),
    _DstsocketPort_Type()
)
dstsocketPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dstsocketPort.setStatus("current")


class _AclStatus_Type(Integer32):
    """Custom type aclStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6))
    )


_AclStatus_Type.__name__ = "Integer32"
_AclStatus_Object = MibTableColumn
aclStatus = _AclStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 52, 1, 1, 18),
    _AclStatus_Type()
)
aclStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclStatus.setStatus("current")
_AclAttachmentTable_Object = MibTable
aclAttachmentTable = _AclAttachmentTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 52, 2)
)
if mibBuilder.loadTexts:
    aclAttachmentTable.setStatus("current")
_AclAttachmentEntry_Object = MibTableRow
aclAttachmentEntry = _AclAttachmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 52, 2, 1)
)
aclAttachmentEntry.setIndexNames(
    (0, "MOXA-EDSP506E-MIB", "aclID"),
)
if mibBuilder.loadTexts:
    aclAttachmentEntry.setStatus("current")
_AclID_Type = Integer32
_AclID_Object = MibTableColumn
aclID = _AclID_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 52, 2, 1, 1),
    _AclID_Type()
)
aclID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclID.setStatus("current")
_IngressPort_Type = PortList
_IngressPort_Object = MibTableColumn
ingressPort = _IngressPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 52, 2, 1, 2),
    _IngressPort_Type()
)
ingressPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ingressPort.setStatus("current")
_AclListName_Type = DisplayString
_AclListName_Object = MibTableColumn
aclListName = _AclListName_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 52, 2, 1, 4),
    _AclListName_Type()
)
aclListName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclListName.setStatus("current")
_CpuLoading5s_Type = Integer32
_CpuLoading5s_Object = MibScalar
cpuLoading5s = _CpuLoading5s_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 53),
    _CpuLoading5s_Type()
)
cpuLoading5s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuLoading5s.setStatus("current")
_CpuLoading30s_Type = Integer32
_CpuLoading30s_Object = MibScalar
cpuLoading30s = _CpuLoading30s_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 54),
    _CpuLoading30s_Type()
)
cpuLoading30s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuLoading30s.setStatus("current")
_CpuLoading300s_Type = Integer32
_CpuLoading300s_Object = MibScalar
cpuLoading300s = _CpuLoading300s_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 55),
    _CpuLoading300s_Type()
)
cpuLoading300s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuLoading300s.setStatus("current")
_TotalMemory_Type = Integer32
_TotalMemory_Object = MibScalar
totalMemory = _TotalMemory_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 56),
    _TotalMemory_Type()
)
totalMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalMemory.setStatus("current")
_FreeMemory_Type = Integer32
_FreeMemory_Object = MibScalar
freeMemory = _FreeMemory_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 57),
    _FreeMemory_Type()
)
freeMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    freeMemory.setStatus("current")
_UsedMemory_Type = Integer32
_UsedMemory_Object = MibScalar
usedMemory = _UsedMemory_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 58),
    _UsedMemory_Type()
)
usedMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usedMemory.setStatus("current")
_MemoryUsage_Type = Integer32
_MemoryUsage_Object = MibScalar
memoryUsage = _MemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 59),
    _MemoryUsage_Type()
)
memoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryUsage.setStatus("current")


class _LoopProtection_Type(Integer32):
    """Custom type loopProtection based on Integer32"""
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


_LoopProtection_Type.__name__ = "Integer32"
_LoopProtection_Object = MibScalar
loopProtection = _LoopProtection_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 61),
    _LoopProtection_Type()
)
loopProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loopProtection.setStatus("current")
_EventSettings_ObjectIdentity = ObjectIdentity
eventSettings = _EventSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 62)
)
_SystemEventSettingsTable_Object = MibTable
systemEventSettingsTable = _SystemEventSettingsTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 62, 1)
)
if mibBuilder.loadTexts:
    systemEventSettingsTable.setStatus("current")
_SystemEventSettingsEntry_Object = MibTableRow
systemEventSettingsEntry = _SystemEventSettingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 62, 1, 1)
)
systemEventSettingsEntry.setIndexNames(
    (0, "MOXA-EDSP506E-MIB", "systemEventIndex"),
)
if mibBuilder.loadTexts:
    systemEventSettingsEntry.setStatus("current")
_SystemEventIndex_Type = Integer32
_SystemEventIndex_Object = MibTableColumn
systemEventIndex = _SystemEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 62, 1, 1, 1),
    _SystemEventIndex_Type()
)
systemEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemEventIndex.setStatus("current")


class _SystemEventActive_Type(Integer32):
    """Custom type systemEventActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_SystemEventActive_Type.__name__ = "Integer32"
_SystemEventActive_Object = MibTableColumn
systemEventActive = _SystemEventActive_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 62, 1, 1, 2),
    _SystemEventActive_Type()
)
systemEventActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemEventActive.setStatus("current")
_SystemEventName_Type = DisplayString
_SystemEventName_Object = MibTableColumn
systemEventName = _SystemEventName_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 62, 1, 1, 3),
    _SystemEventName_Type()
)
systemEventName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemEventName.setStatus("current")


class _SystemEventSupport_Type(Integer32):
    """Custom type systemEventSupport based on Integer32"""
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
              28,
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("support-SNMPTrap-only", 1),
          ("support-Email-only", 2),
          ("support-SNMP-Trap-Email", 3),
          ("support-Syslog-only", 4),
          ("support-SNMPTrap-Syslog", 5),
          ("support-Email-Syslog", 6),
          ("support-SNMPTrap-Email-Syslog", 7),
          ("support-Relay1-only", 8),
          ("support-SNMPTrap-Relay1", 9),
          ("support-Email-Relay1", 10),
          ("support-SNMPTrap-Email-Relay1", 11),
          ("support-Syslog-Relay1", 12),
          ("support-SNMPTrap-Syslog-Relay1", 13),
          ("support-Email-Syslog-Relay1", 14),
          ("support-SNMPTrap-Email-Syslog-Relay1", 15),
          ("support-Relay2-only", 16),
          ("support-SNMPTrap-Relay2", 17),
          ("support-Email-Relay2", 18),
          ("support-SNMPTrap-Email-Relay2", 19),
          ("support-Syslog-Relay2", 20),
          ("support-SNMPTrap-Syslog-Relay2", 21),
          ("support-Email-Syslog-Relay2", 22),
          ("support-SNMPTrap-Email-Syslog-Relay2", 23),
          ("support-Relay1-Relay2", 24),
          ("support-SNMPTrap-Relay1-Relay2", 25),
          ("support-Syslog-Relay1-Relay2", 28),
          ("support-Email-Syslog-Relay1-Relay2", 30),
          ("support-all-SNMPTrap-Email-Syslog-Relay1-Relay2", 31))
    )


_SystemEventSupport_Type.__name__ = "Integer32"
_SystemEventSupport_Object = MibTableColumn
systemEventSupport = _SystemEventSupport_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 62, 1, 1, 4),
    _SystemEventSupport_Type()
)
systemEventSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemEventSupport.setStatus("current")


class _SystemEventModuleEnable_Type(Integer32):
    """Custom type systemEventModuleEnable based on Integer32"""
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
              28,
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("enable-SNMPTrap-only", 1),
          ("enable-Email-only", 2),
          ("enable-SNMPTrap-Email", 3),
          ("enable-Syslog-only", 4),
          ("enable-SNMPTrap-Syslog", 5),
          ("enable-Email-Syslog", 6),
          ("enable-SNMPTrap-Email-Syslog", 7),
          ("enable-Relay1-only", 8),
          ("enable-SNMPTrap-Relay1", 9),
          ("enable-Email-Relay1", 10),
          ("enable-SNMPTrap-Email-Relay1", 11),
          ("enable-Syslog-Relay1", 12),
          ("enable-SNMPTrap-Syslog-Relay1", 13),
          ("enable-Email-Syslog-Relay1", 14),
          ("enable-SNMPTrap-Email-Syslog-Relay1", 15),
          ("enable-Relay2-only", 16),
          ("enable-SNMPTrap-Relay2", 17),
          ("enable-Email-Relay2", 18),
          ("enable-SNMPTrap-Email-Relay2", 19),
          ("enable-Syslog-Relay2", 20),
          ("enable-SNMPTrap-Syslog-Relay2", 21),
          ("enable-Email-Syslog-Relay2", 22),
          ("enable-SNMPTrap-Email-Syslog-Relay2", 23),
          ("enable-Relay1-Relay2", 24),
          ("enable-SNMPTrap-Relay1-Relay2", 25),
          ("enable-Syslog-Relay1-Relay2", 28),
          ("enable-Email-Syslog-Relay1-Relay2", 30),
          ("enable-All-SNMPTrap-Email-Syslog-Relay1-Relay2", 31))
    )


_SystemEventModuleEnable_Type.__name__ = "Integer32"
_SystemEventModuleEnable_Object = MibTableColumn
systemEventModuleEnable = _SystemEventModuleEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 62, 1, 1, 5),
    _SystemEventModuleEnable_Type()
)
systemEventModuleEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemEventModuleEnable.setStatus("current")


class _SystemEventSeverity_Type(Integer32):
    """Custom type systemEventSeverity based on Integer32"""
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
        *(("emergency", 0),
          ("alert", 1),
          ("critical", 2),
          ("error", 3),
          ("warning", 4),
          ("notice", 5),
          ("information", 6),
          ("debug", 7))
    )


_SystemEventSeverity_Type.__name__ = "Integer32"
_SystemEventSeverity_Object = MibTableColumn
systemEventSeverity = _SystemEventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 62, 1, 1, 6),
    _SystemEventSeverity_Type()
)
systemEventSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemEventSeverity.setStatus("current")
_PortEventSettingsTable_Object = MibTable
portEventSettingsTable = _PortEventSettingsTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 62, 2)
)
if mibBuilder.loadTexts:
    portEventSettingsTable.setStatus("current")
_PortEventSettingsEntry_Object = MibTableRow
portEventSettingsEntry = _PortEventSettingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 62, 2, 1)
)
portEventSettingsEntry.setIndexNames(
    (0, "MOXA-EDSP506E-MIB", "portEventIndex"),
)
if mibBuilder.loadTexts:
    portEventSettingsEntry.setStatus("current")
_PortEventIndex_Type = Integer32
_PortEventIndex_Object = MibTableColumn
portEventIndex = _PortEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 62, 2, 1, 1),
    _PortEventIndex_Type()
)
portEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portEventIndex.setStatus("current")
_PortEventLabel_Type = DisplayString
_PortEventLabel_Object = MibTableColumn
portEventLabel = _PortEventLabel_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 62, 2, 1, 2),
    _PortEventLabel_Type()
)
portEventLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portEventLabel.setStatus("current")


class _PortEventActive_Type(Integer32):
    """Custom type portEventActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_PortEventActive_Type.__name__ = "Integer32"
_PortEventActive_Object = MibTableColumn
portEventActive = _PortEventActive_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 62, 2, 1, 3),
    _PortEventActive_Type()
)
portEventActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portEventActive.setStatus("current")


class _PortEventEnable_Type(Integer32):
    """Custom type portEventEnable based on Integer32"""
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
          ("enable-LinkOn-only", 1),
          ("enable-LinkOff-only", 2),
          ("enable-LinkOn-LinkOff", 3),
          ("enable-TrafficOverload-only", 4),
          ("enable-LinkOn-TrafficOverload", 5),
          ("enable-LinkOff-TrafficOverload", 6),
          ("enable-All-LinkOn-LinkOff-TrafficOverload", 7))
    )


_PortEventEnable_Type.__name__ = "Integer32"
_PortEventEnable_Object = MibTableColumn
portEventEnable = _PortEventEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 62, 2, 1, 4),
    _PortEventEnable_Type()
)
portEventEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portEventEnable.setStatus("current")


class _PortEventTrafficThreshold_Type(Integer32):
    """Custom type portEventTrafficThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PortEventTrafficThreshold_Type.__name__ = "Integer32"
_PortEventTrafficThreshold_Object = MibTableColumn
portEventTrafficThreshold = _PortEventTrafficThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 62, 2, 1, 5),
    _PortEventTrafficThreshold_Type()
)
portEventTrafficThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portEventTrafficThreshold.setStatus("current")


class _PortEventTrafficDuration_Type(Integer32):
    """Custom type portEventTrafficDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_PortEventTrafficDuration_Type.__name__ = "Integer32"
_PortEventTrafficDuration_Object = MibTableColumn
portEventTrafficDuration = _PortEventTrafficDuration_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 62, 2, 1, 6),
    _PortEventTrafficDuration_Type()
)
portEventTrafficDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portEventTrafficDuration.setStatus("current")


class _PortEventModuleEnable_Type(Integer32):
    """Custom type portEventModuleEnable based on Integer32"""
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
              28,
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("enable-SNMPTrap-only", 1),
          ("enable-Email-only", 2),
          ("enable-SNMPTrap-Email", 3),
          ("enable-Syslog-only", 4),
          ("enable-SNMPTrap-Syslog", 5),
          ("enable-Email-Syslog", 6),
          ("enable-SNMPTrap-Email-Syslog", 7),
          ("enable-Relay1-only", 8),
          ("enable-SNMPTrap-Relay1", 9),
          ("enable-Email-Relay1", 10),
          ("enable-SNMPTrap-Email-Relay1", 11),
          ("enable-Syslog-Relay1", 12),
          ("enable-SNMPTrap-Syslog-Relay1", 13),
          ("enable-Email-Syslog-Relay1", 14),
          ("enable-SNMPTrap-Email-Syslog-Relay1", 15),
          ("enable-Relay2-only", 16),
          ("enable-SNMPTrap-Relay2", 17),
          ("enable-Email-Relay2", 18),
          ("enable-SNMPTrap-Email-Relay2", 19),
          ("enable-Syslog-Relay2", 20),
          ("enable-SNMPTrap-Syslog-Relay2", 21),
          ("enable-Email-Syslog-Relay2", 22),
          ("enable-SNMPTrap-Email-Syslog-Relay2", 23),
          ("enable-Relay1-Relay2", 24),
          ("enable-SNMPTrap-Relay1-Relay2", 25),
          ("enable-Syslog-Relay1-Relay2", 28),
          ("enable-Email-Syslog-Relay1-Relay2", 30),
          ("enable-All-SNMPTrap-Email-Syslog-Relay1-Relay2", 31))
    )


_PortEventModuleEnable_Type.__name__ = "Integer32"
_PortEventModuleEnable_Object = MibTableColumn
portEventModuleEnable = _PortEventModuleEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 62, 2, 1, 7),
    _PortEventModuleEnable_Type()
)
portEventModuleEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portEventModuleEnable.setStatus("current")


class _PortEventSeverity_Type(Integer32):
    """Custom type portEventSeverity based on Integer32"""
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
        *(("emergency", 0),
          ("alert", 1),
          ("critical", 2),
          ("error", 3),
          ("warning", 4),
          ("notice", 5),
          ("information", 6),
          ("debug", 7))
    )


_PortEventSeverity_Type.__name__ = "Integer32"
_PortEventSeverity_Object = MibTableColumn
portEventSeverity = _PortEventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 62, 2, 1, 8),
    _PortEventSeverity_Type()
)
portEventSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portEventSeverity.setStatus("current")
_ManagementInterface_ObjectIdentity = ObjectIdentity
managementInterface = _ManagementInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 63)
)


class _HttpEnable_Type(Integer32):
    """Custom type httpEnable based on Integer32"""
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


_HttpEnable_Type.__name__ = "Integer32"
_HttpEnable_Object = MibScalar
httpEnable = _HttpEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 63, 1),
    _HttpEnable_Type()
)
httpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpEnable.setStatus("current")


class _HttpPort_Type(Integer32):
    """Custom type httpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HttpPort_Type.__name__ = "Integer32"
_HttpPort_Object = MibScalar
httpPort = _HttpPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 63, 2),
    _HttpPort_Type()
)
httpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpPort.setStatus("current")


class _SslEnable_Type(Integer32):
    """Custom type sslEnable based on Integer32"""
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


_SslEnable_Type.__name__ = "Integer32"
_SslEnable_Object = MibScalar
sslEnable = _SslEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 63, 3),
    _SslEnable_Type()
)
sslEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslEnable.setStatus("current")


class _SslPort_Type(Integer32):
    """Custom type sslPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SslPort_Type.__name__ = "Integer32"
_SslPort_Object = MibScalar
sslPort = _SslPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 63, 4),
    _SslPort_Type()
)
sslPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslPort.setStatus("current")


class _TelnetEnable_Type(Integer32):
    """Custom type telnetEnable based on Integer32"""
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


_TelnetEnable_Type.__name__ = "Integer32"
_TelnetEnable_Object = MibScalar
telnetEnable = _TelnetEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 63, 5),
    _TelnetEnable_Type()
)
telnetEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetEnable.setStatus("current")


class _TelnetPort_Type(Integer32):
    """Custom type telnetPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TelnetPort_Type.__name__ = "Integer32"
_TelnetPort_Object = MibScalar
telnetPort = _TelnetPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 63, 6),
    _TelnetPort_Type()
)
telnetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetPort.setStatus("current")


class _SshEnable_Type(Integer32):
    """Custom type sshEnable based on Integer32"""
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


_SshEnable_Type.__name__ = "Integer32"
_SshEnable_Object = MibScalar
sshEnable = _SshEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 63, 7),
    _SshEnable_Type()
)
sshEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshEnable.setStatus("current")


class _SshPort_Type(Integer32):
    """Custom type sshPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SshPort_Type.__name__ = "Integer32"
_SshPort_Object = MibScalar
sshPort = _SshPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 63, 8),
    _SshPort_Type()
)
sshPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshPort.setStatus("current")


class _MgmtInterfaceAutoLogout_Type(Integer32):
    """Custom type mgmtInterfaceAutoLogout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_MgmtInterfaceAutoLogout_Type.__name__ = "Integer32"
_MgmtInterfaceAutoLogout_Object = MibScalar
mgmtInterfaceAutoLogout = _MgmtInterfaceAutoLogout_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 63, 9),
    _MgmtInterfaceAutoLogout_Type()
)
mgmtInterfaceAutoLogout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtInterfaceAutoLogout.setStatus("current")


class _SnmpdEnable_Type(Integer32):
    """Custom type snmpdEnable based on Integer32"""
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


_SnmpdEnable_Type.__name__ = "Integer32"
_SnmpdEnable_Object = MibScalar
snmpdEnable = _SnmpdEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 63, 10),
    _SnmpdEnable_Type()
)
snmpdEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpdEnable.setStatus("current")


class _SnmpdPort_Type(Integer32):
    """Custom type snmpdPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnmpdPort_Type.__name__ = "Integer32"
_SnmpdPort_Object = MibScalar
snmpdPort = _SnmpdPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 63, 11),
    _SnmpdPort_Type()
)
snmpdPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpdPort.setStatus("current")


class _MoxaUtilityServiceEnable_Type(Integer32):
    """Custom type moxaUtilityServiceEnable based on Integer32"""
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


_MoxaUtilityServiceEnable_Type.__name__ = "Integer32"
_MoxaUtilityServiceEnable_Object = MibScalar
moxaUtilityServiceEnable = _MoxaUtilityServiceEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 63, 12),
    _MoxaUtilityServiceEnable_Type()
)
moxaUtilityServiceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moxaUtilityServiceEnable.setStatus("current")


class _MoxaUtilityServicePort_Type(Integer32):
    """Custom type moxaUtilityServicePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MoxaUtilityServicePort_Type.__name__ = "Integer32"
_MoxaUtilityServicePort_Object = MibScalar
moxaUtilityServicePort = _MoxaUtilityServicePort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 63, 13),
    _MoxaUtilityServicePort_Type()
)
moxaUtilityServicePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moxaUtilityServicePort.setStatus("current")


class _HttpMaxLoginUsers_Type(Integer32):
    """Custom type httpMaxLoginUsers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HttpMaxLoginUsers_Type.__name__ = "Integer32"
_HttpMaxLoginUsers_Object = MibScalar
httpMaxLoginUsers = _HttpMaxLoginUsers_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 63, 14),
    _HttpMaxLoginUsers_Type()
)
httpMaxLoginUsers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpMaxLoginUsers.setStatus("current")


class _TelnetMaxLoginUsers_Type(Integer32):
    """Custom type telnetMaxLoginUsers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_TelnetMaxLoginUsers_Type.__name__ = "Integer32"
_TelnetMaxLoginUsers_Object = MibScalar
telnetMaxLoginUsers = _TelnetMaxLoginUsers_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 63, 15),
    _TelnetMaxLoginUsers_Type()
)
telnetMaxLoginUsers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetMaxLoginUsers.setStatus("current")


class _MoxaNewCmdEnable_Type(Integer32):
    """Custom type moxaNewCmdEnable based on Integer32"""
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


_MoxaNewCmdEnable_Type.__name__ = "Integer32"
_MoxaNewCmdEnable_Object = MibScalar
moxaNewCmdEnable = _MoxaNewCmdEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 63, 16),
    _MoxaNewCmdEnable_Type()
)
moxaNewCmdEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moxaNewCmdEnable.setStatus("current")
_SwitchLocator_ObjectIdentity = ObjectIdentity
switchLocator = _SwitchLocator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 64)
)


class _BlinkingLocatorLED_Type(Integer32):
    """Custom type blinkingLocatorLED based on Integer32"""
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


_BlinkingLocatorLED_Type.__name__ = "Integer32"
_BlinkingLocatorLED_Object = MibScalar
blinkingLocatorLED = _BlinkingLocatorLED_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 64, 1),
    _BlinkingLocatorLED_Type()
)
blinkingLocatorLED.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blinkingLocatorLED.setStatus("current")
_DisableLocatorLEDTime_Type = Integer32
_DisableLocatorLEDTime_Object = MibScalar
disableLocatorLEDTime = _DisableLocatorLEDTime_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 64, 2),
    _DisableLocatorLEDTime_Type()
)
disableLocatorLEDTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    disableLocatorLEDTime.setStatus("current")
_UiVersion_Type = Integer32
_UiVersion_Object = MibScalar
uiVersion = _UiVersion_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 65),
    _UiVersion_Type()
)
uiVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uiVersion.setStatus("current")


class _SupportIfXTable_Type(Integer32):
    """Custom type supportIfXTable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_SupportIfXTable_Type.__name__ = "Integer32"
_SupportIfXTable_Object = MibScalar
supportIfXTable = _SupportIfXTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 69),
    _SupportIfXTable_Type()
)
supportIfXTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supportIfXTable.setStatus("current")
_PasswordPolicy_ObjectIdentity = ObjectIdentity
passwordPolicy = _PasswordPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 70)
)


class _PwdMinLength_Type(Integer32):
    """Custom type pwdMinLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 16),
    )


_PwdMinLength_Type.__name__ = "Integer32"
_PwdMinLength_Object = MibScalar
pwdMinLength = _PwdMinLength_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 70, 1),
    _PwdMinLength_Type()
)
pwdMinLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwdMinLength.setStatus("current")


class _PwdComplexityCheckEnable_Type(Integer32):
    """Custom type pwdComplexityCheckEnable based on Integer32"""
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


_PwdComplexityCheckEnable_Type.__name__ = "Integer32"
_PwdComplexityCheckEnable_Object = MibScalar
pwdComplexityCheckEnable = _PwdComplexityCheckEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 70, 2),
    _PwdComplexityCheckEnable_Type()
)
pwdComplexityCheckEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwdComplexityCheckEnable.setStatus("current")


class _PwdComplexityCheckDigitEnable_Type(Integer32):
    """Custom type pwdComplexityCheckDigitEnable based on Integer32"""
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


_PwdComplexityCheckDigitEnable_Type.__name__ = "Integer32"
_PwdComplexityCheckDigitEnable_Object = MibScalar
pwdComplexityCheckDigitEnable = _PwdComplexityCheckDigitEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 70, 3),
    _PwdComplexityCheckDigitEnable_Type()
)
pwdComplexityCheckDigitEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwdComplexityCheckDigitEnable.setStatus("current")


class _PwdComplexityCheckAlphabetEnable_Type(Integer32):
    """Custom type pwdComplexityCheckAlphabetEnable based on Integer32"""
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


_PwdComplexityCheckAlphabetEnable_Type.__name__ = "Integer32"
_PwdComplexityCheckAlphabetEnable_Object = MibScalar
pwdComplexityCheckAlphabetEnable = _PwdComplexityCheckAlphabetEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 70, 4),
    _PwdComplexityCheckAlphabetEnable_Type()
)
pwdComplexityCheckAlphabetEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwdComplexityCheckAlphabetEnable.setStatus("current")


class _PwdComplexityCheckSpecialCharEnable_Type(Integer32):
    """Custom type pwdComplexityCheckSpecialCharEnable based on Integer32"""
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


_PwdComplexityCheckSpecialCharEnable_Type.__name__ = "Integer32"
_PwdComplexityCheckSpecialCharEnable_Object = MibScalar
pwdComplexityCheckSpecialCharEnable = _PwdComplexityCheckSpecialCharEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 70, 5),
    _PwdComplexityCheckSpecialCharEnable_Type()
)
pwdComplexityCheckSpecialCharEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwdComplexityCheckSpecialCharEnable.setStatus("current")
_LoginLockout_ObjectIdentity = ObjectIdentity
loginLockout = _LoginLockout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 71)
)


class _LoginFailureLockoutEnable_Type(Integer32):
    """Custom type loginFailureLockoutEnable based on Integer32"""
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


_LoginFailureLockoutEnable_Type.__name__ = "Integer32"
_LoginFailureLockoutEnable_Object = MibScalar
loginFailureLockoutEnable = _LoginFailureLockoutEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 71, 1),
    _LoginFailureLockoutEnable_Type()
)
loginFailureLockoutEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loginFailureLockoutEnable.setStatus("current")


class _LoginFailureLockoutRetrys_Type(Integer32):
    """Custom type loginFailureLockoutRetrys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_LoginFailureLockoutRetrys_Type.__name__ = "Integer32"
_LoginFailureLockoutRetrys_Object = MibScalar
loginFailureLockoutRetrys = _LoginFailureLockoutRetrys_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 71, 2),
    _LoginFailureLockoutRetrys_Type()
)
loginFailureLockoutRetrys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loginFailureLockoutRetrys.setStatus("current")


class _LoginFailureLockoutTime_Type(Integer32):
    """Custom type loginFailureLockoutTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_LoginFailureLockoutTime_Type.__name__ = "Integer32"
_LoginFailureLockoutTime_Object = MibScalar
loginFailureLockoutTime = _LoginFailureLockoutTime_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 71, 3),
    _LoginFailureLockoutTime_Type()
)
loginFailureLockoutTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loginFailureLockoutTime.setStatus("current")
_SystemNotifyMessage_ObjectIdentity = ObjectIdentity
systemNotifyMessage = _SystemNotifyMessage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 72)
)
_HttpLoginMessage_Type = DisplayString
_HttpLoginMessage_Object = MibScalar
httpLoginMessage = _HttpLoginMessage_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 72, 1),
    _HttpLoginMessage_Type()
)
httpLoginMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpLoginMessage.setStatus("current")
_HttpLoginFailureMessage_Type = DisplayString
_HttpLoginFailureMessage_Object = MibScalar
httpLoginFailureMessage = _HttpLoginFailureMessage_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 72, 2),
    _HttpLoginFailureMessage_Type()
)
httpLoginFailureMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpLoginFailureMessage.setStatus("current")
_SyslogManagement_ObjectIdentity = ObjectIdentity
syslogManagement = _SyslogManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 73)
)


class _LoggingCapacityThreshold_Type(Integer32):
    """Custom type loggingCapacityThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LoggingCapacityThreshold_Type.__name__ = "Integer32"
_LoggingCapacityThreshold_Object = MibScalar
loggingCapacityThreshold = _LoggingCapacityThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 73, 1),
    _LoggingCapacityThreshold_Type()
)
loggingCapacityThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loggingCapacityThreshold.setStatus("current")


class _LoggingCapacityTrapWarningEnable_Type(Integer32):
    """Custom type loggingCapacityTrapWarningEnable based on Integer32"""
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


_LoggingCapacityTrapWarningEnable_Type.__name__ = "Integer32"
_LoggingCapacityTrapWarningEnable_Object = MibScalar
loggingCapacityTrapWarningEnable = _LoggingCapacityTrapWarningEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 73, 2),
    _LoggingCapacityTrapWarningEnable_Type()
)
loggingCapacityTrapWarningEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loggingCapacityTrapWarningEnable.setStatus("current")


class _LoggingCapacityEmailWarningEnable_Type(Integer32):
    """Custom type loggingCapacityEmailWarningEnable based on Integer32"""
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


_LoggingCapacityEmailWarningEnable_Type.__name__ = "Integer32"
_LoggingCapacityEmailWarningEnable_Object = MibScalar
loggingCapacityEmailWarningEnable = _LoggingCapacityEmailWarningEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 73, 3),
    _LoggingCapacityEmailWarningEnable_Type()
)
loggingCapacityEmailWarningEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loggingCapacityEmailWarningEnable.setStatus("current")


class _LoggingOversizeAction_Type(Integer32):
    """Custom type loggingOversizeAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("overwrite", 0),
          ("stoprecord", 1))
    )


_LoggingOversizeAction_Type.__name__ = "Integer32"
_LoggingOversizeAction_Object = MibScalar
loggingOversizeAction = _LoggingOversizeAction_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 73, 4),
    _LoggingOversizeAction_Type()
)
loggingOversizeAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loggingOversizeAction.setStatus("current")
_CertificateManagement_ObjectIdentity = ObjectIdentity
certificateManagement = _CertificateManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 74)
)


class _SslCertGen_Type(Integer32):
    """Custom type sslCertGen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("generate", 1))
    )


_SslCertGen_Type.__name__ = "Integer32"
_SslCertGen_Object = MibScalar
sslCertGen = _SslCertGen_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 74, 1),
    _SslCertGen_Type()
)
sslCertGen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslCertGen.setStatus("current")


class _SshKeyGen_Type(Integer32):
    """Custom type sshKeyGen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("generate", 1))
    )


_SshKeyGen_Type.__name__ = "Integer32"
_SshKeyGen_Object = MibScalar
sshKeyGen = _SshKeyGen_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 74, 2),
    _SshKeyGen_Type()
)
sshKeyGen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshKeyGen.setStatus("current")


class _IvlSwitch_Type(Integer32):
    """Custom type ivlSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("svl", 0),
          ("ivl", 1))
    )


_IvlSwitch_Type.__name__ = "Integer32"
_IvlSwitch_Object = MibScalar
ivlSwitch = _IvlSwitch_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 76),
    _IvlSwitch_Type()
)
ivlSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ivlSwitch.setStatus("current")


class _SupportMacSticky_Type(Integer32):
    """Custom type supportMacSticky based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-support", 0),
          ("support", 1))
    )


_SupportMacSticky_Type.__name__ = "Integer32"
_SupportMacSticky_Object = MibScalar
supportMacSticky = _SupportMacSticky_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 77),
    _SupportMacSticky_Type()
)
supportMacSticky.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supportMacSticky.setStatus("current")
_SerialNumber_Type = DisplayString
_SerialNumber_Object = MibScalar
serialNumber = _SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 78),
    _SerialNumber_Type()
)
serialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNumber.setStatus("current")


class _ConfigEncryptEnable_Type(Integer32):
    """Custom type configEncryptEnable based on Integer32"""
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


_ConfigEncryptEnable_Type.__name__ = "Integer32"
_ConfigEncryptEnable_Object = MibScalar
configEncryptEnable = _ConfigEncryptEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 1, 79),
    _ConfigEncryptEnable_Type()
)
configEncryptEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configEncryptEnable.setStatus("current")
_SwTraps_ObjectIdentity = ObjectIdentity
swTraps = _SwTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 2)
)


class _VarconfigChangeTrap_Type(Integer32):
    """Custom type varconfigChangeTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("configChanged", 2))
    )


_VarconfigChangeTrap_Type.__name__ = "Integer32"
_VarconfigChangeTrap_Object = MibScalar
varconfigChangeTrap = _VarconfigChangeTrap_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 2, 1),
    _VarconfigChangeTrap_Type()
)
varconfigChangeTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    varconfigChangeTrap.setStatus("current")


class _Varpower1Trap_Type(Integer32):
    """Custom type varpower1Trap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("on2off", 2),
          ("off2on", 3))
    )


_Varpower1Trap_Type.__name__ = "Integer32"
_Varpower1Trap_Object = MibScalar
varpower1Trap = _Varpower1Trap_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 2, 2),
    _Varpower1Trap_Type()
)
varpower1Trap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    varpower1Trap.setStatus("current")


class _Varpower2Trap_Type(Integer32):
    """Custom type varpower2Trap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("on2off", 2),
          ("off2on", 3))
    )


_Varpower2Trap_Type.__name__ = "Integer32"
_Varpower2Trap_Object = MibScalar
varpower2Trap = _Varpower2Trap_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 2, 3),
    _Varpower2Trap_Type()
)
varpower2Trap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    varpower2Trap.setStatus("current")
_VartrafficOverloadTrap_Type = Integer32
_VartrafficOverloadTrap_Object = MibScalar
vartrafficOverloadTrap = _VartrafficOverloadTrap_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 2, 4),
    _VartrafficOverloadTrap_Type()
)
vartrafficOverloadTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vartrafficOverloadTrap.setStatus("current")


class _VarredundancyTopologyChangedTrap_Type(Integer32):
    """Custom type varredundancyTopologyChangedTrap based on Integer32"""
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
        *(("none", 1),
          ("topologyChanged", 2),
          ("topologyChangedTurboChainHead", 3),
          ("topologyChangedTurboChainTail", 4))
    )


_VarredundancyTopologyChangedTrap_Type.__name__ = "Integer32"
_VarredundancyTopologyChangedTrap_Object = MibScalar
varredundancyTopologyChangedTrap = _VarredundancyTopologyChangedTrap_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 2, 5),
    _VarredundancyTopologyChangedTrap_Type()
)
varredundancyTopologyChangedTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    varredundancyTopologyChangedTrap.setStatus("current")


class _VarturboRingCouplingPortChangedTrap_Type(Integer32):
    """Custom type varturboRingCouplingPortChangedTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("couplingPortChanged", 2))
    )


_VarturboRingCouplingPortChangedTrap_Type.__name__ = "Integer32"
_VarturboRingCouplingPortChangedTrap_Object = MibScalar
varturboRingCouplingPortChangedTrap = _VarturboRingCouplingPortChangedTrap_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 2, 6),
    _VarturboRingCouplingPortChangedTrap_Type()
)
varturboRingCouplingPortChangedTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    varturboRingCouplingPortChangedTrap.setStatus("current")


class _VarturboRingMasterChangedTrap_Type(Integer32):
    """Custom type varturboRingMasterChangedTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("ringMasterChanged", 2))
    )


_VarturboRingMasterChangedTrap_Type.__name__ = "Integer32"
_VarturboRingMasterChangedTrap_Object = MibScalar
varturboRingMasterChangedTrap = _VarturboRingMasterChangedTrap_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 2, 7),
    _VarturboRingMasterChangedTrap_Type()
)
varturboRingMasterChangedTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    varturboRingMasterChangedTrap.setStatus("current")


class _VarPoEWarningTrap_Type(Integer32):
    """Custom type varPoEWarningTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
        *(("pdOverCurrent", 1),
          ("pdCheckFail", 2),
          ("pdPowerOn", 3),
          ("pdPowerOff", 4),
          ("exceedSystemThreshold", 5),
          ("pseFetBad", 6),
          ("pseOverTemperature", 7),
          ("pseVeeUvlo", 8),
          ("exceedSystemPowerBudget", 9))
    )


_VarPoEWarningTrap_Type.__name__ = "Integer32"
_VarPoEWarningTrap_Object = MibScalar
varPoEWarningTrap = _VarPoEWarningTrap_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 2, 16),
    _VarPoEWarningTrap_Type()
)
varPoEWarningTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    varPoEWarningTrap.setStatus("current")
_VarPortLoopDetectedTrap_Type = Integer32
_VarPortLoopDetectedTrap_Object = MibScalar
varPortLoopDetectedTrap = _VarPortLoopDetectedTrap_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 2, 17),
    _VarPortLoopDetectedTrap_Type()
)
varPortLoopDetectedTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    varPortLoopDetectedTrap.setStatus("current")


class _VarRateLimitedOnTrap_Type(Integer32):
    """Custom type varRateLimitedOnTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("rateLimitON", 2),
          ("rateLimitOFF", 3))
    )


_VarRateLimitedOnTrap_Type.__name__ = "Integer32"
_VarRateLimitedOnTrap_Object = MibScalar
varRateLimitedOnTrap = _VarRateLimitedOnTrap_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 2, 18),
    _VarRateLimitedOnTrap_Type()
)
varRateLimitedOnTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    varRateLimitedOnTrap.setStatus("current")
_VarLLDPChgTrap_Type = Integer32
_VarLLDPChgTrap_Object = MibScalar
varLLDPChgTrap = _VarLLDPChgTrap_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 2, 19),
    _VarLLDPChgTrap_Type()
)
varLLDPChgTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    varLLDPChgTrap.setStatus("current")


class _VarABC02WarningTrap_Type(Integer32):
    """Custom type varABC02WarningTrap based on Integer32"""
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
        *(("noEnoughSpace", 1),
          ("nnauthorizedMediaIsDetected", 2),
          ("exportConfigurationFail", 3),
          ("exportLogFail", 4),
          ("autoImportConfigurationFail", 5))
    )


_VarABC02WarningTrap_Type.__name__ = "Integer32"
_VarABC02WarningTrap_Object = MibScalar
varABC02WarningTrap = _VarABC02WarningTrap_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 2, 20),
    _VarABC02WarningTrap_Type()
)
varABC02WarningTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    varABC02WarningTrap.setStatus("current")


class _VarturboRingMasterMismatchTrap_Type(Integer32):
    """Custom type varturboRingMasterMismatchTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("ringMasterMismatch", 2))
    )


_VarturboRingMasterMismatchTrap_Type.__name__ = "Integer32"
_VarturboRingMasterMismatchTrap_Object = MibScalar
varturboRingMasterMismatchTrap = _VarturboRingMasterMismatchTrap_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 2, 22),
    _VarturboRingMasterMismatchTrap_Type()
)
varturboRingMasterMismatchTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    varturboRingMasterMismatchTrap.setStatus("current")
_VarUserAuthSuccessTrap_Type = OctetString
_VarUserAuthSuccessTrap_Object = MibScalar
varUserAuthSuccessTrap = _VarUserAuthSuccessTrap_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 2, 24),
    _VarUserAuthSuccessTrap_Type()
)
varUserAuthSuccessTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    varUserAuthSuccessTrap.setStatus("current")
_VarUserAuthFailTrap_Type = OctetString
_VarUserAuthFailTrap_Object = MibScalar
varUserAuthFailTrap = _VarUserAuthFailTrap_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 2, 25),
    _VarUserAuthFailTrap_Type()
)
varUserAuthFailTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    varUserAuthFailTrap.setStatus("current")


class _VarMacStickyPortViolationPortDisableTrap_Type(Integer32):
    """Custom type varMacStickyPortViolationPortDisableTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("violationPortDisable", 2))
    )


_VarMacStickyPortViolationPortDisableTrap_Type.__name__ = "Integer32"
_VarMacStickyPortViolationPortDisableTrap_Object = MibScalar
varMacStickyPortViolationPortDisableTrap = _VarMacStickyPortViolationPortDisableTrap_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 2, 26),
    _VarMacStickyPortViolationPortDisableTrap_Type()
)
varMacStickyPortViolationPortDisableTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    varMacStickyPortViolationPortDisableTrap.setStatus("current")
_VarFiberWarningTrap_Type = Integer32
_VarFiberWarningTrap_Object = MibScalar
varFiberWarningTrap = _VarFiberWarningTrap_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 2, 28),
    _VarFiberWarningTrap_Type()
)
varFiberWarningTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    varFiberWarningTrap.setStatus("current")
_VarLoggingCapacityTrap_Type = Integer32
_VarLoggingCapacityTrap_Object = MibScalar
varLoggingCapacityTrap = _VarLoggingCapacityTrap_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 2, 29),
    _VarLoggingCapacityTrap_Type()
)
varLoggingCapacityTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    varLoggingCapacityTrap.setStatus("current")
_VarUserInfoChgTrap_Type = OctetString
_VarUserInfoChgTrap_Object = MibScalar
varUserInfoChgTrap = _VarUserInfoChgTrap_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 2, 31),
    _VarUserInfoChgTrap_Type()
)
varUserInfoChgTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    varUserInfoChgTrap.setStatus("current")
_VarConfigImportTrap_Type = Integer32
_VarConfigImportTrap_Object = MibScalar
varConfigImportTrap = _VarConfigImportTrap_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 2, 32),
    _VarConfigImportTrap_Type()
)
varConfigImportTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    varConfigImportTrap.setStatus("current")


class _VarRemoteAuthSuccessTrap_Type(Integer32):
    """Custom type varRemoteAuthSuccessTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tacacs", 1),
          ("radius", 2))
    )


_VarRemoteAuthSuccessTrap_Type.__name__ = "Integer32"
_VarRemoteAuthSuccessTrap_Object = MibScalar
varRemoteAuthSuccessTrap = _VarRemoteAuthSuccessTrap_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 2, 38),
    _VarRemoteAuthSuccessTrap_Type()
)
varRemoteAuthSuccessTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    varRemoteAuthSuccessTrap.setStatus("current")


class _VarRemoteAuthFailTrap_Type(Integer32):
    """Custom type varRemoteAuthFailTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tacacs", 1),
          ("radius", 2))
    )


_VarRemoteAuthFailTrap_Type.__name__ = "Integer32"
_VarRemoteAuthFailTrap_Object = MibScalar
varRemoteAuthFailTrap = _VarRemoteAuthFailTrap_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 2, 39),
    _VarRemoteAuthFailTrap_Type()
)
varRemoteAuthFailTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    varRemoteAuthFailTrap.setStatus("current")


class _VarEPSChangeToOn_Type(Integer32):
    """Custom type varEPSChangeToOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("externalPower1", 1),
          ("externalPower2", 2))
    )


_VarEPSChangeToOn_Type.__name__ = "Integer32"
_VarEPSChangeToOn_Object = MibScalar
varEPSChangeToOn = _VarEPSChangeToOn_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 2, 44),
    _VarEPSChangeToOn_Type()
)
varEPSChangeToOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    varEPSChangeToOn.setStatus("current")


class _VarEPSChangeToOff_Type(Integer32):
    """Custom type varEPSChangeToOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("externalPower1", 1),
          ("externalPower2", 2))
    )


_VarEPSChangeToOff_Type.__name__ = "Integer32"
_VarEPSChangeToOff_Object = MibScalar
varEPSChangeToOff = _VarEPSChangeToOff_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 2, 45),
    _VarEPSChangeToOff_Type()
)
varEPSChangeToOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    varEPSChangeToOff.setStatus("current")

# Managed Objects groups


# Notification objects

configChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 0, 1)
)
configChangeTrap.setObjects(
    ("MOXA-EDSP506E-MIB", "varconfigChangeTrap")
)
if mibBuilder.loadTexts:
    configChangeTrap.setStatus(
        "current"
    )

power1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 0, 2)
)
power1Trap.setObjects(
    ("MOXA-EDSP506E-MIB", "varpower1Trap")
)
if mibBuilder.loadTexts:
    power1Trap.setStatus(
        "current"
    )

power2Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 0, 3)
)
power2Trap.setObjects(
    ("MOXA-EDSP506E-MIB", "varpower2Trap")
)
if mibBuilder.loadTexts:
    power2Trap.setStatus(
        "current"
    )

trafficOverloadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 0, 4)
)
trafficOverloadTrap.setObjects(
    ("MOXA-EDSP506E-MIB", "vartrafficOverloadTrap")
)
if mibBuilder.loadTexts:
    trafficOverloadTrap.setStatus(
        "current"
    )

redundancyTopologyChangedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 0, 5)
)
redundancyTopologyChangedTrap.setObjects(
    ("MOXA-EDSP506E-MIB", "varredundancyTopologyChangedTrap")
)
if mibBuilder.loadTexts:
    redundancyTopologyChangedTrap.setStatus(
        "current"
    )

turboRingCouplingPortChangedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 0, 6)
)
turboRingCouplingPortChangedTrap.setObjects(
    ("MOXA-EDSP506E-MIB", "varturboRingCouplingPortChangedTrap")
)
if mibBuilder.loadTexts:
    turboRingCouplingPortChangedTrap.setStatus(
        "current"
    )

turboRingMasterChangedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 0, 7)
)
turboRingMasterChangedTrap.setObjects(
    ("MOXA-EDSP506E-MIB", "varturboRingMasterChangedTrap")
)
if mibBuilder.loadTexts:
    turboRingMasterChangedTrap.setStatus(
        "current"
    )

poeWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 0, 16)
)
poeWarningTrap.setObjects(
    ("MOXA-EDSP506E-MIB", "varPoEWarningTrap")
)
if mibBuilder.loadTexts:
    poeWarningTrap.setStatus(
        "current"
    )

portLoopDetectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 0, 17)
)
portLoopDetectedTrap.setObjects(
    ("MOXA-EDSP506E-MIB", "varPortLoopDetectedTrap")
)
if mibBuilder.loadTexts:
    portLoopDetectedTrap.setStatus(
        "current"
    )

rateLimitedOnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 0, 18)
)
rateLimitedOnTrap.setObjects(
    ("MOXA-EDSP506E-MIB", "varRateLimitedOnTrap")
)
if mibBuilder.loadTexts:
    rateLimitedOnTrap.setStatus(
        "current"
    )

lldpChgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 0, 19)
)
lldpChgTrap.setObjects(
    ("MOXA-EDSP506E-MIB", "varLLDPChgTrap")
)
if mibBuilder.loadTexts:
    lldpChgTrap.setStatus(
        "current"
    )

abc02WarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 0, 20)
)
abc02WarningTrap.setObjects(
    ("MOXA-EDSP506E-MIB", "varABC02WarningTrap")
)
if mibBuilder.loadTexts:
    abc02WarningTrap.setStatus(
        "current"
    )

turboRingMasterMismatchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 0, 22)
)
turboRingMasterMismatchTrap.setObjects(
    ("MOXA-EDSP506E-MIB", "varturboRingMasterChangedTrap")
)
if mibBuilder.loadTexts:
    turboRingMasterMismatchTrap.setStatus(
        "current"
    )

userAuthSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 0, 24)
)
userAuthSuccessTrap.setObjects(
    ("MOXA-EDSP506E-MIB", "varUserAuthSuccessTrap")
)
if mibBuilder.loadTexts:
    userAuthSuccessTrap.setStatus(
        "current"
    )

userAuthFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 0, 25)
)
userAuthFailTrap.setObjects(
    ("MOXA-EDSP506E-MIB", "varUserAuthFailTrap")
)
if mibBuilder.loadTexts:
    userAuthFailTrap.setStatus(
        "current"
    )

macStickyPortViolationPortDisableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 0, 26)
)
macStickyPortViolationPortDisableTrap.setObjects(
    ("MOXA-EDSP506E-MIB", "varMacStickyPortViolationPortDisableTrap")
)
if mibBuilder.loadTexts:
    macStickyPortViolationPortDisableTrap.setStatus(
        "current"
    )

fiberWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 0, 28)
)
fiberWarningTrap.setObjects(
    ("MOXA-EDSP506E-MIB", "varFiberWarningTrap")
)
if mibBuilder.loadTexts:
    fiberWarningTrap.setStatus(
        "current"
    )

loggingCapacityTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 0, 29)
)
loggingCapacityTrap.setObjects(
    ("MOXA-EDSP506E-MIB", "varLoggingCapacityTrap")
)
if mibBuilder.loadTexts:
    loggingCapacityTrap.setStatus(
        "current"
    )

userInfoChgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 0, 31)
)
userInfoChgTrap.setObjects(
    ("MOXA-EDSP506E-MIB", "varUserInfoChgTrap")
)
if mibBuilder.loadTexts:
    userInfoChgTrap.setStatus(
        "current"
    )

configImportTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 0, 32)
)
configImportTrap.setObjects(
    ("MOXA-EDSP506E-MIB", "varConfigImportTrap")
)
if mibBuilder.loadTexts:
    configImportTrap.setStatus(
        "current"
    )

remoteAuthSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 0, 38)
)
remoteAuthSuccessTrap.setObjects(
    ("MOXA-EDSP506E-MIB", "varRemoteAuthSuccessTrap")
)
if mibBuilder.loadTexts:
    remoteAuthSuccessTrap.setStatus(
        "current"
    )

remoteAuthFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 0, 39)
)
remoteAuthFailTrap.setObjects(
    ("MOXA-EDSP506E-MIB", "varRemoteAuthFailTrap")
)
if mibBuilder.loadTexts:
    remoteAuthFailTrap.setStatus(
        "current"
    )

ePSChangeToOnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 0, 44)
)
ePSChangeToOnTrap.setObjects(
    ("MOXA-EDSP506E-MIB", "varEPSChangeToOn")
)
if mibBuilder.loadTexts:
    ePSChangeToOnTrap.setStatus(
        "current"
    )

ePSChangeToOffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 7, 162, 0, 45)
)
ePSChangeToOffTrap.setObjects(
    ("MOXA-EDSP506E-MIB", "varEPSChangeToOff")
)
if mibBuilder.loadTexts:
    ePSChangeToOffTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MOXA-EDSP506E-MIB",
    **{"PortList": PortList,
       "moxa": moxa,
       "industrialEthernet": industrialEthernet,
       "edsp506e": edsp506e,
       "mibNotificationsPrefix": mibNotificationsPrefix,
       "configChangeTrap": configChangeTrap,
       "power1Trap": power1Trap,
       "power2Trap": power2Trap,
       "trafficOverloadTrap": trafficOverloadTrap,
       "redundancyTopologyChangedTrap": redundancyTopologyChangedTrap,
       "turboRingCouplingPortChangedTrap": turboRingCouplingPortChangedTrap,
       "turboRingMasterChangedTrap": turboRingMasterChangedTrap,
       "poeWarningTrap": poeWarningTrap,
       "portLoopDetectedTrap": portLoopDetectedTrap,
       "rateLimitedOnTrap": rateLimitedOnTrap,
       "lldpChgTrap": lldpChgTrap,
       "abc02WarningTrap": abc02WarningTrap,
       "turboRingMasterMismatchTrap": turboRingMasterMismatchTrap,
       "userAuthSuccessTrap": userAuthSuccessTrap,
       "userAuthFailTrap": userAuthFailTrap,
       "macStickyPortViolationPortDisableTrap": macStickyPortViolationPortDisableTrap,
       "fiberWarningTrap": fiberWarningTrap,
       "loggingCapacityTrap": loggingCapacityTrap,
       "userInfoChgTrap": userInfoChgTrap,
       "configImportTrap": configImportTrap,
       "remoteAuthSuccessTrap": remoteAuthSuccessTrap,
       "remoteAuthFailTrap": remoteAuthFailTrap,
       "ePSChangeToOnTrap": ePSChangeToOnTrap,
       "ePSChangeToOffTrap": ePSChangeToOffTrap,
       "swMgmt": swMgmt,
       "numberOfPorts": numberOfPorts,
       "switchModel": switchModel,
       "firmwareVersion": firmwareVersion,
       "enableWebConfig": enableWebConfig,
       "enableTelnetConsole": enableTelnetConsole,
       "lineSwapRecovery": lineSwapRecovery,
       "networkSetting": networkSetting,
       "switchIpAddr": switchIpAddr,
       "switchIpMask": switchIpMask,
       "defaultGateway": defaultGateway,
       "enableAutoIpConfig": enableAutoIpConfig,
       "dnsServer1IpAddr": dnsServer1IpAddr,
       "snmpTrapCommunity": snmpTrapCommunity,
       "trapServerAddr": trapServerAddr,
       "dnsServer2IpAddr": dnsServer2IpAddr,
       "snmpReadCommunity": snmpReadCommunity,
       "snmpTrap2Community": snmpTrap2Community,
       "trap2ServerAddr": trap2ServerAddr,
       "snmpInformEnable": snmpInformEnable,
       "snmpInformRetries": snmpInformRetries,
       "snmpInformTimeout": snmpInformTimeout,
       "dhcpRetryPeriods": dhcpRetryPeriods,
       "dhcpRetryTimes": dhcpRetryTimes,
       "trapVersion": trapVersion,
       "snmpVersion": snmpVersion,
       "snmpAdminSecurityLevel": snmpAdminSecurityLevel,
       "snmpUserSecurityLevel": snmpUserSecurityLevel,
       "portSetting": portSetting,
       "portTable": portTable,
       "portEntry": portEntry,
       "portIndex": portIndex,
       "portDesc": portDesc,
       "portEnable": portEnable,
       "portSpeed": portSpeed,
       "portMDI": portMDI,
       "portFDXFlowCtrl": portFDXFlowCtrl,
       "portName": portName,
       "portSubdesc": portSubdesc,
       "monitor": monitor,
       "power1InputStatus": power1InputStatus,
       "power2InputStatus": power2InputStatus,
       "monitorPortTable": monitorPortTable,
       "monitorPortEntry": monitorPortEntry,
       "monitorLinkStatus": monitorLinkStatus,
       "monitorSpeed": monitorSpeed,
       "monitorAutoMDI": monitorAutoMDI,
       "monitorTraffic": monitorTraffic,
       "monitorFDXFlowCtrl": monitorFDXFlowCtrl,
       "monitorTxTraffic": monitorTxTraffic,
       "monitorRxTraffic": monitorRxTraffic,
       "monitorDiTable": monitorDiTable,
       "monitorDiEntry": monitorDiEntry,
       "diIndex": diIndex,
       "diInputStatus": diInputStatus,
       "powerConsumption": powerConsumption,
       "monitorFiberCheckTable": monitorFiberCheckTable,
       "monitorFiberCheckEntry": monitorFiberCheckEntry,
       "fiberPort": fiberPort,
       "fiberModelName": fiberModelName,
       "fiberWaveLength": fiberWaveLength,
       "fiberVoltage": fiberVoltage,
       "fiberTemperature": fiberTemperature,
       "fiberTempWarn": fiberTempWarn,
       "fiberTxPower": fiberTxPower,
       "fiberTxPowerWarn": fiberTxPowerWarn,
       "fiberRxPower": fiberRxPower,
       "fiberRxPowerWarn": fiberRxPowerWarn,
       "fiberSN": fiberSN,
       "monitorPoEEPSTable": monitorPoEEPSTable,
       "monitorPoEEPSEntry": monitorPoEEPSEntry,
       "epsIndex": epsIndex,
       "epsState": epsState,
       "emailWarning": emailWarning,
       "emailService": emailService,
       "emailWarningSMTPServer": emailWarningSMTPServer,
       "emailWarningFirstRecipientEmailAddr": emailWarningFirstRecipientEmailAddr,
       "emailWarningSecondRecipientEmailAddr": emailWarningSecondRecipientEmailAddr,
       "emailWarningThirdRecipientEmailAddr": emailWarningThirdRecipientEmailAddr,
       "emailWarningFourthRecipientEmailAddr": emailWarningFourthRecipientEmailAddr,
       "emailWarningSMTPPort": emailWarningSMTPPort,
       "emailWarningSMTPUser": emailWarningSMTPUser,
       "emailWarningSMTPPassword": emailWarningSMTPPassword,
       "emailWarningSMTPTLS": emailWarningSMTPTLS,
       "emailWarningSMTPAuthMethod": emailWarningSMTPAuthMethod,
       "emailWarningSenderEmailAddr": emailWarningSenderEmailAddr,
       "setDeviceIp": setDeviceIp,
       "setDevIpTable": setDevIpTable,
       "setDevIpEntry": setDevIpEntry,
       "setDevIpIndex": setDevIpIndex,
       "setDevIpCurrentIpofDevice": setDevIpCurrentIpofDevice,
       "setDevIpPresentBy": setDevIpPresentBy,
       "setDevIpDedicatedIp": setDevIpDedicatedIp,
       "mirroring": mirroring,
       "targetPort": targetPort,
       "mirroringPort": mirroringPort,
       "monitorDirection": monitorDirection,
       "portTrunking": portTrunking,
       "trunkSettingTable": trunkSettingTable,
       "trunkSettingEntry": trunkSettingEntry,
       "trunkSettingIndex": trunkSettingIndex,
       "trunkType": trunkType,
       "trunkMemberPorts": trunkMemberPorts,
       "trunkTable": trunkTable,
       "trunkEntry": trunkEntry,
       "trunkIndex": trunkIndex,
       "trunkPort": trunkPort,
       "trunkStatus": trunkStatus,
       "commRedundancy": commRedundancy,
       "protocolOfRedundancySetup": protocolOfRedundancySetup,
       "turboRing": turboRing,
       "turboRingMaster": turboRingMaster,
       "turboRingMasterSetup": turboRingMasterSetup,
       "turboRingPortTable": turboRingPortTable,
       "turboRingPortEntry": turboRingPortEntry,
       "turboRingPortIndex": turboRingPortIndex,
       "turboRingPortStatus": turboRingPortStatus,
       "turboRingPortDesignatedBridge": turboRingPortDesignatedBridge,
       "turboRingPortDesignatedPort": turboRingPortDesignatedPort,
       "turboRingDesignatedMaster": turboRingDesignatedMaster,
       "turboRingRdntPort1": turboRingRdntPort1,
       "turboRingRdntPort2": turboRingRdntPort2,
       "turboRingEnableCoupling": turboRingEnableCoupling,
       "turboRingCouplingPort": turboRingCouplingPort,
       "turboRingCouplingPortStatus": turboRingCouplingPortStatus,
       "turboRingControlPort": turboRingControlPort,
       "turboRingControlPortStatus": turboRingControlPortStatus,
       "turboRingBrokenStatus": turboRingBrokenStatus,
       "spanningTree": spanningTree,
       "spanningTreeRoot": spanningTreeRoot,
       "spanningTreeBridgePriority": spanningTreeBridgePriority,
       "spanningTreeHelloTime": spanningTreeHelloTime,
       "spanningTreeMaxAge": spanningTreeMaxAge,
       "spanningTreeForwardingDelay": spanningTreeForwardingDelay,
       "spanningTreeTable": spanningTreeTable,
       "spanningTreeEntry": spanningTreeEntry,
       "spanningTreeIndex": spanningTreeIndex,
       "enableSpanningTree": enableSpanningTree,
       "spanningTreePortPriority": spanningTreePortPriority,
       "spanningTreePortCost": spanningTreePortCost,
       "spanningTreePortStatus": spanningTreePortStatus,
       "spanningTreePortEdge": spanningTreePortEdge,
       "activeProtocolOfRedundancy": activeProtocolOfRedundancy,
       "turboRingV2": turboRingV2,
       "turboRingV2Ring1": turboRingV2Ring1,
       "ringIndexRing1": ringIndexRing1,
       "ringEnableRing1": ringEnableRing1,
       "masterSetupRing1": masterSetupRing1,
       "masterStatusRing1": masterStatusRing1,
       "designatedMasterRing1": designatedMasterRing1,
       "rdnt1stPortRing1": rdnt1stPortRing1,
       "rdnt1stPortStatusRing1": rdnt1stPortStatusRing1,
       "rdnt2ndPortRing1": rdnt2ndPortRing1,
       "rdnt2ndPortStatusRing1": rdnt2ndPortStatusRing1,
       "brokenStatusRing1": brokenStatusRing1,
       "turboRingV2Ring2": turboRingV2Ring2,
       "ringIndexRing2": ringIndexRing2,
       "ringEnableRing2": ringEnableRing2,
       "masterSetupRing2": masterSetupRing2,
       "masterStatusRing2": masterStatusRing2,
       "designatedMasterRing2": designatedMasterRing2,
       "rdnt1stPortRing2": rdnt1stPortRing2,
       "rdnt1stPortStatusRing2": rdnt1stPortStatusRing2,
       "rdnt2ndPortRing2": rdnt2ndPortRing2,
       "rdnt2ndPortStatusRing2": rdnt2ndPortStatusRing2,
       "brokenStatusRing2": brokenStatusRing2,
       "turboRingV2Coupling": turboRingV2Coupling,
       "couplingEnable": couplingEnable,
       "couplingMode": couplingMode,
       "coupling1stPort": coupling1stPort,
       "coupling1stPortStatus": coupling1stPortStatus,
       "coupling2ndPort": coupling2ndPort,
       "coupling2ndPortStatus": coupling2ndPortStatus,
       "turboChain": turboChain,
       "turboChainRole": turboChainRole,
       "turboChainPort1": turboChainPort1,
       "turboChainPort2": turboChainPort2,
       "turboChainPort1Status": turboChainPort1Status,
       "turboChainPort2Status": turboChainPort2Status,
       "turboChainPort1PartnerBridge": turboChainPort1PartnerBridge,
       "turboChainPort2PartnerBridge": turboChainPort2PartnerBridge,
       "relayWarning": relayWarning,
       "relayWarningTable": relayWarningTable,
       "relayWarningEntry": relayWarningEntry,
       "relayAlarmIndex": relayAlarmIndex,
       "relayWarningRelayContact": relayWarningRelayContact,
       "overrideRelayWarningSetting": overrideRelayWarningSetting,
       "relayWarningPower1Off": relayWarningPower1Off,
       "relayWarningPower1OffStatus": relayWarningPower1OffStatus,
       "relayWarningPower2Off": relayWarningPower2Off,
       "relayWarningPower2OffStatus": relayWarningPower2OffStatus,
       "relayWarningTurboRingBreak": relayWarningTurboRingBreak,
       "relayWarningTurboRingBreakStatus": relayWarningTurboRingBreakStatus,
       "portRelayWarningTable": portRelayWarningTable,
       "portRelayWarningEntry": portRelayWarningEntry,
       "relayWarningLinkChanged": relayWarningLinkChanged,
       "relayWarningLinkChangedStatus": relayWarningLinkChangedStatus,
       "relayWarningTrafficOverload": relayWarningTrafficOverload,
       "relayWarningTrafficOverloadStatus": relayWarningTrafficOverloadStatus,
       "relayWarningRxTrafficThreshold": relayWarningRxTrafficThreshold,
       "relayWarningTrafficDuration": relayWarningTrafficDuration,
       "diRelayWarningTable": diRelayWarningTable,
       "diRelayWarningEntry": diRelayWarningEntry,
       "relayWarningDiInputChanged": relayWarningDiInputChanged,
       "relayWarningDiInputChangedStatus": relayWarningDiInputChangedStatus,
       "trafficPrioritization": trafficPrioritization,
       "qosClassification": qosClassification,
       "schedulingMechanism": schedulingMechanism,
       "qosPortTable": qosPortTable,
       "qosPortEntry": qosPortEntry,
       "dscpInspection": dscpInspection,
       "cosInspection": cosInspection,
       "portPriority": portPriority,
       "priorityMapping": priorityMapping,
       "priorityMappingTable": priorityMappingTable,
       "priorityMappingEntry": priorityMappingEntry,
       "priorityTag": priorityTag,
       "priorityMappedQueue": priorityMappedQueue,
       "dscpMapping": dscpMapping,
       "dscpMappingTable": dscpMappingTable,
       "dscpMappingEntry": dscpMappingEntry,
       "dscpClass": dscpClass,
       "dscpMappedPriority": dscpMappedPriority,
       "vlan": vlan,
       "vlanPortSettingTable": vlanPortSettingTable,
       "vlanPortSettingEntry": vlanPortSettingEntry,
       "portVlanType": portVlanType,
       "portDefaultVid": portDefaultVid,
       "portFixedVid": portFixedVid,
       "portForbiddenVid": portForbiddenVid,
       "portFixedVidUntag": portFixedVidUntag,
       "vlanTable": vlanTable,
       "vlanEntry": vlanEntry,
       "vlanId": vlanId,
       "joinedAccessPorts": joinedAccessPorts,
       "joinedTrunkPorts": joinedTrunkPorts,
       "joinedHybridPorts": joinedHybridPorts,
       "vlanName": vlanName,
       "managementVlanId": managementVlanId,
       "vlanType": vlanType,
       "portbaseVlanSettingTable": portbaseVlanSettingTable,
       "portbaseVlanSettingEntry": portbaseVlanSettingEntry,
       "portbaseVlanSettingIndex": portbaseVlanSettingIndex,
       "portbaseVlanMemberPorts": portbaseVlanMemberPorts,
       "enableGvrp": enableGvrp,
       "multicastFiltering": multicastFiltering,
       "igmpSnooping": igmpSnooping,
       "querierQueryInterval": querierQueryInterval,
       "igmpSnoopingSettingTable": igmpSnoopingSettingTable,
       "igmpSnoopingSettingEntry": igmpSnoopingSettingEntry,
       "enableIgmpSnooping": enableIgmpSnooping,
       "enableQuerier": enableQuerier,
       "fixedMulticastQuerierPorts": fixedMulticastQuerierPorts,
       "learnedMulticastQuerierPorts": learnedMulticastQuerierPorts,
       "enableGlobalIgmpSnooping": enableGlobalIgmpSnooping,
       "multicastFastForwarding": multicastFastForwarding,
       "staticMulticast": staticMulticast,
       "staticMulticastTable": staticMulticastTable,
       "staticMulticastEntry": staticMulticastEntry,
       "staticMulticastAddress": staticMulticastAddress,
       "staticMulticastPorts": staticMulticastPorts,
       "staticMulticastStatus": staticMulticastStatus,
       "gmrp": gmrp,
       "gmrpSettingTable": gmrpSettingTable,
       "gmrpSettingEntry": gmrpSettingEntry,
       "enableGMRP": enableGMRP,
       "gmrpTable": gmrpTable,
       "gmrpEntry": gmrpEntry,
       "gmrpMulticastGroup": gmrpMulticastGroup,
       "gmrpFixedPorts": gmrpFixedPorts,
       "gmrpLearnedPorts": gmrpLearnedPorts,
       "mfb": mfb,
       "mfbSettingTable": mfbSettingTable,
       "mfbSettingEntry": mfbSettingEntry,
       "filterBehavior": filterBehavior,
       "rateLimiting": rateLimiting,
       "droppacketModeRateLimitingIngressTable": droppacketModeRateLimitingIngressTable,
       "droppacketModeRateLimitingIngressEntry": droppacketModeRateLimitingIngressEntry,
       "ingressLimitRate": ingressLimitRate,
       "egressLimitRate": egressLimitRate,
       "broadcastStormProtection": broadcastStormProtection,
       "bcastStormProtection": bcastStormProtection,
       "bcastStormProtectionIncludeMcast": bcastStormProtectionIncludeMcast,
       "bcastStormProtectionIncludeUcast": bcastStormProtectionIncludeUcast,
       "portDisableMode": portDisableMode,
       "portDisableModePeriod": portDisableModePeriod,
       "portDisableModeTable": portDisableModeTable,
       "portDisableModeEntry": portDisableModeEntry,
       "ingressLimit": ingressLimit,
       "rateLimitingAction": rateLimitingAction,
       "security": security,
       "userLoginSetting": userLoginSetting,
       "userLoginServer": userLoginServer,
       "tacacsServerSetting": tacacsServerSetting,
       "tacacsLoginAuthServer": tacacsLoginAuthServer,
       "tacacsLoginAuthPort": tacacsLoginAuthPort,
       "tacacsLoginAuthSharedKey": tacacsLoginAuthSharedKey,
       "tacacsLoginAuthAuthType": tacacsLoginAuthAuthType,
       "tacacsLoginAuthTimeout": tacacsLoginAuthTimeout,
       "radiusServerSetting": radiusServerSetting,
       "radiusLoginAuthServer": radiusLoginAuthServer,
       "radiusLoginAuthPort": radiusLoginAuthPort,
       "radiusLoginAuthSharedKey": radiusLoginAuthSharedKey,
       "radiusLoginAuthAuthType": radiusLoginAuthAuthType,
       "radiusLoginAuthTimeout": radiusLoginAuthTimeout,
       "portAccessControl": portAccessControl,
       "staticPortLockLegacy": staticPortLockLegacy,
       "staticPortLockLegacyAddress": staticPortLockLegacyAddress,
       "staticPortLockLegacyPort": staticPortLockLegacyPort,
       "staticPortLockLegacyStatus": staticPortLockLegacyStatus,
       "dot1x": dot1x,
       "dataBaseOption": dataBaseOption,
       "dot1xReauthEnable": dot1xReauthEnable,
       "dot1xReauthPeriod": dot1xReauthPeriod,
       "dot1xSettingTable": dot1xSettingTable,
       "dot1xSettingEntry": dot1xSettingEntry,
       "enableDot1X": enableDot1X,
       "dot1xReauthTable": dot1xReauthTable,
       "dot1xReauthEntry": dot1xReauthEntry,
       "dot1xReauthPortIndex": dot1xReauthPortIndex,
       "dot1xReauth": dot1xReauth,
       "dot1xRadius": dot1xRadius,
       "dot1xSameAsAuthServer": dot1xSameAsAuthServer,
       "dot1x1stRadiusServer": dot1x1stRadiusServer,
       "dot1x1stRadiusPort": dot1x1stRadiusPort,
       "dot1x1stRadiusSharedKey": dot1x1stRadiusSharedKey,
       "dot1x2ndRadiusServer": dot1x2ndRadiusServer,
       "dot1x2ndRadiusPort": dot1x2ndRadiusPort,
       "dot1x2ndRadiusSharedKey": dot1x2ndRadiusSharedKey,
       "portAccessControlTable": portAccessControlTable,
       "portAccessControlEntry": portAccessControlEntry,
       "portAccessControlAddress": portAccessControlAddress,
       "portAccessControlPortNo": portAccessControlPortNo,
       "portAccessControlAccessStatus": portAccessControlAccessStatus,
       "portAccessControlStatus": portAccessControlStatus,
       "portAccessControlVid": portAccessControlVid,
       "portSecurity": portSecurity,
       "portSecurityModeTable": portSecurityModeTable,
       "portSecurityModeEntry": portSecurityModeEntry,
       "portSecurityModePort": portSecurityModePort,
       "portSecurityModeSelect": portSecurityModeSelect,
       "portSecurityModeLimit": portSecurityModeLimit,
       "portSecurityModeViolationPortDisable": portSecurityModeViolationPortDisable,
       "portSecurityModeStatus": portSecurityModeStatus,
       "staticPortLock": staticPortLock,
       "staticPortLockAddress": staticPortLockAddress,
       "staticPortLockPort": staticPortLockPort,
       "staticPortLockStatus": staticPortLockStatus,
       "staticPortLockVid": staticPortLockVid,
       "macAddressSticky": macAddressSticky,
       "macAddressStickyAddress": macAddressStickyAddress,
       "macAddressStickyPort": macAddressStickyPort,
       "macAddressStickyVid": macAddressStickyVid,
       "macAddressStickyStatus": macAddressStickyStatus,
       "mab": mab,
       "mabDBOption": mabDBOption,
       "mabReauthEnable": mabReauthEnable,
       "mabReauthPeriod": mabReauthPeriod,
       "mabRestartEnable": mabRestartEnable,
       "mabRestartPeriod": mabRestartPeriod,
       "mabSettingTable": mabSettingTable,
       "mabSettingEntry": mabSettingEntry,
       "enableMAB": enableMAB,
       "accessibleIP": accessibleIP,
       "enableAccessibleIP": enableAccessibleIP,
       "accessibleIpTable": accessibleIpTable,
       "accessibleIpEntry": accessibleIpEntry,
       "accessibleIpAddress": accessibleIpAddress,
       "accessibleIpNetMask": accessibleIpNetMask,
       "accessibleIpStatus": accessibleIpStatus,
       "sysFileUpdate": sysFileUpdate,
       "tftpServer": tftpServer,
       "firmwarePathName": firmwarePathName,
       "logPathName": logPathName,
       "confPathName": confPathName,
       "tftpUpdate": tftpUpdate,
       "timeSetting": timeSetting,
       "sysDateTime": sysDateTime,
       "calibratePeriod": calibratePeriod,
       "timeServer1": timeServer1,
       "timeServer2": timeServer2,
       "daylightSaving": daylightSaving,
       "startMonth": startMonth,
       "startWeek": startWeek,
       "startDay": startDay,
       "startHour": startHour,
       "endMonth": endMonth,
       "endWeek": endWeek,
       "endDay": endDay,
       "endHour": endHour,
       "offsetHours": offsetHours,
       "enableNTPServer": enableNTPServer,
       "clockSource": clockSource,
       "ntpAuthenticate": ntpAuthenticate,
       "ntpPeerTable": ntpPeerTable,
       "ntpPeerEntry": ntpPeerEntry,
       "ntpPeerIndex": ntpPeerIndex,
       "ntpPeerAddress": ntpPeerAddress,
       "ntpPeerAuthenticate": ntpPeerAuthenticate,
       "ntpPeerAuthenticateKeyid": ntpPeerAuthenticateKeyid,
       "ntpAuthenticateKeyTable": ntpAuthenticateKeyTable,
       "ntpAuthenticateKeyEntry": ntpAuthenticateKeyEntry,
       "ntpAuthenticateKeyIndex": ntpAuthenticateKeyIndex,
       "ntpAuthenticateKeyID": ntpAuthenticateKeyID,
       "ntpAuthenticateKeyString": ntpAuthenticateKeyString,
       "ntpAuthenticateKeyTrusted": ntpAuthenticateKeyTrusted,
       "dipSwitchSetting": dipSwitchSetting,
       "dipSwitchEnableTurboRing": dipSwitchEnableTurboRing,
       "dipSwitchTurboRingPole": dipSwitchTurboRingPole,
       "dipSwitchRingCouplingPole": dipSwitchRingCouplingPole,
       "dipSwitchRingMasterPole": dipSwitchRingMasterPole,
       "backupMediaSetting": backupMediaSetting,
       "abc02Status": abc02Status,
       "abc02AutoImportConfig": abc02AutoImportConfig,
       "abc02AutoExportConfig": abc02AutoExportConfig,
       "abc02AutoExportLog": abc02AutoExportLog,
       "enableWarmStart": enableWarmStart,
       "syslogSetting": syslogSetting,
       "syslogServer1": syslogServer1,
       "syslogServer1port": syslogServer1port,
       "syslogServer2": syslogServer2,
       "syslogServer2port": syslogServer2port,
       "syslogServer3": syslogServer3,
       "syslogServer3port": syslogServer3port,
       "dhcpRelayAgentSetting": dhcpRelayAgentSetting,
       "dhcpServer1": dhcpServer1,
       "dhcpServer2": dhcpServer2,
       "dhcpServer3": dhcpServer3,
       "dhcpServer4": dhcpServer4,
       "option82Setting": option82Setting,
       "enableOption82": enableOption82,
       "option82Type": option82Type,
       "option82Value": option82Value,
       "option82ValueDisplay": option82ValueDisplay,
       "dhcpFunctionTable": dhcpFunctionTable,
       "dhcpFunctionEntry": dhcpFunctionEntry,
       "dhcpPortIndex": dhcpPortIndex,
       "circuitID": circuitID,
       "option82Enable": option82Enable,
       "poeSetting": poeSetting,
       "poePortTable": poePortTable,
       "poePortEntry": poePortEntry,
       "poePortIndex": poePortIndex,
       "poePortEnable": poePortEnable,
       "powerLimit": powerLimit,
       "pdfailure": pdfailure,
       "pdipaddr": pdipaddr,
       "pdPollingInterval": pdPollingInterval,
       "poeporttimetabling": poeporttimetabling,
       "poePortLegacyPdDetect": poePortLegacyPdDetect,
       "pdNoResponseTimeout": pdNoResponseTimeout,
       "pdNoResponseAction": pdNoResponseAction,
       "poePowerOutputMode": poePowerOutputMode,
       "poePortPowerPriority": poePortPowerPriority,
       "poeTimeTable": poeTimeTable,
       "poeTimeEntry": poeTimeEntry,
       "poeTPortIndex": poeTPortIndex,
       "poeWeekDay": poeWeekDay,
       "poeDayEnable": poeDayEnable,
       "poeDayStart": poeDayStart,
       "poeDayStop": poeDayStop,
       "poeStatusTable": poeStatusTable,
       "poeStatusEntry": poeStatusEntry,
       "poePortStatus": poePortStatus,
       "poePortConsumption": poePortConsumption,
       "poePortVoltage": poePortVoltage,
       "poePortCurrent": poePortCurrent,
       "poePortPowerOutput": poePortPowerOutput,
       "poePortClass": poePortClass,
       "poePortPdFailCheck": poePortPdFailCheck,
       "poePortPdStatusDescription": poePortPdStatusDescription,
       "poeSystemSetting": poeSystemSetting,
       "poeSysPowerEnable": poeSysPowerEnable,
       "poeSysPowerThreshold": poeSysPowerThreshold,
       "poeSysThresholdCutOff": poeSysThresholdCutOff,
       "poeSysAllocatedPower": poeSysAllocatedPower,
       "poeSysMeasuredPower": poeSysMeasuredPower,
       "poeSysPowerBudget": poeSysPowerBudget,
       "ieee1588Setting": ieee1588Setting,
       "ptpv1Setting": ptpv1Setting,
       "enablePtpv1": enablePtpv1,
       "clockModev1": clockModev1,
       "syncIntervalv1": syncIntervalv1,
       "subDomainNamev1": subDomainNamev1,
       "preferMasterv1": preferMasterv1,
       "ptpv2Setting": ptpv2Setting,
       "enablePtp": enablePtp,
       "clockMode": clockMode,
       "transport": transport,
       "syncInterval": syncInterval,
       "logMinDelayReqInterval": logMinDelayReqInterval,
       "logMinPdelayReqInterval": logMinPdelayReqInterval,
       "logAnnounceInterval": logAnnounceInterval,
       "announceReceiptTimeout": announceReceiptTimeout,
       "priority1": priority1,
       "priority2": priority2,
       "clockClass": clockClass,
       "domainNumber": domainNumber,
       "localUtcOffset": localUtcOffset,
       "localUtcOffsetValid": localUtcOffsetValid,
       "localLeap59": localLeap59,
       "localLeap61": localLeap61,
       "localPtpTimescale": localPtpTimescale,
       "localArbTime": localArbTime,
       "ptpv1Status": ptpv1Status,
       "offsetToMasterv1": offsetToMasterv1,
       "meanPathDelayv1": meanPathDelayv1,
       "grandMasterUuidv1": grandMasterUuidv1,
       "parentUuidv1": parentUuidv1,
       "clockStratumv1": clockStratumv1,
       "clockIdentifierv1": clockIdentifierv1,
       "ptpv2Status": ptpv2Status,
       "offsetToMaster": offsetToMaster,
       "meanPathDelay": meanPathDelay,
       "parentIdentity": parentIdentity,
       "grandmasterIdentity": grandmasterIdentity,
       "grandmasterClockClass": grandmasterClockClass,
       "grandmasterClockAccuracy": grandmasterClockAccuracy,
       "grandmasterPriority1": grandmasterPriority1,
       "grandmasterPriority2": grandmasterPriority2,
       "stepsRemoved": stepsRemoved,
       "currentUtcOffset": currentUtcOffset,
       "currentUtcOffsetValid": currentUtcOffsetValid,
       "leap59": leap59,
       "leap61": leap61,
       "ptpTimescale": ptpTimescale,
       "timesource": timesource,
       "ptpPortTable": ptpPortTable,
       "ptpPortEntry": ptpPortEntry,
       "ptpPortIndex": ptpPortIndex,
       "ptpPortEnable": ptpPortEnable,
       "ptpPortStatus": ptpPortStatus,
       "diagnosis": diagnosis,
       "lldpSetting": lldpSetting,
       "enableLLDP": enableLLDP,
       "lldpMSGInterval": lldpMSGInterval,
       "agingTime": agingTime,
       "garpSetting": garpSetting,
       "joinTime": joinTime,
       "leaveTime": leaveTime,
       "leaveAllTime": leaveAllTime,
       "eventlog": eventlog,
       "eventlogTable": eventlogTable,
       "eventlogEntry": eventlogEntry,
       "eventlogIndex": eventlogIndex,
       "eventlogBootup": eventlogBootup,
       "eventlogDate": eventlogDate,
       "eventlogTime": eventlogTime,
       "eventlogUptime": eventlogUptime,
       "eventlogEvent": eventlogEvent,
       "eventlogClear": eventlogClear,
       "industrialProtocol": industrialProtocol,
       "eipSetting": eipSetting,
       "enableEtherNetIP": enableEtherNetIP,
       "modbusSetting": modbusSetting,
       "enableModbus": enableModbus,
       "profinetioSetting": profinetioSetting,
       "enableProfinetIO": enableProfinetIO,
       "enableFactoryDefault": enableFactoryDefault,
       "consoleLoginMode": consoleLoginMode,
       "accessControlList": accessControlList,
       "accessControlTable": accessControlTable,
       "accessControlEntry": accessControlEntry,
       "aclRuleIndex": aclRuleIndex,
       "listID": listID,
       "filterType": filterType,
       "actionFlag": actionFlag,
       "srcMacAddr": srcMacAddr,
       "srcMacMask": srcMacMask,
       "dstMacAddr": dstMacAddr,
       "dstMacMask": dstMacMask,
       "etherType": etherType,
       "vlanID": vlanID,
       "srcIpAddr": srcIpAddr,
       "srcNetmask": srcNetmask,
       "dstIpAddr": dstIpAddr,
       "dstNetmask": dstNetmask,
       "protocolCode": protocolCode,
       "srcsocketPort": srcsocketPort,
       "dstsocketPort": dstsocketPort,
       "aclStatus": aclStatus,
       "aclAttachmentTable": aclAttachmentTable,
       "aclAttachmentEntry": aclAttachmentEntry,
       "aclID": aclID,
       "ingressPort": ingressPort,
       "aclListName": aclListName,
       "cpuLoading5s": cpuLoading5s,
       "cpuLoading30s": cpuLoading30s,
       "cpuLoading300s": cpuLoading300s,
       "totalMemory": totalMemory,
       "freeMemory": freeMemory,
       "usedMemory": usedMemory,
       "memoryUsage": memoryUsage,
       "loopProtection": loopProtection,
       "eventSettings": eventSettings,
       "systemEventSettingsTable": systemEventSettingsTable,
       "systemEventSettingsEntry": systemEventSettingsEntry,
       "systemEventIndex": systemEventIndex,
       "systemEventActive": systemEventActive,
       "systemEventName": systemEventName,
       "systemEventSupport": systemEventSupport,
       "systemEventModuleEnable": systemEventModuleEnable,
       "systemEventSeverity": systemEventSeverity,
       "portEventSettingsTable": portEventSettingsTable,
       "portEventSettingsEntry": portEventSettingsEntry,
       "portEventIndex": portEventIndex,
       "portEventLabel": portEventLabel,
       "portEventActive": portEventActive,
       "portEventEnable": portEventEnable,
       "portEventTrafficThreshold": portEventTrafficThreshold,
       "portEventTrafficDuration": portEventTrafficDuration,
       "portEventModuleEnable": portEventModuleEnable,
       "portEventSeverity": portEventSeverity,
       "managementInterface": managementInterface,
       "httpEnable": httpEnable,
       "httpPort": httpPort,
       "sslEnable": sslEnable,
       "sslPort": sslPort,
       "telnetEnable": telnetEnable,
       "telnetPort": telnetPort,
       "sshEnable": sshEnable,
       "sshPort": sshPort,
       "mgmtInterfaceAutoLogout": mgmtInterfaceAutoLogout,
       "snmpdEnable": snmpdEnable,
       "snmpdPort": snmpdPort,
       "moxaUtilityServiceEnable": moxaUtilityServiceEnable,
       "moxaUtilityServicePort": moxaUtilityServicePort,
       "httpMaxLoginUsers": httpMaxLoginUsers,
       "telnetMaxLoginUsers": telnetMaxLoginUsers,
       "moxaNewCmdEnable": moxaNewCmdEnable,
       "switchLocator": switchLocator,
       "blinkingLocatorLED": blinkingLocatorLED,
       "disableLocatorLEDTime": disableLocatorLEDTime,
       "uiVersion": uiVersion,
       "supportIfXTable": supportIfXTable,
       "passwordPolicy": passwordPolicy,
       "pwdMinLength": pwdMinLength,
       "pwdComplexityCheckEnable": pwdComplexityCheckEnable,
       "pwdComplexityCheckDigitEnable": pwdComplexityCheckDigitEnable,
       "pwdComplexityCheckAlphabetEnable": pwdComplexityCheckAlphabetEnable,
       "pwdComplexityCheckSpecialCharEnable": pwdComplexityCheckSpecialCharEnable,
       "loginLockout": loginLockout,
       "loginFailureLockoutEnable": loginFailureLockoutEnable,
       "loginFailureLockoutRetrys": loginFailureLockoutRetrys,
       "loginFailureLockoutTime": loginFailureLockoutTime,
       "systemNotifyMessage": systemNotifyMessage,
       "httpLoginMessage": httpLoginMessage,
       "httpLoginFailureMessage": httpLoginFailureMessage,
       "syslogManagement": syslogManagement,
       "loggingCapacityThreshold": loggingCapacityThreshold,
       "loggingCapacityTrapWarningEnable": loggingCapacityTrapWarningEnable,
       "loggingCapacityEmailWarningEnable": loggingCapacityEmailWarningEnable,
       "loggingOversizeAction": loggingOversizeAction,
       "certificateManagement": certificateManagement,
       "sslCertGen": sslCertGen,
       "sshKeyGen": sshKeyGen,
       "ivlSwitch": ivlSwitch,
       "supportMacSticky": supportMacSticky,
       "serialNumber": serialNumber,
       "configEncryptEnable": configEncryptEnable,
       "swTraps": swTraps,
       "varconfigChangeTrap": varconfigChangeTrap,
       "varpower1Trap": varpower1Trap,
       "varpower2Trap": varpower2Trap,
       "vartrafficOverloadTrap": vartrafficOverloadTrap,
       "varredundancyTopologyChangedTrap": varredundancyTopologyChangedTrap,
       "varturboRingCouplingPortChangedTrap": varturboRingCouplingPortChangedTrap,
       "varturboRingMasterChangedTrap": varturboRingMasterChangedTrap,
       "varPoEWarningTrap": varPoEWarningTrap,
       "varPortLoopDetectedTrap": varPortLoopDetectedTrap,
       "varRateLimitedOnTrap": varRateLimitedOnTrap,
       "varLLDPChgTrap": varLLDPChgTrap,
       "varABC02WarningTrap": varABC02WarningTrap,
       "varturboRingMasterMismatchTrap": varturboRingMasterMismatchTrap,
       "varUserAuthSuccessTrap": varUserAuthSuccessTrap,
       "varUserAuthFailTrap": varUserAuthFailTrap,
       "varMacStickyPortViolationPortDisableTrap": varMacStickyPortViolationPortDisableTrap,
       "varFiberWarningTrap": varFiberWarningTrap,
       "varLoggingCapacityTrap": varLoggingCapacityTrap,
       "varUserInfoChgTrap": varUserInfoChgTrap,
       "varConfigImportTrap": varConfigImportTrap,
       "varRemoteAuthSuccessTrap": varRemoteAuthSuccessTrap,
       "varRemoteAuthFailTrap": varRemoteAuthFailTrap,
       "varEPSChangeToOn": varEPSChangeToOn,
       "varEPSChangeToOff": varEPSChangeToOff}
)
