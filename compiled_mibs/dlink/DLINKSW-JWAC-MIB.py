# SNMP MIB module (DLINKSW-JWAC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\DLINKSW-JWAC-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:37:23 2025
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

(dlinkIndustrialCommon,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlinkIndustrialCommon")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressIPv4,
 InetAddressIPv6,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv4",
    "InetAddressIPv6",
    "InetAddressPrefixLength",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dlinkSwJwacMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 155)
)
if mibBuilder.loadTexts:
    dlinkSwJwacMIB.setRevisions(
        ("2013-10-08 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DJwacNotifications_ObjectIdentity = ObjectIdentity
dJwacNotifications = _DJwacNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 155, 0)
)
_DJwacObjects_ObjectIdentity = ObjectIdentity
dJwacObjects = _DJwacObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 155, 1)
)
_DJwacCommonCtrl_ObjectIdentity = ObjectIdentity
dJwacCommonCtrl = _DJwacCommonCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 155, 1, 1)
)
_DJwacSystemAuthEnabled_Type = TruthValue
_DJwacSystemAuthEnabled_Object = MibScalar
dJwacSystemAuthEnabled = _DJwacSystemAuthEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 155, 1, 1, 1),
    _DJwacSystemAuthEnabled_Type()
)
dJwacSystemAuthEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dJwacSystemAuthEnabled.setStatus("current")
_DJwacVirtualIpv4_Type = InetAddressIPv4
_DJwacVirtualIpv4_Object = MibScalar
dJwacVirtualIpv4 = _DJwacVirtualIpv4_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 155, 1, 1, 2),
    _DJwacVirtualIpv4_Type()
)
dJwacVirtualIpv4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dJwacVirtualIpv4.setStatus("current")
_DJwacVirtualIpv6_Type = InetAddressIPv6
_DJwacVirtualIpv6_Object = MibScalar
dJwacVirtualIpv6 = _DJwacVirtualIpv6_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 155, 1, 1, 3),
    _DJwacVirtualIpv6_Type()
)
dJwacVirtualIpv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dJwacVirtualIpv6.setStatus("current")
_DJwacVirtualUrl_Type = SnmpAdminString
_DJwacVirtualUrl_Object = MibScalar
dJwacVirtualUrl = _DJwacVirtualUrl_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 155, 1, 1, 4),
    _DJwacVirtualUrl_Type()
)
dJwacVirtualUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dJwacVirtualUrl.setStatus("current")


class _DJwacAuthMethod_Type(Integer32):
    """Custom type dJwacAuthMethod based on Integer32"""
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
        *(("md5", 1),
          ("chap", 2),
          ("pap", 3),
          ("msChap", 4),
          ("msChapv2", 5))
    )


_DJwacAuthMethod_Type.__name__ = "Integer32"
_DJwacAuthMethod_Object = MibScalar
dJwacAuthMethod = _DJwacAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 155, 1, 1, 5),
    _DJwacAuthMethod_Type()
)
dJwacAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dJwacAuthMethod.setStatus("current")
_DJwacForcibleLogout_Type = TruthValue
_DJwacForcibleLogout_Object = MibScalar
dJwacForcibleLogout = _DJwacForcibleLogout_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 155, 1, 1, 6),
    _DJwacForcibleLogout_Type()
)
dJwacForcibleLogout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dJwacForcibleLogout.setStatus("current")
_DJwacQserverV4Url_Type = SnmpAdminString
_DJwacQserverV4Url_Object = MibScalar
dJwacQserverV4Url = _DJwacQserverV4Url_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 155, 1, 1, 7),
    _DJwacQserverV4Url_Type()
)
dJwacQserverV4Url.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dJwacQserverV4Url.setStatus("current")
_DJwacQserverV6Url_Type = SnmpAdminString
_DJwacQserverV6Url_Object = MibScalar
dJwacQserverV6Url = _DJwacQserverV6Url_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 155, 1, 1, 8),
    _DJwacQserverV6Url_Type()
)
dJwacQserverV6Url.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dJwacQserverV6Url.setStatus("current")
_DJwacQserverMonitorEnabled_Type = TruthValue
_DJwacQserverMonitorEnabled_Object = MibScalar
dJwacQserverMonitorEnabled = _DJwacQserverMonitorEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 155, 1, 1, 9),
    _DJwacQserverMonitorEnabled_Type()
)
dJwacQserverMonitorEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dJwacQserverMonitorEnabled.setStatus("current")


