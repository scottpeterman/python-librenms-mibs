# SNMP MIB module (FORTINET-FORTIEXTENDER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\fortinet\FORTINET-FORTIEXTENDER-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:44:49 2025
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

(FnBoolState,
 FnIndex,
 fortinet) = mibBuilder.importSymbols(
    "FORTINET-CORE-MIB",
    "FnBoolState",
    "FnIndex",
    "fortinet")

(ifEntry,
 ifIndex,
 ifName) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifEntry",
    "ifIndex",
    "ifName")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

fnFortiExtenderMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FextHeader_ObjectIdentity = ObjectIdentity
fextHeader = _FextHeader_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 1)
)
_FextVersion_ObjectIdentity = ObjectIdentity
fextVersion = _FextVersion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 1, 1)
)


class _FextVersionConfig_Type(DisplayString):
    """Custom type fextVersionConfig based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FextVersionConfig_Type.__name__ = "DisplayString"
_FextVersionConfig_Object = MibScalar
fextVersionConfig = _FextVersionConfig_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 1, 1, 1),
    _FextVersionConfig_Type()
)
fextVersionConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextVersionConfig.setStatus("current")


class _FextVersionCarrier_Type(DisplayString):
    """Custom type fextVersionCarrier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_FextVersionCarrier_Type.__name__ = "DisplayString"
_FextVersionCarrier_Object = MibScalar
fextVersionCarrier = _FextVersionCarrier_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 1, 1, 2),
    _FextVersionCarrier_Type()
)
fextVersionCarrier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextVersionCarrier.setStatus("current")


class _FextVersionSimmap_Type(DisplayString):
    """Custom type fextVersionSimmap based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FextVersionSimmap_Type.__name__ = "DisplayString"
_FextVersionSimmap_Object = MibScalar
fextVersionSimmap = _FextVersionSimmap_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 1, 1, 3),
    _FextVersionSimmap_Type()
)
fextVersionSimmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextVersionSimmap.setStatus("current")
_FextSystem_ObjectIdentity = ObjectIdentity
fextSystem = _FextSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2)
)
_FextGlobal_ObjectIdentity = ObjectIdentity
fextGlobal = _FextGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 1)
)
if mibBuilder.loadTexts:
    fextGlobal.setStatus("current")


class _FextHostname_Type(DisplayString):
    """Custom type fextHostname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FextHostname_Type.__name__ = "DisplayString"
_FextHostname_Object = MibScalar
fextHostname = _FextHostname_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 1, 1),
    _FextHostname_Type()
)
fextHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextHostname.setStatus("current")


class _FextTimezone_Type(Integer32):
    """Custom type fextTimezone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 82),
    )


_FextTimezone_Type.__name__ = "Integer32"
_FextTimezone_Object = MibScalar
fextTimezone = _FextTimezone_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 1, 2),
    _FextTimezone_Type()
)
fextTimezone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextTimezone.setStatus("current")
_FextAutoInstallImage_Type = DisplayString
_FextAutoInstallImage_Object = MibScalar
fextAutoInstallImage = _FextAutoInstallImage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 1, 3),
    _FextAutoInstallImage_Type()
)
fextAutoInstallImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextAutoInstallImage.setStatus("current")


class _FextDefaultImageFile_Type(DisplayString):
    """Custom type fextDefaultImageFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FextDefaultImageFile_Type.__name__ = "DisplayString"
_FextDefaultImageFile_Object = MibScalar
fextDefaultImageFile = _FextDefaultImageFile_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 1, 4),
    _FextDefaultImageFile_Type()
)
fextDefaultImageFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextDefaultImageFile.setStatus("current")


class _FextMDMFWServer_Type(DisplayString):
    """Custom type fextMDMFWServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FextMDMFWServer_Type.__name__ = "DisplayString"
_FextMDMFWServer_Object = MibScalar
fextMDMFWServer = _FextMDMFWServer_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 1, 5),
    _FextMDMFWServer_Type()
)
fextMDMFWServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextMDMFWServer.setStatus("current")


class _FextOSFWServer_Type(DisplayString):
    """Custom type fextOSFWServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FextOSFWServer_Type.__name__ = "DisplayString"
_FextOSFWServer_Object = MibScalar
fextOSFWServer = _FextOSFWServer_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 1, 6),
    _FextOSFWServer_Type()
)
fextOSFWServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextOSFWServer.setStatus("current")
_FextManagement_ObjectIdentity = ObjectIdentity
fextManagement = _FextManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 2)
)
if mibBuilder.loadTexts:
    fextManagement.setStatus("current")
_FextMgmtDiscoveryType_Type = DisplayString
_FextMgmtDiscoveryType_Object = MibScalar
fextMgmtDiscoveryType = _FextMgmtDiscoveryType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 2, 1),
    _FextMgmtDiscoveryType_Type()
)
fextMgmtDiscoveryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextMgmtDiscoveryType.setStatus("current")
_FextMgmtFortigate_ObjectIdentity = ObjectIdentity
fextMgmtFortigate = _FextMgmtFortigate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 2, 2)
)
if mibBuilder.loadTexts:
    fextMgmtFortigate.setStatus("current")
_FextFGTDiscoveryType_Type = DisplayString
_FextFGTDiscoveryType_Object = MibScalar
fextFGTDiscoveryType = _FextFGTDiscoveryType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 2, 2, 1),
    _FextFGTDiscoveryType_Type()
)
fextFGTDiscoveryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextFGTDiscoveryType.setStatus("current")
_FextFGTStaticIP_Type = DisplayString
_FextFGTStaticIP_Object = MibScalar
fextFGTStaticIP = _FextFGTStaticIP_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 2, 2, 2),
    _FextFGTStaticIP_Type()
)
fextFGTStaticIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextFGTStaticIP.setStatus("current")


class _FextFGTControlPort_Type(Integer32):
    """Custom type fextFGTControlPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 49150),
    )


_FextFGTControlPort_Type.__name__ = "Integer32"
_FextFGTControlPort_Object = MibScalar
fextFGTControlPort = _FextFGTControlPort_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 2, 2, 3),
    _FextFGTControlPort_Type()
)
fextFGTControlPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextFGTControlPort.setStatus("current")


class _FextFGTDataPort_Type(Integer32):
    """Custom type fextFGTDataPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 49150),
    )


_FextFGTDataPort_Type.__name__ = "Integer32"
_FextFGTDataPort_Object = MibScalar
fextFGTDataPort = _FextFGTDataPort_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 2, 2, 4),
    _FextFGTDataPort_Type()
)
fextFGTDataPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextFGTDataPort.setStatus("current")
_FextFGTDiscoveryIntf_Type = DisplayString
_FextFGTDiscoveryIntf_Object = MibScalar
fextFGTDiscoveryIntf = _FextFGTDiscoveryIntf_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 2, 2, 5),
    _FextFGTDiscoveryIntf_Type()
)
fextFGTDiscoveryIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextFGTDiscoveryIntf.setStatus("current")
_FextFGTIngressIntf_Type = DisplayString
_FextFGTIngressIntf_Object = MibScalar
fextFGTIngressIntf = _FextFGTIngressIntf_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 2, 2, 6),
    _FextFGTIngressIntf_Type()
)
fextFGTIngressIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextFGTIngressIntf.setStatus("current")
_FextMgmtCloud_ObjectIdentity = ObjectIdentity
fextMgmtCloud = _FextMgmtCloud_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 2, 3)
)
if mibBuilder.loadTexts:
    fextMgmtCloud.setStatus("current")
_FextCloudDispatcher_Type = DisplayString
_FextCloudDispatcher_Object = MibScalar
fextCloudDispatcher = _FextCloudDispatcher_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 2, 3, 1),
    _FextCloudDispatcher_Type()
)
fextCloudDispatcher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextCloudDispatcher.setStatus("current")
_FextCloudDispatcherPort_Type = Integer32
_FextCloudDispatcherPort_Object = MibScalar
fextCloudDispatcherPort = _FextCloudDispatcherPort_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 2, 3, 2),
    _FextCloudDispatcherPort_Type()
)
fextCloudDispatcherPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextCloudDispatcherPort.setStatus("current")
_FextCloudMode_Type = DisplayString
_FextCloudMode_Object = MibScalar
fextCloudMode = _FextCloudMode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 2, 3, 3),
    _FextCloudMode_Type()
)
fextCloudMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextCloudMode.setStatus("current")
_FextCloudProxy_Type = DisplayString
_FextCloudProxy_Object = MibScalar
fextCloudProxy = _FextCloudProxy_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 2, 3, 4),
    _FextCloudProxy_Type()
)
fextCloudProxy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextCloudProxy.setStatus("current")
_FextCloudProxyServer_Type = DisplayString
_FextCloudProxyServer_Object = MibScalar
fextCloudProxyServer = _FextCloudProxyServer_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 2, 3, 5),
    _FextCloudProxyServer_Type()
)
fextCloudProxyServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextCloudProxyServer.setStatus("current")
_FextCloudProxyPort_Type = Integer32
_FextCloudProxyPort_Object = MibScalar
fextCloudProxyPort = _FextCloudProxyPort_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 2, 3, 6),
    _FextCloudProxyPort_Type()
)
fextCloudProxyPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextCloudProxyPort.setStatus("current")
_FextMgmtLocal_ObjectIdentity = ObjectIdentity
fextMgmtLocal = _FextMgmtLocal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 2, 4)
)
if mibBuilder.loadTexts:
    fextMgmtLocal.setStatus("current")
_FextLocalMode_Type = DisplayString
_FextLocalMode_Object = MibScalar
fextLocalMode = _FextLocalMode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 2, 4, 1),
    _FextLocalMode_Type()
)
fextLocalMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextLocalMode.setStatus("current")
_FextMgmtLocalAccess_ObjectIdentity = ObjectIdentity
fextMgmtLocalAccess = _FextMgmtLocalAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 2, 5)
)
if mibBuilder.loadTexts:
    fextMgmtLocalAccess.setStatus("current")


class _FextAccessHTTP_Type(Integer32):
    """Custom type fextAccessHTTP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FextAccessHTTP_Type.__name__ = "Integer32"
_FextAccessHTTP_Object = MibScalar
fextAccessHTTP = _FextAccessHTTP_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 2, 5, 1),
    _FextAccessHTTP_Type()
)
fextAccessHTTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextAccessHTTP.setStatus("current")


class _FextAccessHTTPS_Type(Integer32):
    """Custom type fextAccessHTTPS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FextAccessHTTPS_Type.__name__ = "Integer32"
_FextAccessHTTPS_Object = MibScalar
fextAccessHTTPS = _FextAccessHTTPS_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 2, 5, 2),
    _FextAccessHTTPS_Type()
)
fextAccessHTTPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextAccessHTTPS.setStatus("current")


class _FextAccessSSH_Type(Integer32):
    """Custom type fextAccessSSH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FextAccessSSH_Type.__name__ = "Integer32"
_FextAccessSSH_Object = MibScalar
fextAccessSSH = _FextAccessSSH_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 2, 5, 3),
    _FextAccessSSH_Type()
)
fextAccessSSH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextAccessSSH.setStatus("current")


class _FextAccessTelnet_Type(Integer32):
    """Custom type fextAccessTelnet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FextAccessTelnet_Type.__name__ = "Integer32"
_FextAccessTelnet_Object = MibScalar
fextAccessTelnet = _FextAccessTelnet_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 2, 5, 4),
    _FextAccessTelnet_Type()
)
fextAccessTelnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextAccessTelnet.setStatus("current")


class _FextAccessTimeout_Type(Integer32):
    """Custom type fextAccessTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 480),
    )


_FextAccessTimeout_Type.__name__ = "Integer32"
_FextAccessTimeout_Object = MibScalar
fextAccessTimeout = _FextAccessTimeout_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 2, 5, 5),
    _FextAccessTimeout_Type()
)
fextAccessTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextAccessTimeout.setStatus("current")
_FextMgmtFGTBackup_ObjectIdentity = ObjectIdentity
fextMgmtFGTBackup = _FextMgmtFGTBackup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 2, 6)
)
if mibBuilder.loadTexts:
    fextMgmtFGTBackup.setStatus("current")
_FextBackupVRRPInterface_Type = DisplayString
_FextBackupVRRPInterface_Object = MibScalar
fextBackupVRRPInterface = _FextBackupVRRPInterface_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 2, 6, 1),
    _FextBackupVRRPInterface_Type()
)
fextBackupVRRPInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextBackupVRRPInterface.setStatus("current")
_FextBackupStatus_Type = DisplayString
_FextBackupStatus_Object = MibScalar
fextBackupStatus = _FextBackupStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 2, 6, 2),
    _FextBackupStatus_Type()
)
fextBackupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextBackupStatus.setStatus("current")
_FextInterface_Object = MibTable
fextInterface = _FextInterface_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 3)
)
if mibBuilder.loadTexts:
    fextInterface.setStatus("current")
_FextInterfaceEntry_Object = MibTableRow
fextInterfaceEntry = _FextInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 3, 1)
)
fextInterfaceEntry.setIndexNames(
    (0, "FORTINET-FORTIEXTENDER-MIB", "fextInterfaceIndex"),
)
if mibBuilder.loadTexts:
    fextInterfaceEntry.setStatus("current")
_FextInterfaceIndex_Type = FnIndex
_FextInterfaceIndex_Object = MibTableColumn
fextInterfaceIndex = _FextInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 3, 1, 1),
    _FextInterfaceIndex_Type()
)
fextInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fextInterfaceIndex.setStatus("current")
_FextInterfaceName_Type = DisplayString
_FextInterfaceName_Object = MibTableColumn
fextInterfaceName = _FextInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 3, 1, 2),
    _FextInterfaceName_Type()
)
fextInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInterfaceName.setStatus("current")
_FextInterfaceType_Type = DisplayString
_FextInterfaceType_Object = MibTableColumn
fextInterfaceType = _FextInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 3, 1, 3),
    _FextInterfaceType_Type()
)
fextInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInterfaceType.setStatus("current")
_FextInterfaceStatus_Type = DisplayString
_FextInterfaceStatus_Object = MibTableColumn
fextInterfaceStatus = _FextInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 3, 1, 4),
    _FextInterfaceStatus_Type()
)
fextInterfaceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInterfaceStatus.setStatus("current")
_FextInterfaceMode_Type = DisplayString
_FextInterfaceMode_Object = MibTableColumn
fextInterfaceMode = _FextInterfaceMode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 3, 1, 5),
    _FextInterfaceMode_Type()
)
fextInterfaceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInterfaceMode.setStatus("current")
_FextInterfaceIP_Type = DisplayString
_FextInterfaceIP_Object = MibTableColumn
fextInterfaceIP = _FextInterfaceIP_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 3, 1, 6),
    _FextInterfaceIP_Type()
)
fextInterfaceIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInterfaceIP.setStatus("current")


class _FextInterfaceIPMask_Type(Integer32):
    """Custom type fextInterfaceIPMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 32),
    )


_FextInterfaceIPMask_Type.__name__ = "Integer32"
_FextInterfaceIPMask_Object = MibTableColumn
fextInterfaceIPMask = _FextInterfaceIPMask_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 3, 1, 7),
    _FextInterfaceIPMask_Type()
)
fextInterfaceIPMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInterfaceIPMask.setStatus("current")
_FextInterfaceGateway_Type = DisplayString
_FextInterfaceGateway_Object = MibTableColumn
fextInterfaceGateway = _FextInterfaceGateway_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 3, 1, 8),
    _FextInterfaceGateway_Type()
)
fextInterfaceGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInterfaceGateway.setStatus("current")
_FextInterfaceMTUOverride_Type = DisplayString
_FextInterfaceMTUOverride_Object = MibTableColumn
fextInterfaceMTUOverride = _FextInterfaceMTUOverride_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 3, 1, 9),
    _FextInterfaceMTUOverride_Type()
)
fextInterfaceMTUOverride.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInterfaceMTUOverride.setStatus("current")


class _FextInterfaceMTU_Type(Integer32):
    """Custom type fextInterfaceMTU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 1500),
    )


_FextInterfaceMTU_Type.__name__ = "Integer32"
_FextInterfaceMTU_Object = MibTableColumn
fextInterfaceMTU = _FextInterfaceMTU_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 3, 1, 10),
    _FextInterfaceMTU_Type()
)
fextInterfaceMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInterfaceMTU.setStatus("current")


class _FextInterfaceRID_Type(Integer32):
    """Custom type fextInterfaceRID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 1500),
    )


_FextInterfaceRID_Type.__name__ = "Integer32"
_FextInterfaceRID_Object = MibTableColumn
fextInterfaceRID = _FextInterfaceRID_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 3, 1, 11),
    _FextInterfaceRID_Type()
)
fextInterfaceRID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInterfaceRID.setStatus("current")


class _FextInterfaceVID_Type(Integer32):
    """Custom type fextInterfaceVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 1500),
    )


_FextInterfaceVID_Type.__name__ = "Integer32"
_FextInterfaceVID_Object = MibTableColumn
fextInterfaceVID = _FextInterfaceVID_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 3, 1, 12),
    _FextInterfaceVID_Type()
)
fextInterfaceVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInterfaceVID.setStatus("current")
_FextInterfaceIngressIntf_Type = DisplayString
_FextInterfaceIngressIntf_Object = MibTableColumn
fextInterfaceIngressIntf = _FextInterfaceIngressIntf_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 3, 1, 13),
    _FextInterfaceIngressIntf_Type()
)
fextInterfaceIngressIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInterfaceIngressIntf.setStatus("current")
_FextInterfaceVRRPVirtualMAC_Type = DisplayString
_FextInterfaceVRRPVirtualMAC_Object = MibTableColumn
fextInterfaceVRRPVirtualMAC = _FextInterfaceVRRPVirtualMAC_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 3, 1, 14),
    _FextInterfaceVRRPVirtualMAC_Type()
)
fextInterfaceVRRPVirtualMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInterfaceVRRPVirtualMAC.setStatus("current")
_FextInterfaceAllowAccess_Type = DisplayString
_FextInterfaceAllowAccess_Object = MibTableColumn
fextInterfaceAllowAccess = _FextInterfaceAllowAccess_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 3, 1, 15),
    _FextInterfaceAllowAccess_Type()
)
fextInterfaceAllowAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInterfaceAllowAccess.setStatus("current")
_FextInterfaceAlgorithm_Type = DisplayString
_FextInterfaceAlgorithm_Object = MibTableColumn
fextInterfaceAlgorithm = _FextInterfaceAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 3, 1, 16),
    _FextInterfaceAlgorithm_Type()
)
fextInterfaceAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInterfaceAlgorithm.setStatus("current")
_FextInterfaceFEC_Type = DisplayString
_FextInterfaceFEC_Object = MibTableColumn
fextInterfaceFEC = _FextInterfaceFEC_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 3, 1, 17),
    _FextInterfaceFEC_Type()
)
fextInterfaceFEC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInterfaceFEC.setStatus("current")


class _FextInterfaceSessionTimeout_Type(Integer32):
    """Custom type fextInterfaceSessionTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_FextInterfaceSessionTimeout_Type.__name__ = "Integer32"
_FextInterfaceSessionTimeout_Object = MibTableColumn
fextInterfaceSessionTimeout = _FextInterfaceSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 3, 1, 18),
    _FextInterfaceSessionTimeout_Type()
)
fextInterfaceSessionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInterfaceSessionTimeout.setStatus("current")


class _FextInterfaceGracePeriod_Type(Integer32):
    """Custom type fextInterfaceGracePeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_FextInterfaceGracePeriod_Type.__name__ = "Integer32"
_FextInterfaceGracePeriod_Object = MibTableColumn
fextInterfaceGracePeriod = _FextInterfaceGracePeriod_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 3, 1, 19),
    _FextInterfaceGracePeriod_Type()
)
fextInterfaceGracePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInterfaceGracePeriod.setStatus("current")
_FextInterfaceMembers_Type = DisplayString
_FextInterfaceMembers_Object = MibTableColumn
fextInterfaceMembers = _FextInterfaceMembers_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 3, 1, 20),
    _FextInterfaceMembers_Type()
)
fextInterfaceMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInterfaceMembers.setStatus("current")
_FextDHCPServer_Object = MibTable
fextDHCPServer = _FextDHCPServer_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 4)
)
if mibBuilder.loadTexts:
    fextDHCPServer.setStatus("current")
_FextDHCPServerEntry_Object = MibTableRow
fextDHCPServerEntry = _FextDHCPServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 4, 1)
)
fextDHCPServerEntry.setIndexNames(
    (0, "FORTINET-FORTIEXTENDER-MIB", "fextDHCPServerIndex"),
)
if mibBuilder.loadTexts:
    fextDHCPServerEntry.setStatus("current")
_FextDHCPServerIndex_Type = FnIndex
_FextDHCPServerIndex_Object = MibTableColumn
fextDHCPServerIndex = _FextDHCPServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 4, 1, 1),
    _FextDHCPServerIndex_Type()
)
fextDHCPServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fextDHCPServerIndex.setStatus("current")
_FextDHCPServerName_Type = DisplayString
_FextDHCPServerName_Object = MibTableColumn
fextDHCPServerName = _FextDHCPServerName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 4, 1, 2),
    _FextDHCPServerName_Type()
)
fextDHCPServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextDHCPServerName.setStatus("current")
_FextDHCPServerStatus_Type = DisplayString
_FextDHCPServerStatus_Object = MibTableColumn
fextDHCPServerStatus = _FextDHCPServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 4, 1, 3),
    _FextDHCPServerStatus_Type()
)
fextDHCPServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextDHCPServerStatus.setStatus("current")


class _FextDHCPServerLeaseTime_Type(Integer32):
    """Custom type fextDHCPServerLeaseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 8640000),
    )


_FextDHCPServerLeaseTime_Type.__name__ = "Integer32"
_FextDHCPServerLeaseTime_Object = MibTableColumn
fextDHCPServerLeaseTime = _FextDHCPServerLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 4, 1, 4),
    _FextDHCPServerLeaseTime_Type()
)
fextDHCPServerLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextDHCPServerLeaseTime.setStatus("current")
_FextDHCPServerDNS_Type = DisplayString
_FextDHCPServerDNS_Object = MibTableColumn
fextDHCPServerDNS = _FextDHCPServerDNS_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 4, 1, 5),
    _FextDHCPServerDNS_Type()
)
fextDHCPServerDNS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextDHCPServerDNS.setStatus("current")
_FextDHCPServerNTP_Type = DisplayString
_FextDHCPServerNTP_Object = MibTableColumn
fextDHCPServerNTP = _FextDHCPServerNTP_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 4, 1, 6),
    _FextDHCPServerNTP_Type()
)
fextDHCPServerNTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextDHCPServerNTP.setStatus("current")
_FextDHCPServerNTP1_Type = DisplayString
_FextDHCPServerNTP1_Object = MibTableColumn
fextDHCPServerNTP1 = _FextDHCPServerNTP1_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 4, 1, 7),
    _FextDHCPServerNTP1_Type()
)
fextDHCPServerNTP1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextDHCPServerNTP1.setStatus("current")
_FextDHCPServerNTP2_Type = DisplayString
_FextDHCPServerNTP2_Object = MibTableColumn
fextDHCPServerNTP2 = _FextDHCPServerNTP2_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 4, 1, 8),
    _FextDHCPServerNTP2_Type()
)
fextDHCPServerNTP2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextDHCPServerNTP2.setStatus("current")
_FextDHCPServerNTP3_Type = DisplayString
_FextDHCPServerNTP3_Object = MibTableColumn
fextDHCPServerNTP3 = _FextDHCPServerNTP3_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 4, 1, 9),
    _FextDHCPServerNTP3_Type()
)
fextDHCPServerNTP3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextDHCPServerNTP3.setStatus("current")
_FextDHCPServerGatewayIP_Type = DisplayString
_FextDHCPServerGatewayIP_Object = MibTableColumn
fextDHCPServerGatewayIP = _FextDHCPServerGatewayIP_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 4, 1, 10),
    _FextDHCPServerGatewayIP_Type()
)
fextDHCPServerGatewayIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextDHCPServerGatewayIP.setStatus("current")
_FextDHCPServerNetmask_Type = DisplayString
_FextDHCPServerNetmask_Object = MibTableColumn
fextDHCPServerNetmask = _FextDHCPServerNetmask_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 4, 1, 11),
    _FextDHCPServerNetmask_Type()
)
fextDHCPServerNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextDHCPServerNetmask.setStatus("current")
_FextDHCPServerInterface_Type = DisplayString
_FextDHCPServerInterface_Object = MibTableColumn
fextDHCPServerInterface = _FextDHCPServerInterface_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 4, 1, 12),
    _FextDHCPServerInterface_Type()
)
fextDHCPServerInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextDHCPServerInterface.setStatus("current")
_FextDHCPServerStartIP_Type = DisplayString
_FextDHCPServerStartIP_Object = MibTableColumn
fextDHCPServerStartIP = _FextDHCPServerStartIP_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 4, 1, 13),
    _FextDHCPServerStartIP_Type()
)
fextDHCPServerStartIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextDHCPServerStartIP.setStatus("current")
_FextDHCPServerEndIP_Type = DisplayString
_FextDHCPServerEndIP_Object = MibTableColumn
fextDHCPServerEndIP = _FextDHCPServerEndIP_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 4, 1, 14),
    _FextDHCPServerEndIP_Type()
)
fextDHCPServerEndIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextDHCPServerEndIP.setStatus("current")


class _FextDHCPServerMTU_Type(Integer32):
    """Custom type fextDHCPServerMTU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 9000),
    )


_FextDHCPServerMTU_Type.__name__ = "Integer32"
_FextDHCPServerMTU_Object = MibTableColumn
fextDHCPServerMTU = _FextDHCPServerMTU_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 4, 1, 15),
    _FextDHCPServerMTU_Type()
)
fextDHCPServerMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextDHCPServerMTU.setStatus("current")
_FextDNS_ObjectIdentity = ObjectIdentity
fextDNS = _FextDNS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 5)
)
if mibBuilder.loadTexts:
    fextDNS.setStatus("current")
_FextDNSPrimary_Type = DisplayString
_FextDNSPrimary_Object = MibScalar
fextDNSPrimary = _FextDNSPrimary_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 5, 1),
    _FextDNSPrimary_Type()
)
fextDNSPrimary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextDNSPrimary.setStatus("current")
_FextDNSSecondary_Type = DisplayString
_FextDNSSecondary_Object = MibScalar
fextDNSSecondary = _FextDNSSecondary_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 5, 2),
    _FextDNSSecondary_Type()
)
fextDNSSecondary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextDNSSecondary.setStatus("current")
_FextDNSOrder_Type = DisplayString
_FextDNSOrder_Object = MibScalar
fextDNSOrder = _FextDNSOrder_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 5, 3),
    _FextDNSOrder_Type()
)
fextDNSOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextDNSOrder.setStatus("current")
_FextVWANMember_Object = MibTable
fextVWANMember = _FextVWANMember_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 6)
)
if mibBuilder.loadTexts:
    fextVWANMember.setStatus("current")
_FextVWANMemberEntry_Object = MibTableRow
fextVWANMemberEntry = _FextVWANMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 6, 1)
)
fextVWANMemberEntry.setIndexNames(
    (0, "FORTINET-FORTIEXTENDER-MIB", "fextVWANMemberIndex"),
)
if mibBuilder.loadTexts:
    fextVWANMemberEntry.setStatus("current")
_FextVWANMemberIndex_Type = FnIndex
_FextVWANMemberIndex_Object = MibTableColumn
fextVWANMemberIndex = _FextVWANMemberIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 6, 1, 1),
    _FextVWANMemberIndex_Type()
)
fextVWANMemberIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fextVWANMemberIndex.setStatus("current")
_FextVWANMemberName_Type = DisplayString
_FextVWANMemberName_Object = MibTableColumn
fextVWANMemberName = _FextVWANMemberName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 6, 1, 2),
    _FextVWANMemberName_Type()
)
fextVWANMemberName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextVWANMemberName.setStatus("current")
_FextVWANMemberTarget_Type = DisplayString
_FextVWANMemberTarget_Object = MibTableColumn
fextVWANMemberTarget = _FextVWANMemberTarget_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 6, 1, 3),
    _FextVWANMemberTarget_Type()
)
fextVWANMemberTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextVWANMemberTarget.setStatus("current")


class _FextVWANMemberPriority_Type(Integer32):
    """Custom type fextVWANMemberPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_FextVWANMemberPriority_Type.__name__ = "Integer32"
_FextVWANMemberPriority_Object = MibTableColumn
fextVWANMemberPriority = _FextVWANMemberPriority_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 6, 1, 4),
    _FextVWANMemberPriority_Type()
)
fextVWANMemberPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextVWANMemberPriority.setStatus("current")


class _FextVWANMemberWeight_Type(Integer32):
    """Custom type fextVWANMemberWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_FextVWANMemberWeight_Type.__name__ = "Integer32"
_FextVWANMemberWeight_Object = MibTableColumn
fextVWANMemberWeight = _FextVWANMemberWeight_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 6, 1, 5),
    _FextVWANMemberWeight_Type()
)
fextVWANMemberWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextVWANMemberWeight.setStatus("current")


class _FextVWANMemberInThreshold_Type(Integer32):
    """Custom type fextVWANMemberInThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FextVWANMemberInThreshold_Type.__name__ = "Integer32"
_FextVWANMemberInThreshold_Object = MibTableColumn
fextVWANMemberInThreshold = _FextVWANMemberInThreshold_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 6, 1, 6),
    _FextVWANMemberInThreshold_Type()
)
fextVWANMemberInThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextVWANMemberInThreshold.setStatus("current")


class _FextVWANMemberOutThreshold_Type(Integer32):
    """Custom type fextVWANMemberOutThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FextVWANMemberOutThreshold_Type.__name__ = "Integer32"
_FextVWANMemberOutThreshold_Object = MibTableColumn
fextVWANMemberOutThreshold = _FextVWANMemberOutThreshold_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 6, 1, 7),
    _FextVWANMemberOutThreshold_Type()
)
fextVWANMemberOutThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextVWANMemberOutThreshold.setStatus("current")


class _FextVWANMemberAllThreshold_Type(Integer32):
    """Custom type fextVWANMemberAllThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FextVWANMemberAllThreshold_Type.__name__ = "Integer32"
_FextVWANMemberAllThreshold_Object = MibTableColumn
fextVWANMemberAllThreshold = _FextVWANMemberAllThreshold_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 6, 1, 8),
    _FextVWANMemberAllThreshold_Type()
)
fextVWANMemberAllThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextVWANMemberAllThreshold.setStatus("current")
_FextVWANMemberHchk_Type = DisplayString
_FextVWANMemberHchk_Object = MibTableColumn
fextVWANMemberHchk = _FextVWANMemberHchk_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 6, 1, 9),
    _FextVWANMemberHchk_Type()
)
fextVWANMemberHchk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextVWANMemberHchk.setStatus("current")


class _FextVWANMemberHchkFailThreshold_Type(Integer32):
    """Custom type fextVWANMemberHchkFailThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FextVWANMemberHchkFailThreshold_Type.__name__ = "Integer32"
_FextVWANMemberHchkFailThreshold_Object = MibTableColumn
fextVWANMemberHchkFailThreshold = _FextVWANMemberHchkFailThreshold_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 6, 1, 10),
    _FextVWANMemberHchkFailThreshold_Type()
)
fextVWANMemberHchkFailThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextVWANMemberHchkFailThreshold.setStatus("current")


class _FextVWANMemberHchkSuccessThreshold_Type(Integer32):
    """Custom type fextVWANMemberHchkSuccessThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FextVWANMemberHchkSuccessThreshold_Type.__name__ = "Integer32"
_FextVWANMemberHchkSuccessThreshold_Object = MibTableColumn
fextVWANMemberHchkSuccessThreshold = _FextVWANMemberHchkSuccessThreshold_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 6, 1, 11),
    _FextVWANMemberHchkSuccessThreshold_Type()
)
fextVWANMemberHchkSuccessThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextVWANMemberHchkSuccessThreshold.setStatus("current")
_FextVWANHchk_Object = MibTable
fextVWANHchk = _FextVWANHchk_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 7)
)
if mibBuilder.loadTexts:
    fextVWANHchk.setStatus("obsolete")
_FextVWANHchkEntry_Object = MibTableRow
fextVWANHchkEntry = _FextVWANHchkEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 7, 1)
)
fextVWANHchkEntry.setIndexNames(
    (0, "FORTINET-FORTIEXTENDER-MIB", "fextVWANHchkIndex"),
)
if mibBuilder.loadTexts:
    fextVWANHchkEntry.setStatus("current")
_FextVWANHchkIndex_Type = FnIndex
_FextVWANHchkIndex_Object = MibTableColumn
fextVWANHchkIndex = _FextVWANHchkIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 7, 1, 1),
    _FextVWANHchkIndex_Type()
)
fextVWANHchkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fextVWANHchkIndex.setStatus("current")
_FextVWANHchkName_Type = DisplayString
_FextVWANHchkName_Object = MibTableColumn
fextVWANHchkName = _FextVWANHchkName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 7, 1, 2),
    _FextVWANHchkName_Type()
)
fextVWANHchkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextVWANHchkName.setStatus("current")
_FextVWANHchkProtocol_Type = DisplayString
_FextVWANHchkProtocol_Object = MibTableColumn
fextVWANHchkProtocol = _FextVWANHchkProtocol_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 7, 1, 3),
    _FextVWANHchkProtocol_Type()
)
fextVWANHchkProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextVWANHchkProtocol.setStatus("current")


class _FextVWANHchkInterval_Type(Integer32):
    """Custom type fextVWANHchkInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_FextVWANHchkInterval_Type.__name__ = "Integer32"
_FextVWANHchkInterval_Object = MibTableColumn
fextVWANHchkInterval = _FextVWANHchkInterval_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 7, 1, 4),
    _FextVWANHchkInterval_Type()
)
fextVWANHchkInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextVWANHchkInterval.setStatus("current")


class _FextVWANHchkProbeCount_Type(Integer32):
    """Custom type fextVWANHchkProbeCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FextVWANHchkProbeCount_Type.__name__ = "Integer32"
_FextVWANHchkProbeCount_Object = MibTableColumn
fextVWANHchkProbeCount = _FextVWANHchkProbeCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 7, 1, 5),
    _FextVWANHchkProbeCount_Type()
)
fextVWANHchkProbeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextVWANHchkProbeCount.setStatus("current")


class _FextVWANHchkProbeTimeout_Type(Integer32):
    """Custom type fextVWANHchkProbeTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FextVWANHchkProbeTimeout_Type.__name__ = "Integer32"
_FextVWANHchkProbeTimeout_Object = MibTableColumn
fextVWANHchkProbeTimeout = _FextVWANHchkProbeTimeout_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 7, 1, 6),
    _FextVWANHchkProbeTimeout_Type()
)
fextVWANHchkProbeTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextVWANHchkProbeTimeout.setStatus("current")
_FextVWANHchkProbeTarget_Type = DisplayString
_FextVWANHchkProbeTarget_Object = MibTableColumn
fextVWANHchkProbeTarget = _FextVWANHchkProbeTarget_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 7, 1, 7),
    _FextVWANHchkProbeTarget_Type()
)
fextVWANHchkProbeTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextVWANHchkProbeTarget.setStatus("current")


class _FextVWANHchkPort_Type(Integer32):
    """Custom type fextVWANHchkPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FextVWANHchkPort_Type.__name__ = "Integer32"
_FextVWANHchkPort_Object = MibTableColumn
fextVWANHchkPort = _FextVWANHchkPort_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 7, 1, 8),
    _FextVWANHchkPort_Type()
)
fextVWANHchkPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextVWANHchkPort.setStatus("current")
_FextVWANHchkHTTPGet_Type = DisplayString
_FextVWANHchkHTTPGet_Object = MibTableColumn
fextVWANHchkHTTPGet = _FextVWANHchkHTTPGet_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 7, 1, 9),
    _FextVWANHchkHTTPGet_Type()
)
fextVWANHchkHTTPGet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextVWANHchkHTTPGet.setStatus("current")
_FextVWANHchkSourceInterface_Type = DisplayString
_FextVWANHchkSourceInterface_Object = MibTableColumn
fextVWANHchkSourceInterface = _FextVWANHchkSourceInterface_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 7, 1, 10),
    _FextVWANHchkSourceInterface_Type()
)
fextVWANHchkSourceInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextVWANHchkSourceInterface.setStatus("current")


class _FextVWANHchkFailCount_Type(Integer32):
    """Custom type fextVWANHchkFailCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FextVWANHchkFailCount_Type.__name__ = "Integer32"
_FextVWANHchkFailCount_Object = MibTableColumn
fextVWANHchkFailCount = _FextVWANHchkFailCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 7, 1, 11),
    _FextVWANHchkFailCount_Type()
)
fextVWANHchkFailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextVWANHchkFailCount.setStatus("current")


class _FextVWANHchkRecoveryCount_Type(Integer32):
    """Custom type fextVWANHchkRecoveryCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FextVWANHchkRecoveryCount_Type.__name__ = "Integer32"
_FextVWANHchkRecoveryCount_Object = MibTableColumn
fextVWANHchkRecoveryCount = _FextVWANHchkRecoveryCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 7, 1, 12),
    _FextVWANHchkRecoveryCount_Type()
)
fextVWANHchkRecoveryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextVWANHchkRecoveryCount.setStatus("current")
_FextSMSNotification_ObjectIdentity = ObjectIdentity
fextSMSNotification = _FextSMSNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 8)
)
if mibBuilder.loadTexts:
    fextSMSNotification.setStatus("current")
_FextSMSNotify_Type = DisplayString
_FextSMSNotify_Object = MibScalar
fextSMSNotify = _FextSMSNotify_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 8, 1),
    _FextSMSNotify_Type()
)
fextSMSNotify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextSMSNotify.setStatus("current")
_FextSMSReceiver_Object = MibTable
fextSMSReceiver = _FextSMSReceiver_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 8, 2)
)
if mibBuilder.loadTexts:
    fextSMSReceiver.setStatus("current")
_FextSMSReceiverEntry_Object = MibTableRow
fextSMSReceiverEntry = _FextSMSReceiverEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 8, 2, 1)
)
fextSMSReceiverEntry.setIndexNames(
    (0, "FORTINET-FORTIEXTENDER-MIB", "fextSMSReceiverIndex"),
)
if mibBuilder.loadTexts:
    fextSMSReceiverEntry.setStatus("current")
_FextSMSReceiverIndex_Type = FnIndex
_FextSMSReceiverIndex_Object = MibTableColumn
fextSMSReceiverIndex = _FextSMSReceiverIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 8, 2, 1, 1),
    _FextSMSReceiverIndex_Type()
)
fextSMSReceiverIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fextSMSReceiverIndex.setStatus("current")
_FextSMSReceiverName_Type = DisplayString
_FextSMSReceiverName_Object = MibTableColumn
fextSMSReceiverName = _FextSMSReceiverName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 8, 2, 1, 2),
    _FextSMSReceiverName_Type()
)
fextSMSReceiverName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextSMSReceiverName.setStatus("current")
_FextSMSReceiverRcvr_Type = DisplayString
_FextSMSReceiverRcvr_Object = MibTableColumn
fextSMSReceiverRcvr = _FextSMSReceiverRcvr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 8, 2, 1, 3),
    _FextSMSReceiverRcvr_Type()
)
fextSMSReceiverRcvr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextSMSReceiverRcvr.setStatus("current")
_FextSMSReceiverNumber_Type = DisplayString
_FextSMSReceiverNumber_Object = MibTableColumn
fextSMSReceiverNumber = _FextSMSReceiverNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 8, 2, 1, 4),
    _FextSMSReceiverNumber_Type()
)
fextSMSReceiverNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextSMSReceiverNumber.setStatus("current")
_FextSMSReceiverAlert_Type = DisplayString
_FextSMSReceiverAlert_Object = MibTableColumn
fextSMSReceiverAlert = _FextSMSReceiverAlert_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 8, 2, 1, 5),
    _FextSMSReceiverAlert_Type()
)
fextSMSReceiverAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextSMSReceiverAlert.setStatus("current")
_FextSMSAlert_ObjectIdentity = ObjectIdentity
fextSMSAlert = _FextSMSAlert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 8, 3)
)
if mibBuilder.loadTexts:
    fextSMSAlert.setStatus("current")
_FextSMSAlertSystemReboot_Type = DisplayString
_FextSMSAlertSystemReboot_Object = MibScalar
fextSMSAlertSystemReboot = _FextSMSAlertSystemReboot_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 8, 3, 1),
    _FextSMSAlertSystemReboot_Type()
)
fextSMSAlertSystemReboot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextSMSAlertSystemReboot.setStatus("current")
_FextSMSAlertLTEDataExhaust_Type = DisplayString
_FextSMSAlertLTEDataExhaust_Object = MibScalar
fextSMSAlertLTEDataExhaust = _FextSMSAlertLTEDataExhaust_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 8, 3, 2),
    _FextSMSAlertLTEDataExhaust_Type()
)
fextSMSAlertLTEDataExhaust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextSMSAlertLTEDataExhaust.setStatus("current")
_FextSMSAlertLTEDisconnect_Type = DisplayString
_FextSMSAlertLTEDisconnect_Object = MibScalar
fextSMSAlertLTEDisconnect = _FextSMSAlertLTEDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 8, 3, 3),
    _FextSMSAlertLTEDisconnect_Type()
)
fextSMSAlertLTEDisconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextSMSAlertLTEDisconnect.setStatus("current")
_FextSMSAlertLTEWeakSignal_Type = DisplayString
_FextSMSAlertLTEWeakSignal_Object = MibScalar
fextSMSAlertLTEWeakSignal = _FextSMSAlertLTEWeakSignal_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 8, 3, 4),
    _FextSMSAlertLTEWeakSignal_Type()
)
fextSMSAlertLTEWeakSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextSMSAlertLTEWeakSignal.setStatus("current")
_FextSMSAlertOSFallback_Type = DisplayString
_FextSMSAlertOSFallback_Object = MibScalar
fextSMSAlertOSFallback = _FextSMSAlertOSFallback_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 8, 3, 5),
    _FextSMSAlertOSFallback_Type()
)
fextSMSAlertOSFallback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextSMSAlertOSFallback.setStatus("current")
_FextSMSAlertNetworkMode_Type = DisplayString
_FextSMSAlertNetworkMode_Object = MibScalar
fextSMSAlertNetworkMode = _FextSMSAlertNetworkMode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 8, 3, 6),
    _FextSMSAlertNetworkMode_Type()
)
fextSMSAlertNetworkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextSMSAlertNetworkMode.setStatus("current")
_FextSMSAlertBackupMode_Type = DisplayString
_FextSMSAlertBackupMode_Object = MibScalar
fextSMSAlertBackupMode = _FextSMSAlertBackupMode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 8, 3, 7),
    _FextSMSAlertBackupMode_Type()
)
fextSMSAlertBackupMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextSMSAlertBackupMode.setStatus("current")
_FextSMSRemoteDiag_ObjectIdentity = ObjectIdentity
fextSMSRemoteDiag = _FextSMSRemoteDiag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 9)
)
if mibBuilder.loadTexts:
    fextSMSRemoteDiag.setStatus("current")
_FextSMSDiag_Type = DisplayString
_FextSMSDiag_Object = MibScalar
fextSMSDiag = _FextSMSDiag_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 9, 1),
    _FextSMSDiag_Type()
)
fextSMSDiag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextSMSDiag.setStatus("current")
_FextSMSUser_Object = MibTable
fextSMSUser = _FextSMSUser_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 9, 2)
)
if mibBuilder.loadTexts:
    fextSMSUser.setStatus("current")
_FextSMSUserEntry_Object = MibTableRow
fextSMSUserEntry = _FextSMSUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 9, 2, 1)
)
fextSMSUserEntry.setIndexNames(
    (0, "FORTINET-FORTIEXTENDER-MIB", "fextSMSUserIndex"),
)
if mibBuilder.loadTexts:
    fextSMSUserEntry.setStatus("current")
_FextSMSUserIndex_Type = FnIndex
_FextSMSUserIndex_Object = MibTableColumn
fextSMSUserIndex = _FextSMSUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 9, 2, 1, 1),
    _FextSMSUserIndex_Type()
)
fextSMSUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fextSMSUserIndex.setStatus("current")
_FextSMSUserName_Type = DisplayString
_FextSMSUserName_Object = MibTableColumn
fextSMSUserName = _FextSMSUserName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 9, 2, 1, 2),
    _FextSMSUserName_Type()
)
fextSMSUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextSMSUserName.setStatus("current")
_FextSMSUserSender_Type = DisplayString
_FextSMSUserSender_Object = MibTableColumn
fextSMSUserSender = _FextSMSUserSender_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 9, 2, 1, 3),
    _FextSMSUserSender_Type()
)
fextSMSUserSender.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextSMSUserSender.setStatus("current")
_FextSMSUserNumber_Type = DisplayString
_FextSMSUserNumber_Object = MibTableColumn
fextSMSUserNumber = _FextSMSUserNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 9, 2, 1, 4),
    _FextSMSUserNumber_Type()
)
fextSMSUserNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextSMSUserNumber.setStatus("current")
_FextSMSUserCommand_Type = DisplayString
_FextSMSUserCommand_Object = MibTableColumn
fextSMSUserCommand = _FextSMSUserCommand_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 9, 2, 1, 5),
    _FextSMSUserCommand_Type()
)
fextSMSUserCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextSMSUserCommand.setStatus("current")
_FextSysLog_ObjectIdentity = ObjectIdentity
fextSysLog = _FextSysLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 10)
)
if mibBuilder.loadTexts:
    fextSysLog.setStatus("current")
_FextSysLogRemoteIP_Type = DisplayString
_FextSysLogRemoteIP_Object = MibScalar
fextSysLogRemoteIP = _FextSysLogRemoteIP_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 10, 1),
    _FextSysLogRemoteIP_Type()
)
fextSysLogRemoteIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextSysLogRemoteIP.setStatus("current")


class _FextSysLogRemotePort_Type(Integer32):
    """Custom type fextSysLogRemotePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FextSysLogRemotePort_Type.__name__ = "Integer32"
_FextSysLogRemotePort_Object = MibScalar
fextSysLogRemotePort = _FextSysLogRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 10, 2),
    _FextSysLogRemotePort_Type()
)
fextSysLogRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextSysLogRemotePort.setStatus("current")
_FextSysLogStatReport_ObjectIdentity = ObjectIdentity
fextSysLogStatReport = _FextSysLogStatReport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 10, 3)
)
if mibBuilder.loadTexts:
    fextSysLogStatReport.setStatus("current")
_FextSysLogStatRptStatus_Type = DisplayString
_FextSysLogStatRptStatus_Object = MibScalar
fextSysLogStatRptStatus = _FextSysLogStatRptStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 10, 3, 1),
    _FextSysLogStatRptStatus_Type()
)
fextSysLogStatRptStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextSysLogStatRptStatus.setStatus("current")


class _FextSysLogStatRptItv_Type(Integer32):
    """Custom type fextSysLogStatRptItv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_FextSysLogStatRptItv_Type.__name__ = "Integer32"
_FextSysLogStatRptItv_Object = MibScalar
fextSysLogStatRptItv = _FextSysLogStatRptItv_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 10, 3, 2),
    _FextSysLogStatRptItv_Type()
)
fextSysLogStatRptItv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextSysLogStatRptItv.setStatus("current")
_FextSysLogStatRptCPUUsage_ObjectIdentity = ObjectIdentity
fextSysLogStatRptCPUUsage = _FextSysLogStatRptCPUUsage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 10, 3, 3)
)
if mibBuilder.loadTexts:
    fextSysLogStatRptCPUUsage.setStatus("current")


class _FextSysLogStatRptCPUUsageThrsd_Type(Integer32):
    """Custom type fextSysLogStatRptCPUUsageThrsd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FextSysLogStatRptCPUUsageThrsd_Type.__name__ = "Integer32"
_FextSysLogStatRptCPUUsageThrsd_Object = MibScalar
fextSysLogStatRptCPUUsageThrsd = _FextSysLogStatRptCPUUsageThrsd_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 10, 3, 3, 1),
    _FextSysLogStatRptCPUUsageThrsd_Type()
)
fextSysLogStatRptCPUUsageThrsd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextSysLogStatRptCPUUsageThrsd.setStatus("current")


class _FextSysLogStatRptCPUUsageVariance_Type(Integer32):
    """Custom type fextSysLogStatRptCPUUsageVariance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FextSysLogStatRptCPUUsageVariance_Type.__name__ = "Integer32"
_FextSysLogStatRptCPUUsageVariance_Object = MibScalar
fextSysLogStatRptCPUUsageVariance = _FextSysLogStatRptCPUUsageVariance_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 10, 3, 3, 2),
    _FextSysLogStatRptCPUUsageVariance_Type()
)
fextSysLogStatRptCPUUsageVariance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextSysLogStatRptCPUUsageVariance.setStatus("current")
_FextSysLogStatRptMemUsage_ObjectIdentity = ObjectIdentity
fextSysLogStatRptMemUsage = _FextSysLogStatRptMemUsage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 10, 3, 4)
)
if mibBuilder.loadTexts:
    fextSysLogStatRptMemUsage.setStatus("current")


class _FextSysLogStatRptMemUsageThrsd_Type(Integer32):
    """Custom type fextSysLogStatRptMemUsageThrsd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FextSysLogStatRptMemUsageThrsd_Type.__name__ = "Integer32"
_FextSysLogStatRptMemUsageThrsd_Object = MibScalar
fextSysLogStatRptMemUsageThrsd = _FextSysLogStatRptMemUsageThrsd_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 10, 3, 4, 1),
    _FextSysLogStatRptMemUsageThrsd_Type()
)
fextSysLogStatRptMemUsageThrsd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextSysLogStatRptMemUsageThrsd.setStatus("current")


class _FextSysLogStatRptMemUsageVariance_Type(Integer32):
    """Custom type fextSysLogStatRptMemUsageVariance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FextSysLogStatRptMemUsageVariance_Type.__name__ = "Integer32"
_FextSysLogStatRptMemUsageVariance_Object = MibScalar
fextSysLogStatRptMemUsageVariance = _FextSysLogStatRptMemUsageVariance_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 10, 3, 4, 2),
    _FextSysLogStatRptMemUsageVariance_Type()
)
fextSysLogStatRptMemUsageVariance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextSysLogStatRptMemUsageVariance.setStatus("current")
_FextSysLogStatRptCPUTemp_ObjectIdentity = ObjectIdentity
fextSysLogStatRptCPUTemp = _FextSysLogStatRptCPUTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 10, 3, 5)
)
if mibBuilder.loadTexts:
    fextSysLogStatRptCPUTemp.setStatus("current")


class _FextSysLogStatRptCPUTempThrsd_Type(Integer32):
    """Custom type fextSysLogStatRptCPUTempThrsd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_FextSysLogStatRptCPUTempThrsd_Type.__name__ = "Integer32"
_FextSysLogStatRptCPUTempThrsd_Object = MibScalar
fextSysLogStatRptCPUTempThrsd = _FextSysLogStatRptCPUTempThrsd_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 10, 3, 5, 1),
    _FextSysLogStatRptCPUTempThrsd_Type()
)
fextSysLogStatRptCPUTempThrsd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextSysLogStatRptCPUTempThrsd.setStatus("current")


class _FextSysLogStatRptCPUTempVariance_Type(Integer32):
    """Custom type fextSysLogStatRptCPUTempVariance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_FextSysLogStatRptCPUTempVariance_Type.__name__ = "Integer32"
_FextSysLogStatRptCPUTempVariance_Object = MibScalar
fextSysLogStatRptCPUTempVariance = _FextSysLogStatRptCPUTempVariance_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 10, 3, 5, 2),
    _FextSysLogStatRptCPUTempVariance_Type()
)
fextSysLogStatRptCPUTempVariance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextSysLogStatRptCPUTempVariance.setStatus("current")
_FextLANSwitch_ObjectIdentity = ObjectIdentity
fextLANSwitch = _FextLANSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 11)
)
if mibBuilder.loadTexts:
    fextLANSwitch.setStatus("current")
_FextLANSwitchPort_Object = MibTable
fextLANSwitchPort = _FextLANSwitchPort_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 11, 1)
)
if mibBuilder.loadTexts:
    fextLANSwitchPort.setStatus("current")
_FextLANSwitchPortEntry_Object = MibTableRow
fextLANSwitchPortEntry = _FextLANSwitchPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 11, 1, 1)
)
fextLANSwitchPortEntry.setIndexNames(
    (0, "FORTINET-FORTIEXTENDER-MIB", "fextLANSwitchPortIndex"),
)
if mibBuilder.loadTexts:
    fextLANSwitchPortEntry.setStatus("current")
_FextLANSwitchPortIndex_Type = FnIndex
_FextLANSwitchPortIndex_Object = MibTableColumn
fextLANSwitchPortIndex = _FextLANSwitchPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 11, 1, 1, 1),
    _FextLANSwitchPortIndex_Type()
)
fextLANSwitchPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fextLANSwitchPortIndex.setStatus("current")
_FextLANSwitchPortName_Type = DisplayString
_FextLANSwitchPortName_Object = MibTableColumn
fextLANSwitchPortName = _FextLANSwitchPortName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 11, 1, 1, 2),
    _FextLANSwitchPortName_Type()
)
fextLANSwitchPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextLANSwitchPortName.setStatus("current")
_FextVirtualWirePair_ObjectIdentity = ObjectIdentity
fextVirtualWirePair = _FextVirtualWirePair_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 12)
)
if mibBuilder.loadTexts:
    fextVirtualWirePair.setStatus("current")
_FextLTE1Mapping_Type = DisplayString
_FextLTE1Mapping_Object = MibScalar
fextLTE1Mapping = _FextLTE1Mapping_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 12, 1),
    _FextLTE1Mapping_Type()
)
fextLTE1Mapping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextLTE1Mapping.setStatus("current")
_FextLTE2Mapping_Type = DisplayString
_FextLTE2Mapping_Object = MibScalar
fextLTE2Mapping = _FextLTE2Mapping_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 2, 12, 2),
    _FextLTE2Mapping_Type()
)
fextLTE2Mapping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextLTE2Mapping.setStatus("current")
_FextLTE_ObjectIdentity = ObjectIdentity
fextLTE = _FextLTE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3)
)
_FextLTESetting_ObjectIdentity = ObjectIdentity
fextLTESetting = _FextLTESetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 1)
)
if mibBuilder.loadTexts:
    fextLTESetting.setStatus("current")
_FextLTEReport_ObjectIdentity = ObjectIdentity
fextLTEReport = _FextLTEReport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 1, 1)
)
if mibBuilder.loadTexts:
    fextLTEReport.setStatus("current")
_FextLTEReportStatus_Type = DisplayString
_FextLTEReportStatus_Object = MibScalar
fextLTEReportStatus = _FextLTEReportStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 1, 1, 1),
    _FextLTEReportStatus_Type()
)
fextLTEReportStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextLTEReportStatus.setStatus("current")
_FextLTEReportInterval_Type = DisplayString
_FextLTEReportInterval_Object = MibScalar
fextLTEReportInterval = _FextLTEReportInterval_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 1, 1, 2),
    _FextLTEReportInterval_Type()
)
fextLTEReportInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextLTEReportInterval.setStatus("current")
_FextLTEReportSignalThreshold_Type = DisplayString
_FextLTEReportSignalThreshold_Object = MibScalar
fextLTEReportSignalThreshold = _FextLTEReportSignalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 1, 1, 3),
    _FextLTEReportSignalThreshold_Type()
)
fextLTEReportSignalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextLTEReportSignalThreshold.setStatus("current")
_FextLTEModem1_ObjectIdentity = ObjectIdentity
fextLTEModem1 = _FextLTEModem1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 1, 2)
)
if mibBuilder.loadTexts:
    fextLTEModem1.setStatus("current")
_FextModem1CertMode_Type = DisplayString
_FextModem1CertMode_Object = MibScalar
fextModem1CertMode = _FextModem1CertMode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 1, 2, 1),
    _FextModem1CertMode_Type()
)
fextModem1CertMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextModem1CertMode.setStatus("current")
_FextModem1DefaultSIM_Type = DisplayString
_FextModem1DefaultSIM_Object = MibScalar
fextModem1DefaultSIM = _FextModem1DefaultSIM_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 1, 2, 2),
    _FextModem1DefaultSIM_Type()
)
fextModem1DefaultSIM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextModem1DefaultSIM.setStatus("current")
_FextModem1PreferredCarrier_Type = DisplayString
_FextModem1PreferredCarrier_Object = MibScalar
fextModem1PreferredCarrier = _FextModem1PreferredCarrier_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 1, 2, 3),
    _FextModem1PreferredCarrier_Type()
)
fextModem1PreferredCarrier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextModem1PreferredCarrier.setStatus("current")
_FextModem1GPS_Type = DisplayString
_FextModem1GPS_Object = MibScalar
fextModem1GPS = _FextModem1GPS_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 1, 2, 4),
    _FextModem1GPS_Type()
)
fextModem1GPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextModem1GPS.setStatus("current")
_FextModem1SIM1Pin_Type = DisplayString
_FextModem1SIM1Pin_Object = MibScalar
fextModem1SIM1Pin = _FextModem1SIM1Pin_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 1, 2, 5),
    _FextModem1SIM1Pin_Type()
)
fextModem1SIM1Pin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextModem1SIM1Pin.setStatus("current")
_FextModem1SIM1PinCode_Type = DisplayString
_FextModem1SIM1PinCode_Object = MibScalar
fextModem1SIM1PinCode = _FextModem1SIM1PinCode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 1, 2, 6),
    _FextModem1SIM1PinCode_Type()
)
fextModem1SIM1PinCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextModem1SIM1PinCode.setStatus("current")
_FextModem1SIM2Pin_Type = DisplayString
_FextModem1SIM2Pin_Object = MibScalar
fextModem1SIM2Pin = _FextModem1SIM2Pin_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 1, 2, 7),
    _FextModem1SIM2Pin_Type()
)
fextModem1SIM2Pin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextModem1SIM2Pin.setStatus("current")
_FextModem1SIM2PinCode_Type = DisplayString
_FextModem1SIM2PinCode_Object = MibScalar
fextModem1SIM2PinCode = _FextModem1SIM2PinCode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 1, 2, 8),
    _FextModem1SIM2PinCode_Type()
)
fextModem1SIM2PinCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextModem1SIM2PinCode.setStatus("current")
_FextModem1AutoSwitch_ObjectIdentity = ObjectIdentity
fextModem1AutoSwitch = _FextModem1AutoSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 1, 2, 9)
)
if mibBuilder.loadTexts:
    fextModem1AutoSwitch.setStatus("current")
_FextModem1SwitchByDisconnect_Type = DisplayString
_FextModem1SwitchByDisconnect_Object = MibScalar
fextModem1SwitchByDisconnect = _FextModem1SwitchByDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 1, 2, 9, 1),
    _FextModem1SwitchByDisconnect_Type()
)
fextModem1SwitchByDisconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextModem1SwitchByDisconnect.setStatus("current")
_FextModem1SwitchBySignal_Type = DisplayString
_FextModem1SwitchBySignal_Object = MibScalar
fextModem1SwitchBySignal = _FextModem1SwitchBySignal_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 1, 2, 9, 2),
    _FextModem1SwitchBySignal_Type()
)
fextModem1SwitchBySignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextModem1SwitchBySignal.setStatus("current")
_FextModem1SwitchByPlan_Type = DisplayString
_FextModem1SwitchByPlan_Object = MibScalar
fextModem1SwitchByPlan = _FextModem1SwitchByPlan_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 1, 2, 9, 3),
    _FextModem1SwitchByPlan_Type()
)
fextModem1SwitchByPlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextModem1SwitchByPlan.setStatus("current")
_FextModem1SwitchDisconnectThreshold_Type = DisplayString
_FextModem1SwitchDisconnectThreshold_Object = MibScalar
fextModem1SwitchDisconnectThreshold = _FextModem1SwitchDisconnectThreshold_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 1, 2, 9, 4),
    _FextModem1SwitchDisconnectThreshold_Type()
)
fextModem1SwitchDisconnectThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextModem1SwitchDisconnectThreshold.setStatus("current")
_FextModem1SwitchDisconnectPeriod_Type = DisplayString
_FextModem1SwitchDisconnectPeriod_Object = MibScalar
fextModem1SwitchDisconnectPeriod = _FextModem1SwitchDisconnectPeriod_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 1, 2, 9, 5),
    _FextModem1SwitchDisconnectPeriod_Type()
)
fextModem1SwitchDisconnectPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextModem1SwitchDisconnectPeriod.setStatus("current")
_FextModem1SwitchBack_Type = DisplayString
_FextModem1SwitchBack_Object = MibScalar
fextModem1SwitchBack = _FextModem1SwitchBack_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 1, 2, 9, 6),
    _FextModem1SwitchBack_Type()
)
fextModem1SwitchBack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextModem1SwitchBack.setStatus("current")
_FextModem1SwitchBackTime_Type = DisplayString
_FextModem1SwitchBackTime_Object = MibScalar
fextModem1SwitchBackTime = _FextModem1SwitchBackTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 1, 2, 9, 7),
    _FextModem1SwitchBackTime_Type()
)
fextModem1SwitchBackTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextModem1SwitchBackTime.setStatus("current")
_FextModem1SwitchBackTimer_Type = DisplayString
_FextModem1SwitchBackTimer_Object = MibScalar
fextModem1SwitchBackTimer = _FextModem1SwitchBackTimer_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 1, 2, 9, 8),
    _FextModem1SwitchBackTimer_Type()
)
fextModem1SwitchBackTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextModem1SwitchBackTimer.setStatus("current")
_FextLTEModem2_ObjectIdentity = ObjectIdentity
fextLTEModem2 = _FextLTEModem2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 1, 3)
)
if mibBuilder.loadTexts:
    fextLTEModem2.setStatus("current")
_FextModem2CertMode_Type = DisplayString
_FextModem2CertMode_Object = MibScalar
fextModem2CertMode = _FextModem2CertMode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 1, 3, 1),
    _FextModem2CertMode_Type()
)
fextModem2CertMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextModem2CertMode.setStatus("current")
_FextModem2DefaultSIM_Type = DisplayString
_FextModem2DefaultSIM_Object = MibScalar
fextModem2DefaultSIM = _FextModem2DefaultSIM_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 1, 3, 2),
    _FextModem2DefaultSIM_Type()
)
fextModem2DefaultSIM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextModem2DefaultSIM.setStatus("current")
_FextModem2PreferredCarrier_Type = DisplayString
_FextModem2PreferredCarrier_Object = MibScalar
fextModem2PreferredCarrier = _FextModem2PreferredCarrier_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 1, 3, 3),
    _FextModem2PreferredCarrier_Type()
)
fextModem2PreferredCarrier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextModem2PreferredCarrier.setStatus("current")
_FextModem2GPS_Type = DisplayString
_FextModem2GPS_Object = MibScalar
fextModem2GPS = _FextModem2GPS_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 1, 3, 4),
    _FextModem2GPS_Type()
)
fextModem2GPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextModem2GPS.setStatus("current")
_FextModem2SIM1Pin_Type = DisplayString
_FextModem2SIM1Pin_Object = MibScalar
fextModem2SIM1Pin = _FextModem2SIM1Pin_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 1, 3, 5),
    _FextModem2SIM1Pin_Type()
)
fextModem2SIM1Pin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextModem2SIM1Pin.setStatus("current")
_FextModem2SIM1PinCode_Type = DisplayString
_FextModem2SIM1PinCode_Object = MibScalar
fextModem2SIM1PinCode = _FextModem2SIM1PinCode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 1, 3, 6),
    _FextModem2SIM1PinCode_Type()
)
fextModem2SIM1PinCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextModem2SIM1PinCode.setStatus("current")
_FextModem2SIM2Pin_Type = DisplayString
_FextModem2SIM2Pin_Object = MibScalar
fextModem2SIM2Pin = _FextModem2SIM2Pin_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 1, 3, 7),
    _FextModem2SIM2Pin_Type()
)
fextModem2SIM2Pin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextModem2SIM2Pin.setStatus("current")
_FextModem2SIM2PinCode_Type = DisplayString
_FextModem2SIM2PinCode_Object = MibScalar
fextModem2SIM2PinCode = _FextModem2SIM2PinCode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 1, 3, 8),
    _FextModem2SIM2PinCode_Type()
)
fextModem2SIM2PinCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextModem2SIM2PinCode.setStatus("current")
_FextModem2AutoSwitch_ObjectIdentity = ObjectIdentity
fextModem2AutoSwitch = _FextModem2AutoSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 1, 3, 9)
)
if mibBuilder.loadTexts:
    fextModem2AutoSwitch.setStatus("current")
_FextModem2SwitchByDisconnect_Type = DisplayString
_FextModem2SwitchByDisconnect_Object = MibScalar
fextModem2SwitchByDisconnect = _FextModem2SwitchByDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 1, 3, 9, 1),
    _FextModem2SwitchByDisconnect_Type()
)
fextModem2SwitchByDisconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextModem2SwitchByDisconnect.setStatus("current")
_FextModem2SwitchBySignal_Type = DisplayString
_FextModem2SwitchBySignal_Object = MibScalar
fextModem2SwitchBySignal = _FextModem2SwitchBySignal_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 1, 3, 9, 2),
    _FextModem2SwitchBySignal_Type()
)
fextModem2SwitchBySignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextModem2SwitchBySignal.setStatus("current")
_FextModem2SwitchByPlan_Type = DisplayString
_FextModem2SwitchByPlan_Object = MibScalar
fextModem2SwitchByPlan = _FextModem2SwitchByPlan_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 1, 3, 9, 3),
    _FextModem2SwitchByPlan_Type()
)
fextModem2SwitchByPlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextModem2SwitchByPlan.setStatus("current")
_FextModem2SwitchDisconnectThreshold_Type = DisplayString
_FextModem2SwitchDisconnectThreshold_Object = MibScalar
fextModem2SwitchDisconnectThreshold = _FextModem2SwitchDisconnectThreshold_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 1, 3, 9, 4),
    _FextModem2SwitchDisconnectThreshold_Type()
)
fextModem2SwitchDisconnectThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextModem2SwitchDisconnectThreshold.setStatus("current")
_FextModem2SwitchDisconnectPeriod_Type = DisplayString
_FextModem2SwitchDisconnectPeriod_Object = MibScalar
fextModem2SwitchDisconnectPeriod = _FextModem2SwitchDisconnectPeriod_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 1, 3, 9, 5),
    _FextModem2SwitchDisconnectPeriod_Type()
)
fextModem2SwitchDisconnectPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextModem2SwitchDisconnectPeriod.setStatus("current")
_FextModem2SwitchBack_Type = DisplayString
_FextModem2SwitchBack_Object = MibScalar
fextModem2SwitchBack = _FextModem2SwitchBack_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 1, 3, 9, 6),
    _FextModem2SwitchBack_Type()
)
fextModem2SwitchBack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextModem2SwitchBack.setStatus("current")
_FextModem2SwitchBackByTime_Type = DisplayString
_FextModem2SwitchBackByTime_Object = MibScalar
fextModem2SwitchBackByTime = _FextModem2SwitchBackByTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 1, 3, 9, 7),
    _FextModem2SwitchBackByTime_Type()
)
fextModem2SwitchBackByTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextModem2SwitchBackByTime.setStatus("current")
_FextModem2SwitchBackByTimer_Type = DisplayString
_FextModem2SwitchBackByTimer_Object = MibScalar
fextModem2SwitchBackByTimer = _FextModem2SwitchBackByTimer_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 1, 3, 9, 8),
    _FextModem2SwitchBackByTimer_Type()
)
fextModem2SwitchBackByTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextModem2SwitchBackByTimer.setStatus("current")
_FextLTECarrier_Object = MibTable
fextLTECarrier = _FextLTECarrier_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 2)
)
if mibBuilder.loadTexts:
    fextLTECarrier.setStatus("current")
_FextLTECarrierEntry_Object = MibTableRow
fextLTECarrierEntry = _FextLTECarrierEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 2, 1)
)
fextLTECarrierEntry.setIndexNames(
    (0, "FORTINET-FORTIEXTENDER-MIB", "fextLTECarrierIndex"),
)
if mibBuilder.loadTexts:
    fextLTECarrierEntry.setStatus("current")
_FextLTECarrierIndex_Type = FnIndex
_FextLTECarrierIndex_Object = MibTableColumn
fextLTECarrierIndex = _FextLTECarrierIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 2, 1, 1),
    _FextLTECarrierIndex_Type()
)
fextLTECarrierIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fextLTECarrierIndex.setStatus("current")
_FextLTECarrierName_Type = DisplayString
_FextLTECarrierName_Object = MibTableColumn
fextLTECarrierName = _FextLTECarrierName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 2, 1, 2),
    _FextLTECarrierName_Type()
)
fextLTECarrierName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextLTECarrierName.setStatus("current")
_FextLTECarrierFirmware_Type = DisplayString
_FextLTECarrierFirmware_Object = MibTableColumn
fextLTECarrierFirmware = _FextLTECarrierFirmware_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 2, 1, 3),
    _FextLTECarrierFirmware_Type()
)
fextLTECarrierFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextLTECarrierFirmware.setStatus("current")
_FextLTECarrierPRI_Type = DisplayString
_FextLTECarrierPRI_Object = MibTableColumn
fextLTECarrierPRI = _FextLTECarrierPRI_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 2, 1, 4),
    _FextLTECarrierPRI_Type()
)
fextLTECarrierPRI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextLTECarrierPRI.setStatus("current")
_FextLTESIMMap_Object = MibTable
fextLTESIMMap = _FextLTESIMMap_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 3)
)
if mibBuilder.loadTexts:
    fextLTESIMMap.setStatus("current")
_FextLTESIMMapEntry_Object = MibTableRow
fextLTESIMMapEntry = _FextLTESIMMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 3, 1)
)
fextLTESIMMapEntry.setIndexNames(
    (0, "FORTINET-FORTIEXTENDER-MIB", "fextLTESIMMapIndex"),
)
if mibBuilder.loadTexts:
    fextLTESIMMapEntry.setStatus("current")
_FextLTESIMMapIndex_Type = FnIndex
_FextLTESIMMapIndex_Object = MibTableColumn
fextLTESIMMapIndex = _FextLTESIMMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 3, 1, 1),
    _FextLTESIMMapIndex_Type()
)
fextLTESIMMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fextLTESIMMapIndex.setStatus("current")
_FextLTESIMMapName_Type = DisplayString
_FextLTESIMMapName_Object = MibTableColumn
fextLTESIMMapName = _FextLTESIMMapName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 3, 1, 2),
    _FextLTESIMMapName_Type()
)
fextLTESIMMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextLTESIMMapName.setStatus("current")
_FextLTESIMMapMCC_Type = DisplayString
_FextLTESIMMapMCC_Object = MibTableColumn
fextLTESIMMapMCC = _FextLTESIMMapMCC_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 3, 1, 3),
    _FextLTESIMMapMCC_Type()
)
fextLTESIMMapMCC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextLTESIMMapMCC.setStatus("current")
_FextLTESIMMapMNC_Type = DisplayString
_FextLTESIMMapMNC_Object = MibTableColumn
fextLTESIMMapMNC = _FextLTESIMMapMNC_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 3, 1, 4),
    _FextLTESIMMapMNC_Type()
)
fextLTESIMMapMNC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextLTESIMMapMNC.setStatus("current")
_FextLTESIMMapCarrier_Type = DisplayString
_FextLTESIMMapCarrier_Object = MibTableColumn
fextLTESIMMapCarrier = _FextLTESIMMapCarrier_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 3, 1, 5),
    _FextLTESIMMapCarrier_Type()
)
fextLTESIMMapCarrier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextLTESIMMapCarrier.setStatus("current")
_FextLTEPlan_Object = MibTable
fextLTEPlan = _FextLTEPlan_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 4)
)
if mibBuilder.loadTexts:
    fextLTEPlan.setStatus("current")
_FextLTEPlanEntry_Object = MibTableRow
fextLTEPlanEntry = _FextLTEPlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 4, 1)
)
fextLTEPlanEntry.setIndexNames(
    (0, "FORTINET-FORTIEXTENDER-MIB", "fextLTEPlanIndex"),
)
if mibBuilder.loadTexts:
    fextLTEPlanEntry.setStatus("current")
_FextLTEPlanIndex_Type = FnIndex
_FextLTEPlanIndex_Object = MibTableColumn
fextLTEPlanIndex = _FextLTEPlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 4, 1, 1),
    _FextLTEPlanIndex_Type()
)
fextLTEPlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fextLTEPlanIndex.setStatus("current")
_FextLTEPlanName_Type = DisplayString
_FextLTEPlanName_Object = MibTableColumn
fextLTEPlanName = _FextLTEPlanName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 4, 1, 2),
    _FextLTEPlanName_Type()
)
fextLTEPlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextLTEPlanName.setStatus("current")
_FextLTEPlanModem_Type = DisplayString
_FextLTEPlanModem_Object = MibTableColumn
fextLTEPlanModem = _FextLTEPlanModem_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 4, 1, 3),
    _FextLTEPlanModem_Type()
)
fextLTEPlanModem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextLTEPlanModem.setStatus("current")
_FextLTEPlanType_Type = DisplayString
_FextLTEPlanType_Object = MibTableColumn
fextLTEPlanType = _FextLTEPlanType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 4, 1, 4),
    _FextLTEPlanType_Type()
)
fextLTEPlanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextLTEPlanType.setStatus("current")
_FextLTEPlanICCID_Type = DisplayString
_FextLTEPlanICCID_Object = MibTableColumn
fextLTEPlanICCID = _FextLTEPlanICCID_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 4, 1, 5),
    _FextLTEPlanICCID_Type()
)
fextLTEPlanICCID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextLTEPlanICCID.setStatus("current")
_FextLTEPlanCarrier_Type = DisplayString
_FextLTEPlanCarrier_Object = MibTableColumn
fextLTEPlanCarrier = _FextLTEPlanCarrier_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 4, 1, 6),
    _FextLTEPlanCarrier_Type()
)
fextLTEPlanCarrier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextLTEPlanCarrier.setStatus("current")
_FextLTEPlanSlot_Type = DisplayString
_FextLTEPlanSlot_Object = MibTableColumn
fextLTEPlanSlot = _FextLTEPlanSlot_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 4, 1, 7),
    _FextLTEPlanSlot_Type()
)
fextLTEPlanSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextLTEPlanSlot.setStatus("current")
_FextLTEPlanAPN_Type = DisplayString
_FextLTEPlanAPN_Object = MibTableColumn
fextLTEPlanAPN = _FextLTEPlanAPN_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 4, 1, 8),
    _FextLTEPlanAPN_Type()
)
fextLTEPlanAPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextLTEPlanAPN.setStatus("current")
_FextLTEPlanAuth_Type = DisplayString
_FextLTEPlanAuth_Object = MibTableColumn
fextLTEPlanAuth = _FextLTEPlanAuth_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 4, 1, 9),
    _FextLTEPlanAuth_Type()
)
fextLTEPlanAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextLTEPlanAuth.setStatus("current")
_FextLTEPlanUser_Type = DisplayString
_FextLTEPlanUser_Object = MibTableColumn
fextLTEPlanUser = _FextLTEPlanUser_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 4, 1, 10),
    _FextLTEPlanUser_Type()
)
fextLTEPlanUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextLTEPlanUser.setStatus("current")
_FextLTEPlanPWD_Type = DisplayString
_FextLTEPlanPWD_Object = MibTableColumn
fextLTEPlanPWD = _FextLTEPlanPWD_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 4, 1, 11),
    _FextLTEPlanPWD_Type()
)
fextLTEPlanPWD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextLTEPlanPWD.setStatus("current")
_FextLTEPlanPDN_Type = DisplayString
_FextLTEPlanPDN_Object = MibTableColumn
fextLTEPlanPDN = _FextLTEPlanPDN_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 4, 1, 12),
    _FextLTEPlanPDN_Type()
)
fextLTEPlanPDN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextLTEPlanPDN.setStatus("current")
_FextLTEPlanSignalThreshold_Type = DisplayString
_FextLTEPlanSignalThreshold_Object = MibTableColumn
fextLTEPlanSignalThreshold = _FextLTEPlanSignalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 4, 1, 13),
    _FextLTEPlanSignalThreshold_Type()
)
fextLTEPlanSignalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextLTEPlanSignalThreshold.setStatus("current")
_FextLTEPlanSignalPeriod_Type = DisplayString
_FextLTEPlanSignalPeriod_Object = MibTableColumn
fextLTEPlanSignalPeriod = _FextLTEPlanSignalPeriod_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 4, 1, 14),
    _FextLTEPlanSignalPeriod_Type()
)
fextLTEPlanSignalPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextLTEPlanSignalPeriod.setStatus("current")
_FextLTEPlanCapacity_Type = DisplayString
_FextLTEPlanCapacity_Object = MibTableColumn
fextLTEPlanCapacity = _FextLTEPlanCapacity_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 4, 1, 15),
    _FextLTEPlanCapacity_Type()
)
fextLTEPlanCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextLTEPlanCapacity.setStatus("current")
_FextLTEPlanMonthlyFee_Type = DisplayString
_FextLTEPlanMonthlyFee_Object = MibTableColumn
fextLTEPlanMonthlyFee = _FextLTEPlanMonthlyFee_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 4, 1, 16),
    _FextLTEPlanMonthlyFee_Type()
)
fextLTEPlanMonthlyFee.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextLTEPlanMonthlyFee.setStatus("current")
_FextLTEPlanBillingDate_Type = DisplayString
_FextLTEPlanBillingDate_Object = MibTableColumn
fextLTEPlanBillingDate = _FextLTEPlanBillingDate_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 4, 1, 17),
    _FextLTEPlanBillingDate_Type()
)
fextLTEPlanBillingDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextLTEPlanBillingDate.setStatus("current")
_FextLTEPlanOverage_Type = DisplayString
_FextLTEPlanOverage_Object = MibTableColumn
fextLTEPlanOverage = _FextLTEPlanOverage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 4, 1, 18),
    _FextLTEPlanOverage_Type()
)
fextLTEPlanOverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextLTEPlanOverage.setStatus("current")
_FextLTEPlanPreferredSubnet_Type = DisplayString
_FextLTEPlanPreferredSubnet_Object = MibTableColumn
fextLTEPlanPreferredSubnet = _FextLTEPlanPreferredSubnet_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 4, 1, 19),
    _FextLTEPlanPreferredSubnet_Type()
)
fextLTEPlanPreferredSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextLTEPlanPreferredSubnet.setStatus("current")
_FextLTEPlanPrivateSubnet_Type = DisplayString
_FextLTEPlanPrivateSubnet_Object = MibTableColumn
fextLTEPlanPrivateSubnet = _FextLTEPlanPrivateSubnet_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 3, 4, 1, 20),
    _FextLTEPlanPrivateSubnet_Type()
)
fextLTEPlanPrivateSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextLTEPlanPrivateSubnet.setStatus("current")
_FextNetwork_ObjectIdentity = ObjectIdentity
fextNetwork = _FextNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 4)
)
_FextNetworkAddress_Object = MibTable
fextNetworkAddress = _FextNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 4, 1)
)
if mibBuilder.loadTexts:
    fextNetworkAddress.setStatus("current")
_FextNetworkAddressEntry_Object = MibTableRow
fextNetworkAddressEntry = _FextNetworkAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 4, 1, 1)
)
fextNetworkAddressEntry.setIndexNames(
    (0, "FORTINET-FORTIEXTENDER-MIB", "fextNetworkAddressIndex"),
)
if mibBuilder.loadTexts:
    fextNetworkAddressEntry.setStatus("current")
_FextNetworkAddressIndex_Type = FnIndex
_FextNetworkAddressIndex_Object = MibTableColumn
fextNetworkAddressIndex = _FextNetworkAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 4, 1, 1, 1),
    _FextNetworkAddressIndex_Type()
)
fextNetworkAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fextNetworkAddressIndex.setStatus("current")
_FextNetworkAddressName_Type = DisplayString
_FextNetworkAddressName_Object = MibTableColumn
fextNetworkAddressName = _FextNetworkAddressName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 4, 1, 1, 2),
    _FextNetworkAddressName_Type()
)
fextNetworkAddressName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextNetworkAddressName.setStatus("current")
_FextNetworkAddressType_Type = DisplayString
_FextNetworkAddressType_Object = MibTableColumn
fextNetworkAddressType = _FextNetworkAddressType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 4, 1, 1, 3),
    _FextNetworkAddressType_Type()
)
fextNetworkAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextNetworkAddressType.setStatus("current")
_FextNetworkAddressSubnet_Type = DisplayString
_FextNetworkAddressSubnet_Object = MibTableColumn
fextNetworkAddressSubnet = _FextNetworkAddressSubnet_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 4, 1, 1, 4),
    _FextNetworkAddressSubnet_Type()
)
fextNetworkAddressSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextNetworkAddressSubnet.setStatus("current")
_FextNetworkAddressStartIP_Type = DisplayString
_FextNetworkAddressStartIP_Object = MibTableColumn
fextNetworkAddressStartIP = _FextNetworkAddressStartIP_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 4, 1, 1, 5),
    _FextNetworkAddressStartIP_Type()
)
fextNetworkAddressStartIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextNetworkAddressStartIP.setStatus("current")
_FextNetworkAddressEndIP_Type = DisplayString
_FextNetworkAddressEndIP_Object = MibTableColumn
fextNetworkAddressEndIP = _FextNetworkAddressEndIP_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 4, 1, 1, 6),
    _FextNetworkAddressEndIP_Type()
)
fextNetworkAddressEndIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextNetworkAddressEndIP.setStatus("current")
_FextNetworkService_ObjectIdentity = ObjectIdentity
fextNetworkService = _FextNetworkService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 4, 2)
)
if mibBuilder.loadTexts:
    fextNetworkService.setStatus("current")
_FextServiceCustom_Object = MibTable
fextServiceCustom = _FextServiceCustom_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 4, 2, 1)
)
if mibBuilder.loadTexts:
    fextServiceCustom.setStatus("current")
_FextServiceCustomEntry_Object = MibTableRow
fextServiceCustomEntry = _FextServiceCustomEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 4, 2, 1, 1)
)
fextServiceCustomEntry.setIndexNames(
    (0, "FORTINET-FORTIEXTENDER-MIB", "fextServiceCustomIndex"),
)
if mibBuilder.loadTexts:
    fextServiceCustomEntry.setStatus("current")
_FextServiceCustomIndex_Type = FnIndex
_FextServiceCustomIndex_Object = MibTableColumn
fextServiceCustomIndex = _FextServiceCustomIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 4, 2, 1, 1, 1),
    _FextServiceCustomIndex_Type()
)
fextServiceCustomIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fextServiceCustomIndex.setStatus("current")
_FextServiceCustomName_Type = DisplayString
_FextServiceCustomName_Object = MibTableColumn
fextServiceCustomName = _FextServiceCustomName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 4, 2, 1, 1, 2),
    _FextServiceCustomName_Type()
)
fextServiceCustomName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextServiceCustomName.setStatus("current")
_FextServiceCustomProtocol_Type = DisplayString
_FextServiceCustomProtocol_Object = MibTableColumn
fextServiceCustomProtocol = _FextServiceCustomProtocol_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 4, 2, 1, 1, 3),
    _FextServiceCustomProtocol_Type()
)
fextServiceCustomProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextServiceCustomProtocol.setStatus("current")
_FextServiceCustomProtocolNumber_Type = DisplayString
_FextServiceCustomProtocolNumber_Object = MibTableColumn
fextServiceCustomProtocolNumber = _FextServiceCustomProtocolNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 4, 2, 1, 1, 4),
    _FextServiceCustomProtocolNumber_Type()
)
fextServiceCustomProtocolNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextServiceCustomProtocolNumber.setStatus("current")
_FextServiceCustomTCPPortRange_Type = DisplayString
_FextServiceCustomTCPPortRange_Object = MibTableColumn
fextServiceCustomTCPPortRange = _FextServiceCustomTCPPortRange_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 4, 2, 1, 1, 5),
    _FextServiceCustomTCPPortRange_Type()
)
fextServiceCustomTCPPortRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextServiceCustomTCPPortRange.setStatus("current")
_FextServiceCustomUDPPortRange_Type = DisplayString
_FextServiceCustomUDPPortRange_Object = MibTableColumn
fextServiceCustomUDPPortRange = _FextServiceCustomUDPPortRange_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 4, 2, 1, 1, 6),
    _FextServiceCustomUDPPortRange_Type()
)
fextServiceCustomUDPPortRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextServiceCustomUDPPortRange.setStatus("current")
_FextFirewall_ObjectIdentity = ObjectIdentity
fextFirewall = _FextFirewall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 5)
)
_FextFirewallPolicy_Object = MibTable
fextFirewallPolicy = _FextFirewallPolicy_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 5, 1)
)
if mibBuilder.loadTexts:
    fextFirewallPolicy.setStatus("current")
_FextFirewallPolicyEntry_Object = MibTableRow
fextFirewallPolicyEntry = _FextFirewallPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 5, 1, 1)
)
fextFirewallPolicyEntry.setIndexNames(
    (0, "FORTINET-FORTIEXTENDER-MIB", "fextFirewallPolicyIndex"),
)
if mibBuilder.loadTexts:
    fextFirewallPolicyEntry.setStatus("current")
_FextFirewallPolicyIndex_Type = FnIndex
_FextFirewallPolicyIndex_Object = MibTableColumn
fextFirewallPolicyIndex = _FextFirewallPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 5, 1, 1, 1),
    _FextFirewallPolicyIndex_Type()
)
fextFirewallPolicyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fextFirewallPolicyIndex.setStatus("current")
_FextFirewallPolicyName_Type = DisplayString
_FextFirewallPolicyName_Object = MibTableColumn
fextFirewallPolicyName = _FextFirewallPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 5, 1, 1, 2),
    _FextFirewallPolicyName_Type()
)
fextFirewallPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextFirewallPolicyName.setStatus("current")
_FextFirewallPolicySrcIntf_Type = DisplayString
_FextFirewallPolicySrcIntf_Object = MibTableColumn
fextFirewallPolicySrcIntf = _FextFirewallPolicySrcIntf_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 5, 1, 1, 3),
    _FextFirewallPolicySrcIntf_Type()
)
fextFirewallPolicySrcIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextFirewallPolicySrcIntf.setStatus("current")
_FextFirewallPolicyDstIntf_Type = DisplayString
_FextFirewallPolicyDstIntf_Object = MibTableColumn
fextFirewallPolicyDstIntf = _FextFirewallPolicyDstIntf_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 5, 1, 1, 4),
    _FextFirewallPolicyDstIntf_Type()
)
fextFirewallPolicyDstIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextFirewallPolicyDstIntf.setStatus("current")
_FextFirewallPolicySrcAddr_Type = DisplayString
_FextFirewallPolicySrcAddr_Object = MibTableColumn
fextFirewallPolicySrcAddr = _FextFirewallPolicySrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 5, 1, 1, 5),
    _FextFirewallPolicySrcAddr_Type()
)
fextFirewallPolicySrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextFirewallPolicySrcAddr.setStatus("current")
_FextFirewallPolicyDstAddr_Type = DisplayString
_FextFirewallPolicyDstAddr_Object = MibTableColumn
fextFirewallPolicyDstAddr = _FextFirewallPolicyDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 5, 1, 1, 6),
    _FextFirewallPolicyDstAddr_Type()
)
fextFirewallPolicyDstAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextFirewallPolicyDstAddr.setStatus("current")
_FextFirewallPolicyAction_Type = DisplayString
_FextFirewallPolicyAction_Object = MibTableColumn
fextFirewallPolicyAction = _FextFirewallPolicyAction_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 5, 1, 1, 7),
    _FextFirewallPolicyAction_Type()
)
fextFirewallPolicyAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextFirewallPolicyAction.setStatus("current")
_FextFirewallPolicyStatus_Type = DisplayString
_FextFirewallPolicyStatus_Object = MibTableColumn
fextFirewallPolicyStatus = _FextFirewallPolicyStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 5, 1, 1, 8),
    _FextFirewallPolicyStatus_Type()
)
fextFirewallPolicyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextFirewallPolicyStatus.setStatus("current")
_FextFirewallPolicyService_Type = DisplayString
_FextFirewallPolicyService_Object = MibTableColumn
fextFirewallPolicyService = _FextFirewallPolicyService_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 5, 1, 1, 9),
    _FextFirewallPolicyService_Type()
)
fextFirewallPolicyService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextFirewallPolicyService.setStatus("current")
_FextFirewallPolicyNAT_Type = DisplayString
_FextFirewallPolicyNAT_Object = MibTableColumn
fextFirewallPolicyNAT = _FextFirewallPolicyNAT_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 5, 1, 1, 10),
    _FextFirewallPolicyNAT_Type()
)
fextFirewallPolicyNAT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextFirewallPolicyNAT.setStatus("current")
_FextRouter_ObjectIdentity = ObjectIdentity
fextRouter = _FextRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 6)
)
_FextRouterPolicy_Object = MibTable
fextRouterPolicy = _FextRouterPolicy_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 6, 1)
)
if mibBuilder.loadTexts:
    fextRouterPolicy.setStatus("current")
_FextRouterPolicyEntry_Object = MibTableRow
fextRouterPolicyEntry = _FextRouterPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 6, 1, 1)
)
fextRouterPolicyEntry.setIndexNames(
    (0, "FORTINET-FORTIEXTENDER-MIB", "fextRouterPolicyIndex"),
)
if mibBuilder.loadTexts:
    fextRouterPolicyEntry.setStatus("current")
_FextRouterPolicyIndex_Type = FnIndex
_FextRouterPolicyIndex_Object = MibTableColumn
fextRouterPolicyIndex = _FextRouterPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 6, 1, 1, 1),
    _FextRouterPolicyIndex_Type()
)
fextRouterPolicyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fextRouterPolicyIndex.setStatus("current")
_FextRouterPolicyName_Type = DisplayString
_FextRouterPolicyName_Object = MibTableColumn
fextRouterPolicyName = _FextRouterPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 6, 1, 1, 2),
    _FextRouterPolicyName_Type()
)
fextRouterPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextRouterPolicyName.setStatus("current")
_FextRouterPolicyInputDevice_Type = DisplayString
_FextRouterPolicyInputDevice_Object = MibTableColumn
fextRouterPolicyInputDevice = _FextRouterPolicyInputDevice_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 6, 1, 1, 3),
    _FextRouterPolicyInputDevice_Type()
)
fextRouterPolicyInputDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextRouterPolicyInputDevice.setStatus("current")
_FextRouterPolicySrcAddr_Type = DisplayString
_FextRouterPolicySrcAddr_Object = MibTableColumn
fextRouterPolicySrcAddr = _FextRouterPolicySrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 6, 1, 1, 4),
    _FextRouterPolicySrcAddr_Type()
)
fextRouterPolicySrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextRouterPolicySrcAddr.setStatus("current")
_FextRouterPolicySrc_Type = DisplayString
_FextRouterPolicySrc_Object = MibTableColumn
fextRouterPolicySrc = _FextRouterPolicySrc_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 6, 1, 1, 5),
    _FextRouterPolicySrc_Type()
)
fextRouterPolicySrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextRouterPolicySrc.setStatus("current")
_FextRouterPolicyDstAddr_Type = DisplayString
_FextRouterPolicyDstAddr_Object = MibTableColumn
fextRouterPolicyDstAddr = _FextRouterPolicyDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 6, 1, 1, 6),
    _FextRouterPolicyDstAddr_Type()
)
fextRouterPolicyDstAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextRouterPolicyDstAddr.setStatus("current")
_FextRouterPolicyDst_Type = DisplayString
_FextRouterPolicyDst_Object = MibTableColumn
fextRouterPolicyDst = _FextRouterPolicyDst_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 6, 1, 1, 7),
    _FextRouterPolicyDst_Type()
)
fextRouterPolicyDst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextRouterPolicyDst.setStatus("current")
_FextRouterPolicyService_Type = DisplayString
_FextRouterPolicyService_Object = MibTableColumn
fextRouterPolicyService = _FextRouterPolicyService_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 6, 1, 1, 8),
    _FextRouterPolicyService_Type()
)
fextRouterPolicyService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextRouterPolicyService.setStatus("current")
_FextRouterPolicyTarget_Type = DisplayString
_FextRouterPolicyTarget_Object = MibTableColumn
fextRouterPolicyTarget = _FextRouterPolicyTarget_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 6, 1, 1, 9),
    _FextRouterPolicyTarget_Type()
)
fextRouterPolicyTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextRouterPolicyTarget.setStatus("current")
_FextRouterPolicyStatus_Type = DisplayString
_FextRouterPolicyStatus_Object = MibTableColumn
fextRouterPolicyStatus = _FextRouterPolicyStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 6, 1, 1, 10),
    _FextRouterPolicyStatus_Type()
)
fextRouterPolicyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextRouterPolicyStatus.setStatus("current")
_FextRouterPolicyComment_Type = DisplayString
_FextRouterPolicyComment_Object = MibTableColumn
fextRouterPolicyComment = _FextRouterPolicyComment_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 6, 1, 1, 11),
    _FextRouterPolicyComment_Type()
)
fextRouterPolicyComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextRouterPolicyComment.setStatus("current")
_FextRouterStatic_Object = MibTable
fextRouterStatic = _FextRouterStatic_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 6, 2)
)
if mibBuilder.loadTexts:
    fextRouterStatic.setStatus("current")
_FextRouterStaticEntry_Object = MibTableRow
fextRouterStaticEntry = _FextRouterStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 6, 2, 1)
)
fextRouterStaticEntry.setIndexNames(
    (0, "FORTINET-FORTIEXTENDER-MIB", "fextRouterStaticIndex"),
)
if mibBuilder.loadTexts:
    fextRouterStaticEntry.setStatus("current")
_FextRouterStaticIndex_Type = FnIndex
_FextRouterStaticIndex_Object = MibTableColumn
fextRouterStaticIndex = _FextRouterStaticIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 6, 2, 1, 1),
    _FextRouterStaticIndex_Type()
)
fextRouterStaticIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fextRouterStaticIndex.setStatus("current")
_FextRouterStaticName_Type = DisplayString
_FextRouterStaticName_Object = MibTableColumn
fextRouterStaticName = _FextRouterStaticName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 6, 2, 1, 2),
    _FextRouterStaticName_Type()
)
fextRouterStaticName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextRouterStaticName.setStatus("current")
_FextRouterStaticStatus_Type = DisplayString
_FextRouterStaticStatus_Object = MibTableColumn
fextRouterStaticStatus = _FextRouterStaticStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 6, 2, 1, 3),
    _FextRouterStaticStatus_Type()
)
fextRouterStaticStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextRouterStaticStatus.setStatus("current")
_FextRouterStaticDst_Type = DisplayString
_FextRouterStaticDst_Object = MibTableColumn
fextRouterStaticDst = _FextRouterStaticDst_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 6, 2, 1, 4),
    _FextRouterStaticDst_Type()
)
fextRouterStaticDst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextRouterStaticDst.setStatus("current")
_FextRouterStaticGateway_Type = DisplayString
_FextRouterStaticGateway_Object = MibTableColumn
fextRouterStaticGateway = _FextRouterStaticGateway_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 6, 2, 1, 5),
    _FextRouterStaticGateway_Type()
)
fextRouterStaticGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextRouterStaticGateway.setStatus("current")
_FextRouterStaticDistance_Type = DisplayString
_FextRouterStaticDistance_Object = MibTableColumn
fextRouterStaticDistance = _FextRouterStaticDistance_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 6, 2, 1, 6),
    _FextRouterStaticDistance_Type()
)
fextRouterStaticDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextRouterStaticDistance.setStatus("current")
_FextRouterStaticDevice_Type = DisplayString
_FextRouterStaticDevice_Object = MibTableColumn
fextRouterStaticDevice = _FextRouterStaticDevice_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 6, 2, 1, 7),
    _FextRouterStaticDevice_Type()
)
fextRouterStaticDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextRouterStaticDevice.setStatus("current")
_FextRouterStaticComment_Type = DisplayString
_FextRouterStaticComment_Object = MibTableColumn
fextRouterStaticComment = _FextRouterStaticComment_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 6, 2, 1, 8),
    _FextRouterStaticComment_Type()
)
fextRouterStaticComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextRouterStaticComment.setStatus("current")
_FextRouterTarget_Object = MibTable
fextRouterTarget = _FextRouterTarget_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 6, 3)
)
if mibBuilder.loadTexts:
    fextRouterTarget.setStatus("current")
_FextRouterTargetEntry_Object = MibTableRow
fextRouterTargetEntry = _FextRouterTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 6, 3, 1)
)
fextRouterTargetEntry.setIndexNames(
    (0, "FORTINET-FORTIEXTENDER-MIB", "fextRouterTargetIndex"),
)
if mibBuilder.loadTexts:
    fextRouterTargetEntry.setStatus("current")
_FextRouterTargetIndex_Type = FnIndex
_FextRouterTargetIndex_Object = MibTableColumn
fextRouterTargetIndex = _FextRouterTargetIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 6, 3, 1, 1),
    _FextRouterTargetIndex_Type()
)
fextRouterTargetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fextRouterTargetIndex.setStatus("current")
_FextRouterTargetName_Type = DisplayString
_FextRouterTargetName_Object = MibTableColumn
fextRouterTargetName = _FextRouterTargetName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 6, 3, 1, 2),
    _FextRouterTargetName_Type()
)
fextRouterTargetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextRouterTargetName.setStatus("current")
_FextRouterTargetInterface_Type = DisplayString
_FextRouterTargetInterface_Object = MibTableColumn
fextRouterTargetInterface = _FextRouterTargetInterface_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 6, 3, 1, 3),
    _FextRouterTargetInterface_Type()
)
fextRouterTargetInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextRouterTargetInterface.setStatus("current")
_FextRouterTargetNextHop_Type = DisplayString
_FextRouterTargetNextHop_Object = MibTableColumn
fextRouterTargetNextHop = _FextRouterTargetNextHop_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 6, 3, 1, 4),
    _FextRouterTargetNextHop_Type()
)
fextRouterTargetNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextRouterTargetNextHop.setStatus("current")
_FextRouterTargetIntfNH_Type = DisplayString
_FextRouterTargetIntfNH_Object = MibTableColumn
fextRouterTargetIntfNH = _FextRouterTargetIntfNH_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 6, 3, 1, 5),
    _FextRouterTargetIntfNH_Type()
)
fextRouterTargetIntfNH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextRouterTargetIntfNH.setStatus("current")
_FextRouterMulticast_ObjectIdentity = ObjectIdentity
fextRouterMulticast = _FextRouterMulticast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 6, 4)
)
if mibBuilder.loadTexts:
    fextRouterMulticast.setStatus("current")
_FextMcastPIMSMGlobal_ObjectIdentity = ObjectIdentity
fextMcastPIMSMGlobal = _FextMcastPIMSMGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 6, 4, 1)
)
if mibBuilder.loadTexts:
    fextMcastPIMSMGlobal.setStatus("current")
_FextPIMSMGlobalJoinPruneInterval_Type = DisplayString
_FextPIMSMGlobalJoinPruneInterval_Object = MibScalar
fextPIMSMGlobalJoinPruneInterval = _FextPIMSMGlobalJoinPruneInterval_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 6, 4, 1, 1),
    _FextPIMSMGlobalJoinPruneInterval_Type()
)
fextPIMSMGlobalJoinPruneInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextPIMSMGlobalJoinPruneInterval.setStatus("current")
_FextPIMSMGlobalHelloInterval_Type = DisplayString
_FextPIMSMGlobalHelloInterval_Object = MibScalar
fextPIMSMGlobalHelloInterval = _FextPIMSMGlobalHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 6, 4, 1, 2),
    _FextPIMSMGlobalHelloInterval_Type()
)
fextPIMSMGlobalHelloInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextPIMSMGlobalHelloInterval.setStatus("current")
_FextPIMSMGlobalRPAddress_Object = MibTable
fextPIMSMGlobalRPAddress = _FextPIMSMGlobalRPAddress_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 6, 4, 1, 3)
)
if mibBuilder.loadTexts:
    fextPIMSMGlobalRPAddress.setStatus("current")
_FextPIMSMGlobalRPAddressEntry_Object = MibTableRow
fextPIMSMGlobalRPAddressEntry = _FextPIMSMGlobalRPAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 6, 4, 1, 3, 1)
)
fextPIMSMGlobalRPAddressEntry.setIndexNames(
    (0, "FORTINET-FORTIEXTENDER-MIB", "fextPIMRPAddressIndex"),
)
if mibBuilder.loadTexts:
    fextPIMSMGlobalRPAddressEntry.setStatus("current")
_FextPIMRPAddressIndex_Type = FnIndex
_FextPIMRPAddressIndex_Object = MibTableColumn
fextPIMRPAddressIndex = _FextPIMRPAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 6, 4, 1, 3, 1, 1),
    _FextPIMRPAddressIndex_Type()
)
fextPIMRPAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fextPIMRPAddressIndex.setStatus("current")
_FextPIMRPAddressName_Type = DisplayString
_FextPIMRPAddressName_Object = MibTableColumn
fextPIMRPAddressName = _FextPIMRPAddressName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 6, 4, 1, 3, 1, 2),
    _FextPIMRPAddressName_Type()
)
fextPIMRPAddressName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextPIMRPAddressName.setStatus("current")
_FextPIMRPAddressAddress_Type = DisplayString
_FextPIMRPAddressAddress_Object = MibTableColumn
fextPIMRPAddressAddress = _FextPIMRPAddressAddress_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 6, 4, 1, 3, 1, 3),
    _FextPIMRPAddressAddress_Type()
)
fextPIMRPAddressAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextPIMRPAddressAddress.setStatus("current")
_FextPIMRPAddressGroup_Type = DisplayString
_FextPIMRPAddressGroup_Object = MibTableColumn
fextPIMRPAddressGroup = _FextPIMRPAddressGroup_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 6, 4, 1, 3, 1, 4),
    _FextPIMRPAddressGroup_Type()
)
fextPIMRPAddressGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextPIMRPAddressGroup.setStatus("current")
_FextMcastInterface_Object = MibTable
fextMcastInterface = _FextMcastInterface_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 6, 4, 2)
)
if mibBuilder.loadTexts:
    fextMcastInterface.setStatus("current")
_FextMcastInterfaceEntry_Object = MibTableRow
fextMcastInterfaceEntry = _FextMcastInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 6, 4, 2, 1)
)
fextMcastInterfaceEntry.setIndexNames(
    (0, "FORTINET-FORTIEXTENDER-MIB", "fextMcastInterfaceIndex"),
)
if mibBuilder.loadTexts:
    fextMcastInterfaceEntry.setStatus("current")
_FextMcastInterfaceIndex_Type = FnIndex
_FextMcastInterfaceIndex_Object = MibTableColumn
fextMcastInterfaceIndex = _FextMcastInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 6, 4, 2, 1, 1),
    _FextMcastInterfaceIndex_Type()
)
fextMcastInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fextMcastInterfaceIndex.setStatus("current")
_FextMcastInterfaceName_Type = DisplayString
_FextMcastInterfaceName_Object = MibTableColumn
fextMcastInterfaceName = _FextMcastInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 6, 4, 2, 1, 2),
    _FextMcastInterfaceName_Type()
)
fextMcastInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextMcastInterfaceName.setStatus("current")
_FextVPN_ObjectIdentity = ObjectIdentity
fextVPN = _FextVPN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 7)
)
_FextVPNIPsec_ObjectIdentity = ObjectIdentity
fextVPNIPsec = _FextVPNIPsec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 7, 1)
)
if mibBuilder.loadTexts:
    fextVPNIPsec.setStatus("current")
_FextVPNIPsecPhase1_Object = MibTable
fextVPNIPsecPhase1 = _FextVPNIPsecPhase1_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 7, 1, 1)
)
if mibBuilder.loadTexts:
    fextVPNIPsecPhase1.setStatus("current")
_FextVPNIPsecPhase1Entry_Object = MibTableRow
fextVPNIPsecPhase1Entry = _FextVPNIPsecPhase1Entry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 7, 1, 1, 1)
)
fextVPNIPsecPhase1Entry.setIndexNames(
    (0, "FORTINET-FORTIEXTENDER-MIB", "fextIPsecPhase1Index"),
)
if mibBuilder.loadTexts:
    fextVPNIPsecPhase1Entry.setStatus("current")
_FextIPsecPhase1Index_Type = FnIndex
_FextIPsecPhase1Index_Object = MibTableColumn
fextIPsecPhase1Index = _FextIPsecPhase1Index_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 7, 1, 1, 1, 1),
    _FextIPsecPhase1Index_Type()
)
fextIPsecPhase1Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fextIPsecPhase1Index.setStatus("current")
_FextIPsecPhase1Name_Type = DisplayString
_FextIPsecPhase1Name_Object = MibTableColumn
fextIPsecPhase1Name = _FextIPsecPhase1Name_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 7, 1, 1, 1, 2),
    _FextIPsecPhase1Name_Type()
)
fextIPsecPhase1Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextIPsecPhase1Name.setStatus("current")
_FextIPsecPhase1IKEVersion_Type = DisplayString
_FextIPsecPhase1IKEVersion_Object = MibTableColumn
fextIPsecPhase1IKEVersion = _FextIPsecPhase1IKEVersion_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 7, 1, 1, 1, 3),
    _FextIPsecPhase1IKEVersion_Type()
)
fextIPsecPhase1IKEVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextIPsecPhase1IKEVersion.setStatus("current")
_FextIPsecPhase1KeyLife_Type = DisplayString
_FextIPsecPhase1KeyLife_Object = MibTableColumn
fextIPsecPhase1KeyLife = _FextIPsecPhase1KeyLife_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 7, 1, 1, 1, 4),
    _FextIPsecPhase1KeyLife_Type()
)
fextIPsecPhase1KeyLife.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextIPsecPhase1KeyLife.setStatus("current")
_FextIPsecPhase1Mode_Type = DisplayString
_FextIPsecPhase1Mode_Object = MibTableColumn
fextIPsecPhase1Mode = _FextIPsecPhase1Mode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 7, 1, 1, 1, 5),
    _FextIPsecPhase1Mode_Type()
)
fextIPsecPhase1Mode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextIPsecPhase1Mode.setStatus("current")
_FextIPsecPhase1Proposal_Type = DisplayString
_FextIPsecPhase1Proposal_Object = MibTableColumn
fextIPsecPhase1Proposal = _FextIPsecPhase1Proposal_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 7, 1, 1, 1, 6),
    _FextIPsecPhase1Proposal_Type()
)
fextIPsecPhase1Proposal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextIPsecPhase1Proposal.setStatus("current")
_FextIPsecPhase1DHGroup_Type = DisplayString
_FextIPsecPhase1DHGroup_Object = MibTableColumn
fextIPsecPhase1DHGroup = _FextIPsecPhase1DHGroup_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 7, 1, 1, 1, 7),
    _FextIPsecPhase1DHGroup_Type()
)
fextIPsecPhase1DHGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextIPsecPhase1DHGroup.setStatus("current")
_FextIPsecPhase1Interface_Type = DisplayString
_FextIPsecPhase1Interface_Object = MibTableColumn
fextIPsecPhase1Interface = _FextIPsecPhase1Interface_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 7, 1, 1, 1, 8),
    _FextIPsecPhase1Interface_Type()
)
fextIPsecPhase1Interface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextIPsecPhase1Interface.setStatus("current")
_FextIPsecPhase1Type_Type = DisplayString
_FextIPsecPhase1Type_Object = MibTableColumn
fextIPsecPhase1Type = _FextIPsecPhase1Type_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 7, 1, 1, 1, 9),
    _FextIPsecPhase1Type_Type()
)
fextIPsecPhase1Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextIPsecPhase1Type.setStatus("current")
_FextIPsecPhase1RemoteGW_Type = DisplayString
_FextIPsecPhase1RemoteGW_Object = MibTableColumn
fextIPsecPhase1RemoteGW = _FextIPsecPhase1RemoteGW_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 7, 1, 1, 1, 10),
    _FextIPsecPhase1RemoteGW_Type()
)
fextIPsecPhase1RemoteGW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextIPsecPhase1RemoteGW.setStatus("current")
_FextIPsecPhase1RemoteGWDDNS_Type = DisplayString
_FextIPsecPhase1RemoteGWDDNS_Object = MibTableColumn
fextIPsecPhase1RemoteGWDDNS = _FextIPsecPhase1RemoteGWDDNS_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 7, 1, 1, 1, 11),
    _FextIPsecPhase1RemoteGWDDNS_Type()
)
fextIPsecPhase1RemoteGWDDNS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextIPsecPhase1RemoteGWDDNS.setStatus("current")
_FextIPsecPhase1AuthMethod_Type = DisplayString
_FextIPsecPhase1AuthMethod_Object = MibTableColumn
fextIPsecPhase1AuthMethod = _FextIPsecPhase1AuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 7, 1, 1, 1, 12),
    _FextIPsecPhase1AuthMethod_Type()
)
fextIPsecPhase1AuthMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextIPsecPhase1AuthMethod.setStatus("current")
_FextIPsecPhase1PSKSecret_Type = DisplayString
_FextIPsecPhase1PSKSecret_Object = MibTableColumn
fextIPsecPhase1PSKSecret = _FextIPsecPhase1PSKSecret_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 7, 1, 1, 1, 13),
    _FextIPsecPhase1PSKSecret_Type()
)
fextIPsecPhase1PSKSecret.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextIPsecPhase1PSKSecret.setStatus("current")
_FextIPsecPhase1Certificate_Type = DisplayString
_FextIPsecPhase1Certificate_Object = MibTableColumn
fextIPsecPhase1Certificate = _FextIPsecPhase1Certificate_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 7, 1, 1, 1, 14),
    _FextIPsecPhase1Certificate_Type()
)
fextIPsecPhase1Certificate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextIPsecPhase1Certificate.setStatus("current")
_FextIPsecPhase1Peer_Type = DisplayString
_FextIPsecPhase1Peer_Object = MibTableColumn
fextIPsecPhase1Peer = _FextIPsecPhase1Peer_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 7, 1, 1, 1, 15),
    _FextIPsecPhase1Peer_Type()
)
fextIPsecPhase1Peer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextIPsecPhase1Peer.setStatus("current")
_FextIPsecPhase1LocalID_Type = DisplayString
_FextIPsecPhase1LocalID_Object = MibTableColumn
fextIPsecPhase1LocalID = _FextIPsecPhase1LocalID_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 7, 1, 1, 1, 16),
    _FextIPsecPhase1LocalID_Type()
)
fextIPsecPhase1LocalID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextIPsecPhase1LocalID.setStatus("current")
_FextIPsecPhase1PeerID_Type = DisplayString
_FextIPsecPhase1PeerID_Object = MibTableColumn
fextIPsecPhase1PeerID = _FextIPsecPhase1PeerID_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 7, 1, 1, 1, 17),
    _FextIPsecPhase1PeerID_Type()
)
fextIPsecPhase1PeerID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextIPsecPhase1PeerID.setStatus("current")
_FextVPNIPsecPhase2_Object = MibTable
fextVPNIPsecPhase2 = _FextVPNIPsecPhase2_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 7, 1, 2)
)
if mibBuilder.loadTexts:
    fextVPNIPsecPhase2.setStatus("current")
_FextVPNIPsecPhase2Entry_Object = MibTableRow
fextVPNIPsecPhase2Entry = _FextVPNIPsecPhase2Entry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 7, 1, 2, 1)
)
fextVPNIPsecPhase2Entry.setIndexNames(
    (0, "FORTINET-FORTIEXTENDER-MIB", "fextIPsecPhase2Index"),
)
if mibBuilder.loadTexts:
    fextVPNIPsecPhase2Entry.setStatus("current")
_FextIPsecPhase2Index_Type = FnIndex
_FextIPsecPhase2Index_Object = MibTableColumn
fextIPsecPhase2Index = _FextIPsecPhase2Index_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 7, 1, 2, 1, 1),
    _FextIPsecPhase2Index_Type()
)
fextIPsecPhase2Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fextIPsecPhase2Index.setStatus("current")
_FextIPsecPhase2Name_Type = DisplayString
_FextIPsecPhase2Name_Object = MibTableColumn
fextIPsecPhase2Name = _FextIPsecPhase2Name_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 7, 1, 2, 1, 2),
    _FextIPsecPhase2Name_Type()
)
fextIPsecPhase2Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextIPsecPhase2Name.setStatus("current")
_FextIPsecPhase2Phase1Name_Type = DisplayString
_FextIPsecPhase2Phase1Name_Object = MibTableColumn
fextIPsecPhase2Phase1Name = _FextIPsecPhase2Phase1Name_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 7, 1, 2, 1, 3),
    _FextIPsecPhase2Phase1Name_Type()
)
fextIPsecPhase2Phase1Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextIPsecPhase2Phase1Name.setStatus("current")
_FextIPsecPhase2Proposal_Type = DisplayString
_FextIPsecPhase2Proposal_Object = MibTableColumn
fextIPsecPhase2Proposal = _FextIPsecPhase2Proposal_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 7, 1, 2, 1, 4),
    _FextIPsecPhase2Proposal_Type()
)
fextIPsecPhase2Proposal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextIPsecPhase2Proposal.setStatus("current")
_FextIPsecPhase2PFS_Type = DisplayString
_FextIPsecPhase2PFS_Object = MibTableColumn
fextIPsecPhase2PFS = _FextIPsecPhase2PFS_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 7, 1, 2, 1, 5),
    _FextIPsecPhase2PFS_Type()
)
fextIPsecPhase2PFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextIPsecPhase2PFS.setStatus("current")
_FextIPsecPhase2DHGroup_Type = DisplayString
_FextIPsecPhase2DHGroup_Object = MibTableColumn
fextIPsecPhase2DHGroup = _FextIPsecPhase2DHGroup_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 7, 1, 2, 1, 6),
    _FextIPsecPhase2DHGroup_Type()
)
fextIPsecPhase2DHGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextIPsecPhase2DHGroup.setStatus("current")
_FextIPsecPhase2KeyLifeType_Type = DisplayString
_FextIPsecPhase2KeyLifeType_Object = MibTableColumn
fextIPsecPhase2KeyLifeType = _FextIPsecPhase2KeyLifeType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 7, 1, 2, 1, 7),
    _FextIPsecPhase2KeyLifeType_Type()
)
fextIPsecPhase2KeyLifeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextIPsecPhase2KeyLifeType.setStatus("current")
_FextIPsecPhase2KeyLifeSeconds_Type = DisplayString
_FextIPsecPhase2KeyLifeSeconds_Object = MibTableColumn
fextIPsecPhase2KeyLifeSeconds = _FextIPsecPhase2KeyLifeSeconds_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 7, 1, 2, 1, 8),
    _FextIPsecPhase2KeyLifeSeconds_Type()
)
fextIPsecPhase2KeyLifeSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextIPsecPhase2KeyLifeSeconds.setStatus("current")
_FextIPsecPhase2KeyLifeKBs_Type = DisplayString
_FextIPsecPhase2KeyLifeKBs_Object = MibTableColumn
fextIPsecPhase2KeyLifeKBs = _FextIPsecPhase2KeyLifeKBs_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 7, 1, 2, 1, 9),
    _FextIPsecPhase2KeyLifeKBs_Type()
)
fextIPsecPhase2KeyLifeKBs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextIPsecPhase2KeyLifeKBs.setStatus("current")
_FextIPsecPhase2Encapsulation_Type = DisplayString
_FextIPsecPhase2Encapsulation_Object = MibTableColumn
fextIPsecPhase2Encapsulation = _FextIPsecPhase2Encapsulation_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 7, 1, 2, 1, 10),
    _FextIPsecPhase2Encapsulation_Type()
)
fextIPsecPhase2Encapsulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextIPsecPhase2Encapsulation.setStatus("current")
_FextIPsecPhase2Protocol_Type = DisplayString
_FextIPsecPhase2Protocol_Object = MibTableColumn
fextIPsecPhase2Protocol = _FextIPsecPhase2Protocol_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 7, 1, 2, 1, 11),
    _FextIPsecPhase2Protocol_Type()
)
fextIPsecPhase2Protocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextIPsecPhase2Protocol.setStatus("current")
_FextIPsecPhase2SrcAddrType_Type = DisplayString
_FextIPsecPhase2SrcAddrType_Object = MibTableColumn
fextIPsecPhase2SrcAddrType = _FextIPsecPhase2SrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 7, 1, 2, 1, 12),
    _FextIPsecPhase2SrcAddrType_Type()
)
fextIPsecPhase2SrcAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextIPsecPhase2SrcAddrType.setStatus("current")
_FextIPsecPhase2SrcSubnet_Type = DisplayString
_FextIPsecPhase2SrcSubnet_Object = MibTableColumn
fextIPsecPhase2SrcSubnet = _FextIPsecPhase2SrcSubnet_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 7, 1, 2, 1, 13),
    _FextIPsecPhase2SrcSubnet_Type()
)
fextIPsecPhase2SrcSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextIPsecPhase2SrcSubnet.setStatus("current")
_FextIPsecPhase2SrcStartIp_Type = DisplayString
_FextIPsecPhase2SrcStartIp_Object = MibTableColumn
fextIPsecPhase2SrcStartIp = _FextIPsecPhase2SrcStartIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 7, 1, 2, 1, 14),
    _FextIPsecPhase2SrcStartIp_Type()
)
fextIPsecPhase2SrcStartIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextIPsecPhase2SrcStartIp.setStatus("current")
_FextIPsecPhase2SrcEndIp_Type = DisplayString
_FextIPsecPhase2SrcEndIp_Object = MibTableColumn
fextIPsecPhase2SrcEndIp = _FextIPsecPhase2SrcEndIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 7, 1, 2, 1, 15),
    _FextIPsecPhase2SrcEndIp_Type()
)
fextIPsecPhase2SrcEndIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextIPsecPhase2SrcEndIp.setStatus("current")
_FextIPsecPhase2SrcName_Type = DisplayString
_FextIPsecPhase2SrcName_Object = MibTableColumn
fextIPsecPhase2SrcName = _FextIPsecPhase2SrcName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 7, 1, 2, 1, 16),
    _FextIPsecPhase2SrcName_Type()
)
fextIPsecPhase2SrcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextIPsecPhase2SrcName.setStatus("current")
_FextIPsecPhase2SrcPort_Type = DisplayString
_FextIPsecPhase2SrcPort_Object = MibTableColumn
fextIPsecPhase2SrcPort = _FextIPsecPhase2SrcPort_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 7, 1, 2, 1, 17),
    _FextIPsecPhase2SrcPort_Type()
)
fextIPsecPhase2SrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextIPsecPhase2SrcPort.setStatus("current")
_FextIPsecPhase2DstAddrType_Type = DisplayString
_FextIPsecPhase2DstAddrType_Object = MibTableColumn
fextIPsecPhase2DstAddrType = _FextIPsecPhase2DstAddrType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 7, 1, 2, 1, 18),
    _FextIPsecPhase2DstAddrType_Type()
)
fextIPsecPhase2DstAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextIPsecPhase2DstAddrType.setStatus("current")
_FextIPsecPhase2DstSubnet_Type = DisplayString
_FextIPsecPhase2DstSubnet_Object = MibTableColumn
fextIPsecPhase2DstSubnet = _FextIPsecPhase2DstSubnet_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 7, 1, 2, 1, 19),
    _FextIPsecPhase2DstSubnet_Type()
)
fextIPsecPhase2DstSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextIPsecPhase2DstSubnet.setStatus("current")
_FextIPsecPhase2DstStartIp_Type = DisplayString
_FextIPsecPhase2DstStartIp_Object = MibTableColumn
fextIPsecPhase2DstStartIp = _FextIPsecPhase2DstStartIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 7, 1, 2, 1, 20),
    _FextIPsecPhase2DstStartIp_Type()
)
fextIPsecPhase2DstStartIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextIPsecPhase2DstStartIp.setStatus("current")
_FextIPsecPhase2DstEndIp_Type = DisplayString
_FextIPsecPhase2DstEndIp_Object = MibTableColumn
fextIPsecPhase2DstEndIp = _FextIPsecPhase2DstEndIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 7, 1, 2, 1, 21),
    _FextIPsecPhase2DstEndIp_Type()
)
fextIPsecPhase2DstEndIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextIPsecPhase2DstEndIp.setStatus("current")
_FextIPsecPhase2DstName_Type = DisplayString
_FextIPsecPhase2DstName_Object = MibTableColumn
fextIPsecPhase2DstName = _FextIPsecPhase2DstName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 7, 1, 2, 1, 22),
    _FextIPsecPhase2DstName_Type()
)
fextIPsecPhase2DstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextIPsecPhase2DstName.setStatus("current")
_FextIPsecPhase2DstPort_Type = DisplayString
_FextIPsecPhase2DstPort_Object = MibTableColumn
fextIPsecPhase2DstPort = _FextIPsecPhase2DstPort_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 7, 1, 2, 1, 23),
    _FextIPsecPhase2DstPort_Type()
)
fextIPsecPhase2DstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextIPsecPhase2DstPort.setStatus("current")
_FextVPNCertificate_ObjectIdentity = ObjectIdentity
fextVPNCertificate = _FextVPNCertificate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 7, 2)
)
if mibBuilder.loadTexts:
    fextVPNCertificate.setStatus("current")
_FextVPNCertificateCA_Object = MibTable
fextVPNCertificateCA = _FextVPNCertificateCA_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 7, 2, 1)
)
if mibBuilder.loadTexts:
    fextVPNCertificateCA.setStatus("current")
_FextVPNCertificateCAEntry_Object = MibTableRow
fextVPNCertificateCAEntry = _FextVPNCertificateCAEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 7, 2, 1, 1)
)
fextVPNCertificateCAEntry.setIndexNames(
    (0, "FORTINET-FORTIEXTENDER-MIB", "fextCertificateCAIndex"),
)
if mibBuilder.loadTexts:
    fextVPNCertificateCAEntry.setStatus("current")
_FextCertificateCAIndex_Type = FnIndex
_FextCertificateCAIndex_Object = MibTableColumn
fextCertificateCAIndex = _FextCertificateCAIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 7, 2, 1, 1, 1),
    _FextCertificateCAIndex_Type()
)
fextCertificateCAIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fextCertificateCAIndex.setStatus("current")
_FextCertificateCAName_Type = DisplayString
_FextCertificateCAName_Object = MibTableColumn
fextCertificateCAName = _FextCertificateCAName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 7, 2, 1, 1, 2),
    _FextCertificateCAName_Type()
)
fextCertificateCAName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextCertificateCAName.setStatus("current")
_FextCertificateCAComment_Type = DisplayString
_FextCertificateCAComment_Object = MibTableColumn
fextCertificateCAComment = _FextCertificateCAComment_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 7, 2, 1, 1, 3),
    _FextCertificateCAComment_Type()
)
fextCertificateCAComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextCertificateCAComment.setStatus("current")
_FextCertificateCASource_Type = DisplayString
_FextCertificateCASource_Object = MibTableColumn
fextCertificateCASource = _FextCertificateCASource_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 7, 2, 1, 1, 4),
    _FextCertificateCASource_Type()
)
fextCertificateCASource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextCertificateCASource.setStatus("current")
_FextVPNCertificateLocal_Object = MibTable
fextVPNCertificateLocal = _FextVPNCertificateLocal_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 7, 2, 2)
)
if mibBuilder.loadTexts:
    fextVPNCertificateLocal.setStatus("current")
_FextVPNCertificateLocalEntry_Object = MibTableRow
fextVPNCertificateLocalEntry = _FextVPNCertificateLocalEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 7, 2, 2, 1)
)
fextVPNCertificateLocalEntry.setIndexNames(
    (0, "FORTINET-FORTIEXTENDER-MIB", "fextCertificateLocalIndex"),
)
if mibBuilder.loadTexts:
    fextVPNCertificateLocalEntry.setStatus("current")
_FextCertificateLocalIndex_Type = FnIndex
_FextCertificateLocalIndex_Object = MibTableColumn
fextCertificateLocalIndex = _FextCertificateLocalIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 7, 2, 2, 1, 1),
    _FextCertificateLocalIndex_Type()
)
fextCertificateLocalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fextCertificateLocalIndex.setStatus("current")
_FextCertificateLocalName_Type = DisplayString
_FextCertificateLocalName_Object = MibTableColumn
fextCertificateLocalName = _FextCertificateLocalName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 7, 2, 2, 1, 2),
    _FextCertificateLocalName_Type()
)
fextCertificateLocalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextCertificateLocalName.setStatus("current")
_FextCertificateLocalComment_Type = DisplayString
_FextCertificateLocalComment_Object = MibTableColumn
fextCertificateLocalComment = _FextCertificateLocalComment_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 7, 2, 2, 1, 3),
    _FextCertificateLocalComment_Type()
)
fextCertificateLocalComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextCertificateLocalComment.setStatus("current")
_FextCertificateLocalSource_Type = DisplayString
_FextCertificateLocalSource_Object = MibTableColumn
fextCertificateLocalSource = _FextCertificateLocalSource_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 7, 2, 2, 1, 4),
    _FextCertificateLocalSource_Type()
)
fextCertificateLocalSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextCertificateLocalSource.setStatus("current")
_FextHMon_ObjectIdentity = ObjectIdentity
fextHMon = _FextHMon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 8)
)
_FextHMonIntf_Object = MibTable
fextHMonIntf = _FextHMonIntf_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 8, 1)
)
if mibBuilder.loadTexts:
    fextHMonIntf.setStatus("current")
_FextHMonIntfEntry_Object = MibTableRow
fextHMonIntfEntry = _FextHMonIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 8, 1, 1)
)
fextHMonIntfEntry.setIndexNames(
    (0, "FORTINET-FORTIEXTENDER-MIB", "fextHMonIntfIndex"),
)
if mibBuilder.loadTexts:
    fextHMonIntfEntry.setStatus("current")
_FextHMonIntfIndex_Type = FnIndex
_FextHMonIntfIndex_Object = MibTableColumn
fextHMonIntfIndex = _FextHMonIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 8, 1, 1, 1),
    _FextHMonIntfIndex_Type()
)
fextHMonIntfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fextHMonIntfIndex.setStatus("current")
_FextHMonIntfName_Type = DisplayString
_FextHMonIntfName_Object = MibTableColumn
fextHMonIntfName = _FextHMonIntfName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 8, 1, 1, 2),
    _FextHMonIntfName_Type()
)
fextHMonIntfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextHMonIntfName.setStatus("current")
_FextHMonIntfInterval_Type = DisplayString
_FextHMonIntfInterval_Object = MibTableColumn
fextHMonIntfInterval = _FextHMonIntfInterval_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 8, 1, 1, 3),
    _FextHMonIntfInterval_Type()
)
fextHMonIntfInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextHMonIntfInterval.setStatus("current")
_FextHMonIntfInterface_Type = DisplayString
_FextHMonIntfInterface_Object = MibTableColumn
fextHMonIntfInterface = _FextHMonIntfInterface_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 8, 1, 1, 4),
    _FextHMonIntfInterface_Type()
)
fextHMonIntfInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextHMonIntfInterface.setStatus("current")
_FextHMonIntfFilter_Type = DisplayString
_FextHMonIntfFilter_Object = MibTableColumn
fextHMonIntfFilter = _FextHMonIntfFilter_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 8, 1, 1, 5),
    _FextHMonIntfFilter_Type()
)
fextHMonIntfFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextHMonIntfFilter.setStatus("current")
_FextHMonHchk_Object = MibTable
fextHMonHchk = _FextHMonHchk_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 8, 2)
)
if mibBuilder.loadTexts:
    fextHMonHchk.setStatus("current")
_FextHMonHchkEntry_Object = MibTableRow
fextHMonHchkEntry = _FextHMonHchkEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 8, 2, 1)
)
fextHMonHchkEntry.setIndexNames(
    (0, "FORTINET-FORTIEXTENDER-MIB", "fextHMonHchkIndex"),
)
if mibBuilder.loadTexts:
    fextHMonHchkEntry.setStatus("current")
_FextHMonHchkIndex_Type = FnIndex
_FextHMonHchkIndex_Object = MibTableColumn
fextHMonHchkIndex = _FextHMonHchkIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 8, 2, 1, 1),
    _FextHMonHchkIndex_Type()
)
fextHMonHchkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fextHMonHchkIndex.setStatus("current")
_FextHMonHchkName_Type = DisplayString
_FextHMonHchkName_Object = MibTableColumn
fextHMonHchkName = _FextHMonHchkName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 8, 2, 1, 2),
    _FextHMonHchkName_Type()
)
fextHMonHchkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextHMonHchkName.setStatus("current")
_FextHMonHchkProtocol_Type = DisplayString
_FextHMonHchkProtocol_Object = MibTableColumn
fextHMonHchkProtocol = _FextHMonHchkProtocol_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 8, 2, 1, 3),
    _FextHMonHchkProtocol_Type()
)
fextHMonHchkProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextHMonHchkProtocol.setStatus("current")
_FextHMonHchkInterval_Type = DisplayString
_FextHMonHchkInterval_Object = MibTableColumn
fextHMonHchkInterval = _FextHMonHchkInterval_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 8, 2, 1, 4),
    _FextHMonHchkInterval_Type()
)
fextHMonHchkInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextHMonHchkInterval.setStatus("current")
_FextHMonHchkProbeCnt_Type = DisplayString
_FextHMonHchkProbeCnt_Object = MibTableColumn
fextHMonHchkProbeCnt = _FextHMonHchkProbeCnt_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 8, 2, 1, 5),
    _FextHMonHchkProbeCnt_Type()
)
fextHMonHchkProbeCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextHMonHchkProbeCnt.setStatus("current")
_FextHMonHchkProbeTM_Type = DisplayString
_FextHMonHchkProbeTM_Object = MibTableColumn
fextHMonHchkProbeTM = _FextHMonHchkProbeTM_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 8, 2, 1, 6),
    _FextHMonHchkProbeTM_Type()
)
fextHMonHchkProbeTM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextHMonHchkProbeTM.setStatus("current")
_FextHMonHchkProbeTarget_Type = DisplayString
_FextHMonHchkProbeTarget_Object = MibTableColumn
fextHMonHchkProbeTarget = _FextHMonHchkProbeTarget_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 8, 2, 1, 7),
    _FextHMonHchkProbeTarget_Type()
)
fextHMonHchkProbeTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextHMonHchkProbeTarget.setStatus("current")
_FextHMonHchkPort_Type = DisplayString
_FextHMonHchkPort_Object = MibTableColumn
fextHMonHchkPort = _FextHMonHchkPort_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 8, 2, 1, 8),
    _FextHMonHchkPort_Type()
)
fextHMonHchkPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextHMonHchkPort.setStatus("current")
_FextHMonHchkHTTPGet_Type = DisplayString
_FextHMonHchkHTTPGet_Object = MibTableColumn
fextHMonHchkHTTPGet = _FextHMonHchkHTTPGet_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 8, 2, 1, 9),
    _FextHMonHchkHTTPGet_Type()
)
fextHMonHchkHTTPGet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextHMonHchkHTTPGet.setStatus("current")
_FextHMonHchkInterface_Type = DisplayString
_FextHMonHchkInterface_Object = MibTableColumn
fextHMonHchkInterface = _FextHMonHchkInterface_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 8, 2, 1, 10),
    _FextHMonHchkInterface_Type()
)
fextHMonHchkInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextHMonHchkInterface.setStatus("current")
_FextHMonHchkSrcType_Type = DisplayString
_FextHMonHchkSrcType_Object = MibTableColumn
fextHMonHchkSrcType = _FextHMonHchkSrcType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 8, 2, 1, 11),
    _FextHMonHchkSrcType_Type()
)
fextHMonHchkSrcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextHMonHchkSrcType.setStatus("current")
_FextHMonHchkSrcInterface_Type = DisplayString
_FextHMonHchkSrcInterface_Object = MibTableColumn
fextHMonHchkSrcInterface = _FextHMonHchkSrcInterface_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 8, 2, 1, 12),
    _FextHMonHchkSrcInterface_Type()
)
fextHMonHchkSrcInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextHMonHchkSrcInterface.setStatus("current")
_FextHMonHchkSrcIP_Type = DisplayString
_FextHMonHchkSrcIP_Object = MibTableColumn
fextHMonHchkSrcIP = _FextHMonHchkSrcIP_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 8, 2, 1, 13),
    _FextHMonHchkSrcIP_Type()
)
fextHMonHchkSrcIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextHMonHchkSrcIP.setStatus("current")
_FextHMonHchkFilter_Type = DisplayString
_FextHMonHchkFilter_Object = MibTableColumn
fextHMonHchkFilter = _FextHMonHchkFilter_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 8, 2, 1, 14),
    _FextHMonHchkFilter_Type()
)
fextHMonHchkFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextHMonHchkFilter.setStatus("current")
_FextSNMP_ObjectIdentity = ObjectIdentity
fextSNMP = _FextSNMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 9)
)
_FextSNMPSysInfo_ObjectIdentity = ObjectIdentity
fextSNMPSysInfo = _FextSNMPSysInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 9, 1)
)
if mibBuilder.loadTexts:
    fextSNMPSysInfo.setStatus("current")
_FextSNMPSysInfoStatus_Type = DisplayString
_FextSNMPSysInfoStatus_Object = MibScalar
fextSNMPSysInfoStatus = _FextSNMPSysInfoStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 9, 1, 1),
    _FextSNMPSysInfoStatus_Type()
)
fextSNMPSysInfoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextSNMPSysInfoStatus.setStatus("current")
_FextSNMPSysInfoDescription_Type = DisplayString
_FextSNMPSysInfoDescription_Object = MibScalar
fextSNMPSysInfoDescription = _FextSNMPSysInfoDescription_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 9, 1, 2),
    _FextSNMPSysInfoDescription_Type()
)
fextSNMPSysInfoDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextSNMPSysInfoDescription.setStatus("current")
_FextSNMPSysInfoContactInfo_Type = DisplayString
_FextSNMPSysInfoContactInfo_Object = MibScalar
fextSNMPSysInfoContactInfo = _FextSNMPSysInfoContactInfo_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 9, 1, 3),
    _FextSNMPSysInfoContactInfo_Type()
)
fextSNMPSysInfoContactInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextSNMPSysInfoContactInfo.setStatus("current")
_FextSNMPSysInfoLocation_Type = DisplayString
_FextSNMPSysInfoLocation_Object = MibScalar
fextSNMPSysInfoLocation = _FextSNMPSysInfoLocation_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 9, 1, 4),
    _FextSNMPSysInfoLocation_Type()
)
fextSNMPSysInfoLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextSNMPSysInfoLocation.setStatus("current")
_FextSNMPCommunity_Object = MibTable
fextSNMPCommunity = _FextSNMPCommunity_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 9, 2)
)
if mibBuilder.loadTexts:
    fextSNMPCommunity.setStatus("current")
_FextSNMPCommunityEntry_Object = MibTableRow
fextSNMPCommunityEntry = _FextSNMPCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 9, 2, 1)
)
fextSNMPCommunityEntry.setIndexNames(
    (0, "FORTINET-FORTIEXTENDER-MIB", "fextSNMPCommunityIndex"),
)
if mibBuilder.loadTexts:
    fextSNMPCommunityEntry.setStatus("current")
_FextSNMPCommunityIndex_Type = FnIndex
_FextSNMPCommunityIndex_Object = MibTableColumn
fextSNMPCommunityIndex = _FextSNMPCommunityIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 9, 2, 1, 1),
    _FextSNMPCommunityIndex_Type()
)
fextSNMPCommunityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fextSNMPCommunityIndex.setStatus("current")
_FextSNMPCommunityID_Type = DisplayString
_FextSNMPCommunityID_Object = MibTableColumn
fextSNMPCommunityID = _FextSNMPCommunityID_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 9, 2, 1, 2),
    _FextSNMPCommunityID_Type()
)
fextSNMPCommunityID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextSNMPCommunityID.setStatus("current")
_FextSNMPCommunityName_Type = DisplayString
_FextSNMPCommunityName_Object = MibTableColumn
fextSNMPCommunityName = _FextSNMPCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 9, 2, 1, 3),
    _FextSNMPCommunityName_Type()
)
fextSNMPCommunityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextSNMPCommunityName.setStatus("current")
_FextSNMPCommunityStatus_Type = DisplayString
_FextSNMPCommunityStatus_Object = MibTableColumn
fextSNMPCommunityStatus = _FextSNMPCommunityStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 9, 2, 1, 4),
    _FextSNMPCommunityStatus_Type()
)
fextSNMPCommunityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextSNMPCommunityStatus.setStatus("current")
_FextSNMPCommunityHosts_Type = DisplayString
_FextSNMPCommunityHosts_Object = MibTableColumn
fextSNMPCommunityHosts = _FextSNMPCommunityHosts_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 9, 2, 1, 5),
    _FextSNMPCommunityHosts_Type()
)
fextSNMPCommunityHosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextSNMPCommunityHosts.setStatus("current")
_FextSNMPCommunityQueryV1Status_Type = DisplayString
_FextSNMPCommunityQueryV1Status_Object = MibTableColumn
fextSNMPCommunityQueryV1Status = _FextSNMPCommunityQueryV1Status_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 9, 2, 1, 6),
    _FextSNMPCommunityQueryV1Status_Type()
)
fextSNMPCommunityQueryV1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextSNMPCommunityQueryV1Status.setStatus("current")
_FextSNMPCommunityQueryV1Port_Type = DisplayString
_FextSNMPCommunityQueryV1Port_Object = MibTableColumn
fextSNMPCommunityQueryV1Port = _FextSNMPCommunityQueryV1Port_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 9, 2, 1, 7),
    _FextSNMPCommunityQueryV1Port_Type()
)
fextSNMPCommunityQueryV1Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextSNMPCommunityQueryV1Port.setStatus("current")
_FextSNMPCommunityQueryV2CStatus_Type = DisplayString
_FextSNMPCommunityQueryV2CStatus_Object = MibTableColumn
fextSNMPCommunityQueryV2CStatus = _FextSNMPCommunityQueryV2CStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 9, 2, 1, 8),
    _FextSNMPCommunityQueryV2CStatus_Type()
)
fextSNMPCommunityQueryV2CStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextSNMPCommunityQueryV2CStatus.setStatus("current")
_FextSNMPCommunityQueryV2CPort_Type = DisplayString
_FextSNMPCommunityQueryV2CPort_Object = MibTableColumn
fextSNMPCommunityQueryV2CPort = _FextSNMPCommunityQueryV2CPort_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 9, 2, 1, 9),
    _FextSNMPCommunityQueryV2CPort_Type()
)
fextSNMPCommunityQueryV2CPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextSNMPCommunityQueryV2CPort.setStatus("current")
_FextSNMPCommunityTrapV1Status_Type = DisplayString
_FextSNMPCommunityTrapV1Status_Object = MibTableColumn
fextSNMPCommunityTrapV1Status = _FextSNMPCommunityTrapV1Status_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 9, 2, 1, 10),
    _FextSNMPCommunityTrapV1Status_Type()
)
fextSNMPCommunityTrapV1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextSNMPCommunityTrapV1Status.setStatus("current")
_FextSNMPCommunityTrapV1LPort_Type = DisplayString
_FextSNMPCommunityTrapV1LPort_Object = MibTableColumn
fextSNMPCommunityTrapV1LPort = _FextSNMPCommunityTrapV1LPort_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 9, 2, 1, 11),
    _FextSNMPCommunityTrapV1LPort_Type()
)
fextSNMPCommunityTrapV1LPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextSNMPCommunityTrapV1LPort.setStatus("current")
_FextSNMPCommunityTrapV1RPort_Type = DisplayString
_FextSNMPCommunityTrapV1RPort_Object = MibTableColumn
fextSNMPCommunityTrapV1RPort = _FextSNMPCommunityTrapV1RPort_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 9, 2, 1, 12),
    _FextSNMPCommunityTrapV1RPort_Type()
)
fextSNMPCommunityTrapV1RPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextSNMPCommunityTrapV1RPort.setStatus("current")
_FextSNMPCommunityTrapV2CStatus_Type = DisplayString
_FextSNMPCommunityTrapV2CStatus_Object = MibTableColumn
fextSNMPCommunityTrapV2CStatus = _FextSNMPCommunityTrapV2CStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 9, 2, 1, 13),
    _FextSNMPCommunityTrapV2CStatus_Type()
)
fextSNMPCommunityTrapV2CStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextSNMPCommunityTrapV2CStatus.setStatus("current")
_FextSNMPCommunityTrapV2CLPort_Type = DisplayString
_FextSNMPCommunityTrapV2CLPort_Object = MibTableColumn
fextSNMPCommunityTrapV2CLPort = _FextSNMPCommunityTrapV2CLPort_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 9, 2, 1, 14),
    _FextSNMPCommunityTrapV2CLPort_Type()
)
fextSNMPCommunityTrapV2CLPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextSNMPCommunityTrapV2CLPort.setStatus("current")
_FextSNMPCommunityTrapV2CRPort_Type = DisplayString
_FextSNMPCommunityTrapV2CRPort_Object = MibTableColumn
fextSNMPCommunityTrapV2CRPort = _FextSNMPCommunityTrapV2CRPort_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 9, 2, 1, 15),
    _FextSNMPCommunityTrapV2CRPort_Type()
)
fextSNMPCommunityTrapV2CRPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextSNMPCommunityTrapV2CRPort.setStatus("current")
_FextSNMPCommunityEvents_Type = DisplayString
_FextSNMPCommunityEvents_Object = MibTableColumn
fextSNMPCommunityEvents = _FextSNMPCommunityEvents_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 9, 2, 1, 16),
    _FextSNMPCommunityEvents_Type()
)
fextSNMPCommunityEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextSNMPCommunityEvents.setStatus("current")
_FextSNMPUser_Object = MibTable
fextSNMPUser = _FextSNMPUser_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 9, 3)
)
if mibBuilder.loadTexts:
    fextSNMPUser.setStatus("current")
_FextSNMPUserEntry_Object = MibTableRow
fextSNMPUserEntry = _FextSNMPUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 9, 3, 1)
)
fextSNMPUserEntry.setIndexNames(
    (0, "FORTINET-FORTIEXTENDER-MIB", "fextSNMPUserIndex"),
)
if mibBuilder.loadTexts:
    fextSNMPUserEntry.setStatus("current")
_FextSNMPUserIndex_Type = FnIndex
_FextSNMPUserIndex_Object = MibTableColumn
fextSNMPUserIndex = _FextSNMPUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 9, 3, 1, 1),
    _FextSNMPUserIndex_Type()
)
fextSNMPUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fextSNMPUserIndex.setStatus("current")
_FextSNMPUserID_Type = DisplayString
_FextSNMPUserID_Object = MibTableColumn
fextSNMPUserID = _FextSNMPUserID_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 9, 3, 1, 2),
    _FextSNMPUserID_Type()
)
fextSNMPUserID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextSNMPUserID.setStatus("current")
_FextSNMPUserName_Type = DisplayString
_FextSNMPUserName_Object = MibTableColumn
fextSNMPUserName = _FextSNMPUserName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 9, 3, 1, 3),
    _FextSNMPUserName_Type()
)
fextSNMPUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextSNMPUserName.setStatus("current")
_FextSNMPUserStatus_Type = DisplayString
_FextSNMPUserStatus_Object = MibTableColumn
fextSNMPUserStatus = _FextSNMPUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 9, 3, 1, 4),
    _FextSNMPUserStatus_Type()
)
fextSNMPUserStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextSNMPUserStatus.setStatus("current")
_FextSNMPUserNotifyHosts_Type = DisplayString
_FextSNMPUserNotifyHosts_Object = MibTableColumn
fextSNMPUserNotifyHosts = _FextSNMPUserNotifyHosts_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 9, 3, 1, 5),
    _FextSNMPUserNotifyHosts_Type()
)
fextSNMPUserNotifyHosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextSNMPUserNotifyHosts.setStatus("current")
_FextSNMPUserTrapStatus_Type = DisplayString
_FextSNMPUserTrapStatus_Object = MibTableColumn
fextSNMPUserTrapStatus = _FextSNMPUserTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 9, 3, 1, 6),
    _FextSNMPUserTrapStatus_Type()
)
fextSNMPUserTrapStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextSNMPUserTrapStatus.setStatus("current")
_FextSNMPUserTrapLPort_Type = DisplayString
_FextSNMPUserTrapLPort_Object = MibTableColumn
fextSNMPUserTrapLPort = _FextSNMPUserTrapLPort_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 9, 3, 1, 7),
    _FextSNMPUserTrapLPort_Type()
)
fextSNMPUserTrapLPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextSNMPUserTrapLPort.setStatus("current")
_FextSNMPUserTrapRPort_Type = DisplayString
_FextSNMPUserTrapRPort_Object = MibTableColumn
fextSNMPUserTrapRPort = _FextSNMPUserTrapRPort_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 9, 3, 1, 8),
    _FextSNMPUserTrapRPort_Type()
)
fextSNMPUserTrapRPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextSNMPUserTrapRPort.setStatus("current")
_FextSNMPUserQueryStatus_Type = DisplayString
_FextSNMPUserQueryStatus_Object = MibTableColumn
fextSNMPUserQueryStatus = _FextSNMPUserQueryStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 9, 3, 1, 9),
    _FextSNMPUserQueryStatus_Type()
)
fextSNMPUserQueryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextSNMPUserQueryStatus.setStatus("current")
_FextSNMPUserQueryPort_Type = DisplayString
_FextSNMPUserQueryPort_Object = MibTableColumn
fextSNMPUserQueryPort = _FextSNMPUserQueryPort_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 9, 3, 1, 10),
    _FextSNMPUserQueryPort_Type()
)
fextSNMPUserQueryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextSNMPUserQueryPort.setStatus("current")
_FextSNMPUserEvents_Type = DisplayString
_FextSNMPUserEvents_Object = MibTableColumn
fextSNMPUserEvents = _FextSNMPUserEvents_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 9, 3, 1, 11),
    _FextSNMPUserEvents_Type()
)
fextSNMPUserEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextSNMPUserEvents.setStatus("current")
_FextSNMPUserSecurityLevel_Type = DisplayString
_FextSNMPUserSecurityLevel_Object = MibTableColumn
fextSNMPUserSecurityLevel = _FextSNMPUserSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 9, 3, 1, 12),
    _FextSNMPUserSecurityLevel_Type()
)
fextSNMPUserSecurityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextSNMPUserSecurityLevel.setStatus("current")
_FextSNMPUserAuthProtocol_Type = DisplayString
_FextSNMPUserAuthProtocol_Object = MibTableColumn
fextSNMPUserAuthProtocol = _FextSNMPUserAuthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 9, 3, 1, 13),
    _FextSNMPUserAuthProtocol_Type()
)
fextSNMPUserAuthProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextSNMPUserAuthProtocol.setStatus("current")
_FextSNMPUserAuthPWD_Type = DisplayString
_FextSNMPUserAuthPWD_Object = MibTableColumn
fextSNMPUserAuthPWD = _FextSNMPUserAuthPWD_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 9, 3, 1, 14),
    _FextSNMPUserAuthPWD_Type()
)
fextSNMPUserAuthPWD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextSNMPUserAuthPWD.setStatus("current")
_FextSNMPUserPrivProtocol_Type = DisplayString
_FextSNMPUserPrivProtocol_Object = MibTableColumn
fextSNMPUserPrivProtocol = _FextSNMPUserPrivProtocol_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 9, 3, 1, 15),
    _FextSNMPUserPrivProtocol_Type()
)
fextSNMPUserPrivProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextSNMPUserPrivProtocol.setStatus("current")
_FextSNMPUserPrivPWD_Type = DisplayString
_FextSNMPUserPrivPWD_Object = MibTableColumn
fextSNMPUserPrivPWD = _FextSNMPUserPrivPWD_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 9, 3, 1, 16),
    _FextSNMPUserPrivPWD_Type()
)
fextSNMPUserPrivPWD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextSNMPUserPrivPWD.setStatus("current")
_FextSNMPHost_Object = MibTable
fextSNMPHost = _FextSNMPHost_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 9, 4)
)
if mibBuilder.loadTexts:
    fextSNMPHost.setStatus("current")
_FextSNMPHostEntry_Object = MibTableRow
fextSNMPHostEntry = _FextSNMPHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 9, 4, 1)
)
fextSNMPHostEntry.setIndexNames(
    (0, "FORTINET-FORTIEXTENDER-MIB", "fextSNMPHostIndex"),
)
if mibBuilder.loadTexts:
    fextSNMPHostEntry.setStatus("current")
_FextSNMPHostIndex_Type = FnIndex
_FextSNMPHostIndex_Object = MibTableColumn
fextSNMPHostIndex = _FextSNMPHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 9, 4, 1, 1),
    _FextSNMPHostIndex_Type()
)
fextSNMPHostIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fextSNMPHostIndex.setStatus("current")
_FextSNMPHostName_Type = DisplayString
_FextSNMPHostName_Object = MibTableColumn
fextSNMPHostName = _FextSNMPHostName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 9, 4, 1, 2),
    _FextSNMPHostName_Type()
)
fextSNMPHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextSNMPHostName.setStatus("current")
_FextSNMPHostIP_Type = DisplayString
_FextSNMPHostIP_Object = MibTableColumn
fextSNMPHostIP = _FextSNMPHostIP_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 9, 4, 1, 3),
    _FextSNMPHostIP_Type()
)
fextSNMPHostIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextSNMPHostIP.setStatus("current")
_FextSNMPHostType_Type = DisplayString
_FextSNMPHostType_Object = MibTableColumn
fextSNMPHostType = _FextSNMPHostType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 9, 4, 1, 4),
    _FextSNMPHostType_Type()
)
fextSNMPHostType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextSNMPHostType.setStatus("current")
_FextInfo_ObjectIdentity = ObjectIdentity
fextInfo = _FextInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21)
)
_FextInfoSystem_ObjectIdentity = ObjectIdentity
fextInfoSystem = _FextInfoSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 1)
)
_FextInfoVersion_ObjectIdentity = ObjectIdentity
fextInfoVersion = _FextInfoVersion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 1, 1)
)
if mibBuilder.loadTexts:
    fextInfoVersion.setStatus("current")
_FextInfoImage_Type = DisplayString
_FextInfoImage_Object = MibScalar
fextInfoImage = _FextInfoImage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 1, 1, 1),
    _FextInfoImage_Type()
)
fextInfoImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoImage.setStatus("current")
_FextInfoImageType_Type = DisplayString
_FextInfoImageType_Object = MibScalar
fextInfoImageType = _FextInfoImageType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 1, 1, 2),
    _FextInfoImageType_Type()
)
fextInfoImageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoImageType.setStatus("current")
_FextInfoModel_Type = DisplayString
_FextInfoModel_Object = MibScalar
fextInfoModel = _FextInfoModel_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 1, 1, 3),
    _FextInfoModel_Type()
)
fextInfoModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoModel.setStatus("current")
_FextInfoMAC_Type = DisplayString
_FextInfoMAC_Object = MibScalar
fextInfoMAC = _FextInfoMAC_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 1, 1, 4),
    _FextInfoMAC_Type()
)
fextInfoMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoMAC.setStatus("current")
_FextInfoSN_Type = DisplayString
_FextInfoSN_Object = MibScalar
fextInfoSN = _FextInfoSN_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 1, 1, 5),
    _FextInfoSN_Type()
)
fextInfoSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoSN.setStatus("current")
_FextInfoLicense_Type = DisplayString
_FextInfoLicense_Object = MibScalar
fextInfoLicense = _FextInfoLicense_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 1, 1, 6),
    _FextInfoLicense_Type()
)
fextInfoLicense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoLicense.setStatus("current")
_FextInfoOEMSN_Type = DisplayString
_FextInfoOEMSN_Object = MibScalar
fextInfoOEMSN = _FextInfoOEMSN_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 1, 1, 7),
    _FextInfoOEMSN_Type()
)
fextInfoOEMSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoOEMSN.setStatus("current")
_FextInfoREV_Type = DisplayString
_FextInfoREV_Object = MibScalar
fextInfoREV = _FextInfoREV_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 1, 1, 8),
    _FextInfoREV_Type()
)
fextInfoREV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoREV.setStatus("current")
_FextInfoVERSION_Type = DisplayString
_FextInfoVERSION_Object = MibScalar
fextInfoVERSION = _FextInfoVERSION_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 1, 1, 9),
    _FextInfoVERSION_Type()
)
fextInfoVERSION.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoVERSION.setStatus("current")
_FextInfoROMREV_Type = DisplayString
_FextInfoROMREV_Object = MibScalar
fextInfoROMREV = _FextInfoROMREV_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 1, 1, 10),
    _FextInfoROMREV_Type()
)
fextInfoROMREV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoROMREV.setStatus("current")
_FextInfoFallbackImage_Type = DisplayString
_FextInfoFallbackImage_Object = MibScalar
fextInfoFallbackImage = _FextInfoFallbackImage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 1, 1, 11),
    _FextInfoFallbackImage_Type()
)
fextInfoFallbackImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoFallbackImage.setStatus("current")
_FextInfoFallbackImageType_Type = DisplayString
_FextInfoFallbackImageType_Object = MibScalar
fextInfoFallbackImageType = _FextInfoFallbackImageType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 1, 1, 12),
    _FextInfoFallbackImageType_Type()
)
fextInfoFallbackImageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoFallbackImageType.setStatus("current")
_FextInfoStatus_ObjectIdentity = ObjectIdentity
fextInfoStatus = _FextInfoStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 1, 2)
)
if mibBuilder.loadTexts:
    fextInfoStatus.setStatus("current")
_FextInfoCPUUsage_Type = Integer32
_FextInfoCPUUsage_Object = MibScalar
fextInfoCPUUsage = _FextInfoCPUUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 1, 2, 1),
    _FextInfoCPUUsage_Type()
)
fextInfoCPUUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoCPUUsage.setStatus("current")
_FextInfoMemUsage_Type = Integer32
_FextInfoMemUsage_Object = MibScalar
fextInfoMemUsage = _FextInfoMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 1, 2, 2),
    _FextInfoMemUsage_Type()
)
fextInfoMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoMemUsage.setStatus("current")
_FextInfoUptime_Type = DisplayString
_FextInfoUptime_Object = MibScalar
fextInfoUptime = _FextInfoUptime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 1, 2, 3),
    _FextInfoUptime_Type()
)
fextInfoUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoUptime.setStatus("current")
_FextInfoInterface_Object = MibTable
fextInfoInterface = _FextInfoInterface_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 1, 3)
)
if mibBuilder.loadTexts:
    fextInfoInterface.setStatus("current")
_FextInfoInterfaceEntry_Object = MibTableRow
fextInfoInterfaceEntry = _FextInfoInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 1, 3, 1)
)
if mibBuilder.loadTexts:
    fextInfoInterfaceEntry.setStatus("current")
_FextInfoInterfaceName_Type = DisplayString
_FextInfoInterfaceName_Object = MibTableColumn
fextInfoInterfaceName = _FextInfoInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 1, 3, 1, 1),
    _FextInfoInterfaceName_Type()
)
fextInfoInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoInterfaceName.setStatus("current")
_FextInfoInterfaceStatus_Type = DisplayString
_FextInfoInterfaceStatus_Object = MibTableColumn
fextInfoInterfaceStatus = _FextInfoInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 1, 3, 1, 2),
    _FextInfoInterfaceStatus_Type()
)
fextInfoInterfaceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoInterfaceStatus.setStatus("current")
_FextInfoInterfaceType_Type = DisplayString
_FextInfoInterfaceType_Object = MibTableColumn
fextInfoInterfaceType = _FextInfoInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 1, 3, 1, 3),
    _FextInfoInterfaceType_Type()
)
fextInfoInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoInterfaceType.setStatus("current")
_FextInfoInterfaceMode_Type = DisplayString
_FextInfoInterfaceMode_Object = MibTableColumn
fextInfoInterfaceMode = _FextInfoInterfaceMode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 1, 3, 1, 4),
    _FextInfoInterfaceMode_Type()
)
fextInfoInterfaceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoInterfaceMode.setStatus("current")
_FextInfoInterfaceIP_Type = DisplayString
_FextInfoInterfaceIP_Object = MibTableColumn
fextInfoInterfaceIP = _FextInfoInterfaceIP_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 1, 3, 1, 5),
    _FextInfoInterfaceIP_Type()
)
fextInfoInterfaceIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoInterfaceIP.setStatus("current")
_FextInfoInterfaceGateway_Type = DisplayString
_FextInfoInterfaceGateway_Object = MibTableColumn
fextInfoInterfaceGateway = _FextInfoInterfaceGateway_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 1, 3, 1, 6),
    _FextInfoInterfaceGateway_Type()
)
fextInfoInterfaceGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoInterfaceGateway.setStatus("current")
_FextInfoDHCPServer_ObjectIdentity = ObjectIdentity
fextInfoDHCPServer = _FextInfoDHCPServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 1, 4)
)
if mibBuilder.loadTexts:
    fextInfoDHCPServer.setStatus("current")
_FextInfoDHCPServerConfig_Object = MibTable
fextInfoDHCPServerConfig = _FextInfoDHCPServerConfig_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 1, 4, 1)
)
if mibBuilder.loadTexts:
    fextInfoDHCPServerConfig.setStatus("current")
_FextInfoDHCPServerEntry_Object = MibTableRow
fextInfoDHCPServerEntry = _FextInfoDHCPServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 1, 4, 1, 1)
)
fextInfoDHCPServerEntry.setIndexNames(
    (0, "FORTINET-FORTIEXTENDER-MIB", "fextInfoDHCPServerIndex"),
)
if mibBuilder.loadTexts:
    fextInfoDHCPServerEntry.setStatus("current")
_FextInfoDHCPServerIndex_Type = FnIndex
_FextInfoDHCPServerIndex_Object = MibTableColumn
fextInfoDHCPServerIndex = _FextInfoDHCPServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 1, 4, 1, 1, 1),
    _FextInfoDHCPServerIndex_Type()
)
fextInfoDHCPServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fextInfoDHCPServerIndex.setStatus("current")
_FextInfoDHCPServerName_Type = DisplayString
_FextInfoDHCPServerName_Object = MibTableColumn
fextInfoDHCPServerName = _FextInfoDHCPServerName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 1, 4, 1, 1, 2),
    _FextInfoDHCPServerName_Type()
)
fextInfoDHCPServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoDHCPServerName.setStatus("current")
_FextInfoDHCPServerStatus_Type = DisplayString
_FextInfoDHCPServerStatus_Object = MibTableColumn
fextInfoDHCPServerStatus = _FextInfoDHCPServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 1, 4, 1, 1, 3),
    _FextInfoDHCPServerStatus_Type()
)
fextInfoDHCPServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoDHCPServerStatus.setStatus("current")


class _FextInfoDHCPServerLeaseTime_Type(Integer32):
    """Custom type fextInfoDHCPServerLeaseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 8640000),
    )


_FextInfoDHCPServerLeaseTime_Type.__name__ = "Integer32"
_FextInfoDHCPServerLeaseTime_Object = MibTableColumn
fextInfoDHCPServerLeaseTime = _FextInfoDHCPServerLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 1, 4, 1, 1, 4),
    _FextInfoDHCPServerLeaseTime_Type()
)
fextInfoDHCPServerLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoDHCPServerLeaseTime.setStatus("current")
_FextInfoDHCPServerInterface_Type = DisplayString
_FextInfoDHCPServerInterface_Object = MibTableColumn
fextInfoDHCPServerInterface = _FextInfoDHCPServerInterface_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 1, 4, 1, 1, 5),
    _FextInfoDHCPServerInterface_Type()
)
fextInfoDHCPServerInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoDHCPServerInterface.setStatus("current")
_FextInfoDHCPServerDNS_Type = DisplayString
_FextInfoDHCPServerDNS_Object = MibTableColumn
fextInfoDHCPServerDNS = _FextInfoDHCPServerDNS_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 1, 4, 1, 1, 6),
    _FextInfoDHCPServerDNS_Type()
)
fextInfoDHCPServerDNS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoDHCPServerDNS.setStatus("current")
_FextInfoDHCPServerDNSServer_Type = DisplayString
_FextInfoDHCPServerDNSServer_Object = MibTableColumn
fextInfoDHCPServerDNSServer = _FextInfoDHCPServerDNSServer_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 1, 4, 1, 1, 7),
    _FextInfoDHCPServerDNSServer_Type()
)
fextInfoDHCPServerDNSServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoDHCPServerDNSServer.setStatus("current")
_FextInfoDHCPServerNTP_Type = DisplayString
_FextInfoDHCPServerNTP_Object = MibTableColumn
fextInfoDHCPServerNTP = _FextInfoDHCPServerNTP_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 1, 4, 1, 1, 8),
    _FextInfoDHCPServerNTP_Type()
)
fextInfoDHCPServerNTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoDHCPServerNTP.setStatus("current")
_FextInfoDHCPServerNTPServer_Type = DisplayString
_FextInfoDHCPServerNTPServer_Object = MibTableColumn
fextInfoDHCPServerNTPServer = _FextInfoDHCPServerNTPServer_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 1, 4, 1, 1, 9),
    _FextInfoDHCPServerNTPServer_Type()
)
fextInfoDHCPServerNTPServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoDHCPServerNTPServer.setStatus("current")
_FextInfoDHCPServerGatewayIP_Type = DisplayString
_FextInfoDHCPServerGatewayIP_Object = MibTableColumn
fextInfoDHCPServerGatewayIP = _FextInfoDHCPServerGatewayIP_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 1, 4, 1, 1, 10),
    _FextInfoDHCPServerGatewayIP_Type()
)
fextInfoDHCPServerGatewayIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoDHCPServerGatewayIP.setStatus("current")
_FextInfoDHCPServerIPRange_Type = DisplayString
_FextInfoDHCPServerIPRange_Object = MibTableColumn
fextInfoDHCPServerIPRange = _FextInfoDHCPServerIPRange_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 1, 4, 1, 1, 11),
    _FextInfoDHCPServerIPRange_Type()
)
fextInfoDHCPServerIPRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoDHCPServerIPRange.setStatus("current")
_FextInfoDHCPServerNetmask_Type = DisplayString
_FextInfoDHCPServerNetmask_Object = MibTableColumn
fextInfoDHCPServerNetmask = _FextInfoDHCPServerNetmask_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 1, 4, 1, 1, 12),
    _FextInfoDHCPServerNetmask_Type()
)
fextInfoDHCPServerNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoDHCPServerNetmask.setStatus("current")
_FextInfoDHCPServerClient_Object = MibTable
fextInfoDHCPServerClient = _FextInfoDHCPServerClient_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 1, 4, 2)
)
if mibBuilder.loadTexts:
    fextInfoDHCPServerClient.setStatus("current")
_FextInfoDHCPServerClientEntry_Object = MibTableRow
fextInfoDHCPServerClientEntry = _FextInfoDHCPServerClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 1, 4, 2, 1)
)
fextInfoDHCPServerClientEntry.setIndexNames(
    (0, "FORTINET-FORTIEXTENDER-MIB", "fextInfoDHCPServerClientIndex"),
)
if mibBuilder.loadTexts:
    fextInfoDHCPServerClientEntry.setStatus("current")
_FextInfoDHCPServerClientIndex_Type = FnIndex
_FextInfoDHCPServerClientIndex_Object = MibTableColumn
fextInfoDHCPServerClientIndex = _FextInfoDHCPServerClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 1, 4, 2, 1, 1),
    _FextInfoDHCPServerClientIndex_Type()
)
fextInfoDHCPServerClientIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fextInfoDHCPServerClientIndex.setStatus("current")
_FextInfoDHCPServerClientMAC_Type = DisplayString
_FextInfoDHCPServerClientMAC_Object = MibTableColumn
fextInfoDHCPServerClientMAC = _FextInfoDHCPServerClientMAC_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 1, 4, 2, 1, 2),
    _FextInfoDHCPServerClientMAC_Type()
)
fextInfoDHCPServerClientMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoDHCPServerClientMAC.setStatus("current")
_FextInfoDHCPServerClientIP_Type = DisplayString
_FextInfoDHCPServerClientIP_Object = MibTableColumn
fextInfoDHCPServerClientIP = _FextInfoDHCPServerClientIP_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 1, 4, 2, 1, 3),
    _FextInfoDHCPServerClientIP_Type()
)
fextInfoDHCPServerClientIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoDHCPServerClientIP.setStatus("current")
_FextInfoDHCPServerClientHost_Type = DisplayString
_FextInfoDHCPServerClientHost_Object = MibTableColumn
fextInfoDHCPServerClientHost = _FextInfoDHCPServerClientHost_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 1, 4, 2, 1, 4),
    _FextInfoDHCPServerClientHost_Type()
)
fextInfoDHCPServerClientHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoDHCPServerClientHost.setStatus("current")
_FextInfoDHCPServerClientLeaseTime_Type = DisplayString
_FextInfoDHCPServerClientLeaseTime_Object = MibTableColumn
fextInfoDHCPServerClientLeaseTime = _FextInfoDHCPServerClientLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 1, 4, 2, 1, 5),
    _FextInfoDHCPServerClientLeaseTime_Type()
)
fextInfoDHCPServerClientLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoDHCPServerClientLeaseTime.setStatus("current")
_FextInfoDHCPClient_Object = MibTable
fextInfoDHCPClient = _FextInfoDHCPClient_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 1, 5)
)
if mibBuilder.loadTexts:
    fextInfoDHCPClient.setStatus("current")
_FextInfoDHCPClientEntry_Object = MibTableRow
fextInfoDHCPClientEntry = _FextInfoDHCPClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 1, 5, 1)
)
fextInfoDHCPClientEntry.setIndexNames(
    (0, "FORTINET-FORTIEXTENDER-MIB", "fextInfoDHCPClientIndex"),
)
if mibBuilder.loadTexts:
    fextInfoDHCPClientEntry.setStatus("current")
_FextInfoDHCPClientIndex_Type = FnIndex
_FextInfoDHCPClientIndex_Object = MibTableColumn
fextInfoDHCPClientIndex = _FextInfoDHCPClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 1, 5, 1, 1),
    _FextInfoDHCPClientIndex_Type()
)
fextInfoDHCPClientIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fextInfoDHCPClientIndex.setStatus("current")
_FextInfoDHCPClientInterface_Type = DisplayString
_FextInfoDHCPClientInterface_Object = MibTableColumn
fextInfoDHCPClientInterface = _FextInfoDHCPClientInterface_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 1, 5, 1, 2),
    _FextInfoDHCPClientInterface_Type()
)
fextInfoDHCPClientInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoDHCPClientInterface.setStatus("current")
_FextInfoDHCPClientIP_Type = DisplayString
_FextInfoDHCPClientIP_Object = MibTableColumn
fextInfoDHCPClientIP = _FextInfoDHCPClientIP_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 1, 5, 1, 3),
    _FextInfoDHCPClientIP_Type()
)
fextInfoDHCPClientIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoDHCPClientIP.setStatus("current")
_FextInfoDHCPClientNetmask_Type = DisplayString
_FextInfoDHCPClientNetmask_Object = MibTableColumn
fextInfoDHCPClientNetmask = _FextInfoDHCPClientNetmask_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 1, 5, 1, 4),
    _FextInfoDHCPClientNetmask_Type()
)
fextInfoDHCPClientNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoDHCPClientNetmask.setStatus("current")
_FextInfoDHCPClientGatewayIP_Type = DisplayString
_FextInfoDHCPClientGatewayIP_Object = MibTableColumn
fextInfoDHCPClientGatewayIP = _FextInfoDHCPClientGatewayIP_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 1, 5, 1, 5),
    _FextInfoDHCPClientGatewayIP_Type()
)
fextInfoDHCPClientGatewayIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoDHCPClientGatewayIP.setStatus("current")
_FextInfoDHCPClientDNSServer_Type = DisplayString
_FextInfoDHCPClientDNSServer_Object = MibTableColumn
fextInfoDHCPClientDNSServer = _FextInfoDHCPClientDNSServer_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 1, 5, 1, 6),
    _FextInfoDHCPClientDNSServer_Type()
)
fextInfoDHCPClientDNSServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoDHCPClientDNSServer.setStatus("current")


class _FextInfoDHCPClientLeaseTime_Type(Integer32):
    """Custom type fextInfoDHCPClientLeaseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 8640000),
    )


_FextInfoDHCPClientLeaseTime_Type.__name__ = "Integer32"
_FextInfoDHCPClientLeaseTime_Object = MibTableColumn
fextInfoDHCPClientLeaseTime = _FextInfoDHCPClientLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 1, 5, 1, 7),
    _FextInfoDHCPClientLeaseTime_Type()
)
fextInfoDHCPClientLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoDHCPClientLeaseTime.setStatus("current")


class _FextInfoDHCPClientLeftTime_Type(Integer32):
    """Custom type fextInfoDHCPClientLeftTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 8640000),
    )


_FextInfoDHCPClientLeftTime_Type.__name__ = "Integer32"
_FextInfoDHCPClientLeftTime_Object = MibTableColumn
fextInfoDHCPClientLeftTime = _FextInfoDHCPClientLeftTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 1, 5, 1, 8),
    _FextInfoDHCPClientLeftTime_Type()
)
fextInfoDHCPClientLeftTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoDHCPClientLeftTime.setStatus("current")
_FextInfoDNS_Object = MibTable
fextInfoDNS = _FextInfoDNS_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 1, 6)
)
if mibBuilder.loadTexts:
    fextInfoDNS.setStatus("current")
_FextInfoDNSEntry_Object = MibTableRow
fextInfoDNSEntry = _FextInfoDNSEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 1, 6, 1)
)
fextInfoDNSEntry.setIndexNames(
    (0, "FORTINET-FORTIEXTENDER-MIB", "fextInfoDNSIndex"),
)
if mibBuilder.loadTexts:
    fextInfoDNSEntry.setStatus("current")
_FextInfoDNSIndex_Type = FnIndex
_FextInfoDNSIndex_Object = MibTableColumn
fextInfoDNSIndex = _FextInfoDNSIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 1, 6, 1, 1),
    _FextInfoDNSIndex_Type()
)
fextInfoDNSIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fextInfoDNSIndex.setStatus("current")
_FextInfoDNSType_Type = DisplayString
_FextInfoDNSType_Object = MibTableColumn
fextInfoDNSType = _FextInfoDNSType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 1, 6, 1, 2),
    _FextInfoDNSType_Type()
)
fextInfoDNSType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoDNSType.setStatus("current")
_FextInfoDNSIP_Type = DisplayString
_FextInfoDNSIP_Object = MibTableColumn
fextInfoDNSIP = _FextInfoDNSIP_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 1, 6, 1, 3),
    _FextInfoDNSIP_Type()
)
fextInfoDNSIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoDNSIP.setStatus("current")
_FextInfoDNSInterface_Type = DisplayString
_FextInfoDNSInterface_Object = MibTableColumn
fextInfoDNSInterface = _FextInfoDNSInterface_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 1, 6, 1, 4),
    _FextInfoDNSInterface_Type()
)
fextInfoDNSInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoDNSInterface.setStatus("current")
_FextInfoExtender_ObjectIdentity = ObjectIdentity
fextInfoExtender = _FextInfoExtender_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 2)
)
_FextInfoEXTDStatus_ObjectIdentity = ObjectIdentity
fextInfoEXTDStatus = _FextInfoEXTDStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 2, 1)
)
if mibBuilder.loadTexts:
    fextInfoEXTDStatus.setStatus("current")
_FextInfoEXTDHostName_Type = DisplayString
_FextInfoEXTDHostName_Object = MibScalar
fextInfoEXTDHostName = _FextInfoEXTDHostName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 2, 1, 1),
    _FextInfoEXTDHostName_Type()
)
fextInfoEXTDHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoEXTDHostName.setStatus("current")
_FextInfoEXTDMode_Type = DisplayString
_FextInfoEXTDMode_Object = MibScalar
fextInfoEXTDMode = _FextInfoEXTDMode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 2, 1, 2),
    _FextInfoEXTDMode_Type()
)
fextInfoEXTDMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoEXTDMode.setStatus("current")
_FextInfoEXTDADDR_Type = DisplayString
_FextInfoEXTDADDR_Object = MibScalar
fextInfoEXTDADDR = _FextInfoEXTDADDR_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 2, 1, 3),
    _FextInfoEXTDADDR_Type()
)
fextInfoEXTDADDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoEXTDADDR.setStatus("current")
_FextInfoEXTDWANADDR_Type = DisplayString
_FextInfoEXTDWANADDR_Object = MibScalar
fextInfoEXTDWANADDR = _FextInfoEXTDWANADDR_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 2, 1, 4),
    _FextInfoEXTDWANADDR_Type()
)
fextInfoEXTDWANADDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoEXTDWANADDR.setStatus("current")
_FextInfoEXTDController_Type = DisplayString
_FextInfoEXTDController_Object = MibScalar
fextInfoEXTDController = _FextInfoEXTDController_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 2, 1, 5),
    _FextInfoEXTDController_Type()
)
fextInfoEXTDController.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoEXTDController.setStatus("current")
_FextInfoEXTDControllerName_Type = DisplayString
_FextInfoEXTDControllerName_Object = MibScalar
fextInfoEXTDControllerName = _FextInfoEXTDControllerName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 2, 1, 6),
    _FextInfoEXTDControllerName_Type()
)
fextInfoEXTDControllerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoEXTDControllerName.setStatus("current")
_FextInfoEXTDDeployed_Type = DisplayString
_FextInfoEXTDDeployed_Object = MibScalar
fextInfoEXTDDeployed = _FextInfoEXTDDeployed_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 2, 1, 7),
    _FextInfoEXTDDeployed_Type()
)
fextInfoEXTDDeployed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoEXTDDeployed.setStatus("current")
_FextInfoEXTDAccount_Type = Integer32
_FextInfoEXTDAccount_Object = MibScalar
fextInfoEXTDAccount = _FextInfoEXTDAccount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 2, 1, 8),
    _FextInfoEXTDAccount_Type()
)
fextInfoEXTDAccount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoEXTDAccount.setStatus("current")
_FextInfoEXTDUptime_Type = Integer32
_FextInfoEXTDUptime_Object = MibScalar
fextInfoEXTDUptime = _FextInfoEXTDUptime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 2, 1, 9),
    _FextInfoEXTDUptime_Type()
)
fextInfoEXTDUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoEXTDUptime.setStatus("current")
_FextInfoEXTDMGMTState_Type = DisplayString
_FextInfoEXTDMGMTState_Object = MibScalar
fextInfoEXTDMGMTState = _FextInfoEXTDMGMTState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 2, 1, 10),
    _FextInfoEXTDMGMTState_Type()
)
fextInfoEXTDMGMTState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoEXTDMGMTState.setStatus("current")
_FextInfoEXTDMAC_Type = DisplayString
_FextInfoEXTDMAC_Object = MibScalar
fextInfoEXTDMAC = _FextInfoEXTDMAC_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 2, 1, 11),
    _FextInfoEXTDMAC_Type()
)
fextInfoEXTDMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoEXTDMAC.setStatus("current")
_FextInfoEXTDNetworkMode_Type = DisplayString
_FextInfoEXTDNetworkMode_Object = MibScalar
fextInfoEXTDNetworkMode = _FextInfoEXTDNetworkMode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 2, 1, 12),
    _FextInfoEXTDNetworkMode_Type()
)
fextInfoEXTDNetworkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoEXTDNetworkMode.setStatus("current")
_FextInfoEXTDFGTBackupMode_Type = DisplayString
_FextInfoEXTDFGTBackupMode_Object = MibScalar
fextInfoEXTDFGTBackupMode = _FextInfoEXTDFGTBackupMode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 2, 1, 13),
    _FextInfoEXTDFGTBackupMode_Type()
)
fextInfoEXTDFGTBackupMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoEXTDFGTBackupMode.setStatus("current")
_FextInfoEXTDDiscoveryType_Type = DisplayString
_FextInfoEXTDDiscoveryType_Object = MibScalar
fextInfoEXTDDiscoveryType = _FextInfoEXTDDiscoveryType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 2, 1, 14),
    _FextInfoEXTDDiscoveryType_Type()
)
fextInfoEXTDDiscoveryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoEXTDDiscoveryType.setStatus("current")
_FextInfoEXTDDiscoveryInterval_Type = Integer32
_FextInfoEXTDDiscoveryInterval_Object = MibScalar
fextInfoEXTDDiscoveryInterval = _FextInfoEXTDDiscoveryInterval_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 2, 1, 15),
    _FextInfoEXTDDiscoveryInterval_Type()
)
fextInfoEXTDDiscoveryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoEXTDDiscoveryInterval.setStatus("current")
_FextInfoEXTDEchoInterval_Type = Integer32
_FextInfoEXTDEchoInterval_Object = MibScalar
fextInfoEXTDEchoInterval = _FextInfoEXTDEchoInterval_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 2, 1, 16),
    _FextInfoEXTDEchoInterval_Type()
)
fextInfoEXTDEchoInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoEXTDEchoInterval.setStatus("current")
_FextInfoEXTDReportInterval_Type = Integer32
_FextInfoEXTDReportInterval_Object = MibScalar
fextInfoEXTDReportInterval = _FextInfoEXTDReportInterval_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 2, 1, 17),
    _FextInfoEXTDReportInterval_Type()
)
fextInfoEXTDReportInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoEXTDReportInterval.setStatus("current")
_FextInfoEXTDStatsInterval_Type = Integer32
_FextInfoEXTDStatsInterval_Object = MibScalar
fextInfoEXTDStatsInterval = _FextInfoEXTDStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 2, 1, 18),
    _FextInfoEXTDStatsInterval_Type()
)
fextInfoEXTDStatsInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoEXTDStatsInterval.setStatus("current")
_FextInfoEXTDMDMFWServer_Type = DisplayString
_FextInfoEXTDMDMFWServer_Object = MibScalar
fextInfoEXTDMDMFWServer = _FextInfoEXTDMDMFWServer_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 2, 1, 19),
    _FextInfoEXTDMDMFWServer_Type()
)
fextInfoEXTDMDMFWServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoEXTDMDMFWServer.setStatus("current")
_FextInfoEXTDOSFWServer_Type = DisplayString
_FextInfoEXTDOSFWServer_Object = MibScalar
fextInfoEXTDOSFWServer = _FextInfoEXTDOSFWServer_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 2, 1, 20),
    _FextInfoEXTDOSFWServer_Type()
)
fextInfoEXTDOSFWServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoEXTDOSFWServer.setStatus("current")
_FextInfoModem_ObjectIdentity = ObjectIdentity
fextInfoModem = _FextInfoModem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 3)
)
_FextInfoModemStatus_Object = MibTable
fextInfoModemStatus = _FextInfoModemStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 3, 1)
)
if mibBuilder.loadTexts:
    fextInfoModemStatus.setStatus("current")
_FextInfoModemStatusEntry_Object = MibTableRow
fextInfoModemStatusEntry = _FextInfoModemStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 3, 1, 1)
)
fextInfoModemStatusEntry.setIndexNames(
    (0, "FORTINET-FORTIEXTENDER-MIB", "fextInfoModemStatusIndex"),
)
if mibBuilder.loadTexts:
    fextInfoModemStatusEntry.setStatus("current")
_FextInfoModemStatusIndex_Type = FnIndex
_FextInfoModemStatusIndex_Object = MibTableColumn
fextInfoModemStatusIndex = _FextInfoModemStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 3, 1, 1, 1),
    _FextInfoModemStatusIndex_Type()
)
fextInfoModemStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fextInfoModemStatusIndex.setStatus("current")
_FextInfoModemStatusModem_Type = DisplayString
_FextInfoModemStatusModem_Object = MibTableColumn
fextInfoModemStatusModem = _FextInfoModemStatusModem_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 3, 1, 1, 2),
    _FextInfoModemStatusModem_Type()
)
fextInfoModemStatusModem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoModemStatusModem.setStatus("current")
_FextInfoModemStatusUSBPath_Type = DisplayString
_FextInfoModemStatusUSBPath_Object = MibTableColumn
fextInfoModemStatusUSBPath = _FextInfoModemStatusUSBPath_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 3, 1, 1, 3),
    _FextInfoModemStatusUSBPath_Type()
)
fextInfoModemStatusUSBPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoModemStatusUSBPath.setStatus("current")
_FextInfoModemStatusVender_Type = DisplayString
_FextInfoModemStatusVender_Object = MibTableColumn
fextInfoModemStatusVender = _FextInfoModemStatusVender_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 3, 1, 1, 4),
    _FextInfoModemStatusVender_Type()
)
fextInfoModemStatusVender.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoModemStatusVender.setStatus("current")
_FextInfoModemStatusProduct_Type = DisplayString
_FextInfoModemStatusProduct_Object = MibTableColumn
fextInfoModemStatusProduct = _FextInfoModemStatusProduct_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 3, 1, 1, 5),
    _FextInfoModemStatusProduct_Type()
)
fextInfoModemStatusProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoModemStatusProduct.setStatus("current")
_FextInfoModemStatusModel_Type = DisplayString
_FextInfoModemStatusModel_Object = MibTableColumn
fextInfoModemStatusModel = _FextInfoModemStatusModel_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 3, 1, 1, 6),
    _FextInfoModemStatusModel_Type()
)
fextInfoModemStatusModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoModemStatusModel.setStatus("current")
_FextInfoModemStatusSIMSlot_Type = DisplayString
_FextInfoModemStatusSIMSlot_Object = MibTableColumn
fextInfoModemStatusSIMSlot = _FextInfoModemStatusSIMSlot_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 3, 1, 1, 7),
    _FextInfoModemStatusSIMSlot_Type()
)
fextInfoModemStatusSIMSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoModemStatusSIMSlot.setStatus("current")
_FextInfoModemStatusRevision_Type = DisplayString
_FextInfoModemStatusRevision_Object = MibTableColumn
fextInfoModemStatusRevision = _FextInfoModemStatusRevision_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 3, 1, 1, 8),
    _FextInfoModemStatusRevision_Type()
)
fextInfoModemStatusRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoModemStatusRevision.setStatus("current")
_FextInfoModemStatusIMEI_Type = DisplayString
_FextInfoModemStatusIMEI_Object = MibTableColumn
fextInfoModemStatusIMEI = _FextInfoModemStatusIMEI_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 3, 1, 1, 9),
    _FextInfoModemStatusIMEI_Type()
)
fextInfoModemStatusIMEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoModemStatusIMEI.setStatus("current")
_FextInfoModemStatusICCID_Type = DisplayString
_FextInfoModemStatusICCID_Object = MibTableColumn
fextInfoModemStatusICCID = _FextInfoModemStatusICCID_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 3, 1, 1, 10),
    _FextInfoModemStatusICCID_Type()
)
fextInfoModemStatusICCID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoModemStatusICCID.setStatus("current")
_FextInfoModemStatusIMSI_Type = DisplayString
_FextInfoModemStatusIMSI_Object = MibTableColumn
fextInfoModemStatusIMSI = _FextInfoModemStatusIMSI_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 3, 1, 1, 11),
    _FextInfoModemStatusIMSI_Type()
)
fextInfoModemStatusIMSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoModemStatusIMSI.setStatus("current")
_FextInfoModemStatusPinStatus_Type = DisplayString
_FextInfoModemStatusPinStatus_Object = MibTableColumn
fextInfoModemStatusPinStatus = _FextInfoModemStatusPinStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 3, 1, 1, 12),
    _FextInfoModemStatusPinStatus_Type()
)
fextInfoModemStatusPinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoModemStatusPinStatus.setStatus("current")
_FextInfoModemStatusPinCode_Type = DisplayString
_FextInfoModemStatusPinCode_Object = MibTableColumn
fextInfoModemStatusPinCode = _FextInfoModemStatusPinCode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 3, 1, 1, 13),
    _FextInfoModemStatusPinCode_Type()
)
fextInfoModemStatusPinCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoModemStatusPinCode.setStatus("current")
_FextInfoModemStatusCarrier_Type = DisplayString
_FextInfoModemStatusCarrier_Object = MibTableColumn
fextInfoModemStatusCarrier = _FextInfoModemStatusCarrier_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 3, 1, 1, 14),
    _FextInfoModemStatusCarrier_Type()
)
fextInfoModemStatusCarrier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoModemStatusCarrier.setStatus("current")
_FextInfoModemStatusAPN_Type = DisplayString
_FextInfoModemStatusAPN_Object = MibTableColumn
fextInfoModemStatusAPN = _FextInfoModemStatusAPN_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 3, 1, 1, 15),
    _FextInfoModemStatusAPN_Type()
)
fextInfoModemStatusAPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoModemStatusAPN.setStatus("current")
_FextInfoModemStatusService_Type = DisplayString
_FextInfoModemStatusService_Object = MibTableColumn
fextInfoModemStatusService = _FextInfoModemStatusService_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 3, 1, 1, 16),
    _FextInfoModemStatusService_Type()
)
fextInfoModemStatusService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoModemStatusService.setStatus("current")
_FextInfoModemStatusPhoneNumber_Type = DisplayString
_FextInfoModemStatusPhoneNumber_Object = MibTableColumn
fextInfoModemStatusPhoneNumber = _FextInfoModemStatusPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 3, 1, 1, 17),
    _FextInfoModemStatusPhoneNumber_Type()
)
fextInfoModemStatusPhoneNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoModemStatusPhoneNumber.setStatus("current")
_FextInfoModemStatusSIM1Pin_Type = DisplayString
_FextInfoModemStatusSIM1Pin_Object = MibTableColumn
fextInfoModemStatusSIM1Pin = _FextInfoModemStatusSIM1Pin_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 3, 1, 1, 18),
    _FextInfoModemStatusSIM1Pin_Type()
)
fextInfoModemStatusSIM1Pin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoModemStatusSIM1Pin.setStatus("current")
_FextInfoModemStatusSIM1Puk_Type = DisplayString
_FextInfoModemStatusSIM1Puk_Object = MibTableColumn
fextInfoModemStatusSIM1Puk = _FextInfoModemStatusSIM1Puk_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 3, 1, 1, 19),
    _FextInfoModemStatusSIM1Puk_Type()
)
fextInfoModemStatusSIM1Puk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoModemStatusSIM1Puk.setStatus("current")
_FextInfoModemStatusSIM2Pin_Type = DisplayString
_FextInfoModemStatusSIM2Pin_Object = MibTableColumn
fextInfoModemStatusSIM2Pin = _FextInfoModemStatusSIM2Pin_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 3, 1, 1, 20),
    _FextInfoModemStatusSIM2Pin_Type()
)
fextInfoModemStatusSIM2Pin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoModemStatusSIM2Pin.setStatus("current")
_FextInfoModemStatusSIM2Puk_Type = DisplayString
_FextInfoModemStatusSIM2Puk_Object = MibTableColumn
fextInfoModemStatusSIM2Puk = _FextInfoModemStatusSIM2Puk_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 3, 1, 1, 21),
    _FextInfoModemStatusSIM2Puk_Type()
)
fextInfoModemStatusSIM2Puk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoModemStatusSIM2Puk.setStatus("current")
_FextInfoModemStatusRSSI_Type = DisplayString
_FextInfoModemStatusRSSI_Object = MibTableColumn
fextInfoModemStatusRSSI = _FextInfoModemStatusRSSI_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 3, 1, 1, 22),
    _FextInfoModemStatusRSSI_Type()
)
fextInfoModemStatusRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoModemStatusRSSI.setStatus("current")
_FextInfoModemStatusSignalStrength_Type = DisplayString
_FextInfoModemStatusSignalStrength_Object = MibTableColumn
fextInfoModemStatusSignalStrength = _FextInfoModemStatusSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 3, 1, 1, 23),
    _FextInfoModemStatusSignalStrength_Type()
)
fextInfoModemStatusSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoModemStatusSignalStrength.setStatus("current")
_FextInfoModemStatusCAState_Type = DisplayString
_FextInfoModemStatusCAState_Object = MibTableColumn
fextInfoModemStatusCAState = _FextInfoModemStatusCAState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 3, 1, 1, 24),
    _FextInfoModemStatusCAState_Type()
)
fextInfoModemStatusCAState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoModemStatusCAState.setStatus("current")
_FextInfoModemStatusCellID_Type = DisplayString
_FextInfoModemStatusCellID_Object = MibTableColumn
fextInfoModemStatusCellID = _FextInfoModemStatusCellID_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 3, 1, 1, 25),
    _FextInfoModemStatusCellID_Type()
)
fextInfoModemStatusCellID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoModemStatusCellID.setStatus("current")
_FextInfoModemStatusBand_Type = DisplayString
_FextInfoModemStatusBand_Object = MibTableColumn
fextInfoModemStatusBand = _FextInfoModemStatusBand_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 3, 1, 1, 26),
    _FextInfoModemStatusBand_Type()
)
fextInfoModemStatusBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoModemStatusBand.setStatus("current")
_FextInfoModemStatusBandwidth_Type = DisplayString
_FextInfoModemStatusBandwidth_Object = MibTableColumn
fextInfoModemStatusBandwidth = _FextInfoModemStatusBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 3, 1, 1, 27),
    _FextInfoModemStatusBandwidth_Type()
)
fextInfoModemStatusBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoModemStatusBandwidth.setStatus("current")
_FextInfoModemStatusSINR_Type = DisplayString
_FextInfoModemStatusSINR_Object = MibTableColumn
fextInfoModemStatusSINR = _FextInfoModemStatusSINR_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 3, 1, 1, 28),
    _FextInfoModemStatusSINR_Type()
)
fextInfoModemStatusSINR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoModemStatusSINR.setStatus("current")
_FextInfoModemStatusRSRP_Type = DisplayString
_FextInfoModemStatusRSRP_Object = MibTableColumn
fextInfoModemStatusRSRP = _FextInfoModemStatusRSRP_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 3, 1, 1, 29),
    _FextInfoModemStatusRSRP_Type()
)
fextInfoModemStatusRSRP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoModemStatusRSRP.setStatus("current")
_FextInfoModemStatusRSRQ_Type = DisplayString
_FextInfoModemStatusRSRQ_Object = MibTableColumn
fextInfoModemStatusRSRQ = _FextInfoModemStatusRSRQ_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 3, 1, 1, 30),
    _FextInfoModemStatusRSRQ_Type()
)
fextInfoModemStatusRSRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoModemStatusRSRQ.setStatus("current")
_FextInfoModemStatusPlanName_Type = DisplayString
_FextInfoModemStatusPlanName_Object = MibTableColumn
fextInfoModemStatusPlanName = _FextInfoModemStatusPlanName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 3, 1, 1, 31),
    _FextInfoModemStatusPlanName_Type()
)
fextInfoModemStatusPlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoModemStatusPlanName.setStatus("current")
_FextInfoModemStatusConnectStatus_Type = DisplayString
_FextInfoModemStatusConnectStatus_Object = MibTableColumn
fextInfoModemStatusConnectStatus = _FextInfoModemStatusConnectStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 3, 1, 1, 32),
    _FextInfoModemStatusConnectStatus_Type()
)
fextInfoModemStatusConnectStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoModemStatusConnectStatus.setStatus("current")
_FextInfoModemStatusReconnectCount_Type = Integer32
_FextInfoModemStatusReconnectCount_Object = MibTableColumn
fextInfoModemStatusReconnectCount = _FextInfoModemStatusReconnectCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 3, 1, 1, 33),
    _FextInfoModemStatusReconnectCount_Type()
)
fextInfoModemStatusReconnectCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoModemStatusReconnectCount.setStatus("current")
_FextInfoModemStatusSmartSIMSwitch_Type = DisplayString
_FextInfoModemStatusSmartSIMSwitch_Object = MibTableColumn
fextInfoModemStatusSmartSIMSwitch = _FextInfoModemStatusSmartSIMSwitch_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 3, 1, 1, 34),
    _FextInfoModemStatusSmartSIMSwitch_Type()
)
fextInfoModemStatusSmartSIMSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoModemStatusSmartSIMSwitch.setStatus("current")
_FextInfoModemStatusUptime_Type = DisplayString
_FextInfoModemStatusUptime_Object = MibTableColumn
fextInfoModemStatusUptime = _FextInfoModemStatusUptime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 3, 1, 1, 35),
    _FextInfoModemStatusUptime_Type()
)
fextInfoModemStatusUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoModemStatusUptime.setStatus("current")
_FextInfoModemStatusClock_Type = DisplayString
_FextInfoModemStatusClock_Object = MibTableColumn
fextInfoModemStatusClock = _FextInfoModemStatusClock_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 3, 1, 1, 36),
    _FextInfoModemStatusClock_Type()
)
fextInfoModemStatusClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoModemStatusClock.setStatus("current")
_FextInfoModemStatusTemperature_Type = DisplayString
_FextInfoModemStatusTemperature_Object = MibTableColumn
fextInfoModemStatusTemperature = _FextInfoModemStatusTemperature_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 3, 1, 1, 37),
    _FextInfoModemStatusTemperature_Type()
)
fextInfoModemStatusTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoModemStatusTemperature.setStatus("current")
_FextInfoModemStatusActivateStatus_Type = DisplayString
_FextInfoModemStatusActivateStatus_Object = MibTableColumn
fextInfoModemStatusActivateStatus = _FextInfoModemStatusActivateStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 3, 1, 1, 38),
    _FextInfoModemStatusActivateStatus_Type()
)
fextInfoModemStatusActivateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoModemStatusActivateStatus.setStatus("current")
_FextInfoModemStatusRoamingStatus_Type = DisplayString
_FextInfoModemStatusRoamingStatus_Object = MibTableColumn
fextInfoModemStatusRoamingStatus = _FextInfoModemStatusRoamingStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 3, 1, 1, 39),
    _FextInfoModemStatusRoamingStatus_Type()
)
fextInfoModemStatusRoamingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoModemStatusRoamingStatus.setStatus("current")
_FextInfoModemStatusLatitude_Type = DisplayString
_FextInfoModemStatusLatitude_Object = MibTableColumn
fextInfoModemStatusLatitude = _FextInfoModemStatusLatitude_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 3, 1, 1, 40),
    _FextInfoModemStatusLatitude_Type()
)
fextInfoModemStatusLatitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoModemStatusLatitude.setStatus("current")
_FextInfoModemStatusLongitude_Type = DisplayString
_FextInfoModemStatusLongitude_Object = MibTableColumn
fextInfoModemStatusLongitude = _FextInfoModemStatusLongitude_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 3, 1, 1, 41),
    _FextInfoModemStatusLongitude_Type()
)
fextInfoModemStatusLongitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoModemStatusLongitude.setStatus("current")
_FextInfoModemFWVersion_ObjectIdentity = ObjectIdentity
fextInfoModemFWVersion = _FextInfoModemFWVersion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 3, 2)
)
if mibBuilder.loadTexts:
    fextInfoModemFWVersion.setStatus("current")
_FextInfoModemFWVersionVersion_Type = DisplayString
_FextInfoModemFWVersionVersion_Object = MibScalar
fextInfoModemFWVersionVersion = _FextInfoModemFWVersionVersion_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 3, 2, 1),
    _FextInfoModemFWVersionVersion_Type()
)
fextInfoModemFWVersionVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoModemFWVersionVersion.setStatus("current")
_FextInfoModemDataUsage_Object = MibTable
fextInfoModemDataUsage = _FextInfoModemDataUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 3, 3)
)
if mibBuilder.loadTexts:
    fextInfoModemDataUsage.setStatus("current")
_FextInfoModemDataUsageEntry_Object = MibTableRow
fextInfoModemDataUsageEntry = _FextInfoModemDataUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 3, 3, 1)
)
fextInfoModemDataUsageEntry.setIndexNames(
    (0, "FORTINET-FORTIEXTENDER-MIB", "fextInfoModemDataUsageIndex"),
)
if mibBuilder.loadTexts:
    fextInfoModemDataUsageEntry.setStatus("current")
_FextInfoModemDataUsageIndex_Type = FnIndex
_FextInfoModemDataUsageIndex_Object = MibTableColumn
fextInfoModemDataUsageIndex = _FextInfoModemDataUsageIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 3, 3, 1, 1),
    _FextInfoModemDataUsageIndex_Type()
)
fextInfoModemDataUsageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fextInfoModemDataUsageIndex.setStatus("current")
_FextInfoModemDataUsageModem_Type = DisplayString
_FextInfoModemDataUsageModem_Object = MibTableColumn
fextInfoModemDataUsageModem = _FextInfoModemDataUsageModem_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 3, 3, 1, 2),
    _FextInfoModemDataUsageModem_Type()
)
fextInfoModemDataUsageModem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoModemDataUsageModem.setStatus("current")
_FextInfoModemDataUsageSlot_Type = Integer32
_FextInfoModemDataUsageSlot_Object = MibTableColumn
fextInfoModemDataUsageSlot = _FextInfoModemDataUsageSlot_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 3, 3, 1, 3),
    _FextInfoModemDataUsageSlot_Type()
)
fextInfoModemDataUsageSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoModemDataUsageSlot.setStatus("current")
_FextInfoModemDataUsageCarrier_Type = DisplayString
_FextInfoModemDataUsageCarrier_Object = MibTableColumn
fextInfoModemDataUsageCarrier = _FextInfoModemDataUsageCarrier_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 3, 3, 1, 4),
    _FextInfoModemDataUsageCarrier_Type()
)
fextInfoModemDataUsageCarrier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoModemDataUsageCarrier.setStatus("current")
_FextInfoModemDataUsageIMSI_Type = DisplayString
_FextInfoModemDataUsageIMSI_Object = MibTableColumn
fextInfoModemDataUsageIMSI = _FextInfoModemDataUsageIMSI_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 3, 3, 1, 5),
    _FextInfoModemDataUsageIMSI_Type()
)
fextInfoModemDataUsageIMSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoModemDataUsageIMSI.setStatus("current")
_FextInfoModemDataUsageMB_Type = Integer32
_FextInfoModemDataUsageMB_Object = MibTableColumn
fextInfoModemDataUsageMB = _FextInfoModemDataUsageMB_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 3, 3, 1, 6),
    _FextInfoModemDataUsageMB_Type()
)
fextInfoModemDataUsageMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoModemDataUsageMB.setStatus("current")
_FextInfoModemDataUsagePercentage_Type = DisplayString
_FextInfoModemDataUsagePercentage_Object = MibTableColumn
fextInfoModemDataUsagePercentage = _FextInfoModemDataUsagePercentage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 3, 3, 1, 7),
    _FextInfoModemDataUsagePercentage_Type()
)
fextInfoModemDataUsagePercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoModemDataUsagePercentage.setStatus("current")
_FextInfoModemDataUsageDataPlan_Type = Integer32
_FextInfoModemDataUsageDataPlan_Object = MibTableColumn
fextInfoModemDataUsageDataPlan = _FextInfoModemDataUsageDataPlan_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 3, 3, 1, 8),
    _FextInfoModemDataUsageDataPlan_Type()
)
fextInfoModemDataUsageDataPlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoModemDataUsageDataPlan.setStatus("current")
_FextInfoModemDataUsageOverage_Type = DisplayString
_FextInfoModemDataUsageOverage_Object = MibTableColumn
fextInfoModemDataUsageOverage = _FextInfoModemDataUsageOverage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 3, 3, 1, 9),
    _FextInfoModemDataUsageOverage_Type()
)
fextInfoModemDataUsageOverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoModemDataUsageOverage.setStatus("current")
_FextInfoModemDataUsageNextBillDate_Type = DisplayString
_FextInfoModemDataUsageNextBillDate_Object = MibTableColumn
fextInfoModemDataUsageNextBillDate = _FextInfoModemDataUsageNextBillDate_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 3, 3, 1, 10),
    _FextInfoModemDataUsageNextBillDate_Type()
)
fextInfoModemDataUsageNextBillDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoModemDataUsageNextBillDate.setStatus("current")
_FextInfoRouter_ObjectIdentity = ObjectIdentity
fextInfoRouter = _FextInfoRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4)
)
_FextInfoRouterRoute_Object = MibTable
fextInfoRouterRoute = _FextInfoRouterRoute_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 1)
)
if mibBuilder.loadTexts:
    fextInfoRouterRoute.setStatus("current")
_FextInfoRouterRouteEntry_Object = MibTableRow
fextInfoRouterRouteEntry = _FextInfoRouterRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 1, 1)
)
fextInfoRouterRouteEntry.setIndexNames(
    (0, "FORTINET-FORTIEXTENDER-MIB", "fextInfoRouterRouteIndex"),
)
if mibBuilder.loadTexts:
    fextInfoRouterRouteEntry.setStatus("current")
_FextInfoRouterRouteIndex_Type = FnIndex
_FextInfoRouterRouteIndex_Object = MibTableColumn
fextInfoRouterRouteIndex = _FextInfoRouterRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 1, 1, 1),
    _FextInfoRouterRouteIndex_Type()
)
fextInfoRouterRouteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fextInfoRouterRouteIndex.setStatus("current")
_FextInfoRouterRouteType_Type = DisplayString
_FextInfoRouterRouteType_Object = MibTableColumn
fextInfoRouterRouteType = _FextInfoRouterRouteType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 1, 1, 2),
    _FextInfoRouterRouteType_Type()
)
fextInfoRouterRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoRouterRouteType.setStatus("current")
_FextInfoRouterRouteDst_Type = DisplayString
_FextInfoRouterRouteDst_Object = MibTableColumn
fextInfoRouterRouteDst = _FextInfoRouterRouteDst_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 1, 1, 3),
    _FextInfoRouterRouteDst_Type()
)
fextInfoRouterRouteDst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoRouterRouteDst.setStatus("current")
_FextInfoRouterRouteGW_Type = DisplayString
_FextInfoRouterRouteGW_Object = MibTableColumn
fextInfoRouterRouteGW = _FextInfoRouterRouteGW_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 1, 1, 4),
    _FextInfoRouterRouteGW_Type()
)
fextInfoRouterRouteGW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoRouterRouteGW.setStatus("current")
_FextInfoRouterRouteHelp_Type = DisplayString
_FextInfoRouterRouteHelp_Object = MibTableColumn
fextInfoRouterRouteHelp = _FextInfoRouterRouteHelp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 1, 1, 5),
    _FextInfoRouterRouteHelp_Type()
)
fextInfoRouterRouteHelp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoRouterRouteHelp.setStatus("current")
_FextInfoRouterRouteDev_Type = DisplayString
_FextInfoRouterRouteDev_Object = MibTableColumn
fextInfoRouterRouteDev = _FextInfoRouterRouteDev_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 1, 1, 6),
    _FextInfoRouterRouteDev_Type()
)
fextInfoRouterRouteDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoRouterRouteDev.setStatus("current")
_FextInfoRouterPolicy_Object = MibTable
fextInfoRouterPolicy = _FextInfoRouterPolicy_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 2)
)
if mibBuilder.loadTexts:
    fextInfoRouterPolicy.setStatus("current")
_FextInfoRouterPolicyEntry_Object = MibTableRow
fextInfoRouterPolicyEntry = _FextInfoRouterPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 2, 1)
)
fextInfoRouterPolicyEntry.setIndexNames(
    (0, "FORTINET-FORTIEXTENDER-MIB", "fextInfoRouterPolicyIndex"),
)
if mibBuilder.loadTexts:
    fextInfoRouterPolicyEntry.setStatus("current")
_FextInfoRouterPolicyIndex_Type = FnIndex
_FextInfoRouterPolicyIndex_Object = MibTableColumn
fextInfoRouterPolicyIndex = _FextInfoRouterPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 2, 1, 1),
    _FextInfoRouterPolicyIndex_Type()
)
fextInfoRouterPolicyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fextInfoRouterPolicyIndex.setStatus("current")
_FextInfoRouterPolicySeq_Type = Integer32
_FextInfoRouterPolicySeq_Object = MibTableColumn
fextInfoRouterPolicySeq = _FextInfoRouterPolicySeq_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 2, 1, 2),
    _FextInfoRouterPolicySeq_Type()
)
fextInfoRouterPolicySeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoRouterPolicySeq.setStatus("current")
_FextInfoRouterPolicyStatus_Type = DisplayString
_FextInfoRouterPolicyStatus_Object = MibTableColumn
fextInfoRouterPolicyStatus = _FextInfoRouterPolicyStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 2, 1, 3),
    _FextInfoRouterPolicyStatus_Type()
)
fextInfoRouterPolicyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoRouterPolicyStatus.setStatus("current")
_FextInfoRouterPolicyInputIntf_Type = DisplayString
_FextInfoRouterPolicyInputIntf_Object = MibTableColumn
fextInfoRouterPolicyInputIntf = _FextInfoRouterPolicyInputIntf_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 2, 1, 4),
    _FextInfoRouterPolicyInputIntf_Type()
)
fextInfoRouterPolicyInputIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoRouterPolicyInputIntf.setStatus("current")
_FextInfoRouterPolicySrc_Type = DisplayString
_FextInfoRouterPolicySrc_Object = MibTableColumn
fextInfoRouterPolicySrc = _FextInfoRouterPolicySrc_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 2, 1, 5),
    _FextInfoRouterPolicySrc_Type()
)
fextInfoRouterPolicySrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoRouterPolicySrc.setStatus("current")
_FextInfoRouterPolicySrcAddr_Type = DisplayString
_FextInfoRouterPolicySrcAddr_Object = MibTableColumn
fextInfoRouterPolicySrcAddr = _FextInfoRouterPolicySrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 2, 1, 6),
    _FextInfoRouterPolicySrcAddr_Type()
)
fextInfoRouterPolicySrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoRouterPolicySrcAddr.setStatus("current")
_FextInfoRouterPolicyDst_Type = DisplayString
_FextInfoRouterPolicyDst_Object = MibTableColumn
fextInfoRouterPolicyDst = _FextInfoRouterPolicyDst_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 2, 1, 7),
    _FextInfoRouterPolicyDst_Type()
)
fextInfoRouterPolicyDst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoRouterPolicyDst.setStatus("current")
_FextInfoRouterPolicyDstAddr_Type = DisplayString
_FextInfoRouterPolicyDstAddr_Object = MibTableColumn
fextInfoRouterPolicyDstAddr = _FextInfoRouterPolicyDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 2, 1, 8),
    _FextInfoRouterPolicyDstAddr_Type()
)
fextInfoRouterPolicyDstAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoRouterPolicyDstAddr.setStatus("current")
_FextInfoRouterPolicyService_Type = DisplayString
_FextInfoRouterPolicyService_Object = MibTableColumn
fextInfoRouterPolicyService = _FextInfoRouterPolicyService_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 2, 1, 9),
    _FextInfoRouterPolicyService_Type()
)
fextInfoRouterPolicyService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoRouterPolicyService.setStatus("current")
_FextInfoRouterPolicyTarget_Type = DisplayString
_FextInfoRouterPolicyTarget_Object = MibTableColumn
fextInfoRouterPolicyTarget = _FextInfoRouterPolicyTarget_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 2, 1, 10),
    _FextInfoRouterPolicyTarget_Type()
)
fextInfoRouterPolicyTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoRouterPolicyTarget.setStatus("current")
_FextInfoRouterPolicyRoutingTable_Type = DisplayString
_FextInfoRouterPolicyRoutingTable_Object = MibTableColumn
fextInfoRouterPolicyRoutingTable = _FextInfoRouterPolicyRoutingTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 2, 1, 11),
    _FextInfoRouterPolicyRoutingTable_Type()
)
fextInfoRouterPolicyRoutingTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoRouterPolicyRoutingTable.setStatus("current")
_FextInfoRouterPolicyComment_Type = DisplayString
_FextInfoRouterPolicyComment_Object = MibTableColumn
fextInfoRouterPolicyComment = _FextInfoRouterPolicyComment_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 2, 1, 12),
    _FextInfoRouterPolicyComment_Type()
)
fextInfoRouterPolicyComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoRouterPolicyComment.setStatus("current")
_FextInfoRouterTarget_Object = MibTable
fextInfoRouterTarget = _FextInfoRouterTarget_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 3)
)
if mibBuilder.loadTexts:
    fextInfoRouterTarget.setStatus("current")
_FextInfoRouterTargetEntry_Object = MibTableRow
fextInfoRouterTargetEntry = _FextInfoRouterTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 3, 1)
)
fextInfoRouterTargetEntry.setIndexNames(
    (0, "FORTINET-FORTIEXTENDER-MIB", "fextInfoRouterTargetIndex"),
)
if mibBuilder.loadTexts:
    fextInfoRouterTargetEntry.setStatus("current")
_FextInfoRouterTargetIndex_Type = FnIndex
_FextInfoRouterTargetIndex_Object = MibTableColumn
fextInfoRouterTargetIndex = _FextInfoRouterTargetIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 3, 1, 1),
    _FextInfoRouterTargetIndex_Type()
)
fextInfoRouterTargetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fextInfoRouterTargetIndex.setStatus("current")
_FextInfoRouterTargetStatus_Type = DisplayString
_FextInfoRouterTargetStatus_Object = MibTableColumn
fextInfoRouterTargetStatus = _FextInfoRouterTargetStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 3, 1, 2),
    _FextInfoRouterTargetStatus_Type()
)
fextInfoRouterTargetStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoRouterTargetStatus.setStatus("current")
_FextInfoRouterTargetDevice_Type = DisplayString
_FextInfoRouterTargetDevice_Object = MibTableColumn
fextInfoRouterTargetDevice = _FextInfoRouterTargetDevice_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 3, 1, 3),
    _FextInfoRouterTargetDevice_Type()
)
fextInfoRouterTargetDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoRouterTargetDevice.setStatus("current")
_FextInfoRouterTargetDevStatus_Type = DisplayString
_FextInfoRouterTargetDevStatus_Object = MibTableColumn
fextInfoRouterTargetDevStatus = _FextInfoRouterTargetDevStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 3, 1, 4),
    _FextInfoRouterTargetDevStatus_Type()
)
fextInfoRouterTargetDevStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoRouterTargetDevStatus.setStatus("current")
_FextInfoRouterTargetNextHop_Type = DisplayString
_FextInfoRouterTargetNextHop_Object = MibTableColumn
fextInfoRouterTargetNextHop = _FextInfoRouterTargetNextHop_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 3, 1, 5),
    _FextInfoRouterTargetNextHop_Type()
)
fextInfoRouterTargetNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoRouterTargetNextHop.setStatus("current")
_FextInfoRouterTargetNHStatus_Type = DisplayString
_FextInfoRouterTargetNHStatus_Object = MibTableColumn
fextInfoRouterTargetNHStatus = _FextInfoRouterTargetNHStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 3, 1, 6),
    _FextInfoRouterTargetNHStatus_Type()
)
fextInfoRouterTargetNHStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoRouterTargetNHStatus.setStatus("current")
_FextInfoRouterTargetRouteType_Type = DisplayString
_FextInfoRouterTargetRouteType_Object = MibTableColumn
fextInfoRouterTargetRouteType = _FextInfoRouterTargetRouteType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 3, 1, 7),
    _FextInfoRouterTargetRouteType_Type()
)
fextInfoRouterTargetRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoRouterTargetRouteType.setStatus("current")
_FextInfoRouterTargetRoutingTable_Type = DisplayString
_FextInfoRouterTargetRoutingTable_Object = MibTableColumn
fextInfoRouterTargetRoutingTable = _FextInfoRouterTargetRoutingTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 3, 1, 8),
    _FextInfoRouterTargetRoutingTable_Type()
)
fextInfoRouterTargetRoutingTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoRouterTargetRoutingTable.setStatus("current")
_FextInfoRouterTargetRefCounter_Type = Integer32
_FextInfoRouterTargetRefCounter_Object = MibTableColumn
fextInfoRouterTargetRefCounter = _FextInfoRouterTargetRefCounter_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 3, 1, 9),
    _FextInfoRouterTargetRefCounter_Type()
)
fextInfoRouterTargetRefCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoRouterTargetRefCounter.setStatus("current")
_FextInfoRouterMulticast_ObjectIdentity = ObjectIdentity
fextInfoRouterMulticast = _FextInfoRouterMulticast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 4)
)
if mibBuilder.loadTexts:
    fextInfoRouterMulticast.setStatus("current")
_FextInfoMcastPIMSM_ObjectIdentity = ObjectIdentity
fextInfoMcastPIMSM = _FextInfoMcastPIMSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 4, 1)
)
if mibBuilder.loadTexts:
    fextInfoMcastPIMSM.setStatus("current")
_FextInfoPIMSMVIF_Object = MibTable
fextInfoPIMSMVIF = _FextInfoPIMSMVIF_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 4, 1, 1)
)
if mibBuilder.loadTexts:
    fextInfoPIMSMVIF.setStatus("current")
_FextInfoPIMSMVIFEntry_Object = MibTableRow
fextInfoPIMSMVIFEntry = _FextInfoPIMSMVIFEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 4, 1, 1, 1)
)
fextInfoPIMSMVIFEntry.setIndexNames(
    (0, "FORTINET-FORTIEXTENDER-MIB", "fextInfoPIMSMVIFIndex"),
)
if mibBuilder.loadTexts:
    fextInfoPIMSMVIFEntry.setStatus("current")
_FextInfoPIMSMVIFIndex_Type = FnIndex
_FextInfoPIMSMVIFIndex_Object = MibTableColumn
fextInfoPIMSMVIFIndex = _FextInfoPIMSMVIFIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 4, 1, 1, 1, 1),
    _FextInfoPIMSMVIFIndex_Type()
)
fextInfoPIMSMVIFIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fextInfoPIMSMVIFIndex.setStatus("current")
_FextInfoPIMSMVIFName_Type = DisplayString
_FextInfoPIMSMVIFName_Object = MibTableColumn
fextInfoPIMSMVIFName = _FextInfoPIMSMVIFName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 4, 1, 1, 1, 2),
    _FextInfoPIMSMVIFName_Type()
)
fextInfoPIMSMVIFName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoPIMSMVIFName.setStatus("current")
_FextInfoPIMSMVIFAddress_Type = DisplayString
_FextInfoPIMSMVIFAddress_Object = MibTableColumn
fextInfoPIMSMVIFAddress = _FextInfoPIMSMVIFAddress_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 4, 1, 1, 1, 3),
    _FextInfoPIMSMVIFAddress_Type()
)
fextInfoPIMSMVIFAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoPIMSMVIFAddress.setStatus("current")
_FextInfoPIMSMVIFFlag_Type = DisplayString
_FextInfoPIMSMVIFFlag_Object = MibTableColumn
fextInfoPIMSMVIFFlag = _FextInfoPIMSMVIFFlag_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 4, 1, 1, 1, 4),
    _FextInfoPIMSMVIFFlag_Type()
)
fextInfoPIMSMVIFFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoPIMSMVIFFlag.setStatus("current")
_FextInfoPIMSMVIFHelloTimer_Type = Integer32
_FextInfoPIMSMVIFHelloTimer_Object = MibTableColumn
fextInfoPIMSMVIFHelloTimer = _FextInfoPIMSMVIFHelloTimer_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 4, 1, 1, 1, 5),
    _FextInfoPIMSMVIFHelloTimer_Type()
)
fextInfoPIMSMVIFHelloTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoPIMSMVIFHelloTimer.setStatus("current")
_FextInfoPIMSMVIFDRPriority_Type = Integer32
_FextInfoPIMSMVIFDRPriority_Object = MibTableColumn
fextInfoPIMSMVIFDRPriority = _FextInfoPIMSMVIFDRPriority_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 4, 1, 1, 1, 6),
    _FextInfoPIMSMVIFDRPriority_Type()
)
fextInfoPIMSMVIFDRPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoPIMSMVIFDRPriority.setStatus("current")
_FextInfoPIMSMVIFNeighbor_Object = MibTable
fextInfoPIMSMVIFNeighbor = _FextInfoPIMSMVIFNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 4, 1, 2)
)
if mibBuilder.loadTexts:
    fextInfoPIMSMVIFNeighbor.setStatus("current")
_FextInfoPIMSMVIFNeighborEntry_Object = MibTableRow
fextInfoPIMSMVIFNeighborEntry = _FextInfoPIMSMVIFNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 4, 1, 2, 1)
)
fextInfoPIMSMVIFNeighborEntry.setIndexNames(
    (0, "FORTINET-FORTIEXTENDER-MIB", "fextInfoPIMSMVIFIndex"),
    (0, "FORTINET-FORTIEXTENDER-MIB", "fextInfoPIMSMVIFNeighborIndex"),
)
if mibBuilder.loadTexts:
    fextInfoPIMSMVIFNeighborEntry.setStatus("current")
_FextInfoPIMSMVIFNeighborIndex_Type = FnIndex
_FextInfoPIMSMVIFNeighborIndex_Object = MibTableColumn
fextInfoPIMSMVIFNeighborIndex = _FextInfoPIMSMVIFNeighborIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 4, 1, 2, 1, 1),
    _FextInfoPIMSMVIFNeighborIndex_Type()
)
fextInfoPIMSMVIFNeighborIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fextInfoPIMSMVIFNeighborIndex.setStatus("current")
_FextInfoPIMSMVIFNeighborIP_Type = DisplayString
_FextInfoPIMSMVIFNeighborIP_Object = MibTableColumn
fextInfoPIMSMVIFNeighborIP = _FextInfoPIMSMVIFNeighborIP_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 4, 1, 2, 1, 2),
    _FextInfoPIMSMVIFNeighborIP_Type()
)
fextInfoPIMSMVIFNeighborIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoPIMSMVIFNeighborIP.setStatus("current")
_FextInfoPIMSMVIFNeighborExpire_Type = Integer32
_FextInfoPIMSMVIFNeighborExpire_Object = MibTableColumn
fextInfoPIMSMVIFNeighborExpire = _FextInfoPIMSMVIFNeighborExpire_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 4, 1, 2, 1, 3),
    _FextInfoPIMSMVIFNeighborExpire_Type()
)
fextInfoPIMSMVIFNeighborExpire.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoPIMSMVIFNeighborExpire.setStatus("current")
_FextInfoPIMSMRoute_Object = MibTable
fextInfoPIMSMRoute = _FextInfoPIMSMRoute_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 4, 1, 3)
)
if mibBuilder.loadTexts:
    fextInfoPIMSMRoute.setStatus("current")
_FextInfoPIMSMRouteEntry_Object = MibTableRow
fextInfoPIMSMRouteEntry = _FextInfoPIMSMRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 4, 1, 3, 1)
)
fextInfoPIMSMRouteEntry.setIndexNames(
    (0, "FORTINET-FORTIEXTENDER-MIB", "fextInfoPIMSMRouteIndex"),
)
if mibBuilder.loadTexts:
    fextInfoPIMSMRouteEntry.setStatus("current")
_FextInfoPIMSMRouteIndex_Type = FnIndex
_FextInfoPIMSMRouteIndex_Object = MibTableColumn
fextInfoPIMSMRouteIndex = _FextInfoPIMSMRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 4, 1, 3, 1, 1),
    _FextInfoPIMSMRouteIndex_Type()
)
fextInfoPIMSMRouteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fextInfoPIMSMRouteIndex.setStatus("current")
_FextInfoPIMSMRouteSRC_Type = DisplayString
_FextInfoPIMSMRouteSRC_Object = MibTableColumn
fextInfoPIMSMRouteSRC = _FextInfoPIMSMRouteSRC_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 4, 1, 3, 1, 2),
    _FextInfoPIMSMRouteSRC_Type()
)
fextInfoPIMSMRouteSRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoPIMSMRouteSRC.setStatus("current")
_FextInfoPIMSMRouteGRP_Type = DisplayString
_FextInfoPIMSMRouteGRP_Object = MibTableColumn
fextInfoPIMSMRouteGRP = _FextInfoPIMSMRouteGRP_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 4, 1, 3, 1, 3),
    _FextInfoPIMSMRouteGRP_Type()
)
fextInfoPIMSMRouteGRP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoPIMSMRouteGRP.setStatus("current")
_FextInfoPIMSMRouteRP_Type = DisplayString
_FextInfoPIMSMRouteRP_Object = MibTableColumn
fextInfoPIMSMRouteRP = _FextInfoPIMSMRouteRP_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 4, 1, 3, 1, 4),
    _FextInfoPIMSMRouteRP_Type()
)
fextInfoPIMSMRouteRP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoPIMSMRouteRP.setStatus("current")
_FextInfoPIMSMRouteFlag_Type = DisplayString
_FextInfoPIMSMRouteFlag_Object = MibTableColumn
fextInfoPIMSMRouteFlag = _FextInfoPIMSMRouteFlag_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 4, 1, 3, 1, 5),
    _FextInfoPIMSMRouteFlag_Type()
)
fextInfoPIMSMRouteFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoPIMSMRouteFlag.setStatus("current")
_FextInfoPIMSMRouteJoinedOIFs_Type = DisplayString
_FextInfoPIMSMRouteJoinedOIFs_Object = MibTableColumn
fextInfoPIMSMRouteJoinedOIFs = _FextInfoPIMSMRouteJoinedOIFs_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 4, 1, 3, 1, 6),
    _FextInfoPIMSMRouteJoinedOIFs_Type()
)
fextInfoPIMSMRouteJoinedOIFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoPIMSMRouteJoinedOIFs.setStatus("current")
_FextInfoPIMSMRoutePrunedOIFs_Type = DisplayString
_FextInfoPIMSMRoutePrunedOIFs_Object = MibTableColumn
fextInfoPIMSMRoutePrunedOIFs = _FextInfoPIMSMRoutePrunedOIFs_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 4, 1, 3, 1, 7),
    _FextInfoPIMSMRoutePrunedOIFs_Type()
)
fextInfoPIMSMRoutePrunedOIFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoPIMSMRoutePrunedOIFs.setStatus("current")
_FextInfoPIMSMRouteLeavesOIFs_Type = DisplayString
_FextInfoPIMSMRouteLeavesOIFs_Object = MibTableColumn
fextInfoPIMSMRouteLeavesOIFs = _FextInfoPIMSMRouteLeavesOIFs_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 4, 1, 3, 1, 8),
    _FextInfoPIMSMRouteLeavesOIFs_Type()
)
fextInfoPIMSMRouteLeavesOIFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoPIMSMRouteLeavesOIFs.setStatus("current")
_FextInfoPIMSMRouteAssertedOIFs_Type = DisplayString
_FextInfoPIMSMRouteAssertedOIFs_Object = MibTableColumn
fextInfoPIMSMRouteAssertedOIFs = _FextInfoPIMSMRouteAssertedOIFs_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 4, 1, 3, 1, 9),
    _FextInfoPIMSMRouteAssertedOIFs_Type()
)
fextInfoPIMSMRouteAssertedOIFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoPIMSMRouteAssertedOIFs.setStatus("current")
_FextInfoPIMSMRouteOutgoingOIFs_Type = DisplayString
_FextInfoPIMSMRouteOutgoingOIFs_Object = MibTableColumn
fextInfoPIMSMRouteOutgoingOIFs = _FextInfoPIMSMRouteOutgoingOIFs_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 4, 1, 3, 1, 10),
    _FextInfoPIMSMRouteOutgoingOIFs_Type()
)
fextInfoPIMSMRouteOutgoingOIFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoPIMSMRouteOutgoingOIFs.setStatus("current")
_FextInfoPIMSMRouteIncomingIFs_Type = DisplayString
_FextInfoPIMSMRouteIncomingIFs_Object = MibTableColumn
fextInfoPIMSMRouteIncomingIFs = _FextInfoPIMSMRouteIncomingIFs_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 4, 1, 3, 1, 11),
    _FextInfoPIMSMRouteIncomingIFs_Type()
)
fextInfoPIMSMRouteIncomingIFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoPIMSMRouteIncomingIFs.setStatus("current")
_FextInfoPIMSMRouteJoinPruneTimer_Type = Integer32
_FextInfoPIMSMRouteJoinPruneTimer_Object = MibTableColumn
fextInfoPIMSMRouteJoinPruneTimer = _FextInfoPIMSMRouteJoinPruneTimer_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 4, 1, 3, 1, 12),
    _FextInfoPIMSMRouteJoinPruneTimer_Type()
)
fextInfoPIMSMRouteJoinPruneTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoPIMSMRouteJoinPruneTimer.setStatus("current")
_FextInfoPIMSMRP_Object = MibTable
fextInfoPIMSMRP = _FextInfoPIMSMRP_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 4, 1, 4)
)
if mibBuilder.loadTexts:
    fextInfoPIMSMRP.setStatus("current")
_FextInfoPIMSMRPEntry_Object = MibTableRow
fextInfoPIMSMRPEntry = _FextInfoPIMSMRPEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 4, 1, 4, 1)
)
fextInfoPIMSMRPEntry.setIndexNames(
    (0, "FORTINET-FORTIEXTENDER-MIB", "fextInfoPIMSMRPIndex"),
)
if mibBuilder.loadTexts:
    fextInfoPIMSMRPEntry.setStatus("current")
_FextInfoPIMSMRPIndex_Type = FnIndex
_FextInfoPIMSMRPIndex_Object = MibTableColumn
fextInfoPIMSMRPIndex = _FextInfoPIMSMRPIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 4, 1, 4, 1, 1),
    _FextInfoPIMSMRPIndex_Type()
)
fextInfoPIMSMRPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fextInfoPIMSMRPIndex.setStatus("current")
_FextInfoPIMSMRPAddress_Type = DisplayString
_FextInfoPIMSMRPAddress_Object = MibTableColumn
fextInfoPIMSMRPAddress = _FextInfoPIMSMRPAddress_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 4, 1, 4, 1, 2),
    _FextInfoPIMSMRPAddress_Type()
)
fextInfoPIMSMRPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoPIMSMRPAddress.setStatus("current")
_FextInfoPIMSMRPGroup_Object = MibTable
fextInfoPIMSMRPGroup = _FextInfoPIMSMRPGroup_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 4, 1, 5)
)
if mibBuilder.loadTexts:
    fextInfoPIMSMRPGroup.setStatus("current")
_FextInfoPIMSMRPGroupEntry_Object = MibTableRow
fextInfoPIMSMRPGroupEntry = _FextInfoPIMSMRPGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 4, 1, 5, 1)
)
fextInfoPIMSMRPGroupEntry.setIndexNames(
    (0, "FORTINET-FORTIEXTENDER-MIB", "fextInfoPIMSMRPIndex"),
    (0, "FORTINET-FORTIEXTENDER-MIB", "fextInfoPIMSMRPGroupIndex"),
)
if mibBuilder.loadTexts:
    fextInfoPIMSMRPGroupEntry.setStatus("current")
_FextInfoPIMSMRPGroupIndex_Type = FnIndex
_FextInfoPIMSMRPGroupIndex_Object = MibTableColumn
fextInfoPIMSMRPGroupIndex = _FextInfoPIMSMRPGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 4, 1, 5, 1, 1),
    _FextInfoPIMSMRPGroupIndex_Type()
)
fextInfoPIMSMRPGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fextInfoPIMSMRPGroupIndex.setStatus("current")
_FextInfoPIMSMRPGroupAddress_Type = DisplayString
_FextInfoPIMSMRPGroupAddress_Object = MibTableColumn
fextInfoPIMSMRPGroupAddress = _FextInfoPIMSMRPGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 4, 1, 5, 1, 2),
    _FextInfoPIMSMRPGroupAddress_Type()
)
fextInfoPIMSMRPGroupAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoPIMSMRPGroupAddress.setStatus("current")
_FextInfoPIMSMRPGroupPriority_Type = Integer32
_FextInfoPIMSMRPGroupPriority_Object = MibTableColumn
fextInfoPIMSMRPGroupPriority = _FextInfoPIMSMRPGroupPriority_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 4, 1, 5, 1, 3),
    _FextInfoPIMSMRPGroupPriority_Type()
)
fextInfoPIMSMRPGroupPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoPIMSMRPGroupPriority.setStatus("current")
_FextInfoRouterVRRP_Object = MibTable
fextInfoRouterVRRP = _FextInfoRouterVRRP_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 5)
)
if mibBuilder.loadTexts:
    fextInfoRouterVRRP.setStatus("current")
_FextInfoRouterVRRPEntry_Object = MibTableRow
fextInfoRouterVRRPEntry = _FextInfoRouterVRRPEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 5, 1)
)
fextInfoRouterVRRPEntry.setIndexNames(
    (0, "FORTINET-FORTIEXTENDER-MIB", "fextInfoRouterVRRPIndex"),
)
if mibBuilder.loadTexts:
    fextInfoRouterVRRPEntry.setStatus("current")
_FextInfoRouterVRRPIndex_Type = FnIndex
_FextInfoRouterVRRPIndex_Object = MibTableColumn
fextInfoRouterVRRPIndex = _FextInfoRouterVRRPIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 5, 1, 1),
    _FextInfoRouterVRRPIndex_Type()
)
fextInfoRouterVRRPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fextInfoRouterVRRPIndex.setStatus("current")
_FextInfoRouterVRRPIfName_Type = DisplayString
_FextInfoRouterVRRPIfName_Object = MibTableColumn
fextInfoRouterVRRPIfName = _FextInfoRouterVRRPIfName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 5, 1, 2),
    _FextInfoRouterVRRPIfName_Type()
)
fextInfoRouterVRRPIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoRouterVRRPIfName.setStatus("current")
_FextInfoRouterVRRPState_Type = DisplayString
_FextInfoRouterVRRPState_Object = MibTableColumn
fextInfoRouterVRRPState = _FextInfoRouterVRRPState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 4, 5, 1, 3),
    _FextInfoRouterVRRPState_Type()
)
fextInfoRouterVRRPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoRouterVRRPState.setStatus("current")
_FextInfoVWAN_ObjectIdentity = ObjectIdentity
fextInfoVWAN = _FextInfoVWAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 5)
)
_FextInfoVWANStatus_Object = MibTable
fextInfoVWANStatus = _FextInfoVWANStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 5, 1)
)
if mibBuilder.loadTexts:
    fextInfoVWANStatus.setStatus("current")
_FextInfoVWANStatusEntry_Object = MibTableRow
fextInfoVWANStatusEntry = _FextInfoVWANStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 5, 1, 1)
)
fextInfoVWANStatusEntry.setIndexNames(
    (0, "FORTINET-FORTIEXTENDER-MIB", "fextInfoVWANStatusIndex"),
)
if mibBuilder.loadTexts:
    fextInfoVWANStatusEntry.setStatus("current")
_FextInfoVWANStatusIndex_Type = FnIndex
_FextInfoVWANStatusIndex_Object = MibTableColumn
fextInfoVWANStatusIndex = _FextInfoVWANStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 5, 1, 1, 1),
    _FextInfoVWANStatusIndex_Type()
)
fextInfoVWANStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fextInfoVWANStatusIndex.setStatus("current")
_FextInfoVWANStatusName_Type = DisplayString
_FextInfoVWANStatusName_Object = MibTableColumn
fextInfoVWANStatusName = _FextInfoVWANStatusName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 5, 1, 1, 2),
    _FextInfoVWANStatusName_Type()
)
fextInfoVWANStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoVWANStatusName.setStatus("current")
_FextInfoVWANStatusAlgorithm_Type = DisplayString
_FextInfoVWANStatusAlgorithm_Object = MibTableColumn
fextInfoVWANStatusAlgorithm = _FextInfoVWANStatusAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 5, 1, 1, 3),
    _FextInfoVWANStatusAlgorithm_Type()
)
fextInfoVWANStatusAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoVWANStatusAlgorithm.setStatus("current")
_FextInfoVWANStatusRedundantBy_Type = DisplayString
_FextInfoVWANStatusRedundantBy_Object = MibTableColumn
fextInfoVWANStatusRedundantBy = _FextInfoVWANStatusRedundantBy_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 5, 1, 1, 4),
    _FextInfoVWANStatusRedundantBy_Type()
)
fextInfoVWANStatusRedundantBy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoVWANStatusRedundantBy.setStatus("current")
_FextInfoVWANStatusFECName_Type = DisplayString
_FextInfoVWANStatusFECName_Object = MibTableColumn
fextInfoVWANStatusFECName = _FextInfoVWANStatusFECName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 5, 1, 1, 5),
    _FextInfoVWANStatusFECName_Type()
)
fextInfoVWANStatusFECName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoVWANStatusFECName.setStatus("current")
_FextInfoVWANStatusTargetCount_Type = Integer32
_FextInfoVWANStatusTargetCount_Object = MibTableColumn
fextInfoVWANStatusTargetCount = _FextInfoVWANStatusTargetCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 5, 1, 1, 6),
    _FextInfoVWANStatusTargetCount_Type()
)
fextInfoVWANStatusTargetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoVWANStatusTargetCount.setStatus("current")
_FextInfoVWANStatusSessionCount_Type = Integer32
_FextInfoVWANStatusSessionCount_Object = MibTableColumn
fextInfoVWANStatusSessionCount = _FextInfoVWANStatusSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 5, 1, 1, 7),
    _FextInfoVWANStatusSessionCount_Type()
)
fextInfoVWANStatusSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoVWANStatusSessionCount.setStatus("current")
_FextInfoVWANStatusSessionTimeout_Type = Integer32
_FextInfoVWANStatusSessionTimeout_Object = MibTableColumn
fextInfoVWANStatusSessionTimeout = _FextInfoVWANStatusSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 5, 1, 1, 8),
    _FextInfoVWANStatusSessionTimeout_Type()
)
fextInfoVWANStatusSessionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoVWANStatusSessionTimeout.setStatus("current")
_FextInfoVWANStatusVersion_Type = Integer32
_FextInfoVWANStatusVersion_Object = MibTableColumn
fextInfoVWANStatusVersion = _FextInfoVWANStatusVersion_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 5, 1, 1, 9),
    _FextInfoVWANStatusVersion_Type()
)
fextInfoVWANStatusVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoVWANStatusVersion.setStatus("current")
_FextInfoVWANStatusMember_Object = MibTable
fextInfoVWANStatusMember = _FextInfoVWANStatusMember_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 5, 2)
)
if mibBuilder.loadTexts:
    fextInfoVWANStatusMember.setStatus("current")
_FextInfoVWANStatusMemberEntry_Object = MibTableRow
fextInfoVWANStatusMemberEntry = _FextInfoVWANStatusMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 5, 2, 1)
)
fextInfoVWANStatusMemberEntry.setIndexNames(
    (0, "FORTINET-FORTIEXTENDER-MIB", "fextInfoVWANStatusIndex"),
    (0, "FORTINET-FORTIEXTENDER-MIB", "fextInfoVWANStatusMemberIndex"),
)
if mibBuilder.loadTexts:
    fextInfoVWANStatusMemberEntry.setStatus("current")
_FextInfoVWANStatusMemberIndex_Type = FnIndex
_FextInfoVWANStatusMemberIndex_Object = MibTableColumn
fextInfoVWANStatusMemberIndex = _FextInfoVWANStatusMemberIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 5, 2, 1, 1),
    _FextInfoVWANStatusMemberIndex_Type()
)
fextInfoVWANStatusMemberIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fextInfoVWANStatusMemberIndex.setStatus("current")
_FextInfoVWANStatusMemberName_Type = DisplayString
_FextInfoVWANStatusMemberName_Object = MibTableColumn
fextInfoVWANStatusMemberName = _FextInfoVWANStatusMemberName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 5, 2, 1, 2),
    _FextInfoVWANStatusMemberName_Type()
)
fextInfoVWANStatusMemberName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoVWANStatusMemberName.setStatus("current")
_FextInfoVWANStatusMemberStatus_Type = DisplayString
_FextInfoVWANStatusMemberStatus_Object = MibTableColumn
fextInfoVWANStatusMemberStatus = _FextInfoVWANStatusMemberStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 5, 2, 1, 3),
    _FextInfoVWANStatusMemberStatus_Type()
)
fextInfoVWANStatusMemberStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoVWANStatusMemberStatus.setStatus("current")
_FextInfoVWANStatusMemberPriority_Type = Integer32
_FextInfoVWANStatusMemberPriority_Object = MibTableColumn
fextInfoVWANStatusMemberPriority = _FextInfoVWANStatusMemberPriority_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 5, 2, 1, 4),
    _FextInfoVWANStatusMemberPriority_Type()
)
fextInfoVWANStatusMemberPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoVWANStatusMemberPriority.setStatus("current")
_FextInfoVWANStatusMemberWeight_Type = Integer32
_FextInfoVWANStatusMemberWeight_Object = MibTableColumn
fextInfoVWANStatusMemberWeight = _FextInfoVWANStatusMemberWeight_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 5, 2, 1, 5),
    _FextInfoVWANStatusMemberWeight_Type()
)
fextInfoVWANStatusMemberWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoVWANStatusMemberWeight.setStatus("current")
_FextInfoVWANStatusMemberCapacity_Type = Integer32
_FextInfoVWANStatusMemberCapacity_Object = MibTableColumn
fextInfoVWANStatusMemberCapacity = _FextInfoVWANStatusMemberCapacity_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 5, 2, 1, 6),
    _FextInfoVWANStatusMemberCapacity_Type()
)
fextInfoVWANStatusMemberCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoVWANStatusMemberCapacity.setStatus("current")
_FextInfoVWANStatusMemberMonthlyFee_Type = Integer32
_FextInfoVWANStatusMemberMonthlyFee_Object = MibTableColumn
fextInfoVWANStatusMemberMonthlyFee = _FextInfoVWANStatusMemberMonthlyFee_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 5, 2, 1, 7),
    _FextInfoVWANStatusMemberMonthlyFee_Type()
)
fextInfoVWANStatusMemberMonthlyFee.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoVWANStatusMemberMonthlyFee.setStatus("current")
_FextInfoVWANStatusMemberSessionCount_Type = Integer32
_FextInfoVWANStatusMemberSessionCount_Object = MibTableColumn
fextInfoVWANStatusMemberSessionCount = _FextInfoVWANStatusMemberSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 5, 2, 1, 8),
    _FextInfoVWANStatusMemberSessionCount_Type()
)
fextInfoVWANStatusMemberSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoVWANStatusMemberSessionCount.setStatus("current")
_FextInfoVWANStatusMemberReference_Type = Integer32
_FextInfoVWANStatusMemberReference_Object = MibTableColumn
fextInfoVWANStatusMemberReference = _FextInfoVWANStatusMemberReference_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 5, 2, 1, 9),
    _FextInfoVWANStatusMemberReference_Type()
)
fextInfoVWANStatusMemberReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoVWANStatusMemberReference.setStatus("current")
_FextInfoVWANStatusMemberInterface_Type = DisplayString
_FextInfoVWANStatusMemberInterface_Object = MibTableColumn
fextInfoVWANStatusMemberInterface = _FextInfoVWANStatusMemberInterface_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 5, 2, 1, 10),
    _FextInfoVWANStatusMemberInterface_Type()
)
fextInfoVWANStatusMemberInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoVWANStatusMemberInterface.setStatus("current")
_FextInfoVWANStatusMemberNextHop_Type = DisplayString
_FextInfoVWANStatusMemberNextHop_Object = MibTableColumn
fextInfoVWANStatusMemberNextHop = _FextInfoVWANStatusMemberNextHop_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 5, 2, 1, 11),
    _FextInfoVWANStatusMemberNextHop_Type()
)
fextInfoVWANStatusMemberNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoVWANStatusMemberNextHop.setStatus("current")
_FextInfoVWANStatusMemberInBandwidth_Type = Integer32
_FextInfoVWANStatusMemberInBandwidth_Object = MibTableColumn
fextInfoVWANStatusMemberInBandwidth = _FextInfoVWANStatusMemberInBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 5, 2, 1, 12),
    _FextInfoVWANStatusMemberInBandwidth_Type()
)
fextInfoVWANStatusMemberInBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoVWANStatusMemberInBandwidth.setStatus("current")
_FextInfoVWANStatusMemberOutBandwidth_Type = Integer32
_FextInfoVWANStatusMemberOutBandwidth_Object = MibTableColumn
fextInfoVWANStatusMemberOutBandwidth = _FextInfoVWANStatusMemberOutBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 5, 2, 1, 13),
    _FextInfoVWANStatusMemberOutBandwidth_Type()
)
fextInfoVWANStatusMemberOutBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoVWANStatusMemberOutBandwidth.setStatus("current")
_FextInfoVWANStatusMemberTotalBandwidth_Type = Integer32
_FextInfoVWANStatusMemberTotalBandwidth_Object = MibTableColumn
fextInfoVWANStatusMemberTotalBandwidth = _FextInfoVWANStatusMemberTotalBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 5, 2, 1, 14),
    _FextInfoVWANStatusMemberTotalBandwidth_Type()
)
fextInfoVWANStatusMemberTotalBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoVWANStatusMemberTotalBandwidth.setStatus("current")
_FextInfoVWANStatusMemberDataIn_Type = Counter64
_FextInfoVWANStatusMemberDataIn_Object = MibTableColumn
fextInfoVWANStatusMemberDataIn = _FextInfoVWANStatusMemberDataIn_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 5, 2, 1, 15),
    _FextInfoVWANStatusMemberDataIn_Type()
)
fextInfoVWANStatusMemberDataIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoVWANStatusMemberDataIn.setStatus("current")
_FextInfoVWANStatusMemberDataOut_Type = Counter64
_FextInfoVWANStatusMemberDataOut_Object = MibTableColumn
fextInfoVWANStatusMemberDataOut = _FextInfoVWANStatusMemberDataOut_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 5, 2, 1, 16),
    _FextInfoVWANStatusMemberDataOut_Type()
)
fextInfoVWANStatusMemberDataOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoVWANStatusMemberDataOut.setStatus("current")
_FextInfoVWANStatusMemberTPIn_Type = Counter64
_FextInfoVWANStatusMemberTPIn_Object = MibTableColumn
fextInfoVWANStatusMemberTPIn = _FextInfoVWANStatusMemberTPIn_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 5, 2, 1, 17),
    _FextInfoVWANStatusMemberTPIn_Type()
)
fextInfoVWANStatusMemberTPIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoVWANStatusMemberTPIn.setStatus("current")
_FextInfoVWANStatusMemberTPOut_Type = Counter64
_FextInfoVWANStatusMemberTPOut_Object = MibTableColumn
fextInfoVWANStatusMemberTPOut = _FextInfoVWANStatusMemberTPOut_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 5, 2, 1, 18),
    _FextInfoVWANStatusMemberTPOut_Type()
)
fextInfoVWANStatusMemberTPOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoVWANStatusMemberTPOut.setStatus("current")
_FextInfoVWANMember_Object = MibTable
fextInfoVWANMember = _FextInfoVWANMember_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 5, 3)
)
if mibBuilder.loadTexts:
    fextInfoVWANMember.setStatus("current")
_FextInfoVWANMemberEntry_Object = MibTableRow
fextInfoVWANMemberEntry = _FextInfoVWANMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 5, 3, 1)
)
fextInfoVWANMemberEntry.setIndexNames(
    (0, "FORTINET-FORTIEXTENDER-MIB", "fextInfoVWANMemberIndex"),
)
if mibBuilder.loadTexts:
    fextInfoVWANMemberEntry.setStatus("current")
_FextInfoVWANMemberIndex_Type = FnIndex
_FextInfoVWANMemberIndex_Object = MibTableColumn
fextInfoVWANMemberIndex = _FextInfoVWANMemberIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 5, 3, 1, 1),
    _FextInfoVWANMemberIndex_Type()
)
fextInfoVWANMemberIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fextInfoVWANMemberIndex.setStatus("current")
_FextInfoVWANMemberName_Type = DisplayString
_FextInfoVWANMemberName_Object = MibTableColumn
fextInfoVWANMemberName = _FextInfoVWANMemberName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 5, 3, 1, 2),
    _FextInfoVWANMemberName_Type()
)
fextInfoVWANMemberName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoVWANMemberName.setStatus("current")
_FextInfoVWANMemberTarget_Type = DisplayString
_FextInfoVWANMemberTarget_Object = MibTableColumn
fextInfoVWANMemberTarget = _FextInfoVWANMemberTarget_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 5, 3, 1, 3),
    _FextInfoVWANMemberTarget_Type()
)
fextInfoVWANMemberTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoVWANMemberTarget.setStatus("current")
_FextInfoVWANMemberPriority_Type = Integer32
_FextInfoVWANMemberPriority_Object = MibTableColumn
fextInfoVWANMemberPriority = _FextInfoVWANMemberPriority_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 5, 3, 1, 4),
    _FextInfoVWANMemberPriority_Type()
)
fextInfoVWANMemberPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoVWANMemberPriority.setStatus("current")
_FextInfoVWANMemberCapacity_Type = Integer32
_FextInfoVWANMemberCapacity_Object = MibTableColumn
fextInfoVWANMemberCapacity = _FextInfoVWANMemberCapacity_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 5, 3, 1, 5),
    _FextInfoVWANMemberCapacity_Type()
)
fextInfoVWANMemberCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoVWANMemberCapacity.setStatus("current")
_FextInfoVWANMemberMonthlyFee_Type = Integer32
_FextInfoVWANMemberMonthlyFee_Object = MibTableColumn
fextInfoVWANMemberMonthlyFee = _FextInfoVWANMemberMonthlyFee_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 5, 3, 1, 6),
    _FextInfoVWANMemberMonthlyFee_Type()
)
fextInfoVWANMemberMonthlyFee.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoVWANMemberMonthlyFee.setStatus("current")
_FextInfoVWANMemberWeight_Type = Integer32
_FextInfoVWANMemberWeight_Object = MibTableColumn
fextInfoVWANMemberWeight = _FextInfoVWANMemberWeight_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 5, 3, 1, 7),
    _FextInfoVWANMemberWeight_Type()
)
fextInfoVWANMemberWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoVWANMemberWeight.setStatus("current")
_FextInfoVWANMemberInBwThreshold_Type = Integer32
_FextInfoVWANMemberInBwThreshold_Object = MibTableColumn
fextInfoVWANMemberInBwThreshold = _FextInfoVWANMemberInBwThreshold_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 5, 3, 1, 8),
    _FextInfoVWANMemberInBwThreshold_Type()
)
fextInfoVWANMemberInBwThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoVWANMemberInBwThreshold.setStatus("current")
_FextInfoVWANMemberOutBwThreshold_Type = Integer32
_FextInfoVWANMemberOutBwThreshold_Object = MibTableColumn
fextInfoVWANMemberOutBwThreshold = _FextInfoVWANMemberOutBwThreshold_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 5, 3, 1, 9),
    _FextInfoVWANMemberOutBwThreshold_Type()
)
fextInfoVWANMemberOutBwThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoVWANMemberOutBwThreshold.setStatus("current")
_FextInfoVWANMemberTotalBwThreshold_Type = Integer32
_FextInfoVWANMemberTotalBwThreshold_Object = MibTableColumn
fextInfoVWANMemberTotalBwThreshold = _FextInfoVWANMemberTotalBwThreshold_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 5, 3, 1, 10),
    _FextInfoVWANMemberTotalBwThreshold_Type()
)
fextInfoVWANMemberTotalBwThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoVWANMemberTotalBwThreshold.setStatus("current")
_FextInfoVWANMemberReference_Type = Integer32
_FextInfoVWANMemberReference_Object = MibTableColumn
fextInfoVWANMemberReference = _FextInfoVWANMemberReference_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 5, 3, 1, 11),
    _FextInfoVWANMemberReference_Type()
)
fextInfoVWANMemberReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoVWANMemberReference.setStatus("current")
_FextInfoVPN_ObjectIdentity = ObjectIdentity
fextInfoVPN = _FextInfoVPN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 6)
)
_FextInfoVPNIPsec_ObjectIdentity = ObjectIdentity
fextInfoVPNIPsec = _FextInfoVPNIPsec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 6, 1)
)
_FextInfoIPsecTunnel_Object = MibTable
fextInfoIPsecTunnel = _FextInfoIPsecTunnel_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 6, 1, 1)
)
if mibBuilder.loadTexts:
    fextInfoIPsecTunnel.setStatus("current")
_FextInfoIPsecTunnelEntry_Object = MibTableRow
fextInfoIPsecTunnelEntry = _FextInfoIPsecTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 6, 1, 1, 1)
)
fextInfoIPsecTunnelEntry.setIndexNames(
    (0, "FORTINET-FORTIEXTENDER-MIB", "fextInfoIPsecTunIndex"),
)
if mibBuilder.loadTexts:
    fextInfoIPsecTunnelEntry.setStatus("current")
_FextInfoIPsecTunIndex_Type = FnIndex
_FextInfoIPsecTunIndex_Object = MibTableColumn
fextInfoIPsecTunIndex = _FextInfoIPsecTunIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 6, 1, 1, 1, 1),
    _FextInfoIPsecTunIndex_Type()
)
fextInfoIPsecTunIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fextInfoIPsecTunIndex.setStatus("current")
_FextInfoIPsecTunPhase1Name_Type = DisplayString
_FextInfoIPsecTunPhase1Name_Object = MibTableColumn
fextInfoIPsecTunPhase1Name = _FextInfoIPsecTunPhase1Name_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 6, 1, 1, 1, 2),
    _FextInfoIPsecTunPhase1Name_Type()
)
fextInfoIPsecTunPhase1Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoIPsecTunPhase1Name.setStatus("current")
_FextInfoIPsecTunStatus_Type = DisplayString
_FextInfoIPsecTunStatus_Object = MibTableColumn
fextInfoIPsecTunStatus = _FextInfoIPsecTunStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 6, 1, 1, 1, 3),
    _FextInfoIPsecTunStatus_Type()
)
fextInfoIPsecTunStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoIPsecTunStatus.setStatus("current")
_FextInfoIPsecTunLocGwIp_Type = DisplayString
_FextInfoIPsecTunLocGwIp_Object = MibTableColumn
fextInfoIPsecTunLocGwIp = _FextInfoIPsecTunLocGwIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 6, 1, 1, 1, 4),
    _FextInfoIPsecTunLocGwIp_Type()
)
fextInfoIPsecTunLocGwIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoIPsecTunLocGwIp.setStatus("current")
_FextInfoIPsecTunRemGwIp_Type = DisplayString
_FextInfoIPsecTunRemGwIp_Object = MibTableColumn
fextInfoIPsecTunRemGwIp = _FextInfoIPsecTunRemGwIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 6, 1, 1, 1, 5),
    _FextInfoIPsecTunRemGwIp_Type()
)
fextInfoIPsecTunRemGwIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoIPsecTunRemGwIp.setStatus("current")
_FextInfoIPsecTunInBytes_Type = Counter64
_FextInfoIPsecTunInBytes_Object = MibTableColumn
fextInfoIPsecTunInBytes = _FextInfoIPsecTunInBytes_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 6, 1, 1, 1, 6),
    _FextInfoIPsecTunInBytes_Type()
)
fextInfoIPsecTunInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoIPsecTunInBytes.setStatus("current")
_FextInfoIPsecTunOutBytes_Type = Counter64
_FextInfoIPsecTunOutBytes_Object = MibTableColumn
fextInfoIPsecTunOutBytes = _FextInfoIPsecTunOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 6, 1, 1, 1, 7),
    _FextInfoIPsecTunOutBytes_Type()
)
fextInfoIPsecTunOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoIPsecTunOutBytes.setStatus("current")
_FextInfoIPsecTunUpSeconds_Type = Integer32
_FextInfoIPsecTunUpSeconds_Object = MibTableColumn
fextInfoIPsecTunUpSeconds = _FextInfoIPsecTunUpSeconds_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 6, 1, 1, 1, 8),
    _FextInfoIPsecTunUpSeconds_Type()
)
fextInfoIPsecTunUpSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoIPsecTunUpSeconds.setStatus("current")
_FextInfoIPsecTunSelector_Object = MibTable
fextInfoIPsecTunSelector = _FextInfoIPsecTunSelector_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 6, 1, 2)
)
if mibBuilder.loadTexts:
    fextInfoIPsecTunSelector.setStatus("current")
_FextInfoIPsecTunSelectorEntry_Object = MibTableRow
fextInfoIPsecTunSelectorEntry = _FextInfoIPsecTunSelectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 6, 1, 2, 1)
)
fextInfoIPsecTunSelectorEntry.setIndexNames(
    (0, "FORTINET-FORTIEXTENDER-MIB", "fextInfoIPsecTunIndex"),
    (0, "FORTINET-FORTIEXTENDER-MIB", "fextInfoIPsecTunSelectorIndex"),
)
if mibBuilder.loadTexts:
    fextInfoIPsecTunSelectorEntry.setStatus("current")
_FextInfoIPsecTunSelectorIndex_Type = FnIndex
_FextInfoIPsecTunSelectorIndex_Object = MibTableColumn
fextInfoIPsecTunSelectorIndex = _FextInfoIPsecTunSelectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 6, 1, 2, 1, 1),
    _FextInfoIPsecTunSelectorIndex_Type()
)
fextInfoIPsecTunSelectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fextInfoIPsecTunSelectorIndex.setStatus("current")
_FextInfoIPsecTunSelectorP2Name_Type = DisplayString
_FextInfoIPsecTunSelectorP2Name_Object = MibTableColumn
fextInfoIPsecTunSelectorP2Name = _FextInfoIPsecTunSelectorP2Name_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 6, 1, 2, 1, 2),
    _FextInfoIPsecTunSelectorP2Name_Type()
)
fextInfoIPsecTunSelectorP2Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoIPsecTunSelectorP2Name.setStatus("current")
_FextInfoIPsecTunSelectorStatus_Type = DisplayString
_FextInfoIPsecTunSelectorStatus_Object = MibTableColumn
fextInfoIPsecTunSelectorStatus = _FextInfoIPsecTunSelectorStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 6, 1, 2, 1, 3),
    _FextInfoIPsecTunSelectorStatus_Type()
)
fextInfoIPsecTunSelectorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoIPsecTunSelectorStatus.setStatus("current")
_FextInfoIPsecTunSelectorExpire_Type = Integer32
_FextInfoIPsecTunSelectorExpire_Object = MibTableColumn
fextInfoIPsecTunSelectorExpire = _FextInfoIPsecTunSelectorExpire_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 6, 1, 2, 1, 4),
    _FextInfoIPsecTunSelectorExpire_Type()
)
fextInfoIPsecTunSelectorExpire.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoIPsecTunSelectorExpire.setStatus("current")
_FextInfoIPsecTunSelectorSrcNet_Type = DisplayString
_FextInfoIPsecTunSelectorSrcNet_Object = MibTableColumn
fextInfoIPsecTunSelectorSrcNet = _FextInfoIPsecTunSelectorSrcNet_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 6, 1, 2, 1, 5),
    _FextInfoIPsecTunSelectorSrcNet_Type()
)
fextInfoIPsecTunSelectorSrcNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoIPsecTunSelectorSrcNet.setStatus("current")
_FextInfoIPsecTunSelectorDstNet_Type = DisplayString
_FextInfoIPsecTunSelectorDstNet_Object = MibTableColumn
fextInfoIPsecTunSelectorDstNet = _FextInfoIPsecTunSelectorDstNet_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 6, 1, 2, 1, 6),
    _FextInfoIPsecTunSelectorDstNet_Type()
)
fextInfoIPsecTunSelectorDstNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoIPsecTunSelectorDstNet.setStatus("current")
_FextInfoIPsecTunSelectorSrcPort_Type = Integer32
_FextInfoIPsecTunSelectorSrcPort_Object = MibTableColumn
fextInfoIPsecTunSelectorSrcPort = _FextInfoIPsecTunSelectorSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 6, 1, 2, 1, 7),
    _FextInfoIPsecTunSelectorSrcPort_Type()
)
fextInfoIPsecTunSelectorSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoIPsecTunSelectorSrcPort.setStatus("current")
_FextInfoIPsecTunSelectorDstPort_Type = Integer32
_FextInfoIPsecTunSelectorDstPort_Object = MibTableColumn
fextInfoIPsecTunSelectorDstPort = _FextInfoIPsecTunSelectorDstPort_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 6, 1, 2, 1, 8),
    _FextInfoIPsecTunSelectorDstPort_Type()
)
fextInfoIPsecTunSelectorDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoIPsecTunSelectorDstPort.setStatus("current")
_FextInfoIPsecTunSelectorProto_Type = Integer32
_FextInfoIPsecTunSelectorProto_Object = MibTableColumn
fextInfoIPsecTunSelectorProto = _FextInfoIPsecTunSelectorProto_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 6, 1, 2, 1, 9),
    _FextInfoIPsecTunSelectorProto_Type()
)
fextInfoIPsecTunSelectorProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoIPsecTunSelectorProto.setStatus("current")
_FextInfoIPsecTunSelectorInBytes_Type = Counter64
_FextInfoIPsecTunSelectorInBytes_Object = MibTableColumn
fextInfoIPsecTunSelectorInBytes = _FextInfoIPsecTunSelectorInBytes_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 6, 1, 2, 1, 10),
    _FextInfoIPsecTunSelectorInBytes_Type()
)
fextInfoIPsecTunSelectorInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoIPsecTunSelectorInBytes.setStatus("current")
_FextInfoIPsecTunSelectorOutBytes_Type = Counter64
_FextInfoIPsecTunSelectorOutBytes_Object = MibTableColumn
fextInfoIPsecTunSelectorOutBytes = _FextInfoIPsecTunSelectorOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 6, 1, 2, 1, 11),
    _FextInfoIPsecTunSelectorOutBytes_Type()
)
fextInfoIPsecTunSelectorOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoIPsecTunSelectorOutBytes.setStatus("current")
_FextInfoVPNCert_ObjectIdentity = ObjectIdentity
fextInfoVPNCert = _FextInfoVPNCert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 6, 2)
)
_FextInfoVPNCertCA_Object = MibTable
fextInfoVPNCertCA = _FextInfoVPNCertCA_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 6, 2, 1)
)
if mibBuilder.loadTexts:
    fextInfoVPNCertCA.setStatus("current")
_FextInfoVPNCertCAEntry_Object = MibTableRow
fextInfoVPNCertCAEntry = _FextInfoVPNCertCAEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 6, 2, 1, 1)
)
fextInfoVPNCertCAEntry.setIndexNames(
    (0, "FORTINET-FORTIEXTENDER-MIB", "fextInfoVPNCertCAIndex"),
)
if mibBuilder.loadTexts:
    fextInfoVPNCertCAEntry.setStatus("current")
_FextInfoVPNCertCAIndex_Type = FnIndex
_FextInfoVPNCertCAIndex_Object = MibTableColumn
fextInfoVPNCertCAIndex = _FextInfoVPNCertCAIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 6, 2, 1, 1, 1),
    _FextInfoVPNCertCAIndex_Type()
)
fextInfoVPNCertCAIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fextInfoVPNCertCAIndex.setStatus("current")
_FextInfoVPNCertCAName_Type = DisplayString
_FextInfoVPNCertCAName_Object = MibTableColumn
fextInfoVPNCertCAName = _FextInfoVPNCertCAName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 6, 2, 1, 1, 2),
    _FextInfoVPNCertCAName_Type()
)
fextInfoVPNCertCAName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoVPNCertCAName.setStatus("current")
_FextInfoVPNCertCAStatus_Type = DisplayString
_FextInfoVPNCertCAStatus_Object = MibTableColumn
fextInfoVPNCertCAStatus = _FextInfoVPNCertCAStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 6, 2, 1, 1, 3),
    _FextInfoVPNCertCAStatus_Type()
)
fextInfoVPNCertCAStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoVPNCertCAStatus.setStatus("current")
_FextInfoVPNCertCASubject_Type = DisplayString
_FextInfoVPNCertCASubject_Object = MibTableColumn
fextInfoVPNCertCASubject = _FextInfoVPNCertCASubject_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 6, 2, 1, 1, 4),
    _FextInfoVPNCertCASubject_Type()
)
fextInfoVPNCertCASubject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoVPNCertCASubject.setStatus("current")
_FextInfoVPNCertCAIssuer_Type = DisplayString
_FextInfoVPNCertCAIssuer_Object = MibTableColumn
fextInfoVPNCertCAIssuer = _FextInfoVPNCertCAIssuer_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 6, 2, 1, 1, 5),
    _FextInfoVPNCertCAIssuer_Type()
)
fextInfoVPNCertCAIssuer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoVPNCertCAIssuer.setStatus("current")
_FextInfoVPNCertCAValidFrom_Type = DisplayString
_FextInfoVPNCertCAValidFrom_Object = MibTableColumn
fextInfoVPNCertCAValidFrom = _FextInfoVPNCertCAValidFrom_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 6, 2, 1, 1, 6),
    _FextInfoVPNCertCAValidFrom_Type()
)
fextInfoVPNCertCAValidFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoVPNCertCAValidFrom.setStatus("current")
_FextInfoVPNCertCAValidTo_Type = DisplayString
_FextInfoVPNCertCAValidTo_Object = MibTableColumn
fextInfoVPNCertCAValidTo = _FextInfoVPNCertCAValidTo_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 6, 2, 1, 1, 7),
    _FextInfoVPNCertCAValidTo_Type()
)
fextInfoVPNCertCAValidTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoVPNCertCAValidTo.setStatus("current")
_FextInfoVPNCertCAFingerprint_Type = DisplayString
_FextInfoVPNCertCAFingerprint_Object = MibTableColumn
fextInfoVPNCertCAFingerprint = _FextInfoVPNCertCAFingerprint_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 6, 2, 1, 1, 8),
    _FextInfoVPNCertCAFingerprint_Type()
)
fextInfoVPNCertCAFingerprint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoVPNCertCAFingerprint.setStatus("current")
_FextInfoVPNCertCASerialNum_Type = DisplayString
_FextInfoVPNCertCASerialNum_Object = MibTableColumn
fextInfoVPNCertCASerialNum = _FextInfoVPNCertCASerialNum_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 6, 2, 1, 1, 9),
    _FextInfoVPNCertCASerialNum_Type()
)
fextInfoVPNCertCASerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoVPNCertCASerialNum.setStatus("current")
_FextInfoVPNCertLocal_Object = MibTable
fextInfoVPNCertLocal = _FextInfoVPNCertLocal_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 6, 2, 2)
)
if mibBuilder.loadTexts:
    fextInfoVPNCertLocal.setStatus("current")
_FextInfoVPNCertLocalEntry_Object = MibTableRow
fextInfoVPNCertLocalEntry = _FextInfoVPNCertLocalEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 6, 2, 2, 1)
)
fextInfoVPNCertLocalEntry.setIndexNames(
    (0, "FORTINET-FORTIEXTENDER-MIB", "fextInfoVPNCertLocIndex"),
)
if mibBuilder.loadTexts:
    fextInfoVPNCertLocalEntry.setStatus("current")
_FextInfoVPNCertLocIndex_Type = FnIndex
_FextInfoVPNCertLocIndex_Object = MibTableColumn
fextInfoVPNCertLocIndex = _FextInfoVPNCertLocIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 6, 2, 2, 1, 1),
    _FextInfoVPNCertLocIndex_Type()
)
fextInfoVPNCertLocIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fextInfoVPNCertLocIndex.setStatus("current")
_FextInfoVPNCertLocName_Type = DisplayString
_FextInfoVPNCertLocName_Object = MibTableColumn
fextInfoVPNCertLocName = _FextInfoVPNCertLocName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 6, 2, 2, 1, 2),
    _FextInfoVPNCertLocName_Type()
)
fextInfoVPNCertLocName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoVPNCertLocName.setStatus("current")
_FextInfoVPNCertLocStatus_Type = DisplayString
_FextInfoVPNCertLocStatus_Object = MibTableColumn
fextInfoVPNCertLocStatus = _FextInfoVPNCertLocStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 6, 2, 2, 1, 3),
    _FextInfoVPNCertLocStatus_Type()
)
fextInfoVPNCertLocStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoVPNCertLocStatus.setStatus("current")
_FextInfoVPNCertLocSubject_Type = DisplayString
_FextInfoVPNCertLocSubject_Object = MibTableColumn
fextInfoVPNCertLocSubject = _FextInfoVPNCertLocSubject_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 6, 2, 2, 1, 4),
    _FextInfoVPNCertLocSubject_Type()
)
fextInfoVPNCertLocSubject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoVPNCertLocSubject.setStatus("current")
_FextInfoVPNCertLocIssuer_Type = DisplayString
_FextInfoVPNCertLocIssuer_Object = MibTableColumn
fextInfoVPNCertLocIssuer = _FextInfoVPNCertLocIssuer_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 6, 2, 2, 1, 5),
    _FextInfoVPNCertLocIssuer_Type()
)
fextInfoVPNCertLocIssuer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoVPNCertLocIssuer.setStatus("current")
_FextInfoVPNCertLocValidFrom_Type = DisplayString
_FextInfoVPNCertLocValidFrom_Object = MibTableColumn
fextInfoVPNCertLocValidFrom = _FextInfoVPNCertLocValidFrom_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 6, 2, 2, 1, 6),
    _FextInfoVPNCertLocValidFrom_Type()
)
fextInfoVPNCertLocValidFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoVPNCertLocValidFrom.setStatus("current")
_FextInfoVPNCertLocValidTo_Type = DisplayString
_FextInfoVPNCertLocValidTo_Object = MibTableColumn
fextInfoVPNCertLocValidTo = _FextInfoVPNCertLocValidTo_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 6, 2, 2, 1, 7),
    _FextInfoVPNCertLocValidTo_Type()
)
fextInfoVPNCertLocValidTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoVPNCertLocValidTo.setStatus("current")
_FextInfoVPNCertLocFingerprint_Type = DisplayString
_FextInfoVPNCertLocFingerprint_Object = MibTableColumn
fextInfoVPNCertLocFingerprint = _FextInfoVPNCertLocFingerprint_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 6, 2, 2, 1, 8),
    _FextInfoVPNCertLocFingerprint_Type()
)
fextInfoVPNCertLocFingerprint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoVPNCertLocFingerprint.setStatus("current")
_FextInfoVPNCertLocSerialNum_Type = DisplayString
_FextInfoVPNCertLocSerialNum_Object = MibTableColumn
fextInfoVPNCertLocSerialNum = _FextInfoVPNCertLocSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 6, 2, 2, 1, 9),
    _FextInfoVPNCertLocSerialNum_Type()
)
fextInfoVPNCertLocSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoVPNCertLocSerialNum.setStatus("current")
_FextInfoHMon_ObjectIdentity = ObjectIdentity
fextInfoHMon = _FextInfoHMon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 7)
)
_FextInfoHMonIfStat_Object = MibTable
fextInfoHMonIfStat = _FextInfoHMonIfStat_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 7, 1)
)
if mibBuilder.loadTexts:
    fextInfoHMonIfStat.setStatus("current")
_FextInfoHMonIfStatEntry_Object = MibTableRow
fextInfoHMonIfStatEntry = _FextInfoHMonIfStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 7, 1, 1)
)
fextInfoHMonIfStatEntry.setIndexNames(
    (0, "FORTINET-FORTIEXTENDER-MIB", "fextInfoHMonIfStatIndex"),
)
if mibBuilder.loadTexts:
    fextInfoHMonIfStatEntry.setStatus("current")
_FextInfoHMonIfStatIndex_Type = FnIndex
_FextInfoHMonIfStatIndex_Object = MibTableColumn
fextInfoHMonIfStatIndex = _FextInfoHMonIfStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 7, 1, 1, 1),
    _FextInfoHMonIfStatIndex_Type()
)
fextInfoHMonIfStatIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fextInfoHMonIfStatIndex.setStatus("current")
_FextInfoHMonIfStatMonitor_Type = DisplayString
_FextInfoHMonIfStatMonitor_Object = MibTableColumn
fextInfoHMonIfStatMonitor = _FextInfoHMonIfStatMonitor_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 7, 1, 1, 2),
    _FextInfoHMonIfStatMonitor_Type()
)
fextInfoHMonIfStatMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoHMonIfStatMonitor.setStatus("current")
_FextInfoHMonIfStatIfName_Type = DisplayString
_FextInfoHMonIfStatIfName_Object = MibTableColumn
fextInfoHMonIfStatIfName = _FextInfoHMonIfStatIfName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 7, 1, 1, 3),
    _FextInfoHMonIfStatIfName_Type()
)
fextInfoHMonIfStatIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoHMonIfStatIfName.setStatus("current")
_FextInfoHMonIfStatRxBytes_Type = Counter64
_FextInfoHMonIfStatRxBytes_Object = MibTableColumn
fextInfoHMonIfStatRxBytes = _FextInfoHMonIfStatRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 7, 1, 1, 4),
    _FextInfoHMonIfStatRxBytes_Type()
)
fextInfoHMonIfStatRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoHMonIfStatRxBytes.setStatus("current")
_FextInfoHMonIfStatTxBytes_Type = Counter64
_FextInfoHMonIfStatTxBytes_Object = MibTableColumn
fextInfoHMonIfStatTxBytes = _FextInfoHMonIfStatTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 7, 1, 1, 5),
    _FextInfoHMonIfStatTxBytes_Type()
)
fextInfoHMonIfStatTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoHMonIfStatTxBytes.setStatus("current")
_FextInfoHMonIfStatRxPkts_Type = Counter64
_FextInfoHMonIfStatRxPkts_Object = MibTableColumn
fextInfoHMonIfStatRxPkts = _FextInfoHMonIfStatRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 7, 1, 1, 6),
    _FextInfoHMonIfStatRxPkts_Type()
)
fextInfoHMonIfStatRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoHMonIfStatRxPkts.setStatus("current")
_FextInfoHMonIfStatTxPkts_Type = Counter64
_FextInfoHMonIfStatTxPkts_Object = MibTableColumn
fextInfoHMonIfStatTxPkts = _FextInfoHMonIfStatTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 7, 1, 1, 7),
    _FextInfoHMonIfStatTxPkts_Type()
)
fextInfoHMonIfStatTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoHMonIfStatTxPkts.setStatus("current")
_FextInfoHMonIfStatRxDropped_Type = Counter64
_FextInfoHMonIfStatRxDropped_Object = MibTableColumn
fextInfoHMonIfStatRxDropped = _FextInfoHMonIfStatRxDropped_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 7, 1, 1, 8),
    _FextInfoHMonIfStatRxDropped_Type()
)
fextInfoHMonIfStatRxDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoHMonIfStatRxDropped.setStatus("current")
_FextInfoHMonIfStatTxDropped_Type = Counter64
_FextInfoHMonIfStatTxDropped_Object = MibTableColumn
fextInfoHMonIfStatTxDropped = _FextInfoHMonIfStatTxDropped_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 7, 1, 1, 9),
    _FextInfoHMonIfStatTxDropped_Type()
)
fextInfoHMonIfStatTxDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoHMonIfStatTxDropped.setStatus("current")
_FextInfoHMonIfStatRxBps_Type = Counter64
_FextInfoHMonIfStatRxBps_Object = MibTableColumn
fextInfoHMonIfStatRxBps = _FextInfoHMonIfStatRxBps_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 7, 1, 1, 10),
    _FextInfoHMonIfStatRxBps_Type()
)
fextInfoHMonIfStatRxBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoHMonIfStatRxBps.setStatus("current")
_FextInfoHMonIfStatTxBps_Type = Counter64
_FextInfoHMonIfStatTxBps_Object = MibTableColumn
fextInfoHMonIfStatTxBps = _FextInfoHMonIfStatTxBps_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 7, 1, 1, 11),
    _FextInfoHMonIfStatTxBps_Type()
)
fextInfoHMonIfStatTxBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoHMonIfStatTxBps.setStatus("current")
_FextInfoHMonIfStatRxPps_Type = Counter64
_FextInfoHMonIfStatRxPps_Object = MibTableColumn
fextInfoHMonIfStatRxPps = _FextInfoHMonIfStatRxPps_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 7, 1, 1, 12),
    _FextInfoHMonIfStatRxPps_Type()
)
fextInfoHMonIfStatRxPps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoHMonIfStatRxPps.setStatus("current")
_FextInfoHMonIfStatTxPps_Type = Counter64
_FextInfoHMonIfStatTxPps_Object = MibTableColumn
fextInfoHMonIfStatTxPps = _FextInfoHMonIfStatTxPps_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 7, 1, 1, 13),
    _FextInfoHMonIfStatTxPps_Type()
)
fextInfoHMonIfStatTxPps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoHMonIfStatTxPps.setStatus("current")
_FextInfoHMonHChkStat_Object = MibTable
fextInfoHMonHChkStat = _FextInfoHMonHChkStat_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 7, 2)
)
if mibBuilder.loadTexts:
    fextInfoHMonHChkStat.setStatus("current")
_FextInfoHMonHChkStatEntry_Object = MibTableRow
fextInfoHMonHChkStatEntry = _FextInfoHMonHChkStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 7, 2, 1)
)
fextInfoHMonHChkStatEntry.setIndexNames(
    (0, "FORTINET-FORTIEXTENDER-MIB", "fextInfoHMonHChkStatIndex"),
)
if mibBuilder.loadTexts:
    fextInfoHMonHChkStatEntry.setStatus("current")
_FextInfoHMonHChkStatIndex_Type = FnIndex
_FextInfoHMonHChkStatIndex_Object = MibTableColumn
fextInfoHMonHChkStatIndex = _FextInfoHMonHChkStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 7, 2, 1, 1),
    _FextInfoHMonHChkStatIndex_Type()
)
fextInfoHMonHChkStatIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fextInfoHMonHChkStatIndex.setStatus("current")
_FextInfoHMonHChkStatMonitor_Type = DisplayString
_FextInfoHMonHChkStatMonitor_Object = MibTableColumn
fextInfoHMonHChkStatMonitor = _FextInfoHMonHChkStatMonitor_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 7, 2, 1, 2),
    _FextInfoHMonHChkStatMonitor_Type()
)
fextInfoHMonHChkStatMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoHMonHChkStatMonitor.setStatus("current")
_FextInfoHMonHChkStatIfName_Type = DisplayString
_FextInfoHMonHChkStatIfName_Object = MibTableColumn
fextInfoHMonHChkStatIfName = _FextInfoHMonHChkStatIfName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 7, 2, 1, 3),
    _FextInfoHMonHChkStatIfName_Type()
)
fextInfoHMonHChkStatIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoHMonHChkStatIfName.setStatus("current")
_FextInfoHMonHChkStatRttAvg_Type = DisplayString
_FextInfoHMonHChkStatRttAvg_Object = MibTableColumn
fextInfoHMonHChkStatRttAvg = _FextInfoHMonHChkStatRttAvg_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 7, 2, 1, 4),
    _FextInfoHMonHChkStatRttAvg_Type()
)
fextInfoHMonHChkStatRttAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoHMonHChkStatRttAvg.setStatus("current")
_FextInfoHMonHChkStatRttMax_Type = DisplayString
_FextInfoHMonHChkStatRttMax_Object = MibTableColumn
fextInfoHMonHChkStatRttMax = _FextInfoHMonHChkStatRttMax_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 7, 2, 1, 5),
    _FextInfoHMonHChkStatRttMax_Type()
)
fextInfoHMonHChkStatRttMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoHMonHChkStatRttMax.setStatus("current")
_FextInfoHMonHChkStatRttMin_Type = DisplayString
_FextInfoHMonHChkStatRttMin_Object = MibTableColumn
fextInfoHMonHChkStatRttMin = _FextInfoHMonHChkStatRttMin_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 7, 2, 1, 6),
    _FextInfoHMonHChkStatRttMin_Type()
)
fextInfoHMonHChkStatRttMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoHMonHChkStatRttMin.setStatus("current")
_FextInfoHMonHChkStatRttNow_Type = DisplayString
_FextInfoHMonHChkStatRttNow_Object = MibTableColumn
fextInfoHMonHChkStatRttNow = _FextInfoHMonHChkStatRttNow_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 7, 2, 1, 7),
    _FextInfoHMonHChkStatRttNow_Type()
)
fextInfoHMonHChkStatRttNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoHMonHChkStatRttNow.setStatus("current")
_FextInfoHMonHChkStatRttSd_Type = DisplayString
_FextInfoHMonHChkStatRttSd_Object = MibTableColumn
fextInfoHMonHChkStatRttSd = _FextInfoHMonHChkStatRttSd_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 7, 2, 1, 8),
    _FextInfoHMonHChkStatRttSd_Type()
)
fextInfoHMonHChkStatRttSd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoHMonHChkStatRttSd.setStatus("current")
_FextInfoHMonHChkStatRttAmsd_Type = DisplayString
_FextInfoHMonHChkStatRttAmsd_Object = MibTableColumn
fextInfoHMonHChkStatRttAmsd = _FextInfoHMonHChkStatRttAmsd_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 7, 2, 1, 9),
    _FextInfoHMonHChkStatRttAmsd_Type()
)
fextInfoHMonHChkStatRttAmsd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoHMonHChkStatRttAmsd.setStatus("current")
_FextInfoHMonHChkStatLossAvg_Type = DisplayString
_FextInfoHMonHChkStatLossAvg_Object = MibTableColumn
fextInfoHMonHChkStatLossAvg = _FextInfoHMonHChkStatLossAvg_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 7, 2, 1, 10),
    _FextInfoHMonHChkStatLossAvg_Type()
)
fextInfoHMonHChkStatLossAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoHMonHChkStatLossAvg.setStatus("current")
_FextInfoHMonHChkStatLossMax_Type = DisplayString
_FextInfoHMonHChkStatLossMax_Object = MibTableColumn
fextInfoHMonHChkStatLossMax = _FextInfoHMonHChkStatLossMax_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 7, 2, 1, 11),
    _FextInfoHMonHChkStatLossMax_Type()
)
fextInfoHMonHChkStatLossMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoHMonHChkStatLossMax.setStatus("current")
_FextInfoHMonHChkStatLossMin_Type = DisplayString
_FextInfoHMonHChkStatLossMin_Object = MibTableColumn
fextInfoHMonHChkStatLossMin = _FextInfoHMonHChkStatLossMin_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 7, 2, 1, 12),
    _FextInfoHMonHChkStatLossMin_Type()
)
fextInfoHMonHChkStatLossMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoHMonHChkStatLossMin.setStatus("current")
_FextInfoHMonHChkStatLossNow_Type = DisplayString
_FextInfoHMonHChkStatLossNow_Object = MibTableColumn
fextInfoHMonHChkStatLossNow = _FextInfoHMonHChkStatLossNow_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 7, 2, 1, 13),
    _FextInfoHMonHChkStatLossNow_Type()
)
fextInfoHMonHChkStatLossNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoHMonHChkStatLossNow.setStatus("current")
_FextInfoCPM_ObjectIdentity = ObjectIdentity
fextInfoCPM = _FextInfoCPM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 8)
)
_FextInfoCPMStatus_ObjectIdentity = ObjectIdentity
fextInfoCPMStatus = _FextInfoCPMStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 8, 1)
)
if mibBuilder.loadTexts:
    fextInfoCPMStatus.setStatus("current")
_FextInfoCPMProcessID_Type = DisplayString
_FextInfoCPMProcessID_Object = MibScalar
fextInfoCPMProcessID = _FextInfoCPMProcessID_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 8, 1, 1),
    _FextInfoCPMProcessID_Type()
)
fextInfoCPMProcessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoCPMProcessID.setStatus("current")
_FextInfoCPMConnectStatus_Type = DisplayString
_FextInfoCPMConnectStatus_Object = MibScalar
fextInfoCPMConnectStatus = _FextInfoCPMConnectStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 8, 1, 2),
    _FextInfoCPMConnectStatus_Type()
)
fextInfoCPMConnectStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoCPMConnectStatus.setStatus("current")
_FextInfoCPMCloudSSLHost_Type = DisplayString
_FextInfoCPMCloudSSLHost_Object = MibScalar
fextInfoCPMCloudSSLHost = _FextInfoCPMCloudSSLHost_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 8, 1, 3),
    _FextInfoCPMCloudSSLHost_Type()
)
fextInfoCPMCloudSSLHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoCPMCloudSSLHost.setStatus("current")
_FextInfoCPMCloudSSLPort_Type = DisplayString
_FextInfoCPMCloudSSLPort_Object = MibScalar
fextInfoCPMCloudSSLPort = _FextInfoCPMCloudSSLPort_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 8, 1, 4),
    _FextInfoCPMCloudSSLPort_Type()
)
fextInfoCPMCloudSSLPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoCPMCloudSSLPort.setStatus("current")
_FextInfoCPMReconnectCount_Type = DisplayString
_FextInfoCPMReconnectCount_Object = MibScalar
fextInfoCPMReconnectCount = _FextInfoCPMReconnectCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 121, 21, 8, 1, 5),
    _FextInfoCPMReconnectCount_Type()
)
fextInfoCPMReconnectCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fextInfoCPMReconnectCount.setStatus("current")
_FextTraps_ObjectIdentity = ObjectIdentity
fextTraps = _FextTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 100)
)
_FextModel_ObjectIdentity = ObjectIdentity
fextModel = _FextModel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 200)
)
_FextUnknown_ObjectIdentity = ObjectIdentity
fextUnknown = _FextUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 200, 1)
)
_FextVM_ObjectIdentity = ObjectIdentity
fextVM = _FextVM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 200, 10)
)
_Fext20D_ObjectIdentity = ObjectIdentity
fext20D = _Fext20D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 200, 21)
)
_Fext40D_ObjectIdentity = ObjectIdentity
fext40D = _Fext40D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 200, 41)
)
_Fext40DA_ObjectIdentity = ObjectIdentity
fext40DA = _Fext40DA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 200, 42)
)
_Fext200F_ObjectIdentity = ObjectIdentity
fext200F = _Fext200F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 200, 200)
)
_Fext201E_ObjectIdentity = ObjectIdentity
fext201E = _Fext201E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 200, 201)
)
_Fext202E_ObjectIdentity = ObjectIdentity
fext202E = _Fext202E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 200, 202)
)
_Fext211E_ObjectIdentity = ObjectIdentity
fext211E = _Fext211E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 200, 211)
)
_Fext212E_ObjectIdentity = ObjectIdentity
fext212E = _Fext212E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 200, 212)
)
_Fext30GWifi_ObjectIdentity = ObjectIdentity
fext30GWifi = _Fext30GWifi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 200, 301)
)
_Fext311F_ObjectIdentity = ObjectIdentity
fext311F = _Fext311F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 200, 311)
)
_Fext312F_ObjectIdentity = ObjectIdentity
fext312F = _Fext312F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 200, 312)
)
_Fext511F_ObjectIdentity = ObjectIdentity
fext511F = _Fext511F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 200, 511)
)
_FextF11A_ObjectIdentity = ObjectIdentity
fextF11A = _FextF11A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 200, 1011)
)
_FextF11E_ObjectIdentity = ObjectIdentity
fextF11E = _FextF11E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 200, 1012)
)
_Fer511G_ObjectIdentity = ObjectIdentity
fer511G = _Fer511G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 200, 1511)
)
_FextF21A_ObjectIdentity = ObjectIdentity
fextF21A = _FextF21A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 200, 2011)
)
_FextF21E_ObjectIdentity = ObjectIdentity
fextF21E = _FextF21E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 200, 2012)
)
_FextF22A_ObjectIdentity = ObjectIdentity
fextF22A = _FextF22A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 200, 2021)
)
_FextF22E_ObjectIdentity = ObjectIdentity
fextF22E = _FextF22E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 200, 2022)
)
_Fev211FA_ObjectIdentity = ObjectIdentity
fev211FA = _Fev211FA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 200, 2111)
)
_Fev211F_ObjectIdentity = ObjectIdentity
fev211F = _Fev211F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 200, 2112)
)
_Fext212F_ObjectIdentity = ObjectIdentity
fext212F = _Fext212F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 200, 2121)
)
_Fev212FA_ObjectIdentity = ObjectIdentity
fev212FA = _Fev212FA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 200, 2121)
)
_Fev212F_ObjectIdentity = ObjectIdentity
fev212F = _Fev212F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 121, 200, 2122)
)
ifEntry.registerAugmentions(
    ("FORTINET-FORTIEXTENDER-MIB",
     "fextInfoInterfaceEntry")
)
fextInfoInterfaceEntry.setIndexNames(*ifEntry.getIndexNames())

# Managed Objects groups


# Notification objects

fextTrapSystemReboot = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 121, 100, 101)
)
fextTrapSystemReboot.setObjects(
    ("FORTINET-FORTIEXTENDER-MIB", "fextInfoEXTDHostName")
)
if mibBuilder.loadTexts:
    fextTrapSystemReboot.setStatus(
        "current"
    )

fextTrapOSImageFallback = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 121, 100, 102)
)
fextTrapOSImageFallback.setObjects(
    ("FORTINET-FORTIEXTENDER-MIB", "fextInfoEXTDHostName")
)
if mibBuilder.loadTexts:
    fextTrapOSImageFallback.setStatus(
        "current"
    )

fextTrapModeSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 121, 100, 103)
)
fextTrapModeSwitch.setObjects(
    ("FORTINET-FORTIEXTENDER-MIB", "fextInfoEXTDHostName")
)
if mibBuilder.loadTexts:
    fextTrapModeSwitch.setStatus(
        "current"
    )

fextTrapFGTBackupModeSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 121, 100, 104)
)
fextTrapFGTBackupModeSwitch.setObjects(
    ("FORTINET-FORTIEXTENDER-MIB", "fextInfoEXTDHostName")
)
if mibBuilder.loadTexts:
    fextTrapFGTBackupModeSwitch.setStatus(
        "current"
    )

fextTrapDataExhausted = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 121, 100, 201)
)
fextTrapDataExhausted.setObjects(
    ("FORTINET-FORTIEXTENDER-MIB", "fextInfoEXTDHostName")
)
if mibBuilder.loadTexts:
    fextTrapDataExhausted.setStatus(
        "current"
    )

fextTrapSessionDisconnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 121, 100, 202)
)
fextTrapSessionDisconnect.setObjects(
    ("FORTINET-FORTIEXTENDER-MIB", "fextInfoEXTDHostName")
)
if mibBuilder.loadTexts:
    fextTrapSessionDisconnect.setStatus(
        "current"
    )

fextTrapLowSignalStrength = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 121, 100, 203)
)
fextTrapLowSignalStrength.setObjects(
    ("FORTINET-FORTIEXTENDER-MIB", "fextInfoEXTDHostName")
)
if mibBuilder.loadTexts:
    fextTrapLowSignalStrength.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FORTINET-FORTIEXTENDER-MIB",
    **{"fnFortiExtenderMib": fnFortiExtenderMib,
       "fextHeader": fextHeader,
       "fextVersion": fextVersion,
       "fextVersionConfig": fextVersionConfig,
       "fextVersionCarrier": fextVersionCarrier,
       "fextVersionSimmap": fextVersionSimmap,
       "fextSystem": fextSystem,
       "fextGlobal": fextGlobal,
       "fextHostname": fextHostname,
       "fextTimezone": fextTimezone,
       "fextAutoInstallImage": fextAutoInstallImage,
       "fextDefaultImageFile": fextDefaultImageFile,
       "fextMDMFWServer": fextMDMFWServer,
       "fextOSFWServer": fextOSFWServer,
       "fextManagement": fextManagement,
       "fextMgmtDiscoveryType": fextMgmtDiscoveryType,
       "fextMgmtFortigate": fextMgmtFortigate,
       "fextFGTDiscoveryType": fextFGTDiscoveryType,
       "fextFGTStaticIP": fextFGTStaticIP,
       "fextFGTControlPort": fextFGTControlPort,
       "fextFGTDataPort": fextFGTDataPort,
       "fextFGTDiscoveryIntf": fextFGTDiscoveryIntf,
       "fextFGTIngressIntf": fextFGTIngressIntf,
       "fextMgmtCloud": fextMgmtCloud,
       "fextCloudDispatcher": fextCloudDispatcher,
       "fextCloudDispatcherPort": fextCloudDispatcherPort,
       "fextCloudMode": fextCloudMode,
       "fextCloudProxy": fextCloudProxy,
       "fextCloudProxyServer": fextCloudProxyServer,
       "fextCloudProxyPort": fextCloudProxyPort,
       "fextMgmtLocal": fextMgmtLocal,
       "fextLocalMode": fextLocalMode,
       "fextMgmtLocalAccess": fextMgmtLocalAccess,
       "fextAccessHTTP": fextAccessHTTP,
       "fextAccessHTTPS": fextAccessHTTPS,
       "fextAccessSSH": fextAccessSSH,
       "fextAccessTelnet": fextAccessTelnet,
       "fextAccessTimeout": fextAccessTimeout,
       "fextMgmtFGTBackup": fextMgmtFGTBackup,
       "fextBackupVRRPInterface": fextBackupVRRPInterface,
       "fextBackupStatus": fextBackupStatus,
       "fextInterface": fextInterface,
       "fextInterfaceEntry": fextInterfaceEntry,
       "fextInterfaceIndex": fextInterfaceIndex,
       "fextInterfaceName": fextInterfaceName,
       "fextInterfaceType": fextInterfaceType,
       "fextInterfaceStatus": fextInterfaceStatus,
       "fextInterfaceMode": fextInterfaceMode,
       "fextInterfaceIP": fextInterfaceIP,
       "fextInterfaceIPMask": fextInterfaceIPMask,
       "fextInterfaceGateway": fextInterfaceGateway,
       "fextInterfaceMTUOverride": fextInterfaceMTUOverride,
       "fextInterfaceMTU": fextInterfaceMTU,
       "fextInterfaceRID": fextInterfaceRID,
       "fextInterfaceVID": fextInterfaceVID,
       "fextInterfaceIngressIntf": fextInterfaceIngressIntf,
       "fextInterfaceVRRPVirtualMAC": fextInterfaceVRRPVirtualMAC,
       "fextInterfaceAllowAccess": fextInterfaceAllowAccess,
       "fextInterfaceAlgorithm": fextInterfaceAlgorithm,
       "fextInterfaceFEC": fextInterfaceFEC,
       "fextInterfaceSessionTimeout": fextInterfaceSessionTimeout,
       "fextInterfaceGracePeriod": fextInterfaceGracePeriod,
       "fextInterfaceMembers": fextInterfaceMembers,
       "fextDHCPServer": fextDHCPServer,
       "fextDHCPServerEntry": fextDHCPServerEntry,
       "fextDHCPServerIndex": fextDHCPServerIndex,
       "fextDHCPServerName": fextDHCPServerName,
       "fextDHCPServerStatus": fextDHCPServerStatus,
       "fextDHCPServerLeaseTime": fextDHCPServerLeaseTime,
       "fextDHCPServerDNS": fextDHCPServerDNS,
       "fextDHCPServerNTP": fextDHCPServerNTP,
       "fextDHCPServerNTP1": fextDHCPServerNTP1,
       "fextDHCPServerNTP2": fextDHCPServerNTP2,
       "fextDHCPServerNTP3": fextDHCPServerNTP3,
       "fextDHCPServerGatewayIP": fextDHCPServerGatewayIP,
       "fextDHCPServerNetmask": fextDHCPServerNetmask,
       "fextDHCPServerInterface": fextDHCPServerInterface,
       "fextDHCPServerStartIP": fextDHCPServerStartIP,
       "fextDHCPServerEndIP": fextDHCPServerEndIP,
       "fextDHCPServerMTU": fextDHCPServerMTU,
       "fextDNS": fextDNS,
       "fextDNSPrimary": fextDNSPrimary,
       "fextDNSSecondary": fextDNSSecondary,
       "fextDNSOrder": fextDNSOrder,
       "fextVWANMember": fextVWANMember,
       "fextVWANMemberEntry": fextVWANMemberEntry,
       "fextVWANMemberIndex": fextVWANMemberIndex,
       "fextVWANMemberName": fextVWANMemberName,
       "fextVWANMemberTarget": fextVWANMemberTarget,
       "fextVWANMemberPriority": fextVWANMemberPriority,
       "fextVWANMemberWeight": fextVWANMemberWeight,
       "fextVWANMemberInThreshold": fextVWANMemberInThreshold,
       "fextVWANMemberOutThreshold": fextVWANMemberOutThreshold,
       "fextVWANMemberAllThreshold": fextVWANMemberAllThreshold,
       "fextVWANMemberHchk": fextVWANMemberHchk,
       "fextVWANMemberHchkFailThreshold": fextVWANMemberHchkFailThreshold,
       "fextVWANMemberHchkSuccessThreshold": fextVWANMemberHchkSuccessThreshold,
       "fextVWANHchk": fextVWANHchk,
       "fextVWANHchkEntry": fextVWANHchkEntry,
       "fextVWANHchkIndex": fextVWANHchkIndex,
       "fextVWANHchkName": fextVWANHchkName,
       "fextVWANHchkProtocol": fextVWANHchkProtocol,
       "fextVWANHchkInterval": fextVWANHchkInterval,
       "fextVWANHchkProbeCount": fextVWANHchkProbeCount,
       "fextVWANHchkProbeTimeout": fextVWANHchkProbeTimeout,
       "fextVWANHchkProbeTarget": fextVWANHchkProbeTarget,
       "fextVWANHchkPort": fextVWANHchkPort,
       "fextVWANHchkHTTPGet": fextVWANHchkHTTPGet,
       "fextVWANHchkSourceInterface": fextVWANHchkSourceInterface,
       "fextVWANHchkFailCount": fextVWANHchkFailCount,
       "fextVWANHchkRecoveryCount": fextVWANHchkRecoveryCount,
       "fextSMSNotification": fextSMSNotification,
       "fextSMSNotify": fextSMSNotify,
       "fextSMSReceiver": fextSMSReceiver,
       "fextSMSReceiverEntry": fextSMSReceiverEntry,
       "fextSMSReceiverIndex": fextSMSReceiverIndex,
       "fextSMSReceiverName": fextSMSReceiverName,
       "fextSMSReceiverRcvr": fextSMSReceiverRcvr,
       "fextSMSReceiverNumber": fextSMSReceiverNumber,
       "fextSMSReceiverAlert": fextSMSReceiverAlert,
       "fextSMSAlert": fextSMSAlert,
       "fextSMSAlertSystemReboot": fextSMSAlertSystemReboot,
       "fextSMSAlertLTEDataExhaust": fextSMSAlertLTEDataExhaust,
       "fextSMSAlertLTEDisconnect": fextSMSAlertLTEDisconnect,
       "fextSMSAlertLTEWeakSignal": fextSMSAlertLTEWeakSignal,
       "fextSMSAlertOSFallback": fextSMSAlertOSFallback,
       "fextSMSAlertNetworkMode": fextSMSAlertNetworkMode,
       "fextSMSAlertBackupMode": fextSMSAlertBackupMode,
       "fextSMSRemoteDiag": fextSMSRemoteDiag,
       "fextSMSDiag": fextSMSDiag,
       "fextSMSUser": fextSMSUser,
       "fextSMSUserEntry": fextSMSUserEntry,
       "fextSMSUserIndex": fextSMSUserIndex,
       "fextSMSUserName": fextSMSUserName,
       "fextSMSUserSender": fextSMSUserSender,
       "fextSMSUserNumber": fextSMSUserNumber,
       "fextSMSUserCommand": fextSMSUserCommand,
       "fextSysLog": fextSysLog,
       "fextSysLogRemoteIP": fextSysLogRemoteIP,
       "fextSysLogRemotePort": fextSysLogRemotePort,
       "fextSysLogStatReport": fextSysLogStatReport,
       "fextSysLogStatRptStatus": fextSysLogStatRptStatus,
       "fextSysLogStatRptItv": fextSysLogStatRptItv,
       "fextSysLogStatRptCPUUsage": fextSysLogStatRptCPUUsage,
       "fextSysLogStatRptCPUUsageThrsd": fextSysLogStatRptCPUUsageThrsd,
       "fextSysLogStatRptCPUUsageVariance": fextSysLogStatRptCPUUsageVariance,
       "fextSysLogStatRptMemUsage": fextSysLogStatRptMemUsage,
       "fextSysLogStatRptMemUsageThrsd": fextSysLogStatRptMemUsageThrsd,
       "fextSysLogStatRptMemUsageVariance": fextSysLogStatRptMemUsageVariance,
       "fextSysLogStatRptCPUTemp": fextSysLogStatRptCPUTemp,
       "fextSysLogStatRptCPUTempThrsd": fextSysLogStatRptCPUTempThrsd,
       "fextSysLogStatRptCPUTempVariance": fextSysLogStatRptCPUTempVariance,
       "fextLANSwitch": fextLANSwitch,
       "fextLANSwitchPort": fextLANSwitchPort,
       "fextLANSwitchPortEntry": fextLANSwitchPortEntry,
       "fextLANSwitchPortIndex": fextLANSwitchPortIndex,
       "fextLANSwitchPortName": fextLANSwitchPortName,
       "fextVirtualWirePair": fextVirtualWirePair,
       "fextLTE1Mapping": fextLTE1Mapping,
       "fextLTE2Mapping": fextLTE2Mapping,
       "fextLTE": fextLTE,
       "fextLTESetting": fextLTESetting,
       "fextLTEReport": fextLTEReport,
       "fextLTEReportStatus": fextLTEReportStatus,
       "fextLTEReportInterval": fextLTEReportInterval,
       "fextLTEReportSignalThreshold": fextLTEReportSignalThreshold,
       "fextLTEModem1": fextLTEModem1,
       "fextModem1CertMode": fextModem1CertMode,
       "fextModem1DefaultSIM": fextModem1DefaultSIM,
       "fextModem1PreferredCarrier": fextModem1PreferredCarrier,
       "fextModem1GPS": fextModem1GPS,
       "fextModem1SIM1Pin": fextModem1SIM1Pin,
       "fextModem1SIM1PinCode": fextModem1SIM1PinCode,
       "fextModem1SIM2Pin": fextModem1SIM2Pin,
       "fextModem1SIM2PinCode": fextModem1SIM2PinCode,
       "fextModem1AutoSwitch": fextModem1AutoSwitch,
       "fextModem1SwitchByDisconnect": fextModem1SwitchByDisconnect,
       "fextModem1SwitchBySignal": fextModem1SwitchBySignal,
       "fextModem1SwitchByPlan": fextModem1SwitchByPlan,
       "fextModem1SwitchDisconnectThreshold": fextModem1SwitchDisconnectThreshold,
       "fextModem1SwitchDisconnectPeriod": fextModem1SwitchDisconnectPeriod,
       "fextModem1SwitchBack": fextModem1SwitchBack,
       "fextModem1SwitchBackTime": fextModem1SwitchBackTime,
       "fextModem1SwitchBackTimer": fextModem1SwitchBackTimer,
       "fextLTEModem2": fextLTEModem2,
       "fextModem2CertMode": fextModem2CertMode,
       "fextModem2DefaultSIM": fextModem2DefaultSIM,
       "fextModem2PreferredCarrier": fextModem2PreferredCarrier,
       "fextModem2GPS": fextModem2GPS,
       "fextModem2SIM1Pin": fextModem2SIM1Pin,
       "fextModem2SIM1PinCode": fextModem2SIM1PinCode,
       "fextModem2SIM2Pin": fextModem2SIM2Pin,
       "fextModem2SIM2PinCode": fextModem2SIM2PinCode,
       "fextModem2AutoSwitch": fextModem2AutoSwitch,
       "fextModem2SwitchByDisconnect": fextModem2SwitchByDisconnect,
       "fextModem2SwitchBySignal": fextModem2SwitchBySignal,
       "fextModem2SwitchByPlan": fextModem2SwitchByPlan,
       "fextModem2SwitchDisconnectThreshold": fextModem2SwitchDisconnectThreshold,
       "fextModem2SwitchDisconnectPeriod": fextModem2SwitchDisconnectPeriod,
       "fextModem2SwitchBack": fextModem2SwitchBack,
       "fextModem2SwitchBackByTime": fextModem2SwitchBackByTime,
       "fextModem2SwitchBackByTimer": fextModem2SwitchBackByTimer,
       "fextLTECarrier": fextLTECarrier,
       "fextLTECarrierEntry": fextLTECarrierEntry,
       "fextLTECarrierIndex": fextLTECarrierIndex,
       "fextLTECarrierName": fextLTECarrierName,
       "fextLTECarrierFirmware": fextLTECarrierFirmware,
       "fextLTECarrierPRI": fextLTECarrierPRI,
       "fextLTESIMMap": fextLTESIMMap,
       "fextLTESIMMapEntry": fextLTESIMMapEntry,
       "fextLTESIMMapIndex": fextLTESIMMapIndex,
       "fextLTESIMMapName": fextLTESIMMapName,
       "fextLTESIMMapMCC": fextLTESIMMapMCC,
       "fextLTESIMMapMNC": fextLTESIMMapMNC,
       "fextLTESIMMapCarrier": fextLTESIMMapCarrier,
       "fextLTEPlan": fextLTEPlan,
       "fextLTEPlanEntry": fextLTEPlanEntry,
       "fextLTEPlanIndex": fextLTEPlanIndex,
       "fextLTEPlanName": fextLTEPlanName,
       "fextLTEPlanModem": fextLTEPlanModem,
       "fextLTEPlanType": fextLTEPlanType,
       "fextLTEPlanICCID": fextLTEPlanICCID,
       "fextLTEPlanCarrier": fextLTEPlanCarrier,
       "fextLTEPlanSlot": fextLTEPlanSlot,
       "fextLTEPlanAPN": fextLTEPlanAPN,
       "fextLTEPlanAuth": fextLTEPlanAuth,
       "fextLTEPlanUser": fextLTEPlanUser,
       "fextLTEPlanPWD": fextLTEPlanPWD,
       "fextLTEPlanPDN": fextLTEPlanPDN,
       "fextLTEPlanSignalThreshold": fextLTEPlanSignalThreshold,
       "fextLTEPlanSignalPeriod": fextLTEPlanSignalPeriod,
       "fextLTEPlanCapacity": fextLTEPlanCapacity,
       "fextLTEPlanMonthlyFee": fextLTEPlanMonthlyFee,
       "fextLTEPlanBillingDate": fextLTEPlanBillingDate,
       "fextLTEPlanOverage": fextLTEPlanOverage,
       "fextLTEPlanPreferredSubnet": fextLTEPlanPreferredSubnet,
       "fextLTEPlanPrivateSubnet": fextLTEPlanPrivateSubnet,
       "fextNetwork": fextNetwork,
       "fextNetworkAddress": fextNetworkAddress,
       "fextNetworkAddressEntry": fextNetworkAddressEntry,
       "fextNetworkAddressIndex": fextNetworkAddressIndex,
       "fextNetworkAddressName": fextNetworkAddressName,
       "fextNetworkAddressType": fextNetworkAddressType,
       "fextNetworkAddressSubnet": fextNetworkAddressSubnet,
       "fextNetworkAddressStartIP": fextNetworkAddressStartIP,
       "fextNetworkAddressEndIP": fextNetworkAddressEndIP,
       "fextNetworkService": fextNetworkService,
       "fextServiceCustom": fextServiceCustom,
       "fextServiceCustomEntry": fextServiceCustomEntry,
       "fextServiceCustomIndex": fextServiceCustomIndex,
       "fextServiceCustomName": fextServiceCustomName,
       "fextServiceCustomProtocol": fextServiceCustomProtocol,
       "fextServiceCustomProtocolNumber": fextServiceCustomProtocolNumber,
       "fextServiceCustomTCPPortRange": fextServiceCustomTCPPortRange,
       "fextServiceCustomUDPPortRange": fextServiceCustomUDPPortRange,
       "fextFirewall": fextFirewall,
       "fextFirewallPolicy": fextFirewallPolicy,
       "fextFirewallPolicyEntry": fextFirewallPolicyEntry,
       "fextFirewallPolicyIndex": fextFirewallPolicyIndex,
       "fextFirewallPolicyName": fextFirewallPolicyName,
       "fextFirewallPolicySrcIntf": fextFirewallPolicySrcIntf,
       "fextFirewallPolicyDstIntf": fextFirewallPolicyDstIntf,
       "fextFirewallPolicySrcAddr": fextFirewallPolicySrcAddr,
       "fextFirewallPolicyDstAddr": fextFirewallPolicyDstAddr,
       "fextFirewallPolicyAction": fextFirewallPolicyAction,
       "fextFirewallPolicyStatus": fextFirewallPolicyStatus,
       "fextFirewallPolicyService": fextFirewallPolicyService,
       "fextFirewallPolicyNAT": fextFirewallPolicyNAT,
       "fextRouter": fextRouter,
       "fextRouterPolicy": fextRouterPolicy,
       "fextRouterPolicyEntry": fextRouterPolicyEntry,
       "fextRouterPolicyIndex": fextRouterPolicyIndex,
       "fextRouterPolicyName": fextRouterPolicyName,
       "fextRouterPolicyInputDevice": fextRouterPolicyInputDevice,
       "fextRouterPolicySrcAddr": fextRouterPolicySrcAddr,
       "fextRouterPolicySrc": fextRouterPolicySrc,
       "fextRouterPolicyDstAddr": fextRouterPolicyDstAddr,
       "fextRouterPolicyDst": fextRouterPolicyDst,
       "fextRouterPolicyService": fextRouterPolicyService,
       "fextRouterPolicyTarget": fextRouterPolicyTarget,
       "fextRouterPolicyStatus": fextRouterPolicyStatus,
       "fextRouterPolicyComment": fextRouterPolicyComment,
       "fextRouterStatic": fextRouterStatic,
       "fextRouterStaticEntry": fextRouterStaticEntry,
       "fextRouterStaticIndex": fextRouterStaticIndex,
       "fextRouterStaticName": fextRouterStaticName,
       "fextRouterStaticStatus": fextRouterStaticStatus,
       "fextRouterStaticDst": fextRouterStaticDst,
       "fextRouterStaticGateway": fextRouterStaticGateway,
       "fextRouterStaticDistance": fextRouterStaticDistance,
       "fextRouterStaticDevice": fextRouterStaticDevice,
       "fextRouterStaticComment": fextRouterStaticComment,
       "fextRouterTarget": fextRouterTarget,
       "fextRouterTargetEntry": fextRouterTargetEntry,
       "fextRouterTargetIndex": fextRouterTargetIndex,
       "fextRouterTargetName": fextRouterTargetName,
       "fextRouterTargetInterface": fextRouterTargetInterface,
       "fextRouterTargetNextHop": fextRouterTargetNextHop,
       "fextRouterTargetIntfNH": fextRouterTargetIntfNH,
       "fextRouterMulticast": fextRouterMulticast,
       "fextMcastPIMSMGlobal": fextMcastPIMSMGlobal,
       "fextPIMSMGlobalJoinPruneInterval": fextPIMSMGlobalJoinPruneInterval,
       "fextPIMSMGlobalHelloInterval": fextPIMSMGlobalHelloInterval,
       "fextPIMSMGlobalRPAddress": fextPIMSMGlobalRPAddress,
       "fextPIMSMGlobalRPAddressEntry": fextPIMSMGlobalRPAddressEntry,
       "fextPIMRPAddressIndex": fextPIMRPAddressIndex,
       "fextPIMRPAddressName": fextPIMRPAddressName,
       "fextPIMRPAddressAddress": fextPIMRPAddressAddress,
       "fextPIMRPAddressGroup": fextPIMRPAddressGroup,
       "fextMcastInterface": fextMcastInterface,
       "fextMcastInterfaceEntry": fextMcastInterfaceEntry,
       "fextMcastInterfaceIndex": fextMcastInterfaceIndex,
       "fextMcastInterfaceName": fextMcastInterfaceName,
       "fextVPN": fextVPN,
       "fextVPNIPsec": fextVPNIPsec,
       "fextVPNIPsecPhase1": fextVPNIPsecPhase1,
       "fextVPNIPsecPhase1Entry": fextVPNIPsecPhase1Entry,
       "fextIPsecPhase1Index": fextIPsecPhase1Index,
       "fextIPsecPhase1Name": fextIPsecPhase1Name,
       "fextIPsecPhase1IKEVersion": fextIPsecPhase1IKEVersion,
       "fextIPsecPhase1KeyLife": fextIPsecPhase1KeyLife,
       "fextIPsecPhase1Mode": fextIPsecPhase1Mode,
       "fextIPsecPhase1Proposal": fextIPsecPhase1Proposal,
       "fextIPsecPhase1DHGroup": fextIPsecPhase1DHGroup,
       "fextIPsecPhase1Interface": fextIPsecPhase1Interface,
       "fextIPsecPhase1Type": fextIPsecPhase1Type,
       "fextIPsecPhase1RemoteGW": fextIPsecPhase1RemoteGW,
       "fextIPsecPhase1RemoteGWDDNS": fextIPsecPhase1RemoteGWDDNS,
       "fextIPsecPhase1AuthMethod": fextIPsecPhase1AuthMethod,
       "fextIPsecPhase1PSKSecret": fextIPsecPhase1PSKSecret,
       "fextIPsecPhase1Certificate": fextIPsecPhase1Certificate,
       "fextIPsecPhase1Peer": fextIPsecPhase1Peer,
       "fextIPsecPhase1LocalID": fextIPsecPhase1LocalID,
       "fextIPsecPhase1PeerID": fextIPsecPhase1PeerID,
       "fextVPNIPsecPhase2": fextVPNIPsecPhase2,
       "fextVPNIPsecPhase2Entry": fextVPNIPsecPhase2Entry,
       "fextIPsecPhase2Index": fextIPsecPhase2Index,
       "fextIPsecPhase2Name": fextIPsecPhase2Name,
       "fextIPsecPhase2Phase1Name": fextIPsecPhase2Phase1Name,
       "fextIPsecPhase2Proposal": fextIPsecPhase2Proposal,
       "fextIPsecPhase2PFS": fextIPsecPhase2PFS,
       "fextIPsecPhase2DHGroup": fextIPsecPhase2DHGroup,
       "fextIPsecPhase2KeyLifeType": fextIPsecPhase2KeyLifeType,
       "fextIPsecPhase2KeyLifeSeconds": fextIPsecPhase2KeyLifeSeconds,
       "fextIPsecPhase2KeyLifeKBs": fextIPsecPhase2KeyLifeKBs,
       "fextIPsecPhase2Encapsulation": fextIPsecPhase2Encapsulation,
       "fextIPsecPhase2Protocol": fextIPsecPhase2Protocol,
       "fextIPsecPhase2SrcAddrType": fextIPsecPhase2SrcAddrType,
       "fextIPsecPhase2SrcSubnet": fextIPsecPhase2SrcSubnet,
       "fextIPsecPhase2SrcStartIp": fextIPsecPhase2SrcStartIp,
       "fextIPsecPhase2SrcEndIp": fextIPsecPhase2SrcEndIp,
       "fextIPsecPhase2SrcName": fextIPsecPhase2SrcName,
       "fextIPsecPhase2SrcPort": fextIPsecPhase2SrcPort,
       "fextIPsecPhase2DstAddrType": fextIPsecPhase2DstAddrType,
       "fextIPsecPhase2DstSubnet": fextIPsecPhase2DstSubnet,
       "fextIPsecPhase2DstStartIp": fextIPsecPhase2DstStartIp,
       "fextIPsecPhase2DstEndIp": fextIPsecPhase2DstEndIp,
       "fextIPsecPhase2DstName": fextIPsecPhase2DstName,
       "fextIPsecPhase2DstPort": fextIPsecPhase2DstPort,
       "fextVPNCertificate": fextVPNCertificate,
       "fextVPNCertificateCA": fextVPNCertificateCA,
       "fextVPNCertificateCAEntry": fextVPNCertificateCAEntry,
       "fextCertificateCAIndex": fextCertificateCAIndex,
       "fextCertificateCAName": fextCertificateCAName,
       "fextCertificateCAComment": fextCertificateCAComment,
       "fextCertificateCASource": fextCertificateCASource,
       "fextVPNCertificateLocal": fextVPNCertificateLocal,
       "fextVPNCertificateLocalEntry": fextVPNCertificateLocalEntry,
       "fextCertificateLocalIndex": fextCertificateLocalIndex,
       "fextCertificateLocalName": fextCertificateLocalName,
       "fextCertificateLocalComment": fextCertificateLocalComment,
       "fextCertificateLocalSource": fextCertificateLocalSource,
       "fextHMon": fextHMon,
       "fextHMonIntf": fextHMonIntf,
       "fextHMonIntfEntry": fextHMonIntfEntry,
       "fextHMonIntfIndex": fextHMonIntfIndex,
       "fextHMonIntfName": fextHMonIntfName,
       "fextHMonIntfInterval": fextHMonIntfInterval,
       "fextHMonIntfInterface": fextHMonIntfInterface,
       "fextHMonIntfFilter": fextHMonIntfFilter,
       "fextHMonHchk": fextHMonHchk,
       "fextHMonHchkEntry": fextHMonHchkEntry,
       "fextHMonHchkIndex": fextHMonHchkIndex,
       "fextHMonHchkName": fextHMonHchkName,
       "fextHMonHchkProtocol": fextHMonHchkProtocol,
       "fextHMonHchkInterval": fextHMonHchkInterval,
       "fextHMonHchkProbeCnt": fextHMonHchkProbeCnt,
       "fextHMonHchkProbeTM": fextHMonHchkProbeTM,
       "fextHMonHchkProbeTarget": fextHMonHchkProbeTarget,
       "fextHMonHchkPort": fextHMonHchkPort,
       "fextHMonHchkHTTPGet": fextHMonHchkHTTPGet,
       "fextHMonHchkInterface": fextHMonHchkInterface,
       "fextHMonHchkSrcType": fextHMonHchkSrcType,
       "fextHMonHchkSrcInterface": fextHMonHchkSrcInterface,
       "fextHMonHchkSrcIP": fextHMonHchkSrcIP,
       "fextHMonHchkFilter": fextHMonHchkFilter,
       "fextSNMP": fextSNMP,
       "fextSNMPSysInfo": fextSNMPSysInfo,
       "fextSNMPSysInfoStatus": fextSNMPSysInfoStatus,
       "fextSNMPSysInfoDescription": fextSNMPSysInfoDescription,
       "fextSNMPSysInfoContactInfo": fextSNMPSysInfoContactInfo,
       "fextSNMPSysInfoLocation": fextSNMPSysInfoLocation,
       "fextSNMPCommunity": fextSNMPCommunity,
       "fextSNMPCommunityEntry": fextSNMPCommunityEntry,
       "fextSNMPCommunityIndex": fextSNMPCommunityIndex,
       "fextSNMPCommunityID": fextSNMPCommunityID,
       "fextSNMPCommunityName": fextSNMPCommunityName,
       "fextSNMPCommunityStatus": fextSNMPCommunityStatus,
       "fextSNMPCommunityHosts": fextSNMPCommunityHosts,
       "fextSNMPCommunityQueryV1Status": fextSNMPCommunityQueryV1Status,
       "fextSNMPCommunityQueryV1Port": fextSNMPCommunityQueryV1Port,
       "fextSNMPCommunityQueryV2CStatus": fextSNMPCommunityQueryV2CStatus,
       "fextSNMPCommunityQueryV2CPort": fextSNMPCommunityQueryV2CPort,
       "fextSNMPCommunityTrapV1Status": fextSNMPCommunityTrapV1Status,
       "fextSNMPCommunityTrapV1LPort": fextSNMPCommunityTrapV1LPort,
       "fextSNMPCommunityTrapV1RPort": fextSNMPCommunityTrapV1RPort,
       "fextSNMPCommunityTrapV2CStatus": fextSNMPCommunityTrapV2CStatus,
       "fextSNMPCommunityTrapV2CLPort": fextSNMPCommunityTrapV2CLPort,
       "fextSNMPCommunityTrapV2CRPort": fextSNMPCommunityTrapV2CRPort,
       "fextSNMPCommunityEvents": fextSNMPCommunityEvents,
       "fextSNMPUser": fextSNMPUser,
       "fextSNMPUserEntry": fextSNMPUserEntry,
       "fextSNMPUserIndex": fextSNMPUserIndex,
       "fextSNMPUserID": fextSNMPUserID,
       "fextSNMPUserName": fextSNMPUserName,
       "fextSNMPUserStatus": fextSNMPUserStatus,
       "fextSNMPUserNotifyHosts": fextSNMPUserNotifyHosts,
       "fextSNMPUserTrapStatus": fextSNMPUserTrapStatus,
       "fextSNMPUserTrapLPort": fextSNMPUserTrapLPort,
       "fextSNMPUserTrapRPort": fextSNMPUserTrapRPort,
       "fextSNMPUserQueryStatus": fextSNMPUserQueryStatus,
       "fextSNMPUserQueryPort": fextSNMPUserQueryPort,
       "fextSNMPUserEvents": fextSNMPUserEvents,
       "fextSNMPUserSecurityLevel": fextSNMPUserSecurityLevel,
       "fextSNMPUserAuthProtocol": fextSNMPUserAuthProtocol,
       "fextSNMPUserAuthPWD": fextSNMPUserAuthPWD,
       "fextSNMPUserPrivProtocol": fextSNMPUserPrivProtocol,
       "fextSNMPUserPrivPWD": fextSNMPUserPrivPWD,
       "fextSNMPHost": fextSNMPHost,
       "fextSNMPHostEntry": fextSNMPHostEntry,
       "fextSNMPHostIndex": fextSNMPHostIndex,
       "fextSNMPHostName": fextSNMPHostName,
       "fextSNMPHostIP": fextSNMPHostIP,
       "fextSNMPHostType": fextSNMPHostType,
       "fextInfo": fextInfo,
       "fextInfoSystem": fextInfoSystem,
       "fextInfoVersion": fextInfoVersion,
       "fextInfoImage": fextInfoImage,
       "fextInfoImageType": fextInfoImageType,
       "fextInfoModel": fextInfoModel,
       "fextInfoMAC": fextInfoMAC,
       "fextInfoSN": fextInfoSN,
       "fextInfoLicense": fextInfoLicense,
       "fextInfoOEMSN": fextInfoOEMSN,
       "fextInfoREV": fextInfoREV,
       "fextInfoVERSION": fextInfoVERSION,
       "fextInfoROMREV": fextInfoROMREV,
       "fextInfoFallbackImage": fextInfoFallbackImage,
       "fextInfoFallbackImageType": fextInfoFallbackImageType,
       "fextInfoStatus": fextInfoStatus,
       "fextInfoCPUUsage": fextInfoCPUUsage,
       "fextInfoMemUsage": fextInfoMemUsage,
       "fextInfoUptime": fextInfoUptime,
       "fextInfoInterface": fextInfoInterface,
       "fextInfoInterfaceEntry": fextInfoInterfaceEntry,
       "fextInfoInterfaceName": fextInfoInterfaceName,
       "fextInfoInterfaceStatus": fextInfoInterfaceStatus,
       "fextInfoInterfaceType": fextInfoInterfaceType,
       "fextInfoInterfaceMode": fextInfoInterfaceMode,
       "fextInfoInterfaceIP": fextInfoInterfaceIP,
       "fextInfoInterfaceGateway": fextInfoInterfaceGateway,
       "fextInfoDHCPServer": fextInfoDHCPServer,
       "fextInfoDHCPServerConfig": fextInfoDHCPServerConfig,
       "fextInfoDHCPServerEntry": fextInfoDHCPServerEntry,
       "fextInfoDHCPServerIndex": fextInfoDHCPServerIndex,
       "fextInfoDHCPServerName": fextInfoDHCPServerName,
       "fextInfoDHCPServerStatus": fextInfoDHCPServerStatus,
       "fextInfoDHCPServerLeaseTime": fextInfoDHCPServerLeaseTime,
       "fextInfoDHCPServerInterface": fextInfoDHCPServerInterface,
       "fextInfoDHCPServerDNS": fextInfoDHCPServerDNS,
       "fextInfoDHCPServerDNSServer": fextInfoDHCPServerDNSServer,
       "fextInfoDHCPServerNTP": fextInfoDHCPServerNTP,
       "fextInfoDHCPServerNTPServer": fextInfoDHCPServerNTPServer,
       "fextInfoDHCPServerGatewayIP": fextInfoDHCPServerGatewayIP,
       "fextInfoDHCPServerIPRange": fextInfoDHCPServerIPRange,
       "fextInfoDHCPServerNetmask": fextInfoDHCPServerNetmask,
       "fextInfoDHCPServerClient": fextInfoDHCPServerClient,
       "fextInfoDHCPServerClientEntry": fextInfoDHCPServerClientEntry,
       "fextInfoDHCPServerClientIndex": fextInfoDHCPServerClientIndex,
       "fextInfoDHCPServerClientMAC": fextInfoDHCPServerClientMAC,
       "fextInfoDHCPServerClientIP": fextInfoDHCPServerClientIP,
       "fextInfoDHCPServerClientHost": fextInfoDHCPServerClientHost,
       "fextInfoDHCPServerClientLeaseTime": fextInfoDHCPServerClientLeaseTime,
       "fextInfoDHCPClient": fextInfoDHCPClient,
       "fextInfoDHCPClientEntry": fextInfoDHCPClientEntry,
       "fextInfoDHCPClientIndex": fextInfoDHCPClientIndex,
       "fextInfoDHCPClientInterface": fextInfoDHCPClientInterface,
       "fextInfoDHCPClientIP": fextInfoDHCPClientIP,
       "fextInfoDHCPClientNetmask": fextInfoDHCPClientNetmask,
       "fextInfoDHCPClientGatewayIP": fextInfoDHCPClientGatewayIP,
       "fextInfoDHCPClientDNSServer": fextInfoDHCPClientDNSServer,
       "fextInfoDHCPClientLeaseTime": fextInfoDHCPClientLeaseTime,
       "fextInfoDHCPClientLeftTime": fextInfoDHCPClientLeftTime,
       "fextInfoDNS": fextInfoDNS,
       "fextInfoDNSEntry": fextInfoDNSEntry,
       "fextInfoDNSIndex": fextInfoDNSIndex,
       "fextInfoDNSType": fextInfoDNSType,
       "fextInfoDNSIP": fextInfoDNSIP,
       "fextInfoDNSInterface": fextInfoDNSInterface,
       "fextInfoExtender": fextInfoExtender,
       "fextInfoEXTDStatus": fextInfoEXTDStatus,
       "fextInfoEXTDHostName": fextInfoEXTDHostName,
       "fextInfoEXTDMode": fextInfoEXTDMode,
       "fextInfoEXTDADDR": fextInfoEXTDADDR,
       "fextInfoEXTDWANADDR": fextInfoEXTDWANADDR,
       "fextInfoEXTDController": fextInfoEXTDController,
       "fextInfoEXTDControllerName": fextInfoEXTDControllerName,
       "fextInfoEXTDDeployed": fextInfoEXTDDeployed,
       "fextInfoEXTDAccount": fextInfoEXTDAccount,
       "fextInfoEXTDUptime": fextInfoEXTDUptime,
       "fextInfoEXTDMGMTState": fextInfoEXTDMGMTState,
       "fextInfoEXTDMAC": fextInfoEXTDMAC,
       "fextInfoEXTDNetworkMode": fextInfoEXTDNetworkMode,
       "fextInfoEXTDFGTBackupMode": fextInfoEXTDFGTBackupMode,
       "fextInfoEXTDDiscoveryType": fextInfoEXTDDiscoveryType,
       "fextInfoEXTDDiscoveryInterval": fextInfoEXTDDiscoveryInterval,
       "fextInfoEXTDEchoInterval": fextInfoEXTDEchoInterval,
       "fextInfoEXTDReportInterval": fextInfoEXTDReportInterval,
       "fextInfoEXTDStatsInterval": fextInfoEXTDStatsInterval,
       "fextInfoEXTDMDMFWServer": fextInfoEXTDMDMFWServer,
       "fextInfoEXTDOSFWServer": fextInfoEXTDOSFWServer,
       "fextInfoModem": fextInfoModem,
       "fextInfoModemStatus": fextInfoModemStatus,
       "fextInfoModemStatusEntry": fextInfoModemStatusEntry,
       "fextInfoModemStatusIndex": fextInfoModemStatusIndex,
       "fextInfoModemStatusModem": fextInfoModemStatusModem,
       "fextInfoModemStatusUSBPath": fextInfoModemStatusUSBPath,
       "fextInfoModemStatusVender": fextInfoModemStatusVender,
       "fextInfoModemStatusProduct": fextInfoModemStatusProduct,
       "fextInfoModemStatusModel": fextInfoModemStatusModel,
       "fextInfoModemStatusSIMSlot": fextInfoModemStatusSIMSlot,
       "fextInfoModemStatusRevision": fextInfoModemStatusRevision,
       "fextInfoModemStatusIMEI": fextInfoModemStatusIMEI,
       "fextInfoModemStatusICCID": fextInfoModemStatusICCID,
       "fextInfoModemStatusIMSI": fextInfoModemStatusIMSI,
       "fextInfoModemStatusPinStatus": fextInfoModemStatusPinStatus,
       "fextInfoModemStatusPinCode": fextInfoModemStatusPinCode,
       "fextInfoModemStatusCarrier": fextInfoModemStatusCarrier,
       "fextInfoModemStatusAPN": fextInfoModemStatusAPN,
       "fextInfoModemStatusService": fextInfoModemStatusService,
       "fextInfoModemStatusPhoneNumber": fextInfoModemStatusPhoneNumber,
       "fextInfoModemStatusSIM1Pin": fextInfoModemStatusSIM1Pin,
       "fextInfoModemStatusSIM1Puk": fextInfoModemStatusSIM1Puk,
       "fextInfoModemStatusSIM2Pin": fextInfoModemStatusSIM2Pin,
       "fextInfoModemStatusSIM2Puk": fextInfoModemStatusSIM2Puk,
       "fextInfoModemStatusRSSI": fextInfoModemStatusRSSI,
       "fextInfoModemStatusSignalStrength": fextInfoModemStatusSignalStrength,
       "fextInfoModemStatusCAState": fextInfoModemStatusCAState,
       "fextInfoModemStatusCellID": fextInfoModemStatusCellID,
       "fextInfoModemStatusBand": fextInfoModemStatusBand,
       "fextInfoModemStatusBandwidth": fextInfoModemStatusBandwidth,
       "fextInfoModemStatusSINR": fextInfoModemStatusSINR,
       "fextInfoModemStatusRSRP": fextInfoModemStatusRSRP,
       "fextInfoModemStatusRSRQ": fextInfoModemStatusRSRQ,
       "fextInfoModemStatusPlanName": fextInfoModemStatusPlanName,
       "fextInfoModemStatusConnectStatus": fextInfoModemStatusConnectStatus,
       "fextInfoModemStatusReconnectCount": fextInfoModemStatusReconnectCount,
       "fextInfoModemStatusSmartSIMSwitch": fextInfoModemStatusSmartSIMSwitch,
       "fextInfoModemStatusUptime": fextInfoModemStatusUptime,
       "fextInfoModemStatusClock": fextInfoModemStatusClock,
       "fextInfoModemStatusTemperature": fextInfoModemStatusTemperature,
       "fextInfoModemStatusActivateStatus": fextInfoModemStatusActivateStatus,
       "fextInfoModemStatusRoamingStatus": fextInfoModemStatusRoamingStatus,
       "fextInfoModemStatusLatitude": fextInfoModemStatusLatitude,
       "fextInfoModemStatusLongitude": fextInfoModemStatusLongitude,
       "fextInfoModemFWVersion": fextInfoModemFWVersion,
       "fextInfoModemFWVersionVersion": fextInfoModemFWVersionVersion,
       "fextInfoModemDataUsage": fextInfoModemDataUsage,
       "fextInfoModemDataUsageEntry": fextInfoModemDataUsageEntry,
       "fextInfoModemDataUsageIndex": fextInfoModemDataUsageIndex,
       "fextInfoModemDataUsageModem": fextInfoModemDataUsageModem,
       "fextInfoModemDataUsageSlot": fextInfoModemDataUsageSlot,
       "fextInfoModemDataUsageCarrier": fextInfoModemDataUsageCarrier,
       "fextInfoModemDataUsageIMSI": fextInfoModemDataUsageIMSI,
       "fextInfoModemDataUsageMB": fextInfoModemDataUsageMB,
       "fextInfoModemDataUsagePercentage": fextInfoModemDataUsagePercentage,
       "fextInfoModemDataUsageDataPlan": fextInfoModemDataUsageDataPlan,
       "fextInfoModemDataUsageOverage": fextInfoModemDataUsageOverage,
       "fextInfoModemDataUsageNextBillDate": fextInfoModemDataUsageNextBillDate,
       "fextInfoRouter": fextInfoRouter,
       "fextInfoRouterRoute": fextInfoRouterRoute,
       "fextInfoRouterRouteEntry": fextInfoRouterRouteEntry,
       "fextInfoRouterRouteIndex": fextInfoRouterRouteIndex,
       "fextInfoRouterRouteType": fextInfoRouterRouteType,
       "fextInfoRouterRouteDst": fextInfoRouterRouteDst,
       "fextInfoRouterRouteGW": fextInfoRouterRouteGW,
       "fextInfoRouterRouteHelp": fextInfoRouterRouteHelp,
       "fextInfoRouterRouteDev": fextInfoRouterRouteDev,
       "fextInfoRouterPolicy": fextInfoRouterPolicy,
       "fextInfoRouterPolicyEntry": fextInfoRouterPolicyEntry,
       "fextInfoRouterPolicyIndex": fextInfoRouterPolicyIndex,
       "fextInfoRouterPolicySeq": fextInfoRouterPolicySeq,
       "fextInfoRouterPolicyStatus": fextInfoRouterPolicyStatus,
       "fextInfoRouterPolicyInputIntf": fextInfoRouterPolicyInputIntf,
       "fextInfoRouterPolicySrc": fextInfoRouterPolicySrc,
       "fextInfoRouterPolicySrcAddr": fextInfoRouterPolicySrcAddr,
       "fextInfoRouterPolicyDst": fextInfoRouterPolicyDst,
       "fextInfoRouterPolicyDstAddr": fextInfoRouterPolicyDstAddr,
       "fextInfoRouterPolicyService": fextInfoRouterPolicyService,
       "fextInfoRouterPolicyTarget": fextInfoRouterPolicyTarget,
       "fextInfoRouterPolicyRoutingTable": fextInfoRouterPolicyRoutingTable,
       "fextInfoRouterPolicyComment": fextInfoRouterPolicyComment,
       "fextInfoRouterTarget": fextInfoRouterTarget,
       "fextInfoRouterTargetEntry": fextInfoRouterTargetEntry,
       "fextInfoRouterTargetIndex": fextInfoRouterTargetIndex,
       "fextInfoRouterTargetStatus": fextInfoRouterTargetStatus,
       "fextInfoRouterTargetDevice": fextInfoRouterTargetDevice,
       "fextInfoRouterTargetDevStatus": fextInfoRouterTargetDevStatus,
       "fextInfoRouterTargetNextHop": fextInfoRouterTargetNextHop,
       "fextInfoRouterTargetNHStatus": fextInfoRouterTargetNHStatus,
       "fextInfoRouterTargetRouteType": fextInfoRouterTargetRouteType,
       "fextInfoRouterTargetRoutingTable": fextInfoRouterTargetRoutingTable,
       "fextInfoRouterTargetRefCounter": fextInfoRouterTargetRefCounter,
       "fextInfoRouterMulticast": fextInfoRouterMulticast,
       "fextInfoMcastPIMSM": fextInfoMcastPIMSM,
       "fextInfoPIMSMVIF": fextInfoPIMSMVIF,
       "fextInfoPIMSMVIFEntry": fextInfoPIMSMVIFEntry,
       "fextInfoPIMSMVIFIndex": fextInfoPIMSMVIFIndex,
       "fextInfoPIMSMVIFName": fextInfoPIMSMVIFName,
       "fextInfoPIMSMVIFAddress": fextInfoPIMSMVIFAddress,
       "fextInfoPIMSMVIFFlag": fextInfoPIMSMVIFFlag,
       "fextInfoPIMSMVIFHelloTimer": fextInfoPIMSMVIFHelloTimer,
       "fextInfoPIMSMVIFDRPriority": fextInfoPIMSMVIFDRPriority,
       "fextInfoPIMSMVIFNeighbor": fextInfoPIMSMVIFNeighbor,
       "fextInfoPIMSMVIFNeighborEntry": fextInfoPIMSMVIFNeighborEntry,
       "fextInfoPIMSMVIFNeighborIndex": fextInfoPIMSMVIFNeighborIndex,
       "fextInfoPIMSMVIFNeighborIP": fextInfoPIMSMVIFNeighborIP,
       "fextInfoPIMSMVIFNeighborExpire": fextInfoPIMSMVIFNeighborExpire,
       "fextInfoPIMSMRoute": fextInfoPIMSMRoute,
       "fextInfoPIMSMRouteEntry": fextInfoPIMSMRouteEntry,
       "fextInfoPIMSMRouteIndex": fextInfoPIMSMRouteIndex,
       "fextInfoPIMSMRouteSRC": fextInfoPIMSMRouteSRC,
       "fextInfoPIMSMRouteGRP": fextInfoPIMSMRouteGRP,
       "fextInfoPIMSMRouteRP": fextInfoPIMSMRouteRP,
       "fextInfoPIMSMRouteFlag": fextInfoPIMSMRouteFlag,
       "fextInfoPIMSMRouteJoinedOIFs": fextInfoPIMSMRouteJoinedOIFs,
       "fextInfoPIMSMRoutePrunedOIFs": fextInfoPIMSMRoutePrunedOIFs,
       "fextInfoPIMSMRouteLeavesOIFs": fextInfoPIMSMRouteLeavesOIFs,
       "fextInfoPIMSMRouteAssertedOIFs": fextInfoPIMSMRouteAssertedOIFs,
       "fextInfoPIMSMRouteOutgoingOIFs": fextInfoPIMSMRouteOutgoingOIFs,
       "fextInfoPIMSMRouteIncomingIFs": fextInfoPIMSMRouteIncomingIFs,
       "fextInfoPIMSMRouteJoinPruneTimer": fextInfoPIMSMRouteJoinPruneTimer,
       "fextInfoPIMSMRP": fextInfoPIMSMRP,
       "fextInfoPIMSMRPEntry": fextInfoPIMSMRPEntry,
       "fextInfoPIMSMRPIndex": fextInfoPIMSMRPIndex,
       "fextInfoPIMSMRPAddress": fextInfoPIMSMRPAddress,
       "fextInfoPIMSMRPGroup": fextInfoPIMSMRPGroup,
       "fextInfoPIMSMRPGroupEntry": fextInfoPIMSMRPGroupEntry,
       "fextInfoPIMSMRPGroupIndex": fextInfoPIMSMRPGroupIndex,
       "fextInfoPIMSMRPGroupAddress": fextInfoPIMSMRPGroupAddress,
       "fextInfoPIMSMRPGroupPriority": fextInfoPIMSMRPGroupPriority,
       "fextInfoRouterVRRP": fextInfoRouterVRRP,
       "fextInfoRouterVRRPEntry": fextInfoRouterVRRPEntry,
       "fextInfoRouterVRRPIndex": fextInfoRouterVRRPIndex,
       "fextInfoRouterVRRPIfName": fextInfoRouterVRRPIfName,
       "fextInfoRouterVRRPState": fextInfoRouterVRRPState,
       "fextInfoVWAN": fextInfoVWAN,
       "fextInfoVWANStatus": fextInfoVWANStatus,
       "fextInfoVWANStatusEntry": fextInfoVWANStatusEntry,
       "fextInfoVWANStatusIndex": fextInfoVWANStatusIndex,
       "fextInfoVWANStatusName": fextInfoVWANStatusName,
       "fextInfoVWANStatusAlgorithm": fextInfoVWANStatusAlgorithm,
       "fextInfoVWANStatusRedundantBy": fextInfoVWANStatusRedundantBy,
       "fextInfoVWANStatusFECName": fextInfoVWANStatusFECName,
       "fextInfoVWANStatusTargetCount": fextInfoVWANStatusTargetCount,
       "fextInfoVWANStatusSessionCount": fextInfoVWANStatusSessionCount,
       "fextInfoVWANStatusSessionTimeout": fextInfoVWANStatusSessionTimeout,
       "fextInfoVWANStatusVersion": fextInfoVWANStatusVersion,
       "fextInfoVWANStatusMember": fextInfoVWANStatusMember,
       "fextInfoVWANStatusMemberEntry": fextInfoVWANStatusMemberEntry,
       "fextInfoVWANStatusMemberIndex": fextInfoVWANStatusMemberIndex,
       "fextInfoVWANStatusMemberName": fextInfoVWANStatusMemberName,
       "fextInfoVWANStatusMemberStatus": fextInfoVWANStatusMemberStatus,
       "fextInfoVWANStatusMemberPriority": fextInfoVWANStatusMemberPriority,
       "fextInfoVWANStatusMemberWeight": fextInfoVWANStatusMemberWeight,
       "fextInfoVWANStatusMemberCapacity": fextInfoVWANStatusMemberCapacity,
       "fextInfoVWANStatusMemberMonthlyFee": fextInfoVWANStatusMemberMonthlyFee,
       "fextInfoVWANStatusMemberSessionCount": fextInfoVWANStatusMemberSessionCount,
       "fextInfoVWANStatusMemberReference": fextInfoVWANStatusMemberReference,
       "fextInfoVWANStatusMemberInterface": fextInfoVWANStatusMemberInterface,
       "fextInfoVWANStatusMemberNextHop": fextInfoVWANStatusMemberNextHop,
       "fextInfoVWANStatusMemberInBandwidth": fextInfoVWANStatusMemberInBandwidth,
       "fextInfoVWANStatusMemberOutBandwidth": fextInfoVWANStatusMemberOutBandwidth,
       "fextInfoVWANStatusMemberTotalBandwidth": fextInfoVWANStatusMemberTotalBandwidth,
       "fextInfoVWANStatusMemberDataIn": fextInfoVWANStatusMemberDataIn,
       "fextInfoVWANStatusMemberDataOut": fextInfoVWANStatusMemberDataOut,
       "fextInfoVWANStatusMemberTPIn": fextInfoVWANStatusMemberTPIn,
       "fextInfoVWANStatusMemberTPOut": fextInfoVWANStatusMemberTPOut,
       "fextInfoVWANMember": fextInfoVWANMember,
       "fextInfoVWANMemberEntry": fextInfoVWANMemberEntry,
       "fextInfoVWANMemberIndex": fextInfoVWANMemberIndex,
       "fextInfoVWANMemberName": fextInfoVWANMemberName,
       "fextInfoVWANMemberTarget": fextInfoVWANMemberTarget,
       "fextInfoVWANMemberPriority": fextInfoVWANMemberPriority,
       "fextInfoVWANMemberCapacity": fextInfoVWANMemberCapacity,
       "fextInfoVWANMemberMonthlyFee": fextInfoVWANMemberMonthlyFee,
       "fextInfoVWANMemberWeight": fextInfoVWANMemberWeight,
       "fextInfoVWANMemberInBwThreshold": fextInfoVWANMemberInBwThreshold,
       "fextInfoVWANMemberOutBwThreshold": fextInfoVWANMemberOutBwThreshold,
       "fextInfoVWANMemberTotalBwThreshold": fextInfoVWANMemberTotalBwThreshold,
       "fextInfoVWANMemberReference": fextInfoVWANMemberReference,
       "fextInfoVPN": fextInfoVPN,
       "fextInfoVPNIPsec": fextInfoVPNIPsec,
       "fextInfoIPsecTunnel": fextInfoIPsecTunnel,
       "fextInfoIPsecTunnelEntry": fextInfoIPsecTunnelEntry,
       "fextInfoIPsecTunIndex": fextInfoIPsecTunIndex,
       "fextInfoIPsecTunPhase1Name": fextInfoIPsecTunPhase1Name,
       "fextInfoIPsecTunStatus": fextInfoIPsecTunStatus,
       "fextInfoIPsecTunLocGwIp": fextInfoIPsecTunLocGwIp,
       "fextInfoIPsecTunRemGwIp": fextInfoIPsecTunRemGwIp,
       "fextInfoIPsecTunInBytes": fextInfoIPsecTunInBytes,
       "fextInfoIPsecTunOutBytes": fextInfoIPsecTunOutBytes,
       "fextInfoIPsecTunUpSeconds": fextInfoIPsecTunUpSeconds,
       "fextInfoIPsecTunSelector": fextInfoIPsecTunSelector,
       "fextInfoIPsecTunSelectorEntry": fextInfoIPsecTunSelectorEntry,
       "fextInfoIPsecTunSelectorIndex": fextInfoIPsecTunSelectorIndex,
       "fextInfoIPsecTunSelectorP2Name": fextInfoIPsecTunSelectorP2Name,
       "fextInfoIPsecTunSelectorStatus": fextInfoIPsecTunSelectorStatus,
       "fextInfoIPsecTunSelectorExpire": fextInfoIPsecTunSelectorExpire,
       "fextInfoIPsecTunSelectorSrcNet": fextInfoIPsecTunSelectorSrcNet,
       "fextInfoIPsecTunSelectorDstNet": fextInfoIPsecTunSelectorDstNet,
       "fextInfoIPsecTunSelectorSrcPort": fextInfoIPsecTunSelectorSrcPort,
       "fextInfoIPsecTunSelectorDstPort": fextInfoIPsecTunSelectorDstPort,
       "fextInfoIPsecTunSelectorProto": fextInfoIPsecTunSelectorProto,
       "fextInfoIPsecTunSelectorInBytes": fextInfoIPsecTunSelectorInBytes,
       "fextInfoIPsecTunSelectorOutBytes": fextInfoIPsecTunSelectorOutBytes,
       "fextInfoVPNCert": fextInfoVPNCert,
       "fextInfoVPNCertCA": fextInfoVPNCertCA,
       "fextInfoVPNCertCAEntry": fextInfoVPNCertCAEntry,
       "fextInfoVPNCertCAIndex": fextInfoVPNCertCAIndex,
       "fextInfoVPNCertCAName": fextInfoVPNCertCAName,
       "fextInfoVPNCertCAStatus": fextInfoVPNCertCAStatus,
       "fextInfoVPNCertCASubject": fextInfoVPNCertCASubject,
       "fextInfoVPNCertCAIssuer": fextInfoVPNCertCAIssuer,
       "fextInfoVPNCertCAValidFrom": fextInfoVPNCertCAValidFrom,
       "fextInfoVPNCertCAValidTo": fextInfoVPNCertCAValidTo,
       "fextInfoVPNCertCAFingerprint": fextInfoVPNCertCAFingerprint,
       "fextInfoVPNCertCASerialNum": fextInfoVPNCertCASerialNum,
       "fextInfoVPNCertLocal": fextInfoVPNCertLocal,
       "fextInfoVPNCertLocalEntry": fextInfoVPNCertLocalEntry,
       "fextInfoVPNCertLocIndex": fextInfoVPNCertLocIndex,
       "fextInfoVPNCertLocName": fextInfoVPNCertLocName,
       "fextInfoVPNCertLocStatus": fextInfoVPNCertLocStatus,
       "fextInfoVPNCertLocSubject": fextInfoVPNCertLocSubject,
       "fextInfoVPNCertLocIssuer": fextInfoVPNCertLocIssuer,
       "fextInfoVPNCertLocValidFrom": fextInfoVPNCertLocValidFrom,
       "fextInfoVPNCertLocValidTo": fextInfoVPNCertLocValidTo,
       "fextInfoVPNCertLocFingerprint": fextInfoVPNCertLocFingerprint,
       "fextInfoVPNCertLocSerialNum": fextInfoVPNCertLocSerialNum,
       "fextInfoHMon": fextInfoHMon,
       "fextInfoHMonIfStat": fextInfoHMonIfStat,
       "fextInfoHMonIfStatEntry": fextInfoHMonIfStatEntry,
       "fextInfoHMonIfStatIndex": fextInfoHMonIfStatIndex,
       "fextInfoHMonIfStatMonitor": fextInfoHMonIfStatMonitor,
       "fextInfoHMonIfStatIfName": fextInfoHMonIfStatIfName,
       "fextInfoHMonIfStatRxBytes": fextInfoHMonIfStatRxBytes,
       "fextInfoHMonIfStatTxBytes": fextInfoHMonIfStatTxBytes,
       "fextInfoHMonIfStatRxPkts": fextInfoHMonIfStatRxPkts,
       "fextInfoHMonIfStatTxPkts": fextInfoHMonIfStatTxPkts,
       "fextInfoHMonIfStatRxDropped": fextInfoHMonIfStatRxDropped,
       "fextInfoHMonIfStatTxDropped": fextInfoHMonIfStatTxDropped,
       "fextInfoHMonIfStatRxBps": fextInfoHMonIfStatRxBps,
       "fextInfoHMonIfStatTxBps": fextInfoHMonIfStatTxBps,
       "fextInfoHMonIfStatRxPps": fextInfoHMonIfStatRxPps,
       "fextInfoHMonIfStatTxPps": fextInfoHMonIfStatTxPps,
       "fextInfoHMonHChkStat": fextInfoHMonHChkStat,
       "fextInfoHMonHChkStatEntry": fextInfoHMonHChkStatEntry,
       "fextInfoHMonHChkStatIndex": fextInfoHMonHChkStatIndex,
       "fextInfoHMonHChkStatMonitor": fextInfoHMonHChkStatMonitor,
       "fextInfoHMonHChkStatIfName": fextInfoHMonHChkStatIfName,
       "fextInfoHMonHChkStatRttAvg": fextInfoHMonHChkStatRttAvg,
       "fextInfoHMonHChkStatRttMax": fextInfoHMonHChkStatRttMax,
       "fextInfoHMonHChkStatRttMin": fextInfoHMonHChkStatRttMin,
       "fextInfoHMonHChkStatRttNow": fextInfoHMonHChkStatRttNow,
       "fextInfoHMonHChkStatRttSd": fextInfoHMonHChkStatRttSd,
       "fextInfoHMonHChkStatRttAmsd": fextInfoHMonHChkStatRttAmsd,
       "fextInfoHMonHChkStatLossAvg": fextInfoHMonHChkStatLossAvg,
       "fextInfoHMonHChkStatLossMax": fextInfoHMonHChkStatLossMax,
       "fextInfoHMonHChkStatLossMin": fextInfoHMonHChkStatLossMin,
       "fextInfoHMonHChkStatLossNow": fextInfoHMonHChkStatLossNow,
       "fextInfoCPM": fextInfoCPM,
       "fextInfoCPMStatus": fextInfoCPMStatus,
       "fextInfoCPMProcessID": fextInfoCPMProcessID,
       "fextInfoCPMConnectStatus": fextInfoCPMConnectStatus,
       "fextInfoCPMCloudSSLHost": fextInfoCPMCloudSSLHost,
       "fextInfoCPMCloudSSLPort": fextInfoCPMCloudSSLPort,
       "fextInfoCPMReconnectCount": fextInfoCPMReconnectCount,
       "fextTraps": fextTraps,
       "fextTrapSystemReboot": fextTrapSystemReboot,
       "fextTrapOSImageFallback": fextTrapOSImageFallback,
       "fextTrapModeSwitch": fextTrapModeSwitch,
       "fextTrapFGTBackupModeSwitch": fextTrapFGTBackupModeSwitch,
       "fextTrapDataExhausted": fextTrapDataExhausted,
       "fextTrapSessionDisconnect": fextTrapSessionDisconnect,
       "fextTrapLowSignalStrength": fextTrapLowSignalStrength,
       "fextModel": fextModel,
       "fextUnknown": fextUnknown,
       "fextVM": fextVM,
       "fext20D": fext20D,
       "fext40D": fext40D,
       "fext40DA": fext40DA,
       "fext200F": fext200F,
       "fext201E": fext201E,
       "fext202E": fext202E,
       "fext211E": fext211E,
       "fext212E": fext212E,
       "fext30GWifi": fext30GWifi,
       "fext311F": fext311F,
       "fext312F": fext312F,
       "fext511F": fext511F,
       "fextF11A": fextF11A,
       "fextF11E": fextF11E,
       "fer511G": fer511G,
       "fextF21A": fextF21A,
       "fextF21E": fextF21E,
       "fextF22A": fextF22A,
       "fextF22E": fextF22E,
       "fev211FA": fev211FA,
       "fev211F": fev211F,
       "fext212F": fext212F,
       "fev212FA": fev212FA,
       "fev212F": fev212F}
)