class _DJwacQserverTimeOut_Type(Unsigned32):
    """Custom type dJwacQserverTimeOut based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 300),
    )


_DJwacQserverTimeOut_Type.__name__ = "Unsigned32"
_DJwacQserverTimeOut_Object = MibScalar
dJwacQserverTimeOut = _DJwacQserverTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 155, 1, 1, 10),
    _DJwacQserverTimeOut_Type()
)
dJwacQserverTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dJwacQserverTimeOut.setStatus("current")
_DJwacRedirectEnabled_Type = TruthValue
_DJwacRedirectEnabled_Object = MibScalar
dJwacRedirectEnabled = _DJwacRedirectEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 155, 1, 1, 11),
    _DJwacRedirectEnabled_Type()
)
dJwacRedirectEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dJwacRedirectEnabled.setStatus("current")


class _DJwacRedirectDestination_Type(Integer32):
    """Custom type dJwacRedirectDestination based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("quarantineServer", 1),
          ("jwacLoginPage", 2))
    )


_DJwacRedirectDestination_Type.__name__ = "Integer32"
_DJwacRedirectDestination_Object = MibScalar
dJwacRedirectDestination = _DJwacRedirectDestination_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 155, 1, 1, 12),
    _DJwacRedirectDestination_Type()
)
dJwacRedirectDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dJwacRedirectDestination.setStatus("current")


class _DJwacRedirectDelayTime_Type(Unsigned32):
    """Custom type dJwacRedirectDelayTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_DJwacRedirectDelayTime_Type.__name__ = "Unsigned32"
_DJwacRedirectDelayTime_Object = MibScalar
dJwacRedirectDelayTime = _DJwacRedirectDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 155, 1, 1, 13),
    _DJwacRedirectDelayTime_Type()
)
dJwacRedirectDelayTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dJwacRedirectDelayTime.setStatus("current")
_DJwacUdpFiltering_Type = TruthValue
_DJwacUdpFiltering_Object = MibScalar
dJwacUdpFiltering = _DJwacUdpFiltering_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 155, 1, 1, 14),
    _DJwacUdpFiltering_Type()
)
dJwacUdpFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dJwacUdpFiltering.setStatus("current")


class _DJwacAuthPageLanguage_Type(Integer32):
    """Custom type dJwacAuthPageLanguage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("japanese", 1),
          ("english", 2))
    )


_DJwacAuthPageLanguage_Type.__name__ = "Integer32"
_DJwacAuthPageLanguage_Object = MibScalar
dJwacAuthPageLanguage = _DJwacAuthPageLanguage_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 155, 1, 1, 15),
    _DJwacAuthPageLanguage_Type()
)
dJwacAuthPageLanguage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dJwacAuthPageLanguage.setStatus("current")
_DJwacInterfaceCtrl_ObjectIdentity = ObjectIdentity
dJwacInterfaceCtrl = _DJwacInterfaceCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 155, 1, 2)
)
_DJwacIfCfgTable_Object = MibTable
dJwacIfCfgTable = _DJwacIfCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 155, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dJwacIfCfgTable.setStatus("current")
_DJwacIfCfgEntry_Object = MibTableRow
dJwacIfCfgEntry = _DJwacIfCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 155, 1, 2, 1, 1)
)
dJwacIfCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dJwacIfCfgEntry.setStatus("current")
_DJwacIfAuthEnabled_Type = TruthValue
_DJwacIfAuthEnabled_Object = MibTableColumn
dJwacIfAuthEnabled = _DJwacIfAuthEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 155, 1, 2, 1, 1, 1),
    _DJwacIfAuthEnabled_Type()
)
dJwacIfAuthEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dJwacIfAuthEnabled.setStatus("current")


class _DJwacMaxAuthingUser_Type(Unsigned32):
    """Custom type dJwacMaxAuthingUser based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DJwacMaxAuthingUser_Type.__name__ = "Unsigned32"
_DJwacMaxAuthingUser_Object = MibTableColumn
dJwacMaxAuthingUser = _DJwacMaxAuthingUser_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 155, 1, 2, 1, 1, 2),
    _DJwacMaxAuthingUser_Type()
)
dJwacMaxAuthingUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dJwacMaxAuthingUser.setStatus("current")
_DJwacPageElementsCtrl_ObjectIdentity = ObjectIdentity
dJwacPageElementsCtrl = _DJwacPageElementsCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 155, 1, 3)
)
_DJwacPageElementTable_Object = MibTable
dJwacPageElementTable = _DJwacPageElementTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 155, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dJwacPageElementTable.setStatus("current")
_DJwacPageElementEntry_Object = MibTableRow
dJwacPageElementEntry = _DJwacPageElementEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 155, 1, 3, 1, 1)
)
dJwacPageElementEntry.setIndexNames(
    (0, "DLINKSW-JWAC-MIB", "dJwacPageLanguage"),
)
if mibBuilder.loadTexts:
    dJwacPageElementEntry.setStatus("current")


class _DJwacPageLanguage_Type(Integer32):
    """Custom type dJwacPageLanguage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("japanese", 1),
          ("english", 2))
    )


_DJwacPageLanguage_Type.__name__ = "Integer32"
_DJwacPageLanguage_Object = MibTableColumn
dJwacPageLanguage = _DJwacPageLanguage_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 155, 1, 3, 1, 1, 1),
    _DJwacPageLanguage_Type()
)
dJwacPageLanguage.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dJwacPageLanguage.setStatus("current")
_DJwacPageTitle_Type = SnmpAdminString
_DJwacPageTitle_Object = MibTableColumn
dJwacPageTitle = _DJwacPageTitle_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 155, 1, 3, 1, 1, 2),
    _DJwacPageTitle_Type()
)
dJwacPageTitle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dJwacPageTitle.setStatus("current")
_DJwacPageLoginWindowTitle_Type = SnmpAdminString
_DJwacPageLoginWindowTitle_Object = MibTableColumn
dJwacPageLoginWindowTitle = _DJwacPageLoginWindowTitle_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 155, 1, 3, 1, 1, 3),
    _DJwacPageLoginWindowTitle_Type()
)
dJwacPageLoginWindowTitle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dJwacPageLoginWindowTitle.setStatus("current")
_DJwacPageUserName_Type = SnmpAdminString
_DJwacPageUserName_Object = MibTableColumn
dJwacPageUserName = _DJwacPageUserName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 155, 1, 3, 1, 1, 4),
    _DJwacPageUserName_Type()
)
dJwacPageUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dJwacPageUserName.setStatus("current")
_DJwacPagePassWord_Type = SnmpAdminString
_DJwacPagePassWord_Object = MibTableColumn
dJwacPagePassWord = _DJwacPagePassWord_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 155, 1, 3, 1, 1, 5),
    _DJwacPagePassWord_Type()
)
dJwacPagePassWord.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dJwacPagePassWord.setStatus("current")
_DJwacPageLogoutWindowTitle_Type = SnmpAdminString
_DJwacPageLogoutWindowTitle_Object = MibTableColumn
dJwacPageLogoutWindowTitle = _DJwacPageLogoutWindowTitle_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 155, 1, 3, 1, 1, 6),
    _DJwacPageLogoutWindowTitle_Type()
)
dJwacPageLogoutWindowTitle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dJwacPageLogoutWindowTitle.setStatus("current")
_DJwacPageCopyrightLine1_Type = SnmpAdminString
_DJwacPageCopyrightLine1_Object = MibTableColumn
dJwacPageCopyrightLine1 = _DJwacPageCopyrightLine1_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 155, 1, 3, 1, 1, 7),
    _DJwacPageCopyrightLine1_Type()
)
dJwacPageCopyrightLine1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dJwacPageCopyrightLine1.setStatus("current")
_DJwacPageCopyrightLine2_Type = SnmpAdminString
_DJwacPageCopyrightLine2_Object = MibTableColumn
dJwacPageCopyrightLine2 = _DJwacPageCopyrightLine2_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 155, 1, 3, 1, 1, 8),
    _DJwacPageCopyrightLine2_Type()
)
dJwacPageCopyrightLine2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dJwacPageCopyrightLine2.setStatus("current")
_DJwacPageCopyrightLine3_Type = SnmpAdminString
_DJwacPageCopyrightLine3_Object = MibTableColumn
dJwacPageCopyrightLine3 = _DJwacPageCopyrightLine3_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 155, 1, 3, 1, 1, 9),
    _DJwacPageCopyrightLine3_Type()
)
dJwacPageCopyrightLine3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dJwacPageCopyrightLine3.setStatus("current")
_DJwacPageCopyrightLine4_Type = SnmpAdminString
_DJwacPageCopyrightLine4_Object = MibTableColumn
dJwacPageCopyrightLine4 = _DJwacPageCopyrightLine4_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 155, 1, 3, 1, 1, 10),
    _DJwacPageCopyrightLine4_Type()
)
dJwacPageCopyrightLine4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dJwacPageCopyrightLine4.setStatus("current")
_DJwacPageCopyrightLine5_Type = SnmpAdminString
_DJwacPageCopyrightLine5_Object = MibTableColumn
dJwacPageCopyrightLine5 = _DJwacPageCopyrightLine5_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 155, 1, 3, 1, 1, 11),
    _DJwacPageCopyrightLine5_Type()
)
dJwacPageCopyrightLine5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dJwacPageCopyrightLine5.setStatus("current")
_DJwacUpdateServerCtrl_ObjectIdentity = ObjectIdentity
dJwacUpdateServerCtrl = _DJwacUpdateServerCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 155, 1, 4)
)
_DJwacUpdateServerTable_Object = MibTable
dJwacUpdateServerTable = _DJwacUpdateServerTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 155, 1, 4, 1)
)
if mibBuilder.loadTexts:
    dJwacUpdateServerTable.setStatus("current")
_DJwacUpdateServerEntry_Object = MibTableRow
dJwacUpdateServerEntry = _DJwacUpdateServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 155, 1, 4, 1, 1)
)
dJwacUpdateServerEntry.setIndexNames(
    (0, "DLINKSW-JWAC-MIB", "dJwacUpdateServerAddrType"),
    (0, "DLINKSW-JWAC-MIB", "dJwacUpdateServerAddr"),
    (0, "DLINKSW-JWAC-MIB", "dJwacUpdateServerPrefixLen"),
    (0, "DLINKSW-JWAC-MIB", "dJwacUpdateServerProtocol"),
    (0, "DLINKSW-JWAC-MIB", "dJwacUpdateServerPort"),
)
if mibBuilder.loadTexts:
    dJwacUpdateServerEntry.setStatus("current")
_DJwacUpdateServerAddrType_Type = InetAddressType
_DJwacUpdateServerAddrType_Object = MibTableColumn
dJwacUpdateServerAddrType = _DJwacUpdateServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 155, 1, 4, 1, 1, 1),
    _DJwacUpdateServerAddrType_Type()
)
dJwacUpdateServerAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dJwacUpdateServerAddrType.setStatus("current")
_DJwacUpdateServerAddr_Type = InetAddress
_DJwacUpdateServerAddr_Object = MibTableColumn
dJwacUpdateServerAddr = _DJwacUpdateServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 155, 1, 4, 1, 1, 2),
    _DJwacUpdateServerAddr_Type()
)
dJwacUpdateServerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dJwacUpdateServerAddr.setStatus("current")
_DJwacUpdateServerPrefixLen_Type = InetAddressPrefixLength
_DJwacUpdateServerPrefixLen_Object = MibTableColumn
dJwacUpdateServerPrefixLen = _DJwacUpdateServerPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 155, 1, 4, 1, 1, 3),
    _DJwacUpdateServerPrefixLen_Type()
)
dJwacUpdateServerPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dJwacUpdateServerPrefixLen.setStatus("current")


class _DJwacUpdateServerProtocol_Type(Integer32):
    """Custom type dJwacUpdateServerProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("tcp", 2),
          ("udp", 3))
    )


_DJwacUpdateServerProtocol_Type.__name__ = "Integer32"
_DJwacUpdateServerProtocol_Object = MibTableColumn
dJwacUpdateServerProtocol = _DJwacUpdateServerProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 155, 1, 4, 1, 1, 4),
    _DJwacUpdateServerProtocol_Type()
)
dJwacUpdateServerProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dJwacUpdateServerProtocol.setStatus("current")


class _DJwacUpdateServerPort_Type(Unsigned32):
    """Custom type dJwacUpdateServerPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DJwacUpdateServerPort_Type.__name__ = "Unsigned32"
_DJwacUpdateServerPort_Object = MibTableColumn
dJwacUpdateServerPort = _DJwacUpdateServerPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 155, 1, 4, 1, 1, 5),
    _DJwacUpdateServerPort_Type()
)
dJwacUpdateServerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dJwacUpdateServerPort.setStatus("current")
_DJwacupdateServerRowStatus_Type = RowStatus
_DJwacupdateServerRowStatus_Object = MibTableColumn
dJwacupdateServerRowStatus = _DJwacupdateServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 155, 1, 4, 1, 1, 99),
    _DJwacupdateServerRowStatus_Type()
)
dJwacupdateServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dJwacupdateServerRowStatus.setStatus("current")
_DJwacConformance_ObjectIdentity = ObjectIdentity
dJwacConformance = _DJwacConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 155, 2)
)
_DJwacMIBCompliances_ObjectIdentity = ObjectIdentity
dJwacMIBCompliances = _DJwacMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 155, 2, 1)
)
_DJwacMIBGroups_ObjectIdentity = ObjectIdentity
dJwacMIBGroups = _DJwacMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 155, 2, 2)
)

# Managed Objects groups

dJwacCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 155, 2, 2, 1)
)
dJwacCfgGroup.setObjects(
      *(("DLINKSW-JWAC-MIB", "dJwacSystemAuthEnabled"),
        ("DLINKSW-JWAC-MIB", "dJwacVirtualIpv4"),
        ("DLINKSW-JWAC-MIB", "dJwacVirtualIpv6"),
        ("DLINKSW-JWAC-MIB", "dJwacVirtualUrl"),
        ("DLINKSW-JWAC-MIB", "dJwacAuthMethod"),
        ("DLINKSW-JWAC-MIB", "dJwacForcibleLogout"),
        ("DLINKSW-JWAC-MIB", "dJwacQserverV4Url"),
        ("DLINKSW-JWAC-MIB", "dJwacQserverV6Url"),
        ("DLINKSW-JWAC-MIB", "dJwacQserverMonitorEnabled"),
        ("DLINKSW-JWAC-MIB", "dJwacQserverTimeOut"),
        ("DLINKSW-JWAC-MIB", "dJwacRedirectEnabled"),
        ("DLINKSW-JWAC-MIB", "dJwacRedirectDestination"),
        ("DLINKSW-JWAC-MIB", "dJwacRedirectDelayTime"),
        ("DLINKSW-JWAC-MIB", "dJwacUdpFiltering"),
        ("DLINKSW-JWAC-MIB", "dJwacAuthPageLanguage"))
)
if mibBuilder.loadTexts:
    dJwacCfgGroup.setStatus("current")

dJwacIfCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 155, 2, 2, 2)
)
dJwacIfCfgGroup.setObjects(
      *(("DLINKSW-JWAC-MIB", "dJwacIfAuthEnabled"),
        ("DLINKSW-JWAC-MIB", "dJwacMaxAuthingUser"))
)
if mibBuilder.loadTexts:
    dJwacIfCfgGroup.setStatus("current")

dJwacPageElementsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 155, 2, 2, 3)
)
dJwacPageElementsGroup.setObjects(
      *(("DLINKSW-JWAC-MIB", "dJwacPageTitle"),
        ("DLINKSW-JWAC-MIB", "dJwacPageLoginWindowTitle"),
        ("DLINKSW-JWAC-MIB", "dJwacPageUserName"),
        ("DLINKSW-JWAC-MIB", "dJwacPagePassWord"),
        ("DLINKSW-JWAC-MIB", "dJwacPageLogoutWindowTitle"),
        ("DLINKSW-JWAC-MIB", "dJwacPageCopyrightLine1"),
        ("DLINKSW-JWAC-MIB", "dJwacPageCopyrightLine2"),
        ("DLINKSW-JWAC-MIB", "dJwacPageCopyrightLine3"),
        ("DLINKSW-JWAC-MIB", "dJwacPageCopyrightLine4"),
        ("DLINKSW-JWAC-MIB", "dJwacPageCopyrightLine5"))
)
if mibBuilder.loadTexts:
    dJwacPageElementsGroup.setStatus("current")

dJwacUpdateServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 155, 2, 2, 4)
)
dJwacUpdateServerGroup.setObjects(
      *(("DLINKSW-JWAC-MIB", "dJwacUpdateServerAddrType"),
        ("DLINKSW-JWAC-MIB", "dJwacUpdateServerAddr"),
        ("DLINKSW-JWAC-MIB", "dJwacUpdateServerPrefixLen"),
        ("DLINKSW-JWAC-MIB", "dJwacUpdateServerProtocol"),
        ("DLINKSW-JWAC-MIB", "dJwacUpdateServerPort"),
        ("DLINKSW-JWAC-MIB", "dJwacupdateServerRowStatus"))
)
if mibBuilder.loadTexts:
    dJwacUpdateServerGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dJwacMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 14, 155, 2, 1, 1)
)
dJwacMIBCompliance.setObjects(
      *(("DLINKSW-JWAC-MIB", "dJwacCfgGroup"),
        ("DLINKSW-JWAC-MIB", "dJwacIfCfgGroup"),
        ("DLINKSW-JWAC-MIB", "dJwacPageElementsGroup"),
        ("DLINKSW-JWAC-MIB", "dJwacUpdateServerGroup"))
)
if mibBuilder.loadTexts:
    dJwacMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKSW-JWAC-MIB",
    **{"dlinkSwJwacMIB": dlinkSwJwacMIB,
       "dJwacNotifications": dJwacNotifications,
       "dJwacObjects": dJwacObjects,
       "dJwacCommonCtrl": dJwacCommonCtrl,
       "dJwacSystemAuthEnabled": dJwacSystemAuthEnabled,
       "dJwacVirtualIpv4": dJwacVirtualIpv4,
       "dJwacVirtualIpv6": dJwacVirtualIpv6,
       "dJwacVirtualUrl": dJwacVirtualUrl,
       "dJwacAuthMethod": dJwacAuthMethod,
       "dJwacForcibleLogout": dJwacForcibleLogout,
       "dJwacQserverV4Url": dJwacQserverV4Url,
       "dJwacQserverV6Url": dJwacQserverV6Url,
       "dJwacQserverMonitorEnabled": dJwacQserverMonitorEnabled,
       "dJwacQserverTimeOut": dJwacQserverTimeOut,
       "dJwacRedirectEnabled": dJwacRedirectEnabled,
       "dJwacRedirectDestination": dJwacRedirectDestination,
       "dJwacRedirectDelayTime": dJwacRedirectDelayTime,
       "dJwacUdpFiltering": dJwacUdpFiltering,
       "dJwacAuthPageLanguage": dJwacAuthPageLanguage,
       "dJwacInterfaceCtrl": dJwacInterfaceCtrl,
       "dJwacIfCfgTable": dJwacIfCfgTable,
       "dJwacIfCfgEntry": dJwacIfCfgEntry,
       "dJwacIfAuthEnabled": dJwacIfAuthEnabled,
       "dJwacMaxAuthingUser": dJwacMaxAuthingUser,
       "dJwacPageElementsCtrl": dJwacPageElementsCtrl,
       "dJwacPageElementTable": dJwacPageElementTable,
       "dJwacPageElementEntry": dJwacPageElementEntry,
       "dJwacPageLanguage": dJwacPageLanguage,
       "dJwacPageTitle": dJwacPageTitle,
       "dJwacPageLoginWindowTitle": dJwacPageLoginWindowTitle,
       "dJwacPageUserName": dJwacPageUserName,
       "dJwacPagePassWord": dJwacPagePassWord,
       "dJwacPageLogoutWindowTitle": dJwacPageLogoutWindowTitle,
       "dJwacPageCopyrightLine1": dJwacPageCopyrightLine1,
       "dJwacPageCopyrightLine2": dJwacPageCopyrightLine2,
       "dJwacPageCopyrightLine3": dJwacPageCopyrightLine3,
       "dJwacPageCopyrightLine4": dJwacPageCopyrightLine4,
       "dJwacPageCopyrightLine5": dJwacPageCopyrightLine5,
       "dJwacUpdateServerCtrl": dJwacUpdateServerCtrl,
       "dJwacUpdateServerTable": dJwacUpdateServerTable,
       "dJwacUpdateServerEntry": dJwacUpdateServerEntry,
       "dJwacUpdateServerAddrType": dJwacUpdateServerAddrType,
       "dJwacUpdateServerAddr": dJwacUpdateServerAddr,
       "dJwacUpdateServerPrefixLen": dJwacUpdateServerPrefixLen,
       "dJwacUpdateServerProtocol": dJwacUpdateServerProtocol,
       "dJwacUpdateServerPort": dJwacUpdateServerPort,
       "dJwacupdateServerRowStatus": dJwacupdateServerRowStatus,
       "dJwacConformance": dJwacConformance,
       "dJwacMIBCompliances": dJwacMIBCompliances,
       "dJwacMIBCompliance": dJwacMIBCompliance,
       "dJwacMIBGroups": dJwacMIBGroups,
       "dJwacCfgGroup": dJwacCfgGroup,
       "dJwacIfCfgGroup": dJwacIfCfgGroup,
       "dJwacPageElementsGroup": dJwacPageElementsGroup,
       "dJwacUpdateServerGroup": dJwacUpdateServerGroup}
)
