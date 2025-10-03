# SNMP MIB module (AT-UWC-WLAN-SWITCH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\awplus\AT-UWC-WLAN-SWITCH-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:20:41 2025
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

(atUWC,
 wirelesslan) = mibBuilder.importSymbols(
    "AT-SMI-MIB",
    "atUWC",
    "wirelesslan")

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

(DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

fastPathWLANSwitch = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34)
)
if mibBuilder.loadTexts:
    fastPathWLANSwitch.setRevisions(
        ("2014-12-04 00:00",
         "2014-11-07 00:00",
         "2014-10-29 00:00",
         "2014-09-30 00:00",
         "2014-05-29 00:00",
         "2012-11-29 00:00",
         "2012-06-15 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class WsOui(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3



class TspecSuppAC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("voice", 0),
          ("video", 1))
    )



# MIB Managed Objects in the order of their OIDs

_At_uwc_ObjectIdentity = ObjectIdentity
at_uwc = _At_uwc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 13, 21)
)
_WsTraps_ObjectIdentity = ObjectIdentity
wsTraps = _WsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 0)
)
_WsGlobalConfig_ObjectIdentity = ObjectIdentity
wsGlobalConfig = _WsGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1)
)


class _WsMode_Type(Integer32):
    """Custom type wsMode based on Integer32"""
    defaultValue = 2

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


_WsMode_Type.__name__ = "Integer32"
_WsMode_Object = MibScalar
wsMode = _WsMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 1),
    _WsMode_Type()
)
wsMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMode.setStatus("current")


class _WsCountryCode_Type(DisplayString):
    """Custom type wsCountryCode based on DisplayString"""
    defaultValue = OctetString("US")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_WsCountryCode_Type.__name__ = "DisplayString"
_WsCountryCode_Object = MibScalar
wsCountryCode = _WsCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 2),
    _WsCountryCode_Type()
)
wsCountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsCountryCode.setStatus("current")


class _WsPeerGroupId_Type(Integer32):
    """Custom type wsPeerGroupId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WsPeerGroupId_Type.__name__ = "Integer32"
_WsPeerGroupId_Object = MibScalar
wsPeerGroupId = _WsPeerGroupId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 3),
    _WsPeerGroupId_Type()
)
wsPeerGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPeerGroupId.setStatus("current")


class _WsAPValidationMethod_Type(Integer32):
    """Custom type wsAPValidationMethod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("radius", 2))
    )


_WsAPValidationMethod_Type.__name__ = "Integer32"
_WsAPValidationMethod_Object = MibScalar
wsAPValidationMethod = _WsAPValidationMethod_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 4),
    _WsAPValidationMethod_Type()
)
wsAPValidationMethod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAPValidationMethod.setStatus("current")


class _WsAPAuthenticationMode_Type(Integer32):
    """Custom type wsAPAuthenticationMode based on Integer32"""
    defaultValue = 2

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


_WsAPAuthenticationMode_Type.__name__ = "Integer32"
_WsAPAuthenticationMode_Object = MibScalar
wsAPAuthenticationMode = _WsAPAuthenticationMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 5),
    _WsAPAuthenticationMode_Type()
)
wsAPAuthenticationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPAuthenticationMode.setStatus("current")


class _WsClientRoamAgeTime_Type(Unsigned32):
    """Custom type wsClientRoamAgeTime based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_WsClientRoamAgeTime_Type.__name__ = "Unsigned32"
_WsClientRoamAgeTime_Object = MibScalar
wsClientRoamAgeTime = _WsClientRoamAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 6),
    _WsClientRoamAgeTime_Type()
)
wsClientRoamAgeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsClientRoamAgeTime.setStatus("current")


class _WsRFScanAgeTime_Type(Unsigned32):
    """Custom type wsRFScanAgeTime based on Unsigned32"""
    defaultValue = 24

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 168),
    )


_WsRFScanAgeTime_Type.__name__ = "Unsigned32"
_WsRFScanAgeTime_Object = MibScalar
wsRFScanAgeTime = _WsRFScanAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 7),
    _WsRFScanAgeTime_Type()
)
wsRFScanAgeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRFScanAgeTime.setStatus("current")


class _WsAPFailureAgeTime_Type(Unsigned32):
    """Custom type wsAPFailureAgeTime based on Unsigned32"""
    defaultValue = 24

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 168),
    )


_WsAPFailureAgeTime_Type.__name__ = "Unsigned32"
_WsAPFailureAgeTime_Object = MibScalar
wsAPFailureAgeTime = _WsAPFailureAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 8),
    _WsAPFailureAgeTime_Type()
)
wsAPFailureAgeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPFailureAgeTime.setStatus("current")


class _WsAdHocClientAgeTime_Type(Unsigned32):
    """Custom type wsAdHocClientAgeTime based on Unsigned32"""
    defaultValue = 24

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 168),
    )


_WsAdHocClientAgeTime_Type.__name__ = "Unsigned32"
_WsAdHocClientAgeTime_Object = MibScalar
wsAdHocClientAgeTime = _WsAdHocClientAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 9),
    _WsAdHocClientAgeTime_Type()
)
wsAdHocClientAgeTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAdHocClientAgeTime.setStatus("current")


class _WsDetectedClientAgeTime_Type(Unsigned32):
    """Custom type wsDetectedClientAgeTime based on Unsigned32"""
    defaultValue = 24

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 168),
    )


_WsDetectedClientAgeTime_Type.__name__ = "Unsigned32"
_WsDetectedClientAgeTime_Object = MibScalar
wsDetectedClientAgeTime = _WsDetectedClientAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 10),
    _WsDetectedClientAgeTime_Type()
)
wsDetectedClientAgeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedClientAgeTime.setStatus("current")
_WsValidAPConfigTable_Object = MibTable
wsValidAPConfigTable = _WsValidAPConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 11)
)
if mibBuilder.loadTexts:
    wsValidAPConfigTable.setStatus("current")
_WsValidAPConfigEntry_Object = MibTableRow
wsValidAPConfigEntry = _WsValidAPConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 11, 1)
)
wsValidAPConfigEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsAPMacAddress"),
)
if mibBuilder.loadTexts:
    wsValidAPConfigEntry.setStatus("current")
_WsAPMacAddress_Type = MacAddress
_WsAPMacAddress_Object = MibTableColumn
wsAPMacAddress = _WsAPMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 11, 1, 1),
    _WsAPMacAddress_Type()
)
wsAPMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPMacAddress.setStatus("current")


class _WsAPLocation_Type(DisplayString):
    """Custom type wsAPLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WsAPLocation_Type.__name__ = "DisplayString"
_WsAPLocation_Object = MibTableColumn
wsAPLocation = _WsAPLocation_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 11, 1, 2),
    _WsAPLocation_Type()
)
wsAPLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPLocation.setStatus("current")


class _WsAPMode_Type(Integer32):
    """Custom type wsAPMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("wsManaged", 1),
          ("standalone", 2),
          ("rogue", 3))
    )


_WsAPMode_Type.__name__ = "Integer32"
_WsAPMode_Object = MibTableColumn
wsAPMode = _WsAPMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 11, 1, 3),
    _WsAPMode_Type()
)
wsAPMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPMode.setStatus("current")


class _WsAPAuthenticationPasswd_Type(DisplayString):
    """Custom type wsAPAuthenticationPasswd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 63),
    )


_WsAPAuthenticationPasswd_Type.__name__ = "DisplayString"
_WsAPAuthenticationPasswd_Object = MibTableColumn
wsAPAuthenticationPasswd = _WsAPAuthenticationPasswd_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 11, 1, 4),
    _WsAPAuthenticationPasswd_Type()
)
wsAPAuthenticationPasswd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPAuthenticationPasswd.setStatus("current")


class _WsUseAPProfileId_Type(Integer32):
    """Custom type wsUseAPProfileId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_WsUseAPProfileId_Type.__name__ = "Integer32"
_WsUseAPProfileId_Object = MibTableColumn
wsUseAPProfileId = _WsUseAPProfileId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 11, 1, 5),
    _WsUseAPProfileId_Type()
)
wsUseAPProfileId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsUseAPProfileId.setStatus("current")


class _WsAPRadio1Channel_Type(Integer32):
    """Custom type wsAPRadio1Channel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
        ValueRangeConstraint(36, 36),
        ValueRangeConstraint(40, 40),
        ValueRangeConstraint(42, 42),
        ValueRangeConstraint(44, 44),
        ValueRangeConstraint(48, 48),
        ValueRangeConstraint(50, 50),
        ValueRangeConstraint(52, 52),
        ValueRangeConstraint(56, 56),
        ValueRangeConstraint(58, 58),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(64, 64),
        ValueRangeConstraint(100, 100),
        ValueRangeConstraint(104, 104),
        ValueRangeConstraint(108, 108),
        ValueRangeConstraint(112, 112),
        ValueRangeConstraint(116, 116),
        ValueRangeConstraint(120, 120),
        ValueRangeConstraint(124, 124),
        ValueRangeConstraint(128, 128),
        ValueRangeConstraint(132, 132),
        ValueRangeConstraint(136, 136),
        ValueRangeConstraint(140, 140),
        ValueRangeConstraint(149, 149),
        ValueRangeConstraint(152, 152),
        ValueRangeConstraint(153, 153),
        ValueRangeConstraint(157, 157),
        ValueRangeConstraint(160, 160),
        ValueRangeConstraint(161, 161),
        ValueRangeConstraint(165, 165),
    )


_WsAPRadio1Channel_Type.__name__ = "Integer32"
_WsAPRadio1Channel_Object = MibTableColumn
wsAPRadio1Channel = _WsAPRadio1Channel_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 11, 1, 6),
    _WsAPRadio1Channel_Type()
)
wsAPRadio1Channel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPRadio1Channel.setStatus("current")


class _WsAPRadio2Channel_Type(Integer32):
    """Custom type wsAPRadio2Channel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
        ValueRangeConstraint(36, 36),
        ValueRangeConstraint(40, 40),
        ValueRangeConstraint(42, 42),
        ValueRangeConstraint(44, 44),
        ValueRangeConstraint(48, 48),
        ValueRangeConstraint(50, 50),
        ValueRangeConstraint(52, 52),
        ValueRangeConstraint(56, 56),
        ValueRangeConstraint(58, 58),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(64, 64),
        ValueRangeConstraint(100, 100),
        ValueRangeConstraint(104, 104),
        ValueRangeConstraint(108, 108),
        ValueRangeConstraint(112, 112),
        ValueRangeConstraint(116, 116),
        ValueRangeConstraint(120, 120),
        ValueRangeConstraint(124, 124),
        ValueRangeConstraint(128, 128),
        ValueRangeConstraint(132, 132),
        ValueRangeConstraint(136, 136),
        ValueRangeConstraint(140, 140),
        ValueRangeConstraint(149, 149),
        ValueRangeConstraint(152, 152),
        ValueRangeConstraint(153, 153),
        ValueRangeConstraint(157, 157),
        ValueRangeConstraint(160, 160),
        ValueRangeConstraint(161, 161),
        ValueRangeConstraint(165, 165),
    )


_WsAPRadio2Channel_Type.__name__ = "Integer32"
_WsAPRadio2Channel_Object = MibTableColumn
wsAPRadio2Channel = _WsAPRadio2Channel_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 11, 1, 7),
    _WsAPRadio2Channel_Type()
)
wsAPRadio2Channel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPRadio2Channel.setStatus("current")


class _WsAPRadio1TxPower_Type(Integer32):
    """Custom type wsAPRadio1TxPower based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_WsAPRadio1TxPower_Type.__name__ = "Integer32"
_WsAPRadio1TxPower_Object = MibTableColumn
wsAPRadio1TxPower = _WsAPRadio1TxPower_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 11, 1, 8),
    _WsAPRadio1TxPower_Type()
)
wsAPRadio1TxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPRadio1TxPower.setStatus("current")


class _WsAPRadio2TxPower_Type(Integer32):
    """Custom type wsAPRadio2TxPower based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_WsAPRadio2TxPower_Type.__name__ = "Integer32"
_WsAPRadio2TxPower_Object = MibTableColumn
wsAPRadio2TxPower = _WsAPRadio2TxPower_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 11, 1, 9),
    _WsAPRadio2TxPower_Type()
)
wsAPRadio2TxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPRadio2TxPower.setStatus("current")


class _WsAPStandaloneExpectedChannel_Type(Integer32):
    """Custom type wsAPStandaloneExpectedChannel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
        ValueRangeConstraint(36, 36),
        ValueRangeConstraint(40, 40),
        ValueRangeConstraint(42, 42),
        ValueRangeConstraint(44, 44),
        ValueRangeConstraint(48, 48),
        ValueRangeConstraint(50, 50),
        ValueRangeConstraint(52, 52),
        ValueRangeConstraint(56, 56),
        ValueRangeConstraint(58, 58),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(64, 64),
        ValueRangeConstraint(100, 100),
        ValueRangeConstraint(104, 104),
        ValueRangeConstraint(108, 108),
        ValueRangeConstraint(112, 112),
        ValueRangeConstraint(116, 116),
        ValueRangeConstraint(120, 120),
        ValueRangeConstraint(124, 124),
        ValueRangeConstraint(128, 128),
        ValueRangeConstraint(132, 132),
        ValueRangeConstraint(136, 136),
        ValueRangeConstraint(140, 140),
        ValueRangeConstraint(149, 149),
        ValueRangeConstraint(152, 152),
        ValueRangeConstraint(153, 153),
        ValueRangeConstraint(157, 157),
        ValueRangeConstraint(160, 160),
        ValueRangeConstraint(161, 161),
        ValueRangeConstraint(165, 165),
    )


_WsAPStandaloneExpectedChannel_Type.__name__ = "Integer32"
_WsAPStandaloneExpectedChannel_Object = MibTableColumn
wsAPStandaloneExpectedChannel = _WsAPStandaloneExpectedChannel_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 11, 1, 10),
    _WsAPStandaloneExpectedChannel_Type()
)
wsAPStandaloneExpectedChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPStandaloneExpectedChannel.setStatus("current")


class _WsAPStandaloneExpectedSecurity_Type(Integer32):
    """Custom type wsAPStandaloneExpectedSecurity based on Integer32"""
    defaultValue = 0

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
        *(("any", 0),
          ("open", 1),
          ("wep", 2),
          ("wpa", 3))
    )


_WsAPStandaloneExpectedSecurity_Type.__name__ = "Integer32"
_WsAPStandaloneExpectedSecurity_Object = MibTableColumn
wsAPStandaloneExpectedSecurity = _WsAPStandaloneExpectedSecurity_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 11, 1, 11),
    _WsAPStandaloneExpectedSecurity_Type()
)
wsAPStandaloneExpectedSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPStandaloneExpectedSecurity.setStatus("current")


class _WsAPStandaloneExpectedSsid_Type(DisplayString):
    """Custom type wsAPStandaloneExpectedSsid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WsAPStandaloneExpectedSsid_Type.__name__ = "DisplayString"
_WsAPStandaloneExpectedSsid_Object = MibTableColumn
wsAPStandaloneExpectedSsid = _WsAPStandaloneExpectedSsid_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 11, 1, 12),
    _WsAPStandaloneExpectedSsid_Type()
)
wsAPStandaloneExpectedSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPStandaloneExpectedSsid.setStatus("current")


class _WsAPStandaloneExpectedWds_Type(Integer32):
    """Custom type wsAPStandaloneExpectedWds based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 0),
          ("normal", 1),
          ("bridge", 2))
    )


_WsAPStandaloneExpectedWds_Type.__name__ = "Integer32"
_WsAPStandaloneExpectedWds_Object = MibTableColumn
wsAPStandaloneExpectedWds = _WsAPStandaloneExpectedWds_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 11, 1, 13),
    _WsAPStandaloneExpectedWds_Type()
)
wsAPStandaloneExpectedWds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPStandaloneExpectedWds.setStatus("current")


class _WsAPStandaloneExpectedWired_Type(Integer32):
    """Custom type wsAPStandaloneExpectedWired based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 0),
          ("not-allowed", 1))
    )


_WsAPStandaloneExpectedWired_Type.__name__ = "Integer32"
_WsAPStandaloneExpectedWired_Object = MibTableColumn
wsAPStandaloneExpectedWired = _WsAPStandaloneExpectedWired_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 11, 1, 14),
    _WsAPStandaloneExpectedWired_Type()
)
wsAPStandaloneExpectedWired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPStandaloneExpectedWired.setStatus("current")
_WsAPConfigRowStatus_Type = RowStatus
_WsAPConfigRowStatus_Object = MibTableColumn
wsAPConfigRowStatus = _WsAPConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 11, 1, 15),
    _WsAPConfigRowStatus_Type()
)
wsAPConfigRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPConfigRowStatus.setStatus("current")
_WsGlobalStatus_ObjectIdentity = ObjectIdentity
wsGlobalStatus = _WsGlobalStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 12)
)
_WsIPAddress_Type = IpAddress
_WsIPAddress_Object = MibScalar
wsIPAddress = _WsIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 12, 1),
    _WsIPAddress_Type()
)
wsIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsIPAddress.setStatus("current")


class _WsOperationalStatus_Type(Integer32):
    """Custom type wsOperationalStatus based on Integer32"""
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
        *(("enabled", 1),
          ("enable-pending", 2),
          ("disabled", 3),
          ("disable-pending", 4))
    )


_WsOperationalStatus_Type.__name__ = "Integer32"
_WsOperationalStatus_Object = MibScalar
wsOperationalStatus = _WsOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 12, 2),
    _WsOperationalStatus_Type()
)
wsOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsOperationalStatus.setStatus("current")


class _WsOperationalStatusDisableReason_Type(Integer32):
    """Custom type wsOperationalStatusDisableReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("admin-disabled", 2),
          ("no-ipAddress", 3),
          ("no-sslFiles", 4),
          ("no-loopback-interface", 5),
          ("routing-disabled", 6),
          ("no-active-interface", 7))
    )


_WsOperationalStatusDisableReason_Type.__name__ = "Integer32"
_WsOperationalStatusDisableReason_Object = MibScalar
wsOperationalStatusDisableReason = _WsOperationalStatusDisableReason_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 12, 3),
    _WsOperationalStatusDisableReason_Type()
)
wsOperationalStatusDisableReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsOperationalStatusDisableReason.setStatus("current")


class _WsTotalPeerSwitches_Type(Integer32):
    """Custom type wsTotalPeerSwitches based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_WsTotalPeerSwitches_Type.__name__ = "Integer32"
_WsTotalPeerSwitches_Object = MibScalar
wsTotalPeerSwitches = _WsTotalPeerSwitches_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 12, 4),
    _WsTotalPeerSwitches_Type()
)
wsTotalPeerSwitches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsTotalPeerSwitches.setStatus("current")
_WsTotalAPs_Type = Unsigned32
_WsTotalAPs_Object = MibScalar
wsTotalAPs = _WsTotalAPs_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 12, 5),
    _WsTotalAPs_Type()
)
wsTotalAPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsTotalAPs.setStatus("current")


class _WsTotalManagedAPs_Type(Integer32):
    """Custom type wsTotalManagedAPs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48),
    )


_WsTotalManagedAPs_Type.__name__ = "Integer32"
_WsTotalManagedAPs_Object = MibScalar
wsTotalManagedAPs = _WsTotalManagedAPs_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 12, 6),
    _WsTotalManagedAPs_Type()
)
wsTotalManagedAPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsTotalManagedAPs.setStatus("current")
_WsTotalStandaloneAPs_Type = Unsigned32
_WsTotalStandaloneAPs_Object = MibScalar
wsTotalStandaloneAPs = _WsTotalStandaloneAPs_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 12, 7),
    _WsTotalStandaloneAPs_Type()
)
wsTotalStandaloneAPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsTotalStandaloneAPs.setStatus("current")
_WsTotalDiscoveredAPs_Type = Unsigned32
_WsTotalDiscoveredAPs_Object = MibScalar
wsTotalDiscoveredAPs = _WsTotalDiscoveredAPs_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 12, 8),
    _WsTotalDiscoveredAPs_Type()
)
wsTotalDiscoveredAPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsTotalDiscoveredAPs.setStatus("current")
_WsTotalConnectionFailedAPs_Type = Unsigned32
_WsTotalConnectionFailedAPs_Object = MibScalar
wsTotalConnectionFailedAPs = _WsTotalConnectionFailedAPs_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 12, 9),
    _WsTotalConnectionFailedAPs_Type()
)
wsTotalConnectionFailedAPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsTotalConnectionFailedAPs.setStatus("current")
_WsTotalRogueAPs_Type = Unsigned32
_WsTotalRogueAPs_Object = MibScalar
wsTotalRogueAPs = _WsTotalRogueAPs_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 12, 10),
    _WsTotalRogueAPs_Type()
)
wsTotalRogueAPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsTotalRogueAPs.setStatus("current")
_WsTotalUnknownAPs_Type = Unsigned32
_WsTotalUnknownAPs_Object = MibScalar
wsTotalUnknownAPs = _WsTotalUnknownAPs_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 12, 11),
    _WsTotalUnknownAPs_Type()
)
wsTotalUnknownAPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsTotalUnknownAPs.setStatus("current")
_WsMaximumManagedAPsInPeerGroup_Type = Unsigned32
_WsMaximumManagedAPsInPeerGroup_Object = MibScalar
wsMaximumManagedAPsInPeerGroup = _WsMaximumManagedAPsInPeerGroup_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 12, 12),
    _WsMaximumManagedAPsInPeerGroup_Type()
)
wsMaximumManagedAPsInPeerGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMaximumManagedAPsInPeerGroup.setStatus("current")
_WsTotalClients_Type = Unsigned32
_WsTotalClients_Object = MibScalar
wsTotalClients = _WsTotalClients_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 12, 13),
    _WsTotalClients_Type()
)
wsTotalClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsTotalClients.setStatus("current")
_WsTotalAuthenticatedClients_Type = Unsigned32
_WsTotalAuthenticatedClients_Object = MibScalar
wsTotalAuthenticatedClients = _WsTotalAuthenticatedClients_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 12, 14),
    _WsTotalAuthenticatedClients_Type()
)
wsTotalAuthenticatedClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsTotalAuthenticatedClients.setStatus("current")
_WsMaximumAssociatedClients_Type = Unsigned32
_WsMaximumAssociatedClients_Object = MibScalar
wsMaximumAssociatedClients = _WsMaximumAssociatedClients_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 12, 15),
    _WsMaximumAssociatedClients_Type()
)
wsMaximumAssociatedClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMaximumAssociatedClients.setStatus("current")


class _WsWLANUtilization_Type(Integer32):
    """Custom type wsWLANUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_WsWLANUtilization_Type.__name__ = "Integer32"
_WsWLANUtilization_Object = MibScalar
wsWLANUtilization = _WsWLANUtilization_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 12, 16),
    _WsWLANUtilization_Type()
)
wsWLANUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsWLANUtilization.setStatus("current")


class _WsGlobalStatusRegulatoryDomainFor2GHz_Type(DisplayString):
    """Custom type wsGlobalStatusRegulatoryDomainFor2GHz based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 32),
    )


_WsGlobalStatusRegulatoryDomainFor2GHz_Type.__name__ = "DisplayString"
_WsGlobalStatusRegulatoryDomainFor2GHz_Object = MibScalar
wsGlobalStatusRegulatoryDomainFor2GHz = _WsGlobalStatusRegulatoryDomainFor2GHz_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 12, 18),
    _WsGlobalStatusRegulatoryDomainFor2GHz_Type()
)
wsGlobalStatusRegulatoryDomainFor2GHz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsGlobalStatusRegulatoryDomainFor2GHz.setStatus("current")


class _WsGlobalStatusRegulatoryDomainFor5GHz_Type(DisplayString):
    """Custom type wsGlobalStatusRegulatoryDomainFor5GHz based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 32),
    )


_WsGlobalStatusRegulatoryDomainFor5GHz_Type.__name__ = "DisplayString"
_WsGlobalStatusRegulatoryDomainFor5GHz_Object = MibScalar
wsGlobalStatusRegulatoryDomainFor5GHz = _WsGlobalStatusRegulatoryDomainFor5GHz_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 12, 19),
    _WsGlobalStatusRegulatoryDomainFor5GHz_Type()
)
wsGlobalStatusRegulatoryDomainFor5GHz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsGlobalStatusRegulatoryDomainFor5GHz.setStatus("current")


class _WsGlobalPeerConfigRequestAction_Type(Integer32):
    """Custom type wsGlobalPeerConfigRequestAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("start", 2))
    )


_WsGlobalPeerConfigRequestAction_Type.__name__ = "Integer32"
_WsGlobalPeerConfigRequestAction_Object = MibScalar
wsGlobalPeerConfigRequestAction = _WsGlobalPeerConfigRequestAction_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 12, 20),
    _WsGlobalPeerConfigRequestAction_Type()
)
wsGlobalPeerConfigRequestAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsGlobalPeerConfigRequestAction.setStatus("current")


class _WsGlobalPeerConfigRequestStatus_Type(Integer32):
    """Custom type wsGlobalPeerConfigRequestStatus based on Integer32"""
    defaultValue = 0

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
        *(("notStarted", 0),
          ("requested", 1),
          ("savingConfig", 2),
          ("sendingConfig", 3),
          ("applyingAPprofileConfig", 4),
          ("complete", 5))
    )


_WsGlobalPeerConfigRequestStatus_Type.__name__ = "Integer32"
_WsGlobalPeerConfigRequestStatus_Object = MibScalar
wsGlobalPeerConfigRequestStatus = _WsGlobalPeerConfigRequestStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 12, 21),
    _WsGlobalPeerConfigRequestStatus_Type()
)
wsGlobalPeerConfigRequestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsGlobalPeerConfigRequestStatus.setStatus("current")


class _WsGlobalPeerConfigReceiveStatus_Type(Integer32):
    """Custom type wsGlobalPeerConfigReceiveStatus based on Integer32"""
    defaultValue = 0

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
        *(("notStarted", 0),
          ("receivingConfig", 1),
          ("savingConfig", 2),
          ("applyingAPprofileConfig", 3),
          ("failureInvalidCodeVersion", 4),
          ("failureInvalidHwVersion", 5),
          ("failureInvalidConfig", 6),
          ("failureInvalidPacketFormat", 7),
          ("failureTimeout", 8),
          ("success", 9))
    )


_WsGlobalPeerConfigReceiveStatus_Type.__name__ = "Integer32"
_WsGlobalPeerConfigReceiveStatus_Object = MibScalar
wsGlobalPeerConfigReceiveStatus = _WsGlobalPeerConfigReceiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 12, 22),
    _WsGlobalPeerConfigReceiveStatus_Type()
)
wsGlobalPeerConfigReceiveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsGlobalPeerConfigReceiveStatus.setStatus("current")
_WsGlobalPeerConfigSwitchIp_Type = IpAddress
_WsGlobalPeerConfigSwitchIp_Object = MibScalar
wsGlobalPeerConfigSwitchIp = _WsGlobalPeerConfigSwitchIp_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 12, 23),
    _WsGlobalPeerConfigSwitchIp_Type()
)
wsGlobalPeerConfigSwitchIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsGlobalPeerConfigSwitchIp.setStatus("current")


class _WsGlobalPeerConfigReceived_Type(Bits):
    """Custom type wsGlobalPeerConfigReceived based on Bits"""
    namedValues = NamedValues(
        *(("none", 1),
          ("globalConfig", 2),
          ("discoveryConfig", 3),
          ("validAPDatabase", 4),
          ("channelPowerConfig", 5),
          ("profileNetworkConfig", 6),
          ("knownClientConfig", 7),
          ("captivePortalConfig", 8),
          ("radiusClientConfig", 9),
          ("qosAclConfig", 10),
          ("qosDiffServConfig", 11),
          ("wdsGroupConfig", 12),
          ("deviceLocationConfig", 13))
    )

_WsGlobalPeerConfigReceived_Type.__name__ = "Bits"
_WsGlobalPeerConfigReceived_Object = MibScalar
wsGlobalPeerConfigReceived = _WsGlobalPeerConfigReceived_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 12, 24),
    _WsGlobalPeerConfigReceived_Type()
)
wsGlobalPeerConfigReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsGlobalPeerConfigReceived.setStatus("current")
_WsGlobalPeerConfigReceivedTimestamp_Type = DisplayString
_WsGlobalPeerConfigReceivedTimestamp_Object = MibScalar
wsGlobalPeerConfigReceivedTimestamp = _WsGlobalPeerConfigReceivedTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 12, 25),
    _WsGlobalPeerConfigReceivedTimestamp_Type()
)
wsGlobalPeerConfigReceivedTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsGlobalPeerConfigReceivedTimestamp.setStatus("current")


class _WsClusterControllerIndicator_Type(Integer32):
    """Custom type wsClusterControllerIndicator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_WsClusterControllerIndicator_Type.__name__ = "Integer32"
_WsClusterControllerIndicator_Object = MibScalar
wsClusterControllerIndicator = _WsClusterControllerIndicator_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 12, 26),
    _WsClusterControllerIndicator_Type()
)
wsClusterControllerIndicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsClusterControllerIndicator.setStatus("current")
_WsClusterController_Type = IpAddress
_WsClusterController_Object = MibScalar
wsClusterController = _WsClusterController_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 12, 27),
    _WsClusterController_Type()
)
wsClusterController.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsClusterController.setStatus("current")
_WsRogueAPMitigationCount_Type = Unsigned32
_WsRogueAPMitigationCount_Object = MibScalar
wsRogueAPMitigationCount = _WsRogueAPMitigationCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 12, 28),
    _WsRogueAPMitigationCount_Type()
)
wsRogueAPMitigationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRogueAPMitigationCount.setStatus("current")
_WsRogueAPMitigationLimit_Type = Unsigned32
_WsRogueAPMitigationLimit_Object = MibScalar
wsRogueAPMitigationLimit = _WsRogueAPMitigationLimit_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 12, 29),
    _WsRogueAPMitigationLimit_Type()
)
wsRogueAPMitigationLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRogueAPMitigationLimit.setStatus("current")


class _WsRogueAPAcknowledgeAll_Type(Integer32):
    """Custom type wsRogueAPAcknowledgeAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no-action", 0),
          ("acknowledge", 1))
    )


_WsRogueAPAcknowledgeAll_Type.__name__ = "Integer32"
_WsRogueAPAcknowledgeAll_Object = MibScalar
wsRogueAPAcknowledgeAll = _WsRogueAPAcknowledgeAll_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 12, 30),
    _WsRogueAPAcknowledgeAll_Type()
)
wsRogueAPAcknowledgeAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRogueAPAcknowledgeAll.setStatus("current")
_WsTotalDetectedClients_Type = Unsigned32
_WsTotalDetectedClients_Object = MibScalar
wsTotalDetectedClients = _WsTotalDetectedClients_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 12, 31),
    _WsTotalDetectedClients_Type()
)
wsTotalDetectedClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsTotalDetectedClients.setStatus("current")
_WsMaximumDetectedClients_Type = Unsigned32
_WsMaximumDetectedClients_Object = MibScalar
wsMaximumDetectedClients = _WsMaximumDetectedClients_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 12, 32),
    _WsMaximumDetectedClients_Type()
)
wsMaximumDetectedClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMaximumDetectedClients.setStatus("current")
_WsMaximumDetectedClientPreAuthenticationHistoryEntries_Type = Unsigned32
_WsMaximumDetectedClientPreAuthenticationHistoryEntries_Object = MibScalar
wsMaximumDetectedClientPreAuthenticationHistoryEntries = _WsMaximumDetectedClientPreAuthenticationHistoryEntries_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 12, 33),
    _WsMaximumDetectedClientPreAuthenticationHistoryEntries_Type()
)
wsMaximumDetectedClientPreAuthenticationHistoryEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMaximumDetectedClientPreAuthenticationHistoryEntries.setStatus("current")
_WsTotalDetectedClientPreAuthenticationHistoryEntries_Type = Unsigned32
_WsTotalDetectedClientPreAuthenticationHistoryEntries_Object = MibScalar
wsTotalDetectedClientPreAuthenticationHistoryEntries = _WsTotalDetectedClientPreAuthenticationHistoryEntries_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 12, 34),
    _WsTotalDetectedClientPreAuthenticationHistoryEntries_Type()
)
wsTotalDetectedClientPreAuthenticationHistoryEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsTotalDetectedClientPreAuthenticationHistoryEntries.setStatus("current")
_WsMaximumDetectedClientRoamHistoryEntries_Type = Unsigned32
_WsMaximumDetectedClientRoamHistoryEntries_Object = MibScalar
wsMaximumDetectedClientRoamHistoryEntries = _WsMaximumDetectedClientRoamHistoryEntries_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 12, 35),
    _WsMaximumDetectedClientRoamHistoryEntries_Type()
)
wsMaximumDetectedClientRoamHistoryEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMaximumDetectedClientRoamHistoryEntries.setStatus("current")
_WsTotalDetectedClientRoamHistoryEntries_Type = Unsigned32
_WsTotalDetectedClientRoamHistoryEntries_Object = MibScalar
wsTotalDetectedClientRoamHistoryEntries = _WsTotalDetectedClientRoamHistoryEntries_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 12, 36),
    _WsTotalDetectedClientRoamHistoryEntries_Type()
)
wsTotalDetectedClientRoamHistoryEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsTotalDetectedClientRoamHistoryEntries.setStatus("current")


class _WsRegenerateX509CertificateAction_Type(Integer32):
    """Custom type wsRegenerateX509CertificateAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("start", 2))
    )


_WsRegenerateX509CertificateAction_Type.__name__ = "Integer32"
_WsRegenerateX509CertificateAction_Object = MibScalar
wsRegenerateX509CertificateAction = _WsRegenerateX509CertificateAction_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 12, 37),
    _WsRegenerateX509CertificateAction_Type()
)
wsRegenerateX509CertificateAction.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRegenerateX509CertificateAction.setStatus("current")


class _WsRegenerateX509CertificateStatus_Type(Integer32):
    """Custom type wsRegenerateX509CertificateStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not-in-progress", 1),
          ("started", 2),
          ("in-progress", 3))
    )


_WsRegenerateX509CertificateStatus_Type.__name__ = "Integer32"
_WsRegenerateX509CertificateStatus_Object = MibScalar
wsRegenerateX509CertificateStatus = _WsRegenerateX509CertificateStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 12, 38),
    _WsRegenerateX509CertificateStatus_Type()
)
wsRegenerateX509CertificateStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRegenerateX509CertificateStatus.setStatus("current")


class _WsNetworkMutualAuthenticationStatus_Type(Integer32):
    """Custom type wsNetworkMutualAuthenticationStatus based on Integer32"""
    defaultValue = 1

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
        *(("not-started", 1),
          ("exchange-start", 2),
          ("in-progress", 3),
          ("provisioning-in-progress", 4),
          ("exchange-in-progress", 5),
          ("provisioning-complete", 6),
          ("exchange-complete", 7),
          ("complete-without-errors", 8),
          ("complete-with-errors-refer-to-event-log-for-details", 9))
    )


_WsNetworkMutualAuthenticationStatus_Type.__name__ = "Integer32"
_WsNetworkMutualAuthenticationStatus_Object = MibScalar
wsNetworkMutualAuthenticationStatus = _WsNetworkMutualAuthenticationStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 12, 39),
    _WsNetworkMutualAuthenticationStatus_Type()
)
wsNetworkMutualAuthenticationStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsNetworkMutualAuthenticationStatus.setStatus("current")
_WsTotalProvisioningAPs_Type = Unsigned32
_WsTotalProvisioningAPs_Object = MibScalar
wsTotalProvisioningAPs = _WsTotalProvisioningAPs_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 12, 40),
    _WsTotalProvisioningAPs_Type()
)
wsTotalProvisioningAPs.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsTotalProvisioningAPs.setStatus("current")
_WsMaximumProvisioningAPs_Type = Unsigned32
_WsMaximumProvisioningAPs_Object = MibScalar
wsMaximumProvisioningAPs = _WsMaximumProvisioningAPs_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 12, 41),
    _WsMaximumProvisioningAPs_Type()
)
wsMaximumProvisioningAPs.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsMaximumProvisioningAPs.setStatus("current")
_WsGlobalStatistics_ObjectIdentity = ObjectIdentity
wsGlobalStatistics = _WsGlobalStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 13)
)
_WsTotalWLANBytesTransmitted_Type = Counter64
_WsTotalWLANBytesTransmitted_Object = MibScalar
wsTotalWLANBytesTransmitted = _WsTotalWLANBytesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 13, 1),
    _WsTotalWLANBytesTransmitted_Type()
)
wsTotalWLANBytesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsTotalWLANBytesTransmitted.setStatus("current")
_WsTotalWLANBytesRecvd_Type = Counter64
_WsTotalWLANBytesRecvd_Object = MibScalar
wsTotalWLANBytesRecvd = _WsTotalWLANBytesRecvd_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 13, 2),
    _WsTotalWLANBytesRecvd_Type()
)
wsTotalWLANBytesRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsTotalWLANBytesRecvd.setStatus("current")
_WsTotalWLANPktsTransmitted_Type = Counter64
_WsTotalWLANPktsTransmitted_Object = MibScalar
wsTotalWLANPktsTransmitted = _WsTotalWLANPktsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 13, 3),
    _WsTotalWLANPktsTransmitted_Type()
)
wsTotalWLANPktsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsTotalWLANPktsTransmitted.setStatus("current")
_WsTotalWLANPktsRecvd_Type = Counter64
_WsTotalWLANPktsRecvd_Object = MibScalar
wsTotalWLANPktsRecvd = _WsTotalWLANPktsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 13, 4),
    _WsTotalWLANPktsRecvd_Type()
)
wsTotalWLANPktsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsTotalWLANPktsRecvd.setStatus("current")


class _WsAllStatisticsReset_Type(Integer32):
    """Custom type wsAllStatisticsReset based on Integer32"""
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


_WsAllStatisticsReset_Type.__name__ = "Integer32"
_WsAllStatisticsReset_Object = MibScalar
wsAllStatisticsReset = _WsAllStatisticsReset_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 13, 5),
    _WsAllStatisticsReset_Type()
)
wsAllStatisticsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsAllStatisticsReset.setStatus("current")


class _WsAllStatisticsResetStatus_Type(Integer32):
    """Custom type wsAllStatisticsResetStatus based on Integer32"""
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
        *(("not-started", 0),
          ("requested", 1),
          ("in-progress", 2),
          ("success", 3),
          ("partial-success", 4),
          ("failure", 5))
    )


_WsAllStatisticsResetStatus_Type.__name__ = "Integer32"
_WsAllStatisticsResetStatus_Object = MibScalar
wsAllStatisticsResetStatus = _WsAllStatisticsResetStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 13, 6),
    _WsAllStatisticsResetStatus_Type()
)
wsAllStatisticsResetStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAllStatisticsResetStatus.setStatus("current")
_WsTotalWLANBytesTransmitDropped_Type = Counter64
_WsTotalWLANBytesTransmitDropped_Object = MibScalar
wsTotalWLANBytesTransmitDropped = _WsTotalWLANBytesTransmitDropped_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 13, 7),
    _WsTotalWLANBytesTransmitDropped_Type()
)
wsTotalWLANBytesTransmitDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsTotalWLANBytesTransmitDropped.setStatus("current")
_WsTotalWLANBytesRecvDropped_Type = Counter64
_WsTotalWLANBytesRecvDropped_Object = MibScalar
wsTotalWLANBytesRecvDropped = _WsTotalWLANBytesRecvDropped_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 13, 8),
    _WsTotalWLANBytesRecvDropped_Type()
)
wsTotalWLANBytesRecvDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsTotalWLANBytesRecvDropped.setStatus("current")
_WsTotalWLANPktsTransmitDropped_Type = Counter64
_WsTotalWLANPktsTransmitDropped_Object = MibScalar
wsTotalWLANPktsTransmitDropped = _WsTotalWLANPktsTransmitDropped_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 13, 9),
    _WsTotalWLANPktsTransmitDropped_Type()
)
wsTotalWLANPktsTransmitDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsTotalWLANPktsTransmitDropped.setStatus("current")
_WsTotalWLANPktsRecvDropped_Type = Counter64
_WsTotalWLANPktsRecvDropped_Object = MibScalar
wsTotalWLANPktsRecvDropped = _WsTotalWLANPktsRecvDropped_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 13, 10),
    _WsTotalWLANPktsRecvDropped_Type()
)
wsTotalWLANPktsRecvDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsTotalWLANPktsRecvDropped.setStatus("current")
_WsTotalWLANDistTunnelPktsTransmitted_Type = Counter64
_WsTotalWLANDistTunnelPktsTransmitted_Object = MibScalar
wsTotalWLANDistTunnelPktsTransmitted = _WsTotalWLANDistTunnelPktsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 13, 11),
    _WsTotalWLANDistTunnelPktsTransmitted_Type()
)
wsTotalWLANDistTunnelPktsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsTotalWLANDistTunnelPktsTransmitted.setStatus("current")
_WsTotalWLANDistTunnelRoamedClients_Type = Unsigned32
_WsTotalWLANDistTunnelRoamedClients_Object = MibScalar
wsTotalWLANDistTunnelRoamedClients = _WsTotalWLANDistTunnelRoamedClients_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 13, 12),
    _WsTotalWLANDistTunnelRoamedClients_Type()
)
wsTotalWLANDistTunnelRoamedClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsTotalWLANDistTunnelRoamedClients.setStatus("current")
_WsTotalWLANDistTunnelClientDenials_Type = Unsigned32
_WsTotalWLANDistTunnelClientDenials_Object = MibScalar
wsTotalWLANDistTunnelClientDenials = _WsTotalWLANDistTunnelClientDenials_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 13, 13),
    _WsTotalWLANDistTunnelClientDenials_Type()
)
wsTotalWLANDistTunnelClientDenials.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsTotalWLANDistTunnelClientDenials.setStatus("current")
_WsPeerConfiguration_ObjectIdentity = ObjectIdentity
wsPeerConfiguration = _WsPeerConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 14)
)


class _WsPeerConfigurationGlobal_Type(Integer32):
    """Custom type wsPeerConfigurationGlobal based on Integer32"""
    defaultValue = 1

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


_WsPeerConfigurationGlobal_Type.__name__ = "Integer32"
_WsPeerConfigurationGlobal_Object = MibScalar
wsPeerConfigurationGlobal = _WsPeerConfigurationGlobal_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 14, 1),
    _WsPeerConfigurationGlobal_Type()
)
wsPeerConfigurationGlobal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPeerConfigurationGlobal.setStatus("current")


class _WsPeerConfigurationDiscovery_Type(Integer32):
    """Custom type wsPeerConfigurationDiscovery based on Integer32"""
    defaultValue = 2

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


_WsPeerConfigurationDiscovery_Type.__name__ = "Integer32"
_WsPeerConfigurationDiscovery_Object = MibScalar
wsPeerConfigurationDiscovery = _WsPeerConfigurationDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 14, 2),
    _WsPeerConfigurationDiscovery_Type()
)
wsPeerConfigurationDiscovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPeerConfigurationDiscovery.setStatus("current")


class _WsPeerConfigurationAPDatabase_Type(Integer32):
    """Custom type wsPeerConfigurationAPDatabase based on Integer32"""
    defaultValue = 1

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


_WsPeerConfigurationAPDatabase_Type.__name__ = "Integer32"
_WsPeerConfigurationAPDatabase_Object = MibScalar
wsPeerConfigurationAPDatabase = _WsPeerConfigurationAPDatabase_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 14, 3),
    _WsPeerConfigurationAPDatabase_Type()
)
wsPeerConfigurationAPDatabase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPeerConfigurationAPDatabase.setStatus("current")


class _WsPeerConfigurationChannelPower_Type(Integer32):
    """Custom type wsPeerConfigurationChannelPower based on Integer32"""
    defaultValue = 1

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


_WsPeerConfigurationChannelPower_Type.__name__ = "Integer32"
_WsPeerConfigurationChannelPower_Object = MibScalar
wsPeerConfigurationChannelPower = _WsPeerConfigurationChannelPower_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 14, 4),
    _WsPeerConfigurationChannelPower_Type()
)
wsPeerConfigurationChannelPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPeerConfigurationChannelPower.setStatus("current")


class _WsPeerConfigurationAPProfiles_Type(Integer32):
    """Custom type wsPeerConfigurationAPProfiles based on Integer32"""
    defaultValue = 1

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


_WsPeerConfigurationAPProfiles_Type.__name__ = "Integer32"
_WsPeerConfigurationAPProfiles_Object = MibScalar
wsPeerConfigurationAPProfiles = _WsPeerConfigurationAPProfiles_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 14, 5),
    _WsPeerConfigurationAPProfiles_Type()
)
wsPeerConfigurationAPProfiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPeerConfigurationAPProfiles.setStatus("current")


class _WsPeerConfigurationKnownClients_Type(Integer32):
    """Custom type wsPeerConfigurationKnownClients based on Integer32"""
    defaultValue = 1

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


_WsPeerConfigurationKnownClients_Type.__name__ = "Integer32"
_WsPeerConfigurationKnownClients_Object = MibScalar
wsPeerConfigurationKnownClients = _WsPeerConfigurationKnownClients_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 14, 6),
    _WsPeerConfigurationKnownClients_Type()
)
wsPeerConfigurationKnownClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPeerConfigurationKnownClients.setStatus("current")


class _WsPeerConfigurationCaptivePortal_Type(Integer32):
    """Custom type wsPeerConfigurationCaptivePortal based on Integer32"""
    defaultValue = 1

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


_WsPeerConfigurationCaptivePortal_Type.__name__ = "Integer32"
_WsPeerConfigurationCaptivePortal_Object = MibScalar
wsPeerConfigurationCaptivePortal = _WsPeerConfigurationCaptivePortal_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 14, 7),
    _WsPeerConfigurationCaptivePortal_Type()
)
wsPeerConfigurationCaptivePortal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPeerConfigurationCaptivePortal.setStatus("current")


class _WsPeerConfigurationRadiusClient_Type(Integer32):
    """Custom type wsPeerConfigurationRadiusClient based on Integer32"""
    defaultValue = 1

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


_WsPeerConfigurationRadiusClient_Type.__name__ = "Integer32"
_WsPeerConfigurationRadiusClient_Object = MibScalar
wsPeerConfigurationRadiusClient = _WsPeerConfigurationRadiusClient_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 14, 8),
    _WsPeerConfigurationRadiusClient_Type()
)
wsPeerConfigurationRadiusClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPeerConfigurationRadiusClient.setStatus("current")


class _WsPeerConfigurationQosAcl_Type(Integer32):
    """Custom type wsPeerConfigurationQosAcl based on Integer32"""
    defaultValue = 1

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


_WsPeerConfigurationQosAcl_Type.__name__ = "Integer32"
_WsPeerConfigurationQosAcl_Object = MibScalar
wsPeerConfigurationQosAcl = _WsPeerConfigurationQosAcl_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 14, 9),
    _WsPeerConfigurationQosAcl_Type()
)
wsPeerConfigurationQosAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPeerConfigurationQosAcl.setStatus("current")


class _WsPeerConfigurationQosDiffServ_Type(Integer32):
    """Custom type wsPeerConfigurationQosDiffServ based on Integer32"""
    defaultValue = 1

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


_WsPeerConfigurationQosDiffServ_Type.__name__ = "Integer32"
_WsPeerConfigurationQosDiffServ_Object = MibScalar
wsPeerConfigurationQosDiffServ = _WsPeerConfigurationQosDiffServ_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 14, 10),
    _WsPeerConfigurationQosDiffServ_Type()
)
wsPeerConfigurationQosDiffServ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPeerConfigurationQosDiffServ.setStatus("current")


class _WsPeerConfigurationWdsGroup_Type(Integer32):
    """Custom type wsPeerConfigurationWdsGroup based on Integer32"""
    defaultValue = 1

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


_WsPeerConfigurationWdsGroup_Type.__name__ = "Integer32"
_WsPeerConfigurationWdsGroup_Object = MibScalar
wsPeerConfigurationWdsGroup = _WsPeerConfigurationWdsGroup_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 14, 11),
    _WsPeerConfigurationWdsGroup_Type()
)
wsPeerConfigurationWdsGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPeerConfigurationWdsGroup.setStatus("current")


class _WsPeerConfigurationDeviceLocation_Type(Integer32):
    """Custom type wsPeerConfigurationDeviceLocation based on Integer32"""
    defaultValue = 1

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


_WsPeerConfigurationDeviceLocation_Type.__name__ = "Integer32"
_WsPeerConfigurationDeviceLocation_Object = MibScalar
wsPeerConfigurationDeviceLocation = _WsPeerConfigurationDeviceLocation_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 14, 12),
    _WsPeerConfigurationDeviceLocation_Type()
)
wsPeerConfigurationDeviceLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPeerConfigurationDeviceLocation.setStatus("current")


class _WsClusterPriority_Type(Unsigned32):
    """Custom type wsClusterPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WsClusterPriority_Type.__name__ = "Unsigned32"
_WsClusterPriority_Object = MibScalar
wsClusterPriority = _WsClusterPriority_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 16),
    _WsClusterPriority_Type()
)
wsClusterPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsClusterPriority.setStatus("current")


class _WsAPClientQosMode_Type(Integer32):
    """Custom type wsAPClientQosMode based on Integer32"""
    defaultValue = 2

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


_WsAPClientQosMode_Type.__name__ = "Integer32"
_WsAPClientQosMode_Object = MibScalar
wsAPClientQosMode = _WsAPClientQosMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 17),
    _WsAPClientQosMode_Type()
)
wsAPClientQosMode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAPClientQosMode.setStatus("current")


class _WsAPAutoUpgradeMode_Type(Integer32):
    """Custom type wsAPAutoUpgradeMode based on Integer32"""
    defaultValue = 2

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


_WsAPAutoUpgradeMode_Type.__name__ = "Integer32"
_WsAPAutoUpgradeMode_Object = MibScalar
wsAPAutoUpgradeMode = _WsAPAutoUpgradeMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 18),
    _WsAPAutoUpgradeMode_Type()
)
wsAPAutoUpgradeMode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAPAutoUpgradeMode.setStatus("current")


class _WsDistTunnelIdleTimeout_Type(Unsigned32):
    """Custom type wsDistTunnelIdleTimeout based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 3600),
    )


_WsDistTunnelIdleTimeout_Type.__name__ = "Unsigned32"
_WsDistTunnelIdleTimeout_Object = MibScalar
wsDistTunnelIdleTimeout = _WsDistTunnelIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 19),
    _WsDistTunnelIdleTimeout_Type()
)
wsDistTunnelIdleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDistTunnelIdleTimeout.setStatus("current")


class _WsDistTunnelMaxTimeout_Type(Unsigned32):
    """Custom type wsDistTunnelMaxTimeout based on Unsigned32"""
    defaultValue = 7200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 86400),
    )


_WsDistTunnelMaxTimeout_Type.__name__ = "Unsigned32"
_WsDistTunnelMaxTimeout_Object = MibScalar
wsDistTunnelMaxTimeout = _WsDistTunnelMaxTimeout_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 20),
    _WsDistTunnelMaxTimeout_Type()
)
wsDistTunnelMaxTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDistTunnelMaxTimeout.setStatus("current")


class _WsDistTunnelMaxMcastRepl_Type(Unsigned32):
    """Custom type wsDistTunnelMaxMcastRepl based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_WsDistTunnelMaxMcastRepl_Type.__name__ = "Unsigned32"
_WsDistTunnelMaxMcastRepl_Object = MibScalar
wsDistTunnelMaxMcastRepl = _WsDistTunnelMaxMcastRepl_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 21),
    _WsDistTunnelMaxMcastRepl_Type()
)
wsDistTunnelMaxMcastRepl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDistTunnelMaxMcastRepl.setStatus("current")


class _WsDistTunnelMaxClients_Type(Unsigned32):
    """Custom type wsDistTunnelMaxClients based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8000),
    )


_WsDistTunnelMaxClients_Type.__name__ = "Unsigned32"
_WsDistTunnelMaxClients_Object = MibScalar
wsDistTunnelMaxClients = _WsDistTunnelMaxClients_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 22),
    _WsDistTunnelMaxClients_Type()
)
wsDistTunnelMaxClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDistTunnelMaxClients.setStatus("current")


class _WsMACAuthenticationMode_Type(Integer32):
    """Custom type wsMACAuthenticationMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("whitelist", 1),
          ("blacklist", 2))
    )


_WsMACAuthenticationMode_Type.__name__ = "Integer32"
_WsMACAuthenticationMode_Object = MibScalar
wsMACAuthenticationMode = _WsMACAuthenticationMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 23),
    _WsMACAuthenticationMode_Type()
)
wsMACAuthenticationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMACAuthenticationMode.setStatus("current")
_WsKnownClientTable_Object = MibTable
wsKnownClientTable = _WsKnownClientTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 24)
)
if mibBuilder.loadTexts:
    wsKnownClientTable.setStatus("current")
_WsKnownClientEntry_Object = MibTableRow
wsKnownClientEntry = _WsKnownClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 24, 1)
)
wsKnownClientEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsKnownClientMacAddress"),
)
if mibBuilder.loadTexts:
    wsKnownClientEntry.setStatus("current")
_WsKnownClientMacAddress_Type = MacAddress
_WsKnownClientMacAddress_Object = MibTableColumn
wsKnownClientMacAddress = _WsKnownClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 24, 1, 1),
    _WsKnownClientMacAddress_Type()
)
wsKnownClientMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsKnownClientMacAddress.setStatus("current")


class _WsKnownClientAuthAction_Type(Integer32):
    """Custom type wsKnownClientAuthAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("global", 1),
          ("grant", 2),
          ("deny", 3))
    )


_WsKnownClientAuthAction_Type.__name__ = "Integer32"
_WsKnownClientAuthAction_Object = MibTableColumn
wsKnownClientAuthAction = _WsKnownClientAuthAction_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 24, 1, 2),
    _WsKnownClientAuthAction_Type()
)
wsKnownClientAuthAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsKnownClientAuthAction.setStatus("current")


class _WsKnownClientName_Type(DisplayString):
    """Custom type wsKnownClientName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WsKnownClientName_Type.__name__ = "DisplayString"
_WsKnownClientName_Object = MibTableColumn
wsKnownClientName = _WsKnownClientName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 24, 1, 3),
    _WsKnownClientName_Type()
)
wsKnownClientName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsKnownClientName.setStatus("current")
_WsKnownClientRowStatus_Type = RowStatus
_WsKnownClientRowStatus_Object = MibTableColumn
wsKnownClientRowStatus = _WsKnownClientRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 24, 1, 4),
    _WsKnownClientRowStatus_Type()
)
wsKnownClientRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsKnownClientRowStatus.setStatus("current")
_WsWidsSecurity_ObjectIdentity = ObjectIdentity
wsWidsSecurity = _WsWidsSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 25)
)
_WsWidsApSecurity_ObjectIdentity = ObjectIdentity
wsWidsApSecurity = _WsWidsApSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 25, 1)
)


class _RogueAdminConfig_Type(Integer32):
    """Custom type rogueAdminConfig based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("enable", 1)
    )


_RogueAdminConfig_Type.__name__ = "Integer32"
_RogueAdminConfig_Object = MibScalar
rogueAdminConfig = _RogueAdminConfig_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 25, 1, 1),
    _RogueAdminConfig_Type()
)
rogueAdminConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rogueAdminConfig.setStatus("current")


class _RogueUnknownApManagedSsid_Type(Integer32):
    """Custom type rogueUnknownApManagedSsid based on Integer32"""
    defaultValue = 1

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


_RogueUnknownApManagedSsid_Type.__name__ = "Integer32"
_RogueUnknownApManagedSsid_Object = MibScalar
rogueUnknownApManagedSsid = _RogueUnknownApManagedSsid_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 25, 1, 2),
    _RogueUnknownApManagedSsid_Type()
)
rogueUnknownApManagedSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rogueUnknownApManagedSsid.setStatus("current")


class _RogueFakeManagedApManagedSsid_Type(Integer32):
    """Custom type rogueFakeManagedApManagedSsid based on Integer32"""
    defaultValue = 1

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


_RogueFakeManagedApManagedSsid_Type.__name__ = "Integer32"
_RogueFakeManagedApManagedSsid_Object = MibScalar
rogueFakeManagedApManagedSsid = _RogueFakeManagedApManagedSsid_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 25, 1, 3),
    _RogueFakeManagedApManagedSsid_Type()
)
rogueFakeManagedApManagedSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rogueFakeManagedApManagedSsid.setStatus("current")


class _RogueManagedApNoSsid_Type(Integer32):
    """Custom type rogueManagedApNoSsid based on Integer32"""
    defaultValue = 1

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


_RogueManagedApNoSsid_Type.__name__ = "Integer32"
_RogueManagedApNoSsid_Object = MibScalar
rogueManagedApNoSsid = _RogueManagedApNoSsid_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 25, 1, 4),
    _RogueManagedApNoSsid_Type()
)
rogueManagedApNoSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rogueManagedApNoSsid.setStatus("current")


class _RogueManagedApInvalidChannel_Type(Integer32):
    """Custom type rogueManagedApInvalidChannel based on Integer32"""
    defaultValue = 1

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


_RogueManagedApInvalidChannel_Type.__name__ = "Integer32"
_RogueManagedApInvalidChannel_Object = MibScalar
rogueManagedApInvalidChannel = _RogueManagedApInvalidChannel_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 25, 1, 5),
    _RogueManagedApInvalidChannel_Type()
)
rogueManagedApInvalidChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rogueManagedApInvalidChannel.setStatus("current")


class _RogueManagedSsidInvalidSecurity_Type(Integer32):
    """Custom type rogueManagedSsidInvalidSecurity based on Integer32"""
    defaultValue = 1

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


_RogueManagedSsidInvalidSecurity_Type.__name__ = "Integer32"
_RogueManagedSsidInvalidSecurity_Object = MibScalar
rogueManagedSsidInvalidSecurity = _RogueManagedSsidInvalidSecurity_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 25, 1, 6),
    _RogueManagedSsidInvalidSecurity_Type()
)
rogueManagedSsidInvalidSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rogueManagedSsidInvalidSecurity.setStatus("current")


class _RogueManagedApInvalidSsid_Type(Integer32):
    """Custom type rogueManagedApInvalidSsid based on Integer32"""
    defaultValue = 1

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


_RogueManagedApInvalidSsid_Type.__name__ = "Integer32"
_RogueManagedApInvalidSsid_Object = MibScalar
rogueManagedApInvalidSsid = _RogueManagedApInvalidSsid_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 25, 1, 7),
    _RogueManagedApInvalidSsid_Type()
)
rogueManagedApInvalidSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rogueManagedApInvalidSsid.setStatus("current")


class _RogueApIllegalChannel_Type(Integer32):
    """Custom type rogueApIllegalChannel based on Integer32"""
    defaultValue = 1

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


_RogueApIllegalChannel_Type.__name__ = "Integer32"
_RogueApIllegalChannel_Object = MibScalar
rogueApIllegalChannel = _RogueApIllegalChannel_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 25, 1, 8),
    _RogueApIllegalChannel_Type()
)
rogueApIllegalChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rogueApIllegalChannel.setStatus("current")


class _RogueStandaloneApInvalidConfig_Type(Integer32):
    """Custom type rogueStandaloneApInvalidConfig based on Integer32"""
    defaultValue = 1

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


_RogueStandaloneApInvalidConfig_Type.__name__ = "Integer32"
_RogueStandaloneApInvalidConfig_Object = MibScalar
rogueStandaloneApInvalidConfig = _RogueStandaloneApInvalidConfig_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 25, 1, 9),
    _RogueStandaloneApInvalidConfig_Type()
)
rogueStandaloneApInvalidConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rogueStandaloneApInvalidConfig.setStatus("current")


class _RogueUnexpectedWdsDevice_Type(Integer32):
    """Custom type rogueUnexpectedWdsDevice based on Integer32"""
    defaultValue = 1

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


_RogueUnexpectedWdsDevice_Type.__name__ = "Integer32"
_RogueUnexpectedWdsDevice_Object = MibScalar
rogueUnexpectedWdsDevice = _RogueUnexpectedWdsDevice_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 25, 1, 10),
    _RogueUnexpectedWdsDevice_Type()
)
rogueUnexpectedWdsDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rogueUnexpectedWdsDevice.setStatus("current")


class _RogueUnmanagedApWiredNetwork_Type(Integer32):
    """Custom type rogueUnmanagedApWiredNetwork based on Integer32"""
    defaultValue = 1

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


_RogueUnmanagedApWiredNetwork_Type.__name__ = "Integer32"
_RogueUnmanagedApWiredNetwork_Object = MibScalar
rogueUnmanagedApWiredNetwork = _RogueUnmanagedApWiredNetwork_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 25, 1, 11),
    _RogueUnmanagedApWiredNetwork_Type()
)
rogueUnmanagedApWiredNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rogueUnmanagedApWiredNetwork.setStatus("current")


class _WiredNetworkDetectionInterval_Type(Integer32):
    """Custom type wiredNetworkDetectionInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_WiredNetworkDetectionInterval_Type.__name__ = "Integer32"
_WiredNetworkDetectionInterval_Object = MibScalar
wiredNetworkDetectionInterval = _WiredNetworkDetectionInterval_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 25, 1, 12),
    _WiredNetworkDetectionInterval_Type()
)
wiredNetworkDetectionInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wiredNetworkDetectionInterval.setStatus("current")


class _RogueDetectedTrapInterval_Type(Integer32):
    """Custom type rogueDetectedTrapInterval based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 3600),
    )


_RogueDetectedTrapInterval_Type.__name__ = "Integer32"
_RogueDetectedTrapInterval_Object = MibScalar
rogueDetectedTrapInterval = _RogueDetectedTrapInterval_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 25, 1, 13),
    _RogueDetectedTrapInterval_Type()
)
rogueDetectedTrapInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rogueDetectedTrapInterval.setStatus("current")


class _ApDeauthenticationAttack_Type(Integer32):
    """Custom type apDeauthenticationAttack based on Integer32"""
    defaultValue = 2

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


_ApDeauthenticationAttack_Type.__name__ = "Integer32"
_ApDeauthenticationAttack_Object = MibScalar
apDeauthenticationAttack = _ApDeauthenticationAttack_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 25, 1, 14),
    _ApDeauthenticationAttack_Type()
)
apDeauthenticationAttack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDeauthenticationAttack.setStatus("current")
_WsWidsClientSecurity_ObjectIdentity = ObjectIdentity
wsWidsClientSecurity = _WsWidsClientSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 25, 2)
)


class _RogueDetectedTrapIntvl_Type(Integer32):
    """Custom type rogueDetectedTrapIntvl based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 3600),
    )


_RogueDetectedTrapIntvl_Type.__name__ = "Integer32"
_RogueDetectedTrapIntvl_Object = MibScalar
rogueDetectedTrapIntvl = _RogueDetectedTrapIntvl_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 25, 2, 1),
    _RogueDetectedTrapIntvl_Type()
)
rogueDetectedTrapIntvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rogueDetectedTrapIntvl.setStatus("current")


class _KnownClientDatabaseTest_Type(Integer32):
    """Custom type knownClientDatabaseTest based on Integer32"""
    defaultValue = 2

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


_KnownClientDatabaseTest_Type.__name__ = "Integer32"
_KnownClientDatabaseTest_Object = MibScalar
knownClientDatabaseTest = _KnownClientDatabaseTest_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 25, 2, 2),
    _KnownClientDatabaseTest_Type()
)
knownClientDatabaseTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    knownClientDatabaseTest.setStatus("current")


class _AuthReqTransmitRate_Type(Integer32):
    """Custom type authReqTransmitRate based on Integer32"""
    defaultValue = 1

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


_AuthReqTransmitRate_Type.__name__ = "Integer32"
_AuthReqTransmitRate_Object = MibScalar
authReqTransmitRate = _AuthReqTransmitRate_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 25, 2, 3),
    _AuthReqTransmitRate_Type()
)
authReqTransmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authReqTransmitRate.setStatus("current")


class _ProbeReqTransmitRate_Type(Integer32):
    """Custom type probeReqTransmitRate based on Integer32"""
    defaultValue = 1

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


_ProbeReqTransmitRate_Type.__name__ = "Integer32"
_ProbeReqTransmitRate_Object = MibScalar
probeReqTransmitRate = _ProbeReqTransmitRate_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 25, 2, 4),
    _ProbeReqTransmitRate_Type()
)
probeReqTransmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    probeReqTransmitRate.setStatus("current")


class _DeauthReqTransmitRate_Type(Integer32):
    """Custom type deauthReqTransmitRate based on Integer32"""
    defaultValue = 1

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


_DeauthReqTransmitRate_Type.__name__ = "Integer32"
_DeauthReqTransmitRate_Object = MibScalar
deauthReqTransmitRate = _DeauthReqTransmitRate_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 25, 2, 5),
    _DeauthReqTransmitRate_Type()
)
deauthReqTransmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deauthReqTransmitRate.setStatus("current")


class _MaxFailingAuthentication_Type(Integer32):
    """Custom type maxFailingAuthentication based on Integer32"""
    defaultValue = 1

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


_MaxFailingAuthentication_Type.__name__ = "Integer32"
_MaxFailingAuthentication_Object = MibScalar
maxFailingAuthentication = _MaxFailingAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 25, 2, 6),
    _MaxFailingAuthentication_Type()
)
maxFailingAuthentication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxFailingAuthentication.setStatus("current")


class _AuthWithUnknownAP_Type(Integer32):
    """Custom type authWithUnknownAP based on Integer32"""
    defaultValue = 2

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


_AuthWithUnknownAP_Type.__name__ = "Integer32"
_AuthWithUnknownAP_Object = MibScalar
authWithUnknownAP = _AuthWithUnknownAP_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 25, 2, 7),
    _AuthWithUnknownAP_Type()
)
authWithUnknownAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authWithUnknownAP.setStatus("current")


class _ClientThreatMitigation_Type(Integer32):
    """Custom type clientThreatMitigation based on Integer32"""
    defaultValue = 2

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


_ClientThreatMitigation_Type.__name__ = "Integer32"
_ClientThreatMitigation_Object = MibScalar
clientThreatMitigation = _ClientThreatMitigation_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 25, 2, 8),
    _ClientThreatMitigation_Type()
)
clientThreatMitigation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientThreatMitigation.setStatus("current")


class _DeauthThresholdInterval_Type(Integer32):
    """Custom type deauthThresholdInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_DeauthThresholdInterval_Type.__name__ = "Integer32"
_DeauthThresholdInterval_Object = MibScalar
deauthThresholdInterval = _DeauthThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 25, 2, 9),
    _DeauthThresholdInterval_Type()
)
deauthThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deauthThresholdInterval.setStatus("current")


class _DeauthThresholdValue_Type(Integer32):
    """Custom type deauthThresholdValue based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99999),
    )


_DeauthThresholdValue_Type.__name__ = "Integer32"
_DeauthThresholdValue_Object = MibScalar
deauthThresholdValue = _DeauthThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 25, 2, 10),
    _DeauthThresholdValue_Type()
)
deauthThresholdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deauthThresholdValue.setStatus("current")


class _AuthThresholdInterval_Type(Integer32):
    """Custom type authThresholdInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_AuthThresholdInterval_Type.__name__ = "Integer32"
_AuthThresholdInterval_Object = MibScalar
authThresholdInterval = _AuthThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 25, 2, 11),
    _AuthThresholdInterval_Type()
)
authThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authThresholdInterval.setStatus("current")


class _AuthThresholdValue_Type(Integer32):
    """Custom type authThresholdValue based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99999),
    )


_AuthThresholdValue_Type.__name__ = "Integer32"
_AuthThresholdValue_Object = MibScalar
authThresholdValue = _AuthThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 25, 2, 12),
    _AuthThresholdValue_Type()
)
authThresholdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authThresholdValue.setStatus("current")


class _ProbeThresholdInterval_Type(Integer32):
    """Custom type probeThresholdInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_ProbeThresholdInterval_Type.__name__ = "Integer32"
_ProbeThresholdInterval_Object = MibScalar
probeThresholdInterval = _ProbeThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 25, 2, 13),
    _ProbeThresholdInterval_Type()
)
probeThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    probeThresholdInterval.setStatus("current")


class _ProbeThresholdValue_Type(Integer32):
    """Custom type probeThresholdValue based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99999),
    )


_ProbeThresholdValue_Type.__name__ = "Integer32"
_ProbeThresholdValue_Object = MibScalar
probeThresholdValue = _ProbeThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 25, 2, 14),
    _ProbeThresholdValue_Type()
)
probeThresholdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    probeThresholdValue.setStatus("current")


class _AuthFailureThreshold_Type(Integer32):
    """Custom type authFailureThreshold based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99999),
    )


_AuthFailureThreshold_Type.__name__ = "Integer32"
_AuthFailureThreshold_Object = MibScalar
authFailureThreshold = _AuthFailureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 25, 2, 15),
    _AuthFailureThreshold_Type()
)
authFailureThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authFailureThreshold.setStatus("current")


class _KnownClientDatabaseLocation_Type(Integer32):
    """Custom type knownClientDatabaseLocation based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("radius", 2))
    )


_KnownClientDatabaseLocation_Type.__name__ = "Integer32"
_KnownClientDatabaseLocation_Object = MibScalar
knownClientDatabaseLocation = _KnownClientDatabaseLocation_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 25, 2, 16),
    _KnownClientDatabaseLocation_Type()
)
knownClientDatabaseLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    knownClientDatabaseLocation.setStatus("current")


class _KnownClientDatabaseRadiusServerName_Type(DisplayString):
    """Custom type knownClientDatabaseRadiusServerName based on DisplayString"""
    defaultValue = OctetString("Default-RADIUS-Server")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_KnownClientDatabaseRadiusServerName_Type.__name__ = "DisplayString"
_KnownClientDatabaseRadiusServerName_Object = MibScalar
knownClientDatabaseRadiusServerName = _KnownClientDatabaseRadiusServerName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 25, 2, 17),
    _KnownClientDatabaseRadiusServerName_Type()
)
knownClientDatabaseRadiusServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    knownClientDatabaseRadiusServerName.setStatus("current")


class _KnownClientDatabaseRadiusServerStatus_Type(Integer32):
    """Custom type knownClientDatabaseRadiusServerStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-configured", 1),
          ("configured", 2))
    )


_KnownClientDatabaseRadiusServerStatus_Type.__name__ = "Integer32"
_KnownClientDatabaseRadiusServerStatus_Object = MibScalar
knownClientDatabaseRadiusServerStatus = _KnownClientDatabaseRadiusServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 25, 2, 18),
    _KnownClientDatabaseRadiusServerStatus_Type()
)
knownClientDatabaseRadiusServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    knownClientDatabaseRadiusServerStatus.setStatus("current")


class _NotInOUIDatabase_Type(Integer32):
    """Custom type notInOUIDatabase based on Integer32"""
    defaultValue = 2

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


_NotInOUIDatabase_Type.__name__ = "Integer32"
_NotInOUIDatabase_Object = MibScalar
notInOUIDatabase = _NotInOUIDatabase_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 25, 2, 19),
    _NotInOUIDatabase_Type()
)
notInOUIDatabase.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    notInOUIDatabase.setStatus("current")
_WsGlobalRadiusConfiguration_ObjectIdentity = ObjectIdentity
wsGlobalRadiusConfiguration = _WsGlobalRadiusConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 26)
)
_WsRadiusConfiguration_ObjectIdentity = ObjectIdentity
wsRadiusConfiguration = _WsRadiusConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 26, 1)
)


class _WsAuthRadiusServerName_Type(DisplayString):
    """Custom type wsAuthRadiusServerName based on DisplayString"""
    defaultValue = OctetString("Default-RADIUS-Server")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WsAuthRadiusServerName_Type.__name__ = "DisplayString"
_WsAuthRadiusServerName_Object = MibScalar
wsAuthRadiusServerName = _WsAuthRadiusServerName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 26, 1, 1),
    _WsAuthRadiusServerName_Type()
)
wsAuthRadiusServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAuthRadiusServerName.setStatus("current")


class _WsAuthRadiusServerConfiguredStatus_Type(Integer32):
    """Custom type wsAuthRadiusServerConfiguredStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-configured", 1),
          ("configured", 2))
    )


_WsAuthRadiusServerConfiguredStatus_Type.__name__ = "Integer32"
_WsAuthRadiusServerConfiguredStatus_Object = MibScalar
wsAuthRadiusServerConfiguredStatus = _WsAuthRadiusServerConfiguredStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 26, 1, 2),
    _WsAuthRadiusServerConfiguredStatus_Type()
)
wsAuthRadiusServerConfiguredStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAuthRadiusServerConfiguredStatus.setStatus("current")


class _WsAcctRadiusServerName_Type(DisplayString):
    """Custom type wsAcctRadiusServerName based on DisplayString"""
    defaultValue = OctetString("Default-RADIUS-Server")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WsAcctRadiusServerName_Type.__name__ = "DisplayString"
_WsAcctRadiusServerName_Object = MibScalar
wsAcctRadiusServerName = _WsAcctRadiusServerName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 26, 1, 3),
    _WsAcctRadiusServerName_Type()
)
wsAcctRadiusServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAcctRadiusServerName.setStatus("current")


class _WsAcctRadiusServerConfiguredStatus_Type(Integer32):
    """Custom type wsAcctRadiusServerConfiguredStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-configured", 1),
          ("configured", 2))
    )


_WsAcctRadiusServerConfiguredStatus_Type.__name__ = "Integer32"
_WsAcctRadiusServerConfiguredStatus_Object = MibScalar
wsAcctRadiusServerConfiguredStatus = _WsAcctRadiusServerConfiguredStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 26, 1, 4),
    _WsAcctRadiusServerConfiguredStatus_Type()
)
wsAcctRadiusServerConfiguredStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAcctRadiusServerConfiguredStatus.setStatus("current")


class _WsRadiusAcctMode_Type(Integer32):
    """Custom type wsRadiusAcctMode based on Integer32"""
    defaultValue = 2

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


_WsRadiusAcctMode_Type.__name__ = "Integer32"
_WsRadiusAcctMode_Object = MibScalar
wsRadiusAcctMode = _WsRadiusAcctMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 26, 1, 5),
    _WsRadiusAcctMode_Type()
)
wsRadiusAcctMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRadiusAcctMode.setStatus("current")
_WsSwitchStatusTable_Object = MibTable
wsSwitchStatusTable = _WsSwitchStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 27)
)
if mibBuilder.loadTexts:
    wsSwitchStatusTable.setStatus("current")
_WsSwitchStatusEntry_Object = MibTableRow
wsSwitchStatusEntry = _WsSwitchStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 27, 1)
)
wsSwitchStatusEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsSwitchIPAddress"),
)
if mibBuilder.loadTexts:
    wsSwitchStatusEntry.setStatus("current")
_WsSwitchIPAddress_Type = IpAddress
_WsSwitchIPAddress_Object = MibTableColumn
wsSwitchIPAddress = _WsSwitchIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 27, 1, 1),
    _WsSwitchIPAddress_Type()
)
wsSwitchIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSwitchIPAddress.setStatus("current")


class _WsSwitchClusterPriority_Type(Unsigned32):
    """Custom type wsSwitchClusterPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WsSwitchClusterPriority_Type.__name__ = "Unsigned32"
_WsSwitchClusterPriority_Object = MibTableColumn
wsSwitchClusterPriority = _WsSwitchClusterPriority_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 27, 1, 2),
    _WsSwitchClusterPriority_Type()
)
wsSwitchClusterPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSwitchClusterPriority.setStatus("current")


class _WsSwitchAPImageDownloadMode_Type(DisplayString):
    """Custom type wsSwitchAPImageDownloadMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WsSwitchAPImageDownloadMode_Type.__name__ = "DisplayString"
_WsSwitchAPImageDownloadMode_Object = MibTableColumn
wsSwitchAPImageDownloadMode = _WsSwitchAPImageDownloadMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 27, 1, 3),
    _WsSwitchAPImageDownloadMode_Type()
)
wsSwitchAPImageDownloadMode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsSwitchAPImageDownloadMode.setStatus("current")


class _WsSwitchTotalAPs_Type(Unsigned32):
    """Custom type wsSwitchTotalAPs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48),
    )


_WsSwitchTotalAPs_Type.__name__ = "Unsigned32"
_WsSwitchTotalAPs_Object = MibTableColumn
wsSwitchTotalAPs = _WsSwitchTotalAPs_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 27, 1, 4),
    _WsSwitchTotalAPs_Type()
)
wsSwitchTotalAPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSwitchTotalAPs.setStatus("current")


class _WsSwitchManagedAPs_Type(Unsigned32):
    """Custom type wsSwitchManagedAPs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48),
    )


_WsSwitchManagedAPs_Type.__name__ = "Unsigned32"
_WsSwitchManagedAPs_Object = MibTableColumn
wsSwitchManagedAPs = _WsSwitchManagedAPs_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 27, 1, 5),
    _WsSwitchManagedAPs_Type()
)
wsSwitchManagedAPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSwitchManagedAPs.setStatus("current")


class _WsSwitchDiscoveredAPs_Type(Unsigned32):
    """Custom type wsSwitchDiscoveredAPs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48),
    )


_WsSwitchDiscoveredAPs_Type.__name__ = "Unsigned32"
_WsSwitchDiscoveredAPs_Object = MibTableColumn
wsSwitchDiscoveredAPs = _WsSwitchDiscoveredAPs_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 27, 1, 6),
    _WsSwitchDiscoveredAPs_Type()
)
wsSwitchDiscoveredAPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSwitchDiscoveredAPs.setStatus("current")


class _WsSwitchConnectionFailedAPs_Type(Unsigned32):
    """Custom type wsSwitchConnectionFailedAPs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48),
    )


_WsSwitchConnectionFailedAPs_Type.__name__ = "Unsigned32"
_WsSwitchConnectionFailedAPs_Object = MibTableColumn
wsSwitchConnectionFailedAPs = _WsSwitchConnectionFailedAPs_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 27, 1, 7),
    _WsSwitchConnectionFailedAPs_Type()
)
wsSwitchConnectionFailedAPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSwitchConnectionFailedAPs.setStatus("current")
_WsSwitchMaximumManagedAPs_Type = Unsigned32
_WsSwitchMaximumManagedAPs_Object = MibTableColumn
wsSwitchMaximumManagedAPs = _WsSwitchMaximumManagedAPs_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 27, 1, 8),
    _WsSwitchMaximumManagedAPs_Type()
)
wsSwitchMaximumManagedAPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSwitchMaximumManagedAPs.setStatus("current")


class _WsSwitchTotalClients_Type(Unsigned32):
    """Custom type wsSwitchTotalClients based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8192),
    )


_WsSwitchTotalClients_Type.__name__ = "Unsigned32"
_WsSwitchTotalClients_Object = MibTableColumn
wsSwitchTotalClients = _WsSwitchTotalClients_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 27, 1, 9),
    _WsSwitchTotalClients_Type()
)
wsSwitchTotalClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSwitchTotalClients.setStatus("current")


class _WsSwitchAuthenticatedClients_Type(Unsigned32):
    """Custom type wsSwitchAuthenticatedClients based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8192),
    )


_WsSwitchAuthenticatedClients_Type.__name__ = "Unsigned32"
_WsSwitchAuthenticatedClients_Object = MibTableColumn
wsSwitchAuthenticatedClients = _WsSwitchAuthenticatedClients_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 27, 1, 10),
    _WsSwitchAuthenticatedClients_Type()
)
wsSwitchAuthenticatedClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSwitchAuthenticatedClients.setStatus("current")


class _WsSwitchWLANUtilization_Type(Unsigned32):
    """Custom type wsSwitchWLANUtilization based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_WsSwitchWLANUtilization_Type.__name__ = "Unsigned32"
_WsSwitchWLANUtilization_Object = MibTableColumn
wsSwitchWLANUtilization = _WsSwitchWLANUtilization_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 27, 1, 11),
    _WsSwitchWLANUtilization_Type()
)
wsSwitchWLANUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSwitchWLANUtilization.setStatus("current")
_WsSwitchDistTunnelClients_Type = Unsigned32
_WsSwitchDistTunnelClients_Object = MibTableColumn
wsSwitchDistTunnelClients = _WsSwitchDistTunnelClients_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 27, 1, 12),
    _WsSwitchDistTunnelClients_Type()
)
wsSwitchDistTunnelClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSwitchDistTunnelClients.setStatus("current")
_WsSwitchStatisticsTable_Object = MibTable
wsSwitchStatisticsTable = _WsSwitchStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 28)
)
if mibBuilder.loadTexts:
    wsSwitchStatisticsTable.setStatus("current")
_WsSwitchStatisticsEntry_Object = MibTableRow
wsSwitchStatisticsEntry = _WsSwitchStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 28, 1)
)
wsSwitchStatisticsEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsSwitchIPAddress"),
)
if mibBuilder.loadTexts:
    wsSwitchStatisticsEntry.setStatus("current")
_WsSwitchWLANBytesTransmitted_Type = Counter64
_WsSwitchWLANBytesTransmitted_Object = MibTableColumn
wsSwitchWLANBytesTransmitted = _WsSwitchWLANBytesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 28, 1, 1),
    _WsSwitchWLANBytesTransmitted_Type()
)
wsSwitchWLANBytesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSwitchWLANBytesTransmitted.setStatus("current")
_WsSwitchWLANBytesReceived_Type = Counter64
_WsSwitchWLANBytesReceived_Object = MibTableColumn
wsSwitchWLANBytesReceived = _WsSwitchWLANBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 28, 1, 2),
    _WsSwitchWLANBytesReceived_Type()
)
wsSwitchWLANBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSwitchWLANBytesReceived.setStatus("current")
_WsSwitchWLANPktsTransmitted_Type = Counter64
_WsSwitchWLANPktsTransmitted_Object = MibTableColumn
wsSwitchWLANPktsTransmitted = _WsSwitchWLANPktsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 28, 1, 3),
    _WsSwitchWLANPktsTransmitted_Type()
)
wsSwitchWLANPktsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSwitchWLANPktsTransmitted.setStatus("current")
_WsSwitchWLANPktsReceived_Type = Counter64
_WsSwitchWLANPktsReceived_Object = MibTableColumn
wsSwitchWLANPktsReceived = _WsSwitchWLANPktsReceived_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 28, 1, 4),
    _WsSwitchWLANPktsReceived_Type()
)
wsSwitchWLANPktsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSwitchWLANPktsReceived.setStatus("current")
_WsSwitchWLANBytesTransmitDropped_Type = Counter64
_WsSwitchWLANBytesTransmitDropped_Object = MibTableColumn
wsSwitchWLANBytesTransmitDropped = _WsSwitchWLANBytesTransmitDropped_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 28, 1, 5),
    _WsSwitchWLANBytesTransmitDropped_Type()
)
wsSwitchWLANBytesTransmitDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSwitchWLANBytesTransmitDropped.setStatus("current")
_WsSwitchWLANBytesRecvDropped_Type = Counter64
_WsSwitchWLANBytesRecvDropped_Object = MibTableColumn
wsSwitchWLANBytesRecvDropped = _WsSwitchWLANBytesRecvDropped_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 28, 1, 6),
    _WsSwitchWLANBytesRecvDropped_Type()
)
wsSwitchWLANBytesRecvDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSwitchWLANBytesRecvDropped.setStatus("current")
_WsSwitchWLANPktsTransmitDropped_Type = Counter64
_WsSwitchWLANPktsTransmitDropped_Object = MibTableColumn
wsSwitchWLANPktsTransmitDropped = _WsSwitchWLANPktsTransmitDropped_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 28, 1, 7),
    _WsSwitchWLANPktsTransmitDropped_Type()
)
wsSwitchWLANPktsTransmitDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSwitchWLANPktsTransmitDropped.setStatus("current")
_WsSwitchWLANPktsRecvDropped_Type = Counter64
_WsSwitchWLANPktsRecvDropped_Object = MibTableColumn
wsSwitchWLANPktsRecvDropped = _WsSwitchWLANPktsRecvDropped_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 28, 1, 8),
    _WsSwitchWLANPktsRecvDropped_Type()
)
wsSwitchWLANPktsRecvDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSwitchWLANPktsRecvDropped.setStatus("current")


class _WsAutoIPAssignMode_Type(Integer32):
    """Custom type wsAutoIPAssignMode based on Integer32"""
    defaultValue = 1

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


_WsAutoIPAssignMode_Type.__name__ = "Integer32"
_WsAutoIPAssignMode_Object = MibScalar
wsAutoIPAssignMode = _WsAutoIPAssignMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 29),
    _WsAutoIPAssignMode_Type()
)
wsAutoIPAssignMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAutoIPAssignMode.setStatus("current")
_WsSwitchStaticIPAddress_Type = IpAddress
_WsSwitchStaticIPAddress_Object = MibScalar
wsSwitchStaticIPAddress = _WsSwitchStaticIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 30),
    _WsSwitchStaticIPAddress_Type()
)
wsSwitchStaticIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSwitchStaticIPAddress.setStatus("current")
_WsGlobalTspecConfiguration_ObjectIdentity = ObjectIdentity
wsGlobalTspecConfiguration = _WsGlobalTspecConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 31)
)


class _WsTspecViolationReportInterval_Type(Unsigned32):
    """Custom type wsTspecViolationReportInterval based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_WsTspecViolationReportInterval_Type.__name__ = "Unsigned32"
_WsTspecViolationReportInterval_Object = MibScalar
wsTspecViolationReportInterval = _WsTspecViolationReportInterval_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 31, 1),
    _WsTspecViolationReportInterval_Type()
)
wsTspecViolationReportInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsTspecViolationReportInterval.setStatus("current")


class _NetworkMutualAuthMode_Type(Integer32):
    """Custom type networkMutualAuthMode based on Integer32"""
    defaultValue = 2

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


_NetworkMutualAuthMode_Type.__name__ = "Integer32"
_NetworkMutualAuthMode_Object = MibScalar
networkMutualAuthMode = _NetworkMutualAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 32),
    _NetworkMutualAuthMode_Type()
)
networkMutualAuthMode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    networkMutualAuthMode.setStatus("current")


class _UnmanagedAPReprovisioning_Type(Integer32):
    """Custom type unmanagedAPReprovisioning based on Integer32"""
    defaultValue = 1

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


_UnmanagedAPReprovisioning_Type.__name__ = "Integer32"
_UnmanagedAPReprovisioning_Object = MibScalar
unmanagedAPReprovisioning = _UnmanagedAPReprovisioning_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 33),
    _UnmanagedAPReprovisioning_Type()
)
unmanagedAPReprovisioning.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    unmanagedAPReprovisioning.setStatus("current")


class _ApProvisionDbAgeTime_Type(Unsigned32):
    """Custom type apProvisionDbAgeTime based on Unsigned32"""
    defaultValue = 72

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_ApProvisionDbAgeTime_Type.__name__ = "Unsigned32"
_ApProvisionDbAgeTime_Object = MibScalar
apProvisionDbAgeTime = _ApProvisionDbAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 34),
    _ApProvisionDbAgeTime_Type()
)
apProvisionDbAgeTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apProvisionDbAgeTime.setStatus("current")


class _SwitchProvisioning_Type(Integer32):
    """Custom type switchProvisioning based on Integer32"""
    defaultValue = 1

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


_SwitchProvisioning_Type.__name__ = "Integer32"
_SwitchProvisioning_Object = MibScalar
switchProvisioning = _SwitchProvisioning_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 35),
    _SwitchProvisioning_Type()
)
switchProvisioning.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    switchProvisioning.setStatus("current")


class _WsIpBasePort_Type(Unsigned32):
    """Custom type wsIpBasePort based on Unsigned32"""
    defaultValue = 57775

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65000),
    )


_WsIpBasePort_Type.__name__ = "Unsigned32"
_WsIpBasePort_Object = MibScalar
wsIpBasePort = _WsIpBasePort_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 36),
    _WsIpBasePort_Type()
)
wsIpBasePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsIpBasePort.setStatus("current")


class _DevLocMeasurementSys_Type(Integer32):
    """Custom type devLocMeasurementSys based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("metric", 1),
          ("english", 2))
    )


_DevLocMeasurementSys_Type.__name__ = "Integer32"
_DevLocMeasurementSys_Object = MibScalar
devLocMeasurementSys = _DevLocMeasurementSys_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 37),
    _DevLocMeasurementSys_Type()
)
devLocMeasurementSys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devLocMeasurementSys.setStatus("current")


class _DevLocRfScanLocMode_Type(Integer32):
    """Custom type devLocRfScanLocMode based on Integer32"""
    defaultValue = 1

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


_DevLocRfScanLocMode_Type.__name__ = "Integer32"
_DevLocRfScanLocMode_Object = MibScalar
devLocRfScanLocMode = _DevLocRfScanLocMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 38),
    _DevLocRfScanLocMode_Type()
)
devLocRfScanLocMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devLocRfScanLocMode.setStatus("current")


class _DevLocRfScanLocInterval_Type(Unsigned32):
    """Custom type devLocRfScanLocInterval based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 3600),
    )


_DevLocRfScanLocInterval_Type.__name__ = "Unsigned32"
_DevLocRfScanLocInterval_Object = MibScalar
devLocRfScanLocInterval = _DevLocRfScanLocInterval_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 1, 39),
    _DevLocRfScanLocInterval_Type()
)
devLocRfScanLocInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devLocRfScanLocInterval.setStatus("current")
_Discovery_ObjectIdentity = ObjectIdentity
discovery = _Discovery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 2)
)


class _WsIPPollMode_Type(Integer32):
    """Custom type wsIPPollMode based on Integer32"""
    defaultValue = 1

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


_WsIPPollMode_Type.__name__ = "Integer32"
_WsIPPollMode_Object = MibScalar
wsIPPollMode = _WsIPPollMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 2, 1),
    _WsIPPollMode_Type()
)
wsIPPollMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsIPPollMode.setStatus("current")


class _WsL2DiscoveryMode_Type(Integer32):
    """Custom type wsL2DiscoveryMode based on Integer32"""
    defaultValue = 1

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


_WsL2DiscoveryMode_Type.__name__ = "Integer32"
_WsL2DiscoveryMode_Object = MibScalar
wsL2DiscoveryMode = _WsL2DiscoveryMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 2, 2),
    _WsL2DiscoveryMode_Type()
)
wsL2DiscoveryMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsL2DiscoveryMode.setStatus("current")
_WsIPPollListTable_Object = MibTable
wsIPPollListTable = _WsIPPollListTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 2, 3)
)
if mibBuilder.loadTexts:
    wsIPPollListTable.setStatus("current")
_WsIPPollListEntry_Object = MibTableRow
wsIPPollListEntry = _WsIPPollListEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 2, 3, 1)
)
wsIPPollListEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsPollIpAddress"),
)
if mibBuilder.loadTexts:
    wsIPPollListEntry.setStatus("current")
_WsPollIpAddress_Type = IpAddress
_WsPollIpAddress_Object = MibTableColumn
wsPollIpAddress = _WsPollIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 2, 3, 1, 1),
    _WsPollIpAddress_Type()
)
wsPollIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPollIpAddress.setStatus("current")


class _WsPollIPStatus_Type(Integer32):
    """Custom type wsPollIPStatus based on Integer32"""
    defaultValue = 1

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
        *(("not-polled", 1),
          ("polled", 2),
          ("discovered", 3),
          ("discovered-failed", 4))
    )


_WsPollIPStatus_Type.__name__ = "Integer32"
_WsPollIPStatus_Object = MibTableColumn
wsPollIPStatus = _WsPollIPStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 2, 3, 1, 2),
    _WsPollIPStatus_Type()
)
wsPollIPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPollIPStatus.setStatus("current")
_WsIPPollRowStatus_Type = RowStatus
_WsIPPollRowStatus_Object = MibTableColumn
wsIPPollRowStatus = _WsIPPollRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 2, 3, 1, 3),
    _WsIPPollRowStatus_Type()
)
wsIPPollRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsIPPollRowStatus.setStatus("current")
_WsL2DiscoveryVlanListTable_Object = MibTable
wsL2DiscoveryVlanListTable = _WsL2DiscoveryVlanListTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 2, 4)
)
if mibBuilder.loadTexts:
    wsL2DiscoveryVlanListTable.setStatus("current")
_WsL2DiscoveryVlanListEntry_Object = MibTableRow
wsL2DiscoveryVlanListEntry = _WsL2DiscoveryVlanListEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 2, 4, 1)
)
wsL2DiscoveryVlanListEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsL2DiscoveryVlanId"),
)
if mibBuilder.loadTexts:
    wsL2DiscoveryVlanListEntry.setStatus("current")


class _WsL2DiscoveryVlanId_Type(Integer32):
    """Custom type wsL2DiscoveryVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_WsL2DiscoveryVlanId_Type.__name__ = "Integer32"
_WsL2DiscoveryVlanId_Object = MibTableColumn
wsL2DiscoveryVlanId = _WsL2DiscoveryVlanId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 2, 4, 1, 1),
    _WsL2DiscoveryVlanId_Type()
)
wsL2DiscoveryVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsL2DiscoveryVlanId.setStatus("current")
_WsL2DiscoveryVlanRowStatus_Type = RowStatus
_WsL2DiscoveryVlanRowStatus_Object = MibTableColumn
wsL2DiscoveryVlanRowStatus = _WsL2DiscoveryVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 2, 4, 1, 2),
    _WsL2DiscoveryVlanRowStatus_Type()
)
wsL2DiscoveryVlanRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsL2DiscoveryVlanRowStatus.setStatus("current")


class _WsIPPollListMaxNumOfEntries_Type(Unsigned32):
    """Custom type wsIPPollListMaxNumOfEntries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_WsIPPollListMaxNumOfEntries_Type.__name__ = "Unsigned32"
_WsIPPollListMaxNumOfEntries_Object = MibScalar
wsIPPollListMaxNumOfEntries = _WsIPPollListMaxNumOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 2, 5),
    _WsIPPollListMaxNumOfEntries_Type()
)
wsIPPollListMaxNumOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsIPPollListMaxNumOfEntries.setStatus("current")


class _WsIPPollListNumOfConfigEntries_Type(Unsigned32):
    """Custom type wsIPPollListNumOfConfigEntries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_WsIPPollListNumOfConfigEntries_Type.__name__ = "Unsigned32"
_WsIPPollListNumOfConfigEntries_Object = MibScalar
wsIPPollListNumOfConfigEntries = _WsIPPollListNumOfConfigEntries_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 2, 6),
    _WsIPPollListNumOfConfigEntries_Type()
)
wsIPPollListNumOfConfigEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsIPPollListNumOfConfigEntries.setStatus("current")


class _WsIPPollListNumOfPolledEntries_Type(Unsigned32):
    """Custom type wsIPPollListNumOfPolledEntries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_WsIPPollListNumOfPolledEntries_Type.__name__ = "Unsigned32"
_WsIPPollListNumOfPolledEntries_Object = MibScalar
wsIPPollListNumOfPolledEntries = _WsIPPollListNumOfPolledEntries_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 2, 7),
    _WsIPPollListNumOfPolledEntries_Type()
)
wsIPPollListNumOfPolledEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsIPPollListNumOfPolledEntries.setStatus("current")


class _WsIPPollListNumOfNotPolledEntries_Type(Unsigned32):
    """Custom type wsIPPollListNumOfNotPolledEntries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_WsIPPollListNumOfNotPolledEntries_Type.__name__ = "Unsigned32"
_WsIPPollListNumOfNotPolledEntries_Object = MibScalar
wsIPPollListNumOfNotPolledEntries = _WsIPPollListNumOfNotPolledEntries_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 2, 8),
    _WsIPPollListNumOfNotPolledEntries_Type()
)
wsIPPollListNumOfNotPolledEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsIPPollListNumOfNotPolledEntries.setStatus("current")


class _WsIPPollListNumOfDiscoveredEntries_Type(Unsigned32):
    """Custom type wsIPPollListNumOfDiscoveredEntries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_WsIPPollListNumOfDiscoveredEntries_Type.__name__ = "Unsigned32"
_WsIPPollListNumOfDiscoveredEntries_Object = MibScalar
wsIPPollListNumOfDiscoveredEntries = _WsIPPollListNumOfDiscoveredEntries_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 2, 9),
    _WsIPPollListNumOfDiscoveredEntries_Type()
)
wsIPPollListNumOfDiscoveredEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsIPPollListNumOfDiscoveredEntries.setStatus("current")


class _WsIPPollListNumOfDiscoveredFailedEntries_Type(Unsigned32):
    """Custom type wsIPPollListNumOfDiscoveredFailedEntries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_WsIPPollListNumOfDiscoveredFailedEntries_Type.__name__ = "Unsigned32"
_WsIPPollListNumOfDiscoveredFailedEntries_Object = MibScalar
wsIPPollListNumOfDiscoveredFailedEntries = _WsIPPollListNumOfDiscoveredFailedEntries_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 2, 10),
    _WsIPPollListNumOfDiscoveredFailedEntries_Type()
)
wsIPPollListNumOfDiscoveredFailedEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsIPPollListNumOfDiscoveredFailedEntries.setStatus("current")
_ApProfile_ObjectIdentity = ObjectIdentity
apProfile = _ApProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3)
)
_WsAPProfileTable_Object = MibTable
wsAPProfileTable = _WsAPProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 1)
)
if mibBuilder.loadTexts:
    wsAPProfileTable.setStatus("current")
_WsAPProfileEntry_Object = MibTableRow
wsAPProfileEntry = _WsAPProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 1, 1)
)
wsAPProfileEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsAPProfileId"),
)
if mibBuilder.loadTexts:
    wsAPProfileEntry.setStatus("current")


class _WsAPProfileId_Type(Integer32):
    """Custom type wsAPProfileId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_WsAPProfileId_Type.__name__ = "Integer32"
_WsAPProfileId_Object = MibTableColumn
wsAPProfileId = _WsAPProfileId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 1, 1, 1),
    _WsAPProfileId_Type()
)
wsAPProfileId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPProfileId.setStatus("current")


class _WsAPProfileName_Type(DisplayString):
    """Custom type wsAPProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WsAPProfileName_Type.__name__ = "DisplayString"
_WsAPProfileName_Object = MibTableColumn
wsAPProfileName = _WsAPProfileName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 1, 1, 2),
    _WsAPProfileName_Type()
)
wsAPProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPProfileName.setStatus("current")


class _WsAPProfileState_Type(Integer32):
    """Custom type wsAPProfileState based on Integer32"""
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
        *(("none", 0),
          ("configured", 1),
          ("requested", 2),
          ("in-progress", 3),
          ("associated", 4))
    )


_WsAPProfileState_Type.__name__ = "Integer32"
_WsAPProfileState_Object = MibTableColumn
wsAPProfileState = _WsAPProfileState_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 1, 1, 3),
    _WsAPProfileState_Type()
)
wsAPProfileState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPProfileState.setStatus("current")
_WsAPProfileRowStatus_Type = RowStatus
_WsAPProfileRowStatus_Object = MibTableColumn
wsAPProfileRowStatus = _WsAPProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 1, 1, 8),
    _WsAPProfileRowStatus_Type()
)
wsAPProfileRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPProfileRowStatus.setStatus("current")


class _WsCopyAPProfileToProfileId_Type(Integer32):
    """Custom type wsCopyAPProfileToProfileId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_WsCopyAPProfileToProfileId_Type.__name__ = "Integer32"
_WsCopyAPProfileToProfileId_Object = MibTableColumn
wsCopyAPProfileToProfileId = _WsCopyAPProfileToProfileId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 1, 1, 9),
    _WsCopyAPProfileToProfileId_Type()
)
wsCopyAPProfileToProfileId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsCopyAPProfileToProfileId.setStatus("current")


class _WsAPProfileApply_Type(Integer32):
    """Custom type wsAPProfileApply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("apply", 2))
    )


_WsAPProfileApply_Type.__name__ = "Integer32"
_WsAPProfileApply_Object = MibTableColumn
wsAPProfileApply = _WsAPProfileApply_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 1, 1, 10),
    _WsAPProfileApply_Type()
)
wsAPProfileApply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPProfileApply.setStatus("current")


class _WsAPHardwareTypeID_Type(Integer32):
    """Custom type wsAPHardwareTypeID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_WsAPHardwareTypeID_Type.__name__ = "Integer32"
_WsAPHardwareTypeID_Object = MibTableColumn
wsAPHardwareTypeID = _WsAPHardwareTypeID_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 1, 1, 11),
    _WsAPHardwareTypeID_Type()
)
wsAPHardwareTypeID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAPHardwareTypeID.setStatus("current")


class _WsAPWiredDetectionVlanId_Type(Integer32):
    """Custom type wsAPWiredDetectionVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WsAPWiredDetectionVlanId_Type.__name__ = "Integer32"
_WsAPWiredDetectionVlanId_Object = MibTableColumn
wsAPWiredDetectionVlanId = _WsAPWiredDetectionVlanId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 1, 1, 12),
    _WsAPWiredDetectionVlanId_Type()
)
wsAPWiredDetectionVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPWiredDetectionVlanId.setStatus("current")


class _WsAPProfileDisconnAPFwdingMode_Type(Integer32):
    """Custom type wsAPProfileDisconnAPFwdingMode based on Integer32"""
    defaultValue = 2

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


_WsAPProfileDisconnAPFwdingMode_Type.__name__ = "Integer32"
_WsAPProfileDisconnAPFwdingMode_Object = MibTableColumn
wsAPProfileDisconnAPFwdingMode = _WsAPProfileDisconnAPFwdingMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 1, 1, 13),
    _WsAPProfileDisconnAPFwdingMode_Type()
)
wsAPProfileDisconnAPFwdingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPProfileDisconnAPFwdingMode.setStatus("current")


class _WsAPProfileDisconnAPMgmtMode_Type(Integer32):
    """Custom type wsAPProfileDisconnAPMgmtMode based on Integer32"""
    defaultValue = 1

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


_WsAPProfileDisconnAPMgmtMode_Type.__name__ = "Integer32"
_WsAPProfileDisconnAPMgmtMode_Object = MibTableColumn
wsAPProfileDisconnAPMgmtMode = _WsAPProfileDisconnAPMgmtMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 1, 1, 14),
    _WsAPProfileDisconnAPMgmtMode_Type()
)
wsAPProfileDisconnAPMgmtMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPProfileDisconnAPMgmtMode.setStatus("current")


class _WsAPProfileAeroScoutSupportMode_Type(Integer32):
    """Custom type wsAPProfileAeroScoutSupportMode based on Integer32"""
    defaultValue = 2

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


_WsAPProfileAeroScoutSupportMode_Type.__name__ = "Integer32"
_WsAPProfileAeroScoutSupportMode_Object = MibTableColumn
wsAPProfileAeroScoutSupportMode = _WsAPProfileAeroScoutSupportMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 1, 1, 15),
    _WsAPProfileAeroScoutSupportMode_Type()
)
wsAPProfileAeroScoutSupportMode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAPProfileAeroScoutSupportMode.setStatus("current")
_WsAPProfileRadioTable_Object = MibTable
wsAPProfileRadioTable = _WsAPProfileRadioTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 3)
)
if mibBuilder.loadTexts:
    wsAPProfileRadioTable.setStatus("current")
_WsAPProfileRadioEntry_Object = MibTableRow
wsAPProfileRadioEntry = _WsAPProfileRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 3, 1)
)
wsAPProfileRadioEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsAPProfileId"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsAPRadioInterface"),
)
if mibBuilder.loadTexts:
    wsAPProfileRadioEntry.setStatus("current")


class _WsAPRadioInterface_Type(Integer32):
    """Custom type wsAPRadioInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WsAPRadioInterface_Type.__name__ = "Integer32"
_WsAPRadioInterface_Object = MibTableColumn
wsAPRadioInterface = _WsAPRadioInterface_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 3, 1, 1),
    _WsAPRadioInterface_Type()
)
wsAPRadioInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPRadioInterface.setStatus("current")


class _WsAPRadioAdminMode_Type(Integer32):
    """Custom type wsAPRadioAdminMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_WsAPRadioAdminMode_Type.__name__ = "Integer32"
_WsAPRadioAdminMode_Object = MibTableColumn
wsAPRadioAdminMode = _WsAPRadioAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 3, 1, 2),
    _WsAPRadioAdminMode_Type()
)
wsAPRadioAdminMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPRadioAdminMode.setStatus("current")


class _WsAPRadioFrequency_Type(Integer32):
    """Custom type wsAPRadioFrequency based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("ieee802dot11a", 1),
          ("ieee802dot11bg", 2),
          ("ieee802dot11an", 3),
          ("ieee802dot11bgn", 4),
          ("fiveGHzIeee802dot11n", 5),
          ("twoDotFourGHzIeee802dot11n", 6),
          ("fiveGHzIeee802dot11anac", 7),
          ("fiveGHzIeee802dot11nac", 8))
    )


_WsAPRadioFrequency_Type.__name__ = "Integer32"
_WsAPRadioFrequency_Object = MibTableColumn
wsAPRadioFrequency = _WsAPRadioFrequency_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 3, 1, 3),
    _WsAPRadioFrequency_Type()
)
wsAPRadioFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPRadioFrequency.setStatus("current")


class _WsAPRadioOtherChannelsScanMode_Type(Integer32):
    """Custom type wsAPRadioOtherChannelsScanMode based on Integer32"""
    defaultValue = 2

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


_WsAPRadioOtherChannelsScanMode_Type.__name__ = "Integer32"
_WsAPRadioOtherChannelsScanMode_Object = MibTableColumn
wsAPRadioOtherChannelsScanMode = _WsAPRadioOtherChannelsScanMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 3, 1, 4),
    _WsAPRadioOtherChannelsScanMode_Type()
)
wsAPRadioOtherChannelsScanMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPRadioOtherChannelsScanMode.setStatus("current")


class _WsAPRadioOtherChannelsScanInterval_Type(Integer32):
    """Custom type wsAPRadioOtherChannelsScanInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 120),
    )


_WsAPRadioOtherChannelsScanInterval_Type.__name__ = "Integer32"
_WsAPRadioOtherChannelsScanInterval_Object = MibTableColumn
wsAPRadioOtherChannelsScanInterval = _WsAPRadioOtherChannelsScanInterval_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 3, 1, 5),
    _WsAPRadioOtherChannelsScanInterval_Type()
)
wsAPRadioOtherChannelsScanInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPRadioOtherChannelsScanInterval.setStatus("current")


class _WsAPRadioSentryScanMode_Type(Integer32):
    """Custom type wsAPRadioSentryScanMode based on Integer32"""
    defaultValue = 2

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


_WsAPRadioSentryScanMode_Type.__name__ = "Integer32"
_WsAPRadioSentryScanMode_Object = MibTableColumn
wsAPRadioSentryScanMode = _WsAPRadioSentryScanMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 3, 1, 6),
    _WsAPRadioSentryScanMode_Type()
)
wsAPRadioSentryScanMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPRadioSentryScanMode.setStatus("current")


class _WsAPRadioSentryScanChannel_Type(Integer32):
    """Custom type wsAPRadioSentryScanChannel based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ieee802dot11an", 1),
          ("ieee802dot11bORgn", 2),
          ("all", 3))
    )


_WsAPRadioSentryScanChannel_Type.__name__ = "Integer32"
_WsAPRadioSentryScanChannel_Object = MibTableColumn
wsAPRadioSentryScanChannel = _WsAPRadioSentryScanChannel_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 3, 1, 7),
    _WsAPRadioSentryScanChannel_Type()
)
wsAPRadioSentryScanChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPRadioSentryScanChannel.setStatus("current")


class _WsAPRadioScanDuration_Type(Integer32):
    """Custom type wsAPRadioScanDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 2000),
    )


_WsAPRadioScanDuration_Type.__name__ = "Integer32"
_WsAPRadioScanDuration_Object = MibTableColumn
wsAPRadioScanDuration = _WsAPRadioScanDuration_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 3, 1, 8),
    _WsAPRadioScanDuration_Type()
)
wsAPRadioScanDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPRadioScanDuration.setStatus("current")


class _WsAPRadioRateLimitMode_Type(Integer32):
    """Custom type wsAPRadioRateLimitMode based on Integer32"""
    defaultValue = 2

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


_WsAPRadioRateLimitMode_Type.__name__ = "Integer32"
_WsAPRadioRateLimitMode_Object = MibTableColumn
wsAPRadioRateLimitMode = _WsAPRadioRateLimitMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 3, 1, 9),
    _WsAPRadioRateLimitMode_Type()
)
wsAPRadioRateLimitMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPRadioRateLimitMode.setStatus("current")


class _WsAPRadioRateLimit_Type(Integer32):
    """Custom type wsAPRadioRateLimit based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_WsAPRadioRateLimit_Type.__name__ = "Integer32"
_WsAPRadioRateLimit_Object = MibTableColumn
wsAPRadioRateLimit = _WsAPRadioRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 3, 1, 10),
    _WsAPRadioRateLimit_Type()
)
wsAPRadioRateLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPRadioRateLimit.setStatus("current")


class _WsAPRadioRateLimitBurst_Type(Integer32):
    """Custom type wsAPRadioRateLimitBurst based on Integer32"""
    defaultValue = 75

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 75),
    )


_WsAPRadioRateLimitBurst_Type.__name__ = "Integer32"
_WsAPRadioRateLimitBurst_Object = MibTableColumn
wsAPRadioRateLimitBurst = _WsAPRadioRateLimitBurst_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 3, 1, 11),
    _WsAPRadioRateLimitBurst_Type()
)
wsAPRadioRateLimitBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPRadioRateLimitBurst.setStatus("current")


class _WsAPRadioBeaconInterval_Type(Integer32):
    """Custom type wsAPRadioBeaconInterval based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 2000),
    )


_WsAPRadioBeaconInterval_Type.__name__ = "Integer32"
_WsAPRadioBeaconInterval_Object = MibTableColumn
wsAPRadioBeaconInterval = _WsAPRadioBeaconInterval_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 3, 1, 12),
    _WsAPRadioBeaconInterval_Type()
)
wsAPRadioBeaconInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPRadioBeaconInterval.setStatus("current")


class _WsAPRadioDTIMPeriod_Type(Integer32):
    """Custom type wsAPRadioDTIMPeriod based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WsAPRadioDTIMPeriod_Type.__name__ = "Integer32"
_WsAPRadioDTIMPeriod_Object = MibTableColumn
wsAPRadioDTIMPeriod = _WsAPRadioDTIMPeriod_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 3, 1, 13),
    _WsAPRadioDTIMPeriod_Type()
)
wsAPRadioDTIMPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPRadioDTIMPeriod.setStatus("current")


class _WsAPRadioFragmentationThreshold_Type(Integer32):
    """Custom type wsAPRadioFragmentationThreshold based on Integer32"""
    defaultValue = 2346

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 2346),
    )


_WsAPRadioFragmentationThreshold_Type.__name__ = "Integer32"
_WsAPRadioFragmentationThreshold_Object = MibTableColumn
wsAPRadioFragmentationThreshold = _WsAPRadioFragmentationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 3, 1, 14),
    _WsAPRadioFragmentationThreshold_Type()
)
wsAPRadioFragmentationThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPRadioFragmentationThreshold.setStatus("current")


class _WsAPRadioRTSThreshold_Type(Integer32):
    """Custom type wsAPRadioRTSThreshold based on Integer32"""
    defaultValue = 2347

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2347),
    )


_WsAPRadioRTSThreshold_Type.__name__ = "Integer32"
_WsAPRadioRTSThreshold_Object = MibTableColumn
wsAPRadioRTSThreshold = _WsAPRadioRTSThreshold_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 3, 1, 15),
    _WsAPRadioRTSThreshold_Type()
)
wsAPRadioRTSThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPRadioRTSThreshold.setStatus("current")


class _WsAPRadioShortRetryLimit_Type(Integer32):
    """Custom type wsAPRadioShortRetryLimit based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WsAPRadioShortRetryLimit_Type.__name__ = "Integer32"
_WsAPRadioShortRetryLimit_Object = MibTableColumn
wsAPRadioShortRetryLimit = _WsAPRadioShortRetryLimit_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 3, 1, 16),
    _WsAPRadioShortRetryLimit_Type()
)
wsAPRadioShortRetryLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPRadioShortRetryLimit.setStatus("current")


class _WsAPRadioLongRetryLimit_Type(Integer32):
    """Custom type wsAPRadioLongRetryLimit based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WsAPRadioLongRetryLimit_Type.__name__ = "Integer32"
_WsAPRadioLongRetryLimit_Object = MibTableColumn
wsAPRadioLongRetryLimit = _WsAPRadioLongRetryLimit_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 3, 1, 17),
    _WsAPRadioLongRetryLimit_Type()
)
wsAPRadioLongRetryLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPRadioLongRetryLimit.setStatus("current")


class _WsAPRadioMaxTransmitLifetime_Type(Unsigned32):
    """Custom type wsAPRadioMaxTransmitLifetime based on Unsigned32"""
    defaultValue = 512


_WsAPRadioMaxTransmitLifetime_Type.__name__ = "Unsigned32"
_WsAPRadioMaxTransmitLifetime_Object = MibTableColumn
wsAPRadioMaxTransmitLifetime = _WsAPRadioMaxTransmitLifetime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 3, 1, 18),
    _WsAPRadioMaxTransmitLifetime_Type()
)
wsAPRadioMaxTransmitLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPRadioMaxTransmitLifetime.setStatus("current")


class _WsAPRadioMaxReceiveLifetime_Type(Unsigned32):
    """Custom type wsAPRadioMaxReceiveLifetime based on Unsigned32"""
    defaultValue = 512


_WsAPRadioMaxReceiveLifetime_Type.__name__ = "Unsigned32"
_WsAPRadioMaxReceiveLifetime_Object = MibTableColumn
wsAPRadioMaxReceiveLifetime = _WsAPRadioMaxReceiveLifetime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 3, 1, 19),
    _WsAPRadioMaxReceiveLifetime_Type()
)
wsAPRadioMaxReceiveLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPRadioMaxReceiveLifetime.setStatus("current")


class _WsAPRadioMaxClients_Type(Integer32):
    """Custom type wsAPRadioMaxClients based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_WsAPRadioMaxClients_Type.__name__ = "Integer32"
_WsAPRadioMaxClients_Object = MibTableColumn
wsAPRadioMaxClients = _WsAPRadioMaxClients_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 3, 1, 20),
    _WsAPRadioMaxClients_Type()
)
wsAPRadioMaxClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPRadioMaxClients.setStatus("current")


class _WsAPRadioAutoPowerMode_Type(Integer32):
    """Custom type wsAPRadioAutoPowerMode based on Integer32"""
    defaultValue = 1

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


_WsAPRadioAutoPowerMode_Type.__name__ = "Integer32"
_WsAPRadioAutoPowerMode_Object = MibTableColumn
wsAPRadioAutoPowerMode = _WsAPRadioAutoPowerMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 3, 1, 21),
    _WsAPRadioAutoPowerMode_Type()
)
wsAPRadioAutoPowerMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPRadioAutoPowerMode.setStatus("current")


class _WsAPRadioTxPower_Type(Integer32):
    """Custom type wsAPRadioTxPower based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WsAPRadioTxPower_Type.__name__ = "Integer32"
_WsAPRadioTxPower_Object = MibTableColumn
wsAPRadioTxPower = _WsAPRadioTxPower_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 3, 1, 22),
    _WsAPRadioTxPower_Type()
)
wsAPRadioTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPRadioTxPower.setStatus("current")


class _WsAPRadioWMMMode_Type(Integer32):
    """Custom type wsAPRadioWMMMode based on Integer32"""
    defaultValue = 1

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


_WsAPRadioWMMMode_Type.__name__ = "Integer32"
_WsAPRadioWMMMode_Object = MibTableColumn
wsAPRadioWMMMode = _WsAPRadioWMMMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 3, 1, 23),
    _WsAPRadioWMMMode_Type()
)
wsAPRadioWMMMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPRadioWMMMode.setStatus("current")


class _WsAPRadioLoadBalancingMode_Type(Integer32):
    """Custom type wsAPRadioLoadBalancingMode based on Integer32"""
    defaultValue = 2

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


_WsAPRadioLoadBalancingMode_Type.__name__ = "Integer32"
_WsAPRadioLoadBalancingMode_Object = MibTableColumn
wsAPRadioLoadBalancingMode = _WsAPRadioLoadBalancingMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 3, 1, 24),
    _WsAPRadioLoadBalancingMode_Type()
)
wsAPRadioLoadBalancingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPRadioLoadBalancingMode.setStatus("current")


class _WsAPRadioUtilization_Type(Integer32):
    """Custom type wsAPRadioUtilization based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WsAPRadioUtilization_Type.__name__ = "Integer32"
_WsAPRadioUtilization_Object = MibTableColumn
wsAPRadioUtilization = _WsAPRadioUtilization_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 3, 1, 25),
    _WsAPRadioUtilization_Type()
)
wsAPRadioUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPRadioUtilization.setStatus("current")


class _WsAPRadioAutoChannelMode_Type(Integer32):
    """Custom type wsAPRadioAutoChannelMode based on Integer32"""
    defaultValue = 1

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


_WsAPRadioAutoChannelMode_Type.__name__ = "Integer32"
_WsAPRadioAutoChannelMode_Object = MibTableColumn
wsAPRadioAutoChannelMode = _WsAPRadioAutoChannelMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 3, 1, 26),
    _WsAPRadioAutoChannelMode_Type()
)
wsAPRadioAutoChannelMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPRadioAutoChannelMode.setStatus("current")


class _WsAPRadioStationIsolationMode_Type(Integer32):
    """Custom type wsAPRadioStationIsolationMode based on Integer32"""
    defaultValue = 2

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


_WsAPRadioStationIsolationMode_Type.__name__ = "Integer32"
_WsAPRadioStationIsolationMode_Object = MibTableColumn
wsAPRadioStationIsolationMode = _WsAPRadioStationIsolationMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 3, 1, 27),
    _WsAPRadioStationIsolationMode_Type()
)
wsAPRadioStationIsolationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPRadioStationIsolationMode.setStatus("current")


class _WsAPRadioChannelBandwidth_Type(Integer32):
    """Custom type wsAPRadioChannelBandwidth based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("twentyMHz", 1),
          ("fortyMHz", 2),
          ("eightyMHz", 3))
    )


_WsAPRadioChannelBandwidth_Type.__name__ = "Integer32"
_WsAPRadioChannelBandwidth_Object = MibTableColumn
wsAPRadioChannelBandwidth = _WsAPRadioChannelBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 3, 1, 28),
    _WsAPRadioChannelBandwidth_Type()
)
wsAPRadioChannelBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPRadioChannelBandwidth.setStatus("current")


class _WsAPRadioPrimaryChannel_Type(Integer32):
    """Custom type wsAPRadioPrimaryChannel based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("upper", 1),
          ("lower", 2))
    )


_WsAPRadioPrimaryChannel_Type.__name__ = "Integer32"
_WsAPRadioPrimaryChannel_Object = MibTableColumn
wsAPRadioPrimaryChannel = _WsAPRadioPrimaryChannel_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 3, 1, 29),
    _WsAPRadioPrimaryChannel_Type()
)
wsAPRadioPrimaryChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPRadioPrimaryChannel.setStatus("current")


class _WsAPRadioProtectionMode_Type(Integer32):
    """Custom type wsAPRadioProtectionMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("off", 2))
    )


_WsAPRadioProtectionMode_Type.__name__ = "Integer32"
_WsAPRadioProtectionMode_Object = MibTableColumn
wsAPRadioProtectionMode = _WsAPRadioProtectionMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 3, 1, 30),
    _WsAPRadioProtectionMode_Type()
)
wsAPRadioProtectionMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPRadioProtectionMode.setStatus("current")


class _WsAPRadioShortGuardInterval_Type(Integer32):
    """Custom type wsAPRadioShortGuardInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_WsAPRadioShortGuardInterval_Type.__name__ = "Integer32"
_WsAPRadioShortGuardInterval_Object = MibTableColumn
wsAPRadioShortGuardInterval = _WsAPRadioShortGuardInterval_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 3, 1, 31),
    _WsAPRadioShortGuardInterval_Type()
)
wsAPRadioShortGuardInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPRadioShortGuardInterval.setStatus("current")


class _WsAPRadioSTBCMode_Type(Integer32):
    """Custom type wsAPRadioSTBCMode based on Integer32"""
    defaultValue = 1

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


_WsAPRadioSTBCMode_Type.__name__ = "Integer32"
_WsAPRadioSTBCMode_Object = MibTableColumn
wsAPRadioSTBCMode = _WsAPRadioSTBCMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 3, 1, 32),
    _WsAPRadioSTBCMode_Type()
)
wsAPRadioSTBCMode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAPRadioSTBCMode.setStatus("current")


class _WsAPRadioMulticastTxRate_Type(Integer32):
    """Custom type wsAPRadioMulticastTxRate based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 127),
    )


_WsAPRadioMulticastTxRate_Type.__name__ = "Integer32"
_WsAPRadioMulticastTxRate_Object = MibTableColumn
wsAPRadioMulticastTxRate = _WsAPRadioMulticastTxRate_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 3, 1, 33),
    _WsAPRadioMulticastTxRate_Type()
)
wsAPRadioMulticastTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPRadioMulticastTxRate.setStatus("current")


class _WsAPRadioAPSDMode_Type(Integer32):
    """Custom type wsAPRadioAPSDMode based on Integer32"""
    defaultValue = 1

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


_WsAPRadioAPSDMode_Type.__name__ = "Integer32"
_WsAPRadioAPSDMode_Object = MibTableColumn
wsAPRadioAPSDMode = _WsAPRadioAPSDMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 3, 1, 34),
    _WsAPRadioAPSDMode_Type()
)
wsAPRadioAPSDMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPRadioAPSDMode.setStatus("current")


class _WsAPRadioNoAckMode_Type(Integer32):
    """Custom type wsAPRadioNoAckMode based on Integer32"""
    defaultValue = 2

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


_WsAPRadioNoAckMode_Type.__name__ = "Integer32"
_WsAPRadioNoAckMode_Object = MibTableColumn
wsAPRadioNoAckMode = _WsAPRadioNoAckMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 3, 1, 35),
    _WsAPRadioNoAckMode_Type()
)
wsAPRadioNoAckMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPRadioNoAckMode.setStatus("current")


class _WsAPRadioResourceMeasEnabled_Type(Integer32):
    """Custom type wsAPRadioResourceMeasEnabled based on Integer32"""
    defaultValue = 1

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


_WsAPRadioResourceMeasEnabled_Type.__name__ = "Integer32"
_WsAPRadioResourceMeasEnabled_Object = MibTableColumn
wsAPRadioResourceMeasEnabled = _WsAPRadioResourceMeasEnabled_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 3, 1, 36),
    _WsAPRadioResourceMeasEnabled_Type()
)
wsAPRadioResourceMeasEnabled.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAPRadioResourceMeasEnabled.setStatus("current")


class _WsAPRadioQOSEDCATemplate_Type(Integer32):
    """Custom type wsAPRadioQOSEDCATemplate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("custom", 0),
          ("factory-default", 1),
          ("voice", 2))
    )


_WsAPRadioQOSEDCATemplate_Type.__name__ = "Integer32"
_WsAPRadioQOSEDCATemplate_Object = MibTableColumn
wsAPRadioQOSEDCATemplate = _WsAPRadioQOSEDCATemplate_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 3, 1, 37),
    _WsAPRadioQOSEDCATemplate_Type()
)
wsAPRadioQOSEDCATemplate.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAPRadioQOSEDCATemplate.setStatus("current")


class _WsAPRadioMinTxPower_Type(Integer32):
    """Custom type wsAPRadioMinTxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WsAPRadioMinTxPower_Type.__name__ = "Integer32"
_WsAPRadioMinTxPower_Object = MibTableColumn
wsAPRadioMinTxPower = _WsAPRadioMinTxPower_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 3, 1, 38),
    _WsAPRadioMinTxPower_Type()
)
wsAPRadioMinTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPRadioMinTxPower.setStatus("current")
_WsAPProfileRadioSupportedRatesTable_Object = MibTable
wsAPProfileRadioSupportedRatesTable = _WsAPProfileRadioSupportedRatesTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 4)
)
if mibBuilder.loadTexts:
    wsAPProfileRadioSupportedRatesTable.setStatus("current")
_WsAPProfileRadioSupportedRatesEntry_Object = MibTableRow
wsAPProfileRadioSupportedRatesEntry = _WsAPProfileRadioSupportedRatesEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 4, 1)
)
wsAPProfileRadioSupportedRatesEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsAPProfileId"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsAPRadioInterface"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsSupportedDataRate"),
)
if mibBuilder.loadTexts:
    wsAPProfileRadioSupportedRatesEntry.setStatus("current")


class _WsSupportedDataRate_Type(Integer32):
    """Custom type wsSupportedDataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 127),
    )


_WsSupportedDataRate_Type.__name__ = "Integer32"
_WsSupportedDataRate_Object = MibTableColumn
wsSupportedDataRate = _WsSupportedDataRate_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 4, 1, 1),
    _WsSupportedDataRate_Type()
)
wsSupportedDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSupportedDataRate.setStatus("current")


class _WsAPProfileRadioSupportedDataMode_Type(Integer32):
    """Custom type wsAPProfileRadioSupportedDataMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("supported", 1),
          ("not-supported", 2))
    )


_WsAPProfileRadioSupportedDataMode_Type.__name__ = "Integer32"
_WsAPProfileRadioSupportedDataMode_Object = MibTableColumn
wsAPProfileRadioSupportedDataMode = _WsAPProfileRadioSupportedDataMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 4, 1, 2),
    _WsAPProfileRadioSupportedDataMode_Type()
)
wsAPProfileRadioSupportedDataMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPProfileRadioSupportedDataMode.setStatus("current")
_WsAPProfileRadioBasicRatesTable_Object = MibTable
wsAPProfileRadioBasicRatesTable = _WsAPProfileRadioBasicRatesTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 5)
)
if mibBuilder.loadTexts:
    wsAPProfileRadioBasicRatesTable.setStatus("current")
_WsAPProfileRadioBasicRatesEntry_Object = MibTableRow
wsAPProfileRadioBasicRatesEntry = _WsAPProfileRadioBasicRatesEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 5, 1)
)
wsAPProfileRadioBasicRatesEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsAPProfileId"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsAPRadioInterface"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsBasicDataRate"),
)
if mibBuilder.loadTexts:
    wsAPProfileRadioBasicRatesEntry.setStatus("current")


class _WsBasicDataRate_Type(Integer32):
    """Custom type wsBasicDataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 127),
    )


_WsBasicDataRate_Type.__name__ = "Integer32"
_WsBasicDataRate_Object = MibTableColumn
wsBasicDataRate = _WsBasicDataRate_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 5, 1, 1),
    _WsBasicDataRate_Type()
)
wsBasicDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsBasicDataRate.setStatus("current")


class _WsAPProfileRadioBasicDataMode_Type(Integer32):
    """Custom type wsAPProfileRadioBasicDataMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("basic", 1),
          ("not-basic", 2))
    )


_WsAPProfileRadioBasicDataMode_Type.__name__ = "Integer32"
_WsAPProfileRadioBasicDataMode_Object = MibTableColumn
wsAPProfileRadioBasicDataMode = _WsAPProfileRadioBasicDataMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 5, 1, 2),
    _WsAPProfileRadioBasicDataMode_Type()
)
wsAPProfileRadioBasicDataMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPProfileRadioBasicDataMode.setStatus("current")
_WsAPProfileVAPTable_Object = MibTable
wsAPProfileVAPTable = _WsAPProfileVAPTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 6)
)
if mibBuilder.loadTexts:
    wsAPProfileVAPTable.setStatus("current")
_WsAPProfileVAPEntry_Object = MibTableRow
wsAPProfileVAPEntry = _WsAPProfileVAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 6, 1)
)
wsAPProfileVAPEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsAPProfileId"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsAPRadioInterface"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsVAPId"),
)
if mibBuilder.loadTexts:
    wsAPProfileVAPEntry.setStatus("current")


class _WsVAPId_Type(Integer32):
    """Custom type wsVAPId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WsVAPId_Type.__name__ = "Integer32"
_WsVAPId_Object = MibTableColumn
wsVAPId = _WsVAPId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 6, 1, 1),
    _WsVAPId_Type()
)
wsVAPId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsVAPId.setStatus("current")


class _WsVAPMode_Type(Integer32):
    """Custom type wsVAPMode based on Integer32"""
    defaultValue = 1

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


_WsVAPMode_Type.__name__ = "Integer32"
_WsVAPMode_Object = MibTableColumn
wsVAPMode = _WsVAPMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 6, 1, 2),
    _WsVAPMode_Type()
)
wsVAPMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsVAPMode.setStatus("current")


class _WsVAPNetworkId_Type(Integer32):
    """Custom type wsVAPNetworkId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_WsVAPNetworkId_Type.__name__ = "Integer32"
_WsVAPNetworkId_Object = MibTableColumn
wsVAPNetworkId = _WsVAPNetworkId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 6, 1, 3),
    _WsVAPNetworkId_Type()
)
wsVAPNetworkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsVAPNetworkId.setStatus("current")
_WsAPProfileQOSTable_Object = MibTable
wsAPProfileQOSTable = _WsAPProfileQOSTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 7)
)
if mibBuilder.loadTexts:
    wsAPProfileQOSTable.setStatus("current")
_WsAPProfileQOSEntry_Object = MibTableRow
wsAPProfileQOSEntry = _WsAPProfileQOSEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 7, 1)
)
wsAPProfileQOSEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsAPProfileId"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsAPRadioInterface"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsQOSQueueId"),
)
if mibBuilder.loadTexts:
    wsAPProfileQOSEntry.setStatus("current")


class _WsQOSQueueId_Type(Integer32):
    """Custom type wsQOSQueueId based on Integer32"""
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
        *(("voice", 0),
          ("video", 1),
          ("besteffort", 2),
          ("background", 3))
    )


_WsQOSQueueId_Type.__name__ = "Integer32"
_WsQOSQueueId_Object = MibTableColumn
wsQOSQueueId = _WsQOSQueueId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 7, 1, 1),
    _WsQOSQueueId_Type()
)
wsQOSQueueId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsQOSQueueId.setStatus("current")


class _WsAPEDCAAIFS_Type(Integer32):
    """Custom type wsAPEDCAAIFS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WsAPEDCAAIFS_Type.__name__ = "Integer32"
_WsAPEDCAAIFS_Object = MibTableColumn
wsAPEDCAAIFS = _WsAPEDCAAIFS_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 7, 1, 2),
    _WsAPEDCAAIFS_Type()
)
wsAPEDCAAIFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPEDCAAIFS.setStatus("current")


class _WsAPEDCAMinContentionWindow_Type(Integer32):
    """Custom type wsAPEDCAMinContentionWindow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              7,
              15,
              31,
              63,
              127,
              255,
              511,
              1023)
        )
    )
    namedValues = NamedValues(
        *(("one", 1),
          ("three", 3),
          ("seven", 7),
          ("fifteen", 15),
          ("thirty-one", 31),
          ("sixty-three", 63),
          ("onetwenty-seven", 127),
          ("twofifty-five", 255),
          ("fivehundred-eleven", 511),
          ("onethousand-twentythree", 1023))
    )


_WsAPEDCAMinContentionWindow_Type.__name__ = "Integer32"
_WsAPEDCAMinContentionWindow_Object = MibTableColumn
wsAPEDCAMinContentionWindow = _WsAPEDCAMinContentionWindow_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 7, 1, 3),
    _WsAPEDCAMinContentionWindow_Type()
)
wsAPEDCAMinContentionWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPEDCAMinContentionWindow.setStatus("current")


class _WsAPEDCAMaxContentionWindow_Type(Integer32):
    """Custom type wsAPEDCAMaxContentionWindow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              7,
              15,
              31,
              63,
              127,
              255,
              511,
              1023)
        )
    )
    namedValues = NamedValues(
        *(("one", 1),
          ("three", 3),
          ("seven", 7),
          ("fifteen", 15),
          ("thirty-one", 31),
          ("sixty-three", 63),
          ("onetwenty-seven", 127),
          ("twofifty-five", 255),
          ("fivehundred-eleven", 511),
          ("onethousand-twentythree", 1023))
    )


_WsAPEDCAMaxContentionWindow_Type.__name__ = "Integer32"
_WsAPEDCAMaxContentionWindow_Object = MibTableColumn
wsAPEDCAMaxContentionWindow = _WsAPEDCAMaxContentionWindow_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 7, 1, 4),
    _WsAPEDCAMaxContentionWindow_Type()
)
wsAPEDCAMaxContentionWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPEDCAMaxContentionWindow.setStatus("current")


class _WsAPEDCAMaxBurst_Type(Integer32):
    """Custom type wsAPEDCAMaxBurst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999900),
    )


_WsAPEDCAMaxBurst_Type.__name__ = "Integer32"
_WsAPEDCAMaxBurst_Object = MibTableColumn
wsAPEDCAMaxBurst = _WsAPEDCAMaxBurst_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 7, 1, 5),
    _WsAPEDCAMaxBurst_Type()
)
wsAPEDCAMaxBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPEDCAMaxBurst.setStatus("current")


class _WsStationEDCAAIFS_Type(Integer32):
    """Custom type wsStationEDCAAIFS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WsStationEDCAAIFS_Type.__name__ = "Integer32"
_WsStationEDCAAIFS_Object = MibTableColumn
wsStationEDCAAIFS = _WsStationEDCAAIFS_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 7, 1, 6),
    _WsStationEDCAAIFS_Type()
)
wsStationEDCAAIFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsStationEDCAAIFS.setStatus("current")


class _WsStationEDCAMinContentionWindow_Type(Integer32):
    """Custom type wsStationEDCAMinContentionWindow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              7,
              15,
              31,
              63,
              127,
              255,
              511,
              1023)
        )
    )
    namedValues = NamedValues(
        *(("one", 1),
          ("three", 3),
          ("seven", 7),
          ("fifteen", 15),
          ("thirty-one", 31),
          ("sixty-three", 63),
          ("onetwenty-seven", 127),
          ("twofifty-five", 255),
          ("fivehundred-eleven", 511),
          ("onethousand-twentythree", 1023))
    )


_WsStationEDCAMinContentionWindow_Type.__name__ = "Integer32"
_WsStationEDCAMinContentionWindow_Object = MibTableColumn
wsStationEDCAMinContentionWindow = _WsStationEDCAMinContentionWindow_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 7, 1, 7),
    _WsStationEDCAMinContentionWindow_Type()
)
wsStationEDCAMinContentionWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsStationEDCAMinContentionWindow.setStatus("current")


class _WsStationEDCAMaxContentionWindow_Type(Integer32):
    """Custom type wsStationEDCAMaxContentionWindow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              7,
              15,
              31,
              63,
              127,
              255,
              511,
              1023)
        )
    )
    namedValues = NamedValues(
        *(("one", 1),
          ("three", 3),
          ("seven", 7),
          ("fifteen", 15),
          ("thirty-one", 31),
          ("sixty-three", 63),
          ("onetwenty-seven", 127),
          ("twofifty-five", 255),
          ("fivehundred-eleven", 511),
          ("onethousand-twentythree", 1023))
    )


_WsStationEDCAMaxContentionWindow_Type.__name__ = "Integer32"
_WsStationEDCAMaxContentionWindow_Object = MibTableColumn
wsStationEDCAMaxContentionWindow = _WsStationEDCAMaxContentionWindow_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 7, 1, 8),
    _WsStationEDCAMaxContentionWindow_Type()
)
wsStationEDCAMaxContentionWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsStationEDCAMaxContentionWindow.setStatus("current")


class _WsStationEDCATXOPLimit_Type(Integer32):
    """Custom type wsStationEDCATXOPLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WsStationEDCATXOPLimit_Type.__name__ = "Integer32"
_WsStationEDCATXOPLimit_Object = MibTableColumn
wsStationEDCATXOPLimit = _WsStationEDCATXOPLimit_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 7, 1, 9),
    _WsStationEDCATXOPLimit_Type()
)
wsStationEDCATXOPLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsStationEDCATXOPLimit.setStatus("current")
_WsNetworkTable_Object = MibTable
wsNetworkTable = _WsNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 8)
)
if mibBuilder.loadTexts:
    wsNetworkTable.setStatus("current")
_WsNetworkEntry_Object = MibTableRow
wsNetworkEntry = _WsNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 8, 1)
)
wsNetworkEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsNetworkId"),
)
if mibBuilder.loadTexts:
    wsNetworkEntry.setStatus("current")


class _WsNetworkId_Type(Integer32):
    """Custom type wsNetworkId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_WsNetworkId_Type.__name__ = "Integer32"
_WsNetworkId_Object = MibTableColumn
wsNetworkId = _WsNetworkId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 8, 1, 1),
    _WsNetworkId_Type()
)
wsNetworkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNetworkId.setStatus("current")
_WsNetworkIdRowStatus_Type = RowStatus
_WsNetworkIdRowStatus_Object = MibTableColumn
wsNetworkIdRowStatus = _WsNetworkIdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 8, 1, 2),
    _WsNetworkIdRowStatus_Type()
)
wsNetworkIdRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNetworkIdRowStatus.setStatus("current")


class _WsNetworkSSID_Type(DisplayString):
    """Custom type wsNetworkSSID based on DisplayString"""
    defaultValue = OctetString("Guest Network")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WsNetworkSSID_Type.__name__ = "DisplayString"
_WsNetworkSSID_Object = MibTableColumn
wsNetworkSSID = _WsNetworkSSID_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 8, 1, 3),
    _WsNetworkSSID_Type()
)
wsNetworkSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNetworkSSID.setStatus("current")


class _WsNetworkDefaultVLANId_Type(Integer32):
    """Custom type wsNetworkDefaultVLANId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_WsNetworkDefaultVLANId_Type.__name__ = "Integer32"
_WsNetworkDefaultVLANId_Object = MibTableColumn
wsNetworkDefaultVLANId = _WsNetworkDefaultVLANId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 8, 1, 4),
    _WsNetworkDefaultVLANId_Type()
)
wsNetworkDefaultVLANId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNetworkDefaultVLANId.setStatus("current")


class _WsNetworkHideSSIDMode_Type(Integer32):
    """Custom type wsNetworkHideSSIDMode based on Integer32"""
    defaultValue = 2

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


_WsNetworkHideSSIDMode_Type.__name__ = "Integer32"
_WsNetworkHideSSIDMode_Object = MibTableColumn
wsNetworkHideSSIDMode = _WsNetworkHideSSIDMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 8, 1, 5),
    _WsNetworkHideSSIDMode_Type()
)
wsNetworkHideSSIDMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNetworkHideSSIDMode.setStatus("current")


class _WsNetworkDenyBcastMode_Type(Integer32):
    """Custom type wsNetworkDenyBcastMode based on Integer32"""
    defaultValue = 2

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


_WsNetworkDenyBcastMode_Type.__name__ = "Integer32"
_WsNetworkDenyBcastMode_Object = MibTableColumn
wsNetworkDenyBcastMode = _WsNetworkDenyBcastMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 8, 1, 6),
    _WsNetworkDenyBcastMode_Type()
)
wsNetworkDenyBcastMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNetworkDenyBcastMode.setStatus("current")


class _WsNetworkMACAuthenticationMode_Type(Integer32):
    """Custom type wsNetworkMACAuthenticationMode based on Integer32"""
    defaultValue = 3

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
          ("disable", 3))
    )


_WsNetworkMACAuthenticationMode_Type.__name__ = "Integer32"
_WsNetworkMACAuthenticationMode_Object = MibTableColumn
wsNetworkMACAuthenticationMode = _WsNetworkMACAuthenticationMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 8, 1, 10),
    _WsNetworkMACAuthenticationMode_Type()
)
wsNetworkMACAuthenticationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNetworkMACAuthenticationMode.setStatus("current")


class _WsNetworkRadiusAccountingMode_Type(Integer32):
    """Custom type wsNetworkRadiusAccountingMode based on Integer32"""
    defaultValue = 2

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


_WsNetworkRadiusAccountingMode_Type.__name__ = "Integer32"
_WsNetworkRadiusAccountingMode_Object = MibTableColumn
wsNetworkRadiusAccountingMode = _WsNetworkRadiusAccountingMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 8, 1, 14),
    _WsNetworkRadiusAccountingMode_Type()
)
wsNetworkRadiusAccountingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNetworkRadiusAccountingMode.setStatus("current")


class _WsNetworkSecurityMode_Type(Integer32):
    """Custom type wsNetworkSecurityMode based on Integer32"""
    defaultValue = 1

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
        *(("none", 1),
          ("wepStatic", 2),
          ("wep802dot1x", 3),
          ("wpaPersonal", 4),
          ("wpaEnterprise", 5))
    )


_WsNetworkSecurityMode_Type.__name__ = "Integer32"
_WsNetworkSecurityMode_Object = MibTableColumn
wsNetworkSecurityMode = _WsNetworkSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 8, 1, 15),
    _WsNetworkSecurityMode_Type()
)
wsNetworkSecurityMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNetworkSecurityMode.setStatus("current")


class _WsNetworkWPAVersionsSupported_Type(Integer32):
    """Custom type wsNetworkWPAVersionsSupported based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("wpa", 1),
          ("wpa2", 2),
          ("both", 3))
    )


_WsNetworkWPAVersionsSupported_Type.__name__ = "Integer32"
_WsNetworkWPAVersionsSupported_Object = MibTableColumn
wsNetworkWPAVersionsSupported = _WsNetworkWPAVersionsSupported_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 8, 1, 16),
    _WsNetworkWPAVersionsSupported_Type()
)
wsNetworkWPAVersionsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNetworkWPAVersionsSupported.setStatus("current")


class _WsNetworkWPACipherSuites_Type(Integer32):
    """Custom type wsNetworkWPACipherSuites based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tkip", 1),
          ("ccmp", 2),
          ("both", 3))
    )


_WsNetworkWPACipherSuites_Type.__name__ = "Integer32"
_WsNetworkWPACipherSuites_Object = MibTableColumn
wsNetworkWPACipherSuites = _WsNetworkWPACipherSuites_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 8, 1, 17),
    _WsNetworkWPACipherSuites_Type()
)
wsNetworkWPACipherSuites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNetworkWPACipherSuites.setStatus("current")


class _WsNetworkWPAKeyType_Type(Integer32):
    """Custom type wsNetworkWPAKeyType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ascii", 1)
    )


_WsNetworkWPAKeyType_Type.__name__ = "Integer32"
_WsNetworkWPAKeyType_Object = MibTableColumn
wsNetworkWPAKeyType = _WsNetworkWPAKeyType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 8, 1, 18),
    _WsNetworkWPAKeyType_Type()
)
wsNetworkWPAKeyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNetworkWPAKeyType.setStatus("current")


class _WsNetworkWPAKey_Type(DisplayString):
    """Custom type wsNetworkWPAKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 63),
    )


_WsNetworkWPAKey_Type.__name__ = "DisplayString"
_WsNetworkWPAKey_Object = MibTableColumn
wsNetworkWPAKey = _WsNetworkWPAKey_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 8, 1, 19),
    _WsNetworkWPAKey_Type()
)
wsNetworkWPAKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNetworkWPAKey.setStatus("current")


class _WsNetworkWPA2PreAuthenticationMode_Type(Integer32):
    """Custom type wsNetworkWPA2PreAuthenticationMode based on Integer32"""
    defaultValue = 1

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


_WsNetworkWPA2PreAuthenticationMode_Type.__name__ = "Integer32"
_WsNetworkWPA2PreAuthenticationMode_Object = MibTableColumn
wsNetworkWPA2PreAuthenticationMode = _WsNetworkWPA2PreAuthenticationMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 8, 1, 20),
    _WsNetworkWPA2PreAuthenticationMode_Type()
)
wsNetworkWPA2PreAuthenticationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNetworkWPA2PreAuthenticationMode.setStatus("current")


class _WsNetworkWPA2PreAuthenticationLimit_Type(Integer32):
    """Custom type wsNetworkWPA2PreAuthenticationLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 192),
    )


_WsNetworkWPA2PreAuthenticationLimit_Type.__name__ = "Integer32"
_WsNetworkWPA2PreAuthenticationLimit_Object = MibTableColumn
wsNetworkWPA2PreAuthenticationLimit = _WsNetworkWPA2PreAuthenticationLimit_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 8, 1, 21),
    _WsNetworkWPA2PreAuthenticationLimit_Type()
)
wsNetworkWPA2PreAuthenticationLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNetworkWPA2PreAuthenticationLimit.setStatus("current")


class _WsNetworkWPA2RoambackKeyCacheHoldtime_Type(Integer32):
    """Custom type wsNetworkWPA2RoambackKeyCacheHoldtime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_WsNetworkWPA2RoambackKeyCacheHoldtime_Type.__name__ = "Integer32"
_WsNetworkWPA2RoambackKeyCacheHoldtime_Object = MibTableColumn
wsNetworkWPA2RoambackKeyCacheHoldtime = _WsNetworkWPA2RoambackKeyCacheHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 8, 1, 23),
    _WsNetworkWPA2RoambackKeyCacheHoldtime_Type()
)
wsNetworkWPA2RoambackKeyCacheHoldtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNetworkWPA2RoambackKeyCacheHoldtime.setStatus("current")


class _WsNetworkStaticWEPAuthenticationMode_Type(Integer32):
    """Custom type wsNetworkStaticWEPAuthenticationMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("openSystem", 1),
          ("sharedKey", 2),
          ("both", 3))
    )


_WsNetworkStaticWEPAuthenticationMode_Type.__name__ = "Integer32"
_WsNetworkStaticWEPAuthenticationMode_Object = MibTableColumn
wsNetworkStaticWEPAuthenticationMode = _WsNetworkStaticWEPAuthenticationMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 8, 1, 24),
    _WsNetworkStaticWEPAuthenticationMode_Type()
)
wsNetworkStaticWEPAuthenticationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNetworkStaticWEPAuthenticationMode.setStatus("current")


class _WsNetworkUseWEPTransferKeyIndex_Type(Integer32):
    """Custom type wsNetworkUseWEPTransferKeyIndex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_WsNetworkUseWEPTransferKeyIndex_Type.__name__ = "Integer32"
_WsNetworkUseWEPTransferKeyIndex_Object = MibTableColumn
wsNetworkUseWEPTransferKeyIndex = _WsNetworkUseWEPTransferKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 8, 1, 25),
    _WsNetworkUseWEPTransferKeyIndex_Type()
)
wsNetworkUseWEPTransferKeyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNetworkUseWEPTransferKeyIndex.setStatus("current")


class _WsNetworkWEPKeyType_Type(Integer32):
    """Custom type wsNetworkWEPKeyType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 1),
          ("hex", 2))
    )


_WsNetworkWEPKeyType_Type.__name__ = "Integer32"
_WsNetworkWEPKeyType_Object = MibTableColumn
wsNetworkWEPKeyType = _WsNetworkWEPKeyType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 8, 1, 26),
    _WsNetworkWEPKeyType_Type()
)
wsNetworkWEPKeyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNetworkWEPKeyType.setStatus("current")


class _WsNetworkWEPKeyLength_Type(Integer32):
    """Custom type wsNetworkWEPKeyLength based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(64,
              128)
        )
    )
    namedValues = NamedValues(
        *(("sixty-four", 64),
          ("one-twentyeight", 128))
    )


_WsNetworkWEPKeyLength_Type.__name__ = "Integer32"
_WsNetworkWEPKeyLength_Object = MibTableColumn
wsNetworkWEPKeyLength = _WsNetworkWEPKeyLength_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 8, 1, 27),
    _WsNetworkWEPKeyLength_Type()
)
wsNetworkWEPKeyLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNetworkWEPKeyLength.setStatus("current")


class _WsNetworkWEPKey1_Type(DisplayString):
    """Custom type wsNetworkWEPKey1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(5, 32),
    )


_WsNetworkWEPKey1_Type.__name__ = "DisplayString"
_WsNetworkWEPKey1_Object = MibTableColumn
wsNetworkWEPKey1 = _WsNetworkWEPKey1_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 8, 1, 28),
    _WsNetworkWEPKey1_Type()
)
wsNetworkWEPKey1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNetworkWEPKey1.setStatus("current")


class _WsNetworkWEPKey2_Type(DisplayString):
    """Custom type wsNetworkWEPKey2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(5, 32),
    )


_WsNetworkWEPKey2_Type.__name__ = "DisplayString"
_WsNetworkWEPKey2_Object = MibTableColumn
wsNetworkWEPKey2 = _WsNetworkWEPKey2_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 8, 1, 29),
    _WsNetworkWEPKey2_Type()
)
wsNetworkWEPKey2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNetworkWEPKey2.setStatus("current")


class _WsNetworkWEPKey3_Type(DisplayString):
    """Custom type wsNetworkWEPKey3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(5, 32),
    )


_WsNetworkWEPKey3_Type.__name__ = "DisplayString"
_WsNetworkWEPKey3_Object = MibTableColumn
wsNetworkWEPKey3 = _WsNetworkWEPKey3_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 8, 1, 30),
    _WsNetworkWEPKey3_Type()
)
wsNetworkWEPKey3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNetworkWEPKey3.setStatus("current")


class _WsNetworkWEPKey4_Type(DisplayString):
    """Custom type wsNetworkWEPKey4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(5, 32),
    )


_WsNetworkWEPKey4_Type.__name__ = "DisplayString"
_WsNetworkWEPKey4_Object = MibTableColumn
wsNetworkWEPKey4 = _WsNetworkWEPKey4_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 8, 1, 31),
    _WsNetworkWEPKey4_Type()
)
wsNetworkWEPKey4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNetworkWEPKey4.setStatus("current")


class _WsClearNetworkEntry_Type(Integer32):
    """Custom type wsClearNetworkEntry based on Integer32"""
    defaultValue = 2

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


_WsClearNetworkEntry_Type.__name__ = "Integer32"
_WsClearNetworkEntry_Object = MibTableColumn
wsClearNetworkEntry = _WsClearNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 8, 1, 33),
    _WsClearNetworkEntry_Type()
)
wsClearNetworkEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsClearNetworkEntry.setStatus("current")


class _WsNetworkRedirectMode_Type(Integer32):
    """Custom type wsNetworkRedirectMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("http", 2))
    )


_WsNetworkRedirectMode_Type.__name__ = "Integer32"
_WsNetworkRedirectMode_Object = MibTableColumn
wsNetworkRedirectMode = _WsNetworkRedirectMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 8, 1, 34),
    _WsNetworkRedirectMode_Type()
)
wsNetworkRedirectMode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsNetworkRedirectMode.setStatus("deprecated")


class _WsNetworkRedirectURL_Type(DisplayString):
    """Custom type wsNetworkRedirectURL based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_WsNetworkRedirectURL_Type.__name__ = "DisplayString"
_WsNetworkRedirectURL_Object = MibTableColumn
wsNetworkRedirectURL = _WsNetworkRedirectURL_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 8, 1, 35),
    _WsNetworkRedirectURL_Type()
)
wsNetworkRedirectURL.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsNetworkRedirectURL.setStatus("deprecated")
_WsIfNumber_Type = Integer32
_WsIfNumber_Object = MibTableColumn
wsIfNumber = _WsIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 8, 1, 36),
    _WsIfNumber_Type()
)
wsIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsIfNumber.setStatus("current")


class _WsNetworkAuthRadiusServerName_Type(DisplayString):
    """Custom type wsNetworkAuthRadiusServerName based on DisplayString"""
    defaultValue = OctetString("Default-RADIUS-Server")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WsNetworkAuthRadiusServerName_Type.__name__ = "DisplayString"
_WsNetworkAuthRadiusServerName_Object = MibTableColumn
wsNetworkAuthRadiusServerName = _WsNetworkAuthRadiusServerName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 8, 1, 37),
    _WsNetworkAuthRadiusServerName_Type()
)
wsNetworkAuthRadiusServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNetworkAuthRadiusServerName.setStatus("current")


class _WsNetworkAuthRadiusServerConfiguredStatus_Type(Integer32):
    """Custom type wsNetworkAuthRadiusServerConfiguredStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-configured", 1),
          ("configured", 2))
    )


_WsNetworkAuthRadiusServerConfiguredStatus_Type.__name__ = "Integer32"
_WsNetworkAuthRadiusServerConfiguredStatus_Object = MibTableColumn
wsNetworkAuthRadiusServerConfiguredStatus = _WsNetworkAuthRadiusServerConfiguredStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 8, 1, 38),
    _WsNetworkAuthRadiusServerConfiguredStatus_Type()
)
wsNetworkAuthRadiusServerConfiguredStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNetworkAuthRadiusServerConfiguredStatus.setStatus("current")


class _WsNetworkAcctRadiusServerName_Type(DisplayString):
    """Custom type wsNetworkAcctRadiusServerName based on DisplayString"""
    defaultValue = OctetString("Default-RADIUS-Server")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WsNetworkAcctRadiusServerName_Type.__name__ = "DisplayString"
_WsNetworkAcctRadiusServerName_Object = MibTableColumn
wsNetworkAcctRadiusServerName = _WsNetworkAcctRadiusServerName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 8, 1, 39),
    _WsNetworkAcctRadiusServerName_Type()
)
wsNetworkAcctRadiusServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNetworkAcctRadiusServerName.setStatus("current")


class _WsNetworkAcctRadiusServerConfiguredStatus_Type(Integer32):
    """Custom type wsNetworkAcctRadiusServerConfiguredStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-configured", 1),
          ("configured", 2))
    )


_WsNetworkAcctRadiusServerConfiguredStatus_Type.__name__ = "Integer32"
_WsNetworkAcctRadiusServerConfiguredStatus_Object = MibTableColumn
wsNetworkAcctRadiusServerConfiguredStatus = _WsNetworkAcctRadiusServerConfiguredStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 8, 1, 40),
    _WsNetworkAcctRadiusServerConfiguredStatus_Type()
)
wsNetworkAcctRadiusServerConfiguredStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNetworkAcctRadiusServerConfiguredStatus.setStatus("current")


class _WsUseNetworkRadiusConfig_Type(Integer32):
    """Custom type wsUseNetworkRadiusConfig based on Integer32"""
    defaultValue = 1

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


_WsUseNetworkRadiusConfig_Type.__name__ = "Integer32"
_WsUseNetworkRadiusConfig_Object = MibTableColumn
wsUseNetworkRadiusConfig = _WsUseNetworkRadiusConfig_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 8, 1, 41),
    _WsUseNetworkRadiusConfig_Type()
)
wsUseNetworkRadiusConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsUseNetworkRadiusConfig.setStatus("current")


class _WsNetworkDistTunnelMode_Type(Integer32):
    """Custom type wsNetworkDistTunnelMode based on Integer32"""
    defaultValue = 2

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


_WsNetworkDistTunnelMode_Type.__name__ = "Integer32"
_WsNetworkDistTunnelMode_Object = MibTableColumn
wsNetworkDistTunnelMode = _WsNetworkDistTunnelMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 8, 1, 42),
    _WsNetworkDistTunnelMode_Type()
)
wsNetworkDistTunnelMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNetworkDistTunnelMode.setStatus("current")


class _WsNetworkBcastKeyRefreshRate_Type(Unsigned32):
    """Custom type wsNetworkBcastKeyRefreshRate based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_WsNetworkBcastKeyRefreshRate_Type.__name__ = "Unsigned32"
_WsNetworkBcastKeyRefreshRate_Object = MibTableColumn
wsNetworkBcastKeyRefreshRate = _WsNetworkBcastKeyRefreshRate_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 8, 1, 43),
    _WsNetworkBcastKeyRefreshRate_Type()
)
wsNetworkBcastKeyRefreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNetworkBcastKeyRefreshRate.setStatus("current")


class _WsNetworkSessionKeyRefreshRate_Type(Unsigned32):
    """Custom type wsNetworkSessionKeyRefreshRate based on Unsigned32"""
    defaultValue = 0


_WsNetworkSessionKeyRefreshRate_Type.__name__ = "Unsigned32"
_WsNetworkSessionKeyRefreshRate_Object = MibTableColumn
wsNetworkSessionKeyRefreshRate = _WsNetworkSessionKeyRefreshRate_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 8, 1, 44),
    _WsNetworkSessionKeyRefreshRate_Type()
)
wsNetworkSessionKeyRefreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNetworkSessionKeyRefreshRate.setStatus("current")


class _WsNetworkARPSuppressionMode_Type(Integer32):
    """Custom type wsNetworkARPSuppressionMode based on Integer32"""
    defaultValue = 2

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


_WsNetworkARPSuppressionMode_Type.__name__ = "Integer32"
_WsNetworkARPSuppressionMode_Object = MibTableColumn
wsNetworkARPSuppressionMode = _WsNetworkARPSuppressionMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 8, 1, 45),
    _WsNetworkARPSuppressionMode_Type()
)
wsNetworkARPSuppressionMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNetworkARPSuppressionMode.setStatus("current")


class _WsNetworkBandSteerMode_Type(Integer32):
    """Custom type wsNetworkBandSteerMode based on Integer32"""
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


_WsNetworkBandSteerMode_Type.__name__ = "Integer32"
_WsNetworkBandSteerMode_Object = MibTableColumn
wsNetworkBandSteerMode = _WsNetworkBandSteerMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 8, 1, 46),
    _WsNetworkBandSteerMode_Type()
)
wsNetworkBandSteerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsNetworkBandSteerMode.setStatus("current")
_WsNetworkClientQosTable_Object = MibTable
wsNetworkClientQosTable = _WsNetworkClientQosTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 9)
)
if mibBuilder.loadTexts:
    wsNetworkClientQosTable.setStatus("current")
_WsNetworkClientQosEntry_Object = MibTableRow
wsNetworkClientQosEntry = _WsNetworkClientQosEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 9, 1)
)
if mibBuilder.loadTexts:
    wsNetworkClientQosEntry.setStatus("current")


class _WsNetworkClientQosBandwidthLimitDown_Type(Unsigned32):
    """Custom type wsNetworkClientQosBandwidthLimitDown based on Unsigned32"""
    defaultValue = 0


_WsNetworkClientQosBandwidthLimitDown_Type.__name__ = "Unsigned32"
_WsNetworkClientQosBandwidthLimitDown_Object = MibTableColumn
wsNetworkClientQosBandwidthLimitDown = _WsNetworkClientQosBandwidthLimitDown_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 9, 1, 1),
    _WsNetworkClientQosBandwidthLimitDown_Type()
)
wsNetworkClientQosBandwidthLimitDown.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsNetworkClientQosBandwidthLimitDown.setStatus("current")


class _WsNetworkClientQosBandwidthLimitUp_Type(Unsigned32):
    """Custom type wsNetworkClientQosBandwidthLimitUp based on Unsigned32"""
    defaultValue = 0


_WsNetworkClientQosBandwidthLimitUp_Type.__name__ = "Unsigned32"
_WsNetworkClientQosBandwidthLimitUp_Object = MibTableColumn
wsNetworkClientQosBandwidthLimitUp = _WsNetworkClientQosBandwidthLimitUp_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 9, 1, 2),
    _WsNetworkClientQosBandwidthLimitUp_Type()
)
wsNetworkClientQosBandwidthLimitUp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsNetworkClientQosBandwidthLimitUp.setStatus("current")


class _WsNetworkClientQosAccessControlDownType_Type(Integer32):
    """Custom type wsNetworkClientQosAccessControlDownType based on Integer32"""
    defaultValue = 1

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
          ("ip", 2),
          ("mac", 3),
          ("ipv6", 4))
    )


_WsNetworkClientQosAccessControlDownType_Type.__name__ = "Integer32"
_WsNetworkClientQosAccessControlDownType_Object = MibTableColumn
wsNetworkClientQosAccessControlDownType = _WsNetworkClientQosAccessControlDownType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 9, 1, 3),
    _WsNetworkClientQosAccessControlDownType_Type()
)
wsNetworkClientQosAccessControlDownType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsNetworkClientQosAccessControlDownType.setStatus("current")


class _WsNetworkClientQosAccessControlDownName_Type(DisplayString):
    """Custom type wsNetworkClientQosAccessControlDownName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_WsNetworkClientQosAccessControlDownName_Type.__name__ = "DisplayString"
_WsNetworkClientQosAccessControlDownName_Object = MibTableColumn
wsNetworkClientQosAccessControlDownName = _WsNetworkClientQosAccessControlDownName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 9, 1, 4),
    _WsNetworkClientQosAccessControlDownName_Type()
)
wsNetworkClientQosAccessControlDownName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsNetworkClientQosAccessControlDownName.setStatus("current")


class _WsNetworkClientQosAccessControlUpType_Type(Integer32):
    """Custom type wsNetworkClientQosAccessControlUpType based on Integer32"""
    defaultValue = 1

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
          ("ip", 2),
          ("mac", 3),
          ("ipv6", 4))
    )


_WsNetworkClientQosAccessControlUpType_Type.__name__ = "Integer32"
_WsNetworkClientQosAccessControlUpType_Object = MibTableColumn
wsNetworkClientQosAccessControlUpType = _WsNetworkClientQosAccessControlUpType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 9, 1, 5),
    _WsNetworkClientQosAccessControlUpType_Type()
)
wsNetworkClientQosAccessControlUpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsNetworkClientQosAccessControlUpType.setStatus("current")


class _WsNetworkClientQosAccessControlUpName_Type(DisplayString):
    """Custom type wsNetworkClientQosAccessControlUpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_WsNetworkClientQosAccessControlUpName_Type.__name__ = "DisplayString"
_WsNetworkClientQosAccessControlUpName_Object = MibTableColumn
wsNetworkClientQosAccessControlUpName = _WsNetworkClientQosAccessControlUpName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 9, 1, 6),
    _WsNetworkClientQosAccessControlUpName_Type()
)
wsNetworkClientQosAccessControlUpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsNetworkClientQosAccessControlUpName.setStatus("current")


class _WsNetworkClientQosDiffservPolicyDownType_Type(Integer32):
    """Custom type wsNetworkClientQosDiffservPolicyDownType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("in", 2))
    )


_WsNetworkClientQosDiffservPolicyDownType_Type.__name__ = "Integer32"
_WsNetworkClientQosDiffservPolicyDownType_Object = MibTableColumn
wsNetworkClientQosDiffservPolicyDownType = _WsNetworkClientQosDiffservPolicyDownType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 9, 1, 7),
    _WsNetworkClientQosDiffservPolicyDownType_Type()
)
wsNetworkClientQosDiffservPolicyDownType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsNetworkClientQosDiffservPolicyDownType.setStatus("current")


class _WsNetworkClientQosDiffservPolicyDownName_Type(DisplayString):
    """Custom type wsNetworkClientQosDiffservPolicyDownName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_WsNetworkClientQosDiffservPolicyDownName_Type.__name__ = "DisplayString"
_WsNetworkClientQosDiffservPolicyDownName_Object = MibTableColumn
wsNetworkClientQosDiffservPolicyDownName = _WsNetworkClientQosDiffservPolicyDownName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 9, 1, 8),
    _WsNetworkClientQosDiffservPolicyDownName_Type()
)
wsNetworkClientQosDiffservPolicyDownName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsNetworkClientQosDiffservPolicyDownName.setStatus("current")


class _WsNetworkClientQosDiffservPolicyUpType_Type(Integer32):
    """Custom type wsNetworkClientQosDiffservPolicyUpType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("in", 2))
    )


_WsNetworkClientQosDiffservPolicyUpType_Type.__name__ = "Integer32"
_WsNetworkClientQosDiffservPolicyUpType_Object = MibTableColumn
wsNetworkClientQosDiffservPolicyUpType = _WsNetworkClientQosDiffservPolicyUpType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 9, 1, 9),
    _WsNetworkClientQosDiffservPolicyUpType_Type()
)
wsNetworkClientQosDiffservPolicyUpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsNetworkClientQosDiffservPolicyUpType.setStatus("current")


class _WsNetworkClientQosDiffservPolicyUpName_Type(DisplayString):
    """Custom type wsNetworkClientQosDiffservPolicyUpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_WsNetworkClientQosDiffservPolicyUpName_Type.__name__ = "DisplayString"
_WsNetworkClientQosDiffservPolicyUpName_Object = MibTableColumn
wsNetworkClientQosDiffservPolicyUpName = _WsNetworkClientQosDiffservPolicyUpName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 9, 1, 10),
    _WsNetworkClientQosDiffservPolicyUpName_Type()
)
wsNetworkClientQosDiffservPolicyUpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsNetworkClientQosDiffservPolicyUpName.setStatus("current")


class _WsNetworkClientQosMode_Type(Integer32):
    """Custom type wsNetworkClientQosMode based on Integer32"""
    defaultValue = 2

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


_WsNetworkClientQosMode_Type.__name__ = "Integer32"
_WsNetworkClientQosMode_Object = MibTableColumn
wsNetworkClientQosMode = _WsNetworkClientQosMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 9, 1, 11),
    _WsNetworkClientQosMode_Type()
)
wsNetworkClientQosMode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsNetworkClientQosMode.setStatus("current")
_WsAPProfileRadioSupportedChannelsTable_Object = MibTable
wsAPProfileRadioSupportedChannelsTable = _WsAPProfileRadioSupportedChannelsTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 10)
)
if mibBuilder.loadTexts:
    wsAPProfileRadioSupportedChannelsTable.setStatus("current")
_WsAPProfileRadioSupportedChannelsEntry_Object = MibTableRow
wsAPProfileRadioSupportedChannelsEntry = _WsAPProfileRadioSupportedChannelsEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 10, 1)
)
wsAPProfileRadioSupportedChannelsEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsAPProfileId"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsAPRadioInterface"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsSupportedChannel"),
)
if mibBuilder.loadTexts:
    wsAPProfileRadioSupportedChannelsEntry.setStatus("current")


class _WsSupportedChannel_Type(Integer32):
    """Custom type wsSupportedChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WsSupportedChannel_Type.__name__ = "Integer32"
_WsSupportedChannel_Object = MibTableColumn
wsSupportedChannel = _WsSupportedChannel_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 10, 1, 1),
    _WsSupportedChannel_Type()
)
wsSupportedChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSupportedChannel.setStatus("current")
_WsAPProfileRadioEligibleChannelsTable_Object = MibTable
wsAPProfileRadioEligibleChannelsTable = _WsAPProfileRadioEligibleChannelsTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 11)
)
if mibBuilder.loadTexts:
    wsAPProfileRadioEligibleChannelsTable.setStatus("current")
_WsAPProfileRadioEligibleChannelsEntry_Object = MibTableRow
wsAPProfileRadioEligibleChannelsEntry = _WsAPProfileRadioEligibleChannelsEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 11, 1)
)
wsAPProfileRadioEligibleChannelsEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsAPProfileId"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsAPRadioInterface"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsEligibleChannel"),
)
if mibBuilder.loadTexts:
    wsAPProfileRadioEligibleChannelsEntry.setStatus("current")


class _WsEligibleChannel_Type(Integer32):
    """Custom type wsEligibleChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WsEligibleChannel_Type.__name__ = "Integer32"
_WsEligibleChannel_Object = MibTableColumn
wsEligibleChannel = _WsEligibleChannel_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 11, 1, 1),
    _WsEligibleChannel_Type()
)
wsEligibleChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsEligibleChannel.setStatus("current")
_WsEligibleChannelRowStatus_Type = RowStatus
_WsEligibleChannelRowStatus_Object = MibTableColumn
wsEligibleChannelRowStatus = _WsEligibleChannelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 11, 1, 2),
    _WsEligibleChannelRowStatus_Type()
)
wsEligibleChannelRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsEligibleChannelRowStatus.setStatus("current")
_WsAPProfileRadioTspecTable_Object = MibTable
wsAPProfileRadioTspecTable = _WsAPProfileRadioTspecTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 12)
)
if mibBuilder.loadTexts:
    wsAPProfileRadioTspecTable.setStatus("current")
_WsAPProfileRadioTspecEntry_Object = MibTableRow
wsAPProfileRadioTspecEntry = _WsAPProfileRadioTspecEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 12, 1)
)
if mibBuilder.loadTexts:
    wsAPProfileRadioTspecEntry.setStatus("current")


class _WsAPRadioTspecMode_Type(Integer32):
    """Custom type wsAPRadioTspecMode based on Integer32"""
    defaultValue = 2

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


_WsAPRadioTspecMode_Type.__name__ = "Integer32"
_WsAPRadioTspecMode_Object = MibTableColumn
wsAPRadioTspecMode = _WsAPRadioTspecMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 12, 1, 1),
    _WsAPRadioTspecMode_Type()
)
wsAPRadioTspecMode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAPRadioTspecMode.setStatus("current")


class _WsAPRadioTspecVoiceAcmMode_Type(Integer32):
    """Custom type wsAPRadioTspecVoiceAcmMode based on Integer32"""
    defaultValue = 2

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


_WsAPRadioTspecVoiceAcmMode_Type.__name__ = "Integer32"
_WsAPRadioTspecVoiceAcmMode_Object = MibTableColumn
wsAPRadioTspecVoiceAcmMode = _WsAPRadioTspecVoiceAcmMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 12, 1, 2),
    _WsAPRadioTspecVoiceAcmMode_Type()
)
wsAPRadioTspecVoiceAcmMode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAPRadioTspecVoiceAcmMode.setStatus("current")


class _WsAPRadioTspecVideoAcmMode_Type(Integer32):
    """Custom type wsAPRadioTspecVideoAcmMode based on Integer32"""
    defaultValue = 2

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


_WsAPRadioTspecVideoAcmMode_Type.__name__ = "Integer32"
_WsAPRadioTspecVideoAcmMode_Object = MibTableColumn
wsAPRadioTspecVideoAcmMode = _WsAPRadioTspecVideoAcmMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 12, 1, 3),
    _WsAPRadioTspecVideoAcmMode_Type()
)
wsAPRadioTspecVideoAcmMode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAPRadioTspecVideoAcmMode.setStatus("current")


class _WsAPRadioTspecVoiceAcmLimit_Type(Unsigned32):
    """Custom type wsAPRadioTspecVoiceAcmLimit based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 70),
    )


_WsAPRadioTspecVoiceAcmLimit_Type.__name__ = "Unsigned32"
_WsAPRadioTspecVoiceAcmLimit_Object = MibTableColumn
wsAPRadioTspecVoiceAcmLimit = _WsAPRadioTspecVoiceAcmLimit_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 12, 1, 4),
    _WsAPRadioTspecVoiceAcmLimit_Type()
)
wsAPRadioTspecVoiceAcmLimit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAPRadioTspecVoiceAcmLimit.setStatus("current")


class _WsAPRadioTspecVideoAcmLimit_Type(Unsigned32):
    """Custom type wsAPRadioTspecVideoAcmLimit based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 70),
    )


_WsAPRadioTspecVideoAcmLimit_Type.__name__ = "Unsigned32"
_WsAPRadioTspecVideoAcmLimit_Object = MibTableColumn
wsAPRadioTspecVideoAcmLimit = _WsAPRadioTspecVideoAcmLimit_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 12, 1, 5),
    _WsAPRadioTspecVideoAcmLimit_Type()
)
wsAPRadioTspecVideoAcmLimit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAPRadioTspecVideoAcmLimit.setStatus("current")


class _WsAPRadioTspecRoamReserveLimit_Type(Unsigned32):
    """Custom type wsAPRadioTspecRoamReserveLimit based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 70),
    )


_WsAPRadioTspecRoamReserveLimit_Type.__name__ = "Unsigned32"
_WsAPRadioTspecRoamReserveLimit_Object = MibTableColumn
wsAPRadioTspecRoamReserveLimit = _WsAPRadioTspecRoamReserveLimit_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 12, 1, 6),
    _WsAPRadioTspecRoamReserveLimit_Type()
)
wsAPRadioTspecRoamReserveLimit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAPRadioTspecRoamReserveLimit.setStatus("current")


class _WsAPRadioTspecApInactivityTimeout_Type(Unsigned32):
    """Custom type wsAPRadioTspecApInactivityTimeout based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 120),
    )


_WsAPRadioTspecApInactivityTimeout_Type.__name__ = "Unsigned32"
_WsAPRadioTspecApInactivityTimeout_Object = MibTableColumn
wsAPRadioTspecApInactivityTimeout = _WsAPRadioTspecApInactivityTimeout_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 12, 1, 7),
    _WsAPRadioTspecApInactivityTimeout_Type()
)
wsAPRadioTspecApInactivityTimeout.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAPRadioTspecApInactivityTimeout.setStatus("current")


class _WsAPRadioTspecStaInactivityTimeout_Type(Unsigned32):
    """Custom type wsAPRadioTspecStaInactivityTimeout based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 120),
    )


_WsAPRadioTspecStaInactivityTimeout_Type.__name__ = "Unsigned32"
_WsAPRadioTspecStaInactivityTimeout_Object = MibTableColumn
wsAPRadioTspecStaInactivityTimeout = _WsAPRadioTspecStaInactivityTimeout_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 12, 1, 8),
    _WsAPRadioTspecStaInactivityTimeout_Type()
)
wsAPRadioTspecStaInactivityTimeout.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAPRadioTspecStaInactivityTimeout.setStatus("current")


class _WsAPRadioTspecLegacyWmmQueueMapMode_Type(Integer32):
    """Custom type wsAPRadioTspecLegacyWmmQueueMapMode based on Integer32"""
    defaultValue = 2

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


_WsAPRadioTspecLegacyWmmQueueMapMode_Type.__name__ = "Integer32"
_WsAPRadioTspecLegacyWmmQueueMapMode_Object = MibTableColumn
wsAPRadioTspecLegacyWmmQueueMapMode = _WsAPRadioTspecLegacyWmmQueueMapMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 12, 1, 9),
    _WsAPRadioTspecLegacyWmmQueueMapMode_Type()
)
wsAPRadioTspecLegacyWmmQueueMapMode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAPRadioTspecLegacyWmmQueueMapMode.setStatus("current")
_WsAPProfileRadioMCSIndexTable_Object = MibTable
wsAPProfileRadioMCSIndexTable = _WsAPProfileRadioMCSIndexTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 13)
)
if mibBuilder.loadTexts:
    wsAPProfileRadioMCSIndexTable.setStatus("obsolete")
_WsAPProfileRadioMCSIndexEntry_Object = MibTableRow
wsAPProfileRadioMCSIndexEntry = _WsAPProfileRadioMCSIndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 13, 1)
)
wsAPProfileRadioMCSIndexEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsAPProfileId"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsAPRadioInterface"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsAPRadioMCSIndexValue"),
)
if mibBuilder.loadTexts:
    wsAPProfileRadioMCSIndexEntry.setStatus("obsolete")


class _WsAPRadioMCSIndexValue_Type(Unsigned32):
    """Custom type wsAPRadioMCSIndexValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_WsAPRadioMCSIndexValue_Type.__name__ = "Unsigned32"
_WsAPRadioMCSIndexValue_Object = MibTableColumn
wsAPRadioMCSIndexValue = _WsAPRadioMCSIndexValue_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 13, 1, 1),
    _WsAPRadioMCSIndexValue_Type()
)
wsAPRadioMCSIndexValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPRadioMCSIndexValue.setStatus("obsolete")


class _WsAPRadioMCSIndexAvailable_Type(Integer32):
    """Custom type wsAPRadioMCSIndexAvailable based on Integer32"""
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


_WsAPRadioMCSIndexAvailable_Type.__name__ = "Integer32"
_WsAPRadioMCSIndexAvailable_Object = MibTableColumn
wsAPRadioMCSIndexAvailable = _WsAPRadioMCSIndexAvailable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 3, 13, 1, 2),
    _WsAPRadioMCSIndexAvailable_Type()
)
wsAPRadioMCSIndexAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPRadioMCSIndexAvailable.setStatus("obsolete")
_ApCodeDownload_ObjectIdentity = ObjectIdentity
apCodeDownload = _ApCodeDownload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 4)
)
_WsAPCodeDownloadServerIP_Type = IpAddress
_WsAPCodeDownloadServerIP_Object = MibScalar
wsAPCodeDownloadServerIP = _WsAPCodeDownloadServerIP_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 4, 1),
    _WsAPCodeDownloadServerIP_Type()
)
wsAPCodeDownloadServerIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPCodeDownloadServerIP.setStatus("current")
_WsAPImageTypeFileTable_Object = MibTable
wsAPImageTypeFileTable = _WsAPImageTypeFileTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 4, 2)
)
if mibBuilder.loadTexts:
    wsAPImageTypeFileTable.setStatus("current")
_WsAPImageTypeFileEntry_Object = MibTableRow
wsAPImageTypeFileEntry = _WsAPImageTypeFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 4, 2, 1)
)
wsAPImageTypeFileEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsAPImageTypeID"),
)
if mibBuilder.loadTexts:
    wsAPImageTypeFileEntry.setStatus("current")


class _WsAPImageFilePath_Type(DisplayString):
    """Custom type wsAPImageFilePath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 96),
    )


_WsAPImageFilePath_Type.__name__ = "DisplayString"
_WsAPImageFilePath_Object = MibTableColumn
wsAPImageFilePath = _WsAPImageFilePath_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 4, 2, 1, 1),
    _WsAPImageFilePath_Type()
)
wsAPImageFilePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPImageFilePath.setStatus("current")


class _WsAPImageFileName_Type(DisplayString):
    """Custom type wsAPImageFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WsAPImageFileName_Type.__name__ = "DisplayString"
_WsAPImageFileName_Object = MibTableColumn
wsAPImageFileName = _WsAPImageFileName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 4, 2, 1, 2),
    _WsAPImageFileName_Type()
)
wsAPImageFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPImageFileName.setStatus("current")
_WsAPCodeDownloadMACAddress_Type = MacAddress
_WsAPCodeDownloadMACAddress_Object = MibScalar
wsAPCodeDownloadMACAddress = _WsAPCodeDownloadMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 4, 3),
    _WsAPCodeDownloadMACAddress_Type()
)
wsAPCodeDownloadMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPCodeDownloadMACAddress.setStatus("current")


class _WsAPCodeDownloadGroupSize_Type(Integer32):
    """Custom type wsAPCodeDownloadGroupSize based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_WsAPCodeDownloadGroupSize_Type.__name__ = "Integer32"
_WsAPCodeDownloadGroupSize_Object = MibScalar
wsAPCodeDownloadGroupSize = _WsAPCodeDownloadGroupSize_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 4, 4),
    _WsAPCodeDownloadGroupSize_Type()
)
wsAPCodeDownloadGroupSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPCodeDownloadGroupSize.setStatus("current")


class _WsAPCodeDownloadImageType_Type(Integer32):
    """Custom type wsAPCodeDownloadImageType based on Integer32"""
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
        *(("tq3600", 1),
          ("image2", 2),
          ("image3", 3),
          ("tq2450", 4),
          ("tq4400", 5),
          ("tq4600", 6),
          ("tq3200", 7),
          ("tq3400", 8),
          ("all", 9))
    )


_WsAPCodeDownloadImageType_Type.__name__ = "Integer32"
_WsAPCodeDownloadImageType_Object = MibScalar
wsAPCodeDownloadImageType = _WsAPCodeDownloadImageType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 4, 5),
    _WsAPCodeDownloadImageType_Type()
)
wsAPCodeDownloadImageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPCodeDownloadImageType.setStatus("current")


class _WsAPCodeDownloadStatus_Type(Integer32):
    """Custom type wsAPCodeDownloadStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("not-started", 1),
          ("requested", 2),
          ("code-transfer-in-progress", 3),
          ("aborted", 4),
          ("nvram-update-in-progress", 5),
          ("success", 6),
          ("failure", 7))
    )


_WsAPCodeDownloadStatus_Type.__name__ = "Integer32"
_WsAPCodeDownloadStatus_Object = MibScalar
wsAPCodeDownloadStatus = _WsAPCodeDownloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 4, 6),
    _WsAPCodeDownloadStatus_Type()
)
wsAPCodeDownloadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPCodeDownloadStatus.setStatus("current")


class _WsAPCodeDownloadTotalCount_Type(Integer32):
    """Custom type wsAPCodeDownloadTotalCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_WsAPCodeDownloadTotalCount_Type.__name__ = "Integer32"
_WsAPCodeDownloadTotalCount_Object = MibScalar
wsAPCodeDownloadTotalCount = _WsAPCodeDownloadTotalCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 4, 7),
    _WsAPCodeDownloadTotalCount_Type()
)
wsAPCodeDownloadTotalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPCodeDownloadTotalCount.setStatus("current")


class _WsAPCodeDownloadSuccessCount_Type(Integer32):
    """Custom type wsAPCodeDownloadSuccessCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48),
    )


_WsAPCodeDownloadSuccessCount_Type.__name__ = "Integer32"
_WsAPCodeDownloadSuccessCount_Object = MibScalar
wsAPCodeDownloadSuccessCount = _WsAPCodeDownloadSuccessCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 4, 8),
    _WsAPCodeDownloadSuccessCount_Type()
)
wsAPCodeDownloadSuccessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPCodeDownloadSuccessCount.setStatus("current")


class _WsAPCodeDownloadFailureCount_Type(Integer32):
    """Custom type wsAPCodeDownloadFailureCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48),
    )


_WsAPCodeDownloadFailureCount_Type.__name__ = "Integer32"
_WsAPCodeDownloadFailureCount_Object = MibScalar
wsAPCodeDownloadFailureCount = _WsAPCodeDownloadFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 4, 9),
    _WsAPCodeDownloadFailureCount_Type()
)
wsAPCodeDownloadFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPCodeDownloadFailureCount.setStatus("current")


class _WsAPCodeDownloadAbortCount_Type(Integer32):
    """Custom type wsAPCodeDownloadAbortCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48),
    )


_WsAPCodeDownloadAbortCount_Type.__name__ = "Integer32"
_WsAPCodeDownloadAbortCount_Object = MibScalar
wsAPCodeDownloadAbortCount = _WsAPCodeDownloadAbortCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 4, 10),
    _WsAPCodeDownloadAbortCount_Type()
)
wsAPCodeDownloadAbortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPCodeDownloadAbortCount.setStatus("current")


class _WsAPCodeDownloadAbort_Type(Integer32):
    """Custom type wsAPCodeDownloadAbort based on Integer32"""
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


_WsAPCodeDownloadAbort_Type.__name__ = "Integer32"
_WsAPCodeDownloadAbort_Object = MibScalar
wsAPCodeDownloadAbort = _WsAPCodeDownloadAbort_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 4, 11),
    _WsAPCodeDownloadAbort_Type()
)
wsAPCodeDownloadAbort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPCodeDownloadAbort.setStatus("current")
_RfManagement_ObjectIdentity = ObjectIdentity
rfManagement = _RfManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5)
)
_WsChannelPlanTable_Object = MibTable
wsChannelPlanTable = _WsChannelPlanTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 1)
)
if mibBuilder.loadTexts:
    wsChannelPlanTable.setStatus("current")
_WsChannelPlanEntry_Object = MibTableRow
wsChannelPlanEntry = _WsChannelPlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 1, 1)
)
wsChannelPlanEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsChannelPlan"),
)
if mibBuilder.loadTexts:
    wsChannelPlanEntry.setStatus("current")


class _WsChannelPlan_Type(Integer32):
    """Custom type wsChannelPlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ieee802dot11an", 1),
          ("ieee802dot11bORgn", 2))
    )


_WsChannelPlan_Type.__name__ = "Integer32"
_WsChannelPlan_Object = MibTableColumn
wsChannelPlan = _WsChannelPlan_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 1, 1, 1),
    _WsChannelPlan_Type()
)
wsChannelPlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsChannelPlan.setStatus("current")


class _WsChannelPlanMode_Type(Integer32):
    """Custom type wsChannelPlanMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("interval", 2),
          ("time", 3))
    )


_WsChannelPlanMode_Type.__name__ = "Integer32"
_WsChannelPlanMode_Object = MibTableColumn
wsChannelPlanMode = _WsChannelPlanMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 1, 1, 2),
    _WsChannelPlanMode_Type()
)
wsChannelPlanMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsChannelPlanMode.setStatus("current")


class _WsChannelPlanInterval_Type(Integer32):
    """Custom type wsChannelPlanInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1440),
    )


_WsChannelPlanInterval_Type.__name__ = "Integer32"
_WsChannelPlanInterval_Object = MibTableColumn
wsChannelPlanInterval = _WsChannelPlanInterval_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 1, 1, 3),
    _WsChannelPlanInterval_Type()
)
wsChannelPlanInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsChannelPlanInterval.setStatus("current")


class _WsChannelPlanTime_Type(Integer32):
    """Custom type wsChannelPlanTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_WsChannelPlanTime_Type.__name__ = "Integer32"
_WsChannelPlanTime_Object = MibTableColumn
wsChannelPlanTime = _WsChannelPlanTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 1, 1, 4),
    _WsChannelPlanTime_Type()
)
wsChannelPlanTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsChannelPlanTime.setStatus("current")


class _WsChannelPlanHistoryDepth_Type(Integer32):
    """Custom type wsChannelPlanHistoryDepth based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_WsChannelPlanHistoryDepth_Type.__name__ = "Integer32"
_WsChannelPlanHistoryDepth_Object = MibTableColumn
wsChannelPlanHistoryDepth = _WsChannelPlanHistoryDepth_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 1, 1, 5),
    _WsChannelPlanHistoryDepth_Type()
)
wsChannelPlanHistoryDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsChannelPlanHistoryDepth.setStatus("obsolete")


class _WsChannelPlanOperatingStatus_Type(Integer32):
    """Custom type wsChannelPlanOperatingStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inActive", 2))
    )


_WsChannelPlanOperatingStatus_Type.__name__ = "Integer32"
_WsChannelPlanOperatingStatus_Object = MibTableColumn
wsChannelPlanOperatingStatus = _WsChannelPlanOperatingStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 1, 1, 6),
    _WsChannelPlanOperatingStatus_Type()
)
wsChannelPlanOperatingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsChannelPlanOperatingStatus.setStatus("current")


class _WsChannelPlanLastIterationStatus_Type(Integer32):
    """Custom type wsChannelPlanLastIterationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_WsChannelPlanLastIterationStatus_Type.__name__ = "Integer32"
_WsChannelPlanLastIterationStatus_Object = MibTableColumn
wsChannelPlanLastIterationStatus = _WsChannelPlanLastIterationStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 1, 1, 7),
    _WsChannelPlanLastIterationStatus_Type()
)
wsChannelPlanLastIterationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsChannelPlanLastIterationStatus.setStatus("obsolete")


class _WsChannelPlanManualAction_Type(Integer32):
    """Custom type wsChannelPlanManualAction based on Integer32"""
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
          ("start", 2),
          ("abort", 3),
          ("clear", 4))
    )


_WsChannelPlanManualAction_Type.__name__ = "Integer32"
_WsChannelPlanManualAction_Object = MibTableColumn
wsChannelPlanManualAction = _WsChannelPlanManualAction_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 1, 1, 8),
    _WsChannelPlanManualAction_Type()
)
wsChannelPlanManualAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsChannelPlanManualAction.setStatus("current")


class _WsChannelPlanManualStatus_Type(Integer32):
    """Custom type wsChannelPlanManualStatus based on Integer32"""
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
        *(("none", 1),
          ("algorithm-in-progress", 2),
          ("algorithm-complete", 3),
          ("apply-in-process", 4),
          ("apply-complete", 5))
    )


_WsChannelPlanManualStatus_Type.__name__ = "Integer32"
_WsChannelPlanManualStatus_Object = MibTableColumn
wsChannelPlanManualStatus = _WsChannelPlanManualStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 1, 1, 9),
    _WsChannelPlanManualStatus_Type()
)
wsChannelPlanManualStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsChannelPlanManualStatus.setStatus("obsolete")
_WsChannelPlanLastAlgorithmTime_Type = DisplayString
_WsChannelPlanLastAlgorithmTime_Object = MibTableColumn
wsChannelPlanLastAlgorithmTime = _WsChannelPlanLastAlgorithmTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 1, 1, 10),
    _WsChannelPlanLastAlgorithmTime_Type()
)
wsChannelPlanLastAlgorithmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsChannelPlanLastAlgorithmTime.setStatus("current")


class _WsChannelPlanChangeThreshold_Type(Integer32):
    """Custom type wsChannelPlanChangeThreshold based on Integer32"""
    defaultValue = -82

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-99, -1),
    )


_WsChannelPlanChangeThreshold_Type.__name__ = "Integer32"
_WsChannelPlanChangeThreshold_Object = MibTableColumn
wsChannelPlanChangeThreshold = _WsChannelPlanChangeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 1, 1, 11),
    _WsChannelPlanChangeThreshold_Type()
)
wsChannelPlanChangeThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsChannelPlanChangeThreshold.setStatus("current")


class _WsChannelPlanIgnoreUnamangedAPs_Type(Integer32):
    """Custom type wsChannelPlanIgnoreUnamangedAPs based on Integer32"""
    defaultValue = 1

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


_WsChannelPlanIgnoreUnamangedAPs_Type.__name__ = "Integer32"
_WsChannelPlanIgnoreUnamangedAPs_Object = MibTableColumn
wsChannelPlanIgnoreUnamangedAPs = _WsChannelPlanIgnoreUnamangedAPs_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 1, 1, 12),
    _WsChannelPlanIgnoreUnamangedAPs_Type()
)
wsChannelPlanIgnoreUnamangedAPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsChannelPlanIgnoreUnamangedAPs.setStatus("current")


class _WsChannelPlanNumOfRadios_Type(Integer32):
    """Custom type wsChannelPlanNumOfRadios based on Integer32"""
    defaultValue = 0


_WsChannelPlanNumOfRadios_Type.__name__ = "Integer32"
_WsChannelPlanNumOfRadios_Object = MibTableColumn
wsChannelPlanNumOfRadios = _WsChannelPlanNumOfRadios_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 1, 1, 13),
    _WsChannelPlanNumOfRadios_Type()
)
wsChannelPlanNumOfRadios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsChannelPlanNumOfRadios.setStatus("current")


class _WsChannelPlanNumOfRadiosAnalysed_Type(Integer32):
    """Custom type wsChannelPlanNumOfRadiosAnalysed based on Integer32"""
    defaultValue = 0


_WsChannelPlanNumOfRadiosAnalysed_Type.__name__ = "Integer32"
_WsChannelPlanNumOfRadiosAnalysed_Object = MibTableColumn
wsChannelPlanNumOfRadiosAnalysed = _WsChannelPlanNumOfRadiosAnalysed_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 1, 1, 14),
    _WsChannelPlanNumOfRadiosAnalysed_Type()
)
wsChannelPlanNumOfRadiosAnalysed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsChannelPlanNumOfRadiosAnalysed.setStatus("current")


class _WsChannelPlanNumOfRadiosScanned_Type(Integer32):
    """Custom type wsChannelPlanNumOfRadiosScanned based on Integer32"""
    defaultValue = 0


_WsChannelPlanNumOfRadiosScanned_Type.__name__ = "Integer32"
_WsChannelPlanNumOfRadiosScanned_Object = MibTableColumn
wsChannelPlanNumOfRadiosScanned = _WsChannelPlanNumOfRadiosScanned_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 1, 1, 15),
    _WsChannelPlanNumOfRadiosScanned_Type()
)
wsChannelPlanNumOfRadiosScanned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsChannelPlanNumOfRadiosScanned.setStatus("current")


class _WsChannelPlanNumOfRadiosChanged_Type(Integer32):
    """Custom type wsChannelPlanNumOfRadiosChanged based on Integer32"""
    defaultValue = 0


_WsChannelPlanNumOfRadiosChanged_Type.__name__ = "Integer32"
_WsChannelPlanNumOfRadiosChanged_Object = MibTableColumn
wsChannelPlanNumOfRadiosChanged = _WsChannelPlanNumOfRadiosChanged_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 1, 1, 16),
    _WsChannelPlanNumOfRadiosChanged_Type()
)
wsChannelPlanNumOfRadiosChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsChannelPlanNumOfRadiosChanged.setStatus("current")


class _WsChannelPlanNumOfRadiosChangedToOrigChannel_Type(Integer32):
    """Custom type wsChannelPlanNumOfRadiosChangedToOrigChannel based on Integer32"""
    defaultValue = 0


_WsChannelPlanNumOfRadiosChangedToOrigChannel_Type.__name__ = "Integer32"
_WsChannelPlanNumOfRadiosChangedToOrigChannel_Object = MibTableColumn
wsChannelPlanNumOfRadiosChangedToOrigChannel = _WsChannelPlanNumOfRadiosChangedToOrigChannel_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 1, 1, 17),
    _WsChannelPlanNumOfRadiosChangedToOrigChannel_Type()
)
wsChannelPlanNumOfRadiosChangedToOrigChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsChannelPlanNumOfRadiosChangedToOrigChannel.setStatus("current")
_WsChannelPlanEstimatedTimeOfCompletion_Type = DisplayString
_WsChannelPlanEstimatedTimeOfCompletion_Object = MibTableColumn
wsChannelPlanEstimatedTimeOfCompletion = _WsChannelPlanEstimatedTimeOfCompletion_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 1, 1, 18),
    _WsChannelPlanEstimatedTimeOfCompletion_Type()
)
wsChannelPlanEstimatedTimeOfCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsChannelPlanEstimatedTimeOfCompletion.setStatus("current")


class _WsChannelPlanPercentageComplete_Type(Integer32):
    """Custom type wsChannelPlanPercentageComplete based on Integer32"""
    defaultValue = 0


_WsChannelPlanPercentageComplete_Type.__name__ = "Integer32"
_WsChannelPlanPercentageComplete_Object = MibTableColumn
wsChannelPlanPercentageComplete = _WsChannelPlanPercentageComplete_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 1, 1, 19),
    _WsChannelPlanPercentageComplete_Type()
)
wsChannelPlanPercentageComplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsChannelPlanPercentageComplete.setStatus("current")


class _WsChannelPlanChangeThresholdAdj_Type(Integer32):
    """Custom type wsChannelPlanChangeThresholdAdj based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_WsChannelPlanChangeThresholdAdj_Type.__name__ = "Integer32"
_WsChannelPlanChangeThresholdAdj_Object = MibTableColumn
wsChannelPlanChangeThresholdAdj = _WsChannelPlanChangeThresholdAdj_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 1, 1, 20),
    _WsChannelPlanChangeThresholdAdj_Type()
)
wsChannelPlanChangeThresholdAdj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsChannelPlanChangeThresholdAdj.setStatus("current")


class _WsChannelPlanManagedAPFailureInterval_Type(Integer32):
    """Custom type wsChannelPlanManagedAPFailureInterval based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 600),
    )


_WsChannelPlanManagedAPFailureInterval_Type.__name__ = "Integer32"
_WsChannelPlanManagedAPFailureInterval_Object = MibTableColumn
wsChannelPlanManagedAPFailureInterval = _WsChannelPlanManagedAPFailureInterval_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 1, 1, 21),
    _WsChannelPlanManagedAPFailureInterval_Type()
)
wsChannelPlanManagedAPFailureInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsChannelPlanManagedAPFailureInterval.setStatus("current")


class _WsChannelPlanRunOnManagedApFailure_Type(Integer32):
    """Custom type wsChannelPlanRunOnManagedApFailure based on Integer32"""
    defaultValue = 2

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


_WsChannelPlanRunOnManagedApFailure_Type.__name__ = "Integer32"
_WsChannelPlanRunOnManagedApFailure_Object = MibTableColumn
wsChannelPlanRunOnManagedApFailure = _WsChannelPlanRunOnManagedApFailure_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 1, 1, 22),
    _WsChannelPlanRunOnManagedApFailure_Type()
)
wsChannelPlanRunOnManagedApFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsChannelPlanRunOnManagedApFailure.setStatus("current")
_WsChannelPlanHistoryTable_Object = MibTable
wsChannelPlanHistoryTable = _WsChannelPlanHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 2)
)
if mibBuilder.loadTexts:
    wsChannelPlanHistoryTable.setStatus("obsolete")
_WsChannelPlanHistoryEntry_Object = MibTableRow
wsChannelPlanHistoryEntry = _WsChannelPlanHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 2, 1)
)
wsChannelPlanHistoryEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsChannelPlanHistory"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsChannelPlanAPMacAddress"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsChannelPlanAPRadioInterface"),
)
if mibBuilder.loadTexts:
    wsChannelPlanHistoryEntry.setStatus("obsolete")


class _WsChannelPlanHistory_Type(Integer32):
    """Custom type wsChannelPlanHistory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ieee802dot11an", 1),
          ("ieee802dot11bORgn", 2))
    )


_WsChannelPlanHistory_Type.__name__ = "Integer32"
_WsChannelPlanHistory_Object = MibTableColumn
wsChannelPlanHistory = _WsChannelPlanHistory_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 2, 1, 1),
    _WsChannelPlanHistory_Type()
)
wsChannelPlanHistory.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsChannelPlanHistory.setStatus("obsolete")
_WsChannelPlanAPMacAddress_Type = MacAddress
_WsChannelPlanAPMacAddress_Object = MibTableColumn
wsChannelPlanAPMacAddress = _WsChannelPlanAPMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 2, 1, 2),
    _WsChannelPlanAPMacAddress_Type()
)
wsChannelPlanAPMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsChannelPlanAPMacAddress.setStatus("obsolete")


class _WsChannelPlanAPRadioInterface_Type(Integer32):
    """Custom type wsChannelPlanAPRadioInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WsChannelPlanAPRadioInterface_Type.__name__ = "Integer32"
_WsChannelPlanAPRadioInterface_Object = MibTableColumn
wsChannelPlanAPRadioInterface = _WsChannelPlanAPRadioInterface_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 2, 1, 3),
    _WsChannelPlanAPRadioInterface_Type()
)
wsChannelPlanAPRadioInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsChannelPlanAPRadioInterface.setStatus("obsolete")


class _WsChannelPlanAPLocation_Type(DisplayString):
    """Custom type wsChannelPlanAPLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WsChannelPlanAPLocation_Type.__name__ = "DisplayString"
_WsChannelPlanAPLocation_Object = MibTableColumn
wsChannelPlanAPLocation = _WsChannelPlanAPLocation_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 2, 1, 4),
    _WsChannelPlanAPLocation_Type()
)
wsChannelPlanAPLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsChannelPlanAPLocation.setStatus("obsolete")


class _WsChannelPlanAPHistoryIteration_Type(Integer32):
    """Custom type wsChannelPlanAPHistoryIteration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_WsChannelPlanAPHistoryIteration_Type.__name__ = "Integer32"
_WsChannelPlanAPHistoryIteration_Object = MibTableColumn
wsChannelPlanAPHistoryIteration = _WsChannelPlanAPHistoryIteration_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 2, 1, 5),
    _WsChannelPlanAPHistoryIteration_Type()
)
wsChannelPlanAPHistoryIteration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsChannelPlanAPHistoryIteration.setStatus("obsolete")


class _WsChannelPlanAPChannel_Type(Integer32):
    """Custom type wsChannelPlanAPChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(6, 6),
        ValueRangeConstraint(11, 11),
    )


_WsChannelPlanAPChannel_Type.__name__ = "Integer32"
_WsChannelPlanAPChannel_Object = MibTableColumn
wsChannelPlanAPChannel = _WsChannelPlanAPChannel_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 2, 1, 6),
    _WsChannelPlanAPChannel_Type()
)
wsChannelPlanAPChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsChannelPlanAPChannel.setStatus("obsolete")
_WsChannelPlanManualProposedAdjustmentTable_Object = MibTable
wsChannelPlanManualProposedAdjustmentTable = _WsChannelPlanManualProposedAdjustmentTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 3)
)
if mibBuilder.loadTexts:
    wsChannelPlanManualProposedAdjustmentTable.setStatus("obsolete")
_WsChannelPlanManualProposedAdjustmentEntry_Object = MibTableRow
wsChannelPlanManualProposedAdjustmentEntry = _WsChannelPlanManualProposedAdjustmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 3, 1)
)
wsChannelPlanManualProposedAdjustmentEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsChannelPlanManual"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsChannelPlanManualMacAddress"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsChannelPlanManualAPRadioInterface"),
)
if mibBuilder.loadTexts:
    wsChannelPlanManualProposedAdjustmentEntry.setStatus("obsolete")


class _WsChannelPlanManual_Type(Integer32):
    """Custom type wsChannelPlanManual based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ieee802dot11an", 1),
          ("ieee802dot11bORgn", 2))
    )


_WsChannelPlanManual_Type.__name__ = "Integer32"
_WsChannelPlanManual_Object = MibTableColumn
wsChannelPlanManual = _WsChannelPlanManual_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 3, 1, 1),
    _WsChannelPlanManual_Type()
)
wsChannelPlanManual.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsChannelPlanManual.setStatus("obsolete")
_WsChannelPlanManualMacAddress_Type = MacAddress
_WsChannelPlanManualMacAddress_Object = MibTableColumn
wsChannelPlanManualMacAddress = _WsChannelPlanManualMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 3, 1, 2),
    _WsChannelPlanManualMacAddress_Type()
)
wsChannelPlanManualMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsChannelPlanManualMacAddress.setStatus("obsolete")


class _WsChannelPlanManualAPRadioInterface_Type(Integer32):
    """Custom type wsChannelPlanManualAPRadioInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WsChannelPlanManualAPRadioInterface_Type.__name__ = "Integer32"
_WsChannelPlanManualAPRadioInterface_Object = MibTableColumn
wsChannelPlanManualAPRadioInterface = _WsChannelPlanManualAPRadioInterface_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 3, 1, 3),
    _WsChannelPlanManualAPRadioInterface_Type()
)
wsChannelPlanManualAPRadioInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsChannelPlanManualAPRadioInterface.setStatus("obsolete")


class _WsChannelPlanManualCurrentChannel_Type(Integer32):
    """Custom type wsChannelPlanManualCurrentChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 13),
        ValueRangeConstraint(36, 36),
        ValueRangeConstraint(40, 40),
        ValueRangeConstraint(44, 44),
        ValueRangeConstraint(48, 48),
        ValueRangeConstraint(52, 52),
        ValueRangeConstraint(56, 56),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(64, 64),
    )


_WsChannelPlanManualCurrentChannel_Type.__name__ = "Integer32"
_WsChannelPlanManualCurrentChannel_Object = MibTableColumn
wsChannelPlanManualCurrentChannel = _WsChannelPlanManualCurrentChannel_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 3, 1, 4),
    _WsChannelPlanManualCurrentChannel_Type()
)
wsChannelPlanManualCurrentChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsChannelPlanManualCurrentChannel.setStatus("obsolete")


class _WsChannelPlanManualNewChannel_Type(Integer32):
    """Custom type wsChannelPlanManualNewChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 13),
        ValueRangeConstraint(36, 36),
        ValueRangeConstraint(40, 40),
        ValueRangeConstraint(44, 44),
        ValueRangeConstraint(48, 48),
        ValueRangeConstraint(52, 52),
        ValueRangeConstraint(56, 56),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(64, 64),
    )


_WsChannelPlanManualNewChannel_Type.__name__ = "Integer32"
_WsChannelPlanManualNewChannel_Object = MibTableColumn
wsChannelPlanManualNewChannel = _WsChannelPlanManualNewChannel_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 3, 1, 5),
    _WsChannelPlanManualNewChannel_Type()
)
wsChannelPlanManualNewChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsChannelPlanManualNewChannel.setStatus("obsolete")


class _WsPowerAdjustmentMode_Type(Integer32):
    """Custom type wsPowerAdjustmentMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("interval", 2))
    )


_WsPowerAdjustmentMode_Type.__name__ = "Integer32"
_WsPowerAdjustmentMode_Object = MibScalar
wsPowerAdjustmentMode = _WsPowerAdjustmentMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 4),
    _WsPowerAdjustmentMode_Type()
)
wsPowerAdjustmentMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPowerAdjustmentMode.setStatus("current")


class _WsPowerAdjustmentStrength_Type(Integer32):
    """Custom type wsPowerAdjustmentStrength based on Integer32"""
    defaultValue = -85

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-99, -1),
    )


_WsPowerAdjustmentStrength_Type.__name__ = "Integer32"
_WsPowerAdjustmentStrength_Object = MibScalar
wsPowerAdjustmentStrength = _WsPowerAdjustmentStrength_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 5),
    _WsPowerAdjustmentStrength_Type()
)
wsPowerAdjustmentStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPowerAdjustmentStrength.setStatus("current")


class _WsPowerManualProposedAdjustmentAction_Type(Integer32):
    """Custom type wsPowerManualProposedAdjustmentAction based on Integer32"""
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
          ("start", 2),
          ("apply", 3),
          ("clear", 4))
    )


_WsPowerManualProposedAdjustmentAction_Type.__name__ = "Integer32"
_WsPowerManualProposedAdjustmentAction_Object = MibScalar
wsPowerManualProposedAdjustmentAction = _WsPowerManualProposedAdjustmentAction_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 6),
    _WsPowerManualProposedAdjustmentAction_Type()
)
wsPowerManualProposedAdjustmentAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPowerManualProposedAdjustmentAction.setStatus("current")


class _WsManualPowerAdjustmentStatus_Type(Integer32):
    """Custom type wsManualPowerAdjustmentStatus based on Integer32"""
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
        *(("none", 1),
          ("algorithm-in-progress", 2),
          ("algorithm-complete", 3),
          ("apply-in-process", 4),
          ("apply-complete", 5))
    )


_WsManualPowerAdjustmentStatus_Type.__name__ = "Integer32"
_WsManualPowerAdjustmentStatus_Object = MibScalar
wsManualPowerAdjustmentStatus = _WsManualPowerAdjustmentStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 7),
    _WsManualPowerAdjustmentStatus_Type()
)
wsManualPowerAdjustmentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManualPowerAdjustmentStatus.setStatus("obsolete")
_WsPowerManualProposedAdjustmentTable_Object = MibTable
wsPowerManualProposedAdjustmentTable = _WsPowerManualProposedAdjustmentTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 8)
)
if mibBuilder.loadTexts:
    wsPowerManualProposedAdjustmentTable.setStatus("obsolete")
_WsPowerManualProposedAdjustmentEntry_Object = MibTableRow
wsPowerManualProposedAdjustmentEntry = _WsPowerManualProposedAdjustmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 8, 1)
)
wsPowerManualProposedAdjustmentEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsPowerManualProposedAdjustmentAPMacAddress"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsPowerManualProposedAdjustmentAPRadioInterface"),
)
if mibBuilder.loadTexts:
    wsPowerManualProposedAdjustmentEntry.setStatus("obsolete")
_WsPowerManualProposedAdjustmentAPMacAddress_Type = MacAddress
_WsPowerManualProposedAdjustmentAPMacAddress_Object = MibTableColumn
wsPowerManualProposedAdjustmentAPMacAddress = _WsPowerManualProposedAdjustmentAPMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 8, 1, 1),
    _WsPowerManualProposedAdjustmentAPMacAddress_Type()
)
wsPowerManualProposedAdjustmentAPMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsPowerManualProposedAdjustmentAPMacAddress.setStatus("obsolete")


class _WsPowerManualProposedAdjustmentAPRadioInterface_Type(Integer32):
    """Custom type wsPowerManualProposedAdjustmentAPRadioInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WsPowerManualProposedAdjustmentAPRadioInterface_Type.__name__ = "Integer32"
_WsPowerManualProposedAdjustmentAPRadioInterface_Object = MibTableColumn
wsPowerManualProposedAdjustmentAPRadioInterface = _WsPowerManualProposedAdjustmentAPRadioInterface_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 8, 1, 2),
    _WsPowerManualProposedAdjustmentAPRadioInterface_Type()
)
wsPowerManualProposedAdjustmentAPRadioInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsPowerManualProposedAdjustmentAPRadioInterface.setStatus("obsolete")


class _WsPowerManualProposedAdjustmentAPCurrentTxPower_Type(Integer32):
    """Custom type wsPowerManualProposedAdjustmentAPCurrentTxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WsPowerManualProposedAdjustmentAPCurrentTxPower_Type.__name__ = "Integer32"
_WsPowerManualProposedAdjustmentAPCurrentTxPower_Object = MibTableColumn
wsPowerManualProposedAdjustmentAPCurrentTxPower = _WsPowerManualProposedAdjustmentAPCurrentTxPower_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 8, 1, 3),
    _WsPowerManualProposedAdjustmentAPCurrentTxPower_Type()
)
wsPowerManualProposedAdjustmentAPCurrentTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPowerManualProposedAdjustmentAPCurrentTxPower.setStatus("obsolete")


class _WsPowerManualProposedAdjustmentAPNewTxPower_Type(Integer32):
    """Custom type wsPowerManualProposedAdjustmentAPNewTxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WsPowerManualProposedAdjustmentAPNewTxPower_Type.__name__ = "Integer32"
_WsPowerManualProposedAdjustmentAPNewTxPower_Object = MibTableColumn
wsPowerManualProposedAdjustmentAPNewTxPower = _WsPowerManualProposedAdjustmentAPNewTxPower_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 8, 1, 4),
    _WsPowerManualProposedAdjustmentAPNewTxPower_Type()
)
wsPowerManualProposedAdjustmentAPNewTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPowerManualProposedAdjustmentAPNewTxPower.setStatus("obsolete")


class _WsPowerPlanOperatingStatus_Type(Integer32):
    """Custom type wsPowerPlanOperatingStatus based on Integer32"""
    defaultValue = 0

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
        *(("inactive", 0),
          ("gatheringNbrData", 1),
          ("changingPower", 2),
          ("powerPlanComplete", 3))
    )


_WsPowerPlanOperatingStatus_Type.__name__ = "Integer32"
_WsPowerPlanOperatingStatus_Object = MibScalar
wsPowerPlanOperatingStatus = _WsPowerPlanOperatingStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 9),
    _WsPowerPlanOperatingStatus_Type()
)
wsPowerPlanOperatingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPowerPlanOperatingStatus.setStatus("current")


class _WsPowerPlanAvgNumInterferingAPs_Type(Integer32):
    """Custom type wsPowerPlanAvgNumInterferingAPs based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_WsPowerPlanAvgNumInterferingAPs_Type.__name__ = "Integer32"
_WsPowerPlanAvgNumInterferingAPs_Object = MibScalar
wsPowerPlanAvgNumInterferingAPs = _WsPowerPlanAvgNumInterferingAPs_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 10),
    _WsPowerPlanAvgNumInterferingAPs_Type()
)
wsPowerPlanAvgNumInterferingAPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPowerPlanAvgNumInterferingAPs.setStatus("current")


class _WsPowerPlanAvgNumInterferingVAPs_Type(Integer32):
    """Custom type wsPowerPlanAvgNumInterferingVAPs based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_WsPowerPlanAvgNumInterferingVAPs_Type.__name__ = "Integer32"
_WsPowerPlanAvgNumInterferingVAPs_Object = MibScalar
wsPowerPlanAvgNumInterferingVAPs = _WsPowerPlanAvgNumInterferingVAPs_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 11),
    _WsPowerPlanAvgNumInterferingVAPs_Type()
)
wsPowerPlanAvgNumInterferingVAPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPowerPlanAvgNumInterferingVAPs.setStatus("current")


class _WsPowerPlanAPNumOpRadios_Type(Integer32):
    """Custom type wsPowerPlanAPNumOpRadios based on Integer32"""
    defaultValue = 0


_WsPowerPlanAPNumOpRadios_Type.__name__ = "Integer32"
_WsPowerPlanAPNumOpRadios_Object = MibScalar
wsPowerPlanAPNumOpRadios = _WsPowerPlanAPNumOpRadios_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 12),
    _WsPowerPlanAPNumOpRadios_Type()
)
wsPowerPlanAPNumOpRadios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPowerPlanAPNumOpRadios.setStatus("current")


class _WsPowerPlanAPNumPwrCycles_Type(Integer32):
    """Custom type wsPowerPlanAPNumPwrCycles based on Integer32"""
    defaultValue = 0


_WsPowerPlanAPNumPwrCycles_Type.__name__ = "Integer32"
_WsPowerPlanAPNumPwrCycles_Object = MibScalar
wsPowerPlanAPNumPwrCycles = _WsPowerPlanAPNumPwrCycles_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 13),
    _WsPowerPlanAPNumPwrCycles_Type()
)
wsPowerPlanAPNumPwrCycles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPowerPlanAPNumPwrCycles.setStatus("current")


class _WsPowerPlanGlobalNumPwrChanges_Type(Integer32):
    """Custom type wsPowerPlanGlobalNumPwrChanges based on Integer32"""
    defaultValue = 0


_WsPowerPlanGlobalNumPwrChanges_Type.__name__ = "Integer32"
_WsPowerPlanGlobalNumPwrChanges_Object = MibScalar
wsPowerPlanGlobalNumPwrChanges = _WsPowerPlanGlobalNumPwrChanges_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 14),
    _WsPowerPlanGlobalNumPwrChanges_Type()
)
wsPowerPlanGlobalNumPwrChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPowerPlanGlobalNumPwrChanges.setStatus("current")


class _WsPowerPlanGlobalNumPwrInc_Type(Integer32):
    """Custom type wsPowerPlanGlobalNumPwrInc based on Integer32"""
    defaultValue = 0


_WsPowerPlanGlobalNumPwrInc_Type.__name__ = "Integer32"
_WsPowerPlanGlobalNumPwrInc_Object = MibScalar
wsPowerPlanGlobalNumPwrInc = _WsPowerPlanGlobalNumPwrInc_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 15),
    _WsPowerPlanGlobalNumPwrInc_Type()
)
wsPowerPlanGlobalNumPwrInc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPowerPlanGlobalNumPwrInc.setStatus("current")


class _WsPowerPlanGlobalNumPwrDec_Type(Integer32):
    """Custom type wsPowerPlanGlobalNumPwrDec based on Integer32"""
    defaultValue = 0


_WsPowerPlanGlobalNumPwrDec_Type.__name__ = "Integer32"
_WsPowerPlanGlobalNumPwrDec_Object = MibScalar
wsPowerPlanGlobalNumPwrDec = _WsPowerPlanGlobalNumPwrDec_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 16),
    _WsPowerPlanGlobalNumPwrDec_Type()
)
wsPowerPlanGlobalNumPwrDec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPowerPlanGlobalNumPwrDec.setStatus("current")


class _WsPowerPlanTimeSinceLastPowerPLan_Type(DisplayString):
    """Custom type wsPowerPlanTimeSinceLastPowerPLan based on DisplayString"""
    defaultValue = OctetString("Never")


_WsPowerPlanTimeSinceLastPowerPLan_Type.__name__ = "DisplayString"
_WsPowerPlanTimeSinceLastPowerPLan_Object = MibScalar
wsPowerPlanTimeSinceLastPowerPLan = _WsPowerPlanTimeSinceLastPowerPLan_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 17),
    _WsPowerPlanTimeSinceLastPowerPLan_Type()
)
wsPowerPlanTimeSinceLastPowerPLan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPowerPlanTimeSinceLastPowerPLan.setStatus("current")
_WsChannelPlanPerRadioPerBandTable_Object = MibTable
wsChannelPlanPerRadioPerBandTable = _WsChannelPlanPerRadioPerBandTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 18)
)
if mibBuilder.loadTexts:
    wsChannelPlanPerRadioPerBandTable.setStatus("current")
_WsChannelPlanPerRadioPerBandEntry_Object = MibTableRow
wsChannelPlanPerRadioPerBandEntry = _WsChannelPlanPerRadioPerBandEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 18, 1)
)
wsChannelPlanPerRadioPerBandEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsChannelPlanType"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsChannelPlanAPMacAddr"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsChannelPlanAPRadioIntf"),
)
if mibBuilder.loadTexts:
    wsChannelPlanPerRadioPerBandEntry.setStatus("current")


class _WsChannelPlanType_Type(Integer32):
    """Custom type wsChannelPlanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ieee802dot11an", 1),
          ("ieee802dot11bORgn", 2))
    )


_WsChannelPlanType_Type.__name__ = "Integer32"
_WsChannelPlanType_Object = MibTableColumn
wsChannelPlanType = _WsChannelPlanType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 18, 1, 1),
    _WsChannelPlanType_Type()
)
wsChannelPlanType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsChannelPlanType.setStatus("current")
_WsChannelPlanAPMacAddr_Type = MacAddress
_WsChannelPlanAPMacAddr_Object = MibTableColumn
wsChannelPlanAPMacAddr = _WsChannelPlanAPMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 18, 1, 2),
    _WsChannelPlanAPMacAddr_Type()
)
wsChannelPlanAPMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsChannelPlanAPMacAddr.setStatus("current")


class _WsChannelPlanAPRadioIntf_Type(Integer32):
    """Custom type wsChannelPlanAPRadioIntf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WsChannelPlanAPRadioIntf_Type.__name__ = "Integer32"
_WsChannelPlanAPRadioIntf_Object = MibTableColumn
wsChannelPlanAPRadioIntf = _WsChannelPlanAPRadioIntf_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 18, 1, 3),
    _WsChannelPlanAPRadioIntf_Type()
)
wsChannelPlanAPRadioIntf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsChannelPlanAPRadioIntf.setStatus("current")


class _WsChannelPlanAPIsLocal_Type(Integer32):
    """Custom type wsChannelPlanAPIsLocal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("peerSwitch", 0),
          ("local", 1))
    )


_WsChannelPlanAPIsLocal_Type.__name__ = "Integer32"
_WsChannelPlanAPIsLocal_Object = MibTableColumn
wsChannelPlanAPIsLocal = _WsChannelPlanAPIsLocal_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 18, 1, 4),
    _WsChannelPlanAPIsLocal_Type()
)
wsChannelPlanAPIsLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsChannelPlanAPIsLocal.setStatus("current")
_WsChannelPlanAPCurrentChannel_Type = Integer32
_WsChannelPlanAPCurrentChannel_Object = MibTableColumn
wsChannelPlanAPCurrentChannel = _WsChannelPlanAPCurrentChannel_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 18, 1, 5),
    _WsChannelPlanAPCurrentChannel_Type()
)
wsChannelPlanAPCurrentChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsChannelPlanAPCurrentChannel.setStatus("current")


class _WsChannelPlanAPOldChannel_Type(Integer32):
    """Custom type wsChannelPlanAPOldChannel based on Integer32"""
    defaultValue = 0


_WsChannelPlanAPOldChannel_Type.__name__ = "Integer32"
_WsChannelPlanAPOldChannel_Object = MibTableColumn
wsChannelPlanAPOldChannel = _WsChannelPlanAPOldChannel_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 18, 1, 6),
    _WsChannelPlanAPOldChannel_Type()
)
wsChannelPlanAPOldChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsChannelPlanAPOldChannel.setStatus("current")


class _WsChannelPlanAPStrongestOldSignal_Type(DisplayString):
    """Custom type wsChannelPlanAPStrongestOldSignal based on DisplayString"""
    defaultValue = OctetString("N/A")


_WsChannelPlanAPStrongestOldSignal_Type.__name__ = "DisplayString"
_WsChannelPlanAPStrongestOldSignal_Object = MibTableColumn
wsChannelPlanAPStrongestOldSignal = _WsChannelPlanAPStrongestOldSignal_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 18, 1, 7),
    _WsChannelPlanAPStrongestOldSignal_Type()
)
wsChannelPlanAPStrongestOldSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsChannelPlanAPStrongestOldSignal.setStatus("current")


class _WsChannelPlanAPStrongestNewSignal_Type(DisplayString):
    """Custom type wsChannelPlanAPStrongestNewSignal based on DisplayString"""
    defaultValue = OctetString("N/A")


_WsChannelPlanAPStrongestNewSignal_Type.__name__ = "DisplayString"
_WsChannelPlanAPStrongestNewSignal_Object = MibTableColumn
wsChannelPlanAPStrongestNewSignal = _WsChannelPlanAPStrongestNewSignal_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 18, 1, 8),
    _WsChannelPlanAPStrongestNewSignal_Type()
)
wsChannelPlanAPStrongestNewSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsChannelPlanAPStrongestNewSignal.setStatus("current")


class _WsChannelPlanAPChannelChangeInd_Type(Integer32):
    """Custom type wsChannelPlanAPChannelChangeInd based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1),
          ("wait", 2))
    )


_WsChannelPlanAPChannelChangeInd_Type.__name__ = "Integer32"
_WsChannelPlanAPChannelChangeInd_Object = MibTableColumn
wsChannelPlanAPChannelChangeInd = _WsChannelPlanAPChannelChangeInd_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 18, 1, 9),
    _WsChannelPlanAPChannelChangeInd_Type()
)
wsChannelPlanAPChannelChangeInd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsChannelPlanAPChannelChangeInd.setStatus("current")


class _WsChannelPlanAPReasonCode_Type(Integer32):
    """Custom type wsChannelPlanAPReasonCode based on Integer32"""
    defaultValue = 0

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
        *(("chanPlanNeverExecuted", 0),
          ("channelIsStatic", 1),
          ("oneEligibleChannel", 2),
          ("detectedAPSignalBelowThresh", 3),
          ("chanFoundWithLowInterference", 4),
          ("chanNotFoundWithLowInterference", 5),
          ("partOfWDSLink", 6))
    )


_WsChannelPlanAPReasonCode_Type.__name__ = "Integer32"
_WsChannelPlanAPReasonCode_Object = MibTableColumn
wsChannelPlanAPReasonCode = _WsChannelPlanAPReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 18, 1, 10),
    _WsChannelPlanAPReasonCode_Type()
)
wsChannelPlanAPReasonCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsChannelPlanAPReasonCode.setStatus("current")


class _WsChannelPlanAPStrongestOldManagedAPandSignal_Type(DisplayString):
    """Custom type wsChannelPlanAPStrongestOldManagedAPandSignal based on DisplayString"""
    defaultValue = OctetString("N/A")


_WsChannelPlanAPStrongestOldManagedAPandSignal_Type.__name__ = "DisplayString"
_WsChannelPlanAPStrongestOldManagedAPandSignal_Object = MibTableColumn
wsChannelPlanAPStrongestOldManagedAPandSignal = _WsChannelPlanAPStrongestOldManagedAPandSignal_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 18, 1, 11),
    _WsChannelPlanAPStrongestOldManagedAPandSignal_Type()
)
wsChannelPlanAPStrongestOldManagedAPandSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsChannelPlanAPStrongestOldManagedAPandSignal.setStatus("current")


class _WsChannelPlanAPStrongestNewManagedAPandSignal_Type(DisplayString):
    """Custom type wsChannelPlanAPStrongestNewManagedAPandSignal based on DisplayString"""
    defaultValue = OctetString("N/A")


_WsChannelPlanAPStrongestNewManagedAPandSignal_Type.__name__ = "DisplayString"
_WsChannelPlanAPStrongestNewManagedAPandSignal_Object = MibTableColumn
wsChannelPlanAPStrongestNewManagedAPandSignal = _WsChannelPlanAPStrongestNewManagedAPandSignal_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 18, 1, 12),
    _WsChannelPlanAPStrongestNewManagedAPandSignal_Type()
)
wsChannelPlanAPStrongestNewManagedAPandSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsChannelPlanAPStrongestNewManagedAPandSignal.setStatus("current")


class _WsChannelPlanAPStrongestOldUnmanagedAPandSignal_Type(DisplayString):
    """Custom type wsChannelPlanAPStrongestOldUnmanagedAPandSignal based on DisplayString"""
    defaultValue = OctetString("N/A")


_WsChannelPlanAPStrongestOldUnmanagedAPandSignal_Type.__name__ = "DisplayString"
_WsChannelPlanAPStrongestOldUnmanagedAPandSignal_Object = MibTableColumn
wsChannelPlanAPStrongestOldUnmanagedAPandSignal = _WsChannelPlanAPStrongestOldUnmanagedAPandSignal_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 18, 1, 13),
    _WsChannelPlanAPStrongestOldUnmanagedAPandSignal_Type()
)
wsChannelPlanAPStrongestOldUnmanagedAPandSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsChannelPlanAPStrongestOldUnmanagedAPandSignal.setStatus("current")


class _WsChannelPlanAPStrongestNewUnmanagedAPandSignal_Type(DisplayString):
    """Custom type wsChannelPlanAPStrongestNewUnmanagedAPandSignal based on DisplayString"""
    defaultValue = OctetString("N/A")


_WsChannelPlanAPStrongestNewUnmanagedAPandSignal_Type.__name__ = "DisplayString"
_WsChannelPlanAPStrongestNewUnmanagedAPandSignal_Object = MibTableColumn
wsChannelPlanAPStrongestNewUnmanagedAPandSignal = _WsChannelPlanAPStrongestNewUnmanagedAPandSignal_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 18, 1, 14),
    _WsChannelPlanAPStrongestNewUnmanagedAPandSignal_Type()
)
wsChannelPlanAPStrongestNewUnmanagedAPandSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsChannelPlanAPStrongestNewUnmanagedAPandSignal.setStatus("current")
_WsChannelPlanAPTimeSinceLastChannelChange_Type = DisplayString
_WsChannelPlanAPTimeSinceLastChannelChange_Object = MibTableColumn
wsChannelPlanAPTimeSinceLastChannelChange = _WsChannelPlanAPTimeSinceLastChannelChange_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 18, 1, 15),
    _WsChannelPlanAPTimeSinceLastChannelChange_Type()
)
wsChannelPlanAPTimeSinceLastChannelChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsChannelPlanAPTimeSinceLastChannelChange.setStatus("current")


class _WsChannelPlanAPLastChanScanDuration_Type(Integer32):
    """Custom type wsChannelPlanAPLastChanScanDuration based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999999),
    )


_WsChannelPlanAPLastChanScanDuration_Type.__name__ = "Integer32"
_WsChannelPlanAPLastChanScanDuration_Object = MibTableColumn
wsChannelPlanAPLastChanScanDuration = _WsChannelPlanAPLastChanScanDuration_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 18, 1, 16),
    _WsChannelPlanAPLastChanScanDuration_Type()
)
wsChannelPlanAPLastChanScanDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsChannelPlanAPLastChanScanDuration.setStatus("current")
_WsPowerPlanPerRadioTable_Object = MibTable
wsPowerPlanPerRadioTable = _WsPowerPlanPerRadioTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 19)
)
if mibBuilder.loadTexts:
    wsPowerPlanPerRadioTable.setStatus("current")
_WsPowerPlanPerRadioEntry_Object = MibTableRow
wsPowerPlanPerRadioEntry = _WsPowerPlanPerRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 19, 1)
)
wsPowerPlanPerRadioEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsPowerPlanAPMacAddress"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsPowerPlanAPRadioInterface"),
)
if mibBuilder.loadTexts:
    wsPowerPlanPerRadioEntry.setStatus("current")
_WsPowerPlanAPMacAddress_Type = MacAddress
_WsPowerPlanAPMacAddress_Object = MibTableColumn
wsPowerPlanAPMacAddress = _WsPowerPlanAPMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 19, 1, 1),
    _WsPowerPlanAPMacAddress_Type()
)
wsPowerPlanAPMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsPowerPlanAPMacAddress.setStatus("current")


class _WsPowerPlanAPRadioInterface_Type(Integer32):
    """Custom type wsPowerPlanAPRadioInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WsPowerPlanAPRadioInterface_Type.__name__ = "Integer32"
_WsPowerPlanAPRadioInterface_Object = MibTableColumn
wsPowerPlanAPRadioInterface = _WsPowerPlanAPRadioInterface_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 19, 1, 2),
    _WsPowerPlanAPRadioInterface_Type()
)
wsPowerPlanAPRadioInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsPowerPlanAPRadioInterface.setStatus("current")


class _WsPowerPlanAPIsLocal_Type(Integer32):
    """Custom type wsPowerPlanAPIsLocal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("peerSwitch", 0),
          ("local", 1))
    )


_WsPowerPlanAPIsLocal_Type.__name__ = "Integer32"
_WsPowerPlanAPIsLocal_Object = MibTableColumn
wsPowerPlanAPIsLocal = _WsPowerPlanAPIsLocal_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 19, 1, 3),
    _WsPowerPlanAPIsLocal_Type()
)
wsPowerPlanAPIsLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPowerPlanAPIsLocal.setStatus("current")


class _WsPowerPlanAPChannel_Type(DisplayString):
    """Custom type wsPowerPlanAPChannel based on DisplayString"""
    defaultValue = OctetString("None")


_WsPowerPlanAPChannel_Type.__name__ = "DisplayString"
_WsPowerPlanAPChannel_Object = MibTableColumn
wsPowerPlanAPChannel = _WsPowerPlanAPChannel_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 19, 1, 4),
    _WsPowerPlanAPChannel_Type()
)
wsPowerPlanAPChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPowerPlanAPChannel.setStatus("current")


class _WsPowerPlanAPTxPower_Type(Integer32):
    """Custom type wsPowerPlanAPTxPower based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_WsPowerPlanAPTxPower_Type.__name__ = "Integer32"
_WsPowerPlanAPTxPower_Object = MibTableColumn
wsPowerPlanAPTxPower = _WsPowerPlanAPTxPower_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 19, 1, 5),
    _WsPowerPlanAPTxPower_Type()
)
wsPowerPlanAPTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPowerPlanAPTxPower.setStatus("current")


class _WsPowerPlanAPNumInterferingAPs_Type(Integer32):
    """Custom type wsPowerPlanAPNumInterferingAPs based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_WsPowerPlanAPNumInterferingAPs_Type.__name__ = "Integer32"
_WsPowerPlanAPNumInterferingAPs_Object = MibTableColumn
wsPowerPlanAPNumInterferingAPs = _WsPowerPlanAPNumInterferingAPs_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 19, 1, 6),
    _WsPowerPlanAPNumInterferingAPs_Type()
)
wsPowerPlanAPNumInterferingAPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPowerPlanAPNumInterferingAPs.setStatus("current")


class _WsPowerPlanAPNumInterferingVAPs_Type(Integer32):
    """Custom type wsPowerPlanAPNumInterferingVAPs based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_WsPowerPlanAPNumInterferingVAPs_Type.__name__ = "Integer32"
_WsPowerPlanAPNumInterferingVAPs_Object = MibTableColumn
wsPowerPlanAPNumInterferingVAPs = _WsPowerPlanAPNumInterferingVAPs_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 19, 1, 7),
    _WsPowerPlanAPNumInterferingVAPs_Type()
)
wsPowerPlanAPNumInterferingVAPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPowerPlanAPNumInterferingVAPs.setStatus("current")
_WsPowerPlanAPStrongestDetectorAP_Type = MacAddress
_WsPowerPlanAPStrongestDetectorAP_Object = MibTableColumn
wsPowerPlanAPStrongestDetectorAP = _WsPowerPlanAPStrongestDetectorAP_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 19, 1, 8),
    _WsPowerPlanAPStrongestDetectorAP_Type()
)
wsPowerPlanAPStrongestDetectorAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPowerPlanAPStrongestDetectorAP.setStatus("current")


class _WsPowerPlanAPStrongestDetectorRadio_Type(Integer32):
    """Custom type wsPowerPlanAPStrongestDetectorRadio based on Integer32"""
    defaultValue = 0


_WsPowerPlanAPStrongestDetectorRadio_Type.__name__ = "Integer32"
_WsPowerPlanAPStrongestDetectorRadio_Object = MibTableColumn
wsPowerPlanAPStrongestDetectorRadio = _WsPowerPlanAPStrongestDetectorRadio_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 19, 1, 9),
    _WsPowerPlanAPStrongestDetectorRadio_Type()
)
wsPowerPlanAPStrongestDetectorRadio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPowerPlanAPStrongestDetectorRadio.setStatus("current")


class _WsPowerPlanAPStrongestDetectorSignal_Type(DisplayString):
    """Custom type wsPowerPlanAPStrongestDetectorSignal based on DisplayString"""
    defaultValue = OctetString("None")


_WsPowerPlanAPStrongestDetectorSignal_Type.__name__ = "DisplayString"
_WsPowerPlanAPStrongestDetectorSignal_Object = MibTableColumn
wsPowerPlanAPStrongestDetectorSignal = _WsPowerPlanAPStrongestDetectorSignal_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 19, 1, 10),
    _WsPowerPlanAPStrongestDetectorSignal_Type()
)
wsPowerPlanAPStrongestDetectorSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPowerPlanAPStrongestDetectorSignal.setStatus("current")
_WsPowerPlanAPStrongestDetectedNeighbor_Type = MacAddress
_WsPowerPlanAPStrongestDetectedNeighbor_Object = MibTableColumn
wsPowerPlanAPStrongestDetectedNeighbor = _WsPowerPlanAPStrongestDetectedNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 19, 1, 11),
    _WsPowerPlanAPStrongestDetectedNeighbor_Type()
)
wsPowerPlanAPStrongestDetectedNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPowerPlanAPStrongestDetectedNeighbor.setStatus("current")


class _WsPowerPlanAPStrongestDetectedSignal_Type(DisplayString):
    """Custom type wsPowerPlanAPStrongestDetectedSignal based on DisplayString"""
    defaultValue = OctetString("None")


_WsPowerPlanAPStrongestDetectedSignal_Type.__name__ = "DisplayString"
_WsPowerPlanAPStrongestDetectedSignal_Object = MibTableColumn
wsPowerPlanAPStrongestDetectedSignal = _WsPowerPlanAPStrongestDetectedSignal_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 19, 1, 12),
    _WsPowerPlanAPStrongestDetectedSignal_Type()
)
wsPowerPlanAPStrongestDetectedSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPowerPlanAPStrongestDetectedSignal.setStatus("current")


class _WsPowerPlanAPLastPwrAdjStatus_Type(Integer32):
    """Custom type wsPowerPlanAPLastPwrAdjStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unchanged", 0),
          ("increased", 1),
          ("reduced", 2))
    )


_WsPowerPlanAPLastPwrAdjStatus_Type.__name__ = "Integer32"
_WsPowerPlanAPLastPwrAdjStatus_Object = MibTableColumn
wsPowerPlanAPLastPwrAdjStatus = _WsPowerPlanAPLastPwrAdjStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 19, 1, 13),
    _WsPowerPlanAPLastPwrAdjStatus_Type()
)
wsPowerPlanAPLastPwrAdjStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPowerPlanAPLastPwrAdjStatus.setStatus("current")


class _WsPowerPlanAPLastPwrAdjReasonCode_Type(Integer32):
    """Custom type wsPowerPlanAPLastPwrAdjReasonCode based on Integer32"""
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
        *(("powerPlanNeverExecuted", 0),
          ("powerPlanRadioInSentryMode", 1),
          ("powerPlanRadioAutoPowerDisable", 2),
          ("powerPlanRadioPowerUnchanged", 3),
          ("powerPlanRadioOperatingInMaxPower", 4),
          ("powerPlanRadioOperatingInMinPower", 5),
          ("powerPlanRadioMinPowerIs100", 6),
          ("powerPlanRadioPowerIncreaseRequired", 7),
          ("powerPlanRadioPowerDecreaseRequired", 8),
          ("powerPlanRadioPowerAdjNone", 9),
          ("powerPlanRadioPowerPartOfWDSLink", 10))
    )


_WsPowerPlanAPLastPwrAdjReasonCode_Type.__name__ = "Integer32"
_WsPowerPlanAPLastPwrAdjReasonCode_Object = MibTableColumn
wsPowerPlanAPLastPwrAdjReasonCode = _WsPowerPlanAPLastPwrAdjReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 19, 1, 14),
    _WsPowerPlanAPLastPwrAdjReasonCode_Type()
)
wsPowerPlanAPLastPwrAdjReasonCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPowerPlanAPLastPwrAdjReasonCode.setStatus("current")


class _WsPowerPlanAPNumPwrChanges_Type(Integer32):
    """Custom type wsPowerPlanAPNumPwrChanges based on Integer32"""
    defaultValue = 0


_WsPowerPlanAPNumPwrChanges_Type.__name__ = "Integer32"
_WsPowerPlanAPNumPwrChanges_Object = MibTableColumn
wsPowerPlanAPNumPwrChanges = _WsPowerPlanAPNumPwrChanges_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 19, 1, 15),
    _WsPowerPlanAPNumPwrChanges_Type()
)
wsPowerPlanAPNumPwrChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPowerPlanAPNumPwrChanges.setStatus("current")


class _WsPowerPlanAPNumPwrInc_Type(Integer32):
    """Custom type wsPowerPlanAPNumPwrInc based on Integer32"""
    defaultValue = 0


_WsPowerPlanAPNumPwrInc_Type.__name__ = "Integer32"
_WsPowerPlanAPNumPwrInc_Object = MibTableColumn
wsPowerPlanAPNumPwrInc = _WsPowerPlanAPNumPwrInc_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 19, 1, 16),
    _WsPowerPlanAPNumPwrInc_Type()
)
wsPowerPlanAPNumPwrInc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPowerPlanAPNumPwrInc.setStatus("current")


class _WsPowerPlanAPNumPwrDec_Type(Integer32):
    """Custom type wsPowerPlanAPNumPwrDec based on Integer32"""
    defaultValue = 0


_WsPowerPlanAPNumPwrDec_Type.__name__ = "Integer32"
_WsPowerPlanAPNumPwrDec_Object = MibTableColumn
wsPowerPlanAPNumPwrDec = _WsPowerPlanAPNumPwrDec_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 19, 1, 17),
    _WsPowerPlanAPNumPwrDec_Type()
)
wsPowerPlanAPNumPwrDec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPowerPlanAPNumPwrDec.setStatus("current")
_WsPowerPlanPerProfileTable_Object = MibTable
wsPowerPlanPerProfileTable = _WsPowerPlanPerProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 20)
)
if mibBuilder.loadTexts:
    wsPowerPlanPerProfileTable.setStatus("current")
_WsPowerPlanPerProfileEntry_Object = MibTableRow
wsPowerPlanPerProfileEntry = _WsPowerPlanPerProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 20, 1)
)
wsPowerPlanPerProfileEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsPowerPlanProfileId"),
)
if mibBuilder.loadTexts:
    wsPowerPlanPerProfileEntry.setStatus("current")


class _WsPowerPlanProfileId_Type(Integer32):
    """Custom type wsPowerPlanProfileId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_WsPowerPlanProfileId_Type.__name__ = "Integer32"
_WsPowerPlanProfileId_Object = MibTableColumn
wsPowerPlanProfileId = _WsPowerPlanProfileId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 20, 1, 1),
    _WsPowerPlanProfileId_Type()
)
wsPowerPlanProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsPowerPlanProfileId.setStatus("current")


class _WsPowerPlanPerProfileAvgNumInterferingAPs_Type(Integer32):
    """Custom type wsPowerPlanPerProfileAvgNumInterferingAPs based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_WsPowerPlanPerProfileAvgNumInterferingAPs_Type.__name__ = "Integer32"
_WsPowerPlanPerProfileAvgNumInterferingAPs_Object = MibTableColumn
wsPowerPlanPerProfileAvgNumInterferingAPs = _WsPowerPlanPerProfileAvgNumInterferingAPs_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 20, 1, 2),
    _WsPowerPlanPerProfileAvgNumInterferingAPs_Type()
)
wsPowerPlanPerProfileAvgNumInterferingAPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPowerPlanPerProfileAvgNumInterferingAPs.setStatus("current")


class _WsPowerPlanPerProfileAvgNumInterferingVAPs_Type(Integer32):
    """Custom type wsPowerPlanPerProfileAvgNumInterferingVAPs based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_WsPowerPlanPerProfileAvgNumInterferingVAPs_Type.__name__ = "Integer32"
_WsPowerPlanPerProfileAvgNumInterferingVAPs_Object = MibTableColumn
wsPowerPlanPerProfileAvgNumInterferingVAPs = _WsPowerPlanPerProfileAvgNumInterferingVAPs_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 20, 1, 3),
    _WsPowerPlanPerProfileAvgNumInterferingVAPs_Type()
)
wsPowerPlanPerProfileAvgNumInterferingVAPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPowerPlanPerProfileAvgNumInterferingVAPs.setStatus("current")


class _WsPowerPlanNumPwrChanges_Type(Integer32):
    """Custom type wsPowerPlanNumPwrChanges based on Integer32"""
    defaultValue = 0


_WsPowerPlanNumPwrChanges_Type.__name__ = "Integer32"
_WsPowerPlanNumPwrChanges_Object = MibTableColumn
wsPowerPlanNumPwrChanges = _WsPowerPlanNumPwrChanges_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 20, 1, 4),
    _WsPowerPlanNumPwrChanges_Type()
)
wsPowerPlanNumPwrChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPowerPlanNumPwrChanges.setStatus("current")


class _WsPowerPlanNumPwrInc_Type(Integer32):
    """Custom type wsPowerPlanNumPwrInc based on Integer32"""
    defaultValue = 0


_WsPowerPlanNumPwrInc_Type.__name__ = "Integer32"
_WsPowerPlanNumPwrInc_Object = MibTableColumn
wsPowerPlanNumPwrInc = _WsPowerPlanNumPwrInc_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 20, 1, 5),
    _WsPowerPlanNumPwrInc_Type()
)
wsPowerPlanNumPwrInc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPowerPlanNumPwrInc.setStatus("current")


class _WsPowerPlanNumPwrDec_Type(Integer32):
    """Custom type wsPowerPlanNumPwrDec based on Integer32"""
    defaultValue = 0


_WsPowerPlanNumPwrDec_Type.__name__ = "Integer32"
_WsPowerPlanNumPwrDec_Object = MibTableColumn
wsPowerPlanNumPwrDec = _WsPowerPlanNumPwrDec_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 20, 1, 6),
    _WsPowerPlanNumPwrDec_Type()
)
wsPowerPlanNumPwrDec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPowerPlanNumPwrDec.setStatus("current")


class _WsNtwProvisoningAction_Type(Integer32):
    """Custom type wsNtwProvisoningAction based on Integer32"""
    defaultValue = 0

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
          ("start", 1),
          ("stop", 2))
    )


_WsNtwProvisoningAction_Type.__name__ = "Integer32"
_WsNtwProvisoningAction_Object = MibScalar
wsNtwProvisoningAction = _WsNtwProvisoningAction_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 21),
    _WsNtwProvisoningAction_Type()
)
wsNtwProvisoningAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsNtwProvisoningAction.setStatus("current")


class _WsNtwProvisioningOperatingStatus_Type(Integer32):
    """Custom type wsNtwProvisioningOperatingStatus based on Integer32"""
    defaultValue = 0

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
        *(("notstarted", 0),
          ("running", 1),
          ("finished", 2),
          ("aborted", 3),
          ("failed", 4))
    )


_WsNtwProvisioningOperatingStatus_Type.__name__ = "Integer32"
_WsNtwProvisioningOperatingStatus_Object = MibScalar
wsNtwProvisioningOperatingStatus = _WsNtwProvisioningOperatingStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 22),
    _WsNtwProvisioningOperatingStatus_Type()
)
wsNtwProvisioningOperatingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNtwProvisioningOperatingStatus.setStatus("current")


class _WsNtwProvisioningTimeStamp_Type(Integer32):
    """Custom type wsNtwProvisioningTimeStamp based on Integer32"""
    defaultValue = 0


_WsNtwProvisioningTimeStamp_Type.__name__ = "Integer32"
_WsNtwProvisioningTimeStamp_Object = MibScalar
wsNtwProvisioningTimeStamp = _WsNtwProvisioningTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 23),
    _WsNtwProvisioningTimeStamp_Type()
)
wsNtwProvisioningTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNtwProvisioningTimeStamp.setStatus("current")


class _WsNtwProvisioningChanBGCompletion_Type(Integer32):
    """Custom type wsNtwProvisioningChanBGCompletion based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_WsNtwProvisioningChanBGCompletion_Type.__name__ = "Integer32"
_WsNtwProvisioningChanBGCompletion_Object = MibScalar
wsNtwProvisioningChanBGCompletion = _WsNtwProvisioningChanBGCompletion_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 24),
    _WsNtwProvisioningChanBGCompletion_Type()
)
wsNtwProvisioningChanBGCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNtwProvisioningChanBGCompletion.setStatus("current")


class _WsNtwProvisioningChanACompletion_Type(Integer32):
    """Custom type wsNtwProvisioningChanACompletion based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_WsNtwProvisioningChanACompletion_Type.__name__ = "Integer32"
_WsNtwProvisioningChanACompletion_Object = MibScalar
wsNtwProvisioningChanACompletion = _WsNtwProvisioningChanACompletion_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 25),
    _WsNtwProvisioningChanACompletion_Type()
)
wsNtwProvisioningChanACompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNtwProvisioningChanACompletion.setStatus("current")


class _WsNtwProvisioningPowerPlanCnt_Type(Integer32):
    """Custom type wsNtwProvisioningPowerPlanCnt based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_WsNtwProvisioningPowerPlanCnt_Type.__name__ = "Integer32"
_WsNtwProvisioningPowerPlanCnt_Object = MibScalar
wsNtwProvisioningPowerPlanCnt = _WsNtwProvisioningPowerPlanCnt_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 5, 26),
    _WsNtwProvisioningPowerPlanCnt_Type()
)
wsNtwProvisioningPowerPlanCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNtwProvisioningPowerPlanCnt.setStatus("current")
_ManagedAP_ObjectIdentity = ObjectIdentity
managedAP = _ManagedAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6)
)
_WsManagedAPStatusTable_Object = MibTable
wsManagedAPStatusTable = _WsManagedAPStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 1)
)
if mibBuilder.loadTexts:
    wsManagedAPStatusTable.setStatus("current")
_WsManagedAPStatusEntry_Object = MibTableRow
wsManagedAPStatusEntry = _WsManagedAPStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 1, 1)
)
wsManagedAPStatusEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsManagedAPMacAddress"),
)
if mibBuilder.loadTexts:
    wsManagedAPStatusEntry.setStatus("current")
_WsManagedAPMacAddress_Type = MacAddress
_WsManagedAPMacAddress_Object = MibTableColumn
wsManagedAPMacAddress = _WsManagedAPMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 1, 1, 1),
    _WsManagedAPMacAddress_Type()
)
wsManagedAPMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPMacAddress.setStatus("current")
_WsManagedAPIpAddress_Type = IpAddress
_WsManagedAPIpAddress_Object = MibTableColumn
wsManagedAPIpAddress = _WsManagedAPIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 1, 1, 2),
    _WsManagedAPIpAddress_Type()
)
wsManagedAPIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPIpAddress.setStatus("current")


class _WsManagedAPVendorId_Type(Integer32):
    """Custom type wsManagedAPVendorId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WsManagedAPVendorId_Type.__name__ = "Integer32"
_WsManagedAPVendorId_Object = MibTableColumn
wsManagedAPVendorId = _WsManagedAPVendorId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 1, 1, 3),
    _WsManagedAPVendorId_Type()
)
wsManagedAPVendorId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsManagedAPVendorId.setStatus("current")


class _WsManagedAPSoftwareVersion_Type(DisplayString):
    """Custom type wsManagedAPSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WsManagedAPSoftwareVersion_Type.__name__ = "DisplayString"
_WsManagedAPSoftwareVersion_Object = MibTableColumn
wsManagedAPSoftwareVersion = _WsManagedAPSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 1, 1, 4),
    _WsManagedAPSoftwareVersion_Type()
)
wsManagedAPSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPSoftwareVersion.setStatus("current")
_WsManagedAPHWType_Type = Integer32
_WsManagedAPHWType_Object = MibTableColumn
wsManagedAPHWType = _WsManagedAPHWType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 1, 1, 5),
    _WsManagedAPHWType_Type()
)
wsManagedAPHWType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsManagedAPHWType.setStatus("current")


class _WsManagedAPSerialNumber_Type(DisplayString):
    """Custom type wsManagedAPSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WsManagedAPSerialNumber_Type.__name__ = "DisplayString"
_WsManagedAPSerialNumber_Object = MibTableColumn
wsManagedAPSerialNumber = _WsManagedAPSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 1, 1, 6),
    _WsManagedAPSerialNumber_Type()
)
wsManagedAPSerialNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsManagedAPSerialNumber.setStatus("current")


class _WsManagedAPPartNumber_Type(DisplayString):
    """Custom type wsManagedAPPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WsManagedAPPartNumber_Type.__name__ = "DisplayString"
_WsManagedAPPartNumber_Object = MibTableColumn
wsManagedAPPartNumber = _WsManagedAPPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 1, 1, 7),
    _WsManagedAPPartNumber_Type()
)
wsManagedAPPartNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsManagedAPPartNumber.setStatus("current")


class _WsManagedAPDiscoveryReason_Type(Integer32):
    """Custom type wsManagedAPDiscoveryReason based on Integer32"""
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
        *(("ip-poll", 1),
          ("peer-switch-initiated", 2),
          ("switch-ip-configured-in-ap", 3),
          ("switch-ip-obtained-via-dhcp", 4),
          ("l2Discovery", 5))
    )


_WsManagedAPDiscoveryReason_Type.__name__ = "Integer32"
_WsManagedAPDiscoveryReason_Object = MibTableColumn
wsManagedAPDiscoveryReason = _WsManagedAPDiscoveryReason_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 1, 1, 8),
    _WsManagedAPDiscoveryReason_Type()
)
wsManagedAPDiscoveryReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPDiscoveryReason.setStatus("current")


class _WsManagedAPStatus_Type(Integer32):
    """Custom type wsManagedAPStatus based on Integer32"""
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
        *(("discovered", 1),
          ("authenticated", 2),
          ("upgrading", 3),
          ("managed", 4),
          ("connection-failed", 5),
          ("deleted", 6))
    )


_WsManagedAPStatus_Type.__name__ = "Integer32"
_WsManagedAPStatus_Object = MibTableColumn
wsManagedAPStatus = _WsManagedAPStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 1, 1, 9),
    _WsManagedAPStatus_Type()
)
wsManagedAPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPStatus.setStatus("current")
_WsManagedAPAuthenticatedClients_Type = Unsigned32
_WsManagedAPAuthenticatedClients_Object = MibTableColumn
wsManagedAPAuthenticatedClients = _WsManagedAPAuthenticatedClients_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 1, 1, 10),
    _WsManagedAPAuthenticatedClients_Type()
)
wsManagedAPAuthenticatedClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPAuthenticatedClients.setStatus("current")
_WsManagedAPSysUpTime_Type = TimeTicks
_WsManagedAPSysUpTime_Object = MibTableColumn
wsManagedAPSysUpTime = _WsManagedAPSysUpTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 1, 1, 11),
    _WsManagedAPSysUpTime_Type()
)
wsManagedAPSysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPSysUpTime.setStatus("current")


class _WsManagedAPProfileId_Type(Integer32):
    """Custom type wsManagedAPProfileId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_WsManagedAPProfileId_Type.__name__ = "Integer32"
_WsManagedAPProfileId_Object = MibTableColumn
wsManagedAPProfileId = _WsManagedAPProfileId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 1, 1, 12),
    _WsManagedAPProfileId_Type()
)
wsManagedAPProfileId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPProfileId.setStatus("current")


class _WsManagedAPProfileName_Type(DisplayString):
    """Custom type wsManagedAPProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WsManagedAPProfileName_Type.__name__ = "DisplayString"
_WsManagedAPProfileName_Object = MibTableColumn
wsManagedAPProfileName = _WsManagedAPProfileName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 1, 1, 13),
    _WsManagedAPProfileName_Type()
)
wsManagedAPProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPProfileName.setStatus("current")


class _WsManagedAPProtocolVersion_Type(Integer32):
    """Custom type wsManagedAPProtocolVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WsManagedAPProtocolVersion_Type.__name__ = "Integer32"
_WsManagedAPProtocolVersion_Object = MibTableColumn
wsManagedAPProtocolVersion = _WsManagedAPProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 1, 1, 14),
    _WsManagedAPProtocolVersion_Type()
)
wsManagedAPProtocolVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPProtocolVersion.setStatus("current")


class _WsManagedAPCodeDownloadStatus_Type(Integer32):
    """Custom type wsManagedAPCodeDownloadStatus based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("not-started", 1),
          ("requested", 2),
          ("code-transfer-in-progress", 3),
          ("waiting-for-aps-to-download", 4),
          ("aborted", 5),
          ("nvram-update-in-progress", 6),
          ("timed-out", 7),
          ("failure", 8))
    )


_WsManagedAPCodeDownloadStatus_Type.__name__ = "Integer32"
_WsManagedAPCodeDownloadStatus_Object = MibTableColumn
wsManagedAPCodeDownloadStatus = _WsManagedAPCodeDownloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 1, 1, 15),
    _WsManagedAPCodeDownloadStatus_Type()
)
wsManagedAPCodeDownloadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPCodeDownloadStatus.setStatus("current")


class _WsManagedAPLocation_Type(DisplayString):
    """Custom type wsManagedAPLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WsManagedAPLocation_Type.__name__ = "DisplayString"
_WsManagedAPLocation_Object = MibTableColumn
wsManagedAPLocation = _WsManagedAPLocation_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 1, 1, 16),
    _WsManagedAPLocation_Type()
)
wsManagedAPLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPLocation.setStatus("current")


class _WsManagedAPLastFailingConfigElement_Type(Integer32):
    """Custom type wsManagedAPLastFailingConfigElement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WsManagedAPLastFailingConfigElement_Type.__name__ = "Integer32"
_WsManagedAPLastFailingConfigElement_Object = MibTableColumn
wsManagedAPLastFailingConfigElement = _WsManagedAPLastFailingConfigElement_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 1, 1, 17),
    _WsManagedAPLastFailingConfigElement_Type()
)
wsManagedAPLastFailingConfigElement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPLastFailingConfigElement.setStatus("current")


class _WsManagedAPConfigFailureErrMsg_Type(DisplayString):
    """Custom type wsManagedAPConfigFailureErrMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_WsManagedAPConfigFailureErrMsg_Type.__name__ = "DisplayString"
_WsManagedAPConfigFailureErrMsg_Object = MibTableColumn
wsManagedAPConfigFailureErrMsg = _WsManagedAPConfigFailureErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 1, 1, 18),
    _WsManagedAPConfigFailureErrMsg_Type()
)
wsManagedAPConfigFailureErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPConfigFailureErrMsg.setStatus("current")


class _WsManagedAPReset_Type(Integer32):
    """Custom type wsManagedAPReset based on Integer32"""
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


_WsManagedAPReset_Type.__name__ = "Integer32"
_WsManagedAPReset_Object = MibTableColumn
wsManagedAPReset = _WsManagedAPReset_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 1, 1, 19),
    _WsManagedAPReset_Type()
)
wsManagedAPReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPReset.setStatus("current")


class _WsManagedAPResetStatus_Type(Integer32):
    """Custom type wsManagedAPResetStatus based on Integer32"""
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
        *(("not-started", 1),
          ("in-progress", 2),
          ("success", 3),
          ("failure", 4))
    )


_WsManagedAPResetStatus_Type.__name__ = "Integer32"
_WsManagedAPResetStatus_Object = MibTableColumn
wsManagedAPResetStatus = _WsManagedAPResetStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 1, 1, 20),
    _WsManagedAPResetStatus_Type()
)
wsManagedAPResetStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPResetStatus.setStatus("current")


class _WsManagedAPFailedEntryPurge_Type(Integer32):
    """Custom type wsManagedAPFailedEntryPurge based on Integer32"""
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


_WsManagedAPFailedEntryPurge_Type.__name__ = "Integer32"
_WsManagedAPFailedEntryPurge_Object = MibTableColumn
wsManagedAPFailedEntryPurge = _WsManagedAPFailedEntryPurge_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 1, 1, 21),
    _WsManagedAPFailedEntryPurge_Type()
)
wsManagedAPFailedEntryPurge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPFailedEntryPurge.setStatus("current")


class _WsManagedAPDebugPassword_Type(DisplayString):
    """Custom type wsManagedAPDebugPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WsManagedAPDebugPassword_Type.__name__ = "DisplayString"
_WsManagedAPDebugPassword_Object = MibTableColumn
wsManagedAPDebugPassword = _WsManagedAPDebugPassword_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 1, 1, 22),
    _WsManagedAPDebugPassword_Type()
)
wsManagedAPDebugPassword.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsManagedAPDebugPassword.setStatus("current")


class _WsManagedAPDebugMode_Type(Integer32):
    """Custom type wsManagedAPDebugMode based on Integer32"""
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


_WsManagedAPDebugMode_Type.__name__ = "Integer32"
_WsManagedAPDebugMode_Object = MibTableColumn
wsManagedAPDebugMode = _WsManagedAPDebugMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 1, 1, 23),
    _WsManagedAPDebugMode_Type()
)
wsManagedAPDebugMode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsManagedAPDebugMode.setStatus("current")


class _WsManagedAPDebugStatus_Type(Integer32):
    """Custom type wsManagedAPDebugStatus based on Integer32"""
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
        *(("not-started", 1),
          ("requested", 2),
          ("in-progress", 3),
          ("success", 4),
          ("failure", 5))
    )


_WsManagedAPDebugStatus_Type.__name__ = "Integer32"
_WsManagedAPDebugStatus_Object = MibTableColumn
wsManagedAPDebugStatus = _WsManagedAPDebugStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 1, 1, 24),
    _WsManagedAPDebugStatus_Type()
)
wsManagedAPDebugStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsManagedAPDebugStatus.setStatus("current")
_WsManagedAPAge_Type = TimeTicks
_WsManagedAPAge_Object = MibTableColumn
wsManagedAPAge = _WsManagedAPAge_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 1, 1, 25),
    _WsManagedAPAge_Type()
)
wsManagedAPAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPAge.setStatus("current")


class _WsManagedAPManagingSwitch_Type(Integer32):
    """Custom type wsManagedAPManagingSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local-switch", 1),
          ("peer-switch", 2))
    )


_WsManagedAPManagingSwitch_Type.__name__ = "Integer32"
_WsManagedAPManagingSwitch_Object = MibTableColumn
wsManagedAPManagingSwitch = _WsManagedAPManagingSwitch_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 1, 1, 26),
    _WsManagedAPManagingSwitch_Type()
)
wsManagedAPManagingSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPManagingSwitch.setStatus("current")
_WsManagedAPSwitchMacAddress_Type = MacAddress
_WsManagedAPSwitchMacAddress_Object = MibTableColumn
wsManagedAPSwitchMacAddress = _WsManagedAPSwitchMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 1, 1, 27),
    _WsManagedAPSwitchMacAddress_Type()
)
wsManagedAPSwitchMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPSwitchMacAddress.setStatus("current")
_WsManagedAPSwitchIpAddress_Type = IpAddress
_WsManagedAPSwitchIpAddress_Object = MibTableColumn
wsManagedAPSwitchIpAddress = _WsManagedAPSwitchIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 1, 1, 28),
    _WsManagedAPSwitchIpAddress_Type()
)
wsManagedAPSwitchIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPSwitchIpAddress.setStatus("current")
_WsManagedAPIpMask_Type = IpAddress
_WsManagedAPIpMask_Object = MibTableColumn
wsManagedAPIpMask = _WsManagedAPIpMask_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 1, 1, 29),
    _WsManagedAPIpMask_Type()
)
wsManagedAPIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPIpMask.setStatus("current")
_WsManagedAPDistTunnelHomeAPClients_Type = Unsigned32
_WsManagedAPDistTunnelHomeAPClients_Object = MibTableColumn
wsManagedAPDistTunnelHomeAPClients = _WsManagedAPDistTunnelHomeAPClients_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 1, 1, 30),
    _WsManagedAPDistTunnelHomeAPClients_Type()
)
wsManagedAPDistTunnelHomeAPClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPDistTunnelHomeAPClients.setStatus("current")
_WsManagedAPDistTunnelAssocAPClients_Type = Unsigned32
_WsManagedAPDistTunnelAssocAPClients_Object = MibTableColumn
wsManagedAPDistTunnelAssocAPClients = _WsManagedAPDistTunnelAssocAPClients_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 1, 1, 31),
    _WsManagedAPDistTunnelAssocAPClients_Type()
)
wsManagedAPDistTunnelAssocAPClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPDistTunnelAssocAPClients.setStatus("current")
_WsManagedAPDistTunnelsTotal_Type = Unsigned32
_WsManagedAPDistTunnelsTotal_Object = MibTableColumn
wsManagedAPDistTunnelsTotal = _WsManagedAPDistTunnelsTotal_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 1, 1, 32),
    _WsManagedAPDistTunnelsTotal_Type()
)
wsManagedAPDistTunnelsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPDistTunnelsTotal.setStatus("current")
_WsManagedAPDistTunnelsMaxMcastRepl_Type = Unsigned32
_WsManagedAPDistTunnelsMaxMcastRepl_Object = MibTableColumn
wsManagedAPDistTunnelsMaxMcastRepl = _WsManagedAPDistTunnelsMaxMcastRepl_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 1, 1, 33),
    _WsManagedAPDistTunnelsMaxMcastRepl_Type()
)
wsManagedAPDistTunnelsMaxMcastRepl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPDistTunnelsMaxMcastRepl.setStatus("current")
_WsManagedAPDistTunnelsMaxVlanMcastRepl_Type = Unsigned32
_WsManagedAPDistTunnelsMaxVlanMcastRepl_Object = MibTableColumn
wsManagedAPDistTunnelsMaxVlanMcastRepl = _WsManagedAPDistTunnelsMaxVlanMcastRepl_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 1, 1, 34),
    _WsManagedAPDistTunnelsMaxVlanMcastRepl_Type()
)
wsManagedAPDistTunnelsMaxVlanMcastRepl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPDistTunnelsMaxVlanMcastRepl.setStatus("current")


class _WsManagedAPFailedEntriesPurge_Type(Integer32):
    """Custom type wsManagedAPFailedEntriesPurge based on Integer32"""
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


_WsManagedAPFailedEntriesPurge_Type.__name__ = "Integer32"
_WsManagedAPFailedEntriesPurge_Object = MibScalar
wsManagedAPFailedEntriesPurge = _WsManagedAPFailedEntriesPurge_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 2),
    _WsManagedAPFailedEntriesPurge_Type()
)
wsManagedAPFailedEntriesPurge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPFailedEntriesPurge.setStatus("current")
_WsManagedAPStatisticsTable_Object = MibTable
wsManagedAPStatisticsTable = _WsManagedAPStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 3)
)
if mibBuilder.loadTexts:
    wsManagedAPStatisticsTable.setStatus("current")
_WsManagedAPStatisticsEntry_Object = MibTableRow
wsManagedAPStatisticsEntry = _WsManagedAPStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 3, 1)
)
if mibBuilder.loadTexts:
    wsManagedAPStatisticsEntry.setStatus("current")
_WsManagedAPWLANPktsRecvd_Type = Counter64
_WsManagedAPWLANPktsRecvd_Object = MibTableColumn
wsManagedAPWLANPktsRecvd = _WsManagedAPWLANPktsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 3, 1, 1),
    _WsManagedAPWLANPktsRecvd_Type()
)
wsManagedAPWLANPktsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPWLANPktsRecvd.setStatus("current")
_WsManagedAPWLANBytesRecvd_Type = Counter64
_WsManagedAPWLANBytesRecvd_Object = MibTableColumn
wsManagedAPWLANBytesRecvd = _WsManagedAPWLANBytesRecvd_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 3, 1, 2),
    _WsManagedAPWLANBytesRecvd_Type()
)
wsManagedAPWLANBytesRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPWLANBytesRecvd.setStatus("current")
_WsManagedAPWLANPktsTransmitted_Type = Counter64
_WsManagedAPWLANPktsTransmitted_Object = MibTableColumn
wsManagedAPWLANPktsTransmitted = _WsManagedAPWLANPktsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 3, 1, 3),
    _WsManagedAPWLANPktsTransmitted_Type()
)
wsManagedAPWLANPktsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPWLANPktsTransmitted.setStatus("current")
_WsManagedAPWLANBytesTransmitted_Type = Counter64
_WsManagedAPWLANBytesTransmitted_Object = MibTableColumn
wsManagedAPWLANBytesTransmitted = _WsManagedAPWLANBytesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 3, 1, 4),
    _WsManagedAPWLANBytesTransmitted_Type()
)
wsManagedAPWLANBytesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPWLANBytesTransmitted.setStatus("current")
_WsManagedAPEthernetPktsRecvd_Type = Counter64
_WsManagedAPEthernetPktsRecvd_Object = MibTableColumn
wsManagedAPEthernetPktsRecvd = _WsManagedAPEthernetPktsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 3, 1, 5),
    _WsManagedAPEthernetPktsRecvd_Type()
)
wsManagedAPEthernetPktsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPEthernetPktsRecvd.setStatus("current")
_WsManagedAPEthernetBytesRecvd_Type = Counter64
_WsManagedAPEthernetBytesRecvd_Object = MibTableColumn
wsManagedAPEthernetBytesRecvd = _WsManagedAPEthernetBytesRecvd_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 3, 1, 6),
    _WsManagedAPEthernetBytesRecvd_Type()
)
wsManagedAPEthernetBytesRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPEthernetBytesRecvd.setStatus("current")
_WsManagedAPEthernetMcastPktsRecvd_Type = Counter64
_WsManagedAPEthernetMcastPktsRecvd_Object = MibTableColumn
wsManagedAPEthernetMcastPktsRecvd = _WsManagedAPEthernetMcastPktsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 3, 1, 7),
    _WsManagedAPEthernetMcastPktsRecvd_Type()
)
wsManagedAPEthernetMcastPktsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPEthernetMcastPktsRecvd.setStatus("current")
_WsManagedAPEthernetPktsTransmitted_Type = Counter64
_WsManagedAPEthernetPktsTransmitted_Object = MibTableColumn
wsManagedAPEthernetPktsTransmitted = _WsManagedAPEthernetPktsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 3, 1, 8),
    _WsManagedAPEthernetPktsTransmitted_Type()
)
wsManagedAPEthernetPktsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPEthernetPktsTransmitted.setStatus("current")
_WsManagedAPEthernetBytesTransmitted_Type = Counter64
_WsManagedAPEthernetBytesTransmitted_Object = MibTableColumn
wsManagedAPEthernetBytesTransmitted = _WsManagedAPEthernetBytesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 3, 1, 9),
    _WsManagedAPEthernetBytesTransmitted_Type()
)
wsManagedAPEthernetBytesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPEthernetBytesTransmitted.setStatus("current")
_WsManagedAPEthernetTransmitErrorCount_Type = Counter64
_WsManagedAPEthernetTransmitErrorCount_Object = MibTableColumn
wsManagedAPEthernetTransmitErrorCount = _WsManagedAPEthernetTransmitErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 3, 1, 10),
    _WsManagedAPEthernetTransmitErrorCount_Type()
)
wsManagedAPEthernetTransmitErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPEthernetTransmitErrorCount.setStatus("current")
_WsManagedAPEthernetRecvdErrorCount_Type = Counter64
_WsManagedAPEthernetRecvdErrorCount_Object = MibTableColumn
wsManagedAPEthernetRecvdErrorCount = _WsManagedAPEthernetRecvdErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 3, 1, 11),
    _WsManagedAPEthernetRecvdErrorCount_Type()
)
wsManagedAPEthernetRecvdErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPEthernetRecvdErrorCount.setStatus("current")
_WsManagedAPCL2TunnelBytesRecvd_Type = Counter64
_WsManagedAPCL2TunnelBytesRecvd_Object = MibTableColumn
wsManagedAPCL2TunnelBytesRecvd = _WsManagedAPCL2TunnelBytesRecvd_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 3, 1, 12),
    _WsManagedAPCL2TunnelBytesRecvd_Type()
)
wsManagedAPCL2TunnelBytesRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPCL2TunnelBytesRecvd.setStatus("current")
_WsManagedAPCL2TunnelPktsRecvd_Type = Counter64
_WsManagedAPCL2TunnelPktsRecvd_Object = MibTableColumn
wsManagedAPCL2TunnelPktsRecvd = _WsManagedAPCL2TunnelPktsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 3, 1, 13),
    _WsManagedAPCL2TunnelPktsRecvd_Type()
)
wsManagedAPCL2TunnelPktsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPCL2TunnelPktsRecvd.setStatus("current")
_WsManagedAPCL2TunnelMcastRecvd_Type = Counter64
_WsManagedAPCL2TunnelMcastRecvd_Object = MibTableColumn
wsManagedAPCL2TunnelMcastRecvd = _WsManagedAPCL2TunnelMcastRecvd_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 3, 1, 14),
    _WsManagedAPCL2TunnelMcastRecvd_Type()
)
wsManagedAPCL2TunnelMcastRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPCL2TunnelMcastRecvd.setStatus("current")
_WsManagedAPCL2TunnelBytesTransmitted_Type = Counter64
_WsManagedAPCL2TunnelBytesTransmitted_Object = MibTableColumn
wsManagedAPCL2TunnelBytesTransmitted = _WsManagedAPCL2TunnelBytesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 3, 1, 15),
    _WsManagedAPCL2TunnelBytesTransmitted_Type()
)
wsManagedAPCL2TunnelBytesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPCL2TunnelBytesTransmitted.setStatus("current")
_WsManagedAPCL2TunnelPktsTransmitted_Type = Counter64
_WsManagedAPCL2TunnelPktsTransmitted_Object = MibTableColumn
wsManagedAPCL2TunnelPktsTransmitted = _WsManagedAPCL2TunnelPktsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 3, 1, 16),
    _WsManagedAPCL2TunnelPktsTransmitted_Type()
)
wsManagedAPCL2TunnelPktsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPCL2TunnelPktsTransmitted.setStatus("current")
_WsManagedAPCL2TunnelMcastTransmitted_Type = Counter64
_WsManagedAPCL2TunnelMcastTransmitted_Object = MibTableColumn
wsManagedAPCL2TunnelMcastTransmitted = _WsManagedAPCL2TunnelMcastTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 3, 1, 17),
    _WsManagedAPCL2TunnelMcastTransmitted_Type()
)
wsManagedAPCL2TunnelMcastTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPCL2TunnelMcastTransmitted.setStatus("current")
_WsManagedAPWLANPktsRecvDropped_Type = Counter64
_WsManagedAPWLANPktsRecvDropped_Object = MibTableColumn
wsManagedAPWLANPktsRecvDropped = _WsManagedAPWLANPktsRecvDropped_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 3, 1, 18),
    _WsManagedAPWLANPktsRecvDropped_Type()
)
wsManagedAPWLANPktsRecvDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPWLANPktsRecvDropped.setStatus("current")
_WsManagedAPWLANBytesRecvDropped_Type = Counter64
_WsManagedAPWLANBytesRecvDropped_Object = MibTableColumn
wsManagedAPWLANBytesRecvDropped = _WsManagedAPWLANBytesRecvDropped_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 3, 1, 19),
    _WsManagedAPWLANBytesRecvDropped_Type()
)
wsManagedAPWLANBytesRecvDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPWLANBytesRecvDropped.setStatus("current")
_WsManagedAPWLANPktsTransmitDropped_Type = Counter64
_WsManagedAPWLANPktsTransmitDropped_Object = MibTableColumn
wsManagedAPWLANPktsTransmitDropped = _WsManagedAPWLANPktsTransmitDropped_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 3, 1, 20),
    _WsManagedAPWLANPktsTransmitDropped_Type()
)
wsManagedAPWLANPktsTransmitDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPWLANPktsTransmitDropped.setStatus("current")
_WsManagedAPWLANBytesTransmitDropped_Type = Counter64
_WsManagedAPWLANBytesTransmitDropped_Object = MibTableColumn
wsManagedAPWLANBytesTransmitDropped = _WsManagedAPWLANBytesTransmitDropped_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 3, 1, 21),
    _WsManagedAPWLANBytesTransmitDropped_Type()
)
wsManagedAPWLANBytesTransmitDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPWLANBytesTransmitDropped.setStatus("current")
_WsManagedAPDistTunnelBytesTransmitted_Type = Counter64
_WsManagedAPDistTunnelBytesTransmitted_Object = MibTableColumn
wsManagedAPDistTunnelBytesTransmitted = _WsManagedAPDistTunnelBytesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 3, 1, 22),
    _WsManagedAPDistTunnelBytesTransmitted_Type()
)
wsManagedAPDistTunnelBytesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPDistTunnelBytesTransmitted.setStatus("current")
_WsManagedAPDistTunnelBytesReceived_Type = Counter64
_WsManagedAPDistTunnelBytesReceived_Object = MibTableColumn
wsManagedAPDistTunnelBytesReceived = _WsManagedAPDistTunnelBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 3, 1, 23),
    _WsManagedAPDistTunnelBytesReceived_Type()
)
wsManagedAPDistTunnelBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPDistTunnelBytesReceived.setStatus("current")
_WsManagedAPDistTunnelPacketsTransmitted_Type = Counter64
_WsManagedAPDistTunnelPacketsTransmitted_Object = MibTableColumn
wsManagedAPDistTunnelPacketsTransmitted = _WsManagedAPDistTunnelPacketsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 3, 1, 24),
    _WsManagedAPDistTunnelPacketsTransmitted_Type()
)
wsManagedAPDistTunnelPacketsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPDistTunnelPacketsTransmitted.setStatus("current")
_WsManagedAPDistTunnelPacketsReceived_Type = Counter64
_WsManagedAPDistTunnelPacketsReceived_Object = MibTableColumn
wsManagedAPDistTunnelPacketsReceived = _WsManagedAPDistTunnelPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 3, 1, 25),
    _WsManagedAPDistTunnelPacketsReceived_Type()
)
wsManagedAPDistTunnelPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPDistTunnelPacketsReceived.setStatus("current")
_WsManagedAPDistTunnelMcastPacketsTransmitted_Type = Counter64
_WsManagedAPDistTunnelMcastPacketsTransmitted_Object = MibTableColumn
wsManagedAPDistTunnelMcastPacketsTransmitted = _WsManagedAPDistTunnelMcastPacketsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 3, 1, 26),
    _WsManagedAPDistTunnelMcastPacketsTransmitted_Type()
)
wsManagedAPDistTunnelMcastPacketsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPDistTunnelMcastPacketsTransmitted.setStatus("current")
_WsManagedAPDistTunnelMcastPacketsReceived_Type = Counter64
_WsManagedAPDistTunnelMcastPacketsReceived_Object = MibTableColumn
wsManagedAPDistTunnelMcastPacketsReceived = _WsManagedAPDistTunnelMcastPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 3, 1, 27),
    _WsManagedAPDistTunnelMcastPacketsReceived_Type()
)
wsManagedAPDistTunnelMcastPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPDistTunnelMcastPacketsReceived.setStatus("current")
_WsManagedAPDistTunnelRoamedClients_Type = Unsigned32
_WsManagedAPDistTunnelRoamedClients_Object = MibTableColumn
wsManagedAPDistTunnelRoamedClients = _WsManagedAPDistTunnelRoamedClients_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 3, 1, 28),
    _WsManagedAPDistTunnelRoamedClients_Type()
)
wsManagedAPDistTunnelRoamedClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPDistTunnelRoamedClients.setStatus("current")
_WsManagedAPDistTunnelRoamedClientsIdleTimedOut_Type = Unsigned32
_WsManagedAPDistTunnelRoamedClientsIdleTimedOut_Object = MibTableColumn
wsManagedAPDistTunnelRoamedClientsIdleTimedOut = _WsManagedAPDistTunnelRoamedClientsIdleTimedOut_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 3, 1, 29),
    _WsManagedAPDistTunnelRoamedClientsIdleTimedOut_Type()
)
wsManagedAPDistTunnelRoamedClientsIdleTimedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPDistTunnelRoamedClientsIdleTimedOut.setStatus("current")
_WsManagedAPDistTunnelRoamedClientsAgeTimedOut_Type = Unsigned32
_WsManagedAPDistTunnelRoamedClientsAgeTimedOut_Object = MibTableColumn
wsManagedAPDistTunnelRoamedClientsAgeTimedOut = _WsManagedAPDistTunnelRoamedClientsAgeTimedOut_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 3, 1, 30),
    _WsManagedAPDistTunnelRoamedClientsAgeTimedOut_Type()
)
wsManagedAPDistTunnelRoamedClientsAgeTimedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPDistTunnelRoamedClientsAgeTimedOut.setStatus("current")
_WsManagedAPDistTunnelMaxClientLimitSetupDenials_Type = Unsigned32
_WsManagedAPDistTunnelMaxClientLimitSetupDenials_Object = MibTableColumn
wsManagedAPDistTunnelMaxClientLimitSetupDenials = _WsManagedAPDistTunnelMaxClientLimitSetupDenials_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 3, 1, 31),
    _WsManagedAPDistTunnelMaxClientLimitSetupDenials_Type()
)
wsManagedAPDistTunnelMaxClientLimitSetupDenials.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPDistTunnelMaxClientLimitSetupDenials.setStatus("current")
_WsManagedAPDistTunnelMaxReplSetupDenials_Type = Unsigned32
_WsManagedAPDistTunnelMaxReplSetupDenials_Object = MibTableColumn
wsManagedAPDistTunnelMaxReplSetupDenials = _WsManagedAPDistTunnelMaxReplSetupDenials_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 3, 1, 32),
    _WsManagedAPDistTunnelMaxReplSetupDenials_Type()
)
wsManagedAPDistTunnelMaxReplSetupDenials.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPDistTunnelMaxReplSetupDenials.setStatus("current")
_WsManagedAPARPReqsFromBcastToUcast_Type = Unsigned32
_WsManagedAPARPReqsFromBcastToUcast_Object = MibTableColumn
wsManagedAPARPReqsFromBcastToUcast = _WsManagedAPARPReqsFromBcastToUcast_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 3, 1, 33),
    _WsManagedAPARPReqsFromBcastToUcast_Type()
)
wsManagedAPARPReqsFromBcastToUcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPARPReqsFromBcastToUcast.setStatus("current")
_WsManagedAPFilteredARPRequest_Type = Unsigned32
_WsManagedAPFilteredARPRequest_Object = MibTableColumn
wsManagedAPFilteredARPRequest = _WsManagedAPFilteredARPRequest_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 3, 1, 34),
    _WsManagedAPFilteredARPRequest_Type()
)
wsManagedAPFilteredARPRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPFilteredARPRequest.setStatus("current")
_WsManagedAPBroadcastedARPRequests_Type = Unsigned32
_WsManagedAPBroadcastedARPRequests_Object = MibTableColumn
wsManagedAPBroadcastedARPRequests = _WsManagedAPBroadcastedARPRequests_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 3, 1, 35),
    _WsManagedAPBroadcastedARPRequests_Type()
)
wsManagedAPBroadcastedARPRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPBroadcastedARPRequests.setStatus("current")
_WsManagedAPRadioStatusTable_Object = MibTable
wsManagedAPRadioStatusTable = _WsManagedAPRadioStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 4)
)
if mibBuilder.loadTexts:
    wsManagedAPRadioStatusTable.setStatus("current")
_WsManagedAPRadioStatusEntry_Object = MibTableRow
wsManagedAPRadioStatusEntry = _WsManagedAPRadioStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 4, 1)
)
wsManagedAPRadioStatusEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsManagedAPMacAddress"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsManagedAPRadioInterface"),
)
if mibBuilder.loadTexts:
    wsManagedAPRadioStatusEntry.setStatus("current")


class _WsManagedAPRadioInterface_Type(Integer32):
    """Custom type wsManagedAPRadioInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WsManagedAPRadioInterface_Type.__name__ = "Integer32"
_WsManagedAPRadioInterface_Object = MibTableColumn
wsManagedAPRadioInterface = _WsManagedAPRadioInterface_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 4, 1, 1),
    _WsManagedAPRadioInterface_Type()
)
wsManagedAPRadioInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPRadioInterface.setStatus("current")
_WsManagedAPRadioMacAddress_Type = MacAddress
_WsManagedAPRadioMacAddress_Object = MibTableColumn
wsManagedAPRadioMacAddress = _WsManagedAPRadioMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 4, 1, 2),
    _WsManagedAPRadioMacAddress_Type()
)
wsManagedAPRadioMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPRadioMacAddress.setStatus("current")


class _WsManagedAPRadioChannel_Type(Integer32):
    """Custom type wsManagedAPRadioChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 13),
        ValueRangeConstraint(36, 36),
        ValueRangeConstraint(40, 40),
        ValueRangeConstraint(44, 44),
        ValueRangeConstraint(48, 48),
        ValueRangeConstraint(52, 52),
        ValueRangeConstraint(56, 56),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(64, 64),
    )


_WsManagedAPRadioChannel_Type.__name__ = "Integer32"
_WsManagedAPRadioChannel_Object = MibTableColumn
wsManagedAPRadioChannel = _WsManagedAPRadioChannel_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 4, 1, 3),
    _WsManagedAPRadioChannel_Type()
)
wsManagedAPRadioChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPRadioChannel.setStatus("current")


class _WsManagedAPRadioTxPower_Type(Integer32):
    """Custom type wsManagedAPRadioTxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_WsManagedAPRadioTxPower_Type.__name__ = "Integer32"
_WsManagedAPRadioTxPower_Object = MibTableColumn
wsManagedAPRadioTxPower = _WsManagedAPRadioTxPower_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 4, 1, 4),
    _WsManagedAPRadioTxPower_Type()
)
wsManagedAPRadioTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPRadioTxPower.setStatus("current")
_WsManagedAPRadioAuthenticatedClients_Type = Unsigned32
_WsManagedAPRadioAuthenticatedClients_Object = MibTableColumn
wsManagedAPRadioAuthenticatedClients = _WsManagedAPRadioAuthenticatedClients_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 4, 1, 5),
    _WsManagedAPRadioAuthenticatedClients_Type()
)
wsManagedAPRadioAuthenticatedClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPRadioAuthenticatedClients.setStatus("current")


class _WsManagedAPRadioWLANUtilization_Type(Integer32):
    """Custom type wsManagedAPRadioWLANUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_WsManagedAPRadioWLANUtilization_Type.__name__ = "Integer32"
_WsManagedAPRadioWLANUtilization_Object = MibTableColumn
wsManagedAPRadioWLANUtilization = _WsManagedAPRadioWLANUtilization_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 4, 1, 6),
    _WsManagedAPRadioWLANUtilization_Type()
)
wsManagedAPRadioWLANUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPRadioWLANUtilization.setStatus("current")


class _WsManagedAPRadioFixedChannelIndicator_Type(Integer32):
    """Custom type wsManagedAPRadioFixedChannelIndicator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_WsManagedAPRadioFixedChannelIndicator_Type.__name__ = "Integer32"
_WsManagedAPRadioFixedChannelIndicator_Object = MibTableColumn
wsManagedAPRadioFixedChannelIndicator = _WsManagedAPRadioFixedChannelIndicator_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 4, 1, 7),
    _WsManagedAPRadioFixedChannelIndicator_Type()
)
wsManagedAPRadioFixedChannelIndicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPRadioFixedChannelIndicator.setStatus("current")


class _WsManagedAPRadioMCAStatus_Type(Integer32):
    """Custom type wsManagedAPRadioMCAStatus based on Integer32"""
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
          ("in-progress", 2),
          ("complete", 3),
          ("failure", 4))
    )


_WsManagedAPRadioMCAStatus_Type.__name__ = "Integer32"
_WsManagedAPRadioMCAStatus_Object = MibTableColumn
wsManagedAPRadioMCAStatus = _WsManagedAPRadioMCAStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 4, 1, 8),
    _WsManagedAPRadioMCAStatus_Type()
)
wsManagedAPRadioMCAStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPRadioMCAStatus.setStatus("current")


class _WsManagedAPRadioFixedPowerIndicator_Type(Integer32):
    """Custom type wsManagedAPRadioFixedPowerIndicator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_WsManagedAPRadioFixedPowerIndicator_Type.__name__ = "Integer32"
_WsManagedAPRadioFixedPowerIndicator_Object = MibTableColumn
wsManagedAPRadioFixedPowerIndicator = _WsManagedAPRadioFixedPowerIndicator_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 4, 1, 9),
    _WsManagedAPRadioFixedPowerIndicator_Type()
)
wsManagedAPRadioFixedPowerIndicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPRadioFixedPowerIndicator.setStatus("current")


class _WsManagedAPRadioMPAStatus_Type(Integer32):
    """Custom type wsManagedAPRadioMPAStatus based on Integer32"""
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
          ("in-progress", 2),
          ("complete", 3),
          ("failure", 4))
    )


_WsManagedAPRadioMPAStatus_Type.__name__ = "Integer32"
_WsManagedAPRadioMPAStatus_Object = MibTableColumn
wsManagedAPRadioMPAStatus = _WsManagedAPRadioMPAStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 4, 1, 10),
    _WsManagedAPRadioMPAStatus_Type()
)
wsManagedAPRadioMPAStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPRadioMPAStatus.setStatus("current")
_WsManagedAPRadioNeighborCount_Type = Unsigned32
_WsManagedAPRadioNeighborCount_Object = MibTableColumn
wsManagedAPRadioNeighborCount = _WsManagedAPRadioNeighborCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 4, 1, 11),
    _WsManagedAPRadioNeighborCount_Type()
)
wsManagedAPRadioNeighborCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPRadioNeighborCount.setStatus("current")


class _WsManagedAPRadioFixedChannelAction_Type(Integer32):
    """Custom type wsManagedAPRadioFixedChannelAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("apply", 2))
    )


_WsManagedAPRadioFixedChannelAction_Type.__name__ = "Integer32"
_WsManagedAPRadioFixedChannelAction_Object = MibTableColumn
wsManagedAPRadioFixedChannelAction = _WsManagedAPRadioFixedChannelAction_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 4, 1, 12),
    _WsManagedAPRadioFixedChannelAction_Type()
)
wsManagedAPRadioFixedChannelAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPRadioFixedChannelAction.setStatus("current")


class _WsManagedAPRadioFixedChannel_Type(Integer32):
    """Custom type wsManagedAPRadioFixedChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 13),
        ValueRangeConstraint(36, 36),
        ValueRangeConstraint(40, 40),
        ValueRangeConstraint(44, 44),
        ValueRangeConstraint(48, 48),
        ValueRangeConstraint(52, 52),
        ValueRangeConstraint(56, 56),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(64, 64),
    )


_WsManagedAPRadioFixedChannel_Type.__name__ = "Integer32"
_WsManagedAPRadioFixedChannel_Object = MibTableColumn
wsManagedAPRadioFixedChannel = _WsManagedAPRadioFixedChannel_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 4, 1, 13),
    _WsManagedAPRadioFixedChannel_Type()
)
wsManagedAPRadioFixedChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPRadioFixedChannel.setStatus("current")


class _WsManagedAPRadioFixedPowerAction_Type(Integer32):
    """Custom type wsManagedAPRadioFixedPowerAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("apply", 2))
    )


_WsManagedAPRadioFixedPowerAction_Type.__name__ = "Integer32"
_WsManagedAPRadioFixedPowerAction_Object = MibTableColumn
wsManagedAPRadioFixedPowerAction = _WsManagedAPRadioFixedPowerAction_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 4, 1, 14),
    _WsManagedAPRadioFixedPowerAction_Type()
)
wsManagedAPRadioFixedPowerAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPRadioFixedPowerAction.setStatus("current")


class _WsManagedAPRadioFixedPower_Type(Integer32):
    """Custom type wsManagedAPRadioFixedPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WsManagedAPRadioFixedPower_Type.__name__ = "Integer32"
_WsManagedAPRadioFixedPower_Object = MibTableColumn
wsManagedAPRadioFixedPower = _WsManagedAPRadioFixedPower_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 4, 1, 15),
    _WsManagedAPRadioFixedPower_Type()
)
wsManagedAPRadioFixedPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPRadioFixedPower.setStatus("current")


class _WsManagedAPRadioBandwidth_Type(Integer32):
    """Custom type wsManagedAPRadioBandwidth based on Integer32"""
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
          ("twentyMHz", 1),
          ("fortyMHz", 2),
          ("eightyMHz", 3))
    )


_WsManagedAPRadioBandwidth_Type.__name__ = "Integer32"
_WsManagedAPRadioBandwidth_Object = MibTableColumn
wsManagedAPRadioBandwidth = _WsManagedAPRadioBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 4, 1, 16),
    _WsManagedAPRadioBandwidth_Type()
)
wsManagedAPRadioBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPRadioBandwidth.setStatus("current")


class _WsManagedAPRadioResourceMeasEnabled_Type(Integer32):
    """Custom type wsManagedAPRadioResourceMeasEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_WsManagedAPRadioResourceMeasEnabled_Type.__name__ = "Integer32"
_WsManagedAPRadioResourceMeasEnabled_Object = MibTableColumn
wsManagedAPRadioResourceMeasEnabled = _WsManagedAPRadioResourceMeasEnabled_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 4, 1, 17),
    _WsManagedAPRadioResourceMeasEnabled_Type()
)
wsManagedAPRadioResourceMeasEnabled.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsManagedAPRadioResourceMeasEnabled.setStatus("current")
_WsManagedAPRadioStatisticsTable_Object = MibTable
wsManagedAPRadioStatisticsTable = _WsManagedAPRadioStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 5)
)
if mibBuilder.loadTexts:
    wsManagedAPRadioStatisticsTable.setStatus("current")
_WsManagedAPRadioStatisticsEntry_Object = MibTableRow
wsManagedAPRadioStatisticsEntry = _WsManagedAPRadioStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 5, 1)
)
if mibBuilder.loadTexts:
    wsManagedAPRadioStatisticsEntry.setStatus("current")
_WsManagedAPRadioWLANPktsRecvd_Type = Counter64
_WsManagedAPRadioWLANPktsRecvd_Object = MibTableColumn
wsManagedAPRadioWLANPktsRecvd = _WsManagedAPRadioWLANPktsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 5, 1, 1),
    _WsManagedAPRadioWLANPktsRecvd_Type()
)
wsManagedAPRadioWLANPktsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPRadioWLANPktsRecvd.setStatus("current")
_WsManagedAPRadioWLANBytesRecvd_Type = Counter64
_WsManagedAPRadioWLANBytesRecvd_Object = MibTableColumn
wsManagedAPRadioWLANBytesRecvd = _WsManagedAPRadioWLANBytesRecvd_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 5, 1, 2),
    _WsManagedAPRadioWLANBytesRecvd_Type()
)
wsManagedAPRadioWLANBytesRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPRadioWLANBytesRecvd.setStatus("current")
_WsManagedAPRadioWLANPktsTransmitted_Type = Counter64
_WsManagedAPRadioWLANPktsTransmitted_Object = MibTableColumn
wsManagedAPRadioWLANPktsTransmitted = _WsManagedAPRadioWLANPktsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 5, 1, 3),
    _WsManagedAPRadioWLANPktsTransmitted_Type()
)
wsManagedAPRadioWLANPktsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPRadioWLANPktsTransmitted.setStatus("current")
_WsManagedAPRadioWLANBytesTransmitted_Type = Counter64
_WsManagedAPRadioWLANBytesTransmitted_Object = MibTableColumn
wsManagedAPRadioWLANBytesTransmitted = _WsManagedAPRadioWLANBytesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 5, 1, 4),
    _WsManagedAPRadioWLANBytesTransmitted_Type()
)
wsManagedAPRadioWLANBytesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPRadioWLANBytesTransmitted.setStatus("current")
_WsManagedAPRadioTxFragmentCount_Type = Counter32
_WsManagedAPRadioTxFragmentCount_Object = MibTableColumn
wsManagedAPRadioTxFragmentCount = _WsManagedAPRadioTxFragmentCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 5, 1, 5),
    _WsManagedAPRadioTxFragmentCount_Type()
)
wsManagedAPRadioTxFragmentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPRadioTxFragmentCount.setStatus("current")
_WsManagedAPRadioMcastTxFrameCount_Type = Counter32
_WsManagedAPRadioMcastTxFrameCount_Object = MibTableColumn
wsManagedAPRadioMcastTxFrameCount = _WsManagedAPRadioMcastTxFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 5, 1, 6),
    _WsManagedAPRadioMcastTxFrameCount_Type()
)
wsManagedAPRadioMcastTxFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPRadioMcastTxFrameCount.setStatus("current")
_WsManagedAPRadioFailedCount_Type = Counter32
_WsManagedAPRadioFailedCount_Object = MibTableColumn
wsManagedAPRadioFailedCount = _WsManagedAPRadioFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 5, 1, 7),
    _WsManagedAPRadioFailedCount_Type()
)
wsManagedAPRadioFailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPRadioFailedCount.setStatus("current")
_WsManagedAPRadioRetryCount_Type = Counter32
_WsManagedAPRadioRetryCount_Object = MibTableColumn
wsManagedAPRadioRetryCount = _WsManagedAPRadioRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 5, 1, 8),
    _WsManagedAPRadioRetryCount_Type()
)
wsManagedAPRadioRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPRadioRetryCount.setStatus("current")
_WsManagedAPRadioMultipleRetryCount_Type = Counter32
_WsManagedAPRadioMultipleRetryCount_Object = MibTableColumn
wsManagedAPRadioMultipleRetryCount = _WsManagedAPRadioMultipleRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 5, 1, 9),
    _WsManagedAPRadioMultipleRetryCount_Type()
)
wsManagedAPRadioMultipleRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPRadioMultipleRetryCount.setStatus("current")
_WsManagedAPRadioFrameDuplicateCount_Type = Counter32
_WsManagedAPRadioFrameDuplicateCount_Object = MibTableColumn
wsManagedAPRadioFrameDuplicateCount = _WsManagedAPRadioFrameDuplicateCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 5, 1, 10),
    _WsManagedAPRadioFrameDuplicateCount_Type()
)
wsManagedAPRadioFrameDuplicateCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPRadioFrameDuplicateCount.setStatus("current")
_WsManagedAPRadioRTSSuccessCount_Type = Counter32
_WsManagedAPRadioRTSSuccessCount_Object = MibTableColumn
wsManagedAPRadioRTSSuccessCount = _WsManagedAPRadioRTSSuccessCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 5, 1, 11),
    _WsManagedAPRadioRTSSuccessCount_Type()
)
wsManagedAPRadioRTSSuccessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPRadioRTSSuccessCount.setStatus("current")
_WsManagedAPRadioRTSFailureCount_Type = Counter32
_WsManagedAPRadioRTSFailureCount_Object = MibTableColumn
wsManagedAPRadioRTSFailureCount = _WsManagedAPRadioRTSFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 5, 1, 12),
    _WsManagedAPRadioRTSFailureCount_Type()
)
wsManagedAPRadioRTSFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPRadioRTSFailureCount.setStatus("current")
_WsManagedAPRadioACKFailureCount_Type = Counter32
_WsManagedAPRadioACKFailureCount_Object = MibTableColumn
wsManagedAPRadioACKFailureCount = _WsManagedAPRadioACKFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 5, 1, 13),
    _WsManagedAPRadioACKFailureCount_Type()
)
wsManagedAPRadioACKFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPRadioACKFailureCount.setStatus("current")
_WsManagedAPRadioRecvdFragmentCount_Type = Counter32
_WsManagedAPRadioRecvdFragmentCount_Object = MibTableColumn
wsManagedAPRadioRecvdFragmentCount = _WsManagedAPRadioRecvdFragmentCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 5, 1, 14),
    _WsManagedAPRadioRecvdFragmentCount_Type()
)
wsManagedAPRadioRecvdFragmentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPRadioRecvdFragmentCount.setStatus("current")
_WsManagedAPRadioMcastRecvdFrameCount_Type = Counter32
_WsManagedAPRadioMcastRecvdFrameCount_Object = MibTableColumn
wsManagedAPRadioMcastRecvdFrameCount = _WsManagedAPRadioMcastRecvdFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 5, 1, 15),
    _WsManagedAPRadioMcastRecvdFrameCount_Type()
)
wsManagedAPRadioMcastRecvdFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPRadioMcastRecvdFrameCount.setStatus("current")
_WsManagedAPRadioFCSErrorCount_Type = Counter32
_WsManagedAPRadioFCSErrorCount_Object = MibTableColumn
wsManagedAPRadioFCSErrorCount = _WsManagedAPRadioFCSErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 5, 1, 16),
    _WsManagedAPRadioFCSErrorCount_Type()
)
wsManagedAPRadioFCSErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPRadioFCSErrorCount.setStatus("current")
_WsManagedAPRadioTxFrameCount_Type = Counter32
_WsManagedAPRadioTxFrameCount_Object = MibTableColumn
wsManagedAPRadioTxFrameCount = _WsManagedAPRadioTxFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 5, 1, 17),
    _WsManagedAPRadioTxFrameCount_Type()
)
wsManagedAPRadioTxFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPRadioTxFrameCount.setStatus("current")
_WsManagedAPRadioWEPUndecryptableCount_Type = Counter32
_WsManagedAPRadioWEPUndecryptableCount_Object = MibTableColumn
wsManagedAPRadioWEPUndecryptableCount = _WsManagedAPRadioWEPUndecryptableCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 5, 1, 18),
    _WsManagedAPRadioWEPUndecryptableCount_Type()
)
wsManagedAPRadioWEPUndecryptableCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPRadioWEPUndecryptableCount.setStatus("current")
_WsManagedAPRadioWLANPktsRecvDropped_Type = Counter64
_WsManagedAPRadioWLANPktsRecvDropped_Object = MibTableColumn
wsManagedAPRadioWLANPktsRecvDropped = _WsManagedAPRadioWLANPktsRecvDropped_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 5, 1, 19),
    _WsManagedAPRadioWLANPktsRecvDropped_Type()
)
wsManagedAPRadioWLANPktsRecvDropped.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsManagedAPRadioWLANPktsRecvDropped.setStatus("current")
_WsManagedAPRadioWLANBytesRecvDropped_Type = Counter64
_WsManagedAPRadioWLANBytesRecvDropped_Object = MibTableColumn
wsManagedAPRadioWLANBytesRecvDropped = _WsManagedAPRadioWLANBytesRecvDropped_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 5, 1, 20),
    _WsManagedAPRadioWLANBytesRecvDropped_Type()
)
wsManagedAPRadioWLANBytesRecvDropped.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsManagedAPRadioWLANBytesRecvDropped.setStatus("current")
_WsManagedAPRadioWLANPktsTransmitDropped_Type = Counter64
_WsManagedAPRadioWLANPktsTransmitDropped_Object = MibTableColumn
wsManagedAPRadioWLANPktsTransmitDropped = _WsManagedAPRadioWLANPktsTransmitDropped_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 5, 1, 21),
    _WsManagedAPRadioWLANPktsTransmitDropped_Type()
)
wsManagedAPRadioWLANPktsTransmitDropped.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsManagedAPRadioWLANPktsTransmitDropped.setStatus("current")
_WsManagedAPRadioWLANBytesTransmitDropped_Type = Counter64
_WsManagedAPRadioWLANBytesTransmitDropped_Object = MibTableColumn
wsManagedAPRadioWLANBytesTransmitDropped = _WsManagedAPRadioWLANBytesTransmitDropped_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 5, 1, 22),
    _WsManagedAPRadioWLANBytesTransmitDropped_Type()
)
wsManagedAPRadioWLANBytesTransmitDropped.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsManagedAPRadioWLANBytesTransmitDropped.setStatus("current")
_WsManagedAPNeighborAPListTable_Object = MibTable
wsManagedAPNeighborAPListTable = _WsManagedAPNeighborAPListTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 6)
)
if mibBuilder.loadTexts:
    wsManagedAPNeighborAPListTable.setStatus("current")
_WsManagedAPNeighborAPListEntry_Object = MibTableRow
wsManagedAPNeighborAPListEntry = _WsManagedAPNeighborAPListEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 6, 1)
)
wsManagedAPNeighborAPListEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsManagedAPMacAddress"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsManagedAPRadioInterface"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsNeighborMacAddress"),
)
if mibBuilder.loadTexts:
    wsManagedAPNeighborAPListEntry.setStatus("current")
_WsNeighborMacAddress_Type = MacAddress
_WsNeighborMacAddress_Object = MibTableColumn
wsNeighborMacAddress = _WsNeighborMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 6, 1, 1),
    _WsNeighborMacAddress_Type()
)
wsNeighborMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNeighborMacAddress.setStatus("current")


class _WsNeighborSSID_Type(DisplayString):
    """Custom type wsNeighborSSID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WsNeighborSSID_Type.__name__ = "DisplayString"
_WsNeighborSSID_Object = MibTableColumn
wsNeighborSSID = _WsNeighborSSID_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 6, 1, 2),
    _WsNeighborSSID_Type()
)
wsNeighborSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNeighborSSID.setStatus("current")


class _WsNeighborRSSI_Type(Integer32):
    """Custom type wsNeighborRSSI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_WsNeighborRSSI_Type.__name__ = "Integer32"
_WsNeighborRSSI_Object = MibTableColumn
wsNeighborRSSI = _WsNeighborRSSI_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 6, 1, 3),
    _WsNeighborRSSI_Type()
)
wsNeighborRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNeighborRSSI.setStatus("current")


class _WsNeighborStatus_Type(Integer32):
    """Custom type wsNeighborStatus based on Integer32"""
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
        *(("managed", 1),
          ("unknown", 2),
          ("standalone", 3),
          ("rogue", 4))
    )


_WsNeighborStatus_Type.__name__ = "Integer32"
_WsNeighborStatus_Object = MibTableColumn
wsNeighborStatus = _WsNeighborStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 6, 1, 4),
    _WsNeighborStatus_Type()
)
wsNeighborStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNeighborStatus.setStatus("current")
_WsNeighborAge_Type = TimeTicks
_WsNeighborAge_Object = MibTableColumn
wsNeighborAge = _WsNeighborAge_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 6, 1, 5),
    _WsNeighborAge_Type()
)
wsNeighborAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNeighborAge.setStatus("current")


class _WsManagedAPNeighborEntriesPurge_Type(Integer32):
    """Custom type wsManagedAPNeighborEntriesPurge based on Integer32"""
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


_WsManagedAPNeighborEntriesPurge_Type.__name__ = "Integer32"
_WsManagedAPNeighborEntriesPurge_Object = MibScalar
wsManagedAPNeighborEntriesPurge = _WsManagedAPNeighborEntriesPurge_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 7),
    _WsManagedAPNeighborEntriesPurge_Type()
)
wsManagedAPNeighborEntriesPurge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPNeighborEntriesPurge.setStatus("current")
_WsManagedAPNeighborClientListTable_Object = MibTable
wsManagedAPNeighborClientListTable = _WsManagedAPNeighborClientListTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 8)
)
if mibBuilder.loadTexts:
    wsManagedAPNeighborClientListTable.setStatus("current")
_WsManagedAPNeighborClientListEntry_Object = MibTableRow
wsManagedAPNeighborClientListEntry = _WsManagedAPNeighborClientListEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 8, 1)
)
wsManagedAPNeighborClientListEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsManagedAPMacAddress"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsManagedAPRadioInterface"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsNeighborClientMacAddress"),
)
if mibBuilder.loadTexts:
    wsManagedAPNeighborClientListEntry.setStatus("current")
_WsNeighborClientMacAddress_Type = MacAddress
_WsNeighborClientMacAddress_Object = MibTableColumn
wsNeighborClientMacAddress = _WsNeighborClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 8, 1, 1),
    _WsNeighborClientMacAddress_Type()
)
wsNeighborClientMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNeighborClientMacAddress.setStatus("current")


class _WsNeighborClientRSSI_Type(Integer32):
    """Custom type wsNeighborClientRSSI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_WsNeighborClientRSSI_Type.__name__ = "Integer32"
_WsNeighborClientRSSI_Object = MibTableColumn
wsNeighborClientRSSI = _WsNeighborClientRSSI_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 8, 1, 2),
    _WsNeighborClientRSSI_Type()
)
wsNeighborClientRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNeighborClientRSSI.setStatus("current")


class _WsNeighborClientChannel_Type(Integer32):
    """Custom type wsNeighborClientChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 13),
        ValueRangeConstraint(36, 36),
        ValueRangeConstraint(40, 40),
        ValueRangeConstraint(44, 44),
        ValueRangeConstraint(48, 48),
        ValueRangeConstraint(52, 52),
        ValueRangeConstraint(56, 56),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(64, 64),
    )


_WsNeighborClientChannel_Type.__name__ = "Integer32"
_WsNeighborClientChannel_Object = MibTableColumn
wsNeighborClientChannel = _WsNeighborClientChannel_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 8, 1, 3),
    _WsNeighborClientChannel_Type()
)
wsNeighborClientChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNeighborClientChannel.setStatus("current")
_WsNeighborClientAge_Type = TimeTicks
_WsNeighborClientAge_Object = MibTableColumn
wsNeighborClientAge = _WsNeighborClientAge_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 8, 1, 4),
    _WsNeighborClientAge_Type()
)
wsNeighborClientAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNeighborClientAge.setStatus("current")


class _WsNeighborClientDiscoveryReason_Type(Bits):
    """Custom type wsNeighborClientDiscoveryReason based on Bits"""
    namedValues = NamedValues(
        *(("none", 0),
          ("rfscan-discovered", 1),
          ("neighbor-ap-associated", 2),
          ("current-ap-associated", 3),
          ("probe-request-discovered", 4),
          ("peer-ap-associated", 5),
          ("ad-hoc-rogue", 6))
    )

_WsNeighborClientDiscoveryReason_Type.__name__ = "Bits"
_WsNeighborClientDiscoveryReason_Object = MibTableColumn
wsNeighborClientDiscoveryReason = _WsNeighborClientDiscoveryReason_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 8, 1, 5),
    _WsNeighborClientDiscoveryReason_Type()
)
wsNeighborClientDiscoveryReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNeighborClientDiscoveryReason.setStatus("current")
_WsManagedAPVAPStatusTable_Object = MibTable
wsManagedAPVAPStatusTable = _WsManagedAPVAPStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 9)
)
if mibBuilder.loadTexts:
    wsManagedAPVAPStatusTable.setStatus("current")
_WsManagedAPVAPStatusEntry_Object = MibTableRow
wsManagedAPVAPStatusEntry = _WsManagedAPVAPStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 9, 1)
)
wsManagedAPVAPStatusEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsManagedAPMacAddress"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsManagedAPRadioInterface"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsManagedVAPId"),
)
if mibBuilder.loadTexts:
    wsManagedAPVAPStatusEntry.setStatus("current")


class _WsManagedVAPId_Type(Integer32):
    """Custom type wsManagedVAPId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WsManagedVAPId_Type.__name__ = "Integer32"
_WsManagedVAPId_Object = MibTableColumn
wsManagedVAPId = _WsManagedVAPId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 9, 1, 1),
    _WsManagedVAPId_Type()
)
wsManagedVAPId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedVAPId.setStatus("current")
_WsManagedVAPMacAddress_Type = MacAddress
_WsManagedVAPMacAddress_Object = MibTableColumn
wsManagedVAPMacAddress = _WsManagedVAPMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 9, 1, 2),
    _WsManagedVAPMacAddress_Type()
)
wsManagedVAPMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedVAPMacAddress.setStatus("current")


class _WsManagedVAPSSID_Type(DisplayString):
    """Custom type wsManagedVAPSSID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WsManagedVAPSSID_Type.__name__ = "DisplayString"
_WsManagedVAPSSID_Object = MibTableColumn
wsManagedVAPSSID = _WsManagedVAPSSID_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 9, 1, 3),
    _WsManagedVAPSSID_Type()
)
wsManagedVAPSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedVAPSSID.setStatus("current")
_WsManagedVAPAuthenticatedClients_Type = Unsigned32
_WsManagedVAPAuthenticatedClients_Object = MibTableColumn
wsManagedVAPAuthenticatedClients = _WsManagedVAPAuthenticatedClients_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 9, 1, 4),
    _WsManagedVAPAuthenticatedClients_Type()
)
wsManagedVAPAuthenticatedClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedVAPAuthenticatedClients.setStatus("current")
_WsManagedAPVAPStatisticsTable_Object = MibTable
wsManagedAPVAPStatisticsTable = _WsManagedAPVAPStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 10)
)
if mibBuilder.loadTexts:
    wsManagedAPVAPStatisticsTable.setStatus("current")
_WsManagedAPVAPStatisticsEntry_Object = MibTableRow
wsManagedAPVAPStatisticsEntry = _WsManagedAPVAPStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 10, 1)
)
if mibBuilder.loadTexts:
    wsManagedAPVAPStatisticsEntry.setStatus("current")
_WsManagedVAPAssociationFailures_Type = Counter32
_WsManagedVAPAssociationFailures_Object = MibTableColumn
wsManagedVAPAssociationFailures = _WsManagedVAPAssociationFailures_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 10, 1, 1),
    _WsManagedVAPAssociationFailures_Type()
)
wsManagedVAPAssociationFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedVAPAssociationFailures.setStatus("current")
_WsManagedVAPAuthenticationFailures_Type = Counter32
_WsManagedVAPAuthenticationFailures_Object = MibTableColumn
wsManagedVAPAuthenticationFailures = _WsManagedVAPAuthenticationFailures_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 10, 1, 2),
    _WsManagedVAPAuthenticationFailures_Type()
)
wsManagedVAPAuthenticationFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedVAPAuthenticationFailures.setStatus("current")
_WsManagedVAPWLANPktsRecvd_Type = Counter64
_WsManagedVAPWLANPktsRecvd_Object = MibTableColumn
wsManagedVAPWLANPktsRecvd = _WsManagedVAPWLANPktsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 10, 1, 3),
    _WsManagedVAPWLANPktsRecvd_Type()
)
wsManagedVAPWLANPktsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedVAPWLANPktsRecvd.setStatus("current")
_WsManagedVAPWLANBytesRecvd_Type = Counter64
_WsManagedVAPWLANBytesRecvd_Object = MibTableColumn
wsManagedVAPWLANBytesRecvd = _WsManagedVAPWLANBytesRecvd_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 10, 1, 4),
    _WsManagedVAPWLANBytesRecvd_Type()
)
wsManagedVAPWLANBytesRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedVAPWLANBytesRecvd.setStatus("current")
_WsManagedVAPWLANPktsTransmitted_Type = Counter64
_WsManagedVAPWLANPktsTransmitted_Object = MibTableColumn
wsManagedVAPWLANPktsTransmitted = _WsManagedVAPWLANPktsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 10, 1, 5),
    _WsManagedVAPWLANPktsTransmitted_Type()
)
wsManagedVAPWLANPktsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedVAPWLANPktsTransmitted.setStatus("current")
_WsManagedVAPWLANBytesTransmitted_Type = Counter64
_WsManagedVAPWLANBytesTransmitted_Object = MibTableColumn
wsManagedVAPWLANBytesTransmitted = _WsManagedVAPWLANBytesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 10, 1, 6),
    _WsManagedVAPWLANBytesTransmitted_Type()
)
wsManagedVAPWLANBytesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedVAPWLANBytesTransmitted.setStatus("current")
_WsManagedVAPWLANPktsRecvDropped_Type = Counter64
_WsManagedVAPWLANPktsRecvDropped_Object = MibTableColumn
wsManagedVAPWLANPktsRecvDropped = _WsManagedVAPWLANPktsRecvDropped_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 10, 1, 7),
    _WsManagedVAPWLANPktsRecvDropped_Type()
)
wsManagedVAPWLANPktsRecvDropped.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsManagedVAPWLANPktsRecvDropped.setStatus("current")
_WsManagedVAPWLANBytesRecvDropped_Type = Counter64
_WsManagedVAPWLANBytesRecvDropped_Object = MibTableColumn
wsManagedVAPWLANBytesRecvDropped = _WsManagedVAPWLANBytesRecvDropped_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 10, 1, 8),
    _WsManagedVAPWLANBytesRecvDropped_Type()
)
wsManagedVAPWLANBytesRecvDropped.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsManagedVAPWLANBytesRecvDropped.setStatus("current")
_WsManagedVAPWLANPktsTransmitDropped_Type = Counter64
_WsManagedVAPWLANPktsTransmitDropped_Object = MibTableColumn
wsManagedVAPWLANPktsTransmitDropped = _WsManagedVAPWLANPktsTransmitDropped_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 10, 1, 9),
    _WsManagedVAPWLANPktsTransmitDropped_Type()
)
wsManagedVAPWLANPktsTransmitDropped.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsManagedVAPWLANPktsTransmitDropped.setStatus("current")
_WsManagedVAPWLANBytesTransmitDropped_Type = Counter64
_WsManagedVAPWLANBytesTransmitDropped_Object = MibTableColumn
wsManagedVAPWLANBytesTransmitDropped = _WsManagedVAPWLANBytesTransmitDropped_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 10, 1, 10),
    _WsManagedVAPWLANBytesTransmitDropped_Type()
)
wsManagedVAPWLANBytesTransmitDropped.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsManagedVAPWLANBytesTransmitDropped.setStatus("current")


class _WsManagedAPResetAll_Type(Integer32):
    """Custom type wsManagedAPResetAll based on Integer32"""
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


_WsManagedAPResetAll_Type.__name__ = "Integer32"
_WsManagedAPResetAll_Object = MibScalar
wsManagedAPResetAll = _WsManagedAPResetAll_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 11),
    _WsManagedAPResetAll_Type()
)
wsManagedAPResetAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPResetAll.setStatus("current")
_WsManagedAPRadioEligibleChannelListTable_Object = MibTable
wsManagedAPRadioEligibleChannelListTable = _WsManagedAPRadioEligibleChannelListTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 12)
)
if mibBuilder.loadTexts:
    wsManagedAPRadioEligibleChannelListTable.setStatus("current")
_WsManagedAPRadioEligibleChannelListEntry_Object = MibTableRow
wsManagedAPRadioEligibleChannelListEntry = _WsManagedAPRadioEligibleChannelListEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 12, 1)
)
wsManagedAPRadioEligibleChannelListEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsManagedAPMacAddress"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsManagedAPRadioInterface"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsManagedAPRadioEligibleChannel"),
)
if mibBuilder.loadTexts:
    wsManagedAPRadioEligibleChannelListEntry.setStatus("current")


class _WsManagedAPRadioEligibleChannel_Type(Integer32):
    """Custom type wsManagedAPRadioEligibleChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_WsManagedAPRadioEligibleChannel_Type.__name__ = "Integer32"
_WsManagedAPRadioEligibleChannel_Object = MibTableColumn
wsManagedAPRadioEligibleChannel = _WsManagedAPRadioEligibleChannel_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 12, 1, 1),
    _WsManagedAPRadioEligibleChannel_Type()
)
wsManagedAPRadioEligibleChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPRadioEligibleChannel.setStatus("current")


class _WsManagedAPRadioEligibleChannelRdrDetRequired_Type(Integer32):
    """Custom type wsManagedAPRadioEligibleChannelRdrDetRequired based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_WsManagedAPRadioEligibleChannelRdrDetRequired_Type.__name__ = "Integer32"
_WsManagedAPRadioEligibleChannelRdrDetRequired_Object = MibTableColumn
wsManagedAPRadioEligibleChannelRdrDetRequired = _WsManagedAPRadioEligibleChannelRdrDetRequired_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 12, 1, 2),
    _WsManagedAPRadioEligibleChannelRdrDetRequired_Type()
)
wsManagedAPRadioEligibleChannelRdrDetRequired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPRadioEligibleChannelRdrDetRequired.setStatus("current")


class _WsManagedAPRadioEligibleChannelRdrDetected_Type(Integer32):
    """Custom type wsManagedAPRadioEligibleChannelRdrDetected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_WsManagedAPRadioEligibleChannelRdrDetected_Type.__name__ = "Integer32"
_WsManagedAPRadioEligibleChannelRdrDetected_Object = MibTableColumn
wsManagedAPRadioEligibleChannelRdrDetected = _WsManagedAPRadioEligibleChannelRdrDetected_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 12, 1, 3),
    _WsManagedAPRadioEligibleChannelRdrDetected_Type()
)
wsManagedAPRadioEligibleChannelRdrDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPRadioEligibleChannelRdrDetected.setStatus("current")
_WsManagedAPRadioEligibleChannelLastRdrDetTime_Type = DisplayString
_WsManagedAPRadioEligibleChannelLastRdrDetTime_Object = MibTableColumn
wsManagedAPRadioEligibleChannelLastRdrDetTime = _WsManagedAPRadioEligibleChannelLastRdrDetTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 6, 12, 1, 4),
    _WsManagedAPRadioEligibleChannelLastRdrDetTime_Type()
)
wsManagedAPRadioEligibleChannelLastRdrDetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsManagedAPRadioEligibleChannelLastRdrDetTime.setStatus("current")
_AssociatedClient_ObjectIdentity = ObjectIdentity
associatedClient = _AssociatedClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7)
)
_WsAssociatedClientStatusTable_Object = MibTable
wsAssociatedClientStatusTable = _WsAssociatedClientStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 1)
)
if mibBuilder.loadTexts:
    wsAssociatedClientStatusTable.setStatus("obsolete")
_WsAssociatedClientStatusEntry_Object = MibTableRow
wsAssociatedClientStatusEntry = _WsAssociatedClientStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 1, 1)
)
wsAssociatedClientStatusEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsAssociatedClientMacAddress"),
)
if mibBuilder.loadTexts:
    wsAssociatedClientStatusEntry.setStatus("obsolete")
_WsAssociatedClientMacAddress_Type = MacAddress
_WsAssociatedClientMacAddress_Object = MibTableColumn
wsAssociatedClientMacAddress = _WsAssociatedClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 1, 1, 1),
    _WsAssociatedClientMacAddress_Type()
)
wsAssociatedClientMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAssociatedClientMacAddress.setStatus("obsolete")
_WsAssociatedClientTunnelIpAddress_Type = IpAddress
_WsAssociatedClientTunnelIpAddress_Object = MibTableColumn
wsAssociatedClientTunnelIpAddress = _WsAssociatedClientTunnelIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 1, 1, 2),
    _WsAssociatedClientTunnelIpAddress_Type()
)
wsAssociatedClientTunnelIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAssociatedClientTunnelIpAddress.setStatus("obsolete")


class _WsAssociatedClientUserName_Type(DisplayString):
    """Custom type wsAssociatedClientUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WsAssociatedClientUserName_Type.__name__ = "DisplayString"
_WsAssociatedClientUserName_Object = MibTableColumn
wsAssociatedClientUserName = _WsAssociatedClientUserName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 1, 1, 3),
    _WsAssociatedClientUserName_Type()
)
wsAssociatedClientUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAssociatedClientUserName.setStatus("obsolete")


class _WsAssociatedClientSSID_Type(DisplayString):
    """Custom type wsAssociatedClientSSID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WsAssociatedClientSSID_Type.__name__ = "DisplayString"
_WsAssociatedClientSSID_Object = MibTableColumn
wsAssociatedClientSSID = _WsAssociatedClientSSID_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 1, 1, 4),
    _WsAssociatedClientSSID_Type()
)
wsAssociatedClientSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAssociatedClientSSID.setStatus("obsolete")


class _WsAssociatedClientVLAN_Type(Integer32):
    """Custom type wsAssociatedClientVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WsAssociatedClientVLAN_Type.__name__ = "Integer32"
_WsAssociatedClientVLAN_Object = MibTableColumn
wsAssociatedClientVLAN = _WsAssociatedClientVLAN_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 1, 1, 5),
    _WsAssociatedClientVLAN_Type()
)
wsAssociatedClientVLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAssociatedClientVLAN.setStatus("obsolete")


class _WsAssociatedClientStatus_Type(Integer32):
    """Custom type wsAssociatedClientStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("authenticated", 1),
          ("associated", 2),
          ("disassociated", 3))
    )


_WsAssociatedClientStatus_Type.__name__ = "Integer32"
_WsAssociatedClientStatus_Object = MibTableColumn
wsAssociatedClientStatus = _WsAssociatedClientStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 1, 1, 6),
    _WsAssociatedClientStatus_Type()
)
wsAssociatedClientStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAssociatedClientStatus.setStatus("obsolete")


class _WsAssociatedClientTxDataRate_Type(Integer32):
    """Custom type wsAssociatedClientTxDataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 1200),
    )


_WsAssociatedClientTxDataRate_Type.__name__ = "Integer32"
_WsAssociatedClientTxDataRate_Object = MibTableColumn
wsAssociatedClientTxDataRate = _WsAssociatedClientTxDataRate_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 1, 1, 7),
    _WsAssociatedClientTxDataRate_Type()
)
wsAssociatedClientTxDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAssociatedClientTxDataRate.setStatus("obsolete")
_WsAssociatedClientInactivePeriod_Type = TimeTicks
_WsAssociatedClientInactivePeriod_Object = MibTableColumn
wsAssociatedClientInactivePeriod = _WsAssociatedClientInactivePeriod_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 1, 1, 8),
    _WsAssociatedClientInactivePeriod_Type()
)
wsAssociatedClientInactivePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAssociatedClientInactivePeriod.setStatus("obsolete")


class _WsAssociatedClientDisassociateAction_Type(Integer32):
    """Custom type wsAssociatedClientDisassociateAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("start", 2))
    )


_WsAssociatedClientDisassociateAction_Type.__name__ = "Integer32"
_WsAssociatedClientDisassociateAction_Object = MibTableColumn
wsAssociatedClientDisassociateAction = _WsAssociatedClientDisassociateAction_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 1, 1, 9),
    _WsAssociatedClientDisassociateAction_Type()
)
wsAssociatedClientDisassociateAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAssociatedClientDisassociateAction.setStatus("obsolete")
_WsAssociatedClientAge_Type = TimeTicks
_WsAssociatedClientAge_Object = MibTableColumn
wsAssociatedClientAge = _WsAssociatedClientAge_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 1, 1, 10),
    _WsAssociatedClientAge_Type()
)
wsAssociatedClientAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAssociatedClientAge.setStatus("obsolete")


class _WsAssociatedClientAssociatingSwitch_Type(Integer32):
    """Custom type wsAssociatedClientAssociatingSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local-switch", 1),
          ("peer-switch", 2))
    )


_WsAssociatedClientAssociatingSwitch_Type.__name__ = "Integer32"
_WsAssociatedClientAssociatingSwitch_Object = MibTableColumn
wsAssociatedClientAssociatingSwitch = _WsAssociatedClientAssociatingSwitch_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 1, 1, 11),
    _WsAssociatedClientAssociatingSwitch_Type()
)
wsAssociatedClientAssociatingSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAssociatedClientAssociatingSwitch.setStatus("obsolete")
_WsAssociatedClientSwitchMacAddress_Type = MacAddress
_WsAssociatedClientSwitchMacAddress_Object = MibTableColumn
wsAssociatedClientSwitchMacAddress = _WsAssociatedClientSwitchMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 1, 1, 12),
    _WsAssociatedClientSwitchMacAddress_Type()
)
wsAssociatedClientSwitchMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAssociatedClientSwitchMacAddress.setStatus("obsolete")
_WsAssociatedClientSwitchIpAddress_Type = IpAddress
_WsAssociatedClientSwitchIpAddress_Object = MibTableColumn
wsAssociatedClientSwitchIpAddress = _WsAssociatedClientSwitchIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 1, 1, 13),
    _WsAssociatedClientSwitchIpAddress_Type()
)
wsAssociatedClientSwitchIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAssociatedClientSwitchIpAddress.setStatus("obsolete")


class _WsAssociatedClientDot11nCapable_Type(Integer32):
    """Custom type wsAssociatedClientDot11nCapable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_WsAssociatedClientDot11nCapable_Type.__name__ = "Integer32"
_WsAssociatedClientDot11nCapable_Object = MibTableColumn
wsAssociatedClientDot11nCapable = _WsAssociatedClientDot11nCapable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 1, 1, 14),
    _WsAssociatedClientDot11nCapable_Type()
)
wsAssociatedClientDot11nCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAssociatedClientDot11nCapable.setStatus("obsolete")


class _WsAssociatedClientStbcCapable_Type(Integer32):
    """Custom type wsAssociatedClientStbcCapable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_WsAssociatedClientStbcCapable_Type.__name__ = "Integer32"
_WsAssociatedClientStbcCapable_Object = MibTableColumn
wsAssociatedClientStbcCapable = _WsAssociatedClientStbcCapable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 1, 1, 15),
    _WsAssociatedClientStbcCapable_Type()
)
wsAssociatedClientStbcCapable.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAssociatedClientStbcCapable.setStatus("obsolete")


class _WsAssociatedClientDistTunnelStatus_Type(Integer32):
    """Custom type wsAssociatedClientDistTunnelStatus based on Integer32"""
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


_WsAssociatedClientDistTunnelStatus_Type.__name__ = "Integer32"
_WsAssociatedClientDistTunnelStatus_Object = MibTableColumn
wsAssociatedClientDistTunnelStatus = _WsAssociatedClientDistTunnelStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 1, 1, 16),
    _WsAssociatedClientDistTunnelStatus_Type()
)
wsAssociatedClientDistTunnelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAssociatedClientDistTunnelStatus.setStatus("obsolete")


class _WsAssociatedClientDistTunnelRoamStatus_Type(Integer32):
    """Custom type wsAssociatedClientDistTunnelRoamStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("associated", 0),
          ("home", 1))
    )


_WsAssociatedClientDistTunnelRoamStatus_Type.__name__ = "Integer32"
_WsAssociatedClientDistTunnelRoamStatus_Object = MibTableColumn
wsAssociatedClientDistTunnelRoamStatus = _WsAssociatedClientDistTunnelRoamStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 1, 1, 17),
    _WsAssociatedClientDistTunnelRoamStatus_Type()
)
wsAssociatedClientDistTunnelRoamStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAssociatedClientDistTunnelRoamStatus.setStatus("obsolete")
_WsAssociatedClientDistTunnelHomeAPMac_Type = MacAddress
_WsAssociatedClientDistTunnelHomeAPMac_Object = MibTableColumn
wsAssociatedClientDistTunnelHomeAPMac = _WsAssociatedClientDistTunnelHomeAPMac_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 1, 1, 18),
    _WsAssociatedClientDistTunnelHomeAPMac_Type()
)
wsAssociatedClientDistTunnelHomeAPMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAssociatedClientDistTunnelHomeAPMac.setStatus("obsolete")
_WsAssociatedClientDistTunnelAssocAPMac_Type = MacAddress
_WsAssociatedClientDistTunnelAssocAPMac_Object = MibTableColumn
wsAssociatedClientDistTunnelAssocAPMac = _WsAssociatedClientDistTunnelAssocAPMac_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 1, 1, 19),
    _WsAssociatedClientDistTunnelAssocAPMac_Type()
)
wsAssociatedClientDistTunnelAssocAPMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAssociatedClientDistTunnelAssocAPMac.setStatus("obsolete")
_WsAssociatedClientAPMacAddress_Type = MacAddress
_WsAssociatedClientAPMacAddress_Object = MibTableColumn
wsAssociatedClientAPMacAddress = _WsAssociatedClientAPMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 1, 1, 20),
    _WsAssociatedClientAPMacAddress_Type()
)
wsAssociatedClientAPMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAssociatedClientAPMacAddress.setStatus("obsolete")
_WsAssociatedClientBSSID_Type = MacAddress
_WsAssociatedClientBSSID_Object = MibTableColumn
wsAssociatedClientBSSID = _WsAssociatedClientBSSID_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 1, 1, 21),
    _WsAssociatedClientBSSID_Type()
)
wsAssociatedClientBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAssociatedClientBSSID.setStatus("obsolete")


class _WsAssociatedClientRadioInterface_Type(Integer32):
    """Custom type wsAssociatedClientRadioInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WsAssociatedClientRadioInterface_Type.__name__ = "Integer32"
_WsAssociatedClientRadioInterface_Object = MibTableColumn
wsAssociatedClientRadioInterface = _WsAssociatedClientRadioInterface_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 1, 1, 22),
    _WsAssociatedClientRadioInterface_Type()
)
wsAssociatedClientRadioInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAssociatedClientRadioInterface.setStatus("obsolete")


class _WsAssociatedClientChannel_Type(Integer32):
    """Custom type wsAssociatedClientChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 165),
    )


_WsAssociatedClientChannel_Type.__name__ = "Integer32"
_WsAssociatedClientChannel_Object = MibTableColumn
wsAssociatedClientChannel = _WsAssociatedClientChannel_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 1, 1, 23),
    _WsAssociatedClientChannel_Type()
)
wsAssociatedClientChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAssociatedClientChannel.setStatus("obsolete")
_WsAssociatedClientNwTime_Type = TimeTicks
_WsAssociatedClientNwTime_Object = MibTableColumn
wsAssociatedClientNwTime = _WsAssociatedClientNwTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 1, 1, 24),
    _WsAssociatedClientNwTime_Type()
)
wsAssociatedClientNwTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAssociatedClientNwTime.setStatus("obsolete")
_WsAssociatedClientIpAddress_Type = IpAddress
_WsAssociatedClientIpAddress_Object = MibTableColumn
wsAssociatedClientIpAddress = _WsAssociatedClientIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 1, 1, 25),
    _WsAssociatedClientIpAddress_Type()
)
wsAssociatedClientIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAssociatedClientIpAddress.setStatus("obsolete")


class _WsAssociatedClientNetBiosName_Type(DisplayString):
    """Custom type wsAssociatedClientNetBiosName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_WsAssociatedClientNetBiosName_Type.__name__ = "DisplayString"
_WsAssociatedClientNetBiosName_Object = MibTableColumn
wsAssociatedClientNetBiosName = _WsAssociatedClientNetBiosName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 1, 1, 26),
    _WsAssociatedClientNetBiosName_Type()
)
wsAssociatedClientNetBiosName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAssociatedClientNetBiosName.setStatus("obsolete")


class _WsAssociatedClientRRMSupported_Type(Integer32):
    """Custom type wsAssociatedClientRRMSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("supported", 2),
          ("unsupported", 3))
    )


_WsAssociatedClientRRMSupported_Type.__name__ = "Integer32"
_WsAssociatedClientRRMSupported_Object = MibTableColumn
wsAssociatedClientRRMSupported = _WsAssociatedClientRRMSupported_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 1, 1, 27),
    _WsAssociatedClientRRMSupported_Type()
)
wsAssociatedClientRRMSupported.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAssociatedClientRRMSupported.setStatus("obsolete")


class _WsAssociatedClientRRMLocationReportSupported_Type(Integer32):
    """Custom type wsAssociatedClientRRMLocationReportSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("supported", 1),
          ("unsupported", 2))
    )


_WsAssociatedClientRRMLocationReportSupported_Type.__name__ = "Integer32"
_WsAssociatedClientRRMLocationReportSupported_Object = MibTableColumn
wsAssociatedClientRRMLocationReportSupported = _WsAssociatedClientRRMLocationReportSupported_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 1, 1, 28),
    _WsAssociatedClientRRMLocationReportSupported_Type()
)
wsAssociatedClientRRMLocationReportSupported.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAssociatedClientRRMLocationReportSupported.setStatus("obsolete")


class _WsAssociatedClientRRMBeaconTableMeasurementSupported_Type(Integer32):
    """Custom type wsAssociatedClientRRMBeaconTableMeasurementSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("supported", 1),
          ("unsupported", 2))
    )


_WsAssociatedClientRRMBeaconTableMeasurementSupported_Type.__name__ = "Integer32"
_WsAssociatedClientRRMBeaconTableMeasurementSupported_Object = MibTableColumn
wsAssociatedClientRRMBeaconTableMeasurementSupported = _WsAssociatedClientRRMBeaconTableMeasurementSupported_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 1, 1, 29),
    _WsAssociatedClientRRMBeaconTableMeasurementSupported_Type()
)
wsAssociatedClientRRMBeaconTableMeasurementSupported.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAssociatedClientRRMBeaconTableMeasurementSupported.setStatus("obsolete")


class _WsAssociatedClientRRMBeaconActiveMeasurementSupported_Type(Integer32):
    """Custom type wsAssociatedClientRRMBeaconActiveMeasurementSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("supported", 1),
          ("unsupported", 2))
    )


_WsAssociatedClientRRMBeaconActiveMeasurementSupported_Type.__name__ = "Integer32"
_WsAssociatedClientRRMBeaconActiveMeasurementSupported_Object = MibTableColumn
wsAssociatedClientRRMBeaconActiveMeasurementSupported = _WsAssociatedClientRRMBeaconActiveMeasurementSupported_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 1, 1, 30),
    _WsAssociatedClientRRMBeaconActiveMeasurementSupported_Type()
)
wsAssociatedClientRRMBeaconActiveMeasurementSupported.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAssociatedClientRRMBeaconActiveMeasurementSupported.setStatus("obsolete")


class _WsAssociatedClientRRMBeaconPassiveMeasurementSupported_Type(Integer32):
    """Custom type wsAssociatedClientRRMBeaconPassiveMeasurementSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("supported", 1),
          ("unsupported", 2))
    )


_WsAssociatedClientRRMBeaconPassiveMeasurementSupported_Type.__name__ = "Integer32"
_WsAssociatedClientRRMBeaconPassiveMeasurementSupported_Object = MibTableColumn
wsAssociatedClientRRMBeaconPassiveMeasurementSupported = _WsAssociatedClientRRMBeaconPassiveMeasurementSupported_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 1, 1, 31),
    _WsAssociatedClientRRMBeaconPassiveMeasurementSupported_Type()
)
wsAssociatedClientRRMBeaconPassiveMeasurementSupported.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAssociatedClientRRMBeaconPassiveMeasurementSupported.setStatus("obsolete")


class _WsAssociatedClientRRMChannelLoadMeasurementSupported_Type(Integer32):
    """Custom type wsAssociatedClientRRMChannelLoadMeasurementSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("supported", 1),
          ("unsupported", 2))
    )


_WsAssociatedClientRRMChannelLoadMeasurementSupported_Type.__name__ = "Integer32"
_WsAssociatedClientRRMChannelLoadMeasurementSupported_Object = MibTableColumn
wsAssociatedClientRRMChannelLoadMeasurementSupported = _WsAssociatedClientRRMChannelLoadMeasurementSupported_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 1, 1, 32),
    _WsAssociatedClientRRMChannelLoadMeasurementSupported_Type()
)
wsAssociatedClientRRMChannelLoadMeasurementSupported.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAssociatedClientRRMChannelLoadMeasurementSupported.setStatus("obsolete")
_WsAssociatedClientStatisticsTable_Object = MibTable
wsAssociatedClientStatisticsTable = _WsAssociatedClientStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 2)
)
if mibBuilder.loadTexts:
    wsAssociatedClientStatisticsTable.setStatus("obsolete")
_WsAssociatedClientStatisticsEntry_Object = MibTableRow
wsAssociatedClientStatisticsEntry = _WsAssociatedClientStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 2, 1)
)
if mibBuilder.loadTexts:
    wsAssociatedClientStatisticsEntry.setStatus("obsolete")
_WsAssociatedClientPktsRecvd_Type = Counter64
_WsAssociatedClientPktsRecvd_Object = MibTableColumn
wsAssociatedClientPktsRecvd = _WsAssociatedClientPktsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 2, 1, 1),
    _WsAssociatedClientPktsRecvd_Type()
)
wsAssociatedClientPktsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAssociatedClientPktsRecvd.setStatus("obsolete")
_WsAssociatedClientBytesRecvd_Type = Counter64
_WsAssociatedClientBytesRecvd_Object = MibTableColumn
wsAssociatedClientBytesRecvd = _WsAssociatedClientBytesRecvd_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 2, 1, 2),
    _WsAssociatedClientBytesRecvd_Type()
)
wsAssociatedClientBytesRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAssociatedClientBytesRecvd.setStatus("obsolete")
_WsAssociatedClientPktsTransmitted_Type = Counter64
_WsAssociatedClientPktsTransmitted_Object = MibTableColumn
wsAssociatedClientPktsTransmitted = _WsAssociatedClientPktsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 2, 1, 3),
    _WsAssociatedClientPktsTransmitted_Type()
)
wsAssociatedClientPktsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAssociatedClientPktsTransmitted.setStatus("obsolete")
_WsAssociatedClientBytesTransmitted_Type = Counter64
_WsAssociatedClientBytesTransmitted_Object = MibTableColumn
wsAssociatedClientBytesTransmitted = _WsAssociatedClientBytesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 2, 1, 4),
    _WsAssociatedClientBytesTransmitted_Type()
)
wsAssociatedClientBytesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAssociatedClientBytesTransmitted.setStatus("obsolete")
_WsAssociatedClientDuplicatePktsRecvd_Type = Counter32
_WsAssociatedClientDuplicatePktsRecvd_Object = MibTableColumn
wsAssociatedClientDuplicatePktsRecvd = _WsAssociatedClientDuplicatePktsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 2, 1, 5),
    _WsAssociatedClientDuplicatePktsRecvd_Type()
)
wsAssociatedClientDuplicatePktsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAssociatedClientDuplicatePktsRecvd.setStatus("obsolete")
_WsAssociatedClientFragmentedPktsRecvd_Type = Counter32
_WsAssociatedClientFragmentedPktsRecvd_Object = MibTableColumn
wsAssociatedClientFragmentedPktsRecvd = _WsAssociatedClientFragmentedPktsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 2, 1, 6),
    _WsAssociatedClientFragmentedPktsRecvd_Type()
)
wsAssociatedClientFragmentedPktsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAssociatedClientFragmentedPktsRecvd.setStatus("obsolete")
_WsAssociatedClientFragmentedPktsTransmitted_Type = Counter32
_WsAssociatedClientFragmentedPktsTransmitted_Object = MibTableColumn
wsAssociatedClientFragmentedPktsTransmitted = _WsAssociatedClientFragmentedPktsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 2, 1, 7),
    _WsAssociatedClientFragmentedPktsTransmitted_Type()
)
wsAssociatedClientFragmentedPktsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAssociatedClientFragmentedPktsTransmitted.setStatus("obsolete")
_WsAssociatedClientTransmitRetryCount_Type = Counter32
_WsAssociatedClientTransmitRetryCount_Object = MibTableColumn
wsAssociatedClientTransmitRetryCount = _WsAssociatedClientTransmitRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 2, 1, 8),
    _WsAssociatedClientTransmitRetryCount_Type()
)
wsAssociatedClientTransmitRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAssociatedClientTransmitRetryCount.setStatus("obsolete")
_WsAssociatedClientTransmitRetryFailedCount_Type = Counter32
_WsAssociatedClientTransmitRetryFailedCount_Object = MibTableColumn
wsAssociatedClientTransmitRetryFailedCount = _WsAssociatedClientTransmitRetryFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 2, 1, 9),
    _WsAssociatedClientTransmitRetryFailedCount_Type()
)
wsAssociatedClientTransmitRetryFailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAssociatedClientTransmitRetryFailedCount.setStatus("obsolete")
_WsAssociatedClientPktsRecvDropped_Type = Counter64
_WsAssociatedClientPktsRecvDropped_Object = MibTableColumn
wsAssociatedClientPktsRecvDropped = _WsAssociatedClientPktsRecvDropped_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 2, 1, 10),
    _WsAssociatedClientPktsRecvDropped_Type()
)
wsAssociatedClientPktsRecvDropped.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAssociatedClientPktsRecvDropped.setStatus("obsolete")
_WsAssociatedClientBytesRecvDropped_Type = Counter64
_WsAssociatedClientBytesRecvDropped_Object = MibTableColumn
wsAssociatedClientBytesRecvDropped = _WsAssociatedClientBytesRecvDropped_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 2, 1, 11),
    _WsAssociatedClientBytesRecvDropped_Type()
)
wsAssociatedClientBytesRecvDropped.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAssociatedClientBytesRecvDropped.setStatus("obsolete")
_WsAssociatedClientPktsTransmitDropped_Type = Counter64
_WsAssociatedClientPktsTransmitDropped_Object = MibTableColumn
wsAssociatedClientPktsTransmitDropped = _WsAssociatedClientPktsTransmitDropped_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 2, 1, 12),
    _WsAssociatedClientPktsTransmitDropped_Type()
)
wsAssociatedClientPktsTransmitDropped.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAssociatedClientPktsTransmitDropped.setStatus("obsolete")
_WsAssociatedClientBytesTransmitDropped_Type = Counter64
_WsAssociatedClientBytesTransmitDropped_Object = MibTableColumn
wsAssociatedClientBytesTransmitDropped = _WsAssociatedClientBytesTransmitDropped_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 2, 1, 13),
    _WsAssociatedClientBytesTransmitDropped_Type()
)
wsAssociatedClientBytesTransmitDropped.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAssociatedClientBytesTransmitDropped.setStatus("obsolete")
_WsAssociatedClientTsViolatePktsRecvd_Type = Counter32
_WsAssociatedClientTsViolatePktsRecvd_Object = MibTableColumn
wsAssociatedClientTsViolatePktsRecvd = _WsAssociatedClientTsViolatePktsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 2, 1, 14),
    _WsAssociatedClientTsViolatePktsRecvd_Type()
)
wsAssociatedClientTsViolatePktsRecvd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAssociatedClientTsViolatePktsRecvd.setStatus("obsolete")
_WsAssociatedClientTsViolatePktsTransmitted_Type = Counter32
_WsAssociatedClientTsViolatePktsTransmitted_Object = MibTableColumn
wsAssociatedClientTsViolatePktsTransmitted = _WsAssociatedClientTsViolatePktsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 2, 1, 15),
    _WsAssociatedClientTsViolatePktsTransmitted_Type()
)
wsAssociatedClientTsViolatePktsTransmitted.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAssociatedClientTsViolatePktsTransmitted.setStatus("obsolete")
_WsAssociatedClientNeighborManagedAPStatusTable_Object = MibTable
wsAssociatedClientNeighborManagedAPStatusTable = _WsAssociatedClientNeighborManagedAPStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 3)
)
if mibBuilder.loadTexts:
    wsAssociatedClientNeighborManagedAPStatusTable.setStatus("obsolete")
_WsAssociatedClientNeighborManagedAPStatusEntry_Object = MibTableRow
wsAssociatedClientNeighborManagedAPStatusEntry = _WsAssociatedClientNeighborManagedAPStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 3, 1)
)
wsAssociatedClientNeighborManagedAPStatusEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsClientStationMacAddress"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsClientNeighborWSManagedAPMacAddress"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsClientNeighborWSManagedAPRadioInterface"),
)
if mibBuilder.loadTexts:
    wsAssociatedClientNeighborManagedAPStatusEntry.setStatus("obsolete")
_WsClientStationMacAddress_Type = MacAddress
_WsClientStationMacAddress_Object = MibTableColumn
wsClientStationMacAddress = _WsClientStationMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 3, 1, 1),
    _WsClientStationMacAddress_Type()
)
wsClientStationMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsClientStationMacAddress.setStatus("obsolete")
_WsClientNeighborWSManagedAPMacAddress_Type = MacAddress
_WsClientNeighborWSManagedAPMacAddress_Object = MibTableColumn
wsClientNeighborWSManagedAPMacAddress = _WsClientNeighborWSManagedAPMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 3, 1, 2),
    _WsClientNeighborWSManagedAPMacAddress_Type()
)
wsClientNeighborWSManagedAPMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsClientNeighborWSManagedAPMacAddress.setStatus("obsolete")


class _WsClientNeighborWSManagedAPRadioInterface_Type(Integer32):
    """Custom type wsClientNeighborWSManagedAPRadioInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WsClientNeighborWSManagedAPRadioInterface_Type.__name__ = "Integer32"
_WsClientNeighborWSManagedAPRadioInterface_Object = MibTableColumn
wsClientNeighborWSManagedAPRadioInterface = _WsClientNeighborWSManagedAPRadioInterface_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 3, 1, 3),
    _WsClientNeighborWSManagedAPRadioInterface_Type()
)
wsClientNeighborWSManagedAPRadioInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsClientNeighborWSManagedAPRadioInterface.setStatus("obsolete")


class _WsClientStationDiscoveryReason_Type(Bits):
    """Custom type wsClientStationDiscoveryReason based on Bits"""
    namedValues = NamedValues(
        *(("none", 0),
          ("rfscan-discovered", 1),
          ("neighbor-ap-associated", 2),
          ("current-ap-associated", 3),
          ("probe-request-discovered", 4),
          ("ad-hoc-rogue", 5),
          ("associated-to-peer-ap", 6))
    )

_WsClientStationDiscoveryReason_Type.__name__ = "Bits"
_WsClientStationDiscoveryReason_Object = MibTableColumn
wsClientStationDiscoveryReason = _WsClientStationDiscoveryReason_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 3, 1, 4),
    _WsClientStationDiscoveryReason_Type()
)
wsClientStationDiscoveryReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsClientStationDiscoveryReason.setStatus("obsolete")
_WsVAPAssociatedClientStatusTable_Object = MibTable
wsVAPAssociatedClientStatusTable = _WsVAPAssociatedClientStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 4)
)
if mibBuilder.loadTexts:
    wsVAPAssociatedClientStatusTable.setStatus("obsolete")
_WsVAPAssociatedClientStatusEntry_Object = MibTableRow
wsVAPAssociatedClientStatusEntry = _WsVAPAssociatedClientStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 4, 1)
)
wsVAPAssociatedClientStatusEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsVAPMacAddress"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsVAPAssociatedClientMacAddress"),
)
if mibBuilder.loadTexts:
    wsVAPAssociatedClientStatusEntry.setStatus("obsolete")
_WsVAPMacAddress_Type = MacAddress
_WsVAPMacAddress_Object = MibTableColumn
wsVAPMacAddress = _WsVAPMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 4, 1, 1),
    _WsVAPMacAddress_Type()
)
wsVAPMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsVAPMacAddress.setStatus("obsolete")
_WsVAPAssociatedClientMacAddress_Type = MacAddress
_WsVAPAssociatedClientMacAddress_Object = MibTableColumn
wsVAPAssociatedClientMacAddress = _WsVAPAssociatedClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 4, 1, 2),
    _WsVAPAssociatedClientMacAddress_Type()
)
wsVAPAssociatedClientMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsVAPAssociatedClientMacAddress.setStatus("obsolete")
_WsSSIDAssociatedClientStatusTable_Object = MibTable
wsSSIDAssociatedClientStatusTable = _WsSSIDAssociatedClientStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 5)
)
if mibBuilder.loadTexts:
    wsSSIDAssociatedClientStatusTable.setStatus("obsolete")
_WsSSIDAssociatedClientStatusEntry_Object = MibTableRow
wsSSIDAssociatedClientStatusEntry = _WsSSIDAssociatedClientStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 5, 1)
)
wsSSIDAssociatedClientStatusEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsSSIDAssociatedClientMacAddress"),
)
if mibBuilder.loadTexts:
    wsSSIDAssociatedClientStatusEntry.setStatus("obsolete")


class _WsSSID_Type(DisplayString):
    """Custom type wsSSID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WsSSID_Type.__name__ = "DisplayString"
_WsSSID_Object = MibTableColumn
wsSSID = _WsSSID_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 5, 1, 1),
    _WsSSID_Type()
)
wsSSID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsSSID.setStatus("obsolete")
_WsSSIDAssociatedClientMacAddress_Type = MacAddress
_WsSSIDAssociatedClientMacAddress_Object = MibTableColumn
wsSSIDAssociatedClientMacAddress = _WsSSIDAssociatedClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 5, 1, 2),
    _WsSSIDAssociatedClientMacAddress_Type()
)
wsSSIDAssociatedClientMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSSIDAssociatedClientMacAddress.setStatus("obsolete")
_WsSwitchAssociatedClientStatusTable_Object = MibTable
wsSwitchAssociatedClientStatusTable = _WsSwitchAssociatedClientStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 6)
)
if mibBuilder.loadTexts:
    wsSwitchAssociatedClientStatusTable.setStatus("obsolete")
_WsSwitchAssociatedClientStatusEntry_Object = MibTableRow
wsSwitchAssociatedClientStatusEntry = _WsSwitchAssociatedClientStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 6, 1)
)
wsSwitchAssociatedClientStatusEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsSwitchIPAddress"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsSwitchAssociatedClientMacAddress"),
)
if mibBuilder.loadTexts:
    wsSwitchAssociatedClientStatusEntry.setStatus("obsolete")
_WsAssociatedClientSwitchIPAddress_Type = IpAddress
_WsAssociatedClientSwitchIPAddress_Object = MibTableColumn
wsAssociatedClientSwitchIPAddress = _WsAssociatedClientSwitchIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 6, 1, 1),
    _WsAssociatedClientSwitchIPAddress_Type()
)
wsAssociatedClientSwitchIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAssociatedClientSwitchIPAddress.setStatus("obsolete")
_WsSwitchAssociatedClientMacAddress_Type = MacAddress
_WsSwitchAssociatedClientMacAddress_Object = MibTableColumn
wsSwitchAssociatedClientMacAddress = _WsSwitchAssociatedClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 6, 1, 2),
    _WsSwitchAssociatedClientMacAddress_Type()
)
wsSwitchAssociatedClientMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSwitchAssociatedClientMacAddress.setStatus("obsolete")
_WsAssociatedClientQosStatusTable_Object = MibTable
wsAssociatedClientQosStatusTable = _WsAssociatedClientQosStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 7)
)
if mibBuilder.loadTexts:
    wsAssociatedClientQosStatusTable.setStatus("obsolete")
_WsAssociatedClientQosStatusEntry_Object = MibTableRow
wsAssociatedClientQosStatusEntry = _WsAssociatedClientQosStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 7, 1)
)
if mibBuilder.loadTexts:
    wsAssociatedClientQosStatusEntry.setStatus("obsolete")
_WsAssociatedClientQosBandwidthLimitDown_Type = Unsigned32
_WsAssociatedClientQosBandwidthLimitDown_Object = MibTableColumn
wsAssociatedClientQosBandwidthLimitDown = _WsAssociatedClientQosBandwidthLimitDown_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 7, 1, 1),
    _WsAssociatedClientQosBandwidthLimitDown_Type()
)
wsAssociatedClientQosBandwidthLimitDown.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAssociatedClientQosBandwidthLimitDown.setStatus("obsolete")
_WsAssociatedClientQosBandwidthLimitUp_Type = Unsigned32
_WsAssociatedClientQosBandwidthLimitUp_Object = MibTableColumn
wsAssociatedClientQosBandwidthLimitUp = _WsAssociatedClientQosBandwidthLimitUp_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 7, 1, 2),
    _WsAssociatedClientQosBandwidthLimitUp_Type()
)
wsAssociatedClientQosBandwidthLimitUp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAssociatedClientQosBandwidthLimitUp.setStatus("obsolete")


class _WsAssociatedClientQosAccessControlDownType_Type(Integer32):
    """Custom type wsAssociatedClientQosAccessControlDownType based on Integer32"""
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
          ("ip", 2),
          ("mac", 3),
          ("ipv6", 4))
    )


_WsAssociatedClientQosAccessControlDownType_Type.__name__ = "Integer32"
_WsAssociatedClientQosAccessControlDownType_Object = MibTableColumn
wsAssociatedClientQosAccessControlDownType = _WsAssociatedClientQosAccessControlDownType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 7, 1, 3),
    _WsAssociatedClientQosAccessControlDownType_Type()
)
wsAssociatedClientQosAccessControlDownType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAssociatedClientQosAccessControlDownType.setStatus("obsolete")


class _WsAssociatedClientQosAccessControlDownName_Type(DisplayString):
    """Custom type wsAssociatedClientQosAccessControlDownName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_WsAssociatedClientQosAccessControlDownName_Type.__name__ = "DisplayString"
_WsAssociatedClientQosAccessControlDownName_Object = MibTableColumn
wsAssociatedClientQosAccessControlDownName = _WsAssociatedClientQosAccessControlDownName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 7, 1, 4),
    _WsAssociatedClientQosAccessControlDownName_Type()
)
wsAssociatedClientQosAccessControlDownName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAssociatedClientQosAccessControlDownName.setStatus("obsolete")


class _WsAssociatedClientQosAccessControlUpType_Type(Integer32):
    """Custom type wsAssociatedClientQosAccessControlUpType based on Integer32"""
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
          ("ip", 2),
          ("mac", 3),
          ("ipv6", 4))
    )


_WsAssociatedClientQosAccessControlUpType_Type.__name__ = "Integer32"
_WsAssociatedClientQosAccessControlUpType_Object = MibTableColumn
wsAssociatedClientQosAccessControlUpType = _WsAssociatedClientQosAccessControlUpType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 7, 1, 5),
    _WsAssociatedClientQosAccessControlUpType_Type()
)
wsAssociatedClientQosAccessControlUpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAssociatedClientQosAccessControlUpType.setStatus("obsolete")


class _WsAssociatedClientQosAccessControlUpName_Type(DisplayString):
    """Custom type wsAssociatedClientQosAccessControlUpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_WsAssociatedClientQosAccessControlUpName_Type.__name__ = "DisplayString"
_WsAssociatedClientQosAccessControlUpName_Object = MibTableColumn
wsAssociatedClientQosAccessControlUpName = _WsAssociatedClientQosAccessControlUpName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 7, 1, 6),
    _WsAssociatedClientQosAccessControlUpName_Type()
)
wsAssociatedClientQosAccessControlUpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAssociatedClientQosAccessControlUpName.setStatus("obsolete")


class _WsAssociatedClientQosDiffservPolicyDownType_Type(Integer32):
    """Custom type wsAssociatedClientQosDiffservPolicyDownType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("in", 2))
    )


_WsAssociatedClientQosDiffservPolicyDownType_Type.__name__ = "Integer32"
_WsAssociatedClientQosDiffservPolicyDownType_Object = MibTableColumn
wsAssociatedClientQosDiffservPolicyDownType = _WsAssociatedClientQosDiffservPolicyDownType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 7, 1, 7),
    _WsAssociatedClientQosDiffservPolicyDownType_Type()
)
wsAssociatedClientQosDiffservPolicyDownType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAssociatedClientQosDiffservPolicyDownType.setStatus("obsolete")


class _WsAssociatedClientQosDiffservPolicyDownName_Type(DisplayString):
    """Custom type wsAssociatedClientQosDiffservPolicyDownName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_WsAssociatedClientQosDiffservPolicyDownName_Type.__name__ = "DisplayString"
_WsAssociatedClientQosDiffservPolicyDownName_Object = MibTableColumn
wsAssociatedClientQosDiffservPolicyDownName = _WsAssociatedClientQosDiffservPolicyDownName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 7, 1, 8),
    _WsAssociatedClientQosDiffservPolicyDownName_Type()
)
wsAssociatedClientQosDiffservPolicyDownName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAssociatedClientQosDiffservPolicyDownName.setStatus("obsolete")


class _WsAssociatedClientQosDiffservPolicyUpType_Type(Integer32):
    """Custom type wsAssociatedClientQosDiffservPolicyUpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("in", 2))
    )


_WsAssociatedClientQosDiffservPolicyUpType_Type.__name__ = "Integer32"
_WsAssociatedClientQosDiffservPolicyUpType_Object = MibTableColumn
wsAssociatedClientQosDiffservPolicyUpType = _WsAssociatedClientQosDiffservPolicyUpType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 7, 1, 9),
    _WsAssociatedClientQosDiffservPolicyUpType_Type()
)
wsAssociatedClientQosDiffservPolicyUpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAssociatedClientQosDiffservPolicyUpType.setStatus("obsolete")


class _WsAssociatedClientQosDiffservPolicyUpName_Type(DisplayString):
    """Custom type wsAssociatedClientQosDiffservPolicyUpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_WsAssociatedClientQosDiffservPolicyUpName_Type.__name__ = "DisplayString"
_WsAssociatedClientQosDiffservPolicyUpName_Object = MibTableColumn
wsAssociatedClientQosDiffservPolicyUpName = _WsAssociatedClientQosDiffservPolicyUpName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 7, 1, 10),
    _WsAssociatedClientQosDiffservPolicyUpName_Type()
)
wsAssociatedClientQosDiffservPolicyUpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAssociatedClientQosDiffservPolicyUpName.setStatus("obsolete")


class _WsAssociatedClientQosOperStatus_Type(Integer32):
    """Custom type wsAssociatedClientQosOperStatus based on Integer32"""
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


_WsAssociatedClientQosOperStatus_Type.__name__ = "Integer32"
_WsAssociatedClientQosOperStatus_Object = MibTableColumn
wsAssociatedClientQosOperStatus = _WsAssociatedClientQosOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 7, 1, 11),
    _WsAssociatedClientQosOperStatus_Type()
)
wsAssociatedClientQosOperStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAssociatedClientQosOperStatus.setStatus("obsolete")
_WsAssociatedClientSessionStatisticsTable_Object = MibTable
wsAssociatedClientSessionStatisticsTable = _WsAssociatedClientSessionStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 8)
)
if mibBuilder.loadTexts:
    wsAssociatedClientSessionStatisticsTable.setStatus("obsolete")
_WsAssociatedClientSessionStatisticsEntry_Object = MibTableRow
wsAssociatedClientSessionStatisticsEntry = _WsAssociatedClientSessionStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 8, 1)
)
if mibBuilder.loadTexts:
    wsAssociatedClientSessionStatisticsEntry.setStatus("obsolete")
_WsAssociatedClientSessionPktsRecvd_Type = Counter64
_WsAssociatedClientSessionPktsRecvd_Object = MibTableColumn
wsAssociatedClientSessionPktsRecvd = _WsAssociatedClientSessionPktsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 8, 1, 1),
    _WsAssociatedClientSessionPktsRecvd_Type()
)
wsAssociatedClientSessionPktsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAssociatedClientSessionPktsRecvd.setStatus("obsolete")
_WsAssociatedClientSessionBytesRecvd_Type = Counter64
_WsAssociatedClientSessionBytesRecvd_Object = MibTableColumn
wsAssociatedClientSessionBytesRecvd = _WsAssociatedClientSessionBytesRecvd_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 8, 1, 2),
    _WsAssociatedClientSessionBytesRecvd_Type()
)
wsAssociatedClientSessionBytesRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAssociatedClientSessionBytesRecvd.setStatus("obsolete")
_WsAssociatedClientSessionPktsTransmitted_Type = Counter64
_WsAssociatedClientSessionPktsTransmitted_Object = MibTableColumn
wsAssociatedClientSessionPktsTransmitted = _WsAssociatedClientSessionPktsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 8, 1, 3),
    _WsAssociatedClientSessionPktsTransmitted_Type()
)
wsAssociatedClientSessionPktsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAssociatedClientSessionPktsTransmitted.setStatus("obsolete")
_WsAssociatedClientSessionBytesTransmitted_Type = Counter64
_WsAssociatedClientSessionBytesTransmitted_Object = MibTableColumn
wsAssociatedClientSessionBytesTransmitted = _WsAssociatedClientSessionBytesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 8, 1, 4),
    _WsAssociatedClientSessionBytesTransmitted_Type()
)
wsAssociatedClientSessionBytesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAssociatedClientSessionBytesTransmitted.setStatus("obsolete")
_WsAssociatedClientSessionDuplicatePktsRecvd_Type = Counter32
_WsAssociatedClientSessionDuplicatePktsRecvd_Object = MibTableColumn
wsAssociatedClientSessionDuplicatePktsRecvd = _WsAssociatedClientSessionDuplicatePktsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 8, 1, 5),
    _WsAssociatedClientSessionDuplicatePktsRecvd_Type()
)
wsAssociatedClientSessionDuplicatePktsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAssociatedClientSessionDuplicatePktsRecvd.setStatus("obsolete")
_WsAssociatedClientSessionFragmentedPktsRecvd_Type = Counter32
_WsAssociatedClientSessionFragmentedPktsRecvd_Object = MibTableColumn
wsAssociatedClientSessionFragmentedPktsRecvd = _WsAssociatedClientSessionFragmentedPktsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 8, 1, 6),
    _WsAssociatedClientSessionFragmentedPktsRecvd_Type()
)
wsAssociatedClientSessionFragmentedPktsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAssociatedClientSessionFragmentedPktsRecvd.setStatus("obsolete")
_WsAssociatedClientSessionFragmentedPktsTransmitted_Type = Counter32
_WsAssociatedClientSessionFragmentedPktsTransmitted_Object = MibTableColumn
wsAssociatedClientSessionFragmentedPktsTransmitted = _WsAssociatedClientSessionFragmentedPktsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 8, 1, 7),
    _WsAssociatedClientSessionFragmentedPktsTransmitted_Type()
)
wsAssociatedClientSessionFragmentedPktsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAssociatedClientSessionFragmentedPktsTransmitted.setStatus("obsolete")
_WsAssociatedClientSessionTransmitRetryCount_Type = Counter32
_WsAssociatedClientSessionTransmitRetryCount_Object = MibTableColumn
wsAssociatedClientSessionTransmitRetryCount = _WsAssociatedClientSessionTransmitRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 8, 1, 8),
    _WsAssociatedClientSessionTransmitRetryCount_Type()
)
wsAssociatedClientSessionTransmitRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAssociatedClientSessionTransmitRetryCount.setStatus("obsolete")
_WsAssociatedClientSessionTransmitRetryFailedCount_Type = Counter32
_WsAssociatedClientSessionTransmitRetryFailedCount_Object = MibTableColumn
wsAssociatedClientSessionTransmitRetryFailedCount = _WsAssociatedClientSessionTransmitRetryFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 8, 1, 9),
    _WsAssociatedClientSessionTransmitRetryFailedCount_Type()
)
wsAssociatedClientSessionTransmitRetryFailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAssociatedClientSessionTransmitRetryFailedCount.setStatus("obsolete")
_WsAssociatedClientSessionPktsRecvDropped_Type = Counter64
_WsAssociatedClientSessionPktsRecvDropped_Object = MibTableColumn
wsAssociatedClientSessionPktsRecvDropped = _WsAssociatedClientSessionPktsRecvDropped_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 8, 1, 10),
    _WsAssociatedClientSessionPktsRecvDropped_Type()
)
wsAssociatedClientSessionPktsRecvDropped.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAssociatedClientSessionPktsRecvDropped.setStatus("obsolete")
_WsAssociatedClientSessionBytesRecvDropped_Type = Counter64
_WsAssociatedClientSessionBytesRecvDropped_Object = MibTableColumn
wsAssociatedClientSessionBytesRecvDropped = _WsAssociatedClientSessionBytesRecvDropped_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 8, 1, 11),
    _WsAssociatedClientSessionBytesRecvDropped_Type()
)
wsAssociatedClientSessionBytesRecvDropped.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAssociatedClientSessionBytesRecvDropped.setStatus("obsolete")
_WsAssociatedClientSessionPktsTransmitDropped_Type = Counter64
_WsAssociatedClientSessionPktsTransmitDropped_Object = MibTableColumn
wsAssociatedClientSessionPktsTransmitDropped = _WsAssociatedClientSessionPktsTransmitDropped_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 8, 1, 12),
    _WsAssociatedClientSessionPktsTransmitDropped_Type()
)
wsAssociatedClientSessionPktsTransmitDropped.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAssociatedClientSessionPktsTransmitDropped.setStatus("obsolete")
_WsAssociatedClientSessionBytesTransmitDropped_Type = Counter64
_WsAssociatedClientSessionBytesTransmitDropped_Object = MibTableColumn
wsAssociatedClientSessionBytesTransmitDropped = _WsAssociatedClientSessionBytesTransmitDropped_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 8, 1, 13),
    _WsAssociatedClientSessionBytesTransmitDropped_Type()
)
wsAssociatedClientSessionBytesTransmitDropped.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAssociatedClientSessionBytesTransmitDropped.setStatus("obsolete")
_WsAssociatedClientSessionTSViolatePktsRecvd_Type = Counter32
_WsAssociatedClientSessionTSViolatePktsRecvd_Object = MibTableColumn
wsAssociatedClientSessionTSViolatePktsRecvd = _WsAssociatedClientSessionTSViolatePktsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 8, 1, 14),
    _WsAssociatedClientSessionTSViolatePktsRecvd_Type()
)
wsAssociatedClientSessionTSViolatePktsRecvd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAssociatedClientSessionTSViolatePktsRecvd.setStatus("obsolete")
_WsAssociatedClientSessionTSViolatePktsTransmitted_Type = Counter32
_WsAssociatedClientSessionTSViolatePktsTransmitted_Object = MibTableColumn
wsAssociatedClientSessionTSViolatePktsTransmitted = _WsAssociatedClientSessionTSViolatePktsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 8, 1, 15),
    _WsAssociatedClientSessionTSViolatePktsTransmitted_Type()
)
wsAssociatedClientSessionTSViolatePktsTransmitted.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAssociatedClientSessionTSViolatePktsTransmitted.setStatus("obsolete")
_WsAssociatedClientQosCachedStatusTable_Object = MibTable
wsAssociatedClientQosCachedStatusTable = _WsAssociatedClientQosCachedStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 9)
)
if mibBuilder.loadTexts:
    wsAssociatedClientQosCachedStatusTable.setStatus("obsolete")
_WsAssociatedClientQosCachedStatusEntry_Object = MibTableRow
wsAssociatedClientQosCachedStatusEntry = _WsAssociatedClientQosCachedStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 9, 1)
)
if mibBuilder.loadTexts:
    wsAssociatedClientQosCachedStatusEntry.setStatus("obsolete")
_WsAssociatedClientQosCachedBandwidthLimitDown_Type = Unsigned32
_WsAssociatedClientQosCachedBandwidthLimitDown_Object = MibTableColumn
wsAssociatedClientQosCachedBandwidthLimitDown = _WsAssociatedClientQosCachedBandwidthLimitDown_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 9, 1, 1),
    _WsAssociatedClientQosCachedBandwidthLimitDown_Type()
)
wsAssociatedClientQosCachedBandwidthLimitDown.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAssociatedClientQosCachedBandwidthLimitDown.setStatus("obsolete")
_WsAssociatedClientQosCachedBandwidthLimitUp_Type = Unsigned32
_WsAssociatedClientQosCachedBandwidthLimitUp_Object = MibTableColumn
wsAssociatedClientQosCachedBandwidthLimitUp = _WsAssociatedClientQosCachedBandwidthLimitUp_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 9, 1, 2),
    _WsAssociatedClientQosCachedBandwidthLimitUp_Type()
)
wsAssociatedClientQosCachedBandwidthLimitUp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAssociatedClientQosCachedBandwidthLimitUp.setStatus("obsolete")


class _WsAssociatedClientQosCachedAccessControlDownType_Type(Integer32):
    """Custom type wsAssociatedClientQosCachedAccessControlDownType based on Integer32"""
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
          ("ip", 2),
          ("mac", 3),
          ("ipv6", 4))
    )


_WsAssociatedClientQosCachedAccessControlDownType_Type.__name__ = "Integer32"
_WsAssociatedClientQosCachedAccessControlDownType_Object = MibTableColumn
wsAssociatedClientQosCachedAccessControlDownType = _WsAssociatedClientQosCachedAccessControlDownType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 9, 1, 3),
    _WsAssociatedClientQosCachedAccessControlDownType_Type()
)
wsAssociatedClientQosCachedAccessControlDownType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAssociatedClientQosCachedAccessControlDownType.setStatus("obsolete")


class _WsAssociatedClientQosCachedAccessControlDownName_Type(DisplayString):
    """Custom type wsAssociatedClientQosCachedAccessControlDownName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_WsAssociatedClientQosCachedAccessControlDownName_Type.__name__ = "DisplayString"
_WsAssociatedClientQosCachedAccessControlDownName_Object = MibTableColumn
wsAssociatedClientQosCachedAccessControlDownName = _WsAssociatedClientQosCachedAccessControlDownName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 9, 1, 4),
    _WsAssociatedClientQosCachedAccessControlDownName_Type()
)
wsAssociatedClientQosCachedAccessControlDownName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAssociatedClientQosCachedAccessControlDownName.setStatus("obsolete")


class _WsAssociatedClientQosCachedAccessControlUpType_Type(Integer32):
    """Custom type wsAssociatedClientQosCachedAccessControlUpType based on Integer32"""
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
          ("ip", 2),
          ("mac", 3),
          ("ipv6", 4))
    )


_WsAssociatedClientQosCachedAccessControlUpType_Type.__name__ = "Integer32"
_WsAssociatedClientQosCachedAccessControlUpType_Object = MibTableColumn
wsAssociatedClientQosCachedAccessControlUpType = _WsAssociatedClientQosCachedAccessControlUpType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 9, 1, 5),
    _WsAssociatedClientQosCachedAccessControlUpType_Type()
)
wsAssociatedClientQosCachedAccessControlUpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAssociatedClientQosCachedAccessControlUpType.setStatus("obsolete")


class _WsAssociatedClientQosCachedAccessControlUpName_Type(DisplayString):
    """Custom type wsAssociatedClientQosCachedAccessControlUpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_WsAssociatedClientQosCachedAccessControlUpName_Type.__name__ = "DisplayString"
_WsAssociatedClientQosCachedAccessControlUpName_Object = MibTableColumn
wsAssociatedClientQosCachedAccessControlUpName = _WsAssociatedClientQosCachedAccessControlUpName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 9, 1, 6),
    _WsAssociatedClientQosCachedAccessControlUpName_Type()
)
wsAssociatedClientQosCachedAccessControlUpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAssociatedClientQosCachedAccessControlUpName.setStatus("obsolete")


class _WsAssociatedClientQosCachedDiffservPolicyDownType_Type(Integer32):
    """Custom type wsAssociatedClientQosCachedDiffservPolicyDownType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("in", 2))
    )


_WsAssociatedClientQosCachedDiffservPolicyDownType_Type.__name__ = "Integer32"
_WsAssociatedClientQosCachedDiffservPolicyDownType_Object = MibTableColumn
wsAssociatedClientQosCachedDiffservPolicyDownType = _WsAssociatedClientQosCachedDiffservPolicyDownType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 9, 1, 7),
    _WsAssociatedClientQosCachedDiffservPolicyDownType_Type()
)
wsAssociatedClientQosCachedDiffservPolicyDownType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAssociatedClientQosCachedDiffservPolicyDownType.setStatus("obsolete")


class _WsAssociatedClientQosCachedDiffservPolicyDownName_Type(DisplayString):
    """Custom type wsAssociatedClientQosCachedDiffservPolicyDownName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_WsAssociatedClientQosCachedDiffservPolicyDownName_Type.__name__ = "DisplayString"
_WsAssociatedClientQosCachedDiffservPolicyDownName_Object = MibTableColumn
wsAssociatedClientQosCachedDiffservPolicyDownName = _WsAssociatedClientQosCachedDiffservPolicyDownName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 9, 1, 8),
    _WsAssociatedClientQosCachedDiffservPolicyDownName_Type()
)
wsAssociatedClientQosCachedDiffservPolicyDownName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAssociatedClientQosCachedDiffservPolicyDownName.setStatus("obsolete")


class _WsAssociatedClientQosCachedDiffservPolicyUpType_Type(Integer32):
    """Custom type wsAssociatedClientQosCachedDiffservPolicyUpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("in", 2))
    )


_WsAssociatedClientQosCachedDiffservPolicyUpType_Type.__name__ = "Integer32"
_WsAssociatedClientQosCachedDiffservPolicyUpType_Object = MibTableColumn
wsAssociatedClientQosCachedDiffservPolicyUpType = _WsAssociatedClientQosCachedDiffservPolicyUpType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 9, 1, 9),
    _WsAssociatedClientQosCachedDiffservPolicyUpType_Type()
)
wsAssociatedClientQosCachedDiffservPolicyUpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAssociatedClientQosCachedDiffservPolicyUpType.setStatus("obsolete")


class _WsAssociatedClientQosCachedDiffservPolicyUpName_Type(DisplayString):
    """Custom type wsAssociatedClientQosCachedDiffservPolicyUpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_WsAssociatedClientQosCachedDiffservPolicyUpName_Type.__name__ = "DisplayString"
_WsAssociatedClientQosCachedDiffservPolicyUpName_Object = MibTableColumn
wsAssociatedClientQosCachedDiffservPolicyUpName = _WsAssociatedClientQosCachedDiffservPolicyUpName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 7, 9, 1, 10),
    _WsAssociatedClientQosCachedDiffservPolicyUpName_Type()
)
wsAssociatedClientQosCachedDiffservPolicyUpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAssociatedClientQosCachedDiffservPolicyUpName.setStatus("obsolete")
_PeerSwitch_ObjectIdentity = ObjectIdentity
peerSwitch = _PeerSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 8)
)
_WsPeerStatusTable_Object = MibTable
wsPeerStatusTable = _WsPeerStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 8, 1)
)
if mibBuilder.loadTexts:
    wsPeerStatusTable.setStatus("current")
_WsPeerStatusEntry_Object = MibTableRow
wsPeerStatusEntry = _WsPeerStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 8, 1, 1)
)
wsPeerStatusEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsPeerIpAddress"),
)
if mibBuilder.loadTexts:
    wsPeerStatusEntry.setStatus("current")
_WsPeerIpAddress_Type = IpAddress
_WsPeerIpAddress_Object = MibTableColumn
wsPeerIpAddress = _WsPeerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 8, 1, 1, 1),
    _WsPeerIpAddress_Type()
)
wsPeerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPeerIpAddress.setStatus("current")


class _WsPeerClusterControllerIndicator_Type(Integer32):
    """Custom type wsPeerClusterControllerIndicator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_WsPeerClusterControllerIndicator_Type.__name__ = "Integer32"
_WsPeerClusterControllerIndicator_Object = MibTableColumn
wsPeerClusterControllerIndicator = _WsPeerClusterControllerIndicator_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 8, 1, 1, 2),
    _WsPeerClusterControllerIndicator_Type()
)
wsPeerClusterControllerIndicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPeerClusterControllerIndicator.setStatus("current")


class _WsPeerTotalPeerSwitches_Type(Integer32):
    """Custom type wsPeerTotalPeerSwitches based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_WsPeerTotalPeerSwitches_Type.__name__ = "Integer32"
_WsPeerTotalPeerSwitches_Object = MibTableColumn
wsPeerTotalPeerSwitches = _WsPeerTotalPeerSwitches_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 8, 1, 1, 3),
    _WsPeerTotalPeerSwitches_Type()
)
wsPeerTotalPeerSwitches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPeerTotalPeerSwitches.setStatus("current")


class _WsPeerVendorId_Type(Integer32):
    """Custom type wsPeerVendorId based on Integer32"""
    defaultValue = 0


_WsPeerVendorId_Type.__name__ = "Integer32"
_WsPeerVendorId_Object = MibTableColumn
wsPeerVendorId = _WsPeerVendorId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 8, 1, 1, 4),
    _WsPeerVendorId_Type()
)
wsPeerVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPeerVendorId.setStatus("current")


class _WsPeerProtocolVersion_Type(Integer32):
    """Custom type wsPeerProtocolVersion based on Integer32"""
    defaultValue = 0


_WsPeerProtocolVersion_Type.__name__ = "Integer32"
_WsPeerProtocolVersion_Object = MibTableColumn
wsPeerProtocolVersion = _WsPeerProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 8, 1, 1, 5),
    _WsPeerProtocolVersion_Type()
)
wsPeerProtocolVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPeerProtocolVersion.setStatus("current")


class _WsPeerSoftwareVersion_Type(DisplayString):
    """Custom type wsPeerSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WsPeerSoftwareVersion_Type.__name__ = "DisplayString"
_WsPeerSoftwareVersion_Object = MibTableColumn
wsPeerSoftwareVersion = _WsPeerSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 8, 1, 1, 6),
    _WsPeerSoftwareVersion_Type()
)
wsPeerSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPeerSoftwareVersion.setStatus("current")


class _WsPeerDiscoveryReason_Type(Integer32):
    """Custom type wsPeerDiscoveryReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ip-poll", 1),
          ("l2-poll", 2))
    )


_WsPeerDiscoveryReason_Type.__name__ = "Integer32"
_WsPeerDiscoveryReason_Object = MibTableColumn
wsPeerDiscoveryReason = _WsPeerDiscoveryReason_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 8, 1, 1, 7),
    _WsPeerDiscoveryReason_Type()
)
wsPeerDiscoveryReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPeerDiscoveryReason.setStatus("current")
_WsPeerAge_Type = TimeTicks
_WsPeerAge_Object = MibTableColumn
wsPeerAge = _WsPeerAge_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 8, 1, 1, 8),
    _WsPeerAge_Type()
)
wsPeerAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPeerAge.setStatus("current")


class _WsPeerManagedAPCount_Type(Integer32):
    """Custom type wsPeerManagedAPCount based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 192),
    )


_WsPeerManagedAPCount_Type.__name__ = "Integer32"
_WsPeerManagedAPCount_Object = MibTableColumn
wsPeerManagedAPCount = _WsPeerManagedAPCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 8, 1, 1, 9),
    _WsPeerManagedAPCount_Type()
)
wsPeerManagedAPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPeerManagedAPCount.setStatus("current")


class _WsPeerConfigRequestAction_Type(Integer32):
    """Custom type wsPeerConfigRequestAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("start", 2))
    )


_WsPeerConfigRequestAction_Type.__name__ = "Integer32"
_WsPeerConfigRequestAction_Object = MibTableColumn
wsPeerConfigRequestAction = _WsPeerConfigRequestAction_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 8, 1, 1, 10),
    _WsPeerConfigRequestAction_Type()
)
wsPeerConfigRequestAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPeerConfigRequestAction.setStatus("current")


class _WsPeerConfigRequestStatus_Type(Integer32):
    """Custom type wsPeerConfigRequestStatus based on Integer32"""
    defaultValue = 0

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
        *(("notStarted", 0),
          ("requested", 1),
          ("inProgress", 2),
          ("invalidCodeVersion", 3),
          ("invalidHwVersion", 4),
          ("operationInProgress", 5),
          ("invalidConfig", 6),
          ("invalidPacketFormat", 7),
          ("failureTimeout", 8),
          ("failureGeneric", 9),
          ("success", 10))
    )


_WsPeerConfigRequestStatus_Type.__name__ = "Integer32"
_WsPeerConfigRequestStatus_Object = MibTableColumn
wsPeerConfigRequestStatus = _WsPeerConfigRequestStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 8, 1, 1, 11),
    _WsPeerConfigRequestStatus_Type()
)
wsPeerConfigRequestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPeerConfigRequestStatus.setStatus("current")
_WsPeerConfigSwitchIp_Type = IpAddress
_WsPeerConfigSwitchIp_Object = MibTableColumn
wsPeerConfigSwitchIp = _WsPeerConfigSwitchIp_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 8, 1, 1, 12),
    _WsPeerConfigSwitchIp_Type()
)
wsPeerConfigSwitchIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPeerConfigSwitchIp.setStatus("current")


class _WsPeerConfigReceived_Type(Bits):
    """Custom type wsPeerConfigReceived based on Bits"""
    namedValues = NamedValues(
        *(("none", 1),
          ("globalConfig", 2),
          ("discoveryConfig", 3),
          ("validAPDatabase", 4),
          ("channelPowerConfig", 5),
          ("profileNetworkConfig", 6),
          ("knownClientConfig", 7),
          ("captivePortalConfig", 8),
          ("radiusClientConfig", 9),
          ("qosAclConfig", 10),
          ("qosDiffServConfig", 11),
          ("wdsGroupConfig", 12),
          ("deviceLocationConfig", 13))
    )

_WsPeerConfigReceived_Type.__name__ = "Bits"
_WsPeerConfigReceived_Object = MibTableColumn
wsPeerConfigReceived = _WsPeerConfigReceived_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 8, 1, 1, 13),
    _WsPeerConfigReceived_Type()
)
wsPeerConfigReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPeerConfigReceived.setStatus("current")
_WsPeerConfigReceivedTimestamp_Type = DisplayString
_WsPeerConfigReceivedTimestamp_Object = MibTableColumn
wsPeerConfigReceivedTimestamp = _WsPeerConfigReceivedTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 8, 1, 1, 14),
    _WsPeerConfigReceivedTimestamp_Type()
)
wsPeerConfigReceivedTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPeerConfigReceivedTimestamp.setStatus("current")
_WsPeerSwitchManagedAPTable_Object = MibTable
wsPeerSwitchManagedAPTable = _WsPeerSwitchManagedAPTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 8, 3)
)
if mibBuilder.loadTexts:
    wsPeerSwitchManagedAPTable.setStatus("current")
_WsPeerSwitchManagedAPEntry_Object = MibTableRow
wsPeerSwitchManagedAPEntry = _WsPeerSwitchManagedAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 8, 3, 1)
)
wsPeerSwitchManagedAPEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsPeerSwitchIpAddress"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsPeerSwitchAPMacAddress"),
)
if mibBuilder.loadTexts:
    wsPeerSwitchManagedAPEntry.setStatus("current")
_WsPeerSwitchIpAddress_Type = IpAddress
_WsPeerSwitchIpAddress_Object = MibTableColumn
wsPeerSwitchIpAddress = _WsPeerSwitchIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 8, 3, 1, 1),
    _WsPeerSwitchIpAddress_Type()
)
wsPeerSwitchIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPeerSwitchIpAddress.setStatus("current")
_WsPeerSwitchAPMacAddress_Type = MacAddress
_WsPeerSwitchAPMacAddress_Object = MibTableColumn
wsPeerSwitchAPMacAddress = _WsPeerSwitchAPMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 8, 3, 1, 2),
    _WsPeerSwitchAPMacAddress_Type()
)
wsPeerSwitchAPMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPeerSwitchAPMacAddress.setStatus("current")


class _WsPeerSwitchAPLocation_Type(DisplayString):
    """Custom type wsPeerSwitchAPLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WsPeerSwitchAPLocation_Type.__name__ = "DisplayString"
_WsPeerSwitchAPLocation_Object = MibTableColumn
wsPeerSwitchAPLocation = _WsPeerSwitchAPLocation_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 8, 3, 1, 3),
    _WsPeerSwitchAPLocation_Type()
)
wsPeerSwitchAPLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPeerSwitchAPLocation.setStatus("current")
_WsPeerSwitchAPIPAddress_Type = IpAddress
_WsPeerSwitchAPIPAddress_Object = MibTableColumn
wsPeerSwitchAPIPAddress = _WsPeerSwitchAPIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 8, 3, 1, 4),
    _WsPeerSwitchAPIPAddress_Type()
)
wsPeerSwitchAPIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPeerSwitchAPIPAddress.setStatus("current")


class _WsPeerSwitchAPProfileId_Type(Integer32):
    """Custom type wsPeerSwitchAPProfileId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_WsPeerSwitchAPProfileId_Type.__name__ = "Integer32"
_WsPeerSwitchAPProfileId_Object = MibTableColumn
wsPeerSwitchAPProfileId = _WsPeerSwitchAPProfileId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 8, 3, 1, 5),
    _WsPeerSwitchAPProfileId_Type()
)
wsPeerSwitchAPProfileId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPeerSwitchAPProfileId.setStatus("current")


class _WsPeerSwitchAPProfileName_Type(DisplayString):
    """Custom type wsPeerSwitchAPProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WsPeerSwitchAPProfileName_Type.__name__ = "DisplayString"
_WsPeerSwitchAPProfileName_Object = MibTableColumn
wsPeerSwitchAPProfileName = _WsPeerSwitchAPProfileName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 8, 3, 1, 6),
    _WsPeerSwitchAPProfileName_Type()
)
wsPeerSwitchAPProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPeerSwitchAPProfileName.setStatus("current")
_WsPeerSwitchAPHardwareType_Type = Integer32
_WsPeerSwitchAPHardwareType_Object = MibTableColumn
wsPeerSwitchAPHardwareType = _WsPeerSwitchAPHardwareType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 8, 3, 1, 7),
    _WsPeerSwitchAPHardwareType_Type()
)
wsPeerSwitchAPHardwareType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsPeerSwitchAPHardwareType.setStatus("current")
_IntrusionDetection_ObjectIdentity = ObjectIdentity
intrusionDetection = _IntrusionDetection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9)
)
_WsRFScanAPStatusTable_Object = MibTable
wsRFScanAPStatusTable = _WsRFScanAPStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 1)
)
if mibBuilder.loadTexts:
    wsRFScanAPStatusTable.setStatus("current")
_WsRFScanAPStatusEntry_Object = MibTableRow
wsRFScanAPStatusEntry = _WsRFScanAPStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 1, 1)
)
wsRFScanAPStatusEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsRFScanAPMacAddress"),
)
if mibBuilder.loadTexts:
    wsRFScanAPStatusEntry.setStatus("current")
_WsRFScanAPMacAddress_Type = MacAddress
_WsRFScanAPMacAddress_Object = MibTableColumn
wsRFScanAPMacAddress = _WsRFScanAPMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 1, 1, 1),
    _WsRFScanAPMacAddress_Type()
)
wsRFScanAPMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRFScanAPMacAddress.setStatus("current")


class _WsRFScanAPRadioInterface_Type(Integer32):
    """Custom type wsRFScanAPRadioInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WsRFScanAPRadioInterface_Type.__name__ = "Integer32"
_WsRFScanAPRadioInterface_Object = MibTableColumn
wsRFScanAPRadioInterface = _WsRFScanAPRadioInterface_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 1, 1, 2),
    _WsRFScanAPRadioInterface_Type()
)
wsRFScanAPRadioInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRFScanAPRadioInterface.setStatus("current")
_WsRFScanAPBaseMacAddress_Type = MacAddress
_WsRFScanAPBaseMacAddress_Object = MibTableColumn
wsRFScanAPBaseMacAddress = _WsRFScanAPBaseMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 1, 1, 3),
    _WsRFScanAPBaseMacAddress_Type()
)
wsRFScanAPBaseMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRFScanAPBaseMacAddress.setStatus("current")


class _WsRFScanAPSSID_Type(DisplayString):
    """Custom type wsRFScanAPSSID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WsRFScanAPSSID_Type.__name__ = "DisplayString"
_WsRFScanAPSSID_Object = MibTableColumn
wsRFScanAPSSID = _WsRFScanAPSSID_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 1, 1, 4),
    _WsRFScanAPSSID_Type()
)
wsRFScanAPSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRFScanAPSSID.setStatus("current")


class _WsRFScanAPPhysicalMode_Type(Integer32):
    """Custom type wsRFScanAPPhysicalMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ieee802dot11an", 1),
          ("ieee802dot11bORgn", 2))
    )


_WsRFScanAPPhysicalMode_Type.__name__ = "Integer32"
_WsRFScanAPPhysicalMode_Object = MibTableColumn
wsRFScanAPPhysicalMode = _WsRFScanAPPhysicalMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 1, 1, 5),
    _WsRFScanAPPhysicalMode_Type()
)
wsRFScanAPPhysicalMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRFScanAPPhysicalMode.setStatus("current")


class _WsRFScanAPChannel_Type(Integer32):
    """Custom type wsRFScanAPChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 13),
        ValueRangeConstraint(36, 36),
        ValueRangeConstraint(40, 40),
        ValueRangeConstraint(44, 44),
        ValueRangeConstraint(48, 48),
        ValueRangeConstraint(52, 52),
        ValueRangeConstraint(56, 56),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(64, 64),
    )


_WsRFScanAPChannel_Type.__name__ = "Integer32"
_WsRFScanAPChannel_Object = MibTableColumn
wsRFScanAPChannel = _WsRFScanAPChannel_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 1, 1, 6),
    _WsRFScanAPChannel_Type()
)
wsRFScanAPChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRFScanAPChannel.setStatus("current")
_WsRFScanAPTxRate_Type = DisplayString
_WsRFScanAPTxRate_Object = MibTableColumn
wsRFScanAPTxRate = _WsRFScanAPTxRate_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 1, 1, 7),
    _WsRFScanAPTxRate_Type()
)
wsRFScanAPTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRFScanAPTxRate.setStatus("current")


class _WsRFScanAPBeaconInterval_Type(Integer32):
    """Custom type wsRFScanAPBeaconInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 2000),
    )


_WsRFScanAPBeaconInterval_Type.__name__ = "Integer32"
_WsRFScanAPBeaconInterval_Object = MibTableColumn
wsRFScanAPBeaconInterval = _WsRFScanAPBeaconInterval_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 1, 1, 8),
    _WsRFScanAPBeaconInterval_Type()
)
wsRFScanAPBeaconInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRFScanAPBeaconInterval.setStatus("current")


class _WsRFScanAPStatus_Type(Integer32):
    """Custom type wsRFScanAPStatus based on Integer32"""
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
        *(("managed", 1),
          ("unknown", 2),
          ("standalone", 3),
          ("rogue", 4))
    )


_WsRFScanAPStatus_Type.__name__ = "Integer32"
_WsRFScanAPStatus_Object = MibTableColumn
wsRFScanAPStatus = _WsRFScanAPStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 1, 1, 9),
    _WsRFScanAPStatus_Type()
)
wsRFScanAPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRFScanAPStatus.setStatus("current")
_WsRFScanAPDiscoveredAge_Type = TimeTicks
_WsRFScanAPDiscoveredAge_Object = MibTableColumn
wsRFScanAPDiscoveredAge = _WsRFScanAPDiscoveredAge_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 1, 1, 10),
    _WsRFScanAPDiscoveredAge_Type()
)
wsRFScanAPDiscoveredAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRFScanAPDiscoveredAge.setStatus("current")
_WsRFScanAPAge_Type = TimeTicks
_WsRFScanAPAge_Object = MibTableColumn
wsRFScanAPAge = _WsRFScanAPAge_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 1, 1, 11),
    _WsRFScanAPAge_Type()
)
wsRFScanAPAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRFScanAPAge.setStatus("current")


class _WsRFScanAPStatusInitial_Type(Integer32):
    """Custom type wsRFScanAPStatusInitial based on Integer32"""
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
        *(("managed", 1),
          ("unknown", 2),
          ("standalone", 3),
          ("rogue", 4))
    )


_WsRFScanAPStatusInitial_Type.__name__ = "Integer32"
_WsRFScanAPStatusInitial_Object = MibTableColumn
wsRFScanAPStatusInitial = _WsRFScanAPStatusInitial_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 1, 1, 12),
    _WsRFScanAPStatusInitial_Type()
)
wsRFScanAPStatusInitial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRFScanAPStatusInitial.setStatus("current")


class _WsRFScanAPSecurityMode_Type(Integer32):
    """Custom type wsRFScanAPSecurityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("wep", 2),
          ("wpa", 3))
    )


_WsRFScanAPSecurityMode_Type.__name__ = "Integer32"
_WsRFScanAPSecurityMode_Object = MibTableColumn
wsRFScanAPSecurityMode = _WsRFScanAPSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 1, 1, 13),
    _WsRFScanAPSecurityMode_Type()
)
wsRFScanAPSecurityMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRFScanAPSecurityMode.setStatus("current")
_WsRFScanAPHighRate_Type = DisplayString
_WsRFScanAPHighRate_Object = MibTableColumn
wsRFScanAPHighRate = _WsRFScanAPHighRate_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 1, 1, 14),
    _WsRFScanAPHighRate_Type()
)
wsRFScanAPHighRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRFScanAPHighRate.setStatus("current")


class _WsRFScanAPDot11nMode_Type(Integer32):
    """Custom type wsRFScanAPDot11nMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notsupported", 0),
          ("supported", 1))
    )


_WsRFScanAPDot11nMode_Type.__name__ = "Integer32"
_WsRFScanAPDot11nMode_Object = MibTableColumn
wsRFScanAPDot11nMode = _WsRFScanAPDot11nMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 1, 1, 15),
    _WsRFScanAPDot11nMode_Type()
)
wsRFScanAPDot11nMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRFScanAPDot11nMode.setStatus("current")


class _WsRFScanAPAdHoc_Type(Integer32):
    """Custom type wsRFScanAPAdHoc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notadhoc", 0),
          ("adhoc", 1))
    )


_WsRFScanAPAdHoc_Type.__name__ = "Integer32"
_WsRFScanAPAdHoc_Object = MibTableColumn
wsRFScanAPAdHoc = _WsRFScanAPAdHoc_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 1, 1, 16),
    _WsRFScanAPAdHoc_Type()
)
wsRFScanAPAdHoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRFScanAPAdHoc.setStatus("current")


class _WsRFScanAPPeerManaged_Type(Integer32):
    """Custom type wsRFScanAPPeerManaged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("localswitch", 0),
          ("peerswitch", 1))
    )


_WsRFScanAPPeerManaged_Type.__name__ = "Integer32"
_WsRFScanAPPeerManaged_Object = MibTableColumn
wsRFScanAPPeerManaged = _WsRFScanAPPeerManaged_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 1, 1, 17),
    _WsRFScanAPPeerManaged_Type()
)
wsRFScanAPPeerManaged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRFScanAPPeerManaged.setStatus("current")


class _WsRFScanAPRogueMitigation_Type(Integer32):
    """Custom type wsRFScanAPRogueMitigation based on Integer32"""
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
        *(("notrogue", 0),
          ("inprogress", 1),
          ("attackdisabled", 2),
          ("toomany", 3),
          ("illegalchannel", 4),
          ("spoofing", 5),
          ("adhoc", 6))
    )


_WsRFScanAPRogueMitigation_Type.__name__ = "Integer32"
_WsRFScanAPRogueMitigation_Object = MibTableColumn
wsRFScanAPRogueMitigation = _WsRFScanAPRogueMitigation_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 1, 1, 18),
    _WsRFScanAPRogueMitigation_Type()
)
wsRFScanAPRogueMitigation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRFScanAPRogueMitigation.setStatus("current")


class _WsRFScanAPAcknowledgeRogue_Type(Integer32):
    """Custom type wsRFScanAPAcknowledgeRogue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no-action", 0),
          ("acknowledge", 1))
    )


_WsRFScanAPAcknowledgeRogue_Type.__name__ = "Integer32"
_WsRFScanAPAcknowledgeRogue_Object = MibTableColumn
wsRFScanAPAcknowledgeRogue = _WsRFScanAPAcknowledgeRogue_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 1, 1, 19),
    _WsRFScanAPAcknowledgeRogue_Type()
)
wsRFScanAPAcknowledgeRogue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRFScanAPAcknowledgeRogue.setStatus("current")
_WsRFScanAPBSSID_Type = MacAddress
_WsRFScanAPBSSID_Object = MibTableColumn
wsRFScanAPBSSID = _WsRFScanAPBSSID_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 1, 1, 20),
    _WsRFScanAPBSSID_Type()
)
wsRFScanAPBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRFScanAPBSSID.setStatus("current")


class _WsRFScanAPOUI_Type(DisplayString):
    """Custom type wsRFScanAPOUI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WsRFScanAPOUI_Type.__name__ = "DisplayString"
_WsRFScanAPOUI_Object = MibTableColumn
wsRFScanAPOUI = _WsRFScanAPOUI_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 1, 1, 21),
    _WsRFScanAPOUI_Type()
)
wsRFScanAPOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRFScanAPOUI.setStatus("current")


class _WsRFScanAPRRMSupported_Type(Integer32):
    """Custom type wsRFScanAPRRMSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unsupported", 0),
          ("supported", 1))
    )


_WsRFScanAPRRMSupported_Type.__name__ = "Integer32"
_WsRFScanAPRRMSupported_Object = MibTableColumn
wsRFScanAPRRMSupported = _WsRFScanAPRRMSupported_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 1, 1, 22),
    _WsRFScanAPRRMSupported_Type()
)
wsRFScanAPRRMSupported.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRFScanAPRRMSupported.setStatus("current")


class _WsRFScanAPDot11acMode_Type(Integer32):
    """Custom type wsRFScanAPDot11acMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notsupported", 0),
          ("supported", 1))
    )


_WsRFScanAPDot11acMode_Type.__name__ = "Integer32"
_WsRFScanAPDot11acMode_Object = MibTableColumn
wsRFScanAPDot11acMode = _WsRFScanAPDot11acMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 1, 1, 23),
    _WsRFScanAPDot11acMode_Type()
)
wsRFScanAPDot11acMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRFScanAPDot11acMode.setStatus("current")


class _WsRFScanAPEntriesPurge_Type(Integer32):
    """Custom type wsRFScanAPEntriesPurge based on Integer32"""
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


_WsRFScanAPEntriesPurge_Type.__name__ = "Integer32"
_WsRFScanAPEntriesPurge_Object = MibScalar
wsRFScanAPEntriesPurge = _WsRFScanAPEntriesPurge_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 2),
    _WsRFScanAPEntriesPurge_Type()
)
wsRFScanAPEntriesPurge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRFScanAPEntriesPurge.setStatus("current")
_WsFailureAPStatusTable_Object = MibTable
wsFailureAPStatusTable = _WsFailureAPStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 3)
)
if mibBuilder.loadTexts:
    wsFailureAPStatusTable.setStatus("current")
_WsFailureAPStatusEntry_Object = MibTableRow
wsFailureAPStatusEntry = _WsFailureAPStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 3, 1)
)
wsFailureAPStatusEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsFailedAPMacAddress"),
)
if mibBuilder.loadTexts:
    wsFailureAPStatusEntry.setStatus("current")
_WsFailedAPMacAddress_Type = MacAddress
_WsFailedAPMacAddress_Object = MibTableColumn
wsFailedAPMacAddress = _WsFailedAPMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 3, 1, 1),
    _WsFailedAPMacAddress_Type()
)
wsFailedAPMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsFailedAPMacAddress.setStatus("current")
_WsFailedAPIpAddress_Type = IpAddress
_WsFailedAPIpAddress_Object = MibTableColumn
wsFailedAPIpAddress = _WsFailedAPIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 3, 1, 2),
    _WsFailedAPIpAddress_Type()
)
wsFailedAPIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsFailedAPIpAddress.setStatus("current")


class _WsFailedAPVendorId_Type(Integer32):
    """Custom type wsFailedAPVendorId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("broadcom", 1),
          ("others", 65535))
    )


_WsFailedAPVendorId_Type.__name__ = "Integer32"
_WsFailedAPVendorId_Object = MibTableColumn
wsFailedAPVendorId = _WsFailedAPVendorId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 3, 1, 3),
    _WsFailedAPVendorId_Type()
)
wsFailedAPVendorId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsFailedAPVendorId.setStatus("current")


class _WsFailedAPSoftwareVersion_Type(DisplayString):
    """Custom type wsFailedAPSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WsFailedAPSoftwareVersion_Type.__name__ = "DisplayString"
_WsFailedAPSoftwareVersion_Object = MibTableColumn
wsFailedAPSoftwareVersion = _WsFailedAPSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 3, 1, 4),
    _WsFailedAPSoftwareVersion_Type()
)
wsFailedAPSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsFailedAPSoftwareVersion.setStatus("current")


class _WsFailedAPHWType_Type(Integer32):
    """Custom type wsFailedAPHWType based on Integer32"""
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
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("reserved-1", 1),
          ("reserved-2", 2),
          ("reserved-3", 3),
          ("reserved-4", 4),
          ("tq3600", 5),
          ("reserved-6", 6),
          ("reserved-7", 7),
          ("tq3200", 8),
          ("tq2450", 9),
          ("tq3400", 10),
          ("reserved-11", 11),
          ("tq4400", 12),
          ("tq4600", 13))
    )


_WsFailedAPHWType_Type.__name__ = "Integer32"
_WsFailedAPHWType_Object = MibTableColumn
wsFailedAPHWType = _WsFailedAPHWType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 3, 1, 5),
    _WsFailedAPHWType_Type()
)
wsFailedAPHWType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsFailedAPHWType.setStatus("current")


class _WsFailedAPFailureType_Type(Integer32):
    """Custom type wsFailedAPFailureType based on Integer32"""
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
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("localAuthentication", 1),
          ("noDbEntry", 2),
          ("notManaged", 3),
          ("radiusAuthentication", 4),
          ("radiusChallenged", 5),
          ("radiusUnreachable", 6),
          ("invalidRadiusResponse", 7),
          ("invalidProfileId", 8),
          ("profileMismatch", 9),
          ("radiusMsgSendFailed", 10),
          ("noAPImageAvailable", 11))
    )


_WsFailedAPFailureType_Type.__name__ = "Integer32"
_WsFailedAPFailureType_Object = MibTableColumn
wsFailedAPFailureType = _WsFailedAPFailureType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 3, 1, 6),
    _WsFailedAPFailureType_Type()
)
wsFailedAPFailureType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsFailedAPFailureType.setStatus("current")
_WsFailedAPValidationFailureCount_Type = Unsigned32
_WsFailedAPValidationFailureCount_Object = MibTableColumn
wsFailedAPValidationFailureCount = _WsFailedAPValidationFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 3, 1, 7),
    _WsFailedAPValidationFailureCount_Type()
)
wsFailedAPValidationFailureCount.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsFailedAPValidationFailureCount.setStatus("current")
_WsFailedAPAuthenticationFailureCount_Type = Unsigned32
_WsFailedAPAuthenticationFailureCount_Object = MibTableColumn
wsFailedAPAuthenticationFailureCount = _WsFailedAPAuthenticationFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 3, 1, 8),
    _WsFailedAPAuthenticationFailureCount_Type()
)
wsFailedAPAuthenticationFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsFailedAPAuthenticationFailureCount.setStatus("current")


class _WsFailedAPProtocolVersion_Type(Integer32):
    """Custom type wsFailedAPProtocolVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WsFailedAPProtocolVersion_Type.__name__ = "Integer32"
_WsFailedAPProtocolVersion_Object = MibTableColumn
wsFailedAPProtocolVersion = _WsFailedAPProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 3, 1, 9),
    _WsFailedAPProtocolVersion_Type()
)
wsFailedAPProtocolVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsFailedAPProtocolVersion.setStatus("current")
_WsFailedAPAge_Type = TimeTicks
_WsFailedAPAge_Object = MibTableColumn
wsFailedAPAge = _WsFailedAPAge_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 3, 1, 10),
    _WsFailedAPAge_Type()
)
wsFailedAPAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsFailedAPAge.setStatus("current")


class _WsFailedAPReportingSwitch_Type(Integer32):
    """Custom type wsFailedAPReportingSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local-switch", 1),
          ("peer-switch", 2))
    )


_WsFailedAPReportingSwitch_Type.__name__ = "Integer32"
_WsFailedAPReportingSwitch_Object = MibTableColumn
wsFailedAPReportingSwitch = _WsFailedAPReportingSwitch_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 3, 1, 11),
    _WsFailedAPReportingSwitch_Type()
)
wsFailedAPReportingSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsFailedAPReportingSwitch.setStatus("current")
_WsFailedAPSwitchMacAddress_Type = MacAddress
_WsFailedAPSwitchMacAddress_Object = MibTableColumn
wsFailedAPSwitchMacAddress = _WsFailedAPSwitchMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 3, 1, 12),
    _WsFailedAPSwitchMacAddress_Type()
)
wsFailedAPSwitchMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsFailedAPSwitchMacAddress.setStatus("current")
_WsFailedAPSwitchIpAddress_Type = IpAddress
_WsFailedAPSwitchIpAddress_Object = MibTableColumn
wsFailedAPSwitchIpAddress = _WsFailedAPSwitchIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 3, 1, 13),
    _WsFailedAPSwitchIpAddress_Type()
)
wsFailedAPSwitchIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsFailedAPSwitchIpAddress.setStatus("current")


class _WsAPFailureEntriesPurge_Type(Integer32):
    """Custom type wsAPFailureEntriesPurge based on Integer32"""
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


_WsAPFailureEntriesPurge_Type.__name__ = "Integer32"
_WsAPFailureEntriesPurge_Object = MibScalar
wsAPFailureEntriesPurge = _WsAPFailureEntriesPurge_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 4),
    _WsAPFailureEntriesPurge_Type()
)
wsAPFailureEntriesPurge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPFailureEntriesPurge.setStatus("current")
_WsAdHocClientStatusTable_Object = MibTable
wsAdHocClientStatusTable = _WsAdHocClientStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 5)
)
if mibBuilder.loadTexts:
    wsAdHocClientStatusTable.setStatus("current")
_WsAdHocClientStatusEntry_Object = MibTableRow
wsAdHocClientStatusEntry = _WsAdHocClientStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 5, 1)
)
wsAdHocClientStatusEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsAdHocClientMacAddress"),
)
if mibBuilder.loadTexts:
    wsAdHocClientStatusEntry.setStatus("current")
_WsAdHocClientMacAddress_Type = MacAddress
_WsAdHocClientMacAddress_Object = MibTableColumn
wsAdHocClientMacAddress = _WsAdHocClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 5, 1, 1),
    _WsAdHocClientMacAddress_Type()
)
wsAdHocClientMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAdHocClientMacAddress.setStatus("current")
_WsDetectedAPMacAddress_Type = MacAddress
_WsDetectedAPMacAddress_Object = MibTableColumn
wsDetectedAPMacAddress = _WsDetectedAPMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 5, 1, 2),
    _WsDetectedAPMacAddress_Type()
)
wsDetectedAPMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedAPMacAddress.setStatus("current")


class _WsDetectedAPRadioInterface_Type(Integer32):
    """Custom type wsDetectedAPRadioInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WsDetectedAPRadioInterface_Type.__name__ = "Integer32"
_WsDetectedAPRadioInterface_Object = MibTableColumn
wsDetectedAPRadioInterface = _WsDetectedAPRadioInterface_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 5, 1, 3),
    _WsDetectedAPRadioInterface_Type()
)
wsDetectedAPRadioInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedAPRadioInterface.setStatus("current")


class _WsAdHocClientDetectionMode_Type(Integer32):
    """Custom type wsAdHocClientDetectionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("beacon-frame", 1),
          ("data-frame", 2))
    )


_WsAdHocClientDetectionMode_Type.__name__ = "Integer32"
_WsAdHocClientDetectionMode_Object = MibTableColumn
wsAdHocClientDetectionMode = _WsAdHocClientDetectionMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 5, 1, 4),
    _WsAdHocClientDetectionMode_Type()
)
wsAdHocClientDetectionMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAdHocClientDetectionMode.setStatus("current")
_WsAdHocClientAge_Type = TimeTicks
_WsAdHocClientAge_Object = MibTableColumn
wsAdHocClientAge = _WsAdHocClientAge_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 5, 1, 5),
    _WsAdHocClientAge_Type()
)
wsAdHocClientAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAdHocClientAge.setStatus("current")


class _WsAdHocClientEntriesPurge_Type(Integer32):
    """Custom type wsAdHocClientEntriesPurge based on Integer32"""
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


_WsAdHocClientEntriesPurge_Type.__name__ = "Integer32"
_WsAdHocClientEntriesPurge_Object = MibScalar
wsAdHocClientEntriesPurge = _WsAdHocClientEntriesPurge_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 6),
    _WsAdHocClientEntriesPurge_Type()
)
wsAdHocClientEntriesPurge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAdHocClientEntriesPurge.setStatus("current")
_WsAPTriangulationNonSentryStatusTable_Object = MibTable
wsAPTriangulationNonSentryStatusTable = _WsAPTriangulationNonSentryStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 7)
)
if mibBuilder.loadTexts:
    wsAPTriangulationNonSentryStatusTable.setStatus("current")
_WsAPTriangulationNonSentryStatusEntry_Object = MibTableRow
wsAPTriangulationNonSentryStatusEntry = _WsAPTriangulationNonSentryStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 7, 1)
)
wsAPTriangulationNonSentryStatusEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsAPTriangulationMacAddr"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsAPTriangulationId"),
)
if mibBuilder.loadTexts:
    wsAPTriangulationNonSentryStatusEntry.setStatus("current")
_WsAPTriangulationMacAddr_Type = MacAddress
_WsAPTriangulationMacAddr_Object = MibTableColumn
wsAPTriangulationMacAddr = _WsAPTriangulationMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 7, 1, 1),
    _WsAPTriangulationMacAddr_Type()
)
wsAPTriangulationMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPTriangulationMacAddr.setStatus("current")


class _WsAPTriangulationId_Type(Integer32):
    """Custom type wsAPTriangulationId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_WsAPTriangulationId_Type.__name__ = "Integer32"
_WsAPTriangulationId_Object = MibTableColumn
wsAPTriangulationId = _WsAPTriangulationId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 7, 1, 2),
    _WsAPTriangulationId_Type()
)
wsAPTriangulationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPTriangulationId.setStatus("current")
_WsAPTriangulationNonSentryMacAddr_Type = MacAddress
_WsAPTriangulationNonSentryMacAddr_Object = MibTableColumn
wsAPTriangulationNonSentryMacAddr = _WsAPTriangulationNonSentryMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 7, 1, 3),
    _WsAPTriangulationNonSentryMacAddr_Type()
)
wsAPTriangulationNonSentryMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPTriangulationNonSentryMacAddr.setStatus("current")


class _WsAPTriangulationNonSentryRadio_Type(Integer32):
    """Custom type wsAPTriangulationNonSentryRadio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WsAPTriangulationNonSentryRadio_Type.__name__ = "Integer32"
_WsAPTriangulationNonSentryRadio_Object = MibTableColumn
wsAPTriangulationNonSentryRadio = _WsAPTriangulationNonSentryRadio_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 7, 1, 4),
    _WsAPTriangulationNonSentryRadio_Type()
)
wsAPTriangulationNonSentryRadio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPTriangulationNonSentryRadio.setStatus("current")


class _WsAPTriangulationRssi_Type(Integer32):
    """Custom type wsAPTriangulationRssi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_WsAPTriangulationRssi_Type.__name__ = "Integer32"
_WsAPTriangulationRssi_Object = MibTableColumn
wsAPTriangulationRssi = _WsAPTriangulationRssi_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 7, 1, 5),
    _WsAPTriangulationRssi_Type()
)
wsAPTriangulationRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPTriangulationRssi.setStatus("current")


class _WsAPTriangulationStrength_Type(Integer32):
    """Custom type wsAPTriangulationStrength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-127, 127),
    )


_WsAPTriangulationStrength_Type.__name__ = "Integer32"
_WsAPTriangulationStrength_Object = MibTableColumn
wsAPTriangulationStrength = _WsAPTriangulationStrength_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 7, 1, 6),
    _WsAPTriangulationStrength_Type()
)
wsAPTriangulationStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPTriangulationStrength.setStatus("current")


class _WsAPTriangulationNoise_Type(Integer32):
    """Custom type wsAPTriangulationNoise based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-127, 127),
    )


_WsAPTriangulationNoise_Type.__name__ = "Integer32"
_WsAPTriangulationNoise_Object = MibTableColumn
wsAPTriangulationNoise = _WsAPTriangulationNoise_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 7, 1, 7),
    _WsAPTriangulationNoise_Type()
)
wsAPTriangulationNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPTriangulationNoise.setStatus("current")
_WsAPTriangulationAge_Type = TimeTicks
_WsAPTriangulationAge_Object = MibTableColumn
wsAPTriangulationAge = _WsAPTriangulationAge_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 7, 1, 8),
    _WsAPTriangulationAge_Type()
)
wsAPTriangulationAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPTriangulationAge.setStatus("current")
_WsAPTriangulationSentryStatusTable_Object = MibTable
wsAPTriangulationSentryStatusTable = _WsAPTriangulationSentryStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 8)
)
if mibBuilder.loadTexts:
    wsAPTriangulationSentryStatusTable.setStatus("current")
_WsAPTriangulationSentryStatusEntry_Object = MibTableRow
wsAPTriangulationSentryStatusEntry = _WsAPTriangulationSentryStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 8, 1)
)
wsAPTriangulationSentryStatusEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsAPSentryTriangulationMacAddr"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsAPSentryTriangulationId"),
)
if mibBuilder.loadTexts:
    wsAPTriangulationSentryStatusEntry.setStatus("current")
_WsAPSentryTriangulationMacAddr_Type = MacAddress
_WsAPSentryTriangulationMacAddr_Object = MibTableColumn
wsAPSentryTriangulationMacAddr = _WsAPSentryTriangulationMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 8, 1, 1),
    _WsAPSentryTriangulationMacAddr_Type()
)
wsAPSentryTriangulationMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPSentryTriangulationMacAddr.setStatus("current")


class _WsAPSentryTriangulationId_Type(Integer32):
    """Custom type wsAPSentryTriangulationId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_WsAPSentryTriangulationId_Type.__name__ = "Integer32"
_WsAPSentryTriangulationId_Object = MibTableColumn
wsAPSentryTriangulationId = _WsAPSentryTriangulationId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 8, 1, 2),
    _WsAPSentryTriangulationId_Type()
)
wsAPSentryTriangulationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPSentryTriangulationId.setStatus("current")
_WsAPSentryTriangulationSentryMacAddr_Type = MacAddress
_WsAPSentryTriangulationSentryMacAddr_Object = MibTableColumn
wsAPSentryTriangulationSentryMacAddr = _WsAPSentryTriangulationSentryMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 8, 1, 3),
    _WsAPSentryTriangulationSentryMacAddr_Type()
)
wsAPSentryTriangulationSentryMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPSentryTriangulationSentryMacAddr.setStatus("current")


class _WsAPSentryTriangulationSentryRadio_Type(Integer32):
    """Custom type wsAPSentryTriangulationSentryRadio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WsAPSentryTriangulationSentryRadio_Type.__name__ = "Integer32"
_WsAPSentryTriangulationSentryRadio_Object = MibTableColumn
wsAPSentryTriangulationSentryRadio = _WsAPSentryTriangulationSentryRadio_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 8, 1, 4),
    _WsAPSentryTriangulationSentryRadio_Type()
)
wsAPSentryTriangulationSentryRadio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPSentryTriangulationSentryRadio.setStatus("current")


class _WsAPSentryTriangulationRssi_Type(Integer32):
    """Custom type wsAPSentryTriangulationRssi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_WsAPSentryTriangulationRssi_Type.__name__ = "Integer32"
_WsAPSentryTriangulationRssi_Object = MibTableColumn
wsAPSentryTriangulationRssi = _WsAPSentryTriangulationRssi_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 8, 1, 5),
    _WsAPSentryTriangulationRssi_Type()
)
wsAPSentryTriangulationRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPSentryTriangulationRssi.setStatus("current")


class _WsAPSentryTriangulationStrength_Type(Integer32):
    """Custom type wsAPSentryTriangulationStrength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-127, 127),
    )


_WsAPSentryTriangulationStrength_Type.__name__ = "Integer32"
_WsAPSentryTriangulationStrength_Object = MibTableColumn
wsAPSentryTriangulationStrength = _WsAPSentryTriangulationStrength_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 8, 1, 6),
    _WsAPSentryTriangulationStrength_Type()
)
wsAPSentryTriangulationStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPSentryTriangulationStrength.setStatus("current")


class _WsAPSentryTriangulationNoise_Type(Integer32):
    """Custom type wsAPSentryTriangulationNoise based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-127, 127),
    )


_WsAPSentryTriangulationNoise_Type.__name__ = "Integer32"
_WsAPSentryTriangulationNoise_Object = MibTableColumn
wsAPSentryTriangulationNoise = _WsAPSentryTriangulationNoise_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 8, 1, 7),
    _WsAPSentryTriangulationNoise_Type()
)
wsAPSentryTriangulationNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPSentryTriangulationNoise.setStatus("current")
_WsAPSentryTriangulationAge_Type = TimeTicks
_WsAPSentryTriangulationAge_Object = MibTableColumn
wsAPSentryTriangulationAge = _WsAPSentryTriangulationAge_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 8, 1, 8),
    _WsAPSentryTriangulationAge_Type()
)
wsAPSentryTriangulationAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPSentryTriangulationAge.setStatus("current")
_WsAPRogueClassificationStatusTable_Object = MibTable
wsAPRogueClassificationStatusTable = _WsAPRogueClassificationStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 9)
)
if mibBuilder.loadTexts:
    wsAPRogueClassificationStatusTable.setStatus("current")
_WsAPRogueClassificationStatusEntry_Object = MibTableRow
wsAPRogueClassificationStatusEntry = _WsAPRogueClassificationStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 9, 1)
)
wsAPRogueClassificationStatusEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsAPRogueClassificationMacAddr"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsAPRogueClassificationTestId"),
)
if mibBuilder.loadTexts:
    wsAPRogueClassificationStatusEntry.setStatus("current")
_WsAPRogueClassificationMacAddr_Type = MacAddress
_WsAPRogueClassificationMacAddr_Object = MibTableColumn
wsAPRogueClassificationMacAddr = _WsAPRogueClassificationMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 9, 1, 1),
    _WsAPRogueClassificationMacAddr_Type()
)
wsAPRogueClassificationMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPRogueClassificationMacAddr.setStatus("current")


class _WsAPRogueClassificationTestId_Type(Integer32):
    """Custom type wsAPRogueClassificationTestId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_WsAPRogueClassificationTestId_Type.__name__ = "Integer32"
_WsAPRogueClassificationTestId_Object = MibTableColumn
wsAPRogueClassificationTestId = _WsAPRogueClassificationTestId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 9, 1, 2),
    _WsAPRogueClassificationTestId_Type()
)
wsAPRogueClassificationTestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPRogueClassificationTestId.setStatus("current")


class _WsAPRogueClassificationTestName_Type(Integer32):
    """Custom type wsAPRogueClassificationTestName based on Integer32"""
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
        *(("widsaprogue01", 0),
          ("widsaprogue02", 1),
          ("widsaprogue03", 2),
          ("widsaprogue04", 3),
          ("widsaprogue05", 4),
          ("widsaprogue06", 5),
          ("widsaprogue07", 6),
          ("widsaprogue08", 7),
          ("widsaprogue09", 8),
          ("widsaprogue10", 9),
          ("widsaprogue11", 10))
    )


_WsAPRogueClassificationTestName_Type.__name__ = "Integer32"
_WsAPRogueClassificationTestName_Object = MibTableColumn
wsAPRogueClassificationTestName = _WsAPRogueClassificationTestName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 9, 1, 3),
    _WsAPRogueClassificationTestName_Type()
)
wsAPRogueClassificationTestName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPRogueClassificationTestName.setStatus("current")


class _WsAPRogueClassificationDetected_Type(Integer32):
    """Custom type wsAPRogueClassificationDetected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notdetected", 0),
          ("detected", 1))
    )


_WsAPRogueClassificationDetected_Type.__name__ = "Integer32"
_WsAPRogueClassificationDetected_Object = MibTableColumn
wsAPRogueClassificationDetected = _WsAPRogueClassificationDetected_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 9, 1, 4),
    _WsAPRogueClassificationDetected_Type()
)
wsAPRogueClassificationDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPRogueClassificationDetected.setStatus("current")
_WsAPRogueClassificationReportingAPMac_Type = MacAddress
_WsAPRogueClassificationReportingAPMac_Object = MibTableColumn
wsAPRogueClassificationReportingAPMac = _WsAPRogueClassificationReportingAPMac_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 9, 1, 5),
    _WsAPRogueClassificationReportingAPMac_Type()
)
wsAPRogueClassificationReportingAPMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPRogueClassificationReportingAPMac.setStatus("current")


class _WsAPRogueClassificationReportingAPRadio_Type(Integer32):
    """Custom type wsAPRogueClassificationReportingAPRadio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_WsAPRogueClassificationReportingAPRadio_Type.__name__ = "Integer32"
_WsAPRogueClassificationReportingAPRadio_Object = MibTableColumn
wsAPRogueClassificationReportingAPRadio = _WsAPRogueClassificationReportingAPRadio_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 9, 1, 6),
    _WsAPRogueClassificationReportingAPRadio_Type()
)
wsAPRogueClassificationReportingAPRadio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPRogueClassificationReportingAPRadio.setStatus("current")


class _WsAPRogueClassificationTestState_Type(Integer32):
    """Custom type wsAPRogueClassificationTestState based on Integer32"""
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


_WsAPRogueClassificationTestState_Type.__name__ = "Integer32"
_WsAPRogueClassificationTestState_Object = MibTableColumn
wsAPRogueClassificationTestState = _WsAPRogueClassificationTestState_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 9, 1, 7),
    _WsAPRogueClassificationTestState_Type()
)
wsAPRogueClassificationTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPRogueClassificationTestState.setStatus("current")


class _WsAPRogueClassificationTestResult_Type(Integer32):
    """Custom type wsAPRogueClassificationTestResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notreported", 0),
          ("roguereported", 1))
    )


_WsAPRogueClassificationTestResult_Type.__name__ = "Integer32"
_WsAPRogueClassificationTestResult_Object = MibTableColumn
wsAPRogueClassificationTestResult = _WsAPRogueClassificationTestResult_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 9, 1, 8),
    _WsAPRogueClassificationTestResult_Type()
)
wsAPRogueClassificationTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPRogueClassificationTestResult.setStatus("current")
_WsAPRogueClassificationFirstTime_Type = TimeTicks
_WsAPRogueClassificationFirstTime_Object = MibTableColumn
wsAPRogueClassificationFirstTime = _WsAPRogueClassificationFirstTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 9, 1, 9),
    _WsAPRogueClassificationFirstTime_Type()
)
wsAPRogueClassificationFirstTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPRogueClassificationFirstTime.setStatus("current")
_WsAPRogueClassificationLastTime_Type = TimeTicks
_WsAPRogueClassificationLastTime_Object = MibTableColumn
wsAPRogueClassificationLastTime = _WsAPRogueClassificationLastTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 9, 1, 10),
    _WsAPRogueClassificationLastTime_Type()
)
wsAPRogueClassificationLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPRogueClassificationLastTime.setStatus("current")
_WsAPDeAuthenticationAttackStatusTable_Object = MibTable
wsAPDeAuthenticationAttackStatusTable = _WsAPDeAuthenticationAttackStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 10)
)
if mibBuilder.loadTexts:
    wsAPDeAuthenticationAttackStatusTable.setStatus("current")
_WsAPDeAuthenticationAttackStatusEntry_Object = MibTableRow
wsAPDeAuthenticationAttackStatusEntry = _WsAPDeAuthenticationAttackStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 10, 1)
)
wsAPDeAuthenticationAttackStatusEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsAPDeAuthenticationAttackStatusId"),
)
if mibBuilder.loadTexts:
    wsAPDeAuthenticationAttackStatusEntry.setStatus("current")


class _WsAPDeAuthenticationAttackStatusId_Type(Integer32):
    """Custom type wsAPDeAuthenticationAttackStatusId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_WsAPDeAuthenticationAttackStatusId_Type.__name__ = "Integer32"
_WsAPDeAuthenticationAttackStatusId_Object = MibTableColumn
wsAPDeAuthenticationAttackStatusId = _WsAPDeAuthenticationAttackStatusId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 10, 1, 1),
    _WsAPDeAuthenticationAttackStatusId_Type()
)
wsAPDeAuthenticationAttackStatusId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPDeAuthenticationAttackStatusId.setStatus("current")
_WsAPDeAuthenticationAttackBSSID_Type = MacAddress
_WsAPDeAuthenticationAttackBSSID_Object = MibTableColumn
wsAPDeAuthenticationAttackBSSID = _WsAPDeAuthenticationAttackBSSID_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 10, 1, 2),
    _WsAPDeAuthenticationAttackBSSID_Type()
)
wsAPDeAuthenticationAttackBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPDeAuthenticationAttackBSSID.setStatus("current")


class _WsAPDeAuthenticationAttackChannel_Type(Integer32):
    """Custom type wsAPDeAuthenticationAttackChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 161),
    )


_WsAPDeAuthenticationAttackChannel_Type.__name__ = "Integer32"
_WsAPDeAuthenticationAttackChannel_Object = MibTableColumn
wsAPDeAuthenticationAttackChannel = _WsAPDeAuthenticationAttackChannel_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 10, 1, 3),
    _WsAPDeAuthenticationAttackChannel_Type()
)
wsAPDeAuthenticationAttackChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPDeAuthenticationAttackChannel.setStatus("current")
_WsAPDeAuthenticationAttackTime_Type = TimeTicks
_WsAPDeAuthenticationAttackTime_Object = MibTableColumn
wsAPDeAuthenticationAttackTime = _WsAPDeAuthenticationAttackTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 10, 1, 4),
    _WsAPDeAuthenticationAttackTime_Type()
)
wsAPDeAuthenticationAttackTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPDeAuthenticationAttackTime.setStatus("current")
_WsAPDeAuthenticationAttackAge_Type = TimeTicks
_WsAPDeAuthenticationAttackAge_Object = MibTableColumn
wsAPDeAuthenticationAttackAge = _WsAPDeAuthenticationAttackAge_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 10, 1, 5),
    _WsAPDeAuthenticationAttackAge_Type()
)
wsAPDeAuthenticationAttackAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPDeAuthenticationAttackAge.setStatus("current")
_WsDetectedClientStatusTable_Object = MibTable
wsDetectedClientStatusTable = _WsDetectedClientStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 11)
)
if mibBuilder.loadTexts:
    wsDetectedClientStatusTable.setStatus("current")
_WsDetectedClientStatusEntry_Object = MibTableRow
wsDetectedClientStatusEntry = _WsDetectedClientStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 11, 1)
)
wsDetectedClientStatusEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsDetectedClientMacAddress"),
)
if mibBuilder.loadTexts:
    wsDetectedClientStatusEntry.setStatus("current")
_WsDetectedClientMacAddress_Type = MacAddress
_WsDetectedClientMacAddress_Object = MibTableColumn
wsDetectedClientMacAddress = _WsDetectedClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 11, 1, 1),
    _WsDetectedClientMacAddress_Type()
)
wsDetectedClientMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedClientMacAddress.setStatus("current")


class _WsDetectedClientStatus_Type(Integer32):
    """Custom type wsDetectedClientStatus based on Integer32"""
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
        *(("authenticated", 0),
          ("detected", 1),
          ("known", 2),
          ("black-listed", 3),
          ("rogue", 4))
    )


_WsDetectedClientStatus_Type.__name__ = "Integer32"
_WsDetectedClientStatus_Object = MibTableColumn
wsDetectedClientStatus = _WsDetectedClientStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 11, 1, 2),
    _WsDetectedClientStatus_Type()
)
wsDetectedClientStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedClientStatus.setStatus("current")


class _WsDetectedClientAuthStatus_Type(Integer32):
    """Custom type wsDetectedClientAuthStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-authenticated", 0),
          ("authenticated", 1))
    )


_WsDetectedClientAuthStatus_Type.__name__ = "Integer32"
_WsDetectedClientAuthStatus_Object = MibTableColumn
wsDetectedClientAuthStatus = _WsDetectedClientAuthStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 11, 1, 3),
    _WsDetectedClientAuthStatus_Type()
)
wsDetectedClientAuthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedClientAuthStatus.setStatus("current")
_WsDetectedClientEntryLastUpdatedAt_Type = TimeTicks
_WsDetectedClientEntryLastUpdatedAt_Object = MibTableColumn
wsDetectedClientEntryLastUpdatedAt = _WsDetectedClientEntryLastUpdatedAt_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 11, 1, 4),
    _WsDetectedClientEntryLastUpdatedAt_Type()
)
wsDetectedClientEntryLastUpdatedAt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedClientEntryLastUpdatedAt.setStatus("current")


class _WsDetectedClientThreatDetectedStatus_Type(Integer32):
    """Custom type wsDetectedClientThreatDetectedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-detected", 0),
          ("detected", 1))
    )


_WsDetectedClientThreatDetectedStatus_Type.__name__ = "Integer32"
_WsDetectedClientThreatDetectedStatus_Object = MibTableColumn
wsDetectedClientThreatDetectedStatus = _WsDetectedClientThreatDetectedStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 11, 1, 5),
    _WsDetectedClientThreatDetectedStatus_Type()
)
wsDetectedClientThreatDetectedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedClientThreatDetectedStatus.setStatus("current")


class _WsDetectedClientThreatMitigationStatus_Type(Integer32):
    """Custom type wsDetectedClientThreatMitigationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-done", 0),
          ("done", 1))
    )


_WsDetectedClientThreatMitigationStatus_Type.__name__ = "Integer32"
_WsDetectedClientThreatMitigationStatus_Object = MibTableColumn
wsDetectedClientThreatMitigationStatus = _WsDetectedClientThreatMitigationStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 11, 1, 6),
    _WsDetectedClientThreatMitigationStatus_Type()
)
wsDetectedClientThreatMitigationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedClientThreatMitigationStatus.setStatus("current")


class _WsDetectedClientName_Type(DisplayString):
    """Custom type wsDetectedClientName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WsDetectedClientName_Type.__name__ = "DisplayString"
_WsDetectedClientName_Object = MibTableColumn
wsDetectedClientName = _WsDetectedClientName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 11, 1, 7),
    _WsDetectedClientName_Type()
)
wsDetectedClientName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedClientName.setStatus("current")
_WsDetectedClientEntryCreateTime_Type = TimeTicks
_WsDetectedClientEntryCreateTime_Object = MibTableColumn
wsDetectedClientEntryCreateTime = _WsDetectedClientEntryCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 11, 1, 8),
    _WsDetectedClientEntryCreateTime_Type()
)
wsDetectedClientEntryCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedClientEntryCreateTime.setStatus("current")


class _WsDetectedClientChannel_Type(Unsigned32):
    """Custom type wsDetectedClientChannel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_WsDetectedClientChannel_Type.__name__ = "Unsigned32"
_WsDetectedClientChannel_Object = MibTableColumn
wsDetectedClientChannel = _WsDetectedClientChannel_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 11, 1, 9),
    _WsDetectedClientChannel_Type()
)
wsDetectedClientChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedClientChannel.setStatus("current")


class _WsDetectedClientAuthRSSI_Type(Unsigned32):
    """Custom type wsDetectedClientAuthRSSI based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_WsDetectedClientAuthRSSI_Type.__name__ = "Unsigned32"
_WsDetectedClientAuthRSSI_Object = MibTableColumn
wsDetectedClientAuthRSSI = _WsDetectedClientAuthRSSI_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 11, 1, 10),
    _WsDetectedClientAuthRSSI_Type()
)
wsDetectedClientAuthRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedClientAuthRSSI.setStatus("current")


class _WsDetectedClientAuthSignal_Type(Integer32):
    """Custom type wsDetectedClientAuthSignal based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 128),
    )


_WsDetectedClientAuthSignal_Type.__name__ = "Integer32"
_WsDetectedClientAuthSignal_Object = MibTableColumn
wsDetectedClientAuthSignal = _WsDetectedClientAuthSignal_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 11, 1, 11),
    _WsDetectedClientAuthSignal_Type()
)
wsDetectedClientAuthSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedClientAuthSignal.setStatus("current")


class _WsDetectedClientAuthNoise_Type(Integer32):
    """Custom type wsDetectedClientAuthNoise based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 128),
    )


_WsDetectedClientAuthNoise_Type.__name__ = "Integer32"
_WsDetectedClientAuthNoise_Object = MibTableColumn
wsDetectedClientAuthNoise = _WsDetectedClientAuthNoise_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 11, 1, 12),
    _WsDetectedClientAuthNoise_Type()
)
wsDetectedClientAuthNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedClientAuthNoise.setStatus("current")
_WsDetectedClientProbeReqRecorded_Type = Unsigned32
_WsDetectedClientProbeReqRecorded_Object = MibTableColumn
wsDetectedClientProbeReqRecorded = _WsDetectedClientProbeReqRecorded_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 11, 1, 13),
    _WsDetectedClientProbeReqRecorded_Type()
)
wsDetectedClientProbeReqRecorded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedClientProbeReqRecorded.setStatus("current")
_WsDetectedClientProbeCollectionIntvl_Type = TimeTicks
_WsDetectedClientProbeCollectionIntvl_Object = MibTableColumn
wsDetectedClientProbeCollectionIntvl = _WsDetectedClientProbeCollectionIntvl_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 11, 1, 14),
    _WsDetectedClientProbeCollectionIntvl_Type()
)
wsDetectedClientProbeCollectionIntvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedClientProbeCollectionIntvl.setStatus("current")
_WsDetectedClientHighestNumProbes_Type = Unsigned32
_WsDetectedClientHighestNumProbes_Object = MibTableColumn
wsDetectedClientHighestNumProbes = _WsDetectedClientHighestNumProbes_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 11, 1, 15),
    _WsDetectedClientHighestNumProbes_Type()
)
wsDetectedClientHighestNumProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedClientHighestNumProbes.setStatus("current")
_WsDetectedClientAuthMsgsRecorded_Type = Unsigned32
_WsDetectedClientAuthMsgsRecorded_Object = MibTableColumn
wsDetectedClientAuthMsgsRecorded = _WsDetectedClientAuthMsgsRecorded_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 11, 1, 16),
    _WsDetectedClientAuthMsgsRecorded_Type()
)
wsDetectedClientAuthMsgsRecorded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedClientAuthMsgsRecorded.setStatus("current")
_WsDetectedClientAuthCollectionIntvl_Type = TimeTicks
_WsDetectedClientAuthCollectionIntvl_Object = MibTableColumn
wsDetectedClientAuthCollectionIntvl = _WsDetectedClientAuthCollectionIntvl_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 11, 1, 17),
    _WsDetectedClientAuthCollectionIntvl_Type()
)
wsDetectedClientAuthCollectionIntvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedClientAuthCollectionIntvl.setStatus("current")
_WsDetectedClientHighestNumAuthMsgs_Type = Unsigned32
_WsDetectedClientHighestNumAuthMsgs_Object = MibTableColumn
wsDetectedClientHighestNumAuthMsgs = _WsDetectedClientHighestNumAuthMsgs_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 11, 1, 18),
    _WsDetectedClientHighestNumAuthMsgs_Type()
)
wsDetectedClientHighestNumAuthMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedClientHighestNumAuthMsgs.setStatus("current")
_WsDetectedClientDeAuthMsgsRecorded_Type = Unsigned32
_WsDetectedClientDeAuthMsgsRecorded_Object = MibTableColumn
wsDetectedClientDeAuthMsgsRecorded = _WsDetectedClientDeAuthMsgsRecorded_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 11, 1, 19),
    _WsDetectedClientDeAuthMsgsRecorded_Type()
)
wsDetectedClientDeAuthMsgsRecorded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedClientDeAuthMsgsRecorded.setStatus("current")
_WsDetectedClientDeAuthCollectionIntvl_Type = TimeTicks
_WsDetectedClientDeAuthCollectionIntvl_Object = MibTableColumn
wsDetectedClientDeAuthCollectionIntvl = _WsDetectedClientDeAuthCollectionIntvl_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 11, 1, 20),
    _WsDetectedClientDeAuthCollectionIntvl_Type()
)
wsDetectedClientDeAuthCollectionIntvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedClientDeAuthCollectionIntvl.setStatus("current")
_WsDetectedClientHighestNumDeAuthMsgs_Type = Unsigned32
_WsDetectedClientHighestNumDeAuthMsgs_Object = MibTableColumn
wsDetectedClientHighestNumDeAuthMsgs = _WsDetectedClientHighestNumDeAuthMsgs_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 11, 1, 21),
    _WsDetectedClientHighestNumDeAuthMsgs_Type()
)
wsDetectedClientHighestNumDeAuthMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedClientHighestNumDeAuthMsgs.setStatus("current")
_WsDetectedClientAuthFailures_Type = Unsigned32
_WsDetectedClientAuthFailures_Object = MibTableColumn
wsDetectedClientAuthFailures = _WsDetectedClientAuthFailures_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 11, 1, 22),
    _WsDetectedClientAuthFailures_Type()
)
wsDetectedClientAuthFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedClientAuthFailures.setStatus("current")
_WsDetectedClientProbesDetected_Type = Unsigned32
_WsDetectedClientProbesDetected_Object = MibTableColumn
wsDetectedClientProbesDetected = _WsDetectedClientProbesDetected_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 11, 1, 23),
    _WsDetectedClientProbesDetected_Type()
)
wsDetectedClientProbesDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedClientProbesDetected.setStatus("current")
_WsDetectedClientBcastBSSIDProbes_Type = Unsigned32
_WsDetectedClientBcastBSSIDProbes_Object = MibTableColumn
wsDetectedClientBcastBSSIDProbes = _WsDetectedClientBcastBSSIDProbes_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 11, 1, 24),
    _WsDetectedClientBcastBSSIDProbes_Type()
)
wsDetectedClientBcastBSSIDProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedClientBcastBSSIDProbes.setStatus("current")
_WsDetectedClientBcastSSIDProbes_Type = Unsigned32
_WsDetectedClientBcastSSIDProbes_Object = MibTableColumn
wsDetectedClientBcastSSIDProbes = _WsDetectedClientBcastSSIDProbes_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 11, 1, 25),
    _WsDetectedClientBcastSSIDProbes_Type()
)
wsDetectedClientBcastSSIDProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedClientBcastSSIDProbes.setStatus("current")
_WsDetectedClientSpecificBSSIDProbes_Type = Unsigned32
_WsDetectedClientSpecificBSSIDProbes_Object = MibTableColumn
wsDetectedClientSpecificBSSIDProbes = _WsDetectedClientSpecificBSSIDProbes_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 11, 1, 26),
    _WsDetectedClientSpecificBSSIDProbes_Type()
)
wsDetectedClientSpecificBSSIDProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedClientSpecificBSSIDProbes.setStatus("current")
_WsDetectedClientSpecificSSIDProbes_Type = Unsigned32
_WsDetectedClientSpecificSSIDProbes_Object = MibTableColumn
wsDetectedClientSpecificSSIDProbes = _WsDetectedClientSpecificSSIDProbes_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 11, 1, 27),
    _WsDetectedClientSpecificSSIDProbes_Type()
)
wsDetectedClientSpecificSSIDProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedClientSpecificSSIDProbes.setStatus("current")
_WsDetectedClientLastNonBcastBSSID_Type = MacAddress
_WsDetectedClientLastNonBcastBSSID_Object = MibTableColumn
wsDetectedClientLastNonBcastBSSID = _WsDetectedClientLastNonBcastBSSID_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 11, 1, 28),
    _WsDetectedClientLastNonBcastBSSID_Type()
)
wsDetectedClientLastNonBcastBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedClientLastNonBcastBSSID.setStatus("current")
_WsDetectedClientLastNonBcastSSID_Type = DisplayString
_WsDetectedClientLastNonBcastSSID_Object = MibTableColumn
wsDetectedClientLastNonBcastSSID = _WsDetectedClientLastNonBcastSSID_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 11, 1, 29),
    _WsDetectedClientLastNonBcastSSID_Type()
)
wsDetectedClientLastNonBcastSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedClientLastNonBcastSSID.setStatus("current")
_WsDetectedClientThreatMitigationSent_Type = TimeTicks
_WsDetectedClientThreatMitigationSent_Object = MibTableColumn
wsDetectedClientThreatMitigationSent = _WsDetectedClientThreatMitigationSent_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 11, 1, 30),
    _WsDetectedClientThreatMitigationSent_Type()
)
wsDetectedClientThreatMitigationSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedClientThreatMitigationSent.setStatus("current")


class _WsDetectedClientEntryPurge_Type(Integer32):
    """Custom type wsDetectedClientEntryPurge based on Integer32"""
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


_WsDetectedClientEntryPurge_Type.__name__ = "Integer32"
_WsDetectedClientEntryPurge_Object = MibTableColumn
wsDetectedClientEntryPurge = _WsDetectedClientEntryPurge_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 11, 1, 31),
    _WsDetectedClientEntryPurge_Type()
)
wsDetectedClientEntryPurge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedClientEntryPurge.setStatus("current")


class _WsDetectedClientEntryAcknowledge_Type(Integer32):
    """Custom type wsDetectedClientEntryAcknowledge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no-action", 0),
          ("acknowledge", 1))
    )


_WsDetectedClientEntryAcknowledge_Type.__name__ = "Integer32"
_WsDetectedClientEntryAcknowledge_Object = MibTableColumn
wsDetectedClientEntryAcknowledge = _WsDetectedClientEntryAcknowledge_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 11, 1, 32),
    _WsDetectedClientEntryAcknowledge_Type()
)
wsDetectedClientEntryAcknowledge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedClientEntryAcknowledge.setStatus("current")


class _WsDetectedClientOUI_Type(DisplayString):
    """Custom type wsDetectedClientOUI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WsDetectedClientOUI_Type.__name__ = "DisplayString"
_WsDetectedClientOUI_Object = MibTableColumn
wsDetectedClientOUI = _WsDetectedClientOUI_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 11, 1, 33),
    _WsDetectedClientOUI_Type()
)
wsDetectedClientOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedClientOUI.setStatus("current")


class _WsDetectedClientPurgeAll_Type(Integer32):
    """Custom type wsDetectedClientPurgeAll based on Integer32"""
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


_WsDetectedClientPurgeAll_Type.__name__ = "Integer32"
_WsDetectedClientPurgeAll_Object = MibScalar
wsDetectedClientPurgeAll = _WsDetectedClientPurgeAll_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 12),
    _WsDetectedClientPurgeAll_Type()
)
wsDetectedClientPurgeAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedClientPurgeAll.setStatus("current")


class _WsDetectedClientAcknowledgeAll_Type(Integer32):
    """Custom type wsDetectedClientAcknowledgeAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no-action", 0),
          ("acknowledge", 1))
    )


_WsDetectedClientAcknowledgeAll_Type.__name__ = "Integer32"
_WsDetectedClientAcknowledgeAll_Object = MibScalar
wsDetectedClientAcknowledgeAll = _WsDetectedClientAcknowledgeAll_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 13),
    _WsDetectedClientAcknowledgeAll_Type()
)
wsDetectedClientAcknowledgeAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedClientAcknowledgeAll.setStatus("current")
_WsClientRogueClassificationStatusTable_Object = MibTable
wsClientRogueClassificationStatusTable = _WsClientRogueClassificationStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 14)
)
if mibBuilder.loadTexts:
    wsClientRogueClassificationStatusTable.setStatus("current")
_WsClientRogueClassificationStatusEntry_Object = MibTableRow
wsClientRogueClassificationStatusEntry = _WsClientRogueClassificationStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 14, 1)
)
wsClientRogueClassificationStatusEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsClientRogueClassificationMacAddr"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsClientRogueClassificationTestId"),
)
if mibBuilder.loadTexts:
    wsClientRogueClassificationStatusEntry.setStatus("current")
_WsClientRogueClassificationMacAddr_Type = MacAddress
_WsClientRogueClassificationMacAddr_Object = MibTableColumn
wsClientRogueClassificationMacAddr = _WsClientRogueClassificationMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 14, 1, 1),
    _WsClientRogueClassificationMacAddr_Type()
)
wsClientRogueClassificationMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsClientRogueClassificationMacAddr.setStatus("current")


class _WsClientRogueClassificationTestId_Type(Integer32):
    """Custom type wsClientRogueClassificationTestId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_WsClientRogueClassificationTestId_Type.__name__ = "Integer32"
_WsClientRogueClassificationTestId_Object = MibTableColumn
wsClientRogueClassificationTestId = _WsClientRogueClassificationTestId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 14, 1, 2),
    _WsClientRogueClassificationTestId_Type()
)
wsClientRogueClassificationTestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsClientRogueClassificationTestId.setStatus("current")


class _WsClientRogueClassificationTestName_Type(Integer32):
    """Custom type wsClientRogueClassificationTestName based on Integer32"""
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
        *(("widsclientrogue01", 0),
          ("widsclientrogue02", 1),
          ("widsclientrogue03", 2),
          ("widsclientrogue04", 3),
          ("widsclientrogue05", 4),
          ("widsclientrogue06", 5),
          ("widsclientrogue07", 6))
    )


_WsClientRogueClassificationTestName_Type.__name__ = "Integer32"
_WsClientRogueClassificationTestName_Object = MibTableColumn
wsClientRogueClassificationTestName = _WsClientRogueClassificationTestName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 14, 1, 3),
    _WsClientRogueClassificationTestName_Type()
)
wsClientRogueClassificationTestName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsClientRogueClassificationTestName.setStatus("current")


class _WsClientRogueClassificationDetected_Type(Integer32):
    """Custom type wsClientRogueClassificationDetected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notdetected", 0),
          ("detected", 1))
    )


_WsClientRogueClassificationDetected_Type.__name__ = "Integer32"
_WsClientRogueClassificationDetected_Object = MibTableColumn
wsClientRogueClassificationDetected = _WsClientRogueClassificationDetected_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 14, 1, 4),
    _WsClientRogueClassificationDetected_Type()
)
wsClientRogueClassificationDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsClientRogueClassificationDetected.setStatus("current")
_WsClientRogueClassificationReportingAPMac_Type = MacAddress
_WsClientRogueClassificationReportingAPMac_Object = MibTableColumn
wsClientRogueClassificationReportingAPMac = _WsClientRogueClassificationReportingAPMac_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 14, 1, 5),
    _WsClientRogueClassificationReportingAPMac_Type()
)
wsClientRogueClassificationReportingAPMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsClientRogueClassificationReportingAPMac.setStatus("current")


class _WsClientRogueClassificationReportingAPRadio_Type(Integer32):
    """Custom type wsClientRogueClassificationReportingAPRadio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_WsClientRogueClassificationReportingAPRadio_Type.__name__ = "Integer32"
_WsClientRogueClassificationReportingAPRadio_Object = MibTableColumn
wsClientRogueClassificationReportingAPRadio = _WsClientRogueClassificationReportingAPRadio_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 14, 1, 6),
    _WsClientRogueClassificationReportingAPRadio_Type()
)
wsClientRogueClassificationReportingAPRadio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsClientRogueClassificationReportingAPRadio.setStatus("current")


class _WsClientRogueClassificationTestState_Type(Integer32):
    """Custom type wsClientRogueClassificationTestState based on Integer32"""
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


_WsClientRogueClassificationTestState_Type.__name__ = "Integer32"
_WsClientRogueClassificationTestState_Object = MibTableColumn
wsClientRogueClassificationTestState = _WsClientRogueClassificationTestState_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 14, 1, 7),
    _WsClientRogueClassificationTestState_Type()
)
wsClientRogueClassificationTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsClientRogueClassificationTestState.setStatus("current")


class _WsClientRogueClassificationTestResult_Type(Integer32):
    """Custom type wsClientRogueClassificationTestResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notreported", 0),
          ("roguereported", 1))
    )


_WsClientRogueClassificationTestResult_Type.__name__ = "Integer32"
_WsClientRogueClassificationTestResult_Object = MibTableColumn
wsClientRogueClassificationTestResult = _WsClientRogueClassificationTestResult_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 14, 1, 8),
    _WsClientRogueClassificationTestResult_Type()
)
wsClientRogueClassificationTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsClientRogueClassificationTestResult.setStatus("current")
_WsClientRogueClassificationFirstTime_Type = TimeTicks
_WsClientRogueClassificationFirstTime_Object = MibTableColumn
wsClientRogueClassificationFirstTime = _WsClientRogueClassificationFirstTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 14, 1, 9),
    _WsClientRogueClassificationFirstTime_Type()
)
wsClientRogueClassificationFirstTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsClientRogueClassificationFirstTime.setStatus("current")
_WsClientRogueClassificationLastTime_Type = TimeTicks
_WsClientRogueClassificationLastTime_Object = MibTableColumn
wsClientRogueClassificationLastTime = _WsClientRogueClassificationLastTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 14, 1, 10),
    _WsClientRogueClassificationLastTime_Type()
)
wsClientRogueClassificationLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsClientRogueClassificationLastTime.setStatus("current")
_WsDetectedClientTriangulationNonSentryStatusTable_Object = MibTable
wsDetectedClientTriangulationNonSentryStatusTable = _WsDetectedClientTriangulationNonSentryStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 15)
)
if mibBuilder.loadTexts:
    wsDetectedClientTriangulationNonSentryStatusTable.setStatus("current")
_WsDetectedClientTriangulationNonSentryStatusEntry_Object = MibTableRow
wsDetectedClientTriangulationNonSentryStatusEntry = _WsDetectedClientTriangulationNonSentryStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 15, 1)
)
wsDetectedClientTriangulationNonSentryStatusEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsDetectedClientTriangulationMacAddr"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsDetectedClientTriangulationId"),
)
if mibBuilder.loadTexts:
    wsDetectedClientTriangulationNonSentryStatusEntry.setStatus("current")
_WsDetectedClientTriangulationMacAddr_Type = MacAddress
_WsDetectedClientTriangulationMacAddr_Object = MibTableColumn
wsDetectedClientTriangulationMacAddr = _WsDetectedClientTriangulationMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 15, 1, 1),
    _WsDetectedClientTriangulationMacAddr_Type()
)
wsDetectedClientTriangulationMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedClientTriangulationMacAddr.setStatus("current")


class _WsDetectedClientTriangulationId_Type(Integer32):
    """Custom type wsDetectedClientTriangulationId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_WsDetectedClientTriangulationId_Type.__name__ = "Integer32"
_WsDetectedClientTriangulationId_Object = MibTableColumn
wsDetectedClientTriangulationId = _WsDetectedClientTriangulationId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 15, 1, 2),
    _WsDetectedClientTriangulationId_Type()
)
wsDetectedClientTriangulationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedClientTriangulationId.setStatus("current")
_WsDetectedClientTriangulationNonSentryMacAddr_Type = MacAddress
_WsDetectedClientTriangulationNonSentryMacAddr_Object = MibTableColumn
wsDetectedClientTriangulationNonSentryMacAddr = _WsDetectedClientTriangulationNonSentryMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 15, 1, 3),
    _WsDetectedClientTriangulationNonSentryMacAddr_Type()
)
wsDetectedClientTriangulationNonSentryMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedClientTriangulationNonSentryMacAddr.setStatus("current")


class _WsDetectedClientTriangulationNonSentryRadio_Type(Integer32):
    """Custom type wsDetectedClientTriangulationNonSentryRadio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WsDetectedClientTriangulationNonSentryRadio_Type.__name__ = "Integer32"
_WsDetectedClientTriangulationNonSentryRadio_Object = MibTableColumn
wsDetectedClientTriangulationNonSentryRadio = _WsDetectedClientTriangulationNonSentryRadio_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 15, 1, 4),
    _WsDetectedClientTriangulationNonSentryRadio_Type()
)
wsDetectedClientTriangulationNonSentryRadio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedClientTriangulationNonSentryRadio.setStatus("current")


class _WsDetectedClientTriangulationRssi_Type(Integer32):
    """Custom type wsDetectedClientTriangulationRssi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_WsDetectedClientTriangulationRssi_Type.__name__ = "Integer32"
_WsDetectedClientTriangulationRssi_Object = MibTableColumn
wsDetectedClientTriangulationRssi = _WsDetectedClientTriangulationRssi_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 15, 1, 5),
    _WsDetectedClientTriangulationRssi_Type()
)
wsDetectedClientTriangulationRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedClientTriangulationRssi.setStatus("current")


class _WsDetectedClientTriangulationStrength_Type(Integer32):
    """Custom type wsDetectedClientTriangulationStrength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-127, 127),
    )


_WsDetectedClientTriangulationStrength_Type.__name__ = "Integer32"
_WsDetectedClientTriangulationStrength_Object = MibTableColumn
wsDetectedClientTriangulationStrength = _WsDetectedClientTriangulationStrength_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 15, 1, 6),
    _WsDetectedClientTriangulationStrength_Type()
)
wsDetectedClientTriangulationStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedClientTriangulationStrength.setStatus("current")


class _WsDetectedClientTriangulationNoise_Type(Integer32):
    """Custom type wsDetectedClientTriangulationNoise based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-127, 127),
    )


_WsDetectedClientTriangulationNoise_Type.__name__ = "Integer32"
_WsDetectedClientTriangulationNoise_Object = MibTableColumn
wsDetectedClientTriangulationNoise = _WsDetectedClientTriangulationNoise_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 15, 1, 7),
    _WsDetectedClientTriangulationNoise_Type()
)
wsDetectedClientTriangulationNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedClientTriangulationNoise.setStatus("current")
_WsDetectedClientTriangulationAge_Type = TimeTicks
_WsDetectedClientTriangulationAge_Object = MibTableColumn
wsDetectedClientTriangulationAge = _WsDetectedClientTriangulationAge_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 15, 1, 8),
    _WsDetectedClientTriangulationAge_Type()
)
wsDetectedClientTriangulationAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedClientTriangulationAge.setStatus("current")
_WsDetectedClientTriangulationSentryStatusTable_Object = MibTable
wsDetectedClientTriangulationSentryStatusTable = _WsDetectedClientTriangulationSentryStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 16)
)
if mibBuilder.loadTexts:
    wsDetectedClientTriangulationSentryStatusTable.setStatus("current")
_WsDetectedClientTriangulationSentryStatusEntry_Object = MibTableRow
wsDetectedClientTriangulationSentryStatusEntry = _WsDetectedClientTriangulationSentryStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 16, 1)
)
wsDetectedClientTriangulationSentryStatusEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsDetectedClientSentryTriangulationMacAddr"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsDetectedClientSentryTriangulationId"),
)
if mibBuilder.loadTexts:
    wsDetectedClientTriangulationSentryStatusEntry.setStatus("current")
_WsDetectedClientSentryTriangulationMacAddr_Type = MacAddress
_WsDetectedClientSentryTriangulationMacAddr_Object = MibTableColumn
wsDetectedClientSentryTriangulationMacAddr = _WsDetectedClientSentryTriangulationMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 16, 1, 1),
    _WsDetectedClientSentryTriangulationMacAddr_Type()
)
wsDetectedClientSentryTriangulationMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedClientSentryTriangulationMacAddr.setStatus("current")


class _WsDetectedClientSentryTriangulationId_Type(Integer32):
    """Custom type wsDetectedClientSentryTriangulationId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_WsDetectedClientSentryTriangulationId_Type.__name__ = "Integer32"
_WsDetectedClientSentryTriangulationId_Object = MibTableColumn
wsDetectedClientSentryTriangulationId = _WsDetectedClientSentryTriangulationId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 16, 1, 2),
    _WsDetectedClientSentryTriangulationId_Type()
)
wsDetectedClientSentryTriangulationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedClientSentryTriangulationId.setStatus("current")
_WsDetectedClientSentryTriangulationSentryMacAddr_Type = MacAddress
_WsDetectedClientSentryTriangulationSentryMacAddr_Object = MibTableColumn
wsDetectedClientSentryTriangulationSentryMacAddr = _WsDetectedClientSentryTriangulationSentryMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 16, 1, 3),
    _WsDetectedClientSentryTriangulationSentryMacAddr_Type()
)
wsDetectedClientSentryTriangulationSentryMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedClientSentryTriangulationSentryMacAddr.setStatus("current")


class _WsDetectedClientSentryTriangulationSentryRadio_Type(Integer32):
    """Custom type wsDetectedClientSentryTriangulationSentryRadio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WsDetectedClientSentryTriangulationSentryRadio_Type.__name__ = "Integer32"
_WsDetectedClientSentryTriangulationSentryRadio_Object = MibTableColumn
wsDetectedClientSentryTriangulationSentryRadio = _WsDetectedClientSentryTriangulationSentryRadio_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 16, 1, 4),
    _WsDetectedClientSentryTriangulationSentryRadio_Type()
)
wsDetectedClientSentryTriangulationSentryRadio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedClientSentryTriangulationSentryRadio.setStatus("current")


class _WsDetectedClientSentryTriangulationRssi_Type(Integer32):
    """Custom type wsDetectedClientSentryTriangulationRssi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_WsDetectedClientSentryTriangulationRssi_Type.__name__ = "Integer32"
_WsDetectedClientSentryTriangulationRssi_Object = MibTableColumn
wsDetectedClientSentryTriangulationRssi = _WsDetectedClientSentryTriangulationRssi_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 16, 1, 5),
    _WsDetectedClientSentryTriangulationRssi_Type()
)
wsDetectedClientSentryTriangulationRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedClientSentryTriangulationRssi.setStatus("current")


class _WsDetectedClientSentryTriangulationStrength_Type(Integer32):
    """Custom type wsDetectedClientSentryTriangulationStrength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-127, 127),
    )


_WsDetectedClientSentryTriangulationStrength_Type.__name__ = "Integer32"
_WsDetectedClientSentryTriangulationStrength_Object = MibTableColumn
wsDetectedClientSentryTriangulationStrength = _WsDetectedClientSentryTriangulationStrength_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 16, 1, 6),
    _WsDetectedClientSentryTriangulationStrength_Type()
)
wsDetectedClientSentryTriangulationStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedClientSentryTriangulationStrength.setStatus("current")


class _WsDetectedClientSentryTriangulationNoise_Type(Integer32):
    """Custom type wsDetectedClientSentryTriangulationNoise based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-127, 127),
    )


_WsDetectedClientSentryTriangulationNoise_Type.__name__ = "Integer32"
_WsDetectedClientSentryTriangulationNoise_Object = MibTableColumn
wsDetectedClientSentryTriangulationNoise = _WsDetectedClientSentryTriangulationNoise_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 16, 1, 7),
    _WsDetectedClientSentryTriangulationNoise_Type()
)
wsDetectedClientSentryTriangulationNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedClientSentryTriangulationNoise.setStatus("current")
_WsDetectedClientSentryTriangulationAge_Type = TimeTicks
_WsDetectedClientSentryTriangulationAge_Object = MibTableColumn
wsDetectedClientSentryTriangulationAge = _WsDetectedClientSentryTriangulationAge_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 16, 1, 8),
    _WsDetectedClientSentryTriangulationAge_Type()
)
wsDetectedClientSentryTriangulationAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedClientSentryTriangulationAge.setStatus("current")
_WsDetectedClientPreAuthenticationHistoryTable_Object = MibTable
wsDetectedClientPreAuthenticationHistoryTable = _WsDetectedClientPreAuthenticationHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 17)
)
if mibBuilder.loadTexts:
    wsDetectedClientPreAuthenticationHistoryTable.setStatus("current")
_WsDetectedClientPreAuthenticationHistoryEntry_Object = MibTableRow
wsDetectedClientPreAuthenticationHistoryEntry = _WsDetectedClientPreAuthenticationHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 17, 1)
)
wsDetectedClientPreAuthenticationHistoryEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsDetectedClientPreAuthenticationMacAddr"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsDetectedClientPreAuthenticationId"),
)
if mibBuilder.loadTexts:
    wsDetectedClientPreAuthenticationHistoryEntry.setStatus("current")
_WsDetectedClientPreAuthenticationMacAddr_Type = MacAddress
_WsDetectedClientPreAuthenticationMacAddr_Object = MibTableColumn
wsDetectedClientPreAuthenticationMacAddr = _WsDetectedClientPreAuthenticationMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 17, 1, 1),
    _WsDetectedClientPreAuthenticationMacAddr_Type()
)
wsDetectedClientPreAuthenticationMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedClientPreAuthenticationMacAddr.setStatus("current")
_WsDetectedClientPreAuthenticationId_Type = Unsigned32
_WsDetectedClientPreAuthenticationId_Object = MibTableColumn
wsDetectedClientPreAuthenticationId = _WsDetectedClientPreAuthenticationId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 17, 1, 2),
    _WsDetectedClientPreAuthenticationId_Type()
)
wsDetectedClientPreAuthenticationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedClientPreAuthenticationId.setStatus("current")
_WsDetectedClientPreAuthenticationApMac_Type = MacAddress
_WsDetectedClientPreAuthenticationApMac_Object = MibTableColumn
wsDetectedClientPreAuthenticationApMac = _WsDetectedClientPreAuthenticationApMac_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 17, 1, 3),
    _WsDetectedClientPreAuthenticationApMac_Type()
)
wsDetectedClientPreAuthenticationApMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedClientPreAuthenticationApMac.setStatus("current")


class _WsDetectedClientPreAuthenticationApRadioId_Type(Integer32):
    """Custom type wsDetectedClientPreAuthenticationApRadioId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WsDetectedClientPreAuthenticationApRadioId_Type.__name__ = "Integer32"
_WsDetectedClientPreAuthenticationApRadioId_Object = MibTableColumn
wsDetectedClientPreAuthenticationApRadioId = _WsDetectedClientPreAuthenticationApRadioId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 17, 1, 4),
    _WsDetectedClientPreAuthenticationApRadioId_Type()
)
wsDetectedClientPreAuthenticationApRadioId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedClientPreAuthenticationApRadioId.setStatus("current")
_WsDetectedClientPreAuthenticationVapMac_Type = MacAddress
_WsDetectedClientPreAuthenticationVapMac_Object = MibTableColumn
wsDetectedClientPreAuthenticationVapMac = _WsDetectedClientPreAuthenticationVapMac_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 17, 1, 5),
    _WsDetectedClientPreAuthenticationVapMac_Type()
)
wsDetectedClientPreAuthenticationVapMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedClientPreAuthenticationVapMac.setStatus("current")


class _WsDetectedClientPreAuthenticationSSID_Type(DisplayString):
    """Custom type wsDetectedClientPreAuthenticationSSID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WsDetectedClientPreAuthenticationSSID_Type.__name__ = "DisplayString"
_WsDetectedClientPreAuthenticationSSID_Object = MibTableColumn
wsDetectedClientPreAuthenticationSSID = _WsDetectedClientPreAuthenticationSSID_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 17, 1, 6),
    _WsDetectedClientPreAuthenticationSSID_Type()
)
wsDetectedClientPreAuthenticationSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedClientPreAuthenticationSSID.setStatus("current")
_WsDetectedClientPreAuthenticationAge_Type = TimeTicks
_WsDetectedClientPreAuthenticationAge_Object = MibTableColumn
wsDetectedClientPreAuthenticationAge = _WsDetectedClientPreAuthenticationAge_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 17, 1, 7),
    _WsDetectedClientPreAuthenticationAge_Type()
)
wsDetectedClientPreAuthenticationAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedClientPreAuthenticationAge.setStatus("current")


class _WsDetectedClientPreAuthenticationStatus_Type(Integer32):
    """Custom type wsDetectedClientPreAuthenticationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("success", 0),
          ("failure", 1))
    )


_WsDetectedClientPreAuthenticationStatus_Type.__name__ = "Integer32"
_WsDetectedClientPreAuthenticationStatus_Object = MibTableColumn
wsDetectedClientPreAuthenticationStatus = _WsDetectedClientPreAuthenticationStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 17, 1, 8),
    _WsDetectedClientPreAuthenticationStatus_Type()
)
wsDetectedClientPreAuthenticationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedClientPreAuthenticationStatus.setStatus("current")


class _WsDetectedClientPreAuthenticationHistoryPurgeAll_Type(Integer32):
    """Custom type wsDetectedClientPreAuthenticationHistoryPurgeAll based on Integer32"""
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


_WsDetectedClientPreAuthenticationHistoryPurgeAll_Type.__name__ = "Integer32"
_WsDetectedClientPreAuthenticationHistoryPurgeAll_Object = MibScalar
wsDetectedClientPreAuthenticationHistoryPurgeAll = _WsDetectedClientPreAuthenticationHistoryPurgeAll_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 18),
    _WsDetectedClientPreAuthenticationHistoryPurgeAll_Type()
)
wsDetectedClientPreAuthenticationHistoryPurgeAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedClientPreAuthenticationHistoryPurgeAll.setStatus("current")
_WsDetectedClientRoamHistoryTable_Object = MibTable
wsDetectedClientRoamHistoryTable = _WsDetectedClientRoamHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 19)
)
if mibBuilder.loadTexts:
    wsDetectedClientRoamHistoryTable.setStatus("current")
_WsDetectedClientRoamHistoryEntry_Object = MibTableRow
wsDetectedClientRoamHistoryEntry = _WsDetectedClientRoamHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 19, 1)
)
wsDetectedClientRoamHistoryEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsDetectedClientRoamMacAddr"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsDetectedClientRoamId"),
)
if mibBuilder.loadTexts:
    wsDetectedClientRoamHistoryEntry.setStatus("current")
_WsDetectedClientRoamMacAddr_Type = MacAddress
_WsDetectedClientRoamMacAddr_Object = MibTableColumn
wsDetectedClientRoamMacAddr = _WsDetectedClientRoamMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 19, 1, 1),
    _WsDetectedClientRoamMacAddr_Type()
)
wsDetectedClientRoamMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedClientRoamMacAddr.setStatus("current")
_WsDetectedClientRoamId_Type = Unsigned32
_WsDetectedClientRoamId_Object = MibTableColumn
wsDetectedClientRoamId = _WsDetectedClientRoamId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 19, 1, 2),
    _WsDetectedClientRoamId_Type()
)
wsDetectedClientRoamId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedClientRoamId.setStatus("current")
_WsDetectedClientRoamApMac_Type = MacAddress
_WsDetectedClientRoamApMac_Object = MibTableColumn
wsDetectedClientRoamApMac = _WsDetectedClientRoamApMac_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 19, 1, 3),
    _WsDetectedClientRoamApMac_Type()
)
wsDetectedClientRoamApMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedClientRoamApMac.setStatus("current")


class _WsDetectedClientRoamApRadioId_Type(Integer32):
    """Custom type wsDetectedClientRoamApRadioId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WsDetectedClientRoamApRadioId_Type.__name__ = "Integer32"
_WsDetectedClientRoamApRadioId_Object = MibTableColumn
wsDetectedClientRoamApRadioId = _WsDetectedClientRoamApRadioId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 19, 1, 4),
    _WsDetectedClientRoamApRadioId_Type()
)
wsDetectedClientRoamApRadioId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedClientRoamApRadioId.setStatus("current")
_WsDetectedClientRoamVapMac_Type = MacAddress
_WsDetectedClientRoamVapMac_Object = MibTableColumn
wsDetectedClientRoamVapMac = _WsDetectedClientRoamVapMac_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 19, 1, 5),
    _WsDetectedClientRoamVapMac_Type()
)
wsDetectedClientRoamVapMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedClientRoamVapMac.setStatus("current")


class _WsDetectedClientRoamSSID_Type(DisplayString):
    """Custom type wsDetectedClientRoamSSID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WsDetectedClientRoamSSID_Type.__name__ = "DisplayString"
_WsDetectedClientRoamSSID_Object = MibTableColumn
wsDetectedClientRoamSSID = _WsDetectedClientRoamSSID_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 19, 1, 6),
    _WsDetectedClientRoamSSID_Type()
)
wsDetectedClientRoamSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedClientRoamSSID.setStatus("current")
_WsDetectedClientRoamAge_Type = TimeTicks
_WsDetectedClientRoamAge_Object = MibTableColumn
wsDetectedClientRoamAge = _WsDetectedClientRoamAge_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 19, 1, 7),
    _WsDetectedClientRoamAge_Type()
)
wsDetectedClientRoamAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedClientRoamAge.setStatus("current")


class _WsDetectedClientRoamStatus_Type(Integer32):
    """Custom type wsDetectedClientRoamStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("newAuthentication", 1),
          ("roam", 2))
    )


_WsDetectedClientRoamStatus_Type.__name__ = "Integer32"
_WsDetectedClientRoamStatus_Object = MibTableColumn
wsDetectedClientRoamStatus = _WsDetectedClientRoamStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 19, 1, 8),
    _WsDetectedClientRoamStatus_Type()
)
wsDetectedClientRoamStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedClientRoamStatus.setStatus("current")


class _WsDetectedClientRoamHistoryPurgeAll_Type(Integer32):
    """Custom type wsDetectedClientRoamHistoryPurgeAll based on Integer32"""
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


_WsDetectedClientRoamHistoryPurgeAll_Type.__name__ = "Integer32"
_WsDetectedClientRoamHistoryPurgeAll_Object = MibScalar
wsDetectedClientRoamHistoryPurgeAll = _WsDetectedClientRoamHistoryPurgeAll_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 9, 20),
    _WsDetectedClientRoamHistoryPurgeAll_Type()
)
wsDetectedClientRoamHistoryPurgeAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDetectedClientRoamHistoryPurgeAll.setStatus("current")
_SnmpTrapsConfig_ObjectIdentity = ObjectIdentity
snmpTrapsConfig = _SnmpTrapsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 10)
)


class _WsStatusTrapMode_Type(Integer32):
    """Custom type wsStatusTrapMode based on Integer32"""
    defaultValue = 2

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


_WsStatusTrapMode_Type.__name__ = "Integer32"
_WsStatusTrapMode_Object = MibScalar
wsStatusTrapMode = _WsStatusTrapMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 10, 1),
    _WsStatusTrapMode_Type()
)
wsStatusTrapMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsStatusTrapMode.setStatus("current")


class _WsPeerWSTrapMode_Type(Integer32):
    """Custom type wsPeerWSTrapMode based on Integer32"""
    defaultValue = 2

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


_WsPeerWSTrapMode_Type.__name__ = "Integer32"
_WsPeerWSTrapMode_Object = MibScalar
wsPeerWSTrapMode = _WsPeerWSTrapMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 10, 2),
    _WsPeerWSTrapMode_Type()
)
wsPeerWSTrapMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPeerWSTrapMode.setStatus("current")


class _WsAPStateTrapMode_Type(Integer32):
    """Custom type wsAPStateTrapMode based on Integer32"""
    defaultValue = 2

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


_WsAPStateTrapMode_Type.__name__ = "Integer32"
_WsAPStateTrapMode_Object = MibScalar
wsAPStateTrapMode = _WsAPStateTrapMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 10, 3),
    _WsAPStateTrapMode_Type()
)
wsAPStateTrapMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPStateTrapMode.setStatus("current")


class _WsAPFailureTrapMode_Type(Integer32):
    """Custom type wsAPFailureTrapMode based on Integer32"""
    defaultValue = 2

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


_WsAPFailureTrapMode_Type.__name__ = "Integer32"
_WsAPFailureTrapMode_Object = MibScalar
wsAPFailureTrapMode = _WsAPFailureTrapMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 10, 4),
    _WsAPFailureTrapMode_Type()
)
wsAPFailureTrapMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPFailureTrapMode.setStatus("current")


class _WsRogueAPTrapMode_Type(Integer32):
    """Custom type wsRogueAPTrapMode based on Integer32"""
    defaultValue = 2

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


_WsRogueAPTrapMode_Type.__name__ = "Integer32"
_WsRogueAPTrapMode_Object = MibScalar
wsRogueAPTrapMode = _WsRogueAPTrapMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 10, 5),
    _WsRogueAPTrapMode_Type()
)
wsRogueAPTrapMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRogueAPTrapMode.setStatus("current")


class _WsRFScanTrapMode_Type(Integer32):
    """Custom type wsRFScanTrapMode based on Integer32"""
    defaultValue = 2

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


_WsRFScanTrapMode_Type.__name__ = "Integer32"
_WsRFScanTrapMode_Object = MibScalar
wsRFScanTrapMode = _WsRFScanTrapMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 10, 6),
    _WsRFScanTrapMode_Type()
)
wsRFScanTrapMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRFScanTrapMode.setStatus("current")


class _WsClientStateTrapMode_Type(Integer32):
    """Custom type wsClientStateTrapMode based on Integer32"""
    defaultValue = 2

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


_WsClientStateTrapMode_Type.__name__ = "Integer32"
_WsClientStateTrapMode_Object = MibScalar
wsClientStateTrapMode = _WsClientStateTrapMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 10, 7),
    _WsClientStateTrapMode_Type()
)
wsClientStateTrapMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsClientStateTrapMode.setStatus("current")


class _WsWidsStatusMode_Type(Integer32):
    """Custom type wsWidsStatusMode based on Integer32"""
    defaultValue = 2

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


_WsWidsStatusMode_Type.__name__ = "Integer32"
_WsWidsStatusMode_Object = MibScalar
wsWidsStatusMode = _WsWidsStatusMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 10, 8),
    _WsWidsStatusMode_Type()
)
wsWidsStatusMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsWidsStatusMode.setStatus("current")


class _WsTspecTrapMode_Type(Integer32):
    """Custom type wsTspecTrapMode based on Integer32"""
    defaultValue = 2

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


_WsTspecTrapMode_Type.__name__ = "Integer32"
_WsTspecTrapMode_Object = MibScalar
wsTspecTrapMode = _WsTspecTrapMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 10, 9),
    _WsTspecTrapMode_Type()
)
wsTspecTrapMode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsTspecTrapMode.setStatus("current")


class _WsClientFailureTrapMode_Type(Integer32):
    """Custom type wsClientFailureTrapMode based on Integer32"""
    defaultValue = 2

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


_WsClientFailureTrapMode_Type.__name__ = "Integer32"
_WsClientFailureTrapMode_Object = MibScalar
wsClientFailureTrapMode = _WsClientFailureTrapMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 10, 10),
    _WsClientFailureTrapMode_Type()
)
wsClientFailureTrapMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsClientFailureTrapMode.setStatus("current")
_WsMibInfo_ObjectIdentity = ObjectIdentity
wsMibInfo = _WsMibInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 11)
)
_WsMibVersion_Type = Integer32
_WsMibVersion_Object = MibScalar
wsMibVersion = _WsMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 11, 1),
    _WsMibVersion_Type()
)
wsMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMibVersion.setStatus("current")
_WsCapability_ObjectIdentity = ObjectIdentity
wsCapability = _WsCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 12)
)
_WsAPHardwareCapabilityTable_Object = MibTable
wsAPHardwareCapabilityTable = _WsAPHardwareCapabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 12, 1)
)
if mibBuilder.loadTexts:
    wsAPHardwareCapabilityTable.setStatus("current")
_WsAPHardwareCapabilityEntry_Object = MibTableRow
wsAPHardwareCapabilityEntry = _WsAPHardwareCapabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 12, 1, 1)
)
wsAPHardwareCapabilityEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsAPHWTypeID"),
)
if mibBuilder.loadTexts:
    wsAPHardwareCapabilityEntry.setStatus("current")


class _WsAPHWTypeID_Type(Integer32):
    """Custom type wsAPHWTypeID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 13),
    )


_WsAPHWTypeID_Type.__name__ = "Integer32"
_WsAPHWTypeID_Object = MibTableColumn
wsAPHWTypeID = _WsAPHWTypeID_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 12, 1, 1, 1),
    _WsAPHWTypeID_Type()
)
wsAPHWTypeID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAPHWTypeID.setStatus("current")


class _WsAPHWTypeDescription_Type(DisplayString):
    """Custom type wsAPHWTypeDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WsAPHWTypeDescription_Type.__name__ = "DisplayString"
_WsAPHWTypeDescription_Object = MibTableColumn
wsAPHWTypeDescription = _WsAPHWTypeDescription_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 12, 1, 1, 2),
    _WsAPHWTypeDescription_Type()
)
wsAPHWTypeDescription.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAPHWTypeDescription.setStatus("current")


class _WsAPHWTypeRadioCount_Type(Integer32):
    """Custom type wsAPHWTypeRadioCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WsAPHWTypeRadioCount_Type.__name__ = "Integer32"
_WsAPHWTypeRadioCount_Object = MibTableColumn
wsAPHWTypeRadioCount = _WsAPHWTypeRadioCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 12, 1, 1, 3),
    _WsAPHWTypeRadioCount_Type()
)
wsAPHWTypeRadioCount.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAPHWTypeRadioCount.setStatus("current")


class _WsAPImageTypeID_Type(Integer32):
    """Custom type wsAPImageTypeID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WsAPImageTypeID_Type.__name__ = "Integer32"
_WsAPImageTypeID_Object = MibTableColumn
wsAPImageTypeID = _WsAPImageTypeID_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 12, 1, 1, 4),
    _WsAPImageTypeID_Type()
)
wsAPImageTypeID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAPImageTypeID.setStatus("current")


class _WsAPHWDualBootSuppport_Type(Integer32):
    """Custom type wsAPHWDualBootSuppport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notsupported", 0),
          ("supported", 1))
    )


_WsAPHWDualBootSuppport_Type.__name__ = "Integer32"
_WsAPHWDualBootSuppport_Object = MibTableColumn
wsAPHWDualBootSuppport = _WsAPHWDualBootSuppport_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 12, 1, 1, 5),
    _WsAPHWDualBootSuppport_Type()
)
wsAPHWDualBootSuppport.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAPHWDualBootSuppport.setStatus("current")
_WsAPHardwareRadioCapabilityTable_Object = MibTable
wsAPHardwareRadioCapabilityTable = _WsAPHardwareRadioCapabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 12, 2)
)
if mibBuilder.loadTexts:
    wsAPHardwareRadioCapabilityTable.setStatus("current")
_WsAPHardwareRadioCapabilityEntry_Object = MibTableRow
wsAPHardwareRadioCapabilityEntry = _WsAPHardwareRadioCapabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 12, 2, 1)
)
wsAPHardwareRadioCapabilityEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsAPHWTypeID"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsAPHWTypeRadioNum"),
)
if mibBuilder.loadTexts:
    wsAPHardwareRadioCapabilityEntry.setStatus("current")


class _WsAPHWTypeRadioNum_Type(Integer32):
    """Custom type wsAPHWTypeRadioNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WsAPHWTypeRadioNum_Type.__name__ = "Integer32"
_WsAPHWTypeRadioNum_Object = MibTableColumn
wsAPHWTypeRadioNum = _WsAPHWTypeRadioNum_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 12, 2, 1, 1),
    _WsAPHWTypeRadioNum_Type()
)
wsAPHWTypeRadioNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAPHWTypeRadioNum.setStatus("current")


class _WsAPHWTypeRadioID_Type(Integer32):
    """Custom type wsAPHWTypeRadioID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 43421),
    )


_WsAPHWTypeRadioID_Type.__name__ = "Integer32"
_WsAPHWTypeRadioID_Object = MibTableColumn
wsAPHWTypeRadioID = _WsAPHWTypeRadioID_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 12, 2, 1, 2),
    _WsAPHWTypeRadioID_Type()
)
wsAPHWTypeRadioID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPHWTypeRadioID.setStatus("current")


class _WsAPHWTypeRadioDescription_Type(DisplayString):
    """Custom type wsAPHWTypeRadioDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WsAPHWTypeRadioDescription_Type.__name__ = "DisplayString"
_WsAPHWTypeRadioDescription_Object = MibTableColumn
wsAPHWTypeRadioDescription = _WsAPHWTypeRadioDescription_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 12, 2, 1, 3),
    _WsAPHWTypeRadioDescription_Type()
)
wsAPHWTypeRadioDescription.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAPHWTypeRadioDescription.setStatus("current")


class _WsAPHWTypeRadioVapCount_Type(Integer32):
    """Custom type wsAPHWTypeRadioVapCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_WsAPHWTypeRadioVapCount_Type.__name__ = "Integer32"
_WsAPHWTypeRadioVapCount_Object = MibTableColumn
wsAPHWTypeRadioVapCount = _WsAPHWTypeRadioVapCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 12, 2, 1, 4),
    _WsAPHWTypeRadioVapCount_Type()
)
wsAPHWTypeRadioVapCount.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAPHWTypeRadioVapCount.setStatus("current")


class _WsAPHWTypeRadioAmodeSupport_Type(Integer32):
    """Custom type wsAPHWTypeRadioAmodeSupport based on Integer32"""
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


_WsAPHWTypeRadioAmodeSupport_Type.__name__ = "Integer32"
_WsAPHWTypeRadioAmodeSupport_Object = MibTableColumn
wsAPHWTypeRadioAmodeSupport = _WsAPHWTypeRadioAmodeSupport_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 12, 2, 1, 5),
    _WsAPHWTypeRadioAmodeSupport_Type()
)
wsAPHWTypeRadioAmodeSupport.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAPHWTypeRadioAmodeSupport.setStatus("current")


class _WsAPHWTypeRadioBGmodeSupport_Type(Integer32):
    """Custom type wsAPHWTypeRadioBGmodeSupport based on Integer32"""
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


_WsAPHWTypeRadioBGmodeSupport_Type.__name__ = "Integer32"
_WsAPHWTypeRadioBGmodeSupport_Object = MibTableColumn
wsAPHWTypeRadioBGmodeSupport = _WsAPHWTypeRadioBGmodeSupport_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 12, 2, 1, 6),
    _WsAPHWTypeRadioBGmodeSupport_Type()
)
wsAPHWTypeRadioBGmodeSupport.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAPHWTypeRadioBGmodeSupport.setStatus("current")


class _WsAPHWTypeRadioNmodeSupport_Type(Integer32):
    """Custom type wsAPHWTypeRadioNmodeSupport based on Integer32"""
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


_WsAPHWTypeRadioNmodeSupport_Type.__name__ = "Integer32"
_WsAPHWTypeRadioNmodeSupport_Object = MibTableColumn
wsAPHWTypeRadioNmodeSupport = _WsAPHWTypeRadioNmodeSupport_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 12, 2, 1, 7),
    _WsAPHWTypeRadioNmodeSupport_Type()
)
wsAPHWTypeRadioNmodeSupport.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAPHWTypeRadioNmodeSupport.setStatus("current")


class _WsAPHWTypeRadioACmodeSupport_Type(Integer32):
    """Custom type wsAPHWTypeRadioACmodeSupport based on Integer32"""
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


_WsAPHWTypeRadioACmodeSupport_Type.__name__ = "Integer32"
_WsAPHWTypeRadioACmodeSupport_Object = MibTableColumn
wsAPHWTypeRadioACmodeSupport = _WsAPHWTypeRadioACmodeSupport_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 12, 2, 1, 8),
    _WsAPHWTypeRadioACmodeSupport_Type()
)
wsAPHWTypeRadioACmodeSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAPHWTypeRadioACmodeSupport.setStatus("current")
_WsAPImageTypeCapabilityTable_Object = MibTable
wsAPImageTypeCapabilityTable = _WsAPImageTypeCapabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 12, 3)
)
if mibBuilder.loadTexts:
    wsAPImageTypeCapabilityTable.setStatus("current")
_WsAPImageTypeCapabilityEntry_Object = MibTableRow
wsAPImageTypeCapabilityEntry = _WsAPImageTypeCapabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 12, 3, 1)
)
wsAPImageTypeCapabilityEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsAPImageTypeID"),
)
if mibBuilder.loadTexts:
    wsAPImageTypeCapabilityEntry.setStatus("current")


class _WsAPImageTypeDescription_Type(DisplayString):
    """Custom type wsAPImageTypeDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 96),
    )


_WsAPImageTypeDescription_Type.__name__ = "DisplayString"
_WsAPImageTypeDescription_Object = MibTableColumn
wsAPImageTypeDescription = _WsAPImageTypeDescription_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 12, 3, 1, 1),
    _WsAPImageTypeDescription_Type()
)
wsAPImageTypeDescription.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAPImageTypeDescription.setStatus("current")
_WsAPImageAvailabilityTable_Object = MibTable
wsAPImageAvailabilityTable = _WsAPImageAvailabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 12, 4)
)
if mibBuilder.loadTexts:
    wsAPImageAvailabilityTable.setStatus("current")
_WsAPImageAvailabilityEntry_Object = MibTableRow
wsAPImageAvailabilityEntry = _WsAPImageAvailabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 12, 4, 1)
)
wsAPImageAvailabilityEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsAPImageTypeID"),
)
if mibBuilder.loadTexts:
    wsAPImageAvailabilityEntry.setStatus("current")
_WsAPImageAvailability_Type = DisplayString
_WsAPImageAvailability_Object = MibTableColumn
wsAPImageAvailability = _WsAPImageAvailability_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 12, 4, 1, 1),
    _WsAPImageAvailability_Type()
)
wsAPImageAvailability.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAPImageAvailability.setStatus("current")
_L2centTunnel_ObjectIdentity = ObjectIdentity
l2centTunnel = _L2centTunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 13)
)
_WsL2CentTnnlVlanListTable_Object = MibTable
wsL2CentTnnlVlanListTable = _WsL2CentTnnlVlanListTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 13, 1)
)
if mibBuilder.loadTexts:
    wsL2CentTnnlVlanListTable.setStatus("current")
_WsL2CentTnnlVlanListEntry_Object = MibTableRow
wsL2CentTnnlVlanListEntry = _WsL2CentTnnlVlanListEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 13, 1, 1)
)
wsL2CentTnnlVlanListEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsL2CentTnnlVlanId"),
)
if mibBuilder.loadTexts:
    wsL2CentTnnlVlanListEntry.setStatus("current")


class _WsL2CentTnnlVlanId_Type(Integer32):
    """Custom type wsL2CentTnnlVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_WsL2CentTnnlVlanId_Type.__name__ = "Integer32"
_WsL2CentTnnlVlanId_Object = MibTableColumn
wsL2CentTnnlVlanId = _WsL2CentTnnlVlanId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 13, 1, 1, 1),
    _WsL2CentTnnlVlanId_Type()
)
wsL2CentTnnlVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsL2CentTnnlVlanId.setStatus("current")
_WsL2CentTnnlVlanRowStatus_Type = RowStatus
_WsL2CentTnnlVlanRowStatus_Object = MibTableColumn
wsL2CentTnnlVlanRowStatus = _WsL2CentTnnlVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 13, 1, 1, 2),
    _WsL2CentTnnlVlanRowStatus_Type()
)
wsL2CentTnnlVlanRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsL2CentTnnlVlanRowStatus.setStatus("current")
_WsOuiDatabase_ObjectIdentity = ObjectIdentity
wsOuiDatabase = _WsOuiDatabase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 14)
)
_WsOuiTable_Object = MibTable
wsOuiTable = _WsOuiTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 14, 1)
)
if mibBuilder.loadTexts:
    wsOuiTable.setStatus("current")
_WsOuiEntry_Object = MibTableRow
wsOuiEntry = _WsOuiEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 14, 1, 1)
)
wsOuiEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsOuiValue"),
)
if mibBuilder.loadTexts:
    wsOuiEntry.setStatus("current")
_WsOuiValue_Type = WsOui
_WsOuiValue_Object = MibTableColumn
wsOuiValue = _WsOuiValue_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 14, 1, 1, 1),
    _WsOuiValue_Type()
)
wsOuiValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsOuiValue.setStatus("current")
_WsOuiDescription_Type = DisplayString
_WsOuiDescription_Object = MibTableColumn
wsOuiDescription = _WsOuiDescription_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 14, 1, 1, 2),
    _WsOuiDescription_Type()
)
wsOuiDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsOuiDescription.setStatus("current")
_WsOuiRowStatus_Type = RowStatus
_WsOuiRowStatus_Object = MibTableColumn
wsOuiRowStatus = _WsOuiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 14, 1, 1, 3),
    _WsOuiRowStatus_Type()
)
wsOuiRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsOuiRowStatus.setStatus("current")
_RrmNeighbor_ObjectIdentity = ObjectIdentity
rrmNeighbor = _RrmNeighbor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 15)
)
_WsRrmNeighborTable_Object = MibTable
wsRrmNeighborTable = _WsRrmNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 15, 1)
)
if mibBuilder.loadTexts:
    wsRrmNeighborTable.setStatus("current")
_WsRrmNeighborEntry_Object = MibTableRow
wsRrmNeighborEntry = _WsRrmNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 15, 1, 1)
)
wsRrmNeighborEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsRrmNeighborApMacAddr"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsRrmNeighborVapMacAddr"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsRrmNeighborMacAddr"),
)
if mibBuilder.loadTexts:
    wsRrmNeighborEntry.setStatus("current")
_WsRrmNeighborApMacAddr_Type = MacAddress
_WsRrmNeighborApMacAddr_Object = MibTableColumn
wsRrmNeighborApMacAddr = _WsRrmNeighborApMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 15, 1, 1, 1),
    _WsRrmNeighborApMacAddr_Type()
)
wsRrmNeighborApMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRrmNeighborApMacAddr.setStatus("current")
_WsRrmNeighborVapMacAddr_Type = MacAddress
_WsRrmNeighborVapMacAddr_Object = MibTableColumn
wsRrmNeighborVapMacAddr = _WsRrmNeighborVapMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 15, 1, 1, 2),
    _WsRrmNeighborVapMacAddr_Type()
)
wsRrmNeighborVapMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRrmNeighborVapMacAddr.setStatus("current")
_WsRrmNeighborMacAddr_Type = MacAddress
_WsRrmNeighborMacAddr_Object = MibTableColumn
wsRrmNeighborMacAddr = _WsRrmNeighborMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 15, 1, 1, 3),
    _WsRrmNeighborMacAddr_Type()
)
wsRrmNeighborMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRrmNeighborMacAddr.setStatus("current")


class _WsRrmNeighborRSSI_Type(Integer32):
    """Custom type wsRrmNeighborRSSI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_WsRrmNeighborRSSI_Type.__name__ = "Integer32"
_WsRrmNeighborRSSI_Object = MibTableColumn
wsRrmNeighborRSSI = _WsRrmNeighborRSSI_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 15, 1, 1, 4),
    _WsRrmNeighborRSSI_Type()
)
wsRrmNeighborRSSI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRrmNeighborRSSI.setStatus("current")


class _WsRrmNeighborSSID_Type(DisplayString):
    """Custom type wsRrmNeighborSSID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WsRrmNeighborSSID_Type.__name__ = "DisplayString"
_WsRrmNeighborSSID_Object = MibTableColumn
wsRrmNeighborSSID = _WsRrmNeighborSSID_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 15, 1, 1, 5),
    _WsRrmNeighborSSID_Type()
)
wsRrmNeighborSSID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRrmNeighborSSID.setStatus("current")


class _WsRrmNeighborChannel_Type(Integer32):
    """Custom type wsRrmNeighborChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
        ValueRangeConstraint(36, 36),
        ValueRangeConstraint(40, 40),
        ValueRangeConstraint(42, 42),
        ValueRangeConstraint(44, 44),
        ValueRangeConstraint(48, 48),
        ValueRangeConstraint(50, 50),
        ValueRangeConstraint(52, 52),
        ValueRangeConstraint(56, 56),
        ValueRangeConstraint(58, 58),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(64, 64),
        ValueRangeConstraint(100, 100),
        ValueRangeConstraint(104, 104),
        ValueRangeConstraint(108, 108),
        ValueRangeConstraint(112, 112),
        ValueRangeConstraint(116, 116),
        ValueRangeConstraint(120, 120),
        ValueRangeConstraint(124, 124),
        ValueRangeConstraint(128, 128),
        ValueRangeConstraint(132, 132),
        ValueRangeConstraint(136, 136),
        ValueRangeConstraint(140, 140),
        ValueRangeConstraint(149, 149),
        ValueRangeConstraint(152, 152),
        ValueRangeConstraint(153, 153),
        ValueRangeConstraint(157, 157),
        ValueRangeConstraint(160, 160),
        ValueRangeConstraint(161, 161),
        ValueRangeConstraint(165, 165),
    )


_WsRrmNeighborChannel_Type.__name__ = "Integer32"
_WsRrmNeighborChannel_Object = MibTableColumn
wsRrmNeighborChannel = _WsRrmNeighborChannel_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 15, 1, 1, 6),
    _WsRrmNeighborChannel_Type()
)
wsRrmNeighborChannel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRrmNeighborChannel.setStatus("current")
_WsRrmNeighborAge_Type = TimeTicks
_WsRrmNeighborAge_Object = MibTableColumn
wsRrmNeighborAge = _WsRrmNeighborAge_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 15, 1, 1, 7),
    _WsRrmNeighborAge_Type()
)
wsRrmNeighborAge.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRrmNeighborAge.setStatus("current")


class _WsRrmNeighborAllPurge_Type(Integer32):
    """Custom type wsRrmNeighborAllPurge based on Integer32"""
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


_WsRrmNeighborAllPurge_Type.__name__ = "Integer32"
_WsRrmNeighborAllPurge_Object = MibTableColumn
wsRrmNeighborAllPurge = _WsRrmNeighborAllPurge_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 15, 1, 1, 8),
    _WsRrmNeighborAllPurge_Type()
)
wsRrmNeighborAllPurge.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRrmNeighborAllPurge.setStatus("current")


class _WsRrmNeighborApPurge_Type(Integer32):
    """Custom type wsRrmNeighborApPurge based on Integer32"""
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


_WsRrmNeighborApPurge_Type.__name__ = "Integer32"
_WsRrmNeighborApPurge_Object = MibTableColumn
wsRrmNeighborApPurge = _WsRrmNeighborApPurge_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 15, 1, 1, 9),
    _WsRrmNeighborApPurge_Type()
)
wsRrmNeighborApPurge.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRrmNeighborApPurge.setStatus("current")


class _WsRrmNeighborVapPurge_Type(Integer32):
    """Custom type wsRrmNeighborVapPurge based on Integer32"""
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


_WsRrmNeighborVapPurge_Type.__name__ = "Integer32"
_WsRrmNeighborVapPurge_Object = MibTableColumn
wsRrmNeighborVapPurge = _WsRrmNeighborVapPurge_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 15, 1, 1, 10),
    _WsRrmNeighborVapPurge_Type()
)
wsRrmNeighborVapPurge.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRrmNeighborVapPurge.setStatus("current")
_RrmChannelLoad_ObjectIdentity = ObjectIdentity
rrmChannelLoad = _RrmChannelLoad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 16)
)
_WsRrmChannelLoadHistoryTable_Object = MibTable
wsRrmChannelLoadHistoryTable = _WsRrmChannelLoadHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 16, 1)
)
if mibBuilder.loadTexts:
    wsRrmChannelLoadHistoryTable.setStatus("current")
_WsRrmChannelLoadHistoryEntry_Object = MibTableRow
wsRrmChannelLoadHistoryEntry = _WsRrmChannelLoadHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 16, 1, 1)
)
wsRrmChannelLoadHistoryEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsRrmChannelLoadHistoryEntryId"),
)
if mibBuilder.loadTexts:
    wsRrmChannelLoadHistoryEntry.setStatus("current")
_WsRrmChannelLoadHistoryEntryId_Type = Unsigned32
_WsRrmChannelLoadHistoryEntryId_Object = MibTableColumn
wsRrmChannelLoadHistoryEntryId = _WsRrmChannelLoadHistoryEntryId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 16, 1, 1, 1),
    _WsRrmChannelLoadHistoryEntryId_Type()
)
wsRrmChannelLoadHistoryEntryId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRrmChannelLoadHistoryEntryId.setStatus("current")
_WsRrmChannelLoadHistoryEntryApMacAddr_Type = MacAddress
_WsRrmChannelLoadHistoryEntryApMacAddr_Object = MibTableColumn
wsRrmChannelLoadHistoryEntryApMacAddr = _WsRrmChannelLoadHistoryEntryApMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 16, 1, 1, 2),
    _WsRrmChannelLoadHistoryEntryApMacAddr_Type()
)
wsRrmChannelLoadHistoryEntryApMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRrmChannelLoadHistoryEntryApMacAddr.setStatus("current")
_WsRrmChannelLoadHistoryEntryClientMacAddr_Type = MacAddress
_WsRrmChannelLoadHistoryEntryClientMacAddr_Object = MibTableColumn
wsRrmChannelLoadHistoryEntryClientMacAddr = _WsRrmChannelLoadHistoryEntryClientMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 16, 1, 1, 3),
    _WsRrmChannelLoadHistoryEntryClientMacAddr_Type()
)
wsRrmChannelLoadHistoryEntryClientMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRrmChannelLoadHistoryEntryClientMacAddr.setStatus("current")


class _WsRrmChannelLoadHistoryEntryChannel_Type(Unsigned32):
    """Custom type wsRrmChannelLoadHistoryEntryChannel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
        ValueRangeConstraint(36, 36),
        ValueRangeConstraint(40, 40),
        ValueRangeConstraint(42, 42),
        ValueRangeConstraint(44, 44),
        ValueRangeConstraint(48, 48),
        ValueRangeConstraint(50, 50),
        ValueRangeConstraint(52, 52),
        ValueRangeConstraint(56, 56),
        ValueRangeConstraint(58, 58),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(64, 64),
        ValueRangeConstraint(100, 100),
        ValueRangeConstraint(104, 104),
        ValueRangeConstraint(108, 108),
        ValueRangeConstraint(112, 112),
        ValueRangeConstraint(116, 116),
        ValueRangeConstraint(120, 120),
        ValueRangeConstraint(124, 124),
        ValueRangeConstraint(128, 128),
        ValueRangeConstraint(132, 132),
        ValueRangeConstraint(136, 136),
        ValueRangeConstraint(140, 140),
        ValueRangeConstraint(149, 149),
        ValueRangeConstraint(152, 152),
        ValueRangeConstraint(153, 153),
        ValueRangeConstraint(157, 157),
        ValueRangeConstraint(160, 160),
        ValueRangeConstraint(161, 161),
        ValueRangeConstraint(165, 165),
    )


_WsRrmChannelLoadHistoryEntryChannel_Type.__name__ = "Unsigned32"
_WsRrmChannelLoadHistoryEntryChannel_Object = MibTableColumn
wsRrmChannelLoadHistoryEntryChannel = _WsRrmChannelLoadHistoryEntryChannel_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 16, 1, 1, 4),
    _WsRrmChannelLoadHistoryEntryChannel_Type()
)
wsRrmChannelLoadHistoryEntryChannel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRrmChannelLoadHistoryEntryChannel.setStatus("current")
_WsRrmChannelLoadHistoryEntryAge_Type = TimeTicks
_WsRrmChannelLoadHistoryEntryAge_Object = MibTableColumn
wsRrmChannelLoadHistoryEntryAge = _WsRrmChannelLoadHistoryEntryAge_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 16, 1, 1, 5),
    _WsRrmChannelLoadHistoryEntryAge_Type()
)
wsRrmChannelLoadHistoryEntryAge.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRrmChannelLoadHistoryEntryAge.setStatus("current")


class _WsRrmChannelLoadHistoryEntryLoad_Type(Unsigned32):
    """Custom type wsRrmChannelLoadHistoryEntryLoad based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_WsRrmChannelLoadHistoryEntryLoad_Type.__name__ = "Unsigned32"
_WsRrmChannelLoadHistoryEntryLoad_Object = MibTableColumn
wsRrmChannelLoadHistoryEntryLoad = _WsRrmChannelLoadHistoryEntryLoad_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 16, 1, 1, 6),
    _WsRrmChannelLoadHistoryEntryLoad_Type()
)
wsRrmChannelLoadHistoryEntryLoad.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRrmChannelLoadHistoryEntryLoad.setStatus("current")


class _WsRrmChannelLoadHistoryEntryDuration_Type(Unsigned32):
    """Custom type wsRrmChannelLoadHistoryEntryDuration based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WsRrmChannelLoadHistoryEntryDuration_Type.__name__ = "Unsigned32"
_WsRrmChannelLoadHistoryEntryDuration_Object = MibTableColumn
wsRrmChannelLoadHistoryEntryDuration = _WsRrmChannelLoadHistoryEntryDuration_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 16, 1, 1, 7),
    _WsRrmChannelLoadHistoryEntryDuration_Type()
)
wsRrmChannelLoadHistoryEntryDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRrmChannelLoadHistoryEntryDuration.setStatus("current")
_WsRrmChannelLoadCurrentRequest_ObjectIdentity = ObjectIdentity
wsRrmChannelLoadCurrentRequest = _WsRrmChannelLoadCurrentRequest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 16, 2)
)
_WsRrmChannelLoadCurrentRequestClientMacAddr_Type = MacAddress
_WsRrmChannelLoadCurrentRequestClientMacAddr_Object = MibScalar
wsRrmChannelLoadCurrentRequestClientMacAddr = _WsRrmChannelLoadCurrentRequestClientMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 16, 2, 1),
    _WsRrmChannelLoadCurrentRequestClientMacAddr_Type()
)
wsRrmChannelLoadCurrentRequestClientMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRrmChannelLoadCurrentRequestClientMacAddr.setStatus("current")
_WsRrmChannelLoadCurrentRequestApMacAddr_Type = MacAddress
_WsRrmChannelLoadCurrentRequestApMacAddr_Object = MibScalar
wsRrmChannelLoadCurrentRequestApMacAddr = _WsRrmChannelLoadCurrentRequestApMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 16, 2, 2),
    _WsRrmChannelLoadCurrentRequestApMacAddr_Type()
)
wsRrmChannelLoadCurrentRequestApMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRrmChannelLoadCurrentRequestApMacAddr.setStatus("current")


class _WsRrmChannelLoadCurrentRequestChannel_Type(Unsigned32):
    """Custom type wsRrmChannelLoadCurrentRequestChannel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
        ValueRangeConstraint(36, 36),
        ValueRangeConstraint(40, 40),
        ValueRangeConstraint(42, 42),
        ValueRangeConstraint(44, 44),
        ValueRangeConstraint(48, 48),
        ValueRangeConstraint(50, 50),
        ValueRangeConstraint(52, 52),
        ValueRangeConstraint(56, 56),
        ValueRangeConstraint(58, 58),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(64, 64),
        ValueRangeConstraint(100, 100),
        ValueRangeConstraint(104, 104),
        ValueRangeConstraint(108, 108),
        ValueRangeConstraint(112, 112),
        ValueRangeConstraint(116, 116),
        ValueRangeConstraint(120, 120),
        ValueRangeConstraint(124, 124),
        ValueRangeConstraint(128, 128),
        ValueRangeConstraint(132, 132),
        ValueRangeConstraint(136, 136),
        ValueRangeConstraint(140, 140),
        ValueRangeConstraint(149, 149),
        ValueRangeConstraint(152, 152),
        ValueRangeConstraint(153, 153),
        ValueRangeConstraint(157, 157),
        ValueRangeConstraint(160, 160),
        ValueRangeConstraint(161, 161),
        ValueRangeConstraint(165, 165),
    )


_WsRrmChannelLoadCurrentRequestChannel_Type.__name__ = "Unsigned32"
_WsRrmChannelLoadCurrentRequestChannel_Object = MibScalar
wsRrmChannelLoadCurrentRequestChannel = _WsRrmChannelLoadCurrentRequestChannel_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 16, 2, 3),
    _WsRrmChannelLoadCurrentRequestChannel_Type()
)
wsRrmChannelLoadCurrentRequestChannel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRrmChannelLoadCurrentRequestChannel.setStatus("current")


class _WsRrmChannelLoadCurrentRequestDuration_Type(Unsigned32):
    """Custom type wsRrmChannelLoadCurrentRequestDuration based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WsRrmChannelLoadCurrentRequestDuration_Type.__name__ = "Unsigned32"
_WsRrmChannelLoadCurrentRequestDuration_Object = MibScalar
wsRrmChannelLoadCurrentRequestDuration = _WsRrmChannelLoadCurrentRequestDuration_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 16, 2, 4),
    _WsRrmChannelLoadCurrentRequestDuration_Type()
)
wsRrmChannelLoadCurrentRequestDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRrmChannelLoadCurrentRequestDuration.setStatus("current")


class _WsRrmChannelLoadCurrentRequestStatus_Type(Integer32):
    """Custom type wsRrmChannelLoadCurrentRequestStatus based on Integer32"""
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
        *(("notStarted", 0),
          ("success", 1),
          ("inProgress", 2),
          ("timedOut", 3),
          ("aborted", 4),
          ("incapable", 5),
          ("refused", 6))
    )


_WsRrmChannelLoadCurrentRequestStatus_Type.__name__ = "Integer32"
_WsRrmChannelLoadCurrentRequestStatus_Object = MibScalar
wsRrmChannelLoadCurrentRequestStatus = _WsRrmChannelLoadCurrentRequestStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 16, 2, 5),
    _WsRrmChannelLoadCurrentRequestStatus_Type()
)
wsRrmChannelLoadCurrentRequestStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRrmChannelLoadCurrentRequestStatus.setStatus("current")
_WsRrmChannelLoadCurrentRequestTimeRemaining_Type = TimeTicks
_WsRrmChannelLoadCurrentRequestTimeRemaining_Object = MibScalar
wsRrmChannelLoadCurrentRequestTimeRemaining = _WsRrmChannelLoadCurrentRequestTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 16, 2, 6),
    _WsRrmChannelLoadCurrentRequestTimeRemaining_Type()
)
wsRrmChannelLoadCurrentRequestTimeRemaining.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRrmChannelLoadCurrentRequestTimeRemaining.setStatus("current")


class _WsRrmChannelLoadCurrentRequestAbort_Type(Integer32):
    """Custom type wsRrmChannelLoadCurrentRequestAbort based on Integer32"""
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


_WsRrmChannelLoadCurrentRequestAbort_Type.__name__ = "Integer32"
_WsRrmChannelLoadCurrentRequestAbort_Object = MibScalar
wsRrmChannelLoadCurrentRequestAbort = _WsRrmChannelLoadCurrentRequestAbort_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 16, 2, 7),
    _WsRrmChannelLoadCurrentRequestAbort_Type()
)
wsRrmChannelLoadCurrentRequestAbort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRrmChannelLoadCurrentRequestAbort.setStatus("current")
_WsRrmChannelLoadNewRequest_ObjectIdentity = ObjectIdentity
wsRrmChannelLoadNewRequest = _WsRrmChannelLoadNewRequest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 16, 3)
)
_WsRrmChannelLoadNewRequestClientMacAddr_Type = MacAddress
_WsRrmChannelLoadNewRequestClientMacAddr_Object = MibScalar
wsRrmChannelLoadNewRequestClientMacAddr = _WsRrmChannelLoadNewRequestClientMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 16, 3, 1),
    _WsRrmChannelLoadNewRequestClientMacAddr_Type()
)
wsRrmChannelLoadNewRequestClientMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRrmChannelLoadNewRequestClientMacAddr.setStatus("current")


class _WsRrmChannelLoadNewRequestChannel_Type(Unsigned32):
    """Custom type wsRrmChannelLoadNewRequestChannel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
        ValueRangeConstraint(36, 36),
        ValueRangeConstraint(40, 40),
        ValueRangeConstraint(42, 42),
        ValueRangeConstraint(44, 44),
        ValueRangeConstraint(48, 48),
        ValueRangeConstraint(50, 50),
        ValueRangeConstraint(52, 52),
        ValueRangeConstraint(56, 56),
        ValueRangeConstraint(58, 58),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(64, 64),
        ValueRangeConstraint(100, 100),
        ValueRangeConstraint(104, 104),
        ValueRangeConstraint(108, 108),
        ValueRangeConstraint(112, 112),
        ValueRangeConstraint(116, 116),
        ValueRangeConstraint(120, 120),
        ValueRangeConstraint(124, 124),
        ValueRangeConstraint(128, 128),
        ValueRangeConstraint(132, 132),
        ValueRangeConstraint(136, 136),
        ValueRangeConstraint(140, 140),
        ValueRangeConstraint(149, 149),
        ValueRangeConstraint(152, 152),
        ValueRangeConstraint(153, 153),
        ValueRangeConstraint(157, 157),
        ValueRangeConstraint(160, 160),
        ValueRangeConstraint(161, 161),
        ValueRangeConstraint(165, 165),
    )


_WsRrmChannelLoadNewRequestChannel_Type.__name__ = "Unsigned32"
_WsRrmChannelLoadNewRequestChannel_Object = MibScalar
wsRrmChannelLoadNewRequestChannel = _WsRrmChannelLoadNewRequestChannel_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 16, 3, 2),
    _WsRrmChannelLoadNewRequestChannel_Type()
)
wsRrmChannelLoadNewRequestChannel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRrmChannelLoadNewRequestChannel.setStatus("current")


class _WsRrmChannelLoadNewRequestDuration_Type(Unsigned32):
    """Custom type wsRrmChannelLoadNewRequestDuration based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WsRrmChannelLoadNewRequestDuration_Type.__name__ = "Unsigned32"
_WsRrmChannelLoadNewRequestDuration_Object = MibScalar
wsRrmChannelLoadNewRequestDuration = _WsRrmChannelLoadNewRequestDuration_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 16, 3, 3),
    _WsRrmChannelLoadNewRequestDuration_Type()
)
wsRrmChannelLoadNewRequestDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRrmChannelLoadNewRequestDuration.setStatus("current")


class _WsRrmChannelLoadNewRequestSend_Type(Integer32):
    """Custom type wsRrmChannelLoadNewRequestSend based on Integer32"""
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


_WsRrmChannelLoadNewRequestSend_Type.__name__ = "Integer32"
_WsRrmChannelLoadNewRequestSend_Object = MibScalar
wsRrmChannelLoadNewRequestSend = _WsRrmChannelLoadNewRequestSend_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 16, 3, 4),
    _WsRrmChannelLoadNewRequestSend_Type()
)
wsRrmChannelLoadNewRequestSend.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRrmChannelLoadNewRequestSend.setStatus("current")
_Tspec_ObjectIdentity = ObjectIdentity
tspec = _Tspec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17)
)
_TspecGlobal_ObjectIdentity = ObjectIdentity
tspecGlobal = _TspecGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 1)
)
_WsGlobalTspecStatus_ObjectIdentity = ObjectIdentity
wsGlobalTspecStatus = _WsGlobalTspecStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 1, 1)
)
_WsTspecTotalVoiceTrafficStreams_Type = Unsigned32
_WsTspecTotalVoiceTrafficStreams_Object = MibScalar
wsTspecTotalVoiceTrafficStreams = _WsTspecTotalVoiceTrafficStreams_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 1, 1, 1),
    _WsTspecTotalVoiceTrafficStreams_Type()
)
wsTspecTotalVoiceTrafficStreams.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsTspecTotalVoiceTrafficStreams.setStatus("current")
_WsTspecTotalVideoTrafficStreams_Type = Unsigned32
_WsTspecTotalVideoTrafficStreams_Object = MibScalar
wsTspecTotalVideoTrafficStreams = _WsTspecTotalVideoTrafficStreams_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 1, 1, 2),
    _WsTspecTotalVideoTrafficStreams_Type()
)
wsTspecTotalVideoTrafficStreams.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsTspecTotalVideoTrafficStreams.setStatus("current")
_WsTspecTotalTrafficStreamClients_Type = Unsigned32
_WsTspecTotalTrafficStreamClients_Object = MibScalar
wsTspecTotalTrafficStreamClients = _WsTspecTotalTrafficStreamClients_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 1, 1, 3),
    _WsTspecTotalTrafficStreamClients_Type()
)
wsTspecTotalTrafficStreamClients.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsTspecTotalTrafficStreamClients.setStatus("current")
_WsTspecTotalTrafficStreamRoamingClients_Type = Unsigned32
_WsTspecTotalTrafficStreamRoamingClients_Object = MibScalar
wsTspecTotalTrafficStreamRoamingClients = _WsTspecTotalTrafficStreamRoamingClients_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 1, 1, 4),
    _WsTspecTotalTrafficStreamRoamingClients_Type()
)
wsTspecTotalTrafficStreamRoamingClients.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsTspecTotalTrafficStreamRoamingClients.setStatus("current")
_WsGlobalTspecStatisticsTable_Object = MibTable
wsGlobalTspecStatisticsTable = _WsGlobalTspecStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 1, 2)
)
if mibBuilder.loadTexts:
    wsGlobalTspecStatisticsTable.setStatus("current")
_WsGlobalTspecStatisticsEntry_Object = MibTableRow
wsGlobalTspecStatisticsEntry = _WsGlobalTspecStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 1, 2, 1)
)
wsGlobalTspecStatisticsEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsTspecACIndex"),
)
if mibBuilder.loadTexts:
    wsGlobalTspecStatisticsEntry.setStatus("current")
_WsTspecACIndex_Type = TspecSuppAC
_WsTspecACIndex_Object = MibTableColumn
wsTspecACIndex = _WsTspecACIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 1, 2, 1, 1),
    _WsTspecACIndex_Type()
)
wsTspecACIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsTspecACIndex.setStatus("current")
_WsTotalWLANTspecPktsRecvd_Type = Counter64
_WsTotalWLANTspecPktsRecvd_Object = MibTableColumn
wsTotalWLANTspecPktsRecvd = _WsTotalWLANTspecPktsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 1, 2, 1, 2),
    _WsTotalWLANTspecPktsRecvd_Type()
)
wsTotalWLANTspecPktsRecvd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsTotalWLANTspecPktsRecvd.setStatus("current")
_WsTotalWLANTspecPktsTransmitted_Type = Counter64
_WsTotalWLANTspecPktsTransmitted_Object = MibTableColumn
wsTotalWLANTspecPktsTransmitted = _WsTotalWLANTspecPktsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 1, 2, 1, 3),
    _WsTotalWLANTspecPktsTransmitted_Type()
)
wsTotalWLANTspecPktsTransmitted.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsTotalWLANTspecPktsTransmitted.setStatus("current")
_WsTotalWLANTspecBytesRecvd_Type = Counter64
_WsTotalWLANTspecBytesRecvd_Object = MibTableColumn
wsTotalWLANTspecBytesRecvd = _WsTotalWLANTspecBytesRecvd_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 1, 2, 1, 4),
    _WsTotalWLANTspecBytesRecvd_Type()
)
wsTotalWLANTspecBytesRecvd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsTotalWLANTspecBytesRecvd.setStatus("current")
_WsTotalWLANTspecBytesTransmitted_Type = Counter64
_WsTotalWLANTspecBytesTransmitted_Object = MibTableColumn
wsTotalWLANTspecBytesTransmitted = _WsTotalWLANTspecBytesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 1, 2, 1, 5),
    _WsTotalWLANTspecBytesTransmitted_Type()
)
wsTotalWLANTspecBytesTransmitted.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsTotalWLANTspecBytesTransmitted.setStatus("current")
_WsTotalWLANTspecsAccepted_Type = Counter32
_WsTotalWLANTspecsAccepted_Object = MibTableColumn
wsTotalWLANTspecsAccepted = _WsTotalWLANTspecsAccepted_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 1, 2, 1, 6),
    _WsTotalWLANTspecsAccepted_Type()
)
wsTotalWLANTspecsAccepted.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsTotalWLANTspecsAccepted.setStatus("current")
_WsTotalWLANTspecsRejected_Type = Counter32
_WsTotalWLANTspecsRejected_Object = MibTableColumn
wsTotalWLANTspecsRejected = _WsTotalWLANTspecsRejected_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 1, 2, 1, 7),
    _WsTotalWLANTspecsRejected_Type()
)
wsTotalWLANTspecsRejected.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsTotalWLANTspecsRejected.setStatus("current")
_WsTotalWLANRoamingTspecsAccepted_Type = Counter32
_WsTotalWLANRoamingTspecsAccepted_Object = MibTableColumn
wsTotalWLANRoamingTspecsAccepted = _WsTotalWLANRoamingTspecsAccepted_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 1, 2, 1, 8),
    _WsTotalWLANRoamingTspecsAccepted_Type()
)
wsTotalWLANRoamingTspecsAccepted.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsTotalWLANRoamingTspecsAccepted.setStatus("current")
_WsTotalWLANRoamingTspecsRejected_Type = Counter32
_WsTotalWLANRoamingTspecsRejected_Object = MibTableColumn
wsTotalWLANRoamingTspecsRejected = _WsTotalWLANRoamingTspecsRejected_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 1, 2, 1, 9),
    _WsTotalWLANRoamingTspecsRejected_Type()
)
wsTotalWLANRoamingTspecsRejected.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsTotalWLANRoamingTspecsRejected.setStatus("current")
_TspecSwitch_ObjectIdentity = ObjectIdentity
tspecSwitch = _TspecSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 2)
)
_WsSwitchTspecStatusTable_Object = MibTable
wsSwitchTspecStatusTable = _WsSwitchTspecStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 2, 1)
)
if mibBuilder.loadTexts:
    wsSwitchTspecStatusTable.setStatus("current")
_WsSwitchTspecStatusEntry_Object = MibTableRow
wsSwitchTspecStatusEntry = _WsSwitchTspecStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 2, 1, 1)
)
wsSwitchTspecStatusEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsSwitchIPAddress"),
)
if mibBuilder.loadTexts:
    wsSwitchTspecStatusEntry.setStatus("current")
_WsSwitchTspecTotalVoiceTrafficStreams_Type = Unsigned32
_WsSwitchTspecTotalVoiceTrafficStreams_Object = MibTableColumn
wsSwitchTspecTotalVoiceTrafficStreams = _WsSwitchTspecTotalVoiceTrafficStreams_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 2, 1, 1, 1),
    _WsSwitchTspecTotalVoiceTrafficStreams_Type()
)
wsSwitchTspecTotalVoiceTrafficStreams.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsSwitchTspecTotalVoiceTrafficStreams.setStatus("current")
_WsSwitchTspecTotalVideoTrafficStreams_Type = Unsigned32
_WsSwitchTspecTotalVideoTrafficStreams_Object = MibTableColumn
wsSwitchTspecTotalVideoTrafficStreams = _WsSwitchTspecTotalVideoTrafficStreams_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 2, 1, 1, 2),
    _WsSwitchTspecTotalVideoTrafficStreams_Type()
)
wsSwitchTspecTotalVideoTrafficStreams.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsSwitchTspecTotalVideoTrafficStreams.setStatus("current")
_WsSwitchTspecTotalTrafficStreamClients_Type = Unsigned32
_WsSwitchTspecTotalTrafficStreamClients_Object = MibTableColumn
wsSwitchTspecTotalTrafficStreamClients = _WsSwitchTspecTotalTrafficStreamClients_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 2, 1, 1, 3),
    _WsSwitchTspecTotalTrafficStreamClients_Type()
)
wsSwitchTspecTotalTrafficStreamClients.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsSwitchTspecTotalTrafficStreamClients.setStatus("current")
_WsSwitchTspecTotalTrafficStreamRoamingClients_Type = Unsigned32
_WsSwitchTspecTotalTrafficStreamRoamingClients_Object = MibTableColumn
wsSwitchTspecTotalTrafficStreamRoamingClients = _WsSwitchTspecTotalTrafficStreamRoamingClients_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 2, 1, 1, 4),
    _WsSwitchTspecTotalTrafficStreamRoamingClients_Type()
)
wsSwitchTspecTotalTrafficStreamRoamingClients.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsSwitchTspecTotalTrafficStreamRoamingClients.setStatus("current")
_WsSwitchTspecStatisticsTable_Object = MibTable
wsSwitchTspecStatisticsTable = _WsSwitchTspecStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 2, 2)
)
if mibBuilder.loadTexts:
    wsSwitchTspecStatisticsTable.setStatus("current")
_WsSwitchTspecStatisticsEntry_Object = MibTableRow
wsSwitchTspecStatisticsEntry = _WsSwitchTspecStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 2, 2, 1)
)
wsSwitchTspecStatisticsEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsSwitchIPAddress"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsTspecACIndex"),
)
if mibBuilder.loadTexts:
    wsSwitchTspecStatisticsEntry.setStatus("current")
_WsSwitchWLANTspecPktsRecvd_Type = Counter64
_WsSwitchWLANTspecPktsRecvd_Object = MibTableColumn
wsSwitchWLANTspecPktsRecvd = _WsSwitchWLANTspecPktsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 2, 2, 1, 1),
    _WsSwitchWLANTspecPktsRecvd_Type()
)
wsSwitchWLANTspecPktsRecvd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsSwitchWLANTspecPktsRecvd.setStatus("current")
_WsSwitchWLANTspecPktsTransmitted_Type = Counter64
_WsSwitchWLANTspecPktsTransmitted_Object = MibTableColumn
wsSwitchWLANTspecPktsTransmitted = _WsSwitchWLANTspecPktsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 2, 2, 1, 2),
    _WsSwitchWLANTspecPktsTransmitted_Type()
)
wsSwitchWLANTspecPktsTransmitted.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsSwitchWLANTspecPktsTransmitted.setStatus("current")
_WsSwitchWLANTspecBytesRecvd_Type = Counter64
_WsSwitchWLANTspecBytesRecvd_Object = MibTableColumn
wsSwitchWLANTspecBytesRecvd = _WsSwitchWLANTspecBytesRecvd_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 2, 2, 1, 3),
    _WsSwitchWLANTspecBytesRecvd_Type()
)
wsSwitchWLANTspecBytesRecvd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsSwitchWLANTspecBytesRecvd.setStatus("current")
_WsSwitchWLANTspecBytesTransmitted_Type = Counter64
_WsSwitchWLANTspecBytesTransmitted_Object = MibTableColumn
wsSwitchWLANTspecBytesTransmitted = _WsSwitchWLANTspecBytesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 2, 2, 1, 4),
    _WsSwitchWLANTspecBytesTransmitted_Type()
)
wsSwitchWLANTspecBytesTransmitted.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsSwitchWLANTspecBytesTransmitted.setStatus("current")
_WsSwitchWLANTspecsAccepted_Type = Counter32
_WsSwitchWLANTspecsAccepted_Object = MibTableColumn
wsSwitchWLANTspecsAccepted = _WsSwitchWLANTspecsAccepted_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 2, 2, 1, 5),
    _WsSwitchWLANTspecsAccepted_Type()
)
wsSwitchWLANTspecsAccepted.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsSwitchWLANTspecsAccepted.setStatus("current")
_WsSwitchWLANTspecsRejected_Type = Counter32
_WsSwitchWLANTspecsRejected_Object = MibTableColumn
wsSwitchWLANTspecsRejected = _WsSwitchWLANTspecsRejected_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 2, 2, 1, 6),
    _WsSwitchWLANTspecsRejected_Type()
)
wsSwitchWLANTspecsRejected.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsSwitchWLANTspecsRejected.setStatus("current")
_WsSwitchWLANRoamingTspecsAccepted_Type = Counter32
_WsSwitchWLANRoamingTspecsAccepted_Object = MibTableColumn
wsSwitchWLANRoamingTspecsAccepted = _WsSwitchWLANRoamingTspecsAccepted_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 2, 2, 1, 7),
    _WsSwitchWLANRoamingTspecsAccepted_Type()
)
wsSwitchWLANRoamingTspecsAccepted.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsSwitchWLANRoamingTspecsAccepted.setStatus("current")
_WsSwitchWLANRoamingTspecsRejected_Type = Counter32
_WsSwitchWLANRoamingTspecsRejected_Object = MibTableColumn
wsSwitchWLANRoamingTspecsRejected = _WsSwitchWLANRoamingTspecsRejected_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 2, 2, 1, 8),
    _WsSwitchWLANRoamingTspecsRejected_Type()
)
wsSwitchWLANRoamingTspecsRejected.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsSwitchWLANRoamingTspecsRejected.setStatus("current")
_TspecManagedAP_ObjectIdentity = ObjectIdentity
tspecManagedAP = _TspecManagedAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 3)
)
_WsManagedAPTspecStatusTable_Object = MibTable
wsManagedAPTspecStatusTable = _WsManagedAPTspecStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 3, 1)
)
if mibBuilder.loadTexts:
    wsManagedAPTspecStatusTable.setStatus("current")
_WsManagedAPTspecStatusEntry_Object = MibTableRow
wsManagedAPTspecStatusEntry = _WsManagedAPTspecStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 3, 1, 1)
)
wsManagedAPTspecStatusEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsManagedAPMacAddress"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsTspecACIndex"),
)
if mibBuilder.loadTexts:
    wsManagedAPTspecStatusEntry.setStatus("current")
_WsManagedAPTspecNumActiveTrafficStreams_Type = Unsigned32
_WsManagedAPTspecNumActiveTrafficStreams_Object = MibTableColumn
wsManagedAPTspecNumActiveTrafficStreams = _WsManagedAPTspecNumActiveTrafficStreams_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 3, 1, 1, 1),
    _WsManagedAPTspecNumActiveTrafficStreams_Type()
)
wsManagedAPTspecNumActiveTrafficStreams.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsManagedAPTspecNumActiveTrafficStreams.setStatus("current")
_WsManagedAPTspecNumTrafficStreamClients_Type = Unsigned32
_WsManagedAPTspecNumTrafficStreamClients_Object = MibTableColumn
wsManagedAPTspecNumTrafficStreamClients = _WsManagedAPTspecNumTrafficStreamClients_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 3, 1, 1, 2),
    _WsManagedAPTspecNumTrafficStreamClients_Type()
)
wsManagedAPTspecNumTrafficStreamClients.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsManagedAPTspecNumTrafficStreamClients.setStatus("current")
_WsManagedAPTspecNumTrafficStreamRoamingClients_Type = Unsigned32
_WsManagedAPTspecNumTrafficStreamRoamingClients_Object = MibTableColumn
wsManagedAPTspecNumTrafficStreamRoamingClients = _WsManagedAPTspecNumTrafficStreamRoamingClients_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 3, 1, 1, 3),
    _WsManagedAPTspecNumTrafficStreamRoamingClients_Type()
)
wsManagedAPTspecNumTrafficStreamRoamingClients.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsManagedAPTspecNumTrafficStreamRoamingClients.setStatus("current")
_WsManagedAPTspecStatisticsTable_Object = MibTable
wsManagedAPTspecStatisticsTable = _WsManagedAPTspecStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 3, 2)
)
if mibBuilder.loadTexts:
    wsManagedAPTspecStatisticsTable.setStatus("current")
_WsManagedAPTspecStatisticsEntry_Object = MibTableRow
wsManagedAPTspecStatisticsEntry = _WsManagedAPTspecStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 3, 2, 1)
)
if mibBuilder.loadTexts:
    wsManagedAPTspecStatisticsEntry.setStatus("current")
_WsManagedAPTspecPktsRecvd_Type = Counter64
_WsManagedAPTspecPktsRecvd_Object = MibTableColumn
wsManagedAPTspecPktsRecvd = _WsManagedAPTspecPktsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 3, 2, 1, 1),
    _WsManagedAPTspecPktsRecvd_Type()
)
wsManagedAPTspecPktsRecvd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsManagedAPTspecPktsRecvd.setStatus("current")
_WsManagedAPTspecPktsTransmitted_Type = Counter64
_WsManagedAPTspecPktsTransmitted_Object = MibTableColumn
wsManagedAPTspecPktsTransmitted = _WsManagedAPTspecPktsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 3, 2, 1, 2),
    _WsManagedAPTspecPktsTransmitted_Type()
)
wsManagedAPTspecPktsTransmitted.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsManagedAPTspecPktsTransmitted.setStatus("current")
_WsManagedAPTspecBytesRecvd_Type = Counter64
_WsManagedAPTspecBytesRecvd_Object = MibTableColumn
wsManagedAPTspecBytesRecvd = _WsManagedAPTspecBytesRecvd_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 3, 2, 1, 3),
    _WsManagedAPTspecBytesRecvd_Type()
)
wsManagedAPTspecBytesRecvd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsManagedAPTspecBytesRecvd.setStatus("current")
_WsManagedAPTspecBytesTransmitted_Type = Counter64
_WsManagedAPTspecBytesTransmitted_Object = MibTableColumn
wsManagedAPTspecBytesTransmitted = _WsManagedAPTspecBytesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 3, 2, 1, 4),
    _WsManagedAPTspecBytesTransmitted_Type()
)
wsManagedAPTspecBytesTransmitted.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsManagedAPTspecBytesTransmitted.setStatus("current")
_WsManagedAPTspecsAccepted_Type = Counter32
_WsManagedAPTspecsAccepted_Object = MibTableColumn
wsManagedAPTspecsAccepted = _WsManagedAPTspecsAccepted_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 3, 2, 1, 5),
    _WsManagedAPTspecsAccepted_Type()
)
wsManagedAPTspecsAccepted.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsManagedAPTspecsAccepted.setStatus("current")
_WsManagedAPTspecsRejected_Type = Counter32
_WsManagedAPTspecsRejected_Object = MibTableColumn
wsManagedAPTspecsRejected = _WsManagedAPTspecsRejected_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 3, 2, 1, 6),
    _WsManagedAPTspecsRejected_Type()
)
wsManagedAPTspecsRejected.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsManagedAPTspecsRejected.setStatus("current")
_WsManagedAPRoamingTspecsAccepted_Type = Counter32
_WsManagedAPRoamingTspecsAccepted_Object = MibTableColumn
wsManagedAPRoamingTspecsAccepted = _WsManagedAPRoamingTspecsAccepted_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 3, 2, 1, 7),
    _WsManagedAPRoamingTspecsAccepted_Type()
)
wsManagedAPRoamingTspecsAccepted.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsManagedAPRoamingTspecsAccepted.setStatus("current")
_WsManagedAPRoamingTspecsRejected_Type = Counter32
_WsManagedAPRoamingTspecsRejected_Object = MibTableColumn
wsManagedAPRoamingTspecsRejected = _WsManagedAPRoamingTspecsRejected_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 3, 2, 1, 8),
    _WsManagedAPRoamingTspecsRejected_Type()
)
wsManagedAPRoamingTspecsRejected.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsManagedAPRoamingTspecsRejected.setStatus("current")
_WsManagedAPRadioTspecStatusTable_Object = MibTable
wsManagedAPRadioTspecStatusTable = _WsManagedAPRadioTspecStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 3, 3)
)
if mibBuilder.loadTexts:
    wsManagedAPRadioTspecStatusTable.setStatus("current")
_WsManagedAPRadioTspecStatusEntry_Object = MibTableRow
wsManagedAPRadioTspecStatusEntry = _WsManagedAPRadioTspecStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 3, 3, 1)
)
wsManagedAPRadioTspecStatusEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsManagedAPMacAddress"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsManagedAPRadioInterface"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsTspecACIndex"),
)
if mibBuilder.loadTexts:
    wsManagedAPRadioTspecStatusEntry.setStatus("current")


class _WsManagedAPRadioTspecOperStatus_Type(Integer32):
    """Custom type wsManagedAPRadioTspecOperStatus based on Integer32"""
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


_WsManagedAPRadioTspecOperStatus_Type.__name__ = "Integer32"
_WsManagedAPRadioTspecOperStatus_Object = MibTableColumn
wsManagedAPRadioTspecOperStatus = _WsManagedAPRadioTspecOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 3, 3, 1, 1),
    _WsManagedAPRadioTspecOperStatus_Type()
)
wsManagedAPRadioTspecOperStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsManagedAPRadioTspecOperStatus.setStatus("current")
_WsManagedAPRadioTspecNumActiveTrafficStreams_Type = Unsigned32
_WsManagedAPRadioTspecNumActiveTrafficStreams_Object = MibTableColumn
wsManagedAPRadioTspecNumActiveTrafficStreams = _WsManagedAPRadioTspecNumActiveTrafficStreams_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 3, 3, 1, 2),
    _WsManagedAPRadioTspecNumActiveTrafficStreams_Type()
)
wsManagedAPRadioTspecNumActiveTrafficStreams.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsManagedAPRadioTspecNumActiveTrafficStreams.setStatus("current")
_WsManagedAPRadioTspecNumTrafficStreamClients_Type = Unsigned32
_WsManagedAPRadioTspecNumTrafficStreamClients_Object = MibTableColumn
wsManagedAPRadioTspecNumTrafficStreamClients = _WsManagedAPRadioTspecNumTrafficStreamClients_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 3, 3, 1, 3),
    _WsManagedAPRadioTspecNumTrafficStreamClients_Type()
)
wsManagedAPRadioTspecNumTrafficStreamClients.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsManagedAPRadioTspecNumTrafficStreamClients.setStatus("current")
_WsManagedAPRadioTspecNumTrafficStreamRoamingClients_Type = Unsigned32
_WsManagedAPRadioTspecNumTrafficStreamRoamingClients_Object = MibTableColumn
wsManagedAPRadioTspecNumTrafficStreamRoamingClients = _WsManagedAPRadioTspecNumTrafficStreamRoamingClients_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 3, 3, 1, 4),
    _WsManagedAPRadioTspecNumTrafficStreamRoamingClients_Type()
)
wsManagedAPRadioTspecNumTrafficStreamRoamingClients.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsManagedAPRadioTspecNumTrafficStreamRoamingClients.setStatus("current")
_WsManagedAPRadioTspecMediumTimeAdmitted_Type = Unsigned32
_WsManagedAPRadioTspecMediumTimeAdmitted_Object = MibTableColumn
wsManagedAPRadioTspecMediumTimeAdmitted = _WsManagedAPRadioTspecMediumTimeAdmitted_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 3, 3, 1, 5),
    _WsManagedAPRadioTspecMediumTimeAdmitted_Type()
)
wsManagedAPRadioTspecMediumTimeAdmitted.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsManagedAPRadioTspecMediumTimeAdmitted.setStatus("current")
_WsManagedAPRadioTspecMediumTimeUnallocated_Type = Unsigned32
_WsManagedAPRadioTspecMediumTimeUnallocated_Object = MibTableColumn
wsManagedAPRadioTspecMediumTimeUnallocated = _WsManagedAPRadioTspecMediumTimeUnallocated_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 3, 3, 1, 6),
    _WsManagedAPRadioTspecMediumTimeUnallocated_Type()
)
wsManagedAPRadioTspecMediumTimeUnallocated.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsManagedAPRadioTspecMediumTimeUnallocated.setStatus("current")
_WsManagedAPRadioTspecMediumTimeRoamingUnallocated_Type = Unsigned32
_WsManagedAPRadioTspecMediumTimeRoamingUnallocated_Object = MibTableColumn
wsManagedAPRadioTspecMediumTimeRoamingUnallocated = _WsManagedAPRadioTspecMediumTimeRoamingUnallocated_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 3, 3, 1, 7),
    _WsManagedAPRadioTspecMediumTimeRoamingUnallocated_Type()
)
wsManagedAPRadioTspecMediumTimeRoamingUnallocated.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsManagedAPRadioTspecMediumTimeRoamingUnallocated.setStatus("current")
_WsManagedAPRadioTspecStatisticsTable_Object = MibTable
wsManagedAPRadioTspecStatisticsTable = _WsManagedAPRadioTspecStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 3, 4)
)
if mibBuilder.loadTexts:
    wsManagedAPRadioTspecStatisticsTable.setStatus("current")
_WsManagedAPRadioTspecStatisticsEntry_Object = MibTableRow
wsManagedAPRadioTspecStatisticsEntry = _WsManagedAPRadioTspecStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 3, 4, 1)
)
if mibBuilder.loadTexts:
    wsManagedAPRadioTspecStatisticsEntry.setStatus("current")
_WsManagedAPRadioTspecPktsRecvd_Type = Counter64
_WsManagedAPRadioTspecPktsRecvd_Object = MibTableColumn
wsManagedAPRadioTspecPktsRecvd = _WsManagedAPRadioTspecPktsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 3, 4, 1, 1),
    _WsManagedAPRadioTspecPktsRecvd_Type()
)
wsManagedAPRadioTspecPktsRecvd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsManagedAPRadioTspecPktsRecvd.setStatus("current")
_WsManagedAPRadioTspecPktsTransmitted_Type = Counter64
_WsManagedAPRadioTspecPktsTransmitted_Object = MibTableColumn
wsManagedAPRadioTspecPktsTransmitted = _WsManagedAPRadioTspecPktsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 3, 4, 1, 2),
    _WsManagedAPRadioTspecPktsTransmitted_Type()
)
wsManagedAPRadioTspecPktsTransmitted.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsManagedAPRadioTspecPktsTransmitted.setStatus("current")
_WsManagedAPRadioTspecBytesRecvd_Type = Counter64
_WsManagedAPRadioTspecBytesRecvd_Object = MibTableColumn
wsManagedAPRadioTspecBytesRecvd = _WsManagedAPRadioTspecBytesRecvd_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 3, 4, 1, 3),
    _WsManagedAPRadioTspecBytesRecvd_Type()
)
wsManagedAPRadioTspecBytesRecvd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsManagedAPRadioTspecBytesRecvd.setStatus("current")
_WsManagedAPRadioTspecBytesTransmitted_Type = Counter64
_WsManagedAPRadioTspecBytesTransmitted_Object = MibTableColumn
wsManagedAPRadioTspecBytesTransmitted = _WsManagedAPRadioTspecBytesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 3, 4, 1, 4),
    _WsManagedAPRadioTspecBytesTransmitted_Type()
)
wsManagedAPRadioTspecBytesTransmitted.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsManagedAPRadioTspecBytesTransmitted.setStatus("current")
_WsManagedAPVAPTspecStatusTable_Object = MibTable
wsManagedAPVAPTspecStatusTable = _WsManagedAPVAPTspecStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 3, 5)
)
if mibBuilder.loadTexts:
    wsManagedAPVAPTspecStatusTable.setStatus("current")
_WsManagedAPVAPTspecStatusEntry_Object = MibTableRow
wsManagedAPVAPTspecStatusEntry = _WsManagedAPVAPTspecStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 3, 5, 1)
)
wsManagedAPVAPTspecStatusEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsManagedAPMacAddress"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsManagedAPRadioInterface"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsManagedVAPId"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsTspecACIndex"),
)
if mibBuilder.loadTexts:
    wsManagedAPVAPTspecStatusEntry.setStatus("current")


class _WsManagedAPVAPTspecOperStatus_Type(Integer32):
    """Custom type wsManagedAPVAPTspecOperStatus based on Integer32"""
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


_WsManagedAPVAPTspecOperStatus_Type.__name__ = "Integer32"
_WsManagedAPVAPTspecOperStatus_Object = MibTableColumn
wsManagedAPVAPTspecOperStatus = _WsManagedAPVAPTspecOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 3, 5, 1, 1),
    _WsManagedAPVAPTspecOperStatus_Type()
)
wsManagedAPVAPTspecOperStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsManagedAPVAPTspecOperStatus.setStatus("current")
_WsManagedAPVAPTspecNumActiveTrafficStreams_Type = Unsigned32
_WsManagedAPVAPTspecNumActiveTrafficStreams_Object = MibTableColumn
wsManagedAPVAPTspecNumActiveTrafficStreams = _WsManagedAPVAPTspecNumActiveTrafficStreams_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 3, 5, 1, 2),
    _WsManagedAPVAPTspecNumActiveTrafficStreams_Type()
)
wsManagedAPVAPTspecNumActiveTrafficStreams.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsManagedAPVAPTspecNumActiveTrafficStreams.setStatus("current")
_WsManagedAPVAPTspecNumTrafficStreamClients_Type = Unsigned32
_WsManagedAPVAPTspecNumTrafficStreamClients_Object = MibTableColumn
wsManagedAPVAPTspecNumTrafficStreamClients = _WsManagedAPVAPTspecNumTrafficStreamClients_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 3, 5, 1, 3),
    _WsManagedAPVAPTspecNumTrafficStreamClients_Type()
)
wsManagedAPVAPTspecNumTrafficStreamClients.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsManagedAPVAPTspecNumTrafficStreamClients.setStatus("current")
_WsManagedAPVAPTspecNumTrafficStreamRoamingClients_Type = Unsigned32
_WsManagedAPVAPTspecNumTrafficStreamRoamingClients_Object = MibTableColumn
wsManagedAPVAPTspecNumTrafficStreamRoamingClients = _WsManagedAPVAPTspecNumTrafficStreamRoamingClients_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 3, 5, 1, 4),
    _WsManagedAPVAPTspecNumTrafficStreamRoamingClients_Type()
)
wsManagedAPVAPTspecNumTrafficStreamRoamingClients.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsManagedAPVAPTspecNumTrafficStreamRoamingClients.setStatus("current")
_WsManagedAPVAPTspecMediumTimeAdmitted_Type = Unsigned32
_WsManagedAPVAPTspecMediumTimeAdmitted_Object = MibTableColumn
wsManagedAPVAPTspecMediumTimeAdmitted = _WsManagedAPVAPTspecMediumTimeAdmitted_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 3, 5, 1, 5),
    _WsManagedAPVAPTspecMediumTimeAdmitted_Type()
)
wsManagedAPVAPTspecMediumTimeAdmitted.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsManagedAPVAPTspecMediumTimeAdmitted.setStatus("current")
_WsManagedAPVAPTspecMediumTimeUnallocated_Type = Unsigned32
_WsManagedAPVAPTspecMediumTimeUnallocated_Object = MibTableColumn
wsManagedAPVAPTspecMediumTimeUnallocated = _WsManagedAPVAPTspecMediumTimeUnallocated_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 3, 5, 1, 6),
    _WsManagedAPVAPTspecMediumTimeUnallocated_Type()
)
wsManagedAPVAPTspecMediumTimeUnallocated.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsManagedAPVAPTspecMediumTimeUnallocated.setStatus("current")
_WsManagedAPVAPTspecMediumTimeRoamingUnallocated_Type = Unsigned32
_WsManagedAPVAPTspecMediumTimeRoamingUnallocated_Object = MibTableColumn
wsManagedAPVAPTspecMediumTimeRoamingUnallocated = _WsManagedAPVAPTspecMediumTimeRoamingUnallocated_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 3, 5, 1, 7),
    _WsManagedAPVAPTspecMediumTimeRoamingUnallocated_Type()
)
wsManagedAPVAPTspecMediumTimeRoamingUnallocated.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsManagedAPVAPTspecMediumTimeRoamingUnallocated.setStatus("current")
_WsManagedAPVAPTspecStatisticsTable_Object = MibTable
wsManagedAPVAPTspecStatisticsTable = _WsManagedAPVAPTspecStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 3, 6)
)
if mibBuilder.loadTexts:
    wsManagedAPVAPTspecStatisticsTable.setStatus("current")
_WsManagedAPVAPTspecStatisticsEntry_Object = MibTableRow
wsManagedAPVAPTspecStatisticsEntry = _WsManagedAPVAPTspecStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 3, 6, 1)
)
if mibBuilder.loadTexts:
    wsManagedAPVAPTspecStatisticsEntry.setStatus("current")
_WsManagedAPVAPTspecPktsRecvd_Type = Counter64
_WsManagedAPVAPTspecPktsRecvd_Object = MibTableColumn
wsManagedAPVAPTspecPktsRecvd = _WsManagedAPVAPTspecPktsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 3, 6, 1, 1),
    _WsManagedAPVAPTspecPktsRecvd_Type()
)
wsManagedAPVAPTspecPktsRecvd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsManagedAPVAPTspecPktsRecvd.setStatus("current")
_WsManagedAPVAPTspecPktsTransmitted_Type = Counter64
_WsManagedAPVAPTspecPktsTransmitted_Object = MibTableColumn
wsManagedAPVAPTspecPktsTransmitted = _WsManagedAPVAPTspecPktsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 3, 6, 1, 2),
    _WsManagedAPVAPTspecPktsTransmitted_Type()
)
wsManagedAPVAPTspecPktsTransmitted.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsManagedAPVAPTspecPktsTransmitted.setStatus("current")
_WsManagedAPVAPTspecBytesRecvd_Type = Counter64
_WsManagedAPVAPTspecBytesRecvd_Object = MibTableColumn
wsManagedAPVAPTspecBytesRecvd = _WsManagedAPVAPTspecBytesRecvd_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 3, 6, 1, 3),
    _WsManagedAPVAPTspecBytesRecvd_Type()
)
wsManagedAPVAPTspecBytesRecvd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsManagedAPVAPTspecBytesRecvd.setStatus("current")
_WsManagedAPVAPTspecBytesTransmitted_Type = Counter64
_WsManagedAPVAPTspecBytesTransmitted_Object = MibTableColumn
wsManagedAPVAPTspecBytesTransmitted = _WsManagedAPVAPTspecBytesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 3, 6, 1, 4),
    _WsManagedAPVAPTspecBytesTransmitted_Type()
)
wsManagedAPVAPTspecBytesTransmitted.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsManagedAPVAPTspecBytesTransmitted.setStatus("current")
_TspecClient_ObjectIdentity = ObjectIdentity
tspecClient = _TspecClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 4)
)
_WsAssociatedClientTsStatusTable_Object = MibTable
wsAssociatedClientTsStatusTable = _WsAssociatedClientTsStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 4, 1)
)
if mibBuilder.loadTexts:
    wsAssociatedClientTsStatusTable.setStatus("current")
_WsAssociatedClientTsStatusEntry_Object = MibTableRow
wsAssociatedClientTsStatusEntry = _WsAssociatedClientTsStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 4, 1, 1)
)
wsAssociatedClientTsStatusEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsAssociatedClientMacAddress"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsAssociatedClientTsTid"),
)
if mibBuilder.loadTexts:
    wsAssociatedClientTsStatusEntry.setStatus("current")


class _WsAssociatedClientTsTid_Type(Unsigned32):
    """Custom type wsAssociatedClientTsTid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WsAssociatedClientTsTid_Type.__name__ = "Unsigned32"
_WsAssociatedClientTsTid_Object = MibTableColumn
wsAssociatedClientTsTid = _WsAssociatedClientTsTid_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 4, 1, 1, 1),
    _WsAssociatedClientTsTid_Type()
)
wsAssociatedClientTsTid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAssociatedClientTsTid.setStatus("current")
_WsAssociatedClientTsAccessCategory_Type = TspecSuppAC
_WsAssociatedClientTsAccessCategory_Object = MibTableColumn
wsAssociatedClientTsAccessCategory = _WsAssociatedClientTsAccessCategory_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 4, 1, 1, 2),
    _WsAssociatedClientTsAccessCategory_Type()
)
wsAssociatedClientTsAccessCategory.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAssociatedClientTsAccessCategory.setStatus("current")


class _WsAssociatedClientTsDirection_Type(Integer32):
    """Custom type wsAssociatedClientTsDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("uplink", 1),
          ("downlink", 2),
          ("bidirectional", 3))
    )


_WsAssociatedClientTsDirection_Type.__name__ = "Integer32"
_WsAssociatedClientTsDirection_Object = MibTableColumn
wsAssociatedClientTsDirection = _WsAssociatedClientTsDirection_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 4, 1, 1, 3),
    _WsAssociatedClientTsDirection_Type()
)
wsAssociatedClientTsDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAssociatedClientTsDirection.setStatus("current")
_WsAssociatedClientTsUserPriority_Type = Unsigned32
_WsAssociatedClientTsUserPriority_Object = MibTableColumn
wsAssociatedClientTsUserPriority = _WsAssociatedClientTsUserPriority_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 4, 1, 1, 4),
    _WsAssociatedClientTsUserPriority_Type()
)
wsAssociatedClientTsUserPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAssociatedClientTsUserPriority.setStatus("current")
_WsAssociatedClientTsMediumTime_Type = Unsigned32
_WsAssociatedClientTsMediumTime_Object = MibTableColumn
wsAssociatedClientTsMediumTime = _WsAssociatedClientTsMediumTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 4, 1, 1, 5),
    _WsAssociatedClientTsMediumTime_Type()
)
wsAssociatedClientTsMediumTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAssociatedClientTsMediumTime.setStatus("current")
_WsAssociatedClientTsExcessUsageEvents_Type = Unsigned32
_WsAssociatedClientTsExcessUsageEvents_Object = MibTableColumn
wsAssociatedClientTsExcessUsageEvents = _WsAssociatedClientTsExcessUsageEvents_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 4, 1, 1, 6),
    _WsAssociatedClientTsExcessUsageEvents_Type()
)
wsAssociatedClientTsExcessUsageEvents.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAssociatedClientTsExcessUsageEvents.setStatus("current")


class _WsAssociatedClientTsRoamingClientIndicator_Type(Integer32):
    """Custom type wsAssociatedClientTsRoamingClientIndicator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_WsAssociatedClientTsRoamingClientIndicator_Type.__name__ = "Integer32"
_WsAssociatedClientTsRoamingClientIndicator_Object = MibTableColumn
wsAssociatedClientTsRoamingClientIndicator = _WsAssociatedClientTsRoamingClientIndicator_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 4, 1, 1, 7),
    _WsAssociatedClientTsRoamingClientIndicator_Type()
)
wsAssociatedClientTsRoamingClientIndicator.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAssociatedClientTsRoamingClientIndicator.setStatus("current")
_WsAssociatedClientTsStatisticsTable_Object = MibTable
wsAssociatedClientTsStatisticsTable = _WsAssociatedClientTsStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 4, 2)
)
if mibBuilder.loadTexts:
    wsAssociatedClientTsStatisticsTable.setStatus("current")
_WsAssociatedClientTsStatisticsEntry_Object = MibTableRow
wsAssociatedClientTsStatisticsEntry = _WsAssociatedClientTsStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 4, 2, 1)
)
if mibBuilder.loadTexts:
    wsAssociatedClientTsStatisticsEntry.setStatus("current")
_WsAssociatedClientTsPktsRecvd_Type = Counter64
_WsAssociatedClientTsPktsRecvd_Object = MibTableColumn
wsAssociatedClientTsPktsRecvd = _WsAssociatedClientTsPktsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 4, 2, 1, 1),
    _WsAssociatedClientTsPktsRecvd_Type()
)
wsAssociatedClientTsPktsRecvd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAssociatedClientTsPktsRecvd.setStatus("current")
_WsAssociatedClientTsPktsTransmitted_Type = Counter64
_WsAssociatedClientTsPktsTransmitted_Object = MibTableColumn
wsAssociatedClientTsPktsTransmitted = _WsAssociatedClientTsPktsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 4, 2, 1, 2),
    _WsAssociatedClientTsPktsTransmitted_Type()
)
wsAssociatedClientTsPktsTransmitted.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAssociatedClientTsPktsTransmitted.setStatus("current")
_WsAssociatedClientTsBytesRecvd_Type = Counter64
_WsAssociatedClientTsBytesRecvd_Object = MibTableColumn
wsAssociatedClientTsBytesRecvd = _WsAssociatedClientTsBytesRecvd_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 4, 2, 1, 3),
    _WsAssociatedClientTsBytesRecvd_Type()
)
wsAssociatedClientTsBytesRecvd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAssociatedClientTsBytesRecvd.setStatus("current")
_WsAssociatedClientTsBytesTransmitted_Type = Counter64
_WsAssociatedClientTsBytesTransmitted_Object = MibTableColumn
wsAssociatedClientTsBytesTransmitted = _WsAssociatedClientTsBytesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 17, 4, 2, 1, 4),
    _WsAssociatedClientTsBytesTransmitted_Type()
)
wsAssociatedClientTsBytesTransmitted.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAssociatedClientTsBytesTransmitted.setStatus("current")
_Provisioning_ObjectIdentity = ObjectIdentity
provisioning = _Provisioning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 18)
)
_WsAPProvisioningTable_Object = MibTable
wsAPProvisioningTable = _WsAPProvisioningTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 18, 1)
)
if mibBuilder.loadTexts:
    wsAPProvisioningTable.setStatus("current")
_WsAPProvisioningEntry_Object = MibTableRow
wsAPProvisioningEntry = _WsAPProvisioningEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 18, 1, 1)
)
wsAPProvisioningEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsAPProvMacAddress"),
)
if mibBuilder.loadTexts:
    wsAPProvisioningEntry.setStatus("current")
_WsAPProvMacAddress_Type = MacAddress
_WsAPProvMacAddress_Object = MibTableColumn
wsAPProvMacAddress = _WsAPProvMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 18, 1, 1, 1),
    _WsAPProvMacAddress_Type()
)
wsAPProvMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAPProvMacAddress.setStatus("current")
_WsAPProvIPAddress_Type = IpAddress
_WsAPProvIPAddress_Object = MibTableColumn
wsAPProvIPAddress = _WsAPProvIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 18, 1, 1, 2),
    _WsAPProvIPAddress_Type()
)
wsAPProvIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAPProvIPAddress.setStatus("current")
_WsAPProvPrimarySwitchIP_Type = IpAddress
_WsAPProvPrimarySwitchIP_Object = MibTableColumn
wsAPProvPrimarySwitchIP = _WsAPProvPrimarySwitchIP_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 18, 1, 1, 3),
    _WsAPProvPrimarySwitchIP_Type()
)
wsAPProvPrimarySwitchIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAPProvPrimarySwitchIP.setStatus("current")
_WsAPProvBackupSwitchIP_Type = IpAddress
_WsAPProvBackupSwitchIP_Object = MibTableColumn
wsAPProvBackupSwitchIP = _WsAPProvBackupSwitchIP_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 18, 1, 1, 4),
    _WsAPProvBackupSwitchIP_Type()
)
wsAPProvBackupSwitchIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAPProvBackupSwitchIP.setStatus("current")


class _WsAPProvMutualAuthMode_Type(Integer32):
    """Custom type wsAPProvMutualAuthMode based on Integer32"""
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


_WsAPProvMutualAuthMode_Type.__name__ = "Integer32"
_WsAPProvMutualAuthMode_Object = MibTableColumn
wsAPProvMutualAuthMode = _WsAPProvMutualAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 18, 1, 1, 5),
    _WsAPProvMutualAuthMode_Type()
)
wsAPProvMutualAuthMode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAPProvMutualAuthMode.setStatus("current")


class _WsAPProvUnmanagedAPReprovMode_Type(Integer32):
    """Custom type wsAPProvUnmanagedAPReprovMode based on Integer32"""
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


_WsAPProvUnmanagedAPReprovMode_Type.__name__ = "Integer32"
_WsAPProvUnmanagedAPReprovMode_Object = MibTableColumn
wsAPProvUnmanagedAPReprovMode = _WsAPProvUnmanagedAPReprovMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 18, 1, 1, 6),
    _WsAPProvUnmanagedAPReprovMode_Type()
)
wsAPProvUnmanagedAPReprovMode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAPProvUnmanagedAPReprovMode.setStatus("current")
_WsAPProvAge_Type = TimeTicks
_WsAPProvAge_Object = MibTableColumn
wsAPProvAge = _WsAPProvAge_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 18, 1, 1, 7),
    _WsAPProvAge_Type()
)
wsAPProvAge.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAPProvAge.setStatus("current")
_WsAPProvNewPrimarySwitchIP_Type = IpAddress
_WsAPProvNewPrimarySwitchIP_Object = MibTableColumn
wsAPProvNewPrimarySwitchIP = _WsAPProvNewPrimarySwitchIP_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 18, 1, 1, 8),
    _WsAPProvNewPrimarySwitchIP_Type()
)
wsAPProvNewPrimarySwitchIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAPProvNewPrimarySwitchIP.setStatus("current")
_WsAPProvNewBackupSwitchIP_Type = IpAddress
_WsAPProvNewBackupSwitchIP_Object = MibTableColumn
wsAPProvNewBackupSwitchIP = _WsAPProvNewBackupSwitchIP_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 18, 1, 1, 9),
    _WsAPProvNewBackupSwitchIP_Type()
)
wsAPProvNewBackupSwitchIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAPProvNewBackupSwitchIP.setStatus("current")


class _WsAPProvNewProfileId_Type(Integer32):
    """Custom type wsAPProvNewProfileId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_WsAPProvNewProfileId_Type.__name__ = "Integer32"
_WsAPProvNewProfileId_Object = MibTableColumn
wsAPProvNewProfileId = _WsAPProvNewProfileId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 18, 1, 1, 10),
    _WsAPProvNewProfileId_Type()
)
wsAPProvNewProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAPProvNewProfileId.setStatus("current")


class _WsAPProvCommand_Type(Integer32):
    """Custom type wsAPProvCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("initiate", 1))
    )


_WsAPProvCommand_Type.__name__ = "Integer32"
_WsAPProvCommand_Object = MibTableColumn
wsAPProvCommand = _WsAPProvCommand_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 18, 1, 1, 11),
    _WsAPProvCommand_Type()
)
wsAPProvCommand.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAPProvCommand.setStatus("current")


class _WsAPProvStatus_Type(Integer32):
    """Custom type wsAPProvStatus based on Integer32"""
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
        *(("not-started", 1),
          ("requested", 2),
          ("success", 3),
          ("in-progress", 4),
          ("provisioning-rejected", 5),
          ("timed-out", 6))
    )


_WsAPProvStatus_Type.__name__ = "Integer32"
_WsAPProvStatus_Object = MibTableColumn
wsAPProvStatus = _WsAPProvStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 18, 1, 1, 12),
    _WsAPProvStatus_Type()
)
wsAPProvStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAPProvStatus.setStatus("current")


class _WsAPProvCertProfileTxStatus_Type(Integer32):
    """Custom type wsAPProvCertProfileTxStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not-started", 1),
          ("success", 2),
          ("failed", 3))
    )


_WsAPProvCertProfileTxStatus_Type.__name__ = "Integer32"
_WsAPProvCertProfileTxStatus_Object = MibTableColumn
wsAPProvCertProfileTxStatus = _WsAPProvCertProfileTxStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 18, 1, 1, 13),
    _WsAPProvCertProfileTxStatus_Type()
)
wsAPProvCertProfileTxStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAPProvCertProfileTxStatus.setStatus("current")


class _WsAPProvEntryPurge_Type(Integer32):
    """Custom type wsAPProvEntryPurge based on Integer32"""
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


_WsAPProvEntryPurge_Type.__name__ = "Integer32"
_WsAPProvEntryPurge_Object = MibTableColumn
wsAPProvEntryPurge = _WsAPProvEntryPurge_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 18, 1, 1, 14),
    _WsAPProvEntryPurge_Type()
)
wsAPProvEntryPurge.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAPProvEntryPurge.setStatus("current")


class _WsAPProvisioningInitiateAll_Type(Integer32):
    """Custom type wsAPProvisioningInitiateAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("initiate", 1))
    )


_WsAPProvisioningInitiateAll_Type.__name__ = "Integer32"
_WsAPProvisioningInitiateAll_Object = MibScalar
wsAPProvisioningInitiateAll = _WsAPProvisioningInitiateAll_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 18, 2),
    _WsAPProvisioningInitiateAll_Type()
)
wsAPProvisioningInitiateAll.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAPProvisioningInitiateAll.setStatus("current")


class _WsAPProvisioningDeleteAll_Type(Integer32):
    """Custom type wsAPProvisioningDeleteAll based on Integer32"""
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


_WsAPProvisioningDeleteAll_Type.__name__ = "Integer32"
_WsAPProvisioningDeleteAll_Object = MibScalar
wsAPProvisioningDeleteAll = _WsAPProvisioningDeleteAll_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 18, 3),
    _WsAPProvisioningDeleteAll_Type()
)
wsAPProvisioningDeleteAll.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAPProvisioningDeleteAll.setStatus("current")


class _WsNetworkExchangeCertificates_Type(Integer32):
    """Custom type wsNetworkExchangeCertificates based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("initiate", 1))
    )


_WsNetworkExchangeCertificates_Type.__name__ = "Integer32"
_WsNetworkExchangeCertificates_Object = MibScalar
wsNetworkExchangeCertificates = _WsNetworkExchangeCertificates_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 18, 4),
    _WsNetworkExchangeCertificates_Type()
)
wsNetworkExchangeCertificates.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsNetworkExchangeCertificates.setStatus("current")
_WsSwitchProvIPAddress_Type = IpAddress
_WsSwitchProvIPAddress_Object = MibScalar
wsSwitchProvIPAddress = _WsSwitchProvIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 18, 5),
    _WsSwitchProvIPAddress_Type()
)
wsSwitchProvIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsSwitchProvIPAddress.setStatus("current")


class _WsSwitchProvStatus_Type(Integer32):
    """Custom type wsSwitchProvStatus based on Integer32"""
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
        *(("not-started", 1),
          ("requested", 2),
          ("in-progress", 3),
          ("provisioning-failed", 4),
          ("connection-failed", 5),
          ("success", 6))
    )


_WsSwitchProvStatus_Type.__name__ = "Integer32"
_WsSwitchProvStatus_Object = MibScalar
wsSwitchProvStatus = _WsSwitchProvStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 18, 6),
    _WsSwitchProvStatus_Type()
)
wsSwitchProvStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsSwitchProvStatus.setStatus("current")
_WsSwitchCertReqTarget_Type = IpAddress
_WsSwitchCertReqTarget_Object = MibScalar
wsSwitchCertReqTarget = _WsSwitchCertReqTarget_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 18, 7),
    _WsSwitchCertReqTarget_Type()
)
wsSwitchCertReqTarget.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsSwitchCertReqTarget.setStatus("current")


class _WsSwitchCertReqStatus_Type(Integer32):
    """Custom type wsSwitchCertReqStatus based on Integer32"""
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
        *(("not-started", 1),
          ("requested", 2),
          ("in-progress", 3),
          ("invalid-ip", 4),
          ("timed-out", 5),
          ("success", 6))
    )


_WsSwitchCertReqStatus_Type.__name__ = "Integer32"
_WsSwitchCertReqStatus_Object = MibScalar
wsSwitchCertReqStatus = _WsSwitchCertReqStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 18, 8),
    _WsSwitchCertReqStatus_Type()
)
wsSwitchCertReqStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsSwitchCertReqStatus.setStatus("current")


class _WsSwitchProvisioningCommand_Type(Integer32):
    """Custom type wsSwitchProvisioningCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("initiate", 1))
    )


_WsSwitchProvisioningCommand_Type.__name__ = "Integer32"
_WsSwitchProvisioningCommand_Object = MibScalar
wsSwitchProvisioningCommand = _WsSwitchProvisioningCommand_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 18, 9),
    _WsSwitchProvisioningCommand_Type()
)
wsSwitchProvisioningCommand.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsSwitchProvisioningCommand.setStatus("current")


class _WsSwitchCertReqCommand_Type(Integer32):
    """Custom type wsSwitchCertReqCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("initiate", 1))
    )


_WsSwitchCertReqCommand_Type.__name__ = "Integer32"
_WsSwitchCertReqCommand_Object = MibScalar
wsSwitchCertReqCommand = _WsSwitchCertReqCommand_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 18, 10),
    _WsSwitchCertReqCommand_Type()
)
wsSwitchCertReqCommand.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsSwitchCertReqCommand.setStatus("current")
_WdsManagedAP_ObjectIdentity = ObjectIdentity
wdsManagedAP = _WdsManagedAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 19)
)
_WsWDSAPGroupTable_Object = MibTable
wsWDSAPGroupTable = _WsWDSAPGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 19, 1)
)
if mibBuilder.loadTexts:
    wsWDSAPGroupTable.setStatus("current")
_WsWDSAPGroupEntry_Object = MibTableRow
wsWDSAPGroupEntry = _WsWDSAPGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 19, 1, 1)
)
wsWDSAPGroupEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsWDSAPGroupId"),
)
if mibBuilder.loadTexts:
    wsWDSAPGroupEntry.setStatus("current")


class _WsWDSAPGroupId_Type(Integer32):
    """Custom type wsWDSAPGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WsWDSAPGroupId_Type.__name__ = "Integer32"
_WsWDSAPGroupId_Object = MibTableColumn
wsWDSAPGroupId = _WsWDSAPGroupId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 19, 1, 1, 1),
    _WsWDSAPGroupId_Type()
)
wsWDSAPGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsWDSAPGroupId.setStatus("current")


class _WsWDSAPGroupName_Type(DisplayString):
    """Custom type wsWDSAPGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WsWDSAPGroupName_Type.__name__ = "DisplayString"
_WsWDSAPGroupName_Object = MibTableColumn
wsWDSAPGroupName = _WsWDSAPGroupName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 19, 1, 1, 2),
    _WsWDSAPGroupName_Type()
)
wsWDSAPGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsWDSAPGroupName.setStatus("current")


class _WsWDSAPGroupSpanningTree_Type(Integer32):
    """Custom type wsWDSAPGroupSpanningTree based on Integer32"""
    defaultValue = 2

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


_WsWDSAPGroupSpanningTree_Type.__name__ = "Integer32"
_WsWDSAPGroupSpanningTree_Object = MibTableColumn
wsWDSAPGroupSpanningTree = _WsWDSAPGroupSpanningTree_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 19, 1, 1, 3),
    _WsWDSAPGroupSpanningTree_Type()
)
wsWDSAPGroupSpanningTree.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsWDSAPGroupSpanningTree.setStatus("current")


class _WsWDSAPGroupPassword_Type(DisplayString):
    """Custom type wsWDSAPGroupPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 63),
    )


_WsWDSAPGroupPassword_Type.__name__ = "DisplayString"
_WsWDSAPGroupPassword_Object = MibTableColumn
wsWDSAPGroupPassword = _WsWDSAPGroupPassword_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 19, 1, 1, 4),
    _WsWDSAPGroupPassword_Type()
)
wsWDSAPGroupPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsWDSAPGroupPassword.setStatus("current")
_WsWDSAPGroupRowStatus_Type = RowStatus
_WsWDSAPGroupRowStatus_Object = MibTableColumn
wsWDSAPGroupRowStatus = _WsWDSAPGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 19, 1, 1, 5),
    _WsWDSAPGroupRowStatus_Type()
)
wsWDSAPGroupRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsWDSAPGroupRowStatus.setStatus("current")
_WsWDSAPGroupAPTable_Object = MibTable
wsWDSAPGroupAPTable = _WsWDSAPGroupAPTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 19, 2)
)
if mibBuilder.loadTexts:
    wsWDSAPGroupAPTable.setStatus("current")
_WsWDSAPGroupAPEntry_Object = MibTableRow
wsWDSAPGroupAPEntry = _WsWDSAPGroupAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 19, 2, 1)
)
wsWDSAPGroupAPEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsWDSAPGroupId"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsWDSAPGroupAPMacAddress"),
)
if mibBuilder.loadTexts:
    wsWDSAPGroupAPEntry.setStatus("current")
_WsWDSAPGroupAPMacAddress_Type = MacAddress
_WsWDSAPGroupAPMacAddress_Object = MibTableColumn
wsWDSAPGroupAPMacAddress = _WsWDSAPGroupAPMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 19, 2, 1, 1),
    _WsWDSAPGroupAPMacAddress_Type()
)
wsWDSAPGroupAPMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsWDSAPGroupAPMacAddress.setStatus("current")


class _WsWDSAPGroupAPStpPriority_Type(Integer32):
    """Custom type wsWDSAPGroupAPStpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_WsWDSAPGroupAPStpPriority_Type.__name__ = "Integer32"
_WsWDSAPGroupAPStpPriority_Object = MibTableColumn
wsWDSAPGroupAPStpPriority = _WsWDSAPGroupAPStpPriority_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 19, 2, 1, 2),
    _WsWDSAPGroupAPStpPriority_Type()
)
wsWDSAPGroupAPStpPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsWDSAPGroupAPStpPriority.setStatus("current")
_WsWDSAPGroupAPEntryRowStatus_Type = RowStatus
_WsWDSAPGroupAPEntryRowStatus_Object = MibTableColumn
wsWDSAPGroupAPEntryRowStatus = _WsWDSAPGroupAPEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 19, 2, 1, 3),
    _WsWDSAPGroupAPEntryRowStatus_Type()
)
wsWDSAPGroupAPEntryRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsWDSAPGroupAPEntryRowStatus.setStatus("current")
_WsWDSAPLinkTable_Object = MibTable
wsWDSAPLinkTable = _WsWDSAPLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 19, 3)
)
if mibBuilder.loadTexts:
    wsWDSAPLinkTable.setStatus("current")
_WsWDSAPLinkEntry_Object = MibTableRow
wsWDSAPLinkEntry = _WsWDSAPLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 19, 3, 1)
)
wsWDSAPLinkEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsWDSAPGroupId"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsWDSAPLinkSourceMacAddr"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsWDSAPLinkSourceRadio"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsWDSAPLinkDestMacAddr"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsWDSAPLinkDestRadio"),
)
if mibBuilder.loadTexts:
    wsWDSAPLinkEntry.setStatus("current")
_WsWDSAPLinkSourceMacAddr_Type = MacAddress
_WsWDSAPLinkSourceMacAddr_Object = MibTableColumn
wsWDSAPLinkSourceMacAddr = _WsWDSAPLinkSourceMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 19, 3, 1, 1),
    _WsWDSAPLinkSourceMacAddr_Type()
)
wsWDSAPLinkSourceMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsWDSAPLinkSourceMacAddr.setStatus("current")


class _WsWDSAPLinkSourceRadio_Type(Integer32):
    """Custom type wsWDSAPLinkSourceRadio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WsWDSAPLinkSourceRadio_Type.__name__ = "Integer32"
_WsWDSAPLinkSourceRadio_Object = MibTableColumn
wsWDSAPLinkSourceRadio = _WsWDSAPLinkSourceRadio_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 19, 3, 1, 2),
    _WsWDSAPLinkSourceRadio_Type()
)
wsWDSAPLinkSourceRadio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsWDSAPLinkSourceRadio.setStatus("current")
_WsWDSAPLinkDestMacAddr_Type = MacAddress
_WsWDSAPLinkDestMacAddr_Object = MibTableColumn
wsWDSAPLinkDestMacAddr = _WsWDSAPLinkDestMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 19, 3, 1, 3),
    _WsWDSAPLinkDestMacAddr_Type()
)
wsWDSAPLinkDestMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsWDSAPLinkDestMacAddr.setStatus("current")


class _WsWDSAPLinkDestRadio_Type(Integer32):
    """Custom type wsWDSAPLinkDestRadio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WsWDSAPLinkDestRadio_Type.__name__ = "Integer32"
_WsWDSAPLinkDestRadio_Object = MibTableColumn
wsWDSAPLinkDestRadio = _WsWDSAPLinkDestRadio_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 19, 3, 1, 4),
    _WsWDSAPLinkDestRadio_Type()
)
wsWDSAPLinkDestRadio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsWDSAPLinkDestRadio.setStatus("current")


class _WsWDSAPLinkPathCost_Type(Integer32):
    """Custom type wsWDSAPLinkPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WsWDSAPLinkPathCost_Type.__name__ = "Integer32"
_WsWDSAPLinkPathCost_Object = MibTableColumn
wsWDSAPLinkPathCost = _WsWDSAPLinkPathCost_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 19, 3, 1, 5),
    _WsWDSAPLinkPathCost_Type()
)
wsWDSAPLinkPathCost.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsWDSAPLinkPathCost.setStatus("current")
_WsWDSAPLinkRowStatus_Type = RowStatus
_WsWDSAPLinkRowStatus_Object = MibTableColumn
wsWDSAPLinkRowStatus = _WsWDSAPLinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 19, 3, 1, 6),
    _WsWDSAPLinkRowStatus_Type()
)
wsWDSAPLinkRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsWDSAPLinkRowStatus.setStatus("current")
_WsWDSAPGroupStatusTable_Object = MibTable
wsWDSAPGroupStatusTable = _WsWDSAPGroupStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 19, 4)
)
if mibBuilder.loadTexts:
    wsWDSAPGroupStatusTable.setStatus("current")
_WsWDSAPGroupStatusEntry_Object = MibTableRow
wsWDSAPGroupStatusEntry = _WsWDSAPGroupStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 19, 4, 1)
)
wsWDSAPGroupStatusEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsWDSAPGroupId"),
)
if mibBuilder.loadTexts:
    wsWDSAPGroupStatusEntry.setStatus("current")


class _WsWDSConfigAPCount_Type(Integer32):
    """Custom type wsWDSConfigAPCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_WsWDSConfigAPCount_Type.__name__ = "Integer32"
_WsWDSConfigAPCount_Object = MibTableColumn
wsWDSConfigAPCount = _WsWDSConfigAPCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 19, 4, 1, 1),
    _WsWDSConfigAPCount_Type()
)
wsWDSConfigAPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsWDSConfigAPCount.setStatus("current")


class _WsWDSConnectedAPCount_Type(Integer32):
    """Custom type wsWDSConnectedAPCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_WsWDSConnectedAPCount_Type.__name__ = "Integer32"
_WsWDSConnectedAPCount_Object = MibTableColumn
wsWDSConnectedAPCount = _WsWDSConnectedAPCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 19, 4, 1, 2),
    _WsWDSConnectedAPCount_Type()
)
wsWDSConnectedAPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsWDSConnectedAPCount.setStatus("current")


class _WsWDSRootAPCount_Type(Integer32):
    """Custom type wsWDSRootAPCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_WsWDSRootAPCount_Type.__name__ = "Integer32"
_WsWDSRootAPCount_Object = MibTableColumn
wsWDSRootAPCount = _WsWDSRootAPCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 19, 4, 1, 3),
    _WsWDSRootAPCount_Type()
)
wsWDSRootAPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsWDSRootAPCount.setStatus("current")


class _WsWDSSatelliteAPCount_Type(Integer32):
    """Custom type wsWDSSatelliteAPCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_WsWDSSatelliteAPCount_Type.__name__ = "Integer32"
_WsWDSSatelliteAPCount_Object = MibTableColumn
wsWDSSatelliteAPCount = _WsWDSSatelliteAPCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 19, 4, 1, 4),
    _WsWDSSatelliteAPCount_Type()
)
wsWDSSatelliteAPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsWDSSatelliteAPCount.setStatus("current")
_WsWDSAPRootBridge_Type = MacAddress
_WsWDSAPRootBridge_Object = MibTableColumn
wsWDSAPRootBridge = _WsWDSAPRootBridge_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 19, 4, 1, 5),
    _WsWDSAPRootBridge_Type()
)
wsWDSAPRootBridge.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsWDSAPRootBridge.setStatus("current")


class _WsWDSAPRootDeviceType_Type(Integer32):
    """Custom type wsWDSAPRootDeviceType based on Integer32"""
    defaultValue = 0

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
          ("root-ap", 1),
          ("satellite-ap", 2),
          ("external-device", 3))
    )


_WsWDSAPRootDeviceType_Type.__name__ = "Integer32"
_WsWDSAPRootDeviceType_Object = MibTableColumn
wsWDSAPRootDeviceType = _WsWDSAPRootDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 19, 4, 1, 6),
    _WsWDSAPRootDeviceType_Type()
)
wsWDSAPRootDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsWDSAPRootDeviceType.setStatus("current")


class _WsWDSConfigWDSLinkCount_Type(Integer32):
    """Custom type wsWDSConfigWDSLinkCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_WsWDSConfigWDSLinkCount_Type.__name__ = "Integer32"
_WsWDSConfigWDSLinkCount_Object = MibTableColumn
wsWDSConfigWDSLinkCount = _WsWDSConfigWDSLinkCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 19, 4, 1, 7),
    _WsWDSConfigWDSLinkCount_Type()
)
wsWDSConfigWDSLinkCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsWDSConfigWDSLinkCount.setStatus("current")


class _WsWDSDetectedWDSLinkCount_Type(Integer32):
    """Custom type wsWDSDetectedWDSLinkCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_WsWDSDetectedWDSLinkCount_Type.__name__ = "Integer32"
_WsWDSDetectedWDSLinkCount_Object = MibTableColumn
wsWDSDetectedWDSLinkCount = _WsWDSDetectedWDSLinkCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 19, 4, 1, 8),
    _WsWDSDetectedWDSLinkCount_Type()
)
wsWDSDetectedWDSLinkCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsWDSDetectedWDSLinkCount.setStatus("current")


class _WsWDSBlockedWDSLinkCount_Type(Integer32):
    """Custom type wsWDSBlockedWDSLinkCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_WsWDSBlockedWDSLinkCount_Type.__name__ = "Integer32"
_WsWDSBlockedWDSLinkCount_Object = MibTableColumn
wsWDSBlockedWDSLinkCount = _WsWDSBlockedWDSLinkCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 19, 4, 1, 9),
    _WsWDSBlockedWDSLinkCount_Type()
)
wsWDSBlockedWDSLinkCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsWDSBlockedWDSLinkCount.setStatus("current")


class _WsWDSGroupNewPassword_Type(DisplayString):
    """Custom type wsWDSGroupNewPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 63),
    )


_WsWDSGroupNewPassword_Type.__name__ = "DisplayString"
_WsWDSGroupNewPassword_Object = MibTableColumn
wsWDSGroupNewPassword = _WsWDSGroupNewPassword_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 19, 4, 1, 10),
    _WsWDSGroupNewPassword_Type()
)
wsWDSGroupNewPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsWDSGroupNewPassword.setStatus("current")


class _WsWDSGroupChangePasswdStart_Type(Integer32):
    """Custom type wsWDSGroupChangePasswdStart based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("start", 2))
    )


_WsWDSGroupChangePasswdStart_Type.__name__ = "Integer32"
_WsWDSGroupChangePasswdStart_Object = MibTableColumn
wsWDSGroupChangePasswdStart = _WsWDSGroupChangePasswdStart_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 19, 4, 1, 11),
    _WsWDSGroupChangePasswdStart_Type()
)
wsWDSGroupChangePasswdStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsWDSGroupChangePasswdStart.setStatus("current")


class _WsWDSGroupChangePasswdStatus_Type(Integer32):
    """Custom type wsWDSGroupChangePasswdStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("not-started", 1),
          ("requested", 2),
          ("success", 3),
          ("invalid-password", 4),
          ("in-progress", 5),
          ("timed-out", 6),
          ("failed", 7))
    )


_WsWDSGroupChangePasswdStatus_Type.__name__ = "Integer32"
_WsWDSGroupChangePasswdStatus_Object = MibTableColumn
wsWDSGroupChangePasswdStatus = _WsWDSGroupChangePasswdStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 19, 4, 1, 12),
    _WsWDSGroupChangePasswdStatus_Type()
)
wsWDSGroupChangePasswdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsWDSGroupChangePasswdStatus.setStatus("current")
_WsWDSAPStatusTable_Object = MibTable
wsWDSAPStatusTable = _WsWDSAPStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 19, 5)
)
if mibBuilder.loadTexts:
    wsWDSAPStatusTable.setStatus("current")
_WsWDSAPStatusEntry_Object = MibTableRow
wsWDSAPStatusEntry = _WsWDSAPStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 19, 5, 1)
)
wsWDSAPStatusEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsWDSAPGroupId"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsWDSAPMacAddr"),
)
if mibBuilder.loadTexts:
    wsWDSAPStatusEntry.setStatus("current")
_WsWDSAPMacAddr_Type = MacAddress
_WsWDSAPMacAddr_Object = MibTableColumn
wsWDSAPMacAddr = _WsWDSAPMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 19, 5, 1, 1),
    _WsWDSAPMacAddr_Type()
)
wsWDSAPMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsWDSAPMacAddr.setStatus("current")


class _WsWDSAPConnectionStatus_Type(Integer32):
    """Custom type wsWDSAPConnectionStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-connected", 0),
          ("connected", 1))
    )


_WsWDSAPConnectionStatus_Type.__name__ = "Integer32"
_WsWDSAPConnectionStatus_Object = MibTableColumn
wsWDSAPConnectionStatus = _WsWDSAPConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 19, 5, 1, 2),
    _WsWDSAPConnectionStatus_Type()
)
wsWDSAPConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsWDSAPConnectionStatus.setStatus("current")


class _WsWDSAPSatelliteMode_Type(Integer32):
    """Custom type wsWDSAPSatelliteMode based on Integer32"""
    defaultValue = 0

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
          ("wired", 1),
          ("satellite", 2))
    )


_WsWDSAPSatelliteMode_Type.__name__ = "Integer32"
_WsWDSAPSatelliteMode_Object = MibTableColumn
wsWDSAPSatelliteMode = _WsWDSAPSatelliteMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 19, 5, 1, 3),
    _WsWDSAPSatelliteMode_Type()
)
wsWDSAPSatelliteMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsWDSAPSatelliteMode.setStatus("current")


class _WsWDSAPSTPRootMode_Type(Integer32):
    """Custom type wsWDSAPSTPRootMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-stp-root", 0),
          ("stp-root", 1))
    )


_WsWDSAPSTPRootMode_Type.__name__ = "Integer32"
_WsWDSAPSTPRootMode_Object = MibTableColumn
wsWDSAPSTPRootMode = _WsWDSAPSTPRootMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 19, 5, 1, 4),
    _WsWDSAPSTPRootMode_Type()
)
wsWDSAPSTPRootMode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsWDSAPSTPRootMode.setStatus("current")
_WsWDSAPSTPCost_Type = Unsigned32
_WsWDSAPSTPCost_Object = MibTableColumn
wsWDSAPSTPCost = _WsWDSAPSTPCost_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 19, 5, 1, 5),
    _WsWDSAPSTPCost_Type()
)
wsWDSAPSTPCost.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsWDSAPSTPCost.setStatus("current")


class _WsWDSAPEthPortSTPStatus_Type(Integer32):
    """Custom type wsWDSAPEthPortSTPStatus based on Integer32"""
    defaultValue = 0

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
        *(("disabled", 0),
          ("forwarding", 1),
          ("learning", 2),
          ("listening", 3),
          ("blocking", 4))
    )


_WsWDSAPEthPortSTPStatus_Type.__name__ = "Integer32"
_WsWDSAPEthPortSTPStatus_Object = MibTableColumn
wsWDSAPEthPortSTPStatus = _WsWDSAPEthPortSTPStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 19, 5, 1, 6),
    _WsWDSAPEthPortSTPStatus_Type()
)
wsWDSAPEthPortSTPStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsWDSAPEthPortSTPStatus.setStatus("current")


class _WsWDSAPEthPortMode_Type(Integer32):
    """Custom type wsWDSAPEthPortMode based on Integer32"""
    defaultValue = 0

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


_WsWDSAPEthPortMode_Type.__name__ = "Integer32"
_WsWDSAPEthPortMode_Object = MibTableColumn
wsWDSAPEthPortMode = _WsWDSAPEthPortMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 19, 5, 1, 7),
    _WsWDSAPEthPortMode_Type()
)
wsWDSAPEthPortMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsWDSAPEthPortMode.setStatus("current")


class _WsWDSAPEthPortLinkState_Type(Integer32):
    """Custom type wsWDSAPEthPortLinkState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_WsWDSAPEthPortLinkState_Type.__name__ = "Integer32"
_WsWDSAPEthPortLinkState_Object = MibTableColumn
wsWDSAPEthPortLinkState = _WsWDSAPEthPortLinkState_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 19, 5, 1, 8),
    _WsWDSAPEthPortLinkState_Type()
)
wsWDSAPEthPortLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsWDSAPEthPortLinkState.setStatus("current")
_WsWDSLinkStatusTable_Object = MibTable
wsWDSLinkStatusTable = _WsWDSLinkStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 19, 6)
)
if mibBuilder.loadTexts:
    wsWDSLinkStatusTable.setStatus("current")
_WsWDSLinkStatusEntry_Object = MibTableRow
wsWDSLinkStatusEntry = _WsWDSLinkStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 19, 6, 1)
)
wsWDSLinkStatusEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsWDSAPGroupId"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsWDSSourceMacAddr"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsWDSSourceRadio"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsWDSDestMacAddr"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsWDSDestRadio"),
)
if mibBuilder.loadTexts:
    wsWDSLinkStatusEntry.setStatus("current")
_WsWDSSourceMacAddr_Type = MacAddress
_WsWDSSourceMacAddr_Object = MibTableColumn
wsWDSSourceMacAddr = _WsWDSSourceMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 19, 6, 1, 1),
    _WsWDSSourceMacAddr_Type()
)
wsWDSSourceMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsWDSSourceMacAddr.setStatus("current")


class _WsWDSSourceRadio_Type(Integer32):
    """Custom type wsWDSSourceRadio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WsWDSSourceRadio_Type.__name__ = "Integer32"
_WsWDSSourceRadio_Object = MibTableColumn
wsWDSSourceRadio = _WsWDSSourceRadio_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 19, 6, 1, 2),
    _WsWDSSourceRadio_Type()
)
wsWDSSourceRadio.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsWDSSourceRadio.setStatus("current")
_WsWDSDestMacAddr_Type = MacAddress
_WsWDSDestMacAddr_Object = MibTableColumn
wsWDSDestMacAddr = _WsWDSDestMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 19, 6, 1, 3),
    _WsWDSDestMacAddr_Type()
)
wsWDSDestMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsWDSDestMacAddr.setStatus("current")


class _WsWDSDestRadio_Type(Integer32):
    """Custom type wsWDSDestRadio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WsWDSDestRadio_Type.__name__ = "Integer32"
_WsWDSDestRadio_Object = MibTableColumn
wsWDSDestRadio = _WsWDSDestRadio_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 19, 6, 1, 4),
    _WsWDSDestRadio_Type()
)
wsWDSDestRadio.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsWDSDestRadio.setStatus("current")


class _WsWDSLinkSourceEndPointDetected_Type(Integer32):
    """Custom type wsWDSLinkSourceEndPointDetected based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-detected", 0),
          ("detected", 1))
    )


_WsWDSLinkSourceEndPointDetected_Type.__name__ = "Integer32"
_WsWDSLinkSourceEndPointDetected_Object = MibTableColumn
wsWDSLinkSourceEndPointDetected = _WsWDSLinkSourceEndPointDetected_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 19, 6, 1, 5),
    _WsWDSLinkSourceEndPointDetected_Type()
)
wsWDSLinkSourceEndPointDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsWDSLinkSourceEndPointDetected.setStatus("current")


class _WsWDSLinkDestEndPointDetected_Type(Integer32):
    """Custom type wsWDSLinkDestEndPointDetected based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-detected", 0),
          ("detected", 1))
    )


_WsWDSLinkDestEndPointDetected_Type.__name__ = "Integer32"
_WsWDSLinkDestEndPointDetected_Object = MibTableColumn
wsWDSLinkDestEndPointDetected = _WsWDSLinkDestEndPointDetected_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 19, 6, 1, 6),
    _WsWDSLinkDestEndPointDetected_Type()
)
wsWDSLinkDestEndPointDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsWDSLinkDestEndPointDetected.setStatus("current")


class _WsWDSLinkSourceSTPState_Type(Integer32):
    """Custom type wsWDSLinkSourceSTPState based on Integer32"""
    defaultValue = 0

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
        *(("disabled", 0),
          ("forwarding", 1),
          ("learning", 2),
          ("listening", 3),
          ("blocking", 4))
    )


_WsWDSLinkSourceSTPState_Type.__name__ = "Integer32"
_WsWDSLinkSourceSTPState_Object = MibTableColumn
wsWDSLinkSourceSTPState = _WsWDSLinkSourceSTPState_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 19, 6, 1, 7),
    _WsWDSLinkSourceSTPState_Type()
)
wsWDSLinkSourceSTPState.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsWDSLinkSourceSTPState.setStatus("current")


class _WsWDSLinkDestSTPState_Type(Integer32):
    """Custom type wsWDSLinkDestSTPState based on Integer32"""
    defaultValue = 0

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
        *(("disabled", 0),
          ("forwarding", 1),
          ("learning", 2),
          ("listening", 3),
          ("blocking", 4))
    )


_WsWDSLinkDestSTPState_Type.__name__ = "Integer32"
_WsWDSLinkDestSTPState_Object = MibTableColumn
wsWDSLinkDestSTPState = _WsWDSLinkDestSTPState_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 19, 6, 1, 8),
    _WsWDSLinkDestSTPState_Type()
)
wsWDSLinkDestSTPState.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsWDSLinkDestSTPState.setStatus("current")


class _WsWDSLinkAggregationMode_Type(Integer32):
    """Custom type wsWDSLinkAggregationMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-aggregated", 0),
          ("aggregated", 1))
    )


_WsWDSLinkAggregationMode_Type.__name__ = "Integer32"
_WsWDSLinkAggregationMode_Object = MibTableColumn
wsWDSLinkAggregationMode = _WsWDSLinkAggregationMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 19, 6, 1, 9),
    _WsWDSLinkAggregationMode_Type()
)
wsWDSLinkAggregationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsWDSLinkAggregationMode.setStatus("current")
_WsWDSLinkStatisticsTable_Object = MibTable
wsWDSLinkStatisticsTable = _WsWDSLinkStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 19, 7)
)
if mibBuilder.loadTexts:
    wsWDSLinkStatisticsTable.setStatus("current")
_WsWDSLinkStatisticsEntry_Object = MibTableRow
wsWDSLinkStatisticsEntry = _WsWDSLinkStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 19, 7, 1)
)
if mibBuilder.loadTexts:
    wsWDSLinkStatisticsEntry.setStatus("current")
_WsWDSLinkSourceAPPktsSent_Type = Counter64
_WsWDSLinkSourceAPPktsSent_Object = MibTableColumn
wsWDSLinkSourceAPPktsSent = _WsWDSLinkSourceAPPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 19, 7, 1, 1),
    _WsWDSLinkSourceAPPktsSent_Type()
)
wsWDSLinkSourceAPPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsWDSLinkSourceAPPktsSent.setStatus("current")
_WsWDSLinkSourceAPBytesSent_Type = Counter64
_WsWDSLinkSourceAPBytesSent_Object = MibTableColumn
wsWDSLinkSourceAPBytesSent = _WsWDSLinkSourceAPBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 19, 7, 1, 2),
    _WsWDSLinkSourceAPBytesSent_Type()
)
wsWDSLinkSourceAPBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsWDSLinkSourceAPBytesSent.setStatus("current")
_WsWDSLinkSourceAPPktsRcvd_Type = Counter64
_WsWDSLinkSourceAPPktsRcvd_Object = MibTableColumn
wsWDSLinkSourceAPPktsRcvd = _WsWDSLinkSourceAPPktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 19, 7, 1, 3),
    _WsWDSLinkSourceAPPktsRcvd_Type()
)
wsWDSLinkSourceAPPktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsWDSLinkSourceAPPktsRcvd.setStatus("current")
_WsWDSLinkSourceAPBytesRcvd_Type = Counter64
_WsWDSLinkSourceAPBytesRcvd_Object = MibTableColumn
wsWDSLinkSourceAPBytesRcvd = _WsWDSLinkSourceAPBytesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 19, 7, 1, 4),
    _WsWDSLinkSourceAPBytesRcvd_Type()
)
wsWDSLinkSourceAPBytesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsWDSLinkSourceAPBytesRcvd.setStatus("current")
_WsWDSLinkDestAPPktsSent_Type = Counter64
_WsWDSLinkDestAPPktsSent_Object = MibTableColumn
wsWDSLinkDestAPPktsSent = _WsWDSLinkDestAPPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 19, 7, 1, 5),
    _WsWDSLinkDestAPPktsSent_Type()
)
wsWDSLinkDestAPPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsWDSLinkDestAPPktsSent.setStatus("current")
_WsWDSLinkDestAPBytesSent_Type = Counter64
_WsWDSLinkDestAPBytesSent_Object = MibTableColumn
wsWDSLinkDestAPBytesSent = _WsWDSLinkDestAPBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 19, 7, 1, 6),
    _WsWDSLinkDestAPBytesSent_Type()
)
wsWDSLinkDestAPBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsWDSLinkDestAPBytesSent.setStatus("current")
_WsWDSLinkDestAPPktsRcvd_Type = Counter64
_WsWDSLinkDestAPPktsRcvd_Object = MibTableColumn
wsWDSLinkDestAPPktsRcvd = _WsWDSLinkDestAPPktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 19, 7, 1, 7),
    _WsWDSLinkDestAPPktsRcvd_Type()
)
wsWDSLinkDestAPPktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsWDSLinkDestAPPktsRcvd.setStatus("current")
_WsWDSLinkDestAPBytesRcvd_Type = Counter64
_WsWDSLinkDestAPBytesRcvd_Object = MibTableColumn
wsWDSLinkDestAPBytesRcvd = _WsWDSLinkDestAPBytesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 19, 7, 1, 8),
    _WsWDSLinkDestAPBytesRcvd_Type()
)
wsWDSLinkDestAPBytesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsWDSLinkDestAPBytesRcvd.setStatus("current")


class _WsWDSGroupConfigRequestAction_Type(Integer32):
    """Custom type wsWDSGroupConfigRequestAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("start", 2))
    )


_WsWDSGroupConfigRequestAction_Type.__name__ = "Integer32"
_WsWDSGroupConfigRequestAction_Object = MibScalar
wsWDSGroupConfigRequestAction = _WsWDSGroupConfigRequestAction_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 19, 8),
    _WsWDSGroupConfigRequestAction_Type()
)
wsWDSGroupConfigRequestAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsWDSGroupConfigRequestAction.setStatus("current")
_DeviceLocation_ObjectIdentity = ObjectIdentity
deviceLocation = _DeviceLocation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 20)
)
_WsDevLocBldngTable_Object = MibTable
wsDevLocBldngTable = _WsDevLocBldngTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 20, 1)
)
if mibBuilder.loadTexts:
    wsDevLocBldngTable.setStatus("current")
_WsDevLocBldngEntry_Object = MibTableRow
wsDevLocBldngEntry = _WsDevLocBldngEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 20, 1, 1)
)
wsDevLocBldngEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsDevLocBldngNum"),
)
if mibBuilder.loadTexts:
    wsDevLocBldngEntry.setStatus("current")


class _WsDevLocBldngNum_Type(Integer32):
    """Custom type wsDevLocBldngNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_WsDevLocBldngNum_Type.__name__ = "Integer32"
_WsDevLocBldngNum_Object = MibTableColumn
wsDevLocBldngNum = _WsDevLocBldngNum_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 20, 1, 1, 1),
    _WsDevLocBldngNum_Type()
)
wsDevLocBldngNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDevLocBldngNum.setStatus("current")


class _WsDevLocBldngDesc_Type(DisplayString):
    """Custom type wsDevLocBldngDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WsDevLocBldngDesc_Type.__name__ = "DisplayString"
_WsDevLocBldngDesc_Object = MibTableColumn
wsDevLocBldngDesc = _WsDevLocBldngDesc_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 20, 1, 1, 2),
    _WsDevLocBldngDesc_Type()
)
wsDevLocBldngDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDevLocBldngDesc.setStatus("current")


class _WsDevLocFlrCount_Type(Integer32):
    """Custom type wsDevLocFlrCount based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_WsDevLocFlrCount_Type.__name__ = "Integer32"
_WsDevLocFlrCount_Object = MibTableColumn
wsDevLocFlrCount = _WsDevLocFlrCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 20, 1, 1, 3),
    _WsDevLocFlrCount_Type()
)
wsDevLocFlrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDevLocFlrCount.setStatus("current")


class _WsDevLocApCount_Type(Integer32):
    """Custom type wsDevLocApCount based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 192),
    )


_WsDevLocApCount_Type.__name__ = "Integer32"
_WsDevLocApCount_Object = MibTableColumn
wsDevLocApCount = _WsDevLocApCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 20, 1, 1, 4),
    _WsDevLocApCount_Type()
)
wsDevLocApCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDevLocApCount.setStatus("current")
_WsDevLocBldngRowStatus_Type = RowStatus
_WsDevLocBldngRowStatus_Object = MibTableColumn
wsDevLocBldngRowStatus = _WsDevLocBldngRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 20, 1, 1, 5),
    _WsDevLocBldngRowStatus_Type()
)
wsDevLocBldngRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDevLocBldngRowStatus.setStatus("current")
_WsDevLocBldngFlrTable_Object = MibTable
wsDevLocBldngFlrTable = _WsDevLocBldngFlrTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 20, 2)
)
if mibBuilder.loadTexts:
    wsDevLocBldngFlrTable.setStatus("current")
_WsDevLocBldngFlrEntry_Object = MibTableRow
wsDevLocBldngFlrEntry = _WsDevLocBldngFlrEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 20, 2, 1)
)
wsDevLocBldngFlrEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsDevLocBldngNum"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsDevLocBldngFlrNum"),
)
if mibBuilder.loadTexts:
    wsDevLocBldngFlrEntry.setStatus("current")


class _WsDevLocBldngFlrNum_Type(Integer32):
    """Custom type wsDevLocBldngFlrNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_WsDevLocBldngFlrNum_Type.__name__ = "Integer32"
_WsDevLocBldngFlrNum_Object = MibTableColumn
wsDevLocBldngFlrNum = _WsDevLocBldngFlrNum_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 20, 2, 1, 1),
    _WsDevLocBldngFlrNum_Type()
)
wsDevLocBldngFlrNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsDevLocBldngFlrNum.setStatus("current")


class _WsDevLocBldngFlrDesc_Type(DisplayString):
    """Custom type wsDevLocBldngFlrDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WsDevLocBldngFlrDesc_Type.__name__ = "DisplayString"
_WsDevLocBldngFlrDesc_Object = MibTableColumn
wsDevLocBldngFlrDesc = _WsDevLocBldngFlrDesc_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 20, 2, 1, 2),
    _WsDevLocBldngFlrDesc_Type()
)
wsDevLocBldngFlrDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDevLocBldngFlrDesc.setStatus("current")


class _WsDevLocBldngFlrApCount_Type(Integer32):
    """Custom type wsDevLocBldngFlrApCount based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 192),
    )


_WsDevLocBldngFlrApCount_Type.__name__ = "Integer32"
_WsDevLocBldngFlrApCount_Object = MibTableColumn
wsDevLocBldngFlrApCount = _WsDevLocBldngFlrApCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 20, 2, 1, 3),
    _WsDevLocBldngFlrApCount_Type()
)
wsDevLocBldngFlrApCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDevLocBldngFlrApCount.setStatus("current")
_WsDevLocFlrRowStatus_Type = RowStatus
_WsDevLocFlrRowStatus_Object = MibTableColumn
wsDevLocFlrRowStatus = _WsDevLocFlrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 20, 2, 1, 4),
    _WsDevLocFlrRowStatus_Type()
)
wsDevLocFlrRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDevLocFlrRowStatus.setStatus("current")
_WsDevLocManagedApTable_Object = MibTable
wsDevLocManagedApTable = _WsDevLocManagedApTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 20, 3)
)
if mibBuilder.loadTexts:
    wsDevLocManagedApTable.setStatus("current")
_WsDevLocManagedApEntry_Object = MibTableRow
wsDevLocManagedApEntry = _WsDevLocManagedApEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 20, 3, 1)
)
wsDevLocManagedApEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsDevLocBldngNum"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsDevLocBldngFlrNum"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsDevLocManagedApMac"),
)
if mibBuilder.loadTexts:
    wsDevLocManagedApEntry.setStatus("current")
_WsDevLocManagedApMac_Type = MacAddress
_WsDevLocManagedApMac_Object = MibTableColumn
wsDevLocManagedApMac = _WsDevLocManagedApMac_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 20, 3, 1, 1),
    _WsDevLocManagedApMac_Type()
)
wsDevLocManagedApMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDevLocManagedApMac.setStatus("current")


class _WsDevLocMeasurementUnit_Type(Integer32):
    """Custom type wsDevLocMeasurementUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("meters", 1),
          ("feet", 2))
    )


_WsDevLocMeasurementUnit_Type.__name__ = "Integer32"
_WsDevLocMeasurementUnit_Object = MibTableColumn
wsDevLocMeasurementUnit = _WsDevLocMeasurementUnit_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 20, 3, 1, 2),
    _WsDevLocMeasurementUnit_Type()
)
wsDevLocMeasurementUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDevLocMeasurementUnit.setStatus("current")


class _WsDevLocManagedApXCoord_Type(Integer32):
    """Custom type wsDevLocManagedApXCoord based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-3000, 3000),
    )


_WsDevLocManagedApXCoord_Type.__name__ = "Integer32"
_WsDevLocManagedApXCoord_Object = MibTableColumn
wsDevLocManagedApXCoord = _WsDevLocManagedApXCoord_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 20, 3, 1, 3),
    _WsDevLocManagedApXCoord_Type()
)
wsDevLocManagedApXCoord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDevLocManagedApXCoord.setStatus("current")


class _WsDevLocManagedApYCoord_Type(Integer32):
    """Custom type wsDevLocManagedApYCoord based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-3000, 3000),
    )


_WsDevLocManagedApYCoord_Type.__name__ = "Integer32"
_WsDevLocManagedApYCoord_Object = MibTableColumn
wsDevLocManagedApYCoord = _WsDevLocManagedApYCoord_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 20, 3, 1, 4),
    _WsDevLocManagedApYCoord_Type()
)
wsDevLocManagedApYCoord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDevLocManagedApYCoord.setStatus("current")
_WsDevLocManagedApRowStatus_Type = RowStatus
_WsDevLocManagedApRowStatus_Object = MibTableColumn
wsDevLocManagedApRowStatus = _WsDevLocManagedApRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 20, 3, 1, 5),
    _WsDevLocManagedApRowStatus_Type()
)
wsDevLocManagedApRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDevLocManagedApRowStatus.setStatus("current")
_WsOnDemandTrigger_ObjectIdentity = ObjectIdentity
wsOnDemandTrigger = _WsOnDemandTrigger_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 20, 4)
)


class _WsOnDemandTriggerDeviceType_Type(Integer32):
    """Custom type wsOnDemandTriggerDeviceType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ap", 1),
          ("client", 2))
    )


_WsOnDemandTriggerDeviceType_Type.__name__ = "Integer32"
_WsOnDemandTriggerDeviceType_Object = MibScalar
wsOnDemandTriggerDeviceType = _WsOnDemandTriggerDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 20, 4, 1),
    _WsOnDemandTriggerDeviceType_Type()
)
wsOnDemandTriggerDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsOnDemandTriggerDeviceType.setStatus("current")
_WsOnDemandTriggerDeviceMACAddress_Type = MacAddress
_WsOnDemandTriggerDeviceMACAddress_Object = MibScalar
wsOnDemandTriggerDeviceMACAddress = _WsOnDemandTriggerDeviceMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 20, 4, 2),
    _WsOnDemandTriggerDeviceMACAddress_Type()
)
wsOnDemandTriggerDeviceMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsOnDemandTriggerDeviceMACAddress.setStatus("current")


class _WsOnDemandTriggerBuildingNumber_Type(Unsigned32):
    """Custom type wsOnDemandTriggerBuildingNumber based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_WsOnDemandTriggerBuildingNumber_Type.__name__ = "Unsigned32"
_WsOnDemandTriggerBuildingNumber_Object = MibScalar
wsOnDemandTriggerBuildingNumber = _WsOnDemandTriggerBuildingNumber_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 20, 4, 3),
    _WsOnDemandTriggerBuildingNumber_Type()
)
wsOnDemandTriggerBuildingNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsOnDemandTriggerBuildingNumber.setStatus("current")


class _WsOnDemandTriggerFloorNumber_Type(Unsigned32):
    """Custom type wsOnDemandTriggerFloorNumber based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_WsOnDemandTriggerFloorNumber_Type.__name__ = "Unsigned32"
_WsOnDemandTriggerFloorNumber_Object = MibScalar
wsOnDemandTriggerFloorNumber = _WsOnDemandTriggerFloorNumber_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 20, 4, 4),
    _WsOnDemandTriggerFloorNumber_Type()
)
wsOnDemandTriggerFloorNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsOnDemandTriggerFloorNumber.setStatus("current")


class _WsOnDemandTriggerUseRadios_Type(Integer32):
    """Custom type wsOnDemandTriggerUseRadios based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sentry", 1),
          ("sentryAndOperational", 2))
    )


_WsOnDemandTriggerUseRadios_Type.__name__ = "Integer32"
_WsOnDemandTriggerUseRadios_Object = MibScalar
wsOnDemandTriggerUseRadios = _WsOnDemandTriggerUseRadios_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 20, 4, 5),
    _WsOnDemandTriggerUseRadios_Type()
)
wsOnDemandTriggerUseRadios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsOnDemandTriggerUseRadios.setStatus("current")


class _WsOnDemandTriggerStatus_Type(Integer32):
    """Custom type wsOnDemandTriggerStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notInProgress", 1),
          ("inProgress", 2))
    )


_WsOnDemandTriggerStatus_Type.__name__ = "Integer32"
_WsOnDemandTriggerStatus_Object = MibScalar
wsOnDemandTriggerStatus = _WsOnDemandTriggerStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 20, 4, 6),
    _WsOnDemandTriggerStatus_Type()
)
wsOnDemandTriggerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsOnDemandTriggerStatus.setStatus("current")


class _WsOnDemandTriggerNumOfAPs_Type(Unsigned32):
    """Custom type wsOnDemandTriggerNumOfAPs based on Unsigned32"""
    defaultValue = 0


_WsOnDemandTriggerNumOfAPs_Type.__name__ = "Unsigned32"
_WsOnDemandTriggerNumOfAPs_Object = MibScalar
wsOnDemandTriggerNumOfAPs = _WsOnDemandTriggerNumOfAPs_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 20, 4, 7),
    _WsOnDemandTriggerNumOfAPs_Type()
)
wsOnDemandTriggerNumOfAPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsOnDemandTriggerNumOfAPs.setStatus("current")


class _WsOnDemandTriggerStart_Type(Integer32):
    """Custom type wsOnDemandTriggerStart based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("start", 1))
    )


_WsOnDemandTriggerStart_Type.__name__ = "Integer32"
_WsOnDemandTriggerStart_Object = MibScalar
wsOnDemandTriggerStart = _WsOnDemandTriggerStart_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 20, 4, 8),
    _WsOnDemandTriggerStart_Type()
)
wsOnDemandTriggerStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsOnDemandTriggerStart.setStatus("current")
_WsOnDemandTriggerGlobalStatus_ObjectIdentity = ObjectIdentity
wsOnDemandTriggerGlobalStatus = _WsOnDemandTriggerGlobalStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 20, 5)
)


class _WsOnDemandTriggerGlobalStatusDeviceType_Type(Integer32):
    """Custom type wsOnDemandTriggerGlobalStatusDeviceType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ap", 1),
          ("client", 2))
    )


_WsOnDemandTriggerGlobalStatusDeviceType_Type.__name__ = "Integer32"
_WsOnDemandTriggerGlobalStatusDeviceType_Object = MibScalar
wsOnDemandTriggerGlobalStatusDeviceType = _WsOnDemandTriggerGlobalStatusDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 20, 5, 1),
    _WsOnDemandTriggerGlobalStatusDeviceType_Type()
)
wsOnDemandTriggerGlobalStatusDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsOnDemandTriggerGlobalStatusDeviceType.setStatus("current")
_WsOnDemandTriggerGlobalStatusDeviceMACAddress_Type = MacAddress
_WsOnDemandTriggerGlobalStatusDeviceMACAddress_Object = MibScalar
wsOnDemandTriggerGlobalStatusDeviceMACAddress = _WsOnDemandTriggerGlobalStatusDeviceMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 20, 5, 2),
    _WsOnDemandTriggerGlobalStatusDeviceMACAddress_Type()
)
wsOnDemandTriggerGlobalStatusDeviceMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsOnDemandTriggerGlobalStatusDeviceMACAddress.setStatus("current")


class _WsOnDemandTriggerGlobalStatusBuildingNumber_Type(Unsigned32):
    """Custom type wsOnDemandTriggerGlobalStatusBuildingNumber based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_WsOnDemandTriggerGlobalStatusBuildingNumber_Type.__name__ = "Unsigned32"
_WsOnDemandTriggerGlobalStatusBuildingNumber_Object = MibScalar
wsOnDemandTriggerGlobalStatusBuildingNumber = _WsOnDemandTriggerGlobalStatusBuildingNumber_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 20, 5, 3),
    _WsOnDemandTriggerGlobalStatusBuildingNumber_Type()
)
wsOnDemandTriggerGlobalStatusBuildingNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsOnDemandTriggerGlobalStatusBuildingNumber.setStatus("current")


class _WsOnDemandTriggerGlobalStatusFloorNumber_Type(Unsigned32):
    """Custom type wsOnDemandTriggerGlobalStatusFloorNumber based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_WsOnDemandTriggerGlobalStatusFloorNumber_Type.__name__ = "Unsigned32"
_WsOnDemandTriggerGlobalStatusFloorNumber_Object = MibScalar
wsOnDemandTriggerGlobalStatusFloorNumber = _WsOnDemandTriggerGlobalStatusFloorNumber_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 20, 5, 4),
    _WsOnDemandTriggerGlobalStatusFloorNumber_Type()
)
wsOnDemandTriggerGlobalStatusFloorNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsOnDemandTriggerGlobalStatusFloorNumber.setStatus("current")


class _WsOnDemandTriggerGlobalStatusUsedRadios_Type(Integer32):
    """Custom type wsOnDemandTriggerGlobalStatusUsedRadios based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sentry", 1),
          ("sentryAndOperational", 2))
    )


_WsOnDemandTriggerGlobalStatusUsedRadios_Type.__name__ = "Integer32"
_WsOnDemandTriggerGlobalStatusUsedRadios_Object = MibScalar
wsOnDemandTriggerGlobalStatusUsedRadios = _WsOnDemandTriggerGlobalStatusUsedRadios_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 20, 5, 5),
    _WsOnDemandTriggerGlobalStatusUsedRadios_Type()
)
wsOnDemandTriggerGlobalStatusUsedRadios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsOnDemandTriggerGlobalStatusUsedRadios.setStatus("current")


class _WsOnDemandTriggerGlobalStatusCurrentStatus_Type(Integer32):
    """Custom type wsOnDemandTriggerGlobalStatusCurrentStatus based on Integer32"""
    defaultValue = 1

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
        *(("notStarted", 1),
          ("inProgress", 2),
          ("deviceLocated", 3),
          ("deviceNotLocated", 4),
          ("noAPsAvailable", 5))
    )


_WsOnDemandTriggerGlobalStatusCurrentStatus_Type.__name__ = "Integer32"
_WsOnDemandTriggerGlobalStatusCurrentStatus_Object = MibScalar
wsOnDemandTriggerGlobalStatusCurrentStatus = _WsOnDemandTriggerGlobalStatusCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 20, 5, 6),
    _WsOnDemandTriggerGlobalStatusCurrentStatus_Type()
)
wsOnDemandTriggerGlobalStatusCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsOnDemandTriggerGlobalStatusCurrentStatus.setStatus("current")
_WsOnDemandTriggerGlobalStatusSearchTime_Type = TimeTicks
_WsOnDemandTriggerGlobalStatusSearchTime_Object = MibScalar
wsOnDemandTriggerGlobalStatusSearchTime = _WsOnDemandTriggerGlobalStatusSearchTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 20, 5, 7),
    _WsOnDemandTriggerGlobalStatusSearchTime_Type()
)
wsOnDemandTriggerGlobalStatusSearchTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsOnDemandTriggerGlobalStatusSearchTime.setStatus("current")


class _WsOnDemandTriggerGlobalStatusNumOfLocatorAPs_Type(Unsigned32):
    """Custom type wsOnDemandTriggerGlobalStatusNumOfLocatorAPs based on Unsigned32"""
    defaultValue = 0


_WsOnDemandTriggerGlobalStatusNumOfLocatorAPs_Type.__name__ = "Unsigned32"
_WsOnDemandTriggerGlobalStatusNumOfLocatorAPs_Object = MibScalar
wsOnDemandTriggerGlobalStatusNumOfLocatorAPs = _WsOnDemandTriggerGlobalStatusNumOfLocatorAPs_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 20, 5, 8),
    _WsOnDemandTriggerGlobalStatusNumOfLocatorAPs_Type()
)
wsOnDemandTriggerGlobalStatusNumOfLocatorAPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsOnDemandTriggerGlobalStatusNumOfLocatorAPs.setStatus("current")


class _WsOnDemandTriggerGlobalStatusNumOfDetectedAPs_Type(Unsigned32):
    """Custom type wsOnDemandTriggerGlobalStatusNumOfDetectedAPs based on Unsigned32"""
    defaultValue = 0


_WsOnDemandTriggerGlobalStatusNumOfDetectedAPs_Type.__name__ = "Unsigned32"
_WsOnDemandTriggerGlobalStatusNumOfDetectedAPs_Object = MibScalar
wsOnDemandTriggerGlobalStatusNumOfDetectedAPs = _WsOnDemandTriggerGlobalStatusNumOfDetectedAPs_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 20, 5, 9),
    _WsOnDemandTriggerGlobalStatusNumOfDetectedAPs_Type()
)
wsOnDemandTriggerGlobalStatusNumOfDetectedAPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsOnDemandTriggerGlobalStatusNumOfDetectedAPs.setStatus("current")


class _WsOnDemandTriggerGlobalStatusNumOfDetectedBuildings_Type(Unsigned32):
    """Custom type wsOnDemandTriggerGlobalStatusNumOfDetectedBuildings based on Unsigned32"""
    defaultValue = 0


_WsOnDemandTriggerGlobalStatusNumOfDetectedBuildings_Type.__name__ = "Unsigned32"
_WsOnDemandTriggerGlobalStatusNumOfDetectedBuildings_Object = MibScalar
wsOnDemandTriggerGlobalStatusNumOfDetectedBuildings = _WsOnDemandTriggerGlobalStatusNumOfDetectedBuildings_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 20, 5, 10),
    _WsOnDemandTriggerGlobalStatusNumOfDetectedBuildings_Type()
)
wsOnDemandTriggerGlobalStatusNumOfDetectedBuildings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsOnDemandTriggerGlobalStatusNumOfDetectedBuildings.setStatus("current")


class _WsOnDemandTriggerGlobalStatusNumOfDetectedFloors_Type(Unsigned32):
    """Custom type wsOnDemandTriggerGlobalStatusNumOfDetectedFloors based on Unsigned32"""
    defaultValue = 0


_WsOnDemandTriggerGlobalStatusNumOfDetectedFloors_Type.__name__ = "Unsigned32"
_WsOnDemandTriggerGlobalStatusNumOfDetectedFloors_Object = MibScalar
wsOnDemandTriggerGlobalStatusNumOfDetectedFloors = _WsOnDemandTriggerGlobalStatusNumOfDetectedFloors_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 20, 5, 11),
    _WsOnDemandTriggerGlobalStatusNumOfDetectedFloors_Type()
)
wsOnDemandTriggerGlobalStatusNumOfDetectedFloors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsOnDemandTriggerGlobalStatusNumOfDetectedFloors.setStatus("current")


class _WsOnDemandTriggerGlobalStatusHighestSignalFoundBuilding_Type(Unsigned32):
    """Custom type wsOnDemandTriggerGlobalStatusHighestSignalFoundBuilding based on Unsigned32"""
    defaultValue = 0


_WsOnDemandTriggerGlobalStatusHighestSignalFoundBuilding_Type.__name__ = "Unsigned32"
_WsOnDemandTriggerGlobalStatusHighestSignalFoundBuilding_Object = MibScalar
wsOnDemandTriggerGlobalStatusHighestSignalFoundBuilding = _WsOnDemandTriggerGlobalStatusHighestSignalFoundBuilding_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 20, 5, 12),
    _WsOnDemandTriggerGlobalStatusHighestSignalFoundBuilding_Type()
)
wsOnDemandTriggerGlobalStatusHighestSignalFoundBuilding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsOnDemandTriggerGlobalStatusHighestSignalFoundBuilding.setStatus("current")


class _WsOnDemandTriggerGlobalStatusHighestSignalFoundFloor_Type(Unsigned32):
    """Custom type wsOnDemandTriggerGlobalStatusHighestSignalFoundFloor based on Unsigned32"""
    defaultValue = 0


_WsOnDemandTriggerGlobalStatusHighestSignalFoundFloor_Type.__name__ = "Unsigned32"
_WsOnDemandTriggerGlobalStatusHighestSignalFoundFloor_Object = MibScalar
wsOnDemandTriggerGlobalStatusHighestSignalFoundFloor = _WsOnDemandTriggerGlobalStatusHighestSignalFoundFloor_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 20, 5, 13),
    _WsOnDemandTriggerGlobalStatusHighestSignalFoundFloor_Type()
)
wsOnDemandTriggerGlobalStatusHighestSignalFoundFloor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsOnDemandTriggerGlobalStatusHighestSignalFoundFloor.setStatus("current")
_WsOnDemandTriggerFloorStatus_ObjectIdentity = ObjectIdentity
wsOnDemandTriggerFloorStatus = _WsOnDemandTriggerFloorStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 20, 6)
)
_WsOnDemandTriggerFloorStatusTable_Object = MibTable
wsOnDemandTriggerFloorStatusTable = _WsOnDemandTriggerFloorStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 20, 6, 1)
)
if mibBuilder.loadTexts:
    wsOnDemandTriggerFloorStatusTable.setStatus("current")
_WsOnDemandTriggerFloorStatusEntry_Object = MibTableRow
wsOnDemandTriggerFloorStatusEntry = _WsOnDemandTriggerFloorStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 20, 6, 1, 1)
)
wsOnDemandTriggerFloorStatusEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsOnDemandTriggerFloorStatusBuildingNum"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsOnDemandTriggerFloorStatusFloorNum"),
)
if mibBuilder.loadTexts:
    wsOnDemandTriggerFloorStatusEntry.setStatus("current")
_WsOnDemandTriggerFloorStatusBuildingNum_Type = Unsigned32
_WsOnDemandTriggerFloorStatusBuildingNum_Object = MibTableColumn
wsOnDemandTriggerFloorStatusBuildingNum = _WsOnDemandTriggerFloorStatusBuildingNum_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 20, 6, 1, 1, 1),
    _WsOnDemandTriggerFloorStatusBuildingNum_Type()
)
wsOnDemandTriggerFloorStatusBuildingNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsOnDemandTriggerFloorStatusBuildingNum.setStatus("current")
_WsOnDemandTriggerFloorStatusFloorNum_Type = Unsigned32
_WsOnDemandTriggerFloorStatusFloorNum_Object = MibTableColumn
wsOnDemandTriggerFloorStatusFloorNum = _WsOnDemandTriggerFloorStatusFloorNum_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 20, 6, 1, 1, 2),
    _WsOnDemandTriggerFloorStatusFloorNum_Type()
)
wsOnDemandTriggerFloorStatusFloorNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsOnDemandTriggerFloorStatusFloorNum.setStatus("current")


class _WsOnDemandTriggerFloorStatusDeviceFound_Type(Integer32):
    """Custom type wsOnDemandTriggerFloorStatusDeviceFound based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notFound", 1),
          ("found", 2))
    )


_WsOnDemandTriggerFloorStatusDeviceFound_Type.__name__ = "Integer32"
_WsOnDemandTriggerFloorStatusDeviceFound_Object = MibTableColumn
wsOnDemandTriggerFloorStatusDeviceFound = _WsOnDemandTriggerFloorStatusDeviceFound_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 20, 6, 1, 1, 3),
    _WsOnDemandTriggerFloorStatusDeviceFound_Type()
)
wsOnDemandTriggerFloorStatusDeviceFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsOnDemandTriggerFloorStatusDeviceFound.setStatus("current")
_WsOnDemandTriggerFloorStatusNumOfAPs_Type = Unsigned32
_WsOnDemandTriggerFloorStatusNumOfAPs_Object = MibTableColumn
wsOnDemandTriggerFloorStatusNumOfAPs = _WsOnDemandTriggerFloorStatusNumOfAPs_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 20, 6, 1, 1, 4),
    _WsOnDemandTriggerFloorStatusNumOfAPs_Type()
)
wsOnDemandTriggerFloorStatusNumOfAPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsOnDemandTriggerFloorStatusNumOfAPs.setStatus("current")


class _WsOnDemandTriggerFloorStatusSolutionType_Type(Integer32):
    """Custom type wsOnDemandTriggerFloorStatusSolutionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noSolution", 1),
          ("circle", 2),
          ("point", 3))
    )


_WsOnDemandTriggerFloorStatusSolutionType_Type.__name__ = "Integer32"
_WsOnDemandTriggerFloorStatusSolutionType_Object = MibTableColumn
wsOnDemandTriggerFloorStatusSolutionType = _WsOnDemandTriggerFloorStatusSolutionType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 20, 6, 1, 1, 5),
    _WsOnDemandTriggerFloorStatusSolutionType_Type()
)
wsOnDemandTriggerFloorStatusSolutionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsOnDemandTriggerFloorStatusSolutionType.setStatus("current")
_WsOnDemandTriggerFloorStatusXCoordinate_Type = Integer32
_WsOnDemandTriggerFloorStatusXCoordinate_Object = MibTableColumn
wsOnDemandTriggerFloorStatusXCoordinate = _WsOnDemandTriggerFloorStatusXCoordinate_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 20, 6, 1, 1, 6),
    _WsOnDemandTriggerFloorStatusXCoordinate_Type()
)
wsOnDemandTriggerFloorStatusXCoordinate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsOnDemandTriggerFloorStatusXCoordinate.setStatus("current")
_WsOnDemandTriggerFloorStatusYCoordinate_Type = Integer32
_WsOnDemandTriggerFloorStatusYCoordinate_Object = MibTableColumn
wsOnDemandTriggerFloorStatusYCoordinate = _WsOnDemandTriggerFloorStatusYCoordinate_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 20, 6, 1, 1, 7),
    _WsOnDemandTriggerFloorStatusYCoordinate_Type()
)
wsOnDemandTriggerFloorStatusYCoordinate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsOnDemandTriggerFloorStatusYCoordinate.setStatus("current")
_WsOnDemandTriggerFloorStatusCircleRadius_Type = Unsigned32
_WsOnDemandTriggerFloorStatusCircleRadius_Object = MibTableColumn
wsOnDemandTriggerFloorStatusCircleRadius = _WsOnDemandTriggerFloorStatusCircleRadius_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 20, 6, 1, 1, 8),
    _WsOnDemandTriggerFloorStatusCircleRadius_Type()
)
wsOnDemandTriggerFloorStatusCircleRadius.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsOnDemandTriggerFloorStatusCircleRadius.setStatus("current")
_WsOnDemandTriggerFloorStatusSigma_Type = Integer32
_WsOnDemandTriggerFloorStatusSigma_Object = MibTableColumn
wsOnDemandTriggerFloorStatusSigma = _WsOnDemandTriggerFloorStatusSigma_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 20, 6, 1, 1, 9),
    _WsOnDemandTriggerFloorStatusSigma_Type()
)
wsOnDemandTriggerFloorStatusSigma.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsOnDemandTriggerFloorStatusSigma.setStatus("current")
_WsTriangulationLocStatusTable_Object = MibTable
wsTriangulationLocStatusTable = _WsTriangulationLocStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 20, 7)
)
if mibBuilder.loadTexts:
    wsTriangulationLocStatusTable.setStatus("current")
_WsTriangulationLocStatusEntry_Object = MibTableRow
wsTriangulationLocStatusEntry = _WsTriangulationLocStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 20, 7, 1)
)
wsTriangulationLocStatusEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsTriangLocMacAddress"),
)
if mibBuilder.loadTexts:
    wsTriangulationLocStatusEntry.setStatus("current")
_WsTriangLocMacAddress_Type = MacAddress
_WsTriangLocMacAddress_Object = MibTableColumn
wsTriangLocMacAddress = _WsTriangLocMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 20, 7, 1, 1),
    _WsTriangLocMacAddress_Type()
)
wsTriangLocMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsTriangLocMacAddress.setStatus("current")


class _WsTriangLocDataType_Type(Integer32):
    """Custom type wsTriangLocDataType based on Integer32"""
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


_WsTriangLocDataType_Type.__name__ = "Integer32"
_WsTriangLocDataType_Object = MibTableColumn
wsTriangLocDataType = _WsTriangLocDataType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 20, 7, 1, 2),
    _WsTriangLocDataType_Type()
)
wsTriangLocDataType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsTriangLocDataType.setStatus("current")


class _WsTriangLocStatus_Type(Integer32):
    """Custom type wsTriangLocStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not-executed", 1),
          ("success", 2),
          ("failure", 3))
    )


_WsTriangLocStatus_Type.__name__ = "Integer32"
_WsTriangLocStatus_Object = MibTableColumn
wsTriangLocStatus = _WsTriangLocStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 20, 7, 1, 3),
    _WsTriangLocStatus_Type()
)
wsTriangLocStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsTriangLocStatus.setStatus("current")


class _WsTriangLocDeviceType_Type(Integer32):
    """Custom type wsTriangLocDeviceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ap", 1),
          ("client", 2))
    )


_WsTriangLocDeviceType_Type.__name__ = "Integer32"
_WsTriangLocDeviceType_Object = MibTableColumn
wsTriangLocDeviceType = _WsTriangLocDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 20, 7, 1, 4),
    _WsTriangLocDeviceType_Type()
)
wsTriangLocDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsTriangLocDeviceType.setStatus("current")
_WsTriangLocAge_Type = TimeTicks
_WsTriangLocAge_Object = MibTableColumn
wsTriangLocAge = _WsTriangLocAge_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 20, 7, 1, 5),
    _WsTriangLocAge_Type()
)
wsTriangLocAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsTriangLocAge.setStatus("current")


class _WsTriangLocBldng_Type(Integer32):
    """Custom type wsTriangLocBldng based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_WsTriangLocBldng_Type.__name__ = "Integer32"
_WsTriangLocBldng_Object = MibTableColumn
wsTriangLocBldng = _WsTriangLocBldng_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 20, 7, 1, 6),
    _WsTriangLocBldng_Type()
)
wsTriangLocBldng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsTriangLocBldng.setStatus("current")


class _WsTriangLocFlr_Type(Integer32):
    """Custom type wsTriangLocFlr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_WsTriangLocFlr_Type.__name__ = "Integer32"
_WsTriangLocFlr_Object = MibTableColumn
wsTriangLocFlr = _WsTriangLocFlr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 20, 7, 1, 7),
    _WsTriangLocFlr_Type()
)
wsTriangLocFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsTriangLocFlr.setStatus("current")


class _WsTriangLocXCoord_Type(Integer32):
    """Custom type wsTriangLocXCoord based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-3000, 3000),
    )


_WsTriangLocXCoord_Type.__name__ = "Integer32"
_WsTriangLocXCoord_Object = MibTableColumn
wsTriangLocXCoord = _WsTriangLocXCoord_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 20, 7, 1, 8),
    _WsTriangLocXCoord_Type()
)
wsTriangLocXCoord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsTriangLocXCoord.setStatus("current")


class _WsTriangLocYCoord_Type(Integer32):
    """Custom type wsTriangLocYCoord based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-3000, 3000),
    )


_WsTriangLocYCoord_Type.__name__ = "Integer32"
_WsTriangLocYCoord_Object = MibTableColumn
wsTriangLocYCoord = _WsTriangLocYCoord_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 20, 7, 1, 9),
    _WsTriangLocYCoord_Type()
)
wsTriangLocYCoord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsTriangLocYCoord.setStatus("current")
_AuthenticatedClient_ObjectIdentity = ObjectIdentity
authenticatedClient = _AuthenticatedClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21)
)
_WsAuthenticatedClientStatusTable_Object = MibTable
wsAuthenticatedClientStatusTable = _WsAuthenticatedClientStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 1)
)
if mibBuilder.loadTexts:
    wsAuthenticatedClientStatusTable.setStatus("current")
_WsAuthenticatedClientStatusEntry_Object = MibTableRow
wsAuthenticatedClientStatusEntry = _WsAuthenticatedClientStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 1, 1)
)
wsAuthenticatedClientStatusEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsAuthenticatedClientMacAddress"),
)
if mibBuilder.loadTexts:
    wsAuthenticatedClientStatusEntry.setStatus("current")
_WsAuthenticatedClientMacAddress_Type = MacAddress
_WsAuthenticatedClientMacAddress_Object = MibTableColumn
wsAuthenticatedClientMacAddress = _WsAuthenticatedClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 1, 1, 1),
    _WsAuthenticatedClientMacAddress_Type()
)
wsAuthenticatedClientMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAuthenticatedClientMacAddress.setStatus("current")
_WsAuthenticatedClientTunnelIpAddress_Type = IpAddress
_WsAuthenticatedClientTunnelIpAddress_Object = MibTableColumn
wsAuthenticatedClientTunnelIpAddress = _WsAuthenticatedClientTunnelIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 1, 1, 2),
    _WsAuthenticatedClientTunnelIpAddress_Type()
)
wsAuthenticatedClientTunnelIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAuthenticatedClientTunnelIpAddress.setStatus("current")


class _WsAuthenticatedClientUserName_Type(DisplayString):
    """Custom type wsAuthenticatedClientUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WsAuthenticatedClientUserName_Type.__name__ = "DisplayString"
_WsAuthenticatedClientUserName_Object = MibTableColumn
wsAuthenticatedClientUserName = _WsAuthenticatedClientUserName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 1, 1, 3),
    _WsAuthenticatedClientUserName_Type()
)
wsAuthenticatedClientUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAuthenticatedClientUserName.setStatus("current")


class _WsAuthenticatedClientSSID_Type(DisplayString):
    """Custom type wsAuthenticatedClientSSID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WsAuthenticatedClientSSID_Type.__name__ = "DisplayString"
_WsAuthenticatedClientSSID_Object = MibTableColumn
wsAuthenticatedClientSSID = _WsAuthenticatedClientSSID_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 1, 1, 4),
    _WsAuthenticatedClientSSID_Type()
)
wsAuthenticatedClientSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAuthenticatedClientSSID.setStatus("current")


class _WsAuthenticatedClientVLAN_Type(Integer32):
    """Custom type wsAuthenticatedClientVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WsAuthenticatedClientVLAN_Type.__name__ = "Integer32"
_WsAuthenticatedClientVLAN_Object = MibTableColumn
wsAuthenticatedClientVLAN = _WsAuthenticatedClientVLAN_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 1, 1, 5),
    _WsAuthenticatedClientVLAN_Type()
)
wsAuthenticatedClientVLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAuthenticatedClientVLAN.setStatus("current")


class _WsAuthenticatedClientStatus_Type(Integer32):
    """Custom type wsAuthenticatedClientStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("authenticated", 1),
          ("associated", 2),
          ("disassociated", 3))
    )


_WsAuthenticatedClientStatus_Type.__name__ = "Integer32"
_WsAuthenticatedClientStatus_Object = MibTableColumn
wsAuthenticatedClientStatus = _WsAuthenticatedClientStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 1, 1, 6),
    _WsAuthenticatedClientStatus_Type()
)
wsAuthenticatedClientStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAuthenticatedClientStatus.setStatus("current")


class _WsAuthenticatedClientTxDataRate_Type(Integer32):
    """Custom type wsAuthenticatedClientTxDataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 1200),
    )


_WsAuthenticatedClientTxDataRate_Type.__name__ = "Integer32"
_WsAuthenticatedClientTxDataRate_Object = MibTableColumn
wsAuthenticatedClientTxDataRate = _WsAuthenticatedClientTxDataRate_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 1, 1, 7),
    _WsAuthenticatedClientTxDataRate_Type()
)
wsAuthenticatedClientTxDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAuthenticatedClientTxDataRate.setStatus("current")
_WsAuthenticatedClientInactivePeriod_Type = TimeTicks
_WsAuthenticatedClientInactivePeriod_Object = MibTableColumn
wsAuthenticatedClientInactivePeriod = _WsAuthenticatedClientInactivePeriod_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 1, 1, 8),
    _WsAuthenticatedClientInactivePeriod_Type()
)
wsAuthenticatedClientInactivePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAuthenticatedClientInactivePeriod.setStatus("current")


class _WsAuthenticatedClientDisassociateAction_Type(Integer32):
    """Custom type wsAuthenticatedClientDisassociateAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("start", 2))
    )


_WsAuthenticatedClientDisassociateAction_Type.__name__ = "Integer32"
_WsAuthenticatedClientDisassociateAction_Object = MibTableColumn
wsAuthenticatedClientDisassociateAction = _WsAuthenticatedClientDisassociateAction_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 1, 1, 9),
    _WsAuthenticatedClientDisassociateAction_Type()
)
wsAuthenticatedClientDisassociateAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAuthenticatedClientDisassociateAction.setStatus("current")
_WsAuthenticatedClientAge_Type = TimeTicks
_WsAuthenticatedClientAge_Object = MibTableColumn
wsAuthenticatedClientAge = _WsAuthenticatedClientAge_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 1, 1, 10),
    _WsAuthenticatedClientAge_Type()
)
wsAuthenticatedClientAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAuthenticatedClientAge.setStatus("current")


class _WsAuthenticatedClientAssociatingSwitch_Type(Integer32):
    """Custom type wsAuthenticatedClientAssociatingSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local-switch", 1),
          ("peer-switch", 2))
    )


_WsAuthenticatedClientAssociatingSwitch_Type.__name__ = "Integer32"
_WsAuthenticatedClientAssociatingSwitch_Object = MibTableColumn
wsAuthenticatedClientAssociatingSwitch = _WsAuthenticatedClientAssociatingSwitch_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 1, 1, 11),
    _WsAuthenticatedClientAssociatingSwitch_Type()
)
wsAuthenticatedClientAssociatingSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAuthenticatedClientAssociatingSwitch.setStatus("current")
_WsAuthenticatedClientSwitchMacAddress_Type = MacAddress
_WsAuthenticatedClientSwitchMacAddress_Object = MibTableColumn
wsAuthenticatedClientSwitchMacAddress = _WsAuthenticatedClientSwitchMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 1, 1, 12),
    _WsAuthenticatedClientSwitchMacAddress_Type()
)
wsAuthenticatedClientSwitchMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAuthenticatedClientSwitchMacAddress.setStatus("current")
_WsAuthenticatedClientSwitchIpAddress_Type = IpAddress
_WsAuthenticatedClientSwitchIpAddress_Object = MibTableColumn
wsAuthenticatedClientSwitchIpAddress = _WsAuthenticatedClientSwitchIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 1, 1, 13),
    _WsAuthenticatedClientSwitchIpAddress_Type()
)
wsAuthenticatedClientSwitchIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAuthenticatedClientSwitchIpAddress.setStatus("current")


class _WsAuthenticatedClientDot11nCapable_Type(Integer32):
    """Custom type wsAuthenticatedClientDot11nCapable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_WsAuthenticatedClientDot11nCapable_Type.__name__ = "Integer32"
_WsAuthenticatedClientDot11nCapable_Object = MibTableColumn
wsAuthenticatedClientDot11nCapable = _WsAuthenticatedClientDot11nCapable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 1, 1, 14),
    _WsAuthenticatedClientDot11nCapable_Type()
)
wsAuthenticatedClientDot11nCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAuthenticatedClientDot11nCapable.setStatus("current")


class _WsAuthenticatedClientStbcCapable_Type(Integer32):
    """Custom type wsAuthenticatedClientStbcCapable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_WsAuthenticatedClientStbcCapable_Type.__name__ = "Integer32"
_WsAuthenticatedClientStbcCapable_Object = MibTableColumn
wsAuthenticatedClientStbcCapable = _WsAuthenticatedClientStbcCapable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 1, 1, 15),
    _WsAuthenticatedClientStbcCapable_Type()
)
wsAuthenticatedClientStbcCapable.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAuthenticatedClientStbcCapable.setStatus("current")


class _WsAuthenticatedClientDistTunnelStatus_Type(Integer32):
    """Custom type wsAuthenticatedClientDistTunnelStatus based on Integer32"""
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


_WsAuthenticatedClientDistTunnelStatus_Type.__name__ = "Integer32"
_WsAuthenticatedClientDistTunnelStatus_Object = MibTableColumn
wsAuthenticatedClientDistTunnelStatus = _WsAuthenticatedClientDistTunnelStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 1, 1, 16),
    _WsAuthenticatedClientDistTunnelStatus_Type()
)
wsAuthenticatedClientDistTunnelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAuthenticatedClientDistTunnelStatus.setStatus("current")


class _WsAuthenticatedClientDistTunnelRoamStatus_Type(Integer32):
    """Custom type wsAuthenticatedClientDistTunnelRoamStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("associated", 0),
          ("home", 1))
    )


_WsAuthenticatedClientDistTunnelRoamStatus_Type.__name__ = "Integer32"
_WsAuthenticatedClientDistTunnelRoamStatus_Object = MibTableColumn
wsAuthenticatedClientDistTunnelRoamStatus = _WsAuthenticatedClientDistTunnelRoamStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 1, 1, 17),
    _WsAuthenticatedClientDistTunnelRoamStatus_Type()
)
wsAuthenticatedClientDistTunnelRoamStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAuthenticatedClientDistTunnelRoamStatus.setStatus("current")
_WsAuthenticatedClientDistTunnelHomeAPMac_Type = MacAddress
_WsAuthenticatedClientDistTunnelHomeAPMac_Object = MibTableColumn
wsAuthenticatedClientDistTunnelHomeAPMac = _WsAuthenticatedClientDistTunnelHomeAPMac_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 1, 1, 18),
    _WsAuthenticatedClientDistTunnelHomeAPMac_Type()
)
wsAuthenticatedClientDistTunnelHomeAPMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAuthenticatedClientDistTunnelHomeAPMac.setStatus("current")
_WsAuthenticatedClientDistTunnelAssocAPMac_Type = MacAddress
_WsAuthenticatedClientDistTunnelAssocAPMac_Object = MibTableColumn
wsAuthenticatedClientDistTunnelAssocAPMac = _WsAuthenticatedClientDistTunnelAssocAPMac_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 1, 1, 19),
    _WsAuthenticatedClientDistTunnelAssocAPMac_Type()
)
wsAuthenticatedClientDistTunnelAssocAPMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAuthenticatedClientDistTunnelAssocAPMac.setStatus("current")
_WsAuthenticatedClientAPMacAddress_Type = MacAddress
_WsAuthenticatedClientAPMacAddress_Object = MibTableColumn
wsAuthenticatedClientAPMacAddress = _WsAuthenticatedClientAPMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 1, 1, 20),
    _WsAuthenticatedClientAPMacAddress_Type()
)
wsAuthenticatedClientAPMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAuthenticatedClientAPMacAddress.setStatus("current")
_WsAuthenticatedClientBSSID_Type = MacAddress
_WsAuthenticatedClientBSSID_Object = MibTableColumn
wsAuthenticatedClientBSSID = _WsAuthenticatedClientBSSID_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 1, 1, 21),
    _WsAuthenticatedClientBSSID_Type()
)
wsAuthenticatedClientBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAuthenticatedClientBSSID.setStatus("current")


class _WsAuthenticatedClientRadioInterface_Type(Integer32):
    """Custom type wsAuthenticatedClientRadioInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WsAuthenticatedClientRadioInterface_Type.__name__ = "Integer32"
_WsAuthenticatedClientRadioInterface_Object = MibTableColumn
wsAuthenticatedClientRadioInterface = _WsAuthenticatedClientRadioInterface_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 1, 1, 22),
    _WsAuthenticatedClientRadioInterface_Type()
)
wsAuthenticatedClientRadioInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAuthenticatedClientRadioInterface.setStatus("current")


class _WsAuthenticatedClientChannel_Type(Integer32):
    """Custom type wsAuthenticatedClientChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 165),
    )


_WsAuthenticatedClientChannel_Type.__name__ = "Integer32"
_WsAuthenticatedClientChannel_Object = MibTableColumn
wsAuthenticatedClientChannel = _WsAuthenticatedClientChannel_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 1, 1, 23),
    _WsAuthenticatedClientChannel_Type()
)
wsAuthenticatedClientChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAuthenticatedClientChannel.setStatus("current")
_WsAuthenticatedClientNwTime_Type = TimeTicks
_WsAuthenticatedClientNwTime_Object = MibTableColumn
wsAuthenticatedClientNwTime = _WsAuthenticatedClientNwTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 1, 1, 24),
    _WsAuthenticatedClientNwTime_Type()
)
wsAuthenticatedClientNwTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAuthenticatedClientNwTime.setStatus("current")
_WsAuthenticatedClientIpAddress_Type = IpAddress
_WsAuthenticatedClientIpAddress_Object = MibTableColumn
wsAuthenticatedClientIpAddress = _WsAuthenticatedClientIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 1, 1, 25),
    _WsAuthenticatedClientIpAddress_Type()
)
wsAuthenticatedClientIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAuthenticatedClientIpAddress.setStatus("current")


class _WsAuthenticatedClientNetBiosName_Type(DisplayString):
    """Custom type wsAuthenticatedClientNetBiosName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_WsAuthenticatedClientNetBiosName_Type.__name__ = "DisplayString"
_WsAuthenticatedClientNetBiosName_Object = MibTableColumn
wsAuthenticatedClientNetBiosName = _WsAuthenticatedClientNetBiosName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 1, 1, 26),
    _WsAuthenticatedClientNetBiosName_Type()
)
wsAuthenticatedClientNetBiosName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAuthenticatedClientNetBiosName.setStatus("current")


class _WsAuthenticatedClientRRMSupported_Type(Integer32):
    """Custom type wsAuthenticatedClientRRMSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("supported", 2),
          ("unsupported", 3))
    )


_WsAuthenticatedClientRRMSupported_Type.__name__ = "Integer32"
_WsAuthenticatedClientRRMSupported_Object = MibTableColumn
wsAuthenticatedClientRRMSupported = _WsAuthenticatedClientRRMSupported_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 1, 1, 27),
    _WsAuthenticatedClientRRMSupported_Type()
)
wsAuthenticatedClientRRMSupported.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAuthenticatedClientRRMSupported.setStatus("current")


class _WsAuthenticatedClientRRMLocationReportSupported_Type(Integer32):
    """Custom type wsAuthenticatedClientRRMLocationReportSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("supported", 1),
          ("unsupported", 2))
    )


_WsAuthenticatedClientRRMLocationReportSupported_Type.__name__ = "Integer32"
_WsAuthenticatedClientRRMLocationReportSupported_Object = MibTableColumn
wsAuthenticatedClientRRMLocationReportSupported = _WsAuthenticatedClientRRMLocationReportSupported_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 1, 1, 28),
    _WsAuthenticatedClientRRMLocationReportSupported_Type()
)
wsAuthenticatedClientRRMLocationReportSupported.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAuthenticatedClientRRMLocationReportSupported.setStatus("current")


class _WsAuthenticatedClientRRMBeaconTableMeasurementSupported_Type(Integer32):
    """Custom type wsAuthenticatedClientRRMBeaconTableMeasurementSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("supported", 1),
          ("unsupported", 2))
    )


_WsAuthenticatedClientRRMBeaconTableMeasurementSupported_Type.__name__ = "Integer32"
_WsAuthenticatedClientRRMBeaconTableMeasurementSupported_Object = MibTableColumn
wsAuthenticatedClientRRMBeaconTableMeasurementSupported = _WsAuthenticatedClientRRMBeaconTableMeasurementSupported_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 1, 1, 29),
    _WsAuthenticatedClientRRMBeaconTableMeasurementSupported_Type()
)
wsAuthenticatedClientRRMBeaconTableMeasurementSupported.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAuthenticatedClientRRMBeaconTableMeasurementSupported.setStatus("current")


class _WsAuthenticatedClientRRMBeaconActiveMeasurementSupported_Type(Integer32):
    """Custom type wsAuthenticatedClientRRMBeaconActiveMeasurementSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("supported", 1),
          ("unsupported", 2))
    )


_WsAuthenticatedClientRRMBeaconActiveMeasurementSupported_Type.__name__ = "Integer32"
_WsAuthenticatedClientRRMBeaconActiveMeasurementSupported_Object = MibTableColumn
wsAuthenticatedClientRRMBeaconActiveMeasurementSupported = _WsAuthenticatedClientRRMBeaconActiveMeasurementSupported_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 1, 1, 30),
    _WsAuthenticatedClientRRMBeaconActiveMeasurementSupported_Type()
)
wsAuthenticatedClientRRMBeaconActiveMeasurementSupported.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAuthenticatedClientRRMBeaconActiveMeasurementSupported.setStatus("current")


class _WsAuthenticatedClientRRMBeaconPassiveMeasurementSupported_Type(Integer32):
    """Custom type wsAuthenticatedClientRRMBeaconPassiveMeasurementSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("supported", 1),
          ("unsupported", 2))
    )


_WsAuthenticatedClientRRMBeaconPassiveMeasurementSupported_Type.__name__ = "Integer32"
_WsAuthenticatedClientRRMBeaconPassiveMeasurementSupported_Object = MibTableColumn
wsAuthenticatedClientRRMBeaconPassiveMeasurementSupported = _WsAuthenticatedClientRRMBeaconPassiveMeasurementSupported_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 1, 1, 31),
    _WsAuthenticatedClientRRMBeaconPassiveMeasurementSupported_Type()
)
wsAuthenticatedClientRRMBeaconPassiveMeasurementSupported.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAuthenticatedClientRRMBeaconPassiveMeasurementSupported.setStatus("current")


class _WsAuthenticatedClientRRMChannelLoadMeasurementSupported_Type(Integer32):
    """Custom type wsAuthenticatedClientRRMChannelLoadMeasurementSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("supported", 1),
          ("unsupported", 2))
    )


_WsAuthenticatedClientRRMChannelLoadMeasurementSupported_Type.__name__ = "Integer32"
_WsAuthenticatedClientRRMChannelLoadMeasurementSupported_Object = MibTableColumn
wsAuthenticatedClientRRMChannelLoadMeasurementSupported = _WsAuthenticatedClientRRMChannelLoadMeasurementSupported_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 1, 1, 32),
    _WsAuthenticatedClientRRMChannelLoadMeasurementSupported_Type()
)
wsAuthenticatedClientRRMChannelLoadMeasurementSupported.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAuthenticatedClientRRMChannelLoadMeasurementSupported.setStatus("current")


class _WsAuthenticatedClientDot11acCapable_Type(Integer32):
    """Custom type wsAuthenticatedClientDot11acCapable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_WsAuthenticatedClientDot11acCapable_Type.__name__ = "Integer32"
_WsAuthenticatedClientDot11acCapable_Object = MibTableColumn
wsAuthenticatedClientDot11acCapable = _WsAuthenticatedClientDot11acCapable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 1, 1, 33),
    _WsAuthenticatedClientDot11acCapable_Type()
)
wsAuthenticatedClientDot11acCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAuthenticatedClientDot11acCapable.setStatus("current")
_WsAuthenticatedClientStatisticsTable_Object = MibTable
wsAuthenticatedClientStatisticsTable = _WsAuthenticatedClientStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 2)
)
if mibBuilder.loadTexts:
    wsAuthenticatedClientStatisticsTable.setStatus("current")
_WsAuthenticatedClientStatisticsEntry_Object = MibTableRow
wsAuthenticatedClientStatisticsEntry = _WsAuthenticatedClientStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 2, 1)
)
if mibBuilder.loadTexts:
    wsAuthenticatedClientStatisticsEntry.setStatus("current")
_WsAuthenticatedClientPktsRecvd_Type = Counter64
_WsAuthenticatedClientPktsRecvd_Object = MibTableColumn
wsAuthenticatedClientPktsRecvd = _WsAuthenticatedClientPktsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 2, 1, 1),
    _WsAuthenticatedClientPktsRecvd_Type()
)
wsAuthenticatedClientPktsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAuthenticatedClientPktsRecvd.setStatus("current")
_WsAuthenticatedClientBytesRecvd_Type = Counter64
_WsAuthenticatedClientBytesRecvd_Object = MibTableColumn
wsAuthenticatedClientBytesRecvd = _WsAuthenticatedClientBytesRecvd_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 2, 1, 2),
    _WsAuthenticatedClientBytesRecvd_Type()
)
wsAuthenticatedClientBytesRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAuthenticatedClientBytesRecvd.setStatus("current")
_WsAuthenticatedClientPktsTransmitted_Type = Counter64
_WsAuthenticatedClientPktsTransmitted_Object = MibTableColumn
wsAuthenticatedClientPktsTransmitted = _WsAuthenticatedClientPktsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 2, 1, 3),
    _WsAuthenticatedClientPktsTransmitted_Type()
)
wsAuthenticatedClientPktsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAuthenticatedClientPktsTransmitted.setStatus("current")
_WsAuthenticatedClientBytesTransmitted_Type = Counter64
_WsAuthenticatedClientBytesTransmitted_Object = MibTableColumn
wsAuthenticatedClientBytesTransmitted = _WsAuthenticatedClientBytesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 2, 1, 4),
    _WsAuthenticatedClientBytesTransmitted_Type()
)
wsAuthenticatedClientBytesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAuthenticatedClientBytesTransmitted.setStatus("current")
_WsAuthenticatedClientDuplicatePktsRecvd_Type = Counter32
_WsAuthenticatedClientDuplicatePktsRecvd_Object = MibTableColumn
wsAuthenticatedClientDuplicatePktsRecvd = _WsAuthenticatedClientDuplicatePktsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 2, 1, 5),
    _WsAuthenticatedClientDuplicatePktsRecvd_Type()
)
wsAuthenticatedClientDuplicatePktsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAuthenticatedClientDuplicatePktsRecvd.setStatus("current")
_WsAuthenticatedClientFragmentedPktsRecvd_Type = Counter32
_WsAuthenticatedClientFragmentedPktsRecvd_Object = MibTableColumn
wsAuthenticatedClientFragmentedPktsRecvd = _WsAuthenticatedClientFragmentedPktsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 2, 1, 6),
    _WsAuthenticatedClientFragmentedPktsRecvd_Type()
)
wsAuthenticatedClientFragmentedPktsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAuthenticatedClientFragmentedPktsRecvd.setStatus("current")
_WsAuthenticatedClientFragmentedPktsTransmitted_Type = Counter32
_WsAuthenticatedClientFragmentedPktsTransmitted_Object = MibTableColumn
wsAuthenticatedClientFragmentedPktsTransmitted = _WsAuthenticatedClientFragmentedPktsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 2, 1, 7),
    _WsAuthenticatedClientFragmentedPktsTransmitted_Type()
)
wsAuthenticatedClientFragmentedPktsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAuthenticatedClientFragmentedPktsTransmitted.setStatus("current")
_WsAuthenticatedClientTransmitRetryCount_Type = Counter32
_WsAuthenticatedClientTransmitRetryCount_Object = MibTableColumn
wsAuthenticatedClientTransmitRetryCount = _WsAuthenticatedClientTransmitRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 2, 1, 8),
    _WsAuthenticatedClientTransmitRetryCount_Type()
)
wsAuthenticatedClientTransmitRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAuthenticatedClientTransmitRetryCount.setStatus("current")
_WsAuthenticatedClientTransmitRetryFailedCount_Type = Counter32
_WsAuthenticatedClientTransmitRetryFailedCount_Object = MibTableColumn
wsAuthenticatedClientTransmitRetryFailedCount = _WsAuthenticatedClientTransmitRetryFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 2, 1, 9),
    _WsAuthenticatedClientTransmitRetryFailedCount_Type()
)
wsAuthenticatedClientTransmitRetryFailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAuthenticatedClientTransmitRetryFailedCount.setStatus("current")
_WsAuthenticatedClientPktsRecvDropped_Type = Counter64
_WsAuthenticatedClientPktsRecvDropped_Object = MibTableColumn
wsAuthenticatedClientPktsRecvDropped = _WsAuthenticatedClientPktsRecvDropped_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 2, 1, 10),
    _WsAuthenticatedClientPktsRecvDropped_Type()
)
wsAuthenticatedClientPktsRecvDropped.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAuthenticatedClientPktsRecvDropped.setStatus("current")
_WsAuthenticatedClientBytesRecvDropped_Type = Counter64
_WsAuthenticatedClientBytesRecvDropped_Object = MibTableColumn
wsAuthenticatedClientBytesRecvDropped = _WsAuthenticatedClientBytesRecvDropped_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 2, 1, 11),
    _WsAuthenticatedClientBytesRecvDropped_Type()
)
wsAuthenticatedClientBytesRecvDropped.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAuthenticatedClientBytesRecvDropped.setStatus("current")
_WsAuthenticatedClientPktsTransmitDropped_Type = Counter64
_WsAuthenticatedClientPktsTransmitDropped_Object = MibTableColumn
wsAuthenticatedClientPktsTransmitDropped = _WsAuthenticatedClientPktsTransmitDropped_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 2, 1, 12),
    _WsAuthenticatedClientPktsTransmitDropped_Type()
)
wsAuthenticatedClientPktsTransmitDropped.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAuthenticatedClientPktsTransmitDropped.setStatus("current")
_WsAuthenticatedClientBytesTransmitDropped_Type = Counter64
_WsAuthenticatedClientBytesTransmitDropped_Object = MibTableColumn
wsAuthenticatedClientBytesTransmitDropped = _WsAuthenticatedClientBytesTransmitDropped_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 2, 1, 13),
    _WsAuthenticatedClientBytesTransmitDropped_Type()
)
wsAuthenticatedClientBytesTransmitDropped.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAuthenticatedClientBytesTransmitDropped.setStatus("current")
_WsAuthenticatedClientTsViolatePktsRecvd_Type = Counter32
_WsAuthenticatedClientTsViolatePktsRecvd_Object = MibTableColumn
wsAuthenticatedClientTsViolatePktsRecvd = _WsAuthenticatedClientTsViolatePktsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 2, 1, 14),
    _WsAuthenticatedClientTsViolatePktsRecvd_Type()
)
wsAuthenticatedClientTsViolatePktsRecvd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAuthenticatedClientTsViolatePktsRecvd.setStatus("current")
_WsAuthenticatedClientTsViolatePktsTransmitted_Type = Counter32
_WsAuthenticatedClientTsViolatePktsTransmitted_Object = MibTableColumn
wsAuthenticatedClientTsViolatePktsTransmitted = _WsAuthenticatedClientTsViolatePktsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 2, 1, 15),
    _WsAuthenticatedClientTsViolatePktsTransmitted_Type()
)
wsAuthenticatedClientTsViolatePktsTransmitted.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAuthenticatedClientTsViolatePktsTransmitted.setStatus("current")
_WsAuthenticatedClientNeighborManagedAPStatusTable_Object = MibTable
wsAuthenticatedClientNeighborManagedAPStatusTable = _WsAuthenticatedClientNeighborManagedAPStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 3)
)
if mibBuilder.loadTexts:
    wsAuthenticatedClientNeighborManagedAPStatusTable.setStatus("current")
_WsAuthenticatedClientNeighborManagedAPStatusEntry_Object = MibTableRow
wsAuthenticatedClientNeighborManagedAPStatusEntry = _WsAuthenticatedClientNeighborManagedAPStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 3, 1)
)
wsAuthenticatedClientNeighborManagedAPStatusEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsAuthenticatedClientStationMacAddress"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsAuthenticatedClientNeighborWSManagedAPMacAddress"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsAuthenticatedClientNeighborWSManagedAPRadioInterface"),
)
if mibBuilder.loadTexts:
    wsAuthenticatedClientNeighborManagedAPStatusEntry.setStatus("current")
_WsAuthenticatedClientStationMacAddress_Type = MacAddress
_WsAuthenticatedClientStationMacAddress_Object = MibTableColumn
wsAuthenticatedClientStationMacAddress = _WsAuthenticatedClientStationMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 3, 1, 1),
    _WsAuthenticatedClientStationMacAddress_Type()
)
wsAuthenticatedClientStationMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAuthenticatedClientStationMacAddress.setStatus("current")
_WsAuthenticatedClientNeighborWSManagedAPMacAddress_Type = MacAddress
_WsAuthenticatedClientNeighborWSManagedAPMacAddress_Object = MibTableColumn
wsAuthenticatedClientNeighborWSManagedAPMacAddress = _WsAuthenticatedClientNeighborWSManagedAPMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 3, 1, 2),
    _WsAuthenticatedClientNeighborWSManagedAPMacAddress_Type()
)
wsAuthenticatedClientNeighborWSManagedAPMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAuthenticatedClientNeighborWSManagedAPMacAddress.setStatus("current")


class _WsAuthenticatedClientNeighborWSManagedAPRadioInterface_Type(Integer32):
    """Custom type wsAuthenticatedClientNeighborWSManagedAPRadioInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WsAuthenticatedClientNeighborWSManagedAPRadioInterface_Type.__name__ = "Integer32"
_WsAuthenticatedClientNeighborWSManagedAPRadioInterface_Object = MibTableColumn
wsAuthenticatedClientNeighborWSManagedAPRadioInterface = _WsAuthenticatedClientNeighborWSManagedAPRadioInterface_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 3, 1, 3),
    _WsAuthenticatedClientNeighborWSManagedAPRadioInterface_Type()
)
wsAuthenticatedClientNeighborWSManagedAPRadioInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAuthenticatedClientNeighborWSManagedAPRadioInterface.setStatus("current")


class _WsAuthenticatedClientStationDiscoveryReason_Type(Bits):
    """Custom type wsAuthenticatedClientStationDiscoveryReason based on Bits"""
    namedValues = NamedValues(
        *(("none", 0),
          ("rfscan-discovered", 1),
          ("neighbor-ap-associated", 2),
          ("current-ap-associated", 3),
          ("probe-request-discovered", 4),
          ("ad-hoc-rogue", 5),
          ("associated-to-peer-ap", 6))
    )

_WsAuthenticatedClientStationDiscoveryReason_Type.__name__ = "Bits"
_WsAuthenticatedClientStationDiscoveryReason_Object = MibTableColumn
wsAuthenticatedClientStationDiscoveryReason = _WsAuthenticatedClientStationDiscoveryReason_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 3, 1, 4),
    _WsAuthenticatedClientStationDiscoveryReason_Type()
)
wsAuthenticatedClientStationDiscoveryReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAuthenticatedClientStationDiscoveryReason.setStatus("current")
_WsVAPAuthenticatedClientStatusTable_Object = MibTable
wsVAPAuthenticatedClientStatusTable = _WsVAPAuthenticatedClientStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 4)
)
if mibBuilder.loadTexts:
    wsVAPAuthenticatedClientStatusTable.setStatus("current")
_WsVAPAuthenticatedClientStatusEntry_Object = MibTableRow
wsVAPAuthenticatedClientStatusEntry = _WsVAPAuthenticatedClientStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 4, 1)
)
wsVAPAuthenticatedClientStatusEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsAuthenticatedVAPMacAddress"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsVAPAuthenticatedClientMacAddress"),
)
if mibBuilder.loadTexts:
    wsVAPAuthenticatedClientStatusEntry.setStatus("current")
_WsAuthenticatedVAPMacAddress_Type = MacAddress
_WsAuthenticatedVAPMacAddress_Object = MibTableColumn
wsAuthenticatedVAPMacAddress = _WsAuthenticatedVAPMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 4, 1, 1),
    _WsAuthenticatedVAPMacAddress_Type()
)
wsAuthenticatedVAPMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAuthenticatedVAPMacAddress.setStatus("current")
_WsVAPAuthenticatedClientMacAddress_Type = MacAddress
_WsVAPAuthenticatedClientMacAddress_Object = MibTableColumn
wsVAPAuthenticatedClientMacAddress = _WsVAPAuthenticatedClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 4, 1, 2),
    _WsVAPAuthenticatedClientMacAddress_Type()
)
wsVAPAuthenticatedClientMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsVAPAuthenticatedClientMacAddress.setStatus("current")
_WsSSIDAuthenticatedClientStatusTable_Object = MibTable
wsSSIDAuthenticatedClientStatusTable = _WsSSIDAuthenticatedClientStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 5)
)
if mibBuilder.loadTexts:
    wsSSIDAuthenticatedClientStatusTable.setStatus("current")
_WsSSIDAuthenticatedClientStatusEntry_Object = MibTableRow
wsSSIDAuthenticatedClientStatusEntry = _WsSSIDAuthenticatedClientStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 5, 1)
)
wsSSIDAuthenticatedClientStatusEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsSSIDAuthenticatedClientMacAddress"),
)
if mibBuilder.loadTexts:
    wsSSIDAuthenticatedClientStatusEntry.setStatus("current")


class _WsAuthenticatedSSID_Type(DisplayString):
    """Custom type wsAuthenticatedSSID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WsAuthenticatedSSID_Type.__name__ = "DisplayString"
_WsAuthenticatedSSID_Object = MibTableColumn
wsAuthenticatedSSID = _WsAuthenticatedSSID_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 5, 1, 1),
    _WsAuthenticatedSSID_Type()
)
wsAuthenticatedSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAuthenticatedSSID.setStatus("current")
_WsSSIDAuthenticatedClientMacAddress_Type = MacAddress
_WsSSIDAuthenticatedClientMacAddress_Object = MibTableColumn
wsSSIDAuthenticatedClientMacAddress = _WsSSIDAuthenticatedClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 5, 1, 2),
    _WsSSIDAuthenticatedClientMacAddress_Type()
)
wsSSIDAuthenticatedClientMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSSIDAuthenticatedClientMacAddress.setStatus("current")
_WsSwitchAuthenticatedClientStatusTable_Object = MibTable
wsSwitchAuthenticatedClientStatusTable = _WsSwitchAuthenticatedClientStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 6)
)
if mibBuilder.loadTexts:
    wsSwitchAuthenticatedClientStatusTable.setStatus("current")
_WsSwitchAuthenticatedClientStatusEntry_Object = MibTableRow
wsSwitchAuthenticatedClientStatusEntry = _WsSwitchAuthenticatedClientStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 6, 1)
)
wsSwitchAuthenticatedClientStatusEntry.setIndexNames(
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsSwitchIPAddress"),
    (0, "AT-UWC-WLAN-SWITCH-MIB", "wsSwitchAuthenticatedClientMacAddress"),
)
if mibBuilder.loadTexts:
    wsSwitchAuthenticatedClientStatusEntry.setStatus("current")
_WsAuthenticatedClientSwitchIPAddress_Type = IpAddress
_WsAuthenticatedClientSwitchIPAddress_Object = MibTableColumn
wsAuthenticatedClientSwitchIPAddress = _WsAuthenticatedClientSwitchIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 6, 1, 1),
    _WsAuthenticatedClientSwitchIPAddress_Type()
)
wsAuthenticatedClientSwitchIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAuthenticatedClientSwitchIPAddress.setStatus("current")
_WsSwitchAuthenticatedClientMacAddress_Type = MacAddress
_WsSwitchAuthenticatedClientMacAddress_Object = MibTableColumn
wsSwitchAuthenticatedClientMacAddress = _WsSwitchAuthenticatedClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 6, 1, 2),
    _WsSwitchAuthenticatedClientMacAddress_Type()
)
wsSwitchAuthenticatedClientMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSwitchAuthenticatedClientMacAddress.setStatus("current")
_WsAuthenticatedClientQosStatusTable_Object = MibTable
wsAuthenticatedClientQosStatusTable = _WsAuthenticatedClientQosStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 7)
)
if mibBuilder.loadTexts:
    wsAuthenticatedClientQosStatusTable.setStatus("current")
_WsAuthenticatedClientQosStatusEntry_Object = MibTableRow
wsAuthenticatedClientQosStatusEntry = _WsAuthenticatedClientQosStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 7, 1)
)
if mibBuilder.loadTexts:
    wsAuthenticatedClientQosStatusEntry.setStatus("current")
_WsAuthenticatedClientQosBandwidthLimitDown_Type = Unsigned32
_WsAuthenticatedClientQosBandwidthLimitDown_Object = MibTableColumn
wsAuthenticatedClientQosBandwidthLimitDown = _WsAuthenticatedClientQosBandwidthLimitDown_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 7, 1, 1),
    _WsAuthenticatedClientQosBandwidthLimitDown_Type()
)
wsAuthenticatedClientQosBandwidthLimitDown.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAuthenticatedClientQosBandwidthLimitDown.setStatus("current")
_WsAuthenticatedClientQosBandwidthLimitUp_Type = Unsigned32
_WsAuthenticatedClientQosBandwidthLimitUp_Object = MibTableColumn
wsAuthenticatedClientQosBandwidthLimitUp = _WsAuthenticatedClientQosBandwidthLimitUp_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 7, 1, 2),
    _WsAuthenticatedClientQosBandwidthLimitUp_Type()
)
wsAuthenticatedClientQosBandwidthLimitUp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAuthenticatedClientQosBandwidthLimitUp.setStatus("current")


class _WsAuthenticatedClientQosAccessControlDownType_Type(Integer32):
    """Custom type wsAuthenticatedClientQosAccessControlDownType based on Integer32"""
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
          ("ip", 2),
          ("mac", 3),
          ("ipv6", 4))
    )


_WsAuthenticatedClientQosAccessControlDownType_Type.__name__ = "Integer32"
_WsAuthenticatedClientQosAccessControlDownType_Object = MibTableColumn
wsAuthenticatedClientQosAccessControlDownType = _WsAuthenticatedClientQosAccessControlDownType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 7, 1, 3),
    _WsAuthenticatedClientQosAccessControlDownType_Type()
)
wsAuthenticatedClientQosAccessControlDownType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAuthenticatedClientQosAccessControlDownType.setStatus("current")


class _WsAuthenticatedClientQosAccessControlDownName_Type(DisplayString):
    """Custom type wsAuthenticatedClientQosAccessControlDownName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_WsAuthenticatedClientQosAccessControlDownName_Type.__name__ = "DisplayString"
_WsAuthenticatedClientQosAccessControlDownName_Object = MibTableColumn
wsAuthenticatedClientQosAccessControlDownName = _WsAuthenticatedClientQosAccessControlDownName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 7, 1, 4),
    _WsAuthenticatedClientQosAccessControlDownName_Type()
)
wsAuthenticatedClientQosAccessControlDownName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAuthenticatedClientQosAccessControlDownName.setStatus("current")


class _WsAuthenticatedClientQosAccessControlUpType_Type(Integer32):
    """Custom type wsAuthenticatedClientQosAccessControlUpType based on Integer32"""
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
          ("ip", 2),
          ("mac", 3),
          ("ipv6", 4))
    )


_WsAuthenticatedClientQosAccessControlUpType_Type.__name__ = "Integer32"
_WsAuthenticatedClientQosAccessControlUpType_Object = MibTableColumn
wsAuthenticatedClientQosAccessControlUpType = _WsAuthenticatedClientQosAccessControlUpType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 7, 1, 5),
    _WsAuthenticatedClientQosAccessControlUpType_Type()
)
wsAuthenticatedClientQosAccessControlUpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAuthenticatedClientQosAccessControlUpType.setStatus("current")


class _WsAuthenticatedClientQosAccessControlUpName_Type(DisplayString):
    """Custom type wsAuthenticatedClientQosAccessControlUpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_WsAuthenticatedClientQosAccessControlUpName_Type.__name__ = "DisplayString"
_WsAuthenticatedClientQosAccessControlUpName_Object = MibTableColumn
wsAuthenticatedClientQosAccessControlUpName = _WsAuthenticatedClientQosAccessControlUpName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 7, 1, 6),
    _WsAuthenticatedClientQosAccessControlUpName_Type()
)
wsAuthenticatedClientQosAccessControlUpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAuthenticatedClientQosAccessControlUpName.setStatus("current")


class _WsAuthenticatedClientQosDiffservPolicyDownType_Type(Integer32):
    """Custom type wsAuthenticatedClientQosDiffservPolicyDownType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("in", 2))
    )


_WsAuthenticatedClientQosDiffservPolicyDownType_Type.__name__ = "Integer32"
_WsAuthenticatedClientQosDiffservPolicyDownType_Object = MibTableColumn
wsAuthenticatedClientQosDiffservPolicyDownType = _WsAuthenticatedClientQosDiffservPolicyDownType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 7, 1, 7),
    _WsAuthenticatedClientQosDiffservPolicyDownType_Type()
)
wsAuthenticatedClientQosDiffservPolicyDownType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAuthenticatedClientQosDiffservPolicyDownType.setStatus("current")


class _WsAuthenticatedClientQosDiffservPolicyDownName_Type(DisplayString):
    """Custom type wsAuthenticatedClientQosDiffservPolicyDownName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_WsAuthenticatedClientQosDiffservPolicyDownName_Type.__name__ = "DisplayString"
_WsAuthenticatedClientQosDiffservPolicyDownName_Object = MibTableColumn
wsAuthenticatedClientQosDiffservPolicyDownName = _WsAuthenticatedClientQosDiffservPolicyDownName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 7, 1, 8),
    _WsAuthenticatedClientQosDiffservPolicyDownName_Type()
)
wsAuthenticatedClientQosDiffservPolicyDownName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAuthenticatedClientQosDiffservPolicyDownName.setStatus("current")


class _WsAuthenticatedClientQosDiffservPolicyUpType_Type(Integer32):
    """Custom type wsAuthenticatedClientQosDiffservPolicyUpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("in", 2))
    )


_WsAuthenticatedClientQosDiffservPolicyUpType_Type.__name__ = "Integer32"
_WsAuthenticatedClientQosDiffservPolicyUpType_Object = MibTableColumn
wsAuthenticatedClientQosDiffservPolicyUpType = _WsAuthenticatedClientQosDiffservPolicyUpType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 7, 1, 9),
    _WsAuthenticatedClientQosDiffservPolicyUpType_Type()
)
wsAuthenticatedClientQosDiffservPolicyUpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAuthenticatedClientQosDiffservPolicyUpType.setStatus("current")


class _WsAuthenticatedClientQosDiffservPolicyUpName_Type(DisplayString):
    """Custom type wsAuthenticatedClientQosDiffservPolicyUpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_WsAuthenticatedClientQosDiffservPolicyUpName_Type.__name__ = "DisplayString"
_WsAuthenticatedClientQosDiffservPolicyUpName_Object = MibTableColumn
wsAuthenticatedClientQosDiffservPolicyUpName = _WsAuthenticatedClientQosDiffservPolicyUpName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 7, 1, 10),
    _WsAuthenticatedClientQosDiffservPolicyUpName_Type()
)
wsAuthenticatedClientQosDiffservPolicyUpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAuthenticatedClientQosDiffservPolicyUpName.setStatus("current")


class _WsAuthenticatedClientQosOperStatus_Type(Integer32):
    """Custom type wsAuthenticatedClientQosOperStatus based on Integer32"""
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


_WsAuthenticatedClientQosOperStatus_Type.__name__ = "Integer32"
_WsAuthenticatedClientQosOperStatus_Object = MibTableColumn
wsAuthenticatedClientQosOperStatus = _WsAuthenticatedClientQosOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 7, 1, 11),
    _WsAuthenticatedClientQosOperStatus_Type()
)
wsAuthenticatedClientQosOperStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAuthenticatedClientQosOperStatus.setStatus("current")
_WsAuthenticatedClientSessionStatisticsTable_Object = MibTable
wsAuthenticatedClientSessionStatisticsTable = _WsAuthenticatedClientSessionStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 8)
)
if mibBuilder.loadTexts:
    wsAuthenticatedClientSessionStatisticsTable.setStatus("current")
_WsAuthenticatedClientSessionStatisticsEntry_Object = MibTableRow
wsAuthenticatedClientSessionStatisticsEntry = _WsAuthenticatedClientSessionStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 8, 1)
)
if mibBuilder.loadTexts:
    wsAuthenticatedClientSessionStatisticsEntry.setStatus("current")
_WsAuthenticatedClientSessionPktsRecvd_Type = Counter64
_WsAuthenticatedClientSessionPktsRecvd_Object = MibTableColumn
wsAuthenticatedClientSessionPktsRecvd = _WsAuthenticatedClientSessionPktsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 8, 1, 1),
    _WsAuthenticatedClientSessionPktsRecvd_Type()
)
wsAuthenticatedClientSessionPktsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAuthenticatedClientSessionPktsRecvd.setStatus("current")
_WsAuthenticatedClientSessionBytesRecvd_Type = Counter64
_WsAuthenticatedClientSessionBytesRecvd_Object = MibTableColumn
wsAuthenticatedClientSessionBytesRecvd = _WsAuthenticatedClientSessionBytesRecvd_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 8, 1, 2),
    _WsAuthenticatedClientSessionBytesRecvd_Type()
)
wsAuthenticatedClientSessionBytesRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAuthenticatedClientSessionBytesRecvd.setStatus("current")
_WsAuthenticatedClientSessionPktsTransmitted_Type = Counter64
_WsAuthenticatedClientSessionPktsTransmitted_Object = MibTableColumn
wsAuthenticatedClientSessionPktsTransmitted = _WsAuthenticatedClientSessionPktsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 8, 1, 3),
    _WsAuthenticatedClientSessionPktsTransmitted_Type()
)
wsAuthenticatedClientSessionPktsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAuthenticatedClientSessionPktsTransmitted.setStatus("current")
_WsAuthenticatedClientSessionBytesTransmitted_Type = Counter64
_WsAuthenticatedClientSessionBytesTransmitted_Object = MibTableColumn
wsAuthenticatedClientSessionBytesTransmitted = _WsAuthenticatedClientSessionBytesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 8, 1, 4),
    _WsAuthenticatedClientSessionBytesTransmitted_Type()
)
wsAuthenticatedClientSessionBytesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAuthenticatedClientSessionBytesTransmitted.setStatus("current")
_WsAuthenticatedClientSessionDuplicatePktsRecvd_Type = Counter32
_WsAuthenticatedClientSessionDuplicatePktsRecvd_Object = MibTableColumn
wsAuthenticatedClientSessionDuplicatePktsRecvd = _WsAuthenticatedClientSessionDuplicatePktsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 8, 1, 5),
    _WsAuthenticatedClientSessionDuplicatePktsRecvd_Type()
)
wsAuthenticatedClientSessionDuplicatePktsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAuthenticatedClientSessionDuplicatePktsRecvd.setStatus("current")
_WsAuthenticatedClientSessionFragmentedPktsRecvd_Type = Counter32
_WsAuthenticatedClientSessionFragmentedPktsRecvd_Object = MibTableColumn
wsAuthenticatedClientSessionFragmentedPktsRecvd = _WsAuthenticatedClientSessionFragmentedPktsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 8, 1, 6),
    _WsAuthenticatedClientSessionFragmentedPktsRecvd_Type()
)
wsAuthenticatedClientSessionFragmentedPktsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAuthenticatedClientSessionFragmentedPktsRecvd.setStatus("current")
_WsAuthenticatedClientSessionFragmentedPktsTransmitted_Type = Counter32
_WsAuthenticatedClientSessionFragmentedPktsTransmitted_Object = MibTableColumn
wsAuthenticatedClientSessionFragmentedPktsTransmitted = _WsAuthenticatedClientSessionFragmentedPktsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 8, 1, 7),
    _WsAuthenticatedClientSessionFragmentedPktsTransmitted_Type()
)
wsAuthenticatedClientSessionFragmentedPktsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAuthenticatedClientSessionFragmentedPktsTransmitted.setStatus("current")
_WsAuthenticatedClientSessionTransmitRetryCount_Type = Counter32
_WsAuthenticatedClientSessionTransmitRetryCount_Object = MibTableColumn
wsAuthenticatedClientSessionTransmitRetryCount = _WsAuthenticatedClientSessionTransmitRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 8, 1, 8),
    _WsAuthenticatedClientSessionTransmitRetryCount_Type()
)
wsAuthenticatedClientSessionTransmitRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAuthenticatedClientSessionTransmitRetryCount.setStatus("current")
_WsAuthenticatedClientSessionTransmitRetryFailedCount_Type = Counter32
_WsAuthenticatedClientSessionTransmitRetryFailedCount_Object = MibTableColumn
wsAuthenticatedClientSessionTransmitRetryFailedCount = _WsAuthenticatedClientSessionTransmitRetryFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 8, 1, 9),
    _WsAuthenticatedClientSessionTransmitRetryFailedCount_Type()
)
wsAuthenticatedClientSessionTransmitRetryFailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAuthenticatedClientSessionTransmitRetryFailedCount.setStatus("current")
_WsAuthenticatedClientSessionPktsRecvDropped_Type = Counter64
_WsAuthenticatedClientSessionPktsRecvDropped_Object = MibTableColumn
wsAuthenticatedClientSessionPktsRecvDropped = _WsAuthenticatedClientSessionPktsRecvDropped_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 8, 1, 10),
    _WsAuthenticatedClientSessionPktsRecvDropped_Type()
)
wsAuthenticatedClientSessionPktsRecvDropped.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAuthenticatedClientSessionPktsRecvDropped.setStatus("current")
_WsAuthenticatedClientSessionBytesRecvDropped_Type = Counter64
_WsAuthenticatedClientSessionBytesRecvDropped_Object = MibTableColumn
wsAuthenticatedClientSessionBytesRecvDropped = _WsAuthenticatedClientSessionBytesRecvDropped_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 8, 1, 11),
    _WsAuthenticatedClientSessionBytesRecvDropped_Type()
)
wsAuthenticatedClientSessionBytesRecvDropped.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAuthenticatedClientSessionBytesRecvDropped.setStatus("current")
_WsAuthenticatedClientSessionPktsTransmitDropped_Type = Counter64
_WsAuthenticatedClientSessionPktsTransmitDropped_Object = MibTableColumn
wsAuthenticatedClientSessionPktsTransmitDropped = _WsAuthenticatedClientSessionPktsTransmitDropped_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 8, 1, 12),
    _WsAuthenticatedClientSessionPktsTransmitDropped_Type()
)
wsAuthenticatedClientSessionPktsTransmitDropped.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAuthenticatedClientSessionPktsTransmitDropped.setStatus("current")
_WsAuthenticatedClientSessionBytesTransmitDropped_Type = Counter64
_WsAuthenticatedClientSessionBytesTransmitDropped_Object = MibTableColumn
wsAuthenticatedClientSessionBytesTransmitDropped = _WsAuthenticatedClientSessionBytesTransmitDropped_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 8, 1, 13),
    _WsAuthenticatedClientSessionBytesTransmitDropped_Type()
)
wsAuthenticatedClientSessionBytesTransmitDropped.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAuthenticatedClientSessionBytesTransmitDropped.setStatus("current")
_WsAuthenticatedClientSessionTSViolatePktsRecvd_Type = Counter32
_WsAuthenticatedClientSessionTSViolatePktsRecvd_Object = MibTableColumn
wsAuthenticatedClientSessionTSViolatePktsRecvd = _WsAuthenticatedClientSessionTSViolatePktsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 8, 1, 14),
    _WsAuthenticatedClientSessionTSViolatePktsRecvd_Type()
)
wsAuthenticatedClientSessionTSViolatePktsRecvd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAuthenticatedClientSessionTSViolatePktsRecvd.setStatus("current")
_WsAuthenticatedClientSessionTSViolatePktsTransmitted_Type = Counter32
_WsAuthenticatedClientSessionTSViolatePktsTransmitted_Object = MibTableColumn
wsAuthenticatedClientSessionTSViolatePktsTransmitted = _WsAuthenticatedClientSessionTSViolatePktsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 8, 1, 15),
    _WsAuthenticatedClientSessionTSViolatePktsTransmitted_Type()
)
wsAuthenticatedClientSessionTSViolatePktsTransmitted.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAuthenticatedClientSessionTSViolatePktsTransmitted.setStatus("current")
_WsAuthenticatedClientQosCachedStatusTable_Object = MibTable
wsAuthenticatedClientQosCachedStatusTable = _WsAuthenticatedClientQosCachedStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 9)
)
if mibBuilder.loadTexts:
    wsAuthenticatedClientQosCachedStatusTable.setStatus("current")
_WsAuthenticatedClientQosCachedStatusEntry_Object = MibTableRow
wsAuthenticatedClientQosCachedStatusEntry = _WsAuthenticatedClientQosCachedStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 9, 1)
)
if mibBuilder.loadTexts:
    wsAuthenticatedClientQosCachedStatusEntry.setStatus("current")
_WsAuthenticatedClientQosCachedBandwidthLimitDown_Type = Unsigned32
_WsAuthenticatedClientQosCachedBandwidthLimitDown_Object = MibTableColumn
wsAuthenticatedClientQosCachedBandwidthLimitDown = _WsAuthenticatedClientQosCachedBandwidthLimitDown_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 9, 1, 1),
    _WsAuthenticatedClientQosCachedBandwidthLimitDown_Type()
)
wsAuthenticatedClientQosCachedBandwidthLimitDown.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAuthenticatedClientQosCachedBandwidthLimitDown.setStatus("current")
_WsAuthenticatedClientQosCachedBandwidthLimitUp_Type = Unsigned32
_WsAuthenticatedClientQosCachedBandwidthLimitUp_Object = MibTableColumn
wsAuthenticatedClientQosCachedBandwidthLimitUp = _WsAuthenticatedClientQosCachedBandwidthLimitUp_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 9, 1, 2),
    _WsAuthenticatedClientQosCachedBandwidthLimitUp_Type()
)
wsAuthenticatedClientQosCachedBandwidthLimitUp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAuthenticatedClientQosCachedBandwidthLimitUp.setStatus("current")


class _WsAuthenticatedClientQosCachedAccessControlDownType_Type(Integer32):
    """Custom type wsAuthenticatedClientQosCachedAccessControlDownType based on Integer32"""
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
          ("ip", 2),
          ("mac", 3),
          ("ipv6", 4))
    )


_WsAuthenticatedClientQosCachedAccessControlDownType_Type.__name__ = "Integer32"
_WsAuthenticatedClientQosCachedAccessControlDownType_Object = MibTableColumn
wsAuthenticatedClientQosCachedAccessControlDownType = _WsAuthenticatedClientQosCachedAccessControlDownType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 9, 1, 3),
    _WsAuthenticatedClientQosCachedAccessControlDownType_Type()
)
wsAuthenticatedClientQosCachedAccessControlDownType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAuthenticatedClientQosCachedAccessControlDownType.setStatus("current")


class _WsAuthenticatedClientQosCachedAccessControlDownName_Type(DisplayString):
    """Custom type wsAuthenticatedClientQosCachedAccessControlDownName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_WsAuthenticatedClientQosCachedAccessControlDownName_Type.__name__ = "DisplayString"
_WsAuthenticatedClientQosCachedAccessControlDownName_Object = MibTableColumn
wsAuthenticatedClientQosCachedAccessControlDownName = _WsAuthenticatedClientQosCachedAccessControlDownName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 9, 1, 4),
    _WsAuthenticatedClientQosCachedAccessControlDownName_Type()
)
wsAuthenticatedClientQosCachedAccessControlDownName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAuthenticatedClientQosCachedAccessControlDownName.setStatus("current")


class _WsAuthenticatedClientQosCachedAccessControlUpType_Type(Integer32):
    """Custom type wsAuthenticatedClientQosCachedAccessControlUpType based on Integer32"""
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
          ("ip", 2),
          ("mac", 3),
          ("ipv6", 4))
    )


_WsAuthenticatedClientQosCachedAccessControlUpType_Type.__name__ = "Integer32"
_WsAuthenticatedClientQosCachedAccessControlUpType_Object = MibTableColumn
wsAuthenticatedClientQosCachedAccessControlUpType = _WsAuthenticatedClientQosCachedAccessControlUpType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 9, 1, 5),
    _WsAuthenticatedClientQosCachedAccessControlUpType_Type()
)
wsAuthenticatedClientQosCachedAccessControlUpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAuthenticatedClientQosCachedAccessControlUpType.setStatus("current")


class _WsAuthenticatedClientQosCachedAccessControlUpName_Type(DisplayString):
    """Custom type wsAuthenticatedClientQosCachedAccessControlUpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_WsAuthenticatedClientQosCachedAccessControlUpName_Type.__name__ = "DisplayString"
_WsAuthenticatedClientQosCachedAccessControlUpName_Object = MibTableColumn
wsAuthenticatedClientQosCachedAccessControlUpName = _WsAuthenticatedClientQosCachedAccessControlUpName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 9, 1, 6),
    _WsAuthenticatedClientQosCachedAccessControlUpName_Type()
)
wsAuthenticatedClientQosCachedAccessControlUpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAuthenticatedClientQosCachedAccessControlUpName.setStatus("current")


class _WsAuthenticatedClientQosCachedDiffservPolicyDownType_Type(Integer32):
    """Custom type wsAuthenticatedClientQosCachedDiffservPolicyDownType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("in", 2))
    )


_WsAuthenticatedClientQosCachedDiffservPolicyDownType_Type.__name__ = "Integer32"
_WsAuthenticatedClientQosCachedDiffservPolicyDownType_Object = MibTableColumn
wsAuthenticatedClientQosCachedDiffservPolicyDownType = _WsAuthenticatedClientQosCachedDiffservPolicyDownType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 9, 1, 7),
    _WsAuthenticatedClientQosCachedDiffservPolicyDownType_Type()
)
wsAuthenticatedClientQosCachedDiffservPolicyDownType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAuthenticatedClientQosCachedDiffservPolicyDownType.setStatus("current")


class _WsAuthenticatedClientQosCachedDiffservPolicyDownName_Type(DisplayString):
    """Custom type wsAuthenticatedClientQosCachedDiffservPolicyDownName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_WsAuthenticatedClientQosCachedDiffservPolicyDownName_Type.__name__ = "DisplayString"
_WsAuthenticatedClientQosCachedDiffservPolicyDownName_Object = MibTableColumn
wsAuthenticatedClientQosCachedDiffservPolicyDownName = _WsAuthenticatedClientQosCachedDiffservPolicyDownName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 9, 1, 8),
    _WsAuthenticatedClientQosCachedDiffservPolicyDownName_Type()
)
wsAuthenticatedClientQosCachedDiffservPolicyDownName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAuthenticatedClientQosCachedDiffservPolicyDownName.setStatus("current")


class _WsAuthenticatedClientQosCachedDiffservPolicyUpType_Type(Integer32):
    """Custom type wsAuthenticatedClientQosCachedDiffservPolicyUpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("in", 2))
    )


_WsAuthenticatedClientQosCachedDiffservPolicyUpType_Type.__name__ = "Integer32"
_WsAuthenticatedClientQosCachedDiffservPolicyUpType_Object = MibTableColumn
wsAuthenticatedClientQosCachedDiffservPolicyUpType = _WsAuthenticatedClientQosCachedDiffservPolicyUpType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 9, 1, 9),
    _WsAuthenticatedClientQosCachedDiffservPolicyUpType_Type()
)
wsAuthenticatedClientQosCachedDiffservPolicyUpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAuthenticatedClientQosCachedDiffservPolicyUpType.setStatus("current")


class _WsAuthenticatedClientQosCachedDiffservPolicyUpName_Type(DisplayString):
    """Custom type wsAuthenticatedClientQosCachedDiffservPolicyUpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_WsAuthenticatedClientQosCachedDiffservPolicyUpName_Type.__name__ = "DisplayString"
_WsAuthenticatedClientQosCachedDiffservPolicyUpName_Object = MibTableColumn
wsAuthenticatedClientQosCachedDiffservPolicyUpName = _WsAuthenticatedClientQosCachedDiffservPolicyUpName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 21, 9, 1, 10),
    _WsAuthenticatedClientQosCachedDiffservPolicyUpName_Type()
)
wsAuthenticatedClientQosCachedDiffservPolicyUpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsAuthenticatedClientQosCachedDiffservPolicyUpName.setStatus("current")
wsNetworkEntry.registerAugmentions(
    ("AT-UWC-WLAN-SWITCH-MIB",
     "wsNetworkClientQosEntry")
)
wsNetworkClientQosEntry.setIndexNames(*wsNetworkEntry.getIndexNames())
wsAPProfileRadioEntry.registerAugmentions(
    ("AT-UWC-WLAN-SWITCH-MIB",
     "wsAPProfileRadioTspecEntry")
)
wsAPProfileRadioTspecEntry.setIndexNames(*wsAPProfileRadioEntry.getIndexNames())
wsManagedAPStatusEntry.registerAugmentions(
    ("AT-UWC-WLAN-SWITCH-MIB",
     "wsManagedAPStatisticsEntry")
)
wsManagedAPStatisticsEntry.setIndexNames(*wsManagedAPStatusEntry.getIndexNames())
wsManagedAPRadioStatusEntry.registerAugmentions(
    ("AT-UWC-WLAN-SWITCH-MIB",
     "wsManagedAPRadioStatisticsEntry")
)
wsManagedAPRadioStatisticsEntry.setIndexNames(*wsManagedAPRadioStatusEntry.getIndexNames())
wsManagedAPVAPStatusEntry.registerAugmentions(
    ("AT-UWC-WLAN-SWITCH-MIB",
     "wsManagedAPVAPStatisticsEntry")
)
wsManagedAPVAPStatisticsEntry.setIndexNames(*wsManagedAPVAPStatusEntry.getIndexNames())
wsAssociatedClientStatusEntry.registerAugmentions(
    ("AT-UWC-WLAN-SWITCH-MIB",
     "wsAssociatedClientStatisticsEntry")
)
wsAssociatedClientStatisticsEntry.setIndexNames(*wsAssociatedClientStatusEntry.getIndexNames())
wsAssociatedClientStatusEntry.registerAugmentions(
    ("AT-UWC-WLAN-SWITCH-MIB",
     "wsAssociatedClientQosStatusEntry")
)
wsAssociatedClientQosStatusEntry.setIndexNames(*wsAssociatedClientStatusEntry.getIndexNames())
wsAssociatedClientStatusEntry.registerAugmentions(
    ("AT-UWC-WLAN-SWITCH-MIB",
     "wsAssociatedClientSessionStatisticsEntry")
)
wsAssociatedClientSessionStatisticsEntry.setIndexNames(*wsAssociatedClientStatusEntry.getIndexNames())
wsAssociatedClientStatusEntry.registerAugmentions(
    ("AT-UWC-WLAN-SWITCH-MIB",
     "wsAssociatedClientQosCachedStatusEntry")
)
wsAssociatedClientQosCachedStatusEntry.setIndexNames(*wsAssociatedClientStatusEntry.getIndexNames())
wsManagedAPTspecStatusEntry.registerAugmentions(
    ("AT-UWC-WLAN-SWITCH-MIB",
     "wsManagedAPTspecStatisticsEntry")
)
wsManagedAPTspecStatisticsEntry.setIndexNames(*wsManagedAPTspecStatusEntry.getIndexNames())
wsManagedAPRadioTspecStatusEntry.registerAugmentions(
    ("AT-UWC-WLAN-SWITCH-MIB",
     "wsManagedAPRadioTspecStatisticsEntry")
)
wsManagedAPRadioTspecStatisticsEntry.setIndexNames(*wsManagedAPRadioTspecStatusEntry.getIndexNames())
wsManagedAPVAPTspecStatusEntry.registerAugmentions(
    ("AT-UWC-WLAN-SWITCH-MIB",
     "wsManagedAPVAPTspecStatisticsEntry")
)
wsManagedAPVAPTspecStatisticsEntry.setIndexNames(*wsManagedAPVAPTspecStatusEntry.getIndexNames())
wsAssociatedClientTsStatusEntry.registerAugmentions(
    ("AT-UWC-WLAN-SWITCH-MIB",
     "wsAssociatedClientTsStatisticsEntry")
)
wsAssociatedClientTsStatisticsEntry.setIndexNames(*wsAssociatedClientTsStatusEntry.getIndexNames())
wsWDSLinkStatusEntry.registerAugmentions(
    ("AT-UWC-WLAN-SWITCH-MIB",
     "wsWDSLinkStatisticsEntry")
)
wsWDSLinkStatisticsEntry.setIndexNames(*wsWDSLinkStatusEntry.getIndexNames())
wsAuthenticatedClientStatusEntry.registerAugmentions(
    ("AT-UWC-WLAN-SWITCH-MIB",
     "wsAuthenticatedClientStatisticsEntry")
)
wsAuthenticatedClientStatisticsEntry.setIndexNames(*wsAuthenticatedClientStatusEntry.getIndexNames())
wsAuthenticatedClientStatusEntry.registerAugmentions(
    ("AT-UWC-WLAN-SWITCH-MIB",
     "wsAuthenticatedClientQosStatusEntry")
)
wsAuthenticatedClientQosStatusEntry.setIndexNames(*wsAuthenticatedClientStatusEntry.getIndexNames())
wsAuthenticatedClientStatusEntry.registerAugmentions(
    ("AT-UWC-WLAN-SWITCH-MIB",
     "wsAuthenticatedClientSessionStatisticsEntry")
)
wsAuthenticatedClientSessionStatisticsEntry.setIndexNames(*wsAuthenticatedClientStatusEntry.getIndexNames())
wsAuthenticatedClientStatusEntry.registerAugmentions(
    ("AT-UWC-WLAN-SWITCH-MIB",
     "wsAuthenticatedClientQosCachedStatusEntry")
)
wsAuthenticatedClientQosCachedStatusEntry.setIndexNames(*wsAuthenticatedClientStatusEntry.getIndexNames())

# Managed Objects groups


# Notification objects

wsModeEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 0, 1)
)
if mibBuilder.loadTexts:
    wsModeEnabled.setStatus(
        "current"
    )

wsModeDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 0, 2)
)
if mibBuilder.loadTexts:
    wsModeDisabled.setStatus(
        "current"
    )

wsManagedAPDatabaseFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 0, 3)
)
wsManagedAPDatabaseFull.setObjects(
    ("AT-UWC-WLAN-SWITCH-MIB", "wsManagedAPMacAddress")
)
if mibBuilder.loadTexts:
    wsManagedAPDatabaseFull.setStatus(
        "current"
    )

wsManagedAPNeighborAPListFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 0, 4)
)
if mibBuilder.loadTexts:
    wsManagedAPNeighborAPListFull.setStatus(
        "current"
    )

wsManagedAPNeighborClientListFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 0, 5)
)
if mibBuilder.loadTexts:
    wsManagedAPNeighborClientListFull.setStatus(
        "current"
    )

wsAPFailureListFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 0, 6)
)
if mibBuilder.loadTexts:
    wsAPFailureListFull.setStatus(
        "current"
    )

wsRFScanAPListFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 0, 7)
)
if mibBuilder.loadTexts:
    wsRFScanAPListFull.setStatus(
        "current"
    )

wsClientAssociationDatabaseFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 0, 8)
)
wsClientAssociationDatabaseFull.setObjects(
    ("AT-UWC-WLAN-SWITCH-MIB", "wsAssociatedClientMacAddress")
)
if mibBuilder.loadTexts:
    wsClientAssociationDatabaseFull.setStatus(
        "current"
    )

wsPeerSwitchDiscovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 0, 9)
)
wsPeerSwitchDiscovered.setObjects(
    ("AT-UWC-WLAN-SWITCH-MIB", "wsPeerIpAddress")
)
if mibBuilder.loadTexts:
    wsPeerSwitchDiscovered.setStatus(
        "current"
    )

wsPeerSwitchFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 0, 10)
)
wsPeerSwitchFailed.setObjects(
    ("AT-UWC-WLAN-SWITCH-MIB", "wsPeerIpAddress")
)
if mibBuilder.loadTexts:
    wsPeerSwitchFailed.setStatus(
        "current"
    )

wsPeerSwitchUnknownProtocol = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 0, 11)
)
wsPeerSwitchUnknownProtocol.setObjects(
      *(("AT-UWC-WLAN-SWITCH-MIB", "wsPeerIpAddress"),
        ("AT-UWC-WLAN-SWITCH-MIB", "wsPeerProtocolVersion"))
)
if mibBuilder.loadTexts:
    wsPeerSwitchUnknownProtocol.setStatus(
        "current"
    )

wsManagedAPDiscovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 0, 12)
)
wsManagedAPDiscovered.setObjects(
    ("AT-UWC-WLAN-SWITCH-MIB", "wsManagedAPMacAddress")
)
if mibBuilder.loadTexts:
    wsManagedAPDiscovered.setStatus(
        "current"
    )

wsManagedAPFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 0, 13)
)
wsManagedAPFailed.setObjects(
    ("AT-UWC-WLAN-SWITCH-MIB", "wsManagedAPMacAddress")
)
if mibBuilder.loadTexts:
    wsManagedAPFailed.setStatus(
        "current"
    )

wsManagedAPUnknownProtocol = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 0, 14)
)
wsManagedAPUnknownProtocol.setObjects(
      *(("AT-UWC-WLAN-SWITCH-MIB", "wsFailedAPMacAddress"),
        ("AT-UWC-WLAN-SWITCH-MIB", "wsFailedAPProtocolVersion"))
)
if mibBuilder.loadTexts:
    wsManagedAPUnknownProtocol.setStatus(
        "current"
    )

wsAPAssociationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 0, 15)
)
wsAPAssociationFailure.setObjects(
    ("AT-UWC-WLAN-SWITCH-MIB", "wsFailedAPMacAddress")
)
if mibBuilder.loadTexts:
    wsAPAssociationFailure.setStatus(
        "current"
    )

wsAPAuthenticationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 0, 16)
)
wsAPAuthenticationFailure.setObjects(
    ("AT-UWC-WLAN-SWITCH-MIB", "wsFailedAPMacAddress")
)
if mibBuilder.loadTexts:
    wsAPAuthenticationFailure.setStatus(
        "current"
    )

wsRFScanRogueAPDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 0, 17)
)
wsRFScanRogueAPDetected.setObjects(
      *(("AT-UWC-WLAN-SWITCH-MIB", "wsManagedAPMacAddress"),
        ("AT-UWC-WLAN-SWITCH-MIB", "wsManagedAPRadioInterface"),
        ("AT-UWC-WLAN-SWITCH-MIB", "wsRFScanAPMacAddress"),
        ("AT-UWC-WLAN-SWITCH-MIB", "wsRFScanAPSSID"))
)
if mibBuilder.loadTexts:
    wsRFScanRogueAPDetected.setStatus(
        "current"
    )

wsRFScanAPDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 0, 18)
)
wsRFScanAPDetected.setObjects(
      *(("AT-UWC-WLAN-SWITCH-MIB", "wsManagedAPMacAddress"),
        ("AT-UWC-WLAN-SWITCH-MIB", "wsManagedAPRadioInterface"),
        ("AT-UWC-WLAN-SWITCH-MIB", "wsRFScanAPMacAddress"),
        ("AT-UWC-WLAN-SWITCH-MIB", "wsRFScanAPSSID"))
)
if mibBuilder.loadTexts:
    wsRFScanAPDetected.setStatus(
        "current"
    )

wsRFScanNewClientDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 0, 19)
)
wsRFScanNewClientDetected.setObjects(
      *(("AT-UWC-WLAN-SWITCH-MIB", "wsManagedAPMacAddress"),
        ("AT-UWC-WLAN-SWITCH-MIB", "wsManagedAPRadioInterface"),
        ("AT-UWC-WLAN-SWITCH-MIB", "wsNeighborClientMacAddress"))
)
if mibBuilder.loadTexts:
    wsRFScanNewClientDetected.setStatus(
        "current"
    )

wsClientAssociationDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 0, 20)
)
wsClientAssociationDetected.setObjects(
      *(("AT-UWC-WLAN-SWITCH-MIB", "wsAssociatedClientMacAddress"),
        ("AT-UWC-WLAN-SWITCH-MIB", "wsVAPMacAddress"),
        ("AT-UWC-WLAN-SWITCH-MIB", "wsManagedAPMacAddress"))
)
if mibBuilder.loadTexts:
    wsClientAssociationDetected.setStatus(
        "current"
    )

wsClientDisassociationDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 0, 21)
)
wsClientDisassociationDetected.setObjects(
      *(("AT-UWC-WLAN-SWITCH-MIB", "wsAssociatedClientMacAddress"),
        ("AT-UWC-WLAN-SWITCH-MIB", "wsVAPMacAddress"),
        ("AT-UWC-WLAN-SWITCH-MIB", "wsManagedAPMacAddress"))
)
if mibBuilder.loadTexts:
    wsClientDisassociationDetected.setStatus(
        "current"
    )

wsClientRoamDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 0, 22)
)
wsClientRoamDetected.setObjects(
      *(("AT-UWC-WLAN-SWITCH-MIB", "wsAssociatedClientMacAddress"),
        ("AT-UWC-WLAN-SWITCH-MIB", "wsVAPMacAddress"),
        ("AT-UWC-WLAN-SWITCH-MIB", "wsManagedAPMacAddress"))
)
if mibBuilder.loadTexts:
    wsClientRoamDetected.setStatus(
        "current"
    )

wsClientAssociationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 0, 23)
)
wsClientAssociationFailure.setObjects(
    ("AT-UWC-WLAN-SWITCH-MIB", "wsNeighborClientMacAddress")
)
if mibBuilder.loadTexts:
    wsClientAssociationFailure.setStatus(
        "current"
    )

wsClientAuthenticationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 0, 24)
)
wsClientAuthenticationFailure.setObjects(
    ("AT-UWC-WLAN-SWITCH-MIB", "wsNeighborClientMacAddress")
)
if mibBuilder.loadTexts:
    wsClientAuthenticationFailure.setStatus(
        "current"
    )

wsAdHocClientDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 0, 25)
)
wsAdHocClientDetected.setObjects(
      *(("AT-UWC-WLAN-SWITCH-MIB", "wsAdHocClientMacAddress"),
        ("AT-UWC-WLAN-SWITCH-MIB", "wsDetectedAPMacAddress"),
        ("AT-UWC-WLAN-SWITCH-MIB", "wsDetectedAPRadioInterface"))
)
if mibBuilder.loadTexts:
    wsAdHocClientDetected.setStatus(
        "current"
    )

wsWLANBandwidthUtilizationExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 0, 26)
)
wsWLANBandwidthUtilizationExceeded.setObjects(
      *(("AT-UWC-WLAN-SWITCH-MIB", "wsManagedAPMacAddress"),
        ("AT-UWC-WLAN-SWITCH-MIB", "wsManagedAPRadioMacAddress"),
        ("AT-UWC-WLAN-SWITCH-MIB", "wsManagedAPRadioInterface"),
        ("AT-UWC-WLAN-SWITCH-MIB", "wsManagedAPRadioWLANUtilization"))
)
if mibBuilder.loadTexts:
    wsWLANBandwidthUtilizationExceeded.setStatus(
        "current"
    )

wsAdHocClientListFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 0, 27)
)
if mibBuilder.loadTexts:
    wsAdHocClientListFull.setStatus(
        "current"
    )

wsPeerSwitchConfigurationCommandReceived = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 0, 28)
)
wsPeerSwitchConfigurationCommandReceived.setObjects(
      *(("AT-UWC-WLAN-SWITCH-MIB", "wsPeerIpAddress"),
        ("AT-UWC-WLAN-SWITCH-MIB", "wsPeerConfigReceived"))
)
if mibBuilder.loadTexts:
    wsPeerSwitchConfigurationCommandReceived.setStatus(
        "current"
    )

wsPeerSwitchManagedAPLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 0, 29)
)
wsPeerSwitchManagedAPLimitExceeded.setObjects(
      *(("AT-UWC-WLAN-SWITCH-MIB", "wsPeerIpAddress"),
        ("AT-UWC-WLAN-SWITCH-MIB", "wsPeerSwitchAPMacAddress"))
)
if mibBuilder.loadTexts:
    wsPeerSwitchManagedAPLimitExceeded.setStatus(
        "current"
    )

wsPeerSwitchClientLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 0, 30)
)
wsPeerSwitchClientLimitExceeded.setObjects(
      *(("AT-UWC-WLAN-SWITCH-MIB", "wsPeerIpAddress"),
        ("AT-UWC-WLAN-SWITCH-MIB", "wsAssociatedClientMacAddress"))
)
if mibBuilder.loadTexts:
    wsPeerSwitchClientLimitExceeded.setStatus(
        "current"
    )

wsClusterControllerElected = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 0, 32)
)
wsClusterControllerElected.setObjects(
    ("AT-UWC-WLAN-SWITCH-MIB", "wsIPAddress")
)
if mibBuilder.loadTexts:
    wsClusterControllerElected.setStatus(
        "current"
    )

wsClusterMaxAPExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 0, 33)
)
wsClusterMaxAPExceeded.setObjects(
      *(("AT-UWC-WLAN-SWITCH-MIB", "wsIPAddress"),
        ("AT-UWC-WLAN-SWITCH-MIB", "wsManagedAPMacAddress"),
        ("AT-UWC-WLAN-SWITCH-MIB", "wsManagedAPIpAddress"),
        ("AT-UWC-WLAN-SWITCH-MIB", "wsManagedAPSwitchIpAddress"))
)
if mibBuilder.loadTexts:
    wsClusterMaxAPExceeded.setStatus(
        "current"
    )

wsRoguesPresent = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 0, 34)
)
if mibBuilder.loadTexts:
    wsRoguesPresent.setStatus(
        "current"
    )

wsDetectedClientListFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 0, 35)
)
if mibBuilder.loadTexts:
    wsDetectedClientListFull.setStatus(
        "current"
    )

wsRogueClientsPresent = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 0, 36)
)
if mibBuilder.loadTexts:
    wsRogueClientsPresent.setStatus(
        "current"
    )

wsChannelPlanAlgoComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 0, 37)
)
if mibBuilder.loadTexts:
    wsChannelPlanAlgoComplete.setStatus(
        "current"
    )

wsPowerPlanAlgoComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 0, 38)
)
if mibBuilder.loadTexts:
    wsPowerPlanAlgoComplete.setStatus(
        "current"
    )

wsLocallyManagedAPLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 8, 34, 0, 41)
)
wsLocallyManagedAPLimitExceeded.setObjects(
    ("AT-UWC-WLAN-SWITCH-MIB", "wsManagedAPMacAddress")
)
if mibBuilder.loadTexts:
    wsLocallyManagedAPLimitExceeded.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AT-UWC-WLAN-SWITCH-MIB",
    **{"WsOui": WsOui,
       "TspecSuppAC": TspecSuppAC,
       "at-uwc": at_uwc,
       "fastPathWLANSwitch": fastPathWLANSwitch,
       "wsTraps": wsTraps,
       "wsModeEnabled": wsModeEnabled,
       "wsModeDisabled": wsModeDisabled,
       "wsManagedAPDatabaseFull": wsManagedAPDatabaseFull,
       "wsManagedAPNeighborAPListFull": wsManagedAPNeighborAPListFull,
       "wsManagedAPNeighborClientListFull": wsManagedAPNeighborClientListFull,
       "wsAPFailureListFull": wsAPFailureListFull,
       "wsRFScanAPListFull": wsRFScanAPListFull,
       "wsClientAssociationDatabaseFull": wsClientAssociationDatabaseFull,
       "wsPeerSwitchDiscovered": wsPeerSwitchDiscovered,
       "wsPeerSwitchFailed": wsPeerSwitchFailed,
       "wsPeerSwitchUnknownProtocol": wsPeerSwitchUnknownProtocol,
       "wsManagedAPDiscovered": wsManagedAPDiscovered,
       "wsManagedAPFailed": wsManagedAPFailed,
       "wsManagedAPUnknownProtocol": wsManagedAPUnknownProtocol,
       "wsAPAssociationFailure": wsAPAssociationFailure,
       "wsAPAuthenticationFailure": wsAPAuthenticationFailure,
       "wsRFScanRogueAPDetected": wsRFScanRogueAPDetected,
       "wsRFScanAPDetected": wsRFScanAPDetected,
       "wsRFScanNewClientDetected": wsRFScanNewClientDetected,
       "wsClientAssociationDetected": wsClientAssociationDetected,
       "wsClientDisassociationDetected": wsClientDisassociationDetected,
       "wsClientRoamDetected": wsClientRoamDetected,
       "wsClientAssociationFailure": wsClientAssociationFailure,
       "wsClientAuthenticationFailure": wsClientAuthenticationFailure,
       "wsAdHocClientDetected": wsAdHocClientDetected,
       "wsWLANBandwidthUtilizationExceeded": wsWLANBandwidthUtilizationExceeded,
       "wsAdHocClientListFull": wsAdHocClientListFull,
       "wsPeerSwitchConfigurationCommandReceived": wsPeerSwitchConfigurationCommandReceived,
       "wsPeerSwitchManagedAPLimitExceeded": wsPeerSwitchManagedAPLimitExceeded,
       "wsPeerSwitchClientLimitExceeded": wsPeerSwitchClientLimitExceeded,
       "wsClusterControllerElected": wsClusterControllerElected,
       "wsClusterMaxAPExceeded": wsClusterMaxAPExceeded,
       "wsRoguesPresent": wsRoguesPresent,
       "wsDetectedClientListFull": wsDetectedClientListFull,
       "wsRogueClientsPresent": wsRogueClientsPresent,
       "wsChannelPlanAlgoComplete": wsChannelPlanAlgoComplete,
       "wsPowerPlanAlgoComplete": wsPowerPlanAlgoComplete,
       "wsLocallyManagedAPLimitExceeded": wsLocallyManagedAPLimitExceeded,
       "wsGlobalConfig": wsGlobalConfig,
       "wsMode": wsMode,
       "wsCountryCode": wsCountryCode,
       "wsPeerGroupId": wsPeerGroupId,
       "wsAPValidationMethod": wsAPValidationMethod,
       "wsAPAuthenticationMode": wsAPAuthenticationMode,
       "wsClientRoamAgeTime": wsClientRoamAgeTime,
       "wsRFScanAgeTime": wsRFScanAgeTime,
       "wsAPFailureAgeTime": wsAPFailureAgeTime,
       "wsAdHocClientAgeTime": wsAdHocClientAgeTime,
       "wsDetectedClientAgeTime": wsDetectedClientAgeTime,
       "wsValidAPConfigTable": wsValidAPConfigTable,
       "wsValidAPConfigEntry": wsValidAPConfigEntry,
       "wsAPMacAddress": wsAPMacAddress,
       "wsAPLocation": wsAPLocation,
       "wsAPMode": wsAPMode,
       "wsAPAuthenticationPasswd": wsAPAuthenticationPasswd,
       "wsUseAPProfileId": wsUseAPProfileId,
       "wsAPRadio1Channel": wsAPRadio1Channel,
       "wsAPRadio2Channel": wsAPRadio2Channel,
       "wsAPRadio1TxPower": wsAPRadio1TxPower,
       "wsAPRadio2TxPower": wsAPRadio2TxPower,
       "wsAPStandaloneExpectedChannel": wsAPStandaloneExpectedChannel,
       "wsAPStandaloneExpectedSecurity": wsAPStandaloneExpectedSecurity,
       "wsAPStandaloneExpectedSsid": wsAPStandaloneExpectedSsid,
       "wsAPStandaloneExpectedWds": wsAPStandaloneExpectedWds,
       "wsAPStandaloneExpectedWired": wsAPStandaloneExpectedWired,
       "wsAPConfigRowStatus": wsAPConfigRowStatus,
       "wsGlobalStatus": wsGlobalStatus,
       "wsIPAddress": wsIPAddress,
       "wsOperationalStatus": wsOperationalStatus,
       "wsOperationalStatusDisableReason": wsOperationalStatusDisableReason,
       "wsTotalPeerSwitches": wsTotalPeerSwitches,
       "wsTotalAPs": wsTotalAPs,
       "wsTotalManagedAPs": wsTotalManagedAPs,
       "wsTotalStandaloneAPs": wsTotalStandaloneAPs,
       "wsTotalDiscoveredAPs": wsTotalDiscoveredAPs,
       "wsTotalConnectionFailedAPs": wsTotalConnectionFailedAPs,
       "wsTotalRogueAPs": wsTotalRogueAPs,
       "wsTotalUnknownAPs": wsTotalUnknownAPs,
       "wsMaximumManagedAPsInPeerGroup": wsMaximumManagedAPsInPeerGroup,
       "wsTotalClients": wsTotalClients,
       "wsTotalAuthenticatedClients": wsTotalAuthenticatedClients,
       "wsMaximumAssociatedClients": wsMaximumAssociatedClients,
       "wsWLANUtilization": wsWLANUtilization,
       "wsGlobalStatusRegulatoryDomainFor2GHz": wsGlobalStatusRegulatoryDomainFor2GHz,
       "wsGlobalStatusRegulatoryDomainFor5GHz": wsGlobalStatusRegulatoryDomainFor5GHz,
       "wsGlobalPeerConfigRequestAction": wsGlobalPeerConfigRequestAction,
       "wsGlobalPeerConfigRequestStatus": wsGlobalPeerConfigRequestStatus,
       "wsGlobalPeerConfigReceiveStatus": wsGlobalPeerConfigReceiveStatus,
       "wsGlobalPeerConfigSwitchIp": wsGlobalPeerConfigSwitchIp,
       "wsGlobalPeerConfigReceived": wsGlobalPeerConfigReceived,
       "wsGlobalPeerConfigReceivedTimestamp": wsGlobalPeerConfigReceivedTimestamp,
       "wsClusterControllerIndicator": wsClusterControllerIndicator,
       "wsClusterController": wsClusterController,
       "wsRogueAPMitigationCount": wsRogueAPMitigationCount,
       "wsRogueAPMitigationLimit": wsRogueAPMitigationLimit,
       "wsRogueAPAcknowledgeAll": wsRogueAPAcknowledgeAll,
       "wsTotalDetectedClients": wsTotalDetectedClients,
       "wsMaximumDetectedClients": wsMaximumDetectedClients,
       "wsMaximumDetectedClientPreAuthenticationHistoryEntries": wsMaximumDetectedClientPreAuthenticationHistoryEntries,
       "wsTotalDetectedClientPreAuthenticationHistoryEntries": wsTotalDetectedClientPreAuthenticationHistoryEntries,
       "wsMaximumDetectedClientRoamHistoryEntries": wsMaximumDetectedClientRoamHistoryEntries,
       "wsTotalDetectedClientRoamHistoryEntries": wsTotalDetectedClientRoamHistoryEntries,
       "wsRegenerateX509CertificateAction": wsRegenerateX509CertificateAction,
       "wsRegenerateX509CertificateStatus": wsRegenerateX509CertificateStatus,
       "wsNetworkMutualAuthenticationStatus": wsNetworkMutualAuthenticationStatus,
       "wsTotalProvisioningAPs": wsTotalProvisioningAPs,
       "wsMaximumProvisioningAPs": wsMaximumProvisioningAPs,
       "wsGlobalStatistics": wsGlobalStatistics,
       "wsTotalWLANBytesTransmitted": wsTotalWLANBytesTransmitted,
       "wsTotalWLANBytesRecvd": wsTotalWLANBytesRecvd,
       "wsTotalWLANPktsTransmitted": wsTotalWLANPktsTransmitted,
       "wsTotalWLANPktsRecvd": wsTotalWLANPktsRecvd,
       "wsAllStatisticsReset": wsAllStatisticsReset,
       "wsAllStatisticsResetStatus": wsAllStatisticsResetStatus,
       "wsTotalWLANBytesTransmitDropped": wsTotalWLANBytesTransmitDropped,
       "wsTotalWLANBytesRecvDropped": wsTotalWLANBytesRecvDropped,
       "wsTotalWLANPktsTransmitDropped": wsTotalWLANPktsTransmitDropped,
       "wsTotalWLANPktsRecvDropped": wsTotalWLANPktsRecvDropped,
       "wsTotalWLANDistTunnelPktsTransmitted": wsTotalWLANDistTunnelPktsTransmitted,
       "wsTotalWLANDistTunnelRoamedClients": wsTotalWLANDistTunnelRoamedClients,
       "wsTotalWLANDistTunnelClientDenials": wsTotalWLANDistTunnelClientDenials,
       "wsPeerConfiguration": wsPeerConfiguration,
       "wsPeerConfigurationGlobal": wsPeerConfigurationGlobal,
       "wsPeerConfigurationDiscovery": wsPeerConfigurationDiscovery,
       "wsPeerConfigurationAPDatabase": wsPeerConfigurationAPDatabase,
       "wsPeerConfigurationChannelPower": wsPeerConfigurationChannelPower,
       "wsPeerConfigurationAPProfiles": wsPeerConfigurationAPProfiles,
       "wsPeerConfigurationKnownClients": wsPeerConfigurationKnownClients,
       "wsPeerConfigurationCaptivePortal": wsPeerConfigurationCaptivePortal,
       "wsPeerConfigurationRadiusClient": wsPeerConfigurationRadiusClient,
       "wsPeerConfigurationQosAcl": wsPeerConfigurationQosAcl,
       "wsPeerConfigurationQosDiffServ": wsPeerConfigurationQosDiffServ,
       "wsPeerConfigurationWdsGroup": wsPeerConfigurationWdsGroup,
       "wsPeerConfigurationDeviceLocation": wsPeerConfigurationDeviceLocation,
       "wsClusterPriority": wsClusterPriority,
       "wsAPClientQosMode": wsAPClientQosMode,
       "wsAPAutoUpgradeMode": wsAPAutoUpgradeMode,
       "wsDistTunnelIdleTimeout": wsDistTunnelIdleTimeout,
       "wsDistTunnelMaxTimeout": wsDistTunnelMaxTimeout,
       "wsDistTunnelMaxMcastRepl": wsDistTunnelMaxMcastRepl,
       "wsDistTunnelMaxClients": wsDistTunnelMaxClients,
       "wsMACAuthenticationMode": wsMACAuthenticationMode,
       "wsKnownClientTable": wsKnownClientTable,
       "wsKnownClientEntry": wsKnownClientEntry,
       "wsKnownClientMacAddress": wsKnownClientMacAddress,
       "wsKnownClientAuthAction": wsKnownClientAuthAction,
       "wsKnownClientName": wsKnownClientName,
       "wsKnownClientRowStatus": wsKnownClientRowStatus,
       "wsWidsSecurity": wsWidsSecurity,
       "wsWidsApSecurity": wsWidsApSecurity,
       "rogueAdminConfig": rogueAdminConfig,
       "rogueUnknownApManagedSsid": rogueUnknownApManagedSsid,
       "rogueFakeManagedApManagedSsid": rogueFakeManagedApManagedSsid,
       "rogueManagedApNoSsid": rogueManagedApNoSsid,
       "rogueManagedApInvalidChannel": rogueManagedApInvalidChannel,
       "rogueManagedSsidInvalidSecurity": rogueManagedSsidInvalidSecurity,
       "rogueManagedApInvalidSsid": rogueManagedApInvalidSsid,
       "rogueApIllegalChannel": rogueApIllegalChannel,
       "rogueStandaloneApInvalidConfig": rogueStandaloneApInvalidConfig,
       "rogueUnexpectedWdsDevice": rogueUnexpectedWdsDevice,
       "rogueUnmanagedApWiredNetwork": rogueUnmanagedApWiredNetwork,
       "wiredNetworkDetectionInterval": wiredNetworkDetectionInterval,
       "rogueDetectedTrapInterval": rogueDetectedTrapInterval,
       "apDeauthenticationAttack": apDeauthenticationAttack,
       "wsWidsClientSecurity": wsWidsClientSecurity,
       "rogueDetectedTrapIntvl": rogueDetectedTrapIntvl,
       "knownClientDatabaseTest": knownClientDatabaseTest,
       "authReqTransmitRate": authReqTransmitRate,
       "probeReqTransmitRate": probeReqTransmitRate,
       "deauthReqTransmitRate": deauthReqTransmitRate,
       "maxFailingAuthentication": maxFailingAuthentication,
       "authWithUnknownAP": authWithUnknownAP,
       "clientThreatMitigation": clientThreatMitigation,
       "deauthThresholdInterval": deauthThresholdInterval,
       "deauthThresholdValue": deauthThresholdValue,
       "authThresholdInterval": authThresholdInterval,
       "authThresholdValue": authThresholdValue,
       "probeThresholdInterval": probeThresholdInterval,
       "probeThresholdValue": probeThresholdValue,
       "authFailureThreshold": authFailureThreshold,
       "knownClientDatabaseLocation": knownClientDatabaseLocation,
       "knownClientDatabaseRadiusServerName": knownClientDatabaseRadiusServerName,
       "knownClientDatabaseRadiusServerStatus": knownClientDatabaseRadiusServerStatus,
       "notInOUIDatabase": notInOUIDatabase,
       "wsGlobalRadiusConfiguration": wsGlobalRadiusConfiguration,
       "wsRadiusConfiguration": wsRadiusConfiguration,
       "wsAuthRadiusServerName": wsAuthRadiusServerName,
       "wsAuthRadiusServerConfiguredStatus": wsAuthRadiusServerConfiguredStatus,
       "wsAcctRadiusServerName": wsAcctRadiusServerName,
       "wsAcctRadiusServerConfiguredStatus": wsAcctRadiusServerConfiguredStatus,
       "wsRadiusAcctMode": wsRadiusAcctMode,
       "wsSwitchStatusTable": wsSwitchStatusTable,
       "wsSwitchStatusEntry": wsSwitchStatusEntry,
       "wsSwitchIPAddress": wsSwitchIPAddress,
       "wsSwitchClusterPriority": wsSwitchClusterPriority,
       "wsSwitchAPImageDownloadMode": wsSwitchAPImageDownloadMode,
       "wsSwitchTotalAPs": wsSwitchTotalAPs,
       "wsSwitchManagedAPs": wsSwitchManagedAPs,
       "wsSwitchDiscoveredAPs": wsSwitchDiscoveredAPs,
       "wsSwitchConnectionFailedAPs": wsSwitchConnectionFailedAPs,
       "wsSwitchMaximumManagedAPs": wsSwitchMaximumManagedAPs,
       "wsSwitchTotalClients": wsSwitchTotalClients,
       "wsSwitchAuthenticatedClients": wsSwitchAuthenticatedClients,
       "wsSwitchWLANUtilization": wsSwitchWLANUtilization,
       "wsSwitchDistTunnelClients": wsSwitchDistTunnelClients,
       "wsSwitchStatisticsTable": wsSwitchStatisticsTable,
       "wsSwitchStatisticsEntry": wsSwitchStatisticsEntry,
       "wsSwitchWLANBytesTransmitted": wsSwitchWLANBytesTransmitted,
       "wsSwitchWLANBytesReceived": wsSwitchWLANBytesReceived,
       "wsSwitchWLANPktsTransmitted": wsSwitchWLANPktsTransmitted,
       "wsSwitchWLANPktsReceived": wsSwitchWLANPktsReceived,
       "wsSwitchWLANBytesTransmitDropped": wsSwitchWLANBytesTransmitDropped,
       "wsSwitchWLANBytesRecvDropped": wsSwitchWLANBytesRecvDropped,
       "wsSwitchWLANPktsTransmitDropped": wsSwitchWLANPktsTransmitDropped,
       "wsSwitchWLANPktsRecvDropped": wsSwitchWLANPktsRecvDropped,
       "wsAutoIPAssignMode": wsAutoIPAssignMode,
       "wsSwitchStaticIPAddress": wsSwitchStaticIPAddress,
       "wsGlobalTspecConfiguration": wsGlobalTspecConfiguration,
       "wsTspecViolationReportInterval": wsTspecViolationReportInterval,
       "networkMutualAuthMode": networkMutualAuthMode,
       "unmanagedAPReprovisioning": unmanagedAPReprovisioning,
       "apProvisionDbAgeTime": apProvisionDbAgeTime,
       "switchProvisioning": switchProvisioning,
       "wsIpBasePort": wsIpBasePort,
       "devLocMeasurementSys": devLocMeasurementSys,
       "devLocRfScanLocMode": devLocRfScanLocMode,
       "devLocRfScanLocInterval": devLocRfScanLocInterval,
       "discovery": discovery,
       "wsIPPollMode": wsIPPollMode,
       "wsL2DiscoveryMode": wsL2DiscoveryMode,
       "wsIPPollListTable": wsIPPollListTable,
       "wsIPPollListEntry": wsIPPollListEntry,
       "wsPollIpAddress": wsPollIpAddress,
       "wsPollIPStatus": wsPollIPStatus,
       "wsIPPollRowStatus": wsIPPollRowStatus,
       "wsL2DiscoveryVlanListTable": wsL2DiscoveryVlanListTable,
       "wsL2DiscoveryVlanListEntry": wsL2DiscoveryVlanListEntry,
       "wsL2DiscoveryVlanId": wsL2DiscoveryVlanId,
       "wsL2DiscoveryVlanRowStatus": wsL2DiscoveryVlanRowStatus,
       "wsIPPollListMaxNumOfEntries": wsIPPollListMaxNumOfEntries,
       "wsIPPollListNumOfConfigEntries": wsIPPollListNumOfConfigEntries,
       "wsIPPollListNumOfPolledEntries": wsIPPollListNumOfPolledEntries,
       "wsIPPollListNumOfNotPolledEntries": wsIPPollListNumOfNotPolledEntries,
       "wsIPPollListNumOfDiscoveredEntries": wsIPPollListNumOfDiscoveredEntries,
       "wsIPPollListNumOfDiscoveredFailedEntries": wsIPPollListNumOfDiscoveredFailedEntries,
       "apProfile": apProfile,
       "wsAPProfileTable": wsAPProfileTable,
       "wsAPProfileEntry": wsAPProfileEntry,
       "wsAPProfileId": wsAPProfileId,
       "wsAPProfileName": wsAPProfileName,
       "wsAPProfileState": wsAPProfileState,
       "wsAPProfileRowStatus": wsAPProfileRowStatus,
       "wsCopyAPProfileToProfileId": wsCopyAPProfileToProfileId,
       "wsAPProfileApply": wsAPProfileApply,
       "wsAPHardwareTypeID": wsAPHardwareTypeID,
       "wsAPWiredDetectionVlanId": wsAPWiredDetectionVlanId,
       "wsAPProfileDisconnAPFwdingMode": wsAPProfileDisconnAPFwdingMode,
       "wsAPProfileDisconnAPMgmtMode": wsAPProfileDisconnAPMgmtMode,
       "wsAPProfileAeroScoutSupportMode": wsAPProfileAeroScoutSupportMode,
       "wsAPProfileRadioTable": wsAPProfileRadioTable,
       "wsAPProfileRadioEntry": wsAPProfileRadioEntry,
       "wsAPRadioInterface": wsAPRadioInterface,
       "wsAPRadioAdminMode": wsAPRadioAdminMode,
       "wsAPRadioFrequency": wsAPRadioFrequency,
       "wsAPRadioOtherChannelsScanMode": wsAPRadioOtherChannelsScanMode,
       "wsAPRadioOtherChannelsScanInterval": wsAPRadioOtherChannelsScanInterval,
       "wsAPRadioSentryScanMode": wsAPRadioSentryScanMode,
       "wsAPRadioSentryScanChannel": wsAPRadioSentryScanChannel,
       "wsAPRadioScanDuration": wsAPRadioScanDuration,
       "wsAPRadioRateLimitMode": wsAPRadioRateLimitMode,
       "wsAPRadioRateLimit": wsAPRadioRateLimit,
       "wsAPRadioRateLimitBurst": wsAPRadioRateLimitBurst,
       "wsAPRadioBeaconInterval": wsAPRadioBeaconInterval,
       "wsAPRadioDTIMPeriod": wsAPRadioDTIMPeriod,
       "wsAPRadioFragmentationThreshold": wsAPRadioFragmentationThreshold,
       "wsAPRadioRTSThreshold": wsAPRadioRTSThreshold,
       "wsAPRadioShortRetryLimit": wsAPRadioShortRetryLimit,
       "wsAPRadioLongRetryLimit": wsAPRadioLongRetryLimit,
       "wsAPRadioMaxTransmitLifetime": wsAPRadioMaxTransmitLifetime,
       "wsAPRadioMaxReceiveLifetime": wsAPRadioMaxReceiveLifetime,
       "wsAPRadioMaxClients": wsAPRadioMaxClients,
       "wsAPRadioAutoPowerMode": wsAPRadioAutoPowerMode,
       "wsAPRadioTxPower": wsAPRadioTxPower,
       "wsAPRadioWMMMode": wsAPRadioWMMMode,
       "wsAPRadioLoadBalancingMode": wsAPRadioLoadBalancingMode,
       "wsAPRadioUtilization": wsAPRadioUtilization,
       "wsAPRadioAutoChannelMode": wsAPRadioAutoChannelMode,
       "wsAPRadioStationIsolationMode": wsAPRadioStationIsolationMode,
       "wsAPRadioChannelBandwidth": wsAPRadioChannelBandwidth,
       "wsAPRadioPrimaryChannel": wsAPRadioPrimaryChannel,
       "wsAPRadioProtectionMode": wsAPRadioProtectionMode,
       "wsAPRadioShortGuardInterval": wsAPRadioShortGuardInterval,
       "wsAPRadioSTBCMode": wsAPRadioSTBCMode,
       "wsAPRadioMulticastTxRate": wsAPRadioMulticastTxRate,
       "wsAPRadioAPSDMode": wsAPRadioAPSDMode,
       "wsAPRadioNoAckMode": wsAPRadioNoAckMode,
       "wsAPRadioResourceMeasEnabled": wsAPRadioResourceMeasEnabled,
       "wsAPRadioQOSEDCATemplate": wsAPRadioQOSEDCATemplate,
       "wsAPRadioMinTxPower": wsAPRadioMinTxPower,
       "wsAPProfileRadioSupportedRatesTable": wsAPProfileRadioSupportedRatesTable,
       "wsAPProfileRadioSupportedRatesEntry": wsAPProfileRadioSupportedRatesEntry,
       "wsSupportedDataRate": wsSupportedDataRate,
       "wsAPProfileRadioSupportedDataMode": wsAPProfileRadioSupportedDataMode,
       "wsAPProfileRadioBasicRatesTable": wsAPProfileRadioBasicRatesTable,
       "wsAPProfileRadioBasicRatesEntry": wsAPProfileRadioBasicRatesEntry,
       "wsBasicDataRate": wsBasicDataRate,
       "wsAPProfileRadioBasicDataMode": wsAPProfileRadioBasicDataMode,
       "wsAPProfileVAPTable": wsAPProfileVAPTable,
       "wsAPProfileVAPEntry": wsAPProfileVAPEntry,
       "wsVAPId": wsVAPId,
       "wsVAPMode": wsVAPMode,
       "wsVAPNetworkId": wsVAPNetworkId,
       "wsAPProfileQOSTable": wsAPProfileQOSTable,
       "wsAPProfileQOSEntry": wsAPProfileQOSEntry,
       "wsQOSQueueId": wsQOSQueueId,
       "wsAPEDCAAIFS": wsAPEDCAAIFS,
       "wsAPEDCAMinContentionWindow": wsAPEDCAMinContentionWindow,
       "wsAPEDCAMaxContentionWindow": wsAPEDCAMaxContentionWindow,
       "wsAPEDCAMaxBurst": wsAPEDCAMaxBurst,
       "wsStationEDCAAIFS": wsStationEDCAAIFS,
       "wsStationEDCAMinContentionWindow": wsStationEDCAMinContentionWindow,
       "wsStationEDCAMaxContentionWindow": wsStationEDCAMaxContentionWindow,
       "wsStationEDCATXOPLimit": wsStationEDCATXOPLimit,
       "wsNetworkTable": wsNetworkTable,
       "wsNetworkEntry": wsNetworkEntry,
       "wsNetworkId": wsNetworkId,
       "wsNetworkIdRowStatus": wsNetworkIdRowStatus,
       "wsNetworkSSID": wsNetworkSSID,
       "wsNetworkDefaultVLANId": wsNetworkDefaultVLANId,
       "wsNetworkHideSSIDMode": wsNetworkHideSSIDMode,
       "wsNetworkDenyBcastMode": wsNetworkDenyBcastMode,
       "wsNetworkMACAuthenticationMode": wsNetworkMACAuthenticationMode,
       "wsNetworkRadiusAccountingMode": wsNetworkRadiusAccountingMode,
       "wsNetworkSecurityMode": wsNetworkSecurityMode,
       "wsNetworkWPAVersionsSupported": wsNetworkWPAVersionsSupported,
       "wsNetworkWPACipherSuites": wsNetworkWPACipherSuites,
       "wsNetworkWPAKeyType": wsNetworkWPAKeyType,
       "wsNetworkWPAKey": wsNetworkWPAKey,
       "wsNetworkWPA2PreAuthenticationMode": wsNetworkWPA2PreAuthenticationMode,
       "wsNetworkWPA2PreAuthenticationLimit": wsNetworkWPA2PreAuthenticationLimit,
       "wsNetworkWPA2RoambackKeyCacheHoldtime": wsNetworkWPA2RoambackKeyCacheHoldtime,
       "wsNetworkStaticWEPAuthenticationMode": wsNetworkStaticWEPAuthenticationMode,
       "wsNetworkUseWEPTransferKeyIndex": wsNetworkUseWEPTransferKeyIndex,
       "wsNetworkWEPKeyType": wsNetworkWEPKeyType,
       "wsNetworkWEPKeyLength": wsNetworkWEPKeyLength,
       "wsNetworkWEPKey1": wsNetworkWEPKey1,
       "wsNetworkWEPKey2": wsNetworkWEPKey2,
       "wsNetworkWEPKey3": wsNetworkWEPKey3,
       "wsNetworkWEPKey4": wsNetworkWEPKey4,
       "wsClearNetworkEntry": wsClearNetworkEntry,
       "wsNetworkRedirectMode": wsNetworkRedirectMode,
       "wsNetworkRedirectURL": wsNetworkRedirectURL,
       "wsIfNumber": wsIfNumber,
       "wsNetworkAuthRadiusServerName": wsNetworkAuthRadiusServerName,
       "wsNetworkAuthRadiusServerConfiguredStatus": wsNetworkAuthRadiusServerConfiguredStatus,
       "wsNetworkAcctRadiusServerName": wsNetworkAcctRadiusServerName,
       "wsNetworkAcctRadiusServerConfiguredStatus": wsNetworkAcctRadiusServerConfiguredStatus,
       "wsUseNetworkRadiusConfig": wsUseNetworkRadiusConfig,
       "wsNetworkDistTunnelMode": wsNetworkDistTunnelMode,
       "wsNetworkBcastKeyRefreshRate": wsNetworkBcastKeyRefreshRate,
       "wsNetworkSessionKeyRefreshRate": wsNetworkSessionKeyRefreshRate,
       "wsNetworkARPSuppressionMode": wsNetworkARPSuppressionMode,
       "wsNetworkBandSteerMode": wsNetworkBandSteerMode,
       "wsNetworkClientQosTable": wsNetworkClientQosTable,
       "wsNetworkClientQosEntry": wsNetworkClientQosEntry,
       "wsNetworkClientQosBandwidthLimitDown": wsNetworkClientQosBandwidthLimitDown,
       "wsNetworkClientQosBandwidthLimitUp": wsNetworkClientQosBandwidthLimitUp,
       "wsNetworkClientQosAccessControlDownType": wsNetworkClientQosAccessControlDownType,
       "wsNetworkClientQosAccessControlDownName": wsNetworkClientQosAccessControlDownName,
       "wsNetworkClientQosAccessControlUpType": wsNetworkClientQosAccessControlUpType,
       "wsNetworkClientQosAccessControlUpName": wsNetworkClientQosAccessControlUpName,
       "wsNetworkClientQosDiffservPolicyDownType": wsNetworkClientQosDiffservPolicyDownType,
       "wsNetworkClientQosDiffservPolicyDownName": wsNetworkClientQosDiffservPolicyDownName,
       "wsNetworkClientQosDiffservPolicyUpType": wsNetworkClientQosDiffservPolicyUpType,
       "wsNetworkClientQosDiffservPolicyUpName": wsNetworkClientQosDiffservPolicyUpName,
       "wsNetworkClientQosMode": wsNetworkClientQosMode,
       "wsAPProfileRadioSupportedChannelsTable": wsAPProfileRadioSupportedChannelsTable,
       "wsAPProfileRadioSupportedChannelsEntry": wsAPProfileRadioSupportedChannelsEntry,
       "wsSupportedChannel": wsSupportedChannel,
       "wsAPProfileRadioEligibleChannelsTable": wsAPProfileRadioEligibleChannelsTable,
       "wsAPProfileRadioEligibleChannelsEntry": wsAPProfileRadioEligibleChannelsEntry,
       "wsEligibleChannel": wsEligibleChannel,
       "wsEligibleChannelRowStatus": wsEligibleChannelRowStatus,
       "wsAPProfileRadioTspecTable": wsAPProfileRadioTspecTable,
       "wsAPProfileRadioTspecEntry": wsAPProfileRadioTspecEntry,
       "wsAPRadioTspecMode": wsAPRadioTspecMode,
       "wsAPRadioTspecVoiceAcmMode": wsAPRadioTspecVoiceAcmMode,
       "wsAPRadioTspecVideoAcmMode": wsAPRadioTspecVideoAcmMode,
       "wsAPRadioTspecVoiceAcmLimit": wsAPRadioTspecVoiceAcmLimit,
       "wsAPRadioTspecVideoAcmLimit": wsAPRadioTspecVideoAcmLimit,
       "wsAPRadioTspecRoamReserveLimit": wsAPRadioTspecRoamReserveLimit,
       "wsAPRadioTspecApInactivityTimeout": wsAPRadioTspecApInactivityTimeout,
       "wsAPRadioTspecStaInactivityTimeout": wsAPRadioTspecStaInactivityTimeout,
       "wsAPRadioTspecLegacyWmmQueueMapMode": wsAPRadioTspecLegacyWmmQueueMapMode,
       "wsAPProfileRadioMCSIndexTable": wsAPProfileRadioMCSIndexTable,
       "wsAPProfileRadioMCSIndexEntry": wsAPProfileRadioMCSIndexEntry,
       "wsAPRadioMCSIndexValue": wsAPRadioMCSIndexValue,
       "wsAPRadioMCSIndexAvailable": wsAPRadioMCSIndexAvailable,
       "apCodeDownload": apCodeDownload,
       "wsAPCodeDownloadServerIP": wsAPCodeDownloadServerIP,
       "wsAPImageTypeFileTable": wsAPImageTypeFileTable,
       "wsAPImageTypeFileEntry": wsAPImageTypeFileEntry,
       "wsAPImageFilePath": wsAPImageFilePath,
       "wsAPImageFileName": wsAPImageFileName,
       "wsAPCodeDownloadMACAddress": wsAPCodeDownloadMACAddress,
       "wsAPCodeDownloadGroupSize": wsAPCodeDownloadGroupSize,
       "wsAPCodeDownloadImageType": wsAPCodeDownloadImageType,
       "wsAPCodeDownloadStatus": wsAPCodeDownloadStatus,
       "wsAPCodeDownloadTotalCount": wsAPCodeDownloadTotalCount,
       "wsAPCodeDownloadSuccessCount": wsAPCodeDownloadSuccessCount,
       "wsAPCodeDownloadFailureCount": wsAPCodeDownloadFailureCount,
       "wsAPCodeDownloadAbortCount": wsAPCodeDownloadAbortCount,
       "wsAPCodeDownloadAbort": wsAPCodeDownloadAbort,
       "rfManagement": rfManagement,
       "wsChannelPlanTable": wsChannelPlanTable,
       "wsChannelPlanEntry": wsChannelPlanEntry,
       "wsChannelPlan": wsChannelPlan,
       "wsChannelPlanMode": wsChannelPlanMode,
       "wsChannelPlanInterval": wsChannelPlanInterval,
       "wsChannelPlanTime": wsChannelPlanTime,
       "wsChannelPlanHistoryDepth": wsChannelPlanHistoryDepth,
       "wsChannelPlanOperatingStatus": wsChannelPlanOperatingStatus,
       "wsChannelPlanLastIterationStatus": wsChannelPlanLastIterationStatus,
       "wsChannelPlanManualAction": wsChannelPlanManualAction,
       "wsChannelPlanManualStatus": wsChannelPlanManualStatus,
       "wsChannelPlanLastAlgorithmTime": wsChannelPlanLastAlgorithmTime,
       "wsChannelPlanChangeThreshold": wsChannelPlanChangeThreshold,
       "wsChannelPlanIgnoreUnamangedAPs": wsChannelPlanIgnoreUnamangedAPs,
       "wsChannelPlanNumOfRadios": wsChannelPlanNumOfRadios,
       "wsChannelPlanNumOfRadiosAnalysed": wsChannelPlanNumOfRadiosAnalysed,
       "wsChannelPlanNumOfRadiosScanned": wsChannelPlanNumOfRadiosScanned,
       "wsChannelPlanNumOfRadiosChanged": wsChannelPlanNumOfRadiosChanged,
       "wsChannelPlanNumOfRadiosChangedToOrigChannel": wsChannelPlanNumOfRadiosChangedToOrigChannel,
       "wsChannelPlanEstimatedTimeOfCompletion": wsChannelPlanEstimatedTimeOfCompletion,
       "wsChannelPlanPercentageComplete": wsChannelPlanPercentageComplete,
       "wsChannelPlanChangeThresholdAdj": wsChannelPlanChangeThresholdAdj,
       "wsChannelPlanManagedAPFailureInterval": wsChannelPlanManagedAPFailureInterval,
       "wsChannelPlanRunOnManagedApFailure": wsChannelPlanRunOnManagedApFailure,
       "wsChannelPlanHistoryTable": wsChannelPlanHistoryTable,
       "wsChannelPlanHistoryEntry": wsChannelPlanHistoryEntry,
       "wsChannelPlanHistory": wsChannelPlanHistory,
       "wsChannelPlanAPMacAddress": wsChannelPlanAPMacAddress,
       "wsChannelPlanAPRadioInterface": wsChannelPlanAPRadioInterface,
       "wsChannelPlanAPLocation": wsChannelPlanAPLocation,
       "wsChannelPlanAPHistoryIteration": wsChannelPlanAPHistoryIteration,
       "wsChannelPlanAPChannel": wsChannelPlanAPChannel,
       "wsChannelPlanManualProposedAdjustmentTable": wsChannelPlanManualProposedAdjustmentTable,
       "wsChannelPlanManualProposedAdjustmentEntry": wsChannelPlanManualProposedAdjustmentEntry,
       "wsChannelPlanManual": wsChannelPlanManual,
       "wsChannelPlanManualMacAddress": wsChannelPlanManualMacAddress,
       "wsChannelPlanManualAPRadioInterface": wsChannelPlanManualAPRadioInterface,
       "wsChannelPlanManualCurrentChannel": wsChannelPlanManualCurrentChannel,
       "wsChannelPlanManualNewChannel": wsChannelPlanManualNewChannel,
       "wsPowerAdjustmentMode": wsPowerAdjustmentMode,
       "wsPowerAdjustmentStrength": wsPowerAdjustmentStrength,
       "wsPowerManualProposedAdjustmentAction": wsPowerManualProposedAdjustmentAction,
       "wsManualPowerAdjustmentStatus": wsManualPowerAdjustmentStatus,
       "wsPowerManualProposedAdjustmentTable": wsPowerManualProposedAdjustmentTable,
       "wsPowerManualProposedAdjustmentEntry": wsPowerManualProposedAdjustmentEntry,
       "wsPowerManualProposedAdjustmentAPMacAddress": wsPowerManualProposedAdjustmentAPMacAddress,
       "wsPowerManualProposedAdjustmentAPRadioInterface": wsPowerManualProposedAdjustmentAPRadioInterface,
       "wsPowerManualProposedAdjustmentAPCurrentTxPower": wsPowerManualProposedAdjustmentAPCurrentTxPower,
       "wsPowerManualProposedAdjustmentAPNewTxPower": wsPowerManualProposedAdjustmentAPNewTxPower,
       "wsPowerPlanOperatingStatus": wsPowerPlanOperatingStatus,
       "wsPowerPlanAvgNumInterferingAPs": wsPowerPlanAvgNumInterferingAPs,
       "wsPowerPlanAvgNumInterferingVAPs": wsPowerPlanAvgNumInterferingVAPs,
       "wsPowerPlanAPNumOpRadios": wsPowerPlanAPNumOpRadios,
       "wsPowerPlanAPNumPwrCycles": wsPowerPlanAPNumPwrCycles,
       "wsPowerPlanGlobalNumPwrChanges": wsPowerPlanGlobalNumPwrChanges,
       "wsPowerPlanGlobalNumPwrInc": wsPowerPlanGlobalNumPwrInc,
       "wsPowerPlanGlobalNumPwrDec": wsPowerPlanGlobalNumPwrDec,
       "wsPowerPlanTimeSinceLastPowerPLan": wsPowerPlanTimeSinceLastPowerPLan,
       "wsChannelPlanPerRadioPerBandTable": wsChannelPlanPerRadioPerBandTable,
       "wsChannelPlanPerRadioPerBandEntry": wsChannelPlanPerRadioPerBandEntry,
       "wsChannelPlanType": wsChannelPlanType,
       "wsChannelPlanAPMacAddr": wsChannelPlanAPMacAddr,
       "wsChannelPlanAPRadioIntf": wsChannelPlanAPRadioIntf,
       "wsChannelPlanAPIsLocal": wsChannelPlanAPIsLocal,
       "wsChannelPlanAPCurrentChannel": wsChannelPlanAPCurrentChannel,
       "wsChannelPlanAPOldChannel": wsChannelPlanAPOldChannel,
       "wsChannelPlanAPStrongestOldSignal": wsChannelPlanAPStrongestOldSignal,
       "wsChannelPlanAPStrongestNewSignal": wsChannelPlanAPStrongestNewSignal,
       "wsChannelPlanAPChannelChangeInd": wsChannelPlanAPChannelChangeInd,
       "wsChannelPlanAPReasonCode": wsChannelPlanAPReasonCode,
       "wsChannelPlanAPStrongestOldManagedAPandSignal": wsChannelPlanAPStrongestOldManagedAPandSignal,
       "wsChannelPlanAPStrongestNewManagedAPandSignal": wsChannelPlanAPStrongestNewManagedAPandSignal,
       "wsChannelPlanAPStrongestOldUnmanagedAPandSignal": wsChannelPlanAPStrongestOldUnmanagedAPandSignal,
       "wsChannelPlanAPStrongestNewUnmanagedAPandSignal": wsChannelPlanAPStrongestNewUnmanagedAPandSignal,
       "wsChannelPlanAPTimeSinceLastChannelChange": wsChannelPlanAPTimeSinceLastChannelChange,
       "wsChannelPlanAPLastChanScanDuration": wsChannelPlanAPLastChanScanDuration,
       "wsPowerPlanPerRadioTable": wsPowerPlanPerRadioTable,
       "wsPowerPlanPerRadioEntry": wsPowerPlanPerRadioEntry,
       "wsPowerPlanAPMacAddress": wsPowerPlanAPMacAddress,
       "wsPowerPlanAPRadioInterface": wsPowerPlanAPRadioInterface,
       "wsPowerPlanAPIsLocal": wsPowerPlanAPIsLocal,
       "wsPowerPlanAPChannel": wsPowerPlanAPChannel,
       "wsPowerPlanAPTxPower": wsPowerPlanAPTxPower,
       "wsPowerPlanAPNumInterferingAPs": wsPowerPlanAPNumInterferingAPs,
       "wsPowerPlanAPNumInterferingVAPs": wsPowerPlanAPNumInterferingVAPs,
       "wsPowerPlanAPStrongestDetectorAP": wsPowerPlanAPStrongestDetectorAP,
       "wsPowerPlanAPStrongestDetectorRadio": wsPowerPlanAPStrongestDetectorRadio,
       "wsPowerPlanAPStrongestDetectorSignal": wsPowerPlanAPStrongestDetectorSignal,
       "wsPowerPlanAPStrongestDetectedNeighbor": wsPowerPlanAPStrongestDetectedNeighbor,
       "wsPowerPlanAPStrongestDetectedSignal": wsPowerPlanAPStrongestDetectedSignal,
       "wsPowerPlanAPLastPwrAdjStatus": wsPowerPlanAPLastPwrAdjStatus,
       "wsPowerPlanAPLastPwrAdjReasonCode": wsPowerPlanAPLastPwrAdjReasonCode,
       "wsPowerPlanAPNumPwrChanges": wsPowerPlanAPNumPwrChanges,
       "wsPowerPlanAPNumPwrInc": wsPowerPlanAPNumPwrInc,
       "wsPowerPlanAPNumPwrDec": wsPowerPlanAPNumPwrDec,
       "wsPowerPlanPerProfileTable": wsPowerPlanPerProfileTable,
       "wsPowerPlanPerProfileEntry": wsPowerPlanPerProfileEntry,
       "wsPowerPlanProfileId": wsPowerPlanProfileId,
       "wsPowerPlanPerProfileAvgNumInterferingAPs": wsPowerPlanPerProfileAvgNumInterferingAPs,
       "wsPowerPlanPerProfileAvgNumInterferingVAPs": wsPowerPlanPerProfileAvgNumInterferingVAPs,
       "wsPowerPlanNumPwrChanges": wsPowerPlanNumPwrChanges,
       "wsPowerPlanNumPwrInc": wsPowerPlanNumPwrInc,
       "wsPowerPlanNumPwrDec": wsPowerPlanNumPwrDec,
       "wsNtwProvisoningAction": wsNtwProvisoningAction,
       "wsNtwProvisioningOperatingStatus": wsNtwProvisioningOperatingStatus,
       "wsNtwProvisioningTimeStamp": wsNtwProvisioningTimeStamp,
       "wsNtwProvisioningChanBGCompletion": wsNtwProvisioningChanBGCompletion,
       "wsNtwProvisioningChanACompletion": wsNtwProvisioningChanACompletion,
       "wsNtwProvisioningPowerPlanCnt": wsNtwProvisioningPowerPlanCnt,
       "managedAP": managedAP,
       "wsManagedAPStatusTable": wsManagedAPStatusTable,
       "wsManagedAPStatusEntry": wsManagedAPStatusEntry,
       "wsManagedAPMacAddress": wsManagedAPMacAddress,
       "wsManagedAPIpAddress": wsManagedAPIpAddress,
       "wsManagedAPVendorId": wsManagedAPVendorId,
       "wsManagedAPSoftwareVersion": wsManagedAPSoftwareVersion,
       "wsManagedAPHWType": wsManagedAPHWType,
       "wsManagedAPSerialNumber": wsManagedAPSerialNumber,
       "wsManagedAPPartNumber": wsManagedAPPartNumber,
       "wsManagedAPDiscoveryReason": wsManagedAPDiscoveryReason,
       "wsManagedAPStatus": wsManagedAPStatus,
       "wsManagedAPAuthenticatedClients": wsManagedAPAuthenticatedClients,
       "wsManagedAPSysUpTime": wsManagedAPSysUpTime,
       "wsManagedAPProfileId": wsManagedAPProfileId,
       "wsManagedAPProfileName": wsManagedAPProfileName,
       "wsManagedAPProtocolVersion": wsManagedAPProtocolVersion,
       "wsManagedAPCodeDownloadStatus": wsManagedAPCodeDownloadStatus,
       "wsManagedAPLocation": wsManagedAPLocation,
       "wsManagedAPLastFailingConfigElement": wsManagedAPLastFailingConfigElement,
       "wsManagedAPConfigFailureErrMsg": wsManagedAPConfigFailureErrMsg,
       "wsManagedAPReset": wsManagedAPReset,
       "wsManagedAPResetStatus": wsManagedAPResetStatus,
       "wsManagedAPFailedEntryPurge": wsManagedAPFailedEntryPurge,
       "wsManagedAPDebugPassword": wsManagedAPDebugPassword,
       "wsManagedAPDebugMode": wsManagedAPDebugMode,
       "wsManagedAPDebugStatus": wsManagedAPDebugStatus,
       "wsManagedAPAge": wsManagedAPAge,
       "wsManagedAPManagingSwitch": wsManagedAPManagingSwitch,
       "wsManagedAPSwitchMacAddress": wsManagedAPSwitchMacAddress,
       "wsManagedAPSwitchIpAddress": wsManagedAPSwitchIpAddress,
       "wsManagedAPIpMask": wsManagedAPIpMask,
       "wsManagedAPDistTunnelHomeAPClients": wsManagedAPDistTunnelHomeAPClients,
       "wsManagedAPDistTunnelAssocAPClients": wsManagedAPDistTunnelAssocAPClients,
       "wsManagedAPDistTunnelsTotal": wsManagedAPDistTunnelsTotal,
       "wsManagedAPDistTunnelsMaxMcastRepl": wsManagedAPDistTunnelsMaxMcastRepl,
       "wsManagedAPDistTunnelsMaxVlanMcastRepl": wsManagedAPDistTunnelsMaxVlanMcastRepl,
       "wsManagedAPFailedEntriesPurge": wsManagedAPFailedEntriesPurge,
       "wsManagedAPStatisticsTable": wsManagedAPStatisticsTable,
       "wsManagedAPStatisticsEntry": wsManagedAPStatisticsEntry,
       "wsManagedAPWLANPktsRecvd": wsManagedAPWLANPktsRecvd,
       "wsManagedAPWLANBytesRecvd": wsManagedAPWLANBytesRecvd,
       "wsManagedAPWLANPktsTransmitted": wsManagedAPWLANPktsTransmitted,
       "wsManagedAPWLANBytesTransmitted": wsManagedAPWLANBytesTransmitted,
       "wsManagedAPEthernetPktsRecvd": wsManagedAPEthernetPktsRecvd,
       "wsManagedAPEthernetBytesRecvd": wsManagedAPEthernetBytesRecvd,
       "wsManagedAPEthernetMcastPktsRecvd": wsManagedAPEthernetMcastPktsRecvd,
       "wsManagedAPEthernetPktsTransmitted": wsManagedAPEthernetPktsTransmitted,
       "wsManagedAPEthernetBytesTransmitted": wsManagedAPEthernetBytesTransmitted,
       "wsManagedAPEthernetTransmitErrorCount": wsManagedAPEthernetTransmitErrorCount,
       "wsManagedAPEthernetRecvdErrorCount": wsManagedAPEthernetRecvdErrorCount,
       "wsManagedAPCL2TunnelBytesRecvd": wsManagedAPCL2TunnelBytesRecvd,
       "wsManagedAPCL2TunnelPktsRecvd": wsManagedAPCL2TunnelPktsRecvd,
       "wsManagedAPCL2TunnelMcastRecvd": wsManagedAPCL2TunnelMcastRecvd,
       "wsManagedAPCL2TunnelBytesTransmitted": wsManagedAPCL2TunnelBytesTransmitted,
       "wsManagedAPCL2TunnelPktsTransmitted": wsManagedAPCL2TunnelPktsTransmitted,
       "wsManagedAPCL2TunnelMcastTransmitted": wsManagedAPCL2TunnelMcastTransmitted,
       "wsManagedAPWLANPktsRecvDropped": wsManagedAPWLANPktsRecvDropped,
       "wsManagedAPWLANBytesRecvDropped": wsManagedAPWLANBytesRecvDropped,
       "wsManagedAPWLANPktsTransmitDropped": wsManagedAPWLANPktsTransmitDropped,
       "wsManagedAPWLANBytesTransmitDropped": wsManagedAPWLANBytesTransmitDropped,
       "wsManagedAPDistTunnelBytesTransmitted": wsManagedAPDistTunnelBytesTransmitted,
       "wsManagedAPDistTunnelBytesReceived": wsManagedAPDistTunnelBytesReceived,
       "wsManagedAPDistTunnelPacketsTransmitted": wsManagedAPDistTunnelPacketsTransmitted,
       "wsManagedAPDistTunnelPacketsReceived": wsManagedAPDistTunnelPacketsReceived,
       "wsManagedAPDistTunnelMcastPacketsTransmitted": wsManagedAPDistTunnelMcastPacketsTransmitted,
       "wsManagedAPDistTunnelMcastPacketsReceived": wsManagedAPDistTunnelMcastPacketsReceived,
       "wsManagedAPDistTunnelRoamedClients": wsManagedAPDistTunnelRoamedClients,
       "wsManagedAPDistTunnelRoamedClientsIdleTimedOut": wsManagedAPDistTunnelRoamedClientsIdleTimedOut,
       "wsManagedAPDistTunnelRoamedClientsAgeTimedOut": wsManagedAPDistTunnelRoamedClientsAgeTimedOut,
       "wsManagedAPDistTunnelMaxClientLimitSetupDenials": wsManagedAPDistTunnelMaxClientLimitSetupDenials,
       "wsManagedAPDistTunnelMaxReplSetupDenials": wsManagedAPDistTunnelMaxReplSetupDenials,
       "wsManagedAPARPReqsFromBcastToUcast": wsManagedAPARPReqsFromBcastToUcast,
       "wsManagedAPFilteredARPRequest": wsManagedAPFilteredARPRequest,
       "wsManagedAPBroadcastedARPRequests": wsManagedAPBroadcastedARPRequests,
       "wsManagedAPRadioStatusTable": wsManagedAPRadioStatusTable,
       "wsManagedAPRadioStatusEntry": wsManagedAPRadioStatusEntry,
       "wsManagedAPRadioInterface": wsManagedAPRadioInterface,
       "wsManagedAPRadioMacAddress": wsManagedAPRadioMacAddress,
       "wsManagedAPRadioChannel": wsManagedAPRadioChannel,
       "wsManagedAPRadioTxPower": wsManagedAPRadioTxPower,
       "wsManagedAPRadioAuthenticatedClients": wsManagedAPRadioAuthenticatedClients,
       "wsManagedAPRadioWLANUtilization": wsManagedAPRadioWLANUtilization,
       "wsManagedAPRadioFixedChannelIndicator": wsManagedAPRadioFixedChannelIndicator,
       "wsManagedAPRadioMCAStatus": wsManagedAPRadioMCAStatus,
       "wsManagedAPRadioFixedPowerIndicator": wsManagedAPRadioFixedPowerIndicator,
       "wsManagedAPRadioMPAStatus": wsManagedAPRadioMPAStatus,
       "wsManagedAPRadioNeighborCount": wsManagedAPRadioNeighborCount,
       "wsManagedAPRadioFixedChannelAction": wsManagedAPRadioFixedChannelAction,
       "wsManagedAPRadioFixedChannel": wsManagedAPRadioFixedChannel,
       "wsManagedAPRadioFixedPowerAction": wsManagedAPRadioFixedPowerAction,
       "wsManagedAPRadioFixedPower": wsManagedAPRadioFixedPower,
       "wsManagedAPRadioBandwidth": wsManagedAPRadioBandwidth,
       "wsManagedAPRadioResourceMeasEnabled": wsManagedAPRadioResourceMeasEnabled,
       "wsManagedAPRadioStatisticsTable": wsManagedAPRadioStatisticsTable,
       "wsManagedAPRadioStatisticsEntry": wsManagedAPRadioStatisticsEntry,
       "wsManagedAPRadioWLANPktsRecvd": wsManagedAPRadioWLANPktsRecvd,
       "wsManagedAPRadioWLANBytesRecvd": wsManagedAPRadioWLANBytesRecvd,
       "wsManagedAPRadioWLANPktsTransmitted": wsManagedAPRadioWLANPktsTransmitted,
       "wsManagedAPRadioWLANBytesTransmitted": wsManagedAPRadioWLANBytesTransmitted,
       "wsManagedAPRadioTxFragmentCount": wsManagedAPRadioTxFragmentCount,
       "wsManagedAPRadioMcastTxFrameCount": wsManagedAPRadioMcastTxFrameCount,
       "wsManagedAPRadioFailedCount": wsManagedAPRadioFailedCount,
       "wsManagedAPRadioRetryCount": wsManagedAPRadioRetryCount,
       "wsManagedAPRadioMultipleRetryCount": wsManagedAPRadioMultipleRetryCount,
       "wsManagedAPRadioFrameDuplicateCount": wsManagedAPRadioFrameDuplicateCount,
       "wsManagedAPRadioRTSSuccessCount": wsManagedAPRadioRTSSuccessCount,
       "wsManagedAPRadioRTSFailureCount": wsManagedAPRadioRTSFailureCount,
       "wsManagedAPRadioACKFailureCount": wsManagedAPRadioACKFailureCount,
       "wsManagedAPRadioRecvdFragmentCount": wsManagedAPRadioRecvdFragmentCount,
       "wsManagedAPRadioMcastRecvdFrameCount": wsManagedAPRadioMcastRecvdFrameCount,
       "wsManagedAPRadioFCSErrorCount": wsManagedAPRadioFCSErrorCount,
       "wsManagedAPRadioTxFrameCount": wsManagedAPRadioTxFrameCount,
       "wsManagedAPRadioWEPUndecryptableCount": wsManagedAPRadioWEPUndecryptableCount,
       "wsManagedAPRadioWLANPktsRecvDropped": wsManagedAPRadioWLANPktsRecvDropped,
       "wsManagedAPRadioWLANBytesRecvDropped": wsManagedAPRadioWLANBytesRecvDropped,
       "wsManagedAPRadioWLANPktsTransmitDropped": wsManagedAPRadioWLANPktsTransmitDropped,
       "wsManagedAPRadioWLANBytesTransmitDropped": wsManagedAPRadioWLANBytesTransmitDropped,
       "wsManagedAPNeighborAPListTable": wsManagedAPNeighborAPListTable,
       "wsManagedAPNeighborAPListEntry": wsManagedAPNeighborAPListEntry,
       "wsNeighborMacAddress": wsNeighborMacAddress,
       "wsNeighborSSID": wsNeighborSSID,
       "wsNeighborRSSI": wsNeighborRSSI,
       "wsNeighborStatus": wsNeighborStatus,
       "wsNeighborAge": wsNeighborAge,
       "wsManagedAPNeighborEntriesPurge": wsManagedAPNeighborEntriesPurge,
       "wsManagedAPNeighborClientListTable": wsManagedAPNeighborClientListTable,
       "wsManagedAPNeighborClientListEntry": wsManagedAPNeighborClientListEntry,
       "wsNeighborClientMacAddress": wsNeighborClientMacAddress,
       "wsNeighborClientRSSI": wsNeighborClientRSSI,
       "wsNeighborClientChannel": wsNeighborClientChannel,
       "wsNeighborClientAge": wsNeighborClientAge,
       "wsNeighborClientDiscoveryReason": wsNeighborClientDiscoveryReason,
       "wsManagedAPVAPStatusTable": wsManagedAPVAPStatusTable,
       "wsManagedAPVAPStatusEntry": wsManagedAPVAPStatusEntry,
       "wsManagedVAPId": wsManagedVAPId,
       "wsManagedVAPMacAddress": wsManagedVAPMacAddress,
       "wsManagedVAPSSID": wsManagedVAPSSID,
       "wsManagedVAPAuthenticatedClients": wsManagedVAPAuthenticatedClients,
       "wsManagedAPVAPStatisticsTable": wsManagedAPVAPStatisticsTable,
       "wsManagedAPVAPStatisticsEntry": wsManagedAPVAPStatisticsEntry,
       "wsManagedVAPAssociationFailures": wsManagedVAPAssociationFailures,
       "wsManagedVAPAuthenticationFailures": wsManagedVAPAuthenticationFailures,
       "wsManagedVAPWLANPktsRecvd": wsManagedVAPWLANPktsRecvd,
       "wsManagedVAPWLANBytesRecvd": wsManagedVAPWLANBytesRecvd,
       "wsManagedVAPWLANPktsTransmitted": wsManagedVAPWLANPktsTransmitted,
       "wsManagedVAPWLANBytesTransmitted": wsManagedVAPWLANBytesTransmitted,
       "wsManagedVAPWLANPktsRecvDropped": wsManagedVAPWLANPktsRecvDropped,
       "wsManagedVAPWLANBytesRecvDropped": wsManagedVAPWLANBytesRecvDropped,
       "wsManagedVAPWLANPktsTransmitDropped": wsManagedVAPWLANPktsTransmitDropped,
       "wsManagedVAPWLANBytesTransmitDropped": wsManagedVAPWLANBytesTransmitDropped,
       "wsManagedAPResetAll": wsManagedAPResetAll,
       "wsManagedAPRadioEligibleChannelListTable": wsManagedAPRadioEligibleChannelListTable,
       "wsManagedAPRadioEligibleChannelListEntry": wsManagedAPRadioEligibleChannelListEntry,
       "wsManagedAPRadioEligibleChannel": wsManagedAPRadioEligibleChannel,
       "wsManagedAPRadioEligibleChannelRdrDetRequired": wsManagedAPRadioEligibleChannelRdrDetRequired,
       "wsManagedAPRadioEligibleChannelRdrDetected": wsManagedAPRadioEligibleChannelRdrDetected,
       "wsManagedAPRadioEligibleChannelLastRdrDetTime": wsManagedAPRadioEligibleChannelLastRdrDetTime,
       "associatedClient": associatedClient,
       "wsAssociatedClientStatusTable": wsAssociatedClientStatusTable,
       "wsAssociatedClientStatusEntry": wsAssociatedClientStatusEntry,
       "wsAssociatedClientMacAddress": wsAssociatedClientMacAddress,
       "wsAssociatedClientTunnelIpAddress": wsAssociatedClientTunnelIpAddress,
       "wsAssociatedClientUserName": wsAssociatedClientUserName,
       "wsAssociatedClientSSID": wsAssociatedClientSSID,
       "wsAssociatedClientVLAN": wsAssociatedClientVLAN,
       "wsAssociatedClientStatus": wsAssociatedClientStatus,
       "wsAssociatedClientTxDataRate": wsAssociatedClientTxDataRate,
       "wsAssociatedClientInactivePeriod": wsAssociatedClientInactivePeriod,
       "wsAssociatedClientDisassociateAction": wsAssociatedClientDisassociateAction,
       "wsAssociatedClientAge": wsAssociatedClientAge,
       "wsAssociatedClientAssociatingSwitch": wsAssociatedClientAssociatingSwitch,
       "wsAssociatedClientSwitchMacAddress": wsAssociatedClientSwitchMacAddress,
       "wsAssociatedClientSwitchIpAddress": wsAssociatedClientSwitchIpAddress,
       "wsAssociatedClientDot11nCapable": wsAssociatedClientDot11nCapable,
       "wsAssociatedClientStbcCapable": wsAssociatedClientStbcCapable,
       "wsAssociatedClientDistTunnelStatus": wsAssociatedClientDistTunnelStatus,
       "wsAssociatedClientDistTunnelRoamStatus": wsAssociatedClientDistTunnelRoamStatus,
       "wsAssociatedClientDistTunnelHomeAPMac": wsAssociatedClientDistTunnelHomeAPMac,
       "wsAssociatedClientDistTunnelAssocAPMac": wsAssociatedClientDistTunnelAssocAPMac,
       "wsAssociatedClientAPMacAddress": wsAssociatedClientAPMacAddress,
       "wsAssociatedClientBSSID": wsAssociatedClientBSSID,
       "wsAssociatedClientRadioInterface": wsAssociatedClientRadioInterface,
       "wsAssociatedClientChannel": wsAssociatedClientChannel,
       "wsAssociatedClientNwTime": wsAssociatedClientNwTime,
       "wsAssociatedClientIpAddress": wsAssociatedClientIpAddress,
       "wsAssociatedClientNetBiosName": wsAssociatedClientNetBiosName,
       "wsAssociatedClientRRMSupported": wsAssociatedClientRRMSupported,
       "wsAssociatedClientRRMLocationReportSupported": wsAssociatedClientRRMLocationReportSupported,
       "wsAssociatedClientRRMBeaconTableMeasurementSupported": wsAssociatedClientRRMBeaconTableMeasurementSupported,
       "wsAssociatedClientRRMBeaconActiveMeasurementSupported": wsAssociatedClientRRMBeaconActiveMeasurementSupported,
       "wsAssociatedClientRRMBeaconPassiveMeasurementSupported": wsAssociatedClientRRMBeaconPassiveMeasurementSupported,
       "wsAssociatedClientRRMChannelLoadMeasurementSupported": wsAssociatedClientRRMChannelLoadMeasurementSupported,
       "wsAssociatedClientStatisticsTable": wsAssociatedClientStatisticsTable,
       "wsAssociatedClientStatisticsEntry": wsAssociatedClientStatisticsEntry,
       "wsAssociatedClientPktsRecvd": wsAssociatedClientPktsRecvd,
       "wsAssociatedClientBytesRecvd": wsAssociatedClientBytesRecvd,
       "wsAssociatedClientPktsTransmitted": wsAssociatedClientPktsTransmitted,
       "wsAssociatedClientBytesTransmitted": wsAssociatedClientBytesTransmitted,
       "wsAssociatedClientDuplicatePktsRecvd": wsAssociatedClientDuplicatePktsRecvd,
       "wsAssociatedClientFragmentedPktsRecvd": wsAssociatedClientFragmentedPktsRecvd,
       "wsAssociatedClientFragmentedPktsTransmitted": wsAssociatedClientFragmentedPktsTransmitted,
       "wsAssociatedClientTransmitRetryCount": wsAssociatedClientTransmitRetryCount,
       "wsAssociatedClientTransmitRetryFailedCount": wsAssociatedClientTransmitRetryFailedCount,
       "wsAssociatedClientPktsRecvDropped": wsAssociatedClientPktsRecvDropped,
       "wsAssociatedClientBytesRecvDropped": wsAssociatedClientBytesRecvDropped,
       "wsAssociatedClientPktsTransmitDropped": wsAssociatedClientPktsTransmitDropped,
       "wsAssociatedClientBytesTransmitDropped": wsAssociatedClientBytesTransmitDropped,
       "wsAssociatedClientTsViolatePktsRecvd": wsAssociatedClientTsViolatePktsRecvd,
       "wsAssociatedClientTsViolatePktsTransmitted": wsAssociatedClientTsViolatePktsTransmitted,
       "wsAssociatedClientNeighborManagedAPStatusTable": wsAssociatedClientNeighborManagedAPStatusTable,
       "wsAssociatedClientNeighborManagedAPStatusEntry": wsAssociatedClientNeighborManagedAPStatusEntry,
       "wsClientStationMacAddress": wsClientStationMacAddress,
       "wsClientNeighborWSManagedAPMacAddress": wsClientNeighborWSManagedAPMacAddress,
       "wsClientNeighborWSManagedAPRadioInterface": wsClientNeighborWSManagedAPRadioInterface,
       "wsClientStationDiscoveryReason": wsClientStationDiscoveryReason,
       "wsVAPAssociatedClientStatusTable": wsVAPAssociatedClientStatusTable,
       "wsVAPAssociatedClientStatusEntry": wsVAPAssociatedClientStatusEntry,
       "wsVAPMacAddress": wsVAPMacAddress,
       "wsVAPAssociatedClientMacAddress": wsVAPAssociatedClientMacAddress,
       "wsSSIDAssociatedClientStatusTable": wsSSIDAssociatedClientStatusTable,
       "wsSSIDAssociatedClientStatusEntry": wsSSIDAssociatedClientStatusEntry,
       "wsSSID": wsSSID,
       "wsSSIDAssociatedClientMacAddress": wsSSIDAssociatedClientMacAddress,
       "wsSwitchAssociatedClientStatusTable": wsSwitchAssociatedClientStatusTable,
       "wsSwitchAssociatedClientStatusEntry": wsSwitchAssociatedClientStatusEntry,
       "wsAssociatedClientSwitchIPAddress": wsAssociatedClientSwitchIPAddress,
       "wsSwitchAssociatedClientMacAddress": wsSwitchAssociatedClientMacAddress,
       "wsAssociatedClientQosStatusTable": wsAssociatedClientQosStatusTable,
       "wsAssociatedClientQosStatusEntry": wsAssociatedClientQosStatusEntry,
       "wsAssociatedClientQosBandwidthLimitDown": wsAssociatedClientQosBandwidthLimitDown,
       "wsAssociatedClientQosBandwidthLimitUp": wsAssociatedClientQosBandwidthLimitUp,
       "wsAssociatedClientQosAccessControlDownType": wsAssociatedClientQosAccessControlDownType,
       "wsAssociatedClientQosAccessControlDownName": wsAssociatedClientQosAccessControlDownName,
       "wsAssociatedClientQosAccessControlUpType": wsAssociatedClientQosAccessControlUpType,
       "wsAssociatedClientQosAccessControlUpName": wsAssociatedClientQosAccessControlUpName,
       "wsAssociatedClientQosDiffservPolicyDownType": wsAssociatedClientQosDiffservPolicyDownType,
       "wsAssociatedClientQosDiffservPolicyDownName": wsAssociatedClientQosDiffservPolicyDownName,
       "wsAssociatedClientQosDiffservPolicyUpType": wsAssociatedClientQosDiffservPolicyUpType,
       "wsAssociatedClientQosDiffservPolicyUpName": wsAssociatedClientQosDiffservPolicyUpName,
       "wsAssociatedClientQosOperStatus": wsAssociatedClientQosOperStatus,
       "wsAssociatedClientSessionStatisticsTable": wsAssociatedClientSessionStatisticsTable,
       "wsAssociatedClientSessionStatisticsEntry": wsAssociatedClientSessionStatisticsEntry,
       "wsAssociatedClientSessionPktsRecvd": wsAssociatedClientSessionPktsRecvd,
       "wsAssociatedClientSessionBytesRecvd": wsAssociatedClientSessionBytesRecvd,
       "wsAssociatedClientSessionPktsTransmitted": wsAssociatedClientSessionPktsTransmitted,
       "wsAssociatedClientSessionBytesTransmitted": wsAssociatedClientSessionBytesTransmitted,
       "wsAssociatedClientSessionDuplicatePktsRecvd": wsAssociatedClientSessionDuplicatePktsRecvd,
       "wsAssociatedClientSessionFragmentedPktsRecvd": wsAssociatedClientSessionFragmentedPktsRecvd,
       "wsAssociatedClientSessionFragmentedPktsTransmitted": wsAssociatedClientSessionFragmentedPktsTransmitted,
       "wsAssociatedClientSessionTransmitRetryCount": wsAssociatedClientSessionTransmitRetryCount,
       "wsAssociatedClientSessionTransmitRetryFailedCount": wsAssociatedClientSessionTransmitRetryFailedCount,
       "wsAssociatedClientSessionPktsRecvDropped": wsAssociatedClientSessionPktsRecvDropped,
       "wsAssociatedClientSessionBytesRecvDropped": wsAssociatedClientSessionBytesRecvDropped,
       "wsAssociatedClientSessionPktsTransmitDropped": wsAssociatedClientSessionPktsTransmitDropped,
       "wsAssociatedClientSessionBytesTransmitDropped": wsAssociatedClientSessionBytesTransmitDropped,
       "wsAssociatedClientSessionTSViolatePktsRecvd": wsAssociatedClientSessionTSViolatePktsRecvd,
       "wsAssociatedClientSessionTSViolatePktsTransmitted": wsAssociatedClientSessionTSViolatePktsTransmitted,
       "wsAssociatedClientQosCachedStatusTable": wsAssociatedClientQosCachedStatusTable,
       "wsAssociatedClientQosCachedStatusEntry": wsAssociatedClientQosCachedStatusEntry,
       "wsAssociatedClientQosCachedBandwidthLimitDown": wsAssociatedClientQosCachedBandwidthLimitDown,
       "wsAssociatedClientQosCachedBandwidthLimitUp": wsAssociatedClientQosCachedBandwidthLimitUp,
       "wsAssociatedClientQosCachedAccessControlDownType": wsAssociatedClientQosCachedAccessControlDownType,
       "wsAssociatedClientQosCachedAccessControlDownName": wsAssociatedClientQosCachedAccessControlDownName,
       "wsAssociatedClientQosCachedAccessControlUpType": wsAssociatedClientQosCachedAccessControlUpType,
       "wsAssociatedClientQosCachedAccessControlUpName": wsAssociatedClientQosCachedAccessControlUpName,
       "wsAssociatedClientQosCachedDiffservPolicyDownType": wsAssociatedClientQosCachedDiffservPolicyDownType,
       "wsAssociatedClientQosCachedDiffservPolicyDownName": wsAssociatedClientQosCachedDiffservPolicyDownName,
       "wsAssociatedClientQosCachedDiffservPolicyUpType": wsAssociatedClientQosCachedDiffservPolicyUpType,
       "wsAssociatedClientQosCachedDiffservPolicyUpName": wsAssociatedClientQosCachedDiffservPolicyUpName,
       "peerSwitch": peerSwitch,
       "wsPeerStatusTable": wsPeerStatusTable,
       "wsPeerStatusEntry": wsPeerStatusEntry,
       "wsPeerIpAddress": wsPeerIpAddress,
       "wsPeerClusterControllerIndicator": wsPeerClusterControllerIndicator,
       "wsPeerTotalPeerSwitches": wsPeerTotalPeerSwitches,
       "wsPeerVendorId": wsPeerVendorId,
       "wsPeerProtocolVersion": wsPeerProtocolVersion,
       "wsPeerSoftwareVersion": wsPeerSoftwareVersion,
       "wsPeerDiscoveryReason": wsPeerDiscoveryReason,
       "wsPeerAge": wsPeerAge,
       "wsPeerManagedAPCount": wsPeerManagedAPCount,
       "wsPeerConfigRequestAction": wsPeerConfigRequestAction,
       "wsPeerConfigRequestStatus": wsPeerConfigRequestStatus,
       "wsPeerConfigSwitchIp": wsPeerConfigSwitchIp,
       "wsPeerConfigReceived": wsPeerConfigReceived,
       "wsPeerConfigReceivedTimestamp": wsPeerConfigReceivedTimestamp,
       "wsPeerSwitchManagedAPTable": wsPeerSwitchManagedAPTable,
       "wsPeerSwitchManagedAPEntry": wsPeerSwitchManagedAPEntry,
       "wsPeerSwitchIpAddress": wsPeerSwitchIpAddress,
       "wsPeerSwitchAPMacAddress": wsPeerSwitchAPMacAddress,
       "wsPeerSwitchAPLocation": wsPeerSwitchAPLocation,
       "wsPeerSwitchAPIPAddress": wsPeerSwitchAPIPAddress,
       "wsPeerSwitchAPProfileId": wsPeerSwitchAPProfileId,
       "wsPeerSwitchAPProfileName": wsPeerSwitchAPProfileName,
       "wsPeerSwitchAPHardwareType": wsPeerSwitchAPHardwareType,
       "intrusionDetection": intrusionDetection,
       "wsRFScanAPStatusTable": wsRFScanAPStatusTable,
       "wsRFScanAPStatusEntry": wsRFScanAPStatusEntry,
       "wsRFScanAPMacAddress": wsRFScanAPMacAddress,
       "wsRFScanAPRadioInterface": wsRFScanAPRadioInterface,
       "wsRFScanAPBaseMacAddress": wsRFScanAPBaseMacAddress,
       "wsRFScanAPSSID": wsRFScanAPSSID,
       "wsRFScanAPPhysicalMode": wsRFScanAPPhysicalMode,
       "wsRFScanAPChannel": wsRFScanAPChannel,
       "wsRFScanAPTxRate": wsRFScanAPTxRate,
       "wsRFScanAPBeaconInterval": wsRFScanAPBeaconInterval,
       "wsRFScanAPStatus": wsRFScanAPStatus,
       "wsRFScanAPDiscoveredAge": wsRFScanAPDiscoveredAge,
       "wsRFScanAPAge": wsRFScanAPAge,
       "wsRFScanAPStatusInitial": wsRFScanAPStatusInitial,
       "wsRFScanAPSecurityMode": wsRFScanAPSecurityMode,
       "wsRFScanAPHighRate": wsRFScanAPHighRate,
       "wsRFScanAPDot11nMode": wsRFScanAPDot11nMode,
       "wsRFScanAPAdHoc": wsRFScanAPAdHoc,
       "wsRFScanAPPeerManaged": wsRFScanAPPeerManaged,
       "wsRFScanAPRogueMitigation": wsRFScanAPRogueMitigation,
       "wsRFScanAPAcknowledgeRogue": wsRFScanAPAcknowledgeRogue,
       "wsRFScanAPBSSID": wsRFScanAPBSSID,
       "wsRFScanAPOUI": wsRFScanAPOUI,
       "wsRFScanAPRRMSupported": wsRFScanAPRRMSupported,
       "wsRFScanAPDot11acMode": wsRFScanAPDot11acMode,
       "wsRFScanAPEntriesPurge": wsRFScanAPEntriesPurge,
       "wsFailureAPStatusTable": wsFailureAPStatusTable,
       "wsFailureAPStatusEntry": wsFailureAPStatusEntry,
       "wsFailedAPMacAddress": wsFailedAPMacAddress,
       "wsFailedAPIpAddress": wsFailedAPIpAddress,
       "wsFailedAPVendorId": wsFailedAPVendorId,
       "wsFailedAPSoftwareVersion": wsFailedAPSoftwareVersion,
       "wsFailedAPHWType": wsFailedAPHWType,
       "wsFailedAPFailureType": wsFailedAPFailureType,
       "wsFailedAPValidationFailureCount": wsFailedAPValidationFailureCount,
       "wsFailedAPAuthenticationFailureCount": wsFailedAPAuthenticationFailureCount,
       "wsFailedAPProtocolVersion": wsFailedAPProtocolVersion,
       "wsFailedAPAge": wsFailedAPAge,
       "wsFailedAPReportingSwitch": wsFailedAPReportingSwitch,
       "wsFailedAPSwitchMacAddress": wsFailedAPSwitchMacAddress,
       "wsFailedAPSwitchIpAddress": wsFailedAPSwitchIpAddress,
       "wsAPFailureEntriesPurge": wsAPFailureEntriesPurge,
       "wsAdHocClientStatusTable": wsAdHocClientStatusTable,
       "wsAdHocClientStatusEntry": wsAdHocClientStatusEntry,
       "wsAdHocClientMacAddress": wsAdHocClientMacAddress,
       "wsDetectedAPMacAddress": wsDetectedAPMacAddress,
       "wsDetectedAPRadioInterface": wsDetectedAPRadioInterface,
       "wsAdHocClientDetectionMode": wsAdHocClientDetectionMode,
       "wsAdHocClientAge": wsAdHocClientAge,
       "wsAdHocClientEntriesPurge": wsAdHocClientEntriesPurge,
       "wsAPTriangulationNonSentryStatusTable": wsAPTriangulationNonSentryStatusTable,
       "wsAPTriangulationNonSentryStatusEntry": wsAPTriangulationNonSentryStatusEntry,
       "wsAPTriangulationMacAddr": wsAPTriangulationMacAddr,
       "wsAPTriangulationId": wsAPTriangulationId,
       "wsAPTriangulationNonSentryMacAddr": wsAPTriangulationNonSentryMacAddr,
       "wsAPTriangulationNonSentryRadio": wsAPTriangulationNonSentryRadio,
       "wsAPTriangulationRssi": wsAPTriangulationRssi,
       "wsAPTriangulationStrength": wsAPTriangulationStrength,
       "wsAPTriangulationNoise": wsAPTriangulationNoise,
       "wsAPTriangulationAge": wsAPTriangulationAge,
       "wsAPTriangulationSentryStatusTable": wsAPTriangulationSentryStatusTable,
       "wsAPTriangulationSentryStatusEntry": wsAPTriangulationSentryStatusEntry,
       "wsAPSentryTriangulationMacAddr": wsAPSentryTriangulationMacAddr,
       "wsAPSentryTriangulationId": wsAPSentryTriangulationId,
       "wsAPSentryTriangulationSentryMacAddr": wsAPSentryTriangulationSentryMacAddr,
       "wsAPSentryTriangulationSentryRadio": wsAPSentryTriangulationSentryRadio,
       "wsAPSentryTriangulationRssi": wsAPSentryTriangulationRssi,
       "wsAPSentryTriangulationStrength": wsAPSentryTriangulationStrength,
       "wsAPSentryTriangulationNoise": wsAPSentryTriangulationNoise,
       "wsAPSentryTriangulationAge": wsAPSentryTriangulationAge,
       "wsAPRogueClassificationStatusTable": wsAPRogueClassificationStatusTable,
       "wsAPRogueClassificationStatusEntry": wsAPRogueClassificationStatusEntry,
       "wsAPRogueClassificationMacAddr": wsAPRogueClassificationMacAddr,
       "wsAPRogueClassificationTestId": wsAPRogueClassificationTestId,
       "wsAPRogueClassificationTestName": wsAPRogueClassificationTestName,
       "wsAPRogueClassificationDetected": wsAPRogueClassificationDetected,
       "wsAPRogueClassificationReportingAPMac": wsAPRogueClassificationReportingAPMac,
       "wsAPRogueClassificationReportingAPRadio": wsAPRogueClassificationReportingAPRadio,
       "wsAPRogueClassificationTestState": wsAPRogueClassificationTestState,
       "wsAPRogueClassificationTestResult": wsAPRogueClassificationTestResult,
       "wsAPRogueClassificationFirstTime": wsAPRogueClassificationFirstTime,
       "wsAPRogueClassificationLastTime": wsAPRogueClassificationLastTime,
       "wsAPDeAuthenticationAttackStatusTable": wsAPDeAuthenticationAttackStatusTable,
       "wsAPDeAuthenticationAttackStatusEntry": wsAPDeAuthenticationAttackStatusEntry,
       "wsAPDeAuthenticationAttackStatusId": wsAPDeAuthenticationAttackStatusId,
       "wsAPDeAuthenticationAttackBSSID": wsAPDeAuthenticationAttackBSSID,
       "wsAPDeAuthenticationAttackChannel": wsAPDeAuthenticationAttackChannel,
       "wsAPDeAuthenticationAttackTime": wsAPDeAuthenticationAttackTime,
       "wsAPDeAuthenticationAttackAge": wsAPDeAuthenticationAttackAge,
       "wsDetectedClientStatusTable": wsDetectedClientStatusTable,
       "wsDetectedClientStatusEntry": wsDetectedClientStatusEntry,
       "wsDetectedClientMacAddress": wsDetectedClientMacAddress,
       "wsDetectedClientStatus": wsDetectedClientStatus,
       "wsDetectedClientAuthStatus": wsDetectedClientAuthStatus,
       "wsDetectedClientEntryLastUpdatedAt": wsDetectedClientEntryLastUpdatedAt,
       "wsDetectedClientThreatDetectedStatus": wsDetectedClientThreatDetectedStatus,
       "wsDetectedClientThreatMitigationStatus": wsDetectedClientThreatMitigationStatus,
       "wsDetectedClientName": wsDetectedClientName,
       "wsDetectedClientEntryCreateTime": wsDetectedClientEntryCreateTime,
       "wsDetectedClientChannel": wsDetectedClientChannel,
       "wsDetectedClientAuthRSSI": wsDetectedClientAuthRSSI,
       "wsDetectedClientAuthSignal": wsDetectedClientAuthSignal,
       "wsDetectedClientAuthNoise": wsDetectedClientAuthNoise,
       "wsDetectedClientProbeReqRecorded": wsDetectedClientProbeReqRecorded,
       "wsDetectedClientProbeCollectionIntvl": wsDetectedClientProbeCollectionIntvl,
       "wsDetectedClientHighestNumProbes": wsDetectedClientHighestNumProbes,
       "wsDetectedClientAuthMsgsRecorded": wsDetectedClientAuthMsgsRecorded,
       "wsDetectedClientAuthCollectionIntvl": wsDetectedClientAuthCollectionIntvl,
       "wsDetectedClientHighestNumAuthMsgs": wsDetectedClientHighestNumAuthMsgs,
       "wsDetectedClientDeAuthMsgsRecorded": wsDetectedClientDeAuthMsgsRecorded,
       "wsDetectedClientDeAuthCollectionIntvl": wsDetectedClientDeAuthCollectionIntvl,
       "wsDetectedClientHighestNumDeAuthMsgs": wsDetectedClientHighestNumDeAuthMsgs,
       "wsDetectedClientAuthFailures": wsDetectedClientAuthFailures,
       "wsDetectedClientProbesDetected": wsDetectedClientProbesDetected,
       "wsDetectedClientBcastBSSIDProbes": wsDetectedClientBcastBSSIDProbes,
       "wsDetectedClientBcastSSIDProbes": wsDetectedClientBcastSSIDProbes,
       "wsDetectedClientSpecificBSSIDProbes": wsDetectedClientSpecificBSSIDProbes,
       "wsDetectedClientSpecificSSIDProbes": wsDetectedClientSpecificSSIDProbes,
       "wsDetectedClientLastNonBcastBSSID": wsDetectedClientLastNonBcastBSSID,
       "wsDetectedClientLastNonBcastSSID": wsDetectedClientLastNonBcastSSID,
       "wsDetectedClientThreatMitigationSent": wsDetectedClientThreatMitigationSent,
       "wsDetectedClientEntryPurge": wsDetectedClientEntryPurge,
       "wsDetectedClientEntryAcknowledge": wsDetectedClientEntryAcknowledge,
       "wsDetectedClientOUI": wsDetectedClientOUI,
       "wsDetectedClientPurgeAll": wsDetectedClientPurgeAll,
       "wsDetectedClientAcknowledgeAll": wsDetectedClientAcknowledgeAll,
       "wsClientRogueClassificationStatusTable": wsClientRogueClassificationStatusTable,
       "wsClientRogueClassificationStatusEntry": wsClientRogueClassificationStatusEntry,
       "wsClientRogueClassificationMacAddr": wsClientRogueClassificationMacAddr,
       "wsClientRogueClassificationTestId": wsClientRogueClassificationTestId,
       "wsClientRogueClassificationTestName": wsClientRogueClassificationTestName,
       "wsClientRogueClassificationDetected": wsClientRogueClassificationDetected,
       "wsClientRogueClassificationReportingAPMac": wsClientRogueClassificationReportingAPMac,
       "wsClientRogueClassificationReportingAPRadio": wsClientRogueClassificationReportingAPRadio,
       "wsClientRogueClassificationTestState": wsClientRogueClassificationTestState,
       "wsClientRogueClassificationTestResult": wsClientRogueClassificationTestResult,
       "wsClientRogueClassificationFirstTime": wsClientRogueClassificationFirstTime,
       "wsClientRogueClassificationLastTime": wsClientRogueClassificationLastTime,
       "wsDetectedClientTriangulationNonSentryStatusTable": wsDetectedClientTriangulationNonSentryStatusTable,
       "wsDetectedClientTriangulationNonSentryStatusEntry": wsDetectedClientTriangulationNonSentryStatusEntry,
       "wsDetectedClientTriangulationMacAddr": wsDetectedClientTriangulationMacAddr,
       "wsDetectedClientTriangulationId": wsDetectedClientTriangulationId,
       "wsDetectedClientTriangulationNonSentryMacAddr": wsDetectedClientTriangulationNonSentryMacAddr,
       "wsDetectedClientTriangulationNonSentryRadio": wsDetectedClientTriangulationNonSentryRadio,
       "wsDetectedClientTriangulationRssi": wsDetectedClientTriangulationRssi,
       "wsDetectedClientTriangulationStrength": wsDetectedClientTriangulationStrength,
       "wsDetectedClientTriangulationNoise": wsDetectedClientTriangulationNoise,
       "wsDetectedClientTriangulationAge": wsDetectedClientTriangulationAge,
       "wsDetectedClientTriangulationSentryStatusTable": wsDetectedClientTriangulationSentryStatusTable,
       "wsDetectedClientTriangulationSentryStatusEntry": wsDetectedClientTriangulationSentryStatusEntry,
       "wsDetectedClientSentryTriangulationMacAddr": wsDetectedClientSentryTriangulationMacAddr,
       "wsDetectedClientSentryTriangulationId": wsDetectedClientSentryTriangulationId,
       "wsDetectedClientSentryTriangulationSentryMacAddr": wsDetectedClientSentryTriangulationSentryMacAddr,
       "wsDetectedClientSentryTriangulationSentryRadio": wsDetectedClientSentryTriangulationSentryRadio,
       "wsDetectedClientSentryTriangulationRssi": wsDetectedClientSentryTriangulationRssi,
       "wsDetectedClientSentryTriangulationStrength": wsDetectedClientSentryTriangulationStrength,
       "wsDetectedClientSentryTriangulationNoise": wsDetectedClientSentryTriangulationNoise,
       "wsDetectedClientSentryTriangulationAge": wsDetectedClientSentryTriangulationAge,
       "wsDetectedClientPreAuthenticationHistoryTable": wsDetectedClientPreAuthenticationHistoryTable,
       "wsDetectedClientPreAuthenticationHistoryEntry": wsDetectedClientPreAuthenticationHistoryEntry,
       "wsDetectedClientPreAuthenticationMacAddr": wsDetectedClientPreAuthenticationMacAddr,
       "wsDetectedClientPreAuthenticationId": wsDetectedClientPreAuthenticationId,
       "wsDetectedClientPreAuthenticationApMac": wsDetectedClientPreAuthenticationApMac,
       "wsDetectedClientPreAuthenticationApRadioId": wsDetectedClientPreAuthenticationApRadioId,
       "wsDetectedClientPreAuthenticationVapMac": wsDetectedClientPreAuthenticationVapMac,
       "wsDetectedClientPreAuthenticationSSID": wsDetectedClientPreAuthenticationSSID,
       "wsDetectedClientPreAuthenticationAge": wsDetectedClientPreAuthenticationAge,
       "wsDetectedClientPreAuthenticationStatus": wsDetectedClientPreAuthenticationStatus,
       "wsDetectedClientPreAuthenticationHistoryPurgeAll": wsDetectedClientPreAuthenticationHistoryPurgeAll,
       "wsDetectedClientRoamHistoryTable": wsDetectedClientRoamHistoryTable,
       "wsDetectedClientRoamHistoryEntry": wsDetectedClientRoamHistoryEntry,
       "wsDetectedClientRoamMacAddr": wsDetectedClientRoamMacAddr,
       "wsDetectedClientRoamId": wsDetectedClientRoamId,
       "wsDetectedClientRoamApMac": wsDetectedClientRoamApMac,
       "wsDetectedClientRoamApRadioId": wsDetectedClientRoamApRadioId,
       "wsDetectedClientRoamVapMac": wsDetectedClientRoamVapMac,
       "wsDetectedClientRoamSSID": wsDetectedClientRoamSSID,
       "wsDetectedClientRoamAge": wsDetectedClientRoamAge,
       "wsDetectedClientRoamStatus": wsDetectedClientRoamStatus,
       "wsDetectedClientRoamHistoryPurgeAll": wsDetectedClientRoamHistoryPurgeAll,
       "snmpTrapsConfig": snmpTrapsConfig,
       "wsStatusTrapMode": wsStatusTrapMode,
       "wsPeerWSTrapMode": wsPeerWSTrapMode,
       "wsAPStateTrapMode": wsAPStateTrapMode,
       "wsAPFailureTrapMode": wsAPFailureTrapMode,
       "wsRogueAPTrapMode": wsRogueAPTrapMode,
       "wsRFScanTrapMode": wsRFScanTrapMode,
       "wsClientStateTrapMode": wsClientStateTrapMode,
       "wsWidsStatusMode": wsWidsStatusMode,
       "wsTspecTrapMode": wsTspecTrapMode,
       "wsClientFailureTrapMode": wsClientFailureTrapMode,
       "wsMibInfo": wsMibInfo,
       "wsMibVersion": wsMibVersion,
       "wsCapability": wsCapability,
       "wsAPHardwareCapabilityTable": wsAPHardwareCapabilityTable,
       "wsAPHardwareCapabilityEntry": wsAPHardwareCapabilityEntry,
       "wsAPHWTypeID": wsAPHWTypeID,
       "wsAPHWTypeDescription": wsAPHWTypeDescription,
       "wsAPHWTypeRadioCount": wsAPHWTypeRadioCount,
       "wsAPImageTypeID": wsAPImageTypeID,
       "wsAPHWDualBootSuppport": wsAPHWDualBootSuppport,
       "wsAPHardwareRadioCapabilityTable": wsAPHardwareRadioCapabilityTable,
       "wsAPHardwareRadioCapabilityEntry": wsAPHardwareRadioCapabilityEntry,
       "wsAPHWTypeRadioNum": wsAPHWTypeRadioNum,
       "wsAPHWTypeRadioID": wsAPHWTypeRadioID,
       "wsAPHWTypeRadioDescription": wsAPHWTypeRadioDescription,
       "wsAPHWTypeRadioVapCount": wsAPHWTypeRadioVapCount,
       "wsAPHWTypeRadioAmodeSupport": wsAPHWTypeRadioAmodeSupport,
       "wsAPHWTypeRadioBGmodeSupport": wsAPHWTypeRadioBGmodeSupport,
       "wsAPHWTypeRadioNmodeSupport": wsAPHWTypeRadioNmodeSupport,
       "wsAPHWTypeRadioACmodeSupport": wsAPHWTypeRadioACmodeSupport,
       "wsAPImageTypeCapabilityTable": wsAPImageTypeCapabilityTable,
       "wsAPImageTypeCapabilityEntry": wsAPImageTypeCapabilityEntry,
       "wsAPImageTypeDescription": wsAPImageTypeDescription,
       "wsAPImageAvailabilityTable": wsAPImageAvailabilityTable,
       "wsAPImageAvailabilityEntry": wsAPImageAvailabilityEntry,
       "wsAPImageAvailability": wsAPImageAvailability,
       "l2centTunnel": l2centTunnel,
       "wsL2CentTnnlVlanListTable": wsL2CentTnnlVlanListTable,
       "wsL2CentTnnlVlanListEntry": wsL2CentTnnlVlanListEntry,
       "wsL2CentTnnlVlanId": wsL2CentTnnlVlanId,
       "wsL2CentTnnlVlanRowStatus": wsL2CentTnnlVlanRowStatus,
       "wsOuiDatabase": wsOuiDatabase,
       "wsOuiTable": wsOuiTable,
       "wsOuiEntry": wsOuiEntry,
       "wsOuiValue": wsOuiValue,
       "wsOuiDescription": wsOuiDescription,
       "wsOuiRowStatus": wsOuiRowStatus,
       "rrmNeighbor": rrmNeighbor,
       "wsRrmNeighborTable": wsRrmNeighborTable,
       "wsRrmNeighborEntry": wsRrmNeighborEntry,
       "wsRrmNeighborApMacAddr": wsRrmNeighborApMacAddr,
       "wsRrmNeighborVapMacAddr": wsRrmNeighborVapMacAddr,
       "wsRrmNeighborMacAddr": wsRrmNeighborMacAddr,
       "wsRrmNeighborRSSI": wsRrmNeighborRSSI,
       "wsRrmNeighborSSID": wsRrmNeighborSSID,
       "wsRrmNeighborChannel": wsRrmNeighborChannel,
       "wsRrmNeighborAge": wsRrmNeighborAge,
       "wsRrmNeighborAllPurge": wsRrmNeighborAllPurge,
       "wsRrmNeighborApPurge": wsRrmNeighborApPurge,
       "wsRrmNeighborVapPurge": wsRrmNeighborVapPurge,
       "rrmChannelLoad": rrmChannelLoad,
       "wsRrmChannelLoadHistoryTable": wsRrmChannelLoadHistoryTable,
       "wsRrmChannelLoadHistoryEntry": wsRrmChannelLoadHistoryEntry,
       "wsRrmChannelLoadHistoryEntryId": wsRrmChannelLoadHistoryEntryId,
       "wsRrmChannelLoadHistoryEntryApMacAddr": wsRrmChannelLoadHistoryEntryApMacAddr,
       "wsRrmChannelLoadHistoryEntryClientMacAddr": wsRrmChannelLoadHistoryEntryClientMacAddr,
       "wsRrmChannelLoadHistoryEntryChannel": wsRrmChannelLoadHistoryEntryChannel,
       "wsRrmChannelLoadHistoryEntryAge": wsRrmChannelLoadHistoryEntryAge,
       "wsRrmChannelLoadHistoryEntryLoad": wsRrmChannelLoadHistoryEntryLoad,
       "wsRrmChannelLoadHistoryEntryDuration": wsRrmChannelLoadHistoryEntryDuration,
       "wsRrmChannelLoadCurrentRequest": wsRrmChannelLoadCurrentRequest,
       "wsRrmChannelLoadCurrentRequestClientMacAddr": wsRrmChannelLoadCurrentRequestClientMacAddr,
       "wsRrmChannelLoadCurrentRequestApMacAddr": wsRrmChannelLoadCurrentRequestApMacAddr,
       "wsRrmChannelLoadCurrentRequestChannel": wsRrmChannelLoadCurrentRequestChannel,
       "wsRrmChannelLoadCurrentRequestDuration": wsRrmChannelLoadCurrentRequestDuration,
       "wsRrmChannelLoadCurrentRequestStatus": wsRrmChannelLoadCurrentRequestStatus,
       "wsRrmChannelLoadCurrentRequestTimeRemaining": wsRrmChannelLoadCurrentRequestTimeRemaining,
       "wsRrmChannelLoadCurrentRequestAbort": wsRrmChannelLoadCurrentRequestAbort,
       "wsRrmChannelLoadNewRequest": wsRrmChannelLoadNewRequest,
       "wsRrmChannelLoadNewRequestClientMacAddr": wsRrmChannelLoadNewRequestClientMacAddr,
       "wsRrmChannelLoadNewRequestChannel": wsRrmChannelLoadNewRequestChannel,
       "wsRrmChannelLoadNewRequestDuration": wsRrmChannelLoadNewRequestDuration,
       "wsRrmChannelLoadNewRequestSend": wsRrmChannelLoadNewRequestSend,
       "tspec": tspec,
       "tspecGlobal": tspecGlobal,
       "wsGlobalTspecStatus": wsGlobalTspecStatus,
       "wsTspecTotalVoiceTrafficStreams": wsTspecTotalVoiceTrafficStreams,
       "wsTspecTotalVideoTrafficStreams": wsTspecTotalVideoTrafficStreams,
       "wsTspecTotalTrafficStreamClients": wsTspecTotalTrafficStreamClients,
       "wsTspecTotalTrafficStreamRoamingClients": wsTspecTotalTrafficStreamRoamingClients,
       "wsGlobalTspecStatisticsTable": wsGlobalTspecStatisticsTable,
       "wsGlobalTspecStatisticsEntry": wsGlobalTspecStatisticsEntry,
       "wsTspecACIndex": wsTspecACIndex,
       "wsTotalWLANTspecPktsRecvd": wsTotalWLANTspecPktsRecvd,
       "wsTotalWLANTspecPktsTransmitted": wsTotalWLANTspecPktsTransmitted,
       "wsTotalWLANTspecBytesRecvd": wsTotalWLANTspecBytesRecvd,
       "wsTotalWLANTspecBytesTransmitted": wsTotalWLANTspecBytesTransmitted,
       "wsTotalWLANTspecsAccepted": wsTotalWLANTspecsAccepted,
       "wsTotalWLANTspecsRejected": wsTotalWLANTspecsRejected,
       "wsTotalWLANRoamingTspecsAccepted": wsTotalWLANRoamingTspecsAccepted,
       "wsTotalWLANRoamingTspecsRejected": wsTotalWLANRoamingTspecsRejected,
       "tspecSwitch": tspecSwitch,
       "wsSwitchTspecStatusTable": wsSwitchTspecStatusTable,
       "wsSwitchTspecStatusEntry": wsSwitchTspecStatusEntry,
       "wsSwitchTspecTotalVoiceTrafficStreams": wsSwitchTspecTotalVoiceTrafficStreams,
       "wsSwitchTspecTotalVideoTrafficStreams": wsSwitchTspecTotalVideoTrafficStreams,
       "wsSwitchTspecTotalTrafficStreamClients": wsSwitchTspecTotalTrafficStreamClients,
       "wsSwitchTspecTotalTrafficStreamRoamingClients": wsSwitchTspecTotalTrafficStreamRoamingClients,
       "wsSwitchTspecStatisticsTable": wsSwitchTspecStatisticsTable,
       "wsSwitchTspecStatisticsEntry": wsSwitchTspecStatisticsEntry,
       "wsSwitchWLANTspecPktsRecvd": wsSwitchWLANTspecPktsRecvd,
       "wsSwitchWLANTspecPktsTransmitted": wsSwitchWLANTspecPktsTransmitted,
       "wsSwitchWLANTspecBytesRecvd": wsSwitchWLANTspecBytesRecvd,
       "wsSwitchWLANTspecBytesTransmitted": wsSwitchWLANTspecBytesTransmitted,
       "wsSwitchWLANTspecsAccepted": wsSwitchWLANTspecsAccepted,
       "wsSwitchWLANTspecsRejected": wsSwitchWLANTspecsRejected,
       "wsSwitchWLANRoamingTspecsAccepted": wsSwitchWLANRoamingTspecsAccepted,
       "wsSwitchWLANRoamingTspecsRejected": wsSwitchWLANRoamingTspecsRejected,
       "tspecManagedAP": tspecManagedAP,
       "wsManagedAPTspecStatusTable": wsManagedAPTspecStatusTable,
       "wsManagedAPTspecStatusEntry": wsManagedAPTspecStatusEntry,
       "wsManagedAPTspecNumActiveTrafficStreams": wsManagedAPTspecNumActiveTrafficStreams,
       "wsManagedAPTspecNumTrafficStreamClients": wsManagedAPTspecNumTrafficStreamClients,
       "wsManagedAPTspecNumTrafficStreamRoamingClients": wsManagedAPTspecNumTrafficStreamRoamingClients,
       "wsManagedAPTspecStatisticsTable": wsManagedAPTspecStatisticsTable,
       "wsManagedAPTspecStatisticsEntry": wsManagedAPTspecStatisticsEntry,
       "wsManagedAPTspecPktsRecvd": wsManagedAPTspecPktsRecvd,
       "wsManagedAPTspecPktsTransmitted": wsManagedAPTspecPktsTransmitted,
       "wsManagedAPTspecBytesRecvd": wsManagedAPTspecBytesRecvd,
       "wsManagedAPTspecBytesTransmitted": wsManagedAPTspecBytesTransmitted,
       "wsManagedAPTspecsAccepted": wsManagedAPTspecsAccepted,
       "wsManagedAPTspecsRejected": wsManagedAPTspecsRejected,
       "wsManagedAPRoamingTspecsAccepted": wsManagedAPRoamingTspecsAccepted,
       "wsManagedAPRoamingTspecsRejected": wsManagedAPRoamingTspecsRejected,
       "wsManagedAPRadioTspecStatusTable": wsManagedAPRadioTspecStatusTable,
       "wsManagedAPRadioTspecStatusEntry": wsManagedAPRadioTspecStatusEntry,
       "wsManagedAPRadioTspecOperStatus": wsManagedAPRadioTspecOperStatus,
       "wsManagedAPRadioTspecNumActiveTrafficStreams": wsManagedAPRadioTspecNumActiveTrafficStreams,
       "wsManagedAPRadioTspecNumTrafficStreamClients": wsManagedAPRadioTspecNumTrafficStreamClients,
       "wsManagedAPRadioTspecNumTrafficStreamRoamingClients": wsManagedAPRadioTspecNumTrafficStreamRoamingClients,
       "wsManagedAPRadioTspecMediumTimeAdmitted": wsManagedAPRadioTspecMediumTimeAdmitted,
       "wsManagedAPRadioTspecMediumTimeUnallocated": wsManagedAPRadioTspecMediumTimeUnallocated,
       "wsManagedAPRadioTspecMediumTimeRoamingUnallocated": wsManagedAPRadioTspecMediumTimeRoamingUnallocated,
       "wsManagedAPRadioTspecStatisticsTable": wsManagedAPRadioTspecStatisticsTable,
       "wsManagedAPRadioTspecStatisticsEntry": wsManagedAPRadioTspecStatisticsEntry,
       "wsManagedAPRadioTspecPktsRecvd": wsManagedAPRadioTspecPktsRecvd,
       "wsManagedAPRadioTspecPktsTransmitted": wsManagedAPRadioTspecPktsTransmitted,
       "wsManagedAPRadioTspecBytesRecvd": wsManagedAPRadioTspecBytesRecvd,
       "wsManagedAPRadioTspecBytesTransmitted": wsManagedAPRadioTspecBytesTransmitted,
       "wsManagedAPVAPTspecStatusTable": wsManagedAPVAPTspecStatusTable,
       "wsManagedAPVAPTspecStatusEntry": wsManagedAPVAPTspecStatusEntry,
       "wsManagedAPVAPTspecOperStatus": wsManagedAPVAPTspecOperStatus,
       "wsManagedAPVAPTspecNumActiveTrafficStreams": wsManagedAPVAPTspecNumActiveTrafficStreams,
       "wsManagedAPVAPTspecNumTrafficStreamClients": wsManagedAPVAPTspecNumTrafficStreamClients,
       "wsManagedAPVAPTspecNumTrafficStreamRoamingClients": wsManagedAPVAPTspecNumTrafficStreamRoamingClients,
       "wsManagedAPVAPTspecMediumTimeAdmitted": wsManagedAPVAPTspecMediumTimeAdmitted,
       "wsManagedAPVAPTspecMediumTimeUnallocated": wsManagedAPVAPTspecMediumTimeUnallocated,
       "wsManagedAPVAPTspecMediumTimeRoamingUnallocated": wsManagedAPVAPTspecMediumTimeRoamingUnallocated,
       "wsManagedAPVAPTspecStatisticsTable": wsManagedAPVAPTspecStatisticsTable,
       "wsManagedAPVAPTspecStatisticsEntry": wsManagedAPVAPTspecStatisticsEntry,
       "wsManagedAPVAPTspecPktsRecvd": wsManagedAPVAPTspecPktsRecvd,
       "wsManagedAPVAPTspecPktsTransmitted": wsManagedAPVAPTspecPktsTransmitted,
       "wsManagedAPVAPTspecBytesRecvd": wsManagedAPVAPTspecBytesRecvd,
       "wsManagedAPVAPTspecBytesTransmitted": wsManagedAPVAPTspecBytesTransmitted,
       "tspecClient": tspecClient,
       "wsAssociatedClientTsStatusTable": wsAssociatedClientTsStatusTable,
       "wsAssociatedClientTsStatusEntry": wsAssociatedClientTsStatusEntry,
       "wsAssociatedClientTsTid": wsAssociatedClientTsTid,
       "wsAssociatedClientTsAccessCategory": wsAssociatedClientTsAccessCategory,
       "wsAssociatedClientTsDirection": wsAssociatedClientTsDirection,
       "wsAssociatedClientTsUserPriority": wsAssociatedClientTsUserPriority,
       "wsAssociatedClientTsMediumTime": wsAssociatedClientTsMediumTime,
       "wsAssociatedClientTsExcessUsageEvents": wsAssociatedClientTsExcessUsageEvents,
       "wsAssociatedClientTsRoamingClientIndicator": wsAssociatedClientTsRoamingClientIndicator,
       "wsAssociatedClientTsStatisticsTable": wsAssociatedClientTsStatisticsTable,
       "wsAssociatedClientTsStatisticsEntry": wsAssociatedClientTsStatisticsEntry,
       "wsAssociatedClientTsPktsRecvd": wsAssociatedClientTsPktsRecvd,
       "wsAssociatedClientTsPktsTransmitted": wsAssociatedClientTsPktsTransmitted,
       "wsAssociatedClientTsBytesRecvd": wsAssociatedClientTsBytesRecvd,
       "wsAssociatedClientTsBytesTransmitted": wsAssociatedClientTsBytesTransmitted,
       "provisioning": provisioning,
       "wsAPProvisioningTable": wsAPProvisioningTable,
       "wsAPProvisioningEntry": wsAPProvisioningEntry,
       "wsAPProvMacAddress": wsAPProvMacAddress,
       "wsAPProvIPAddress": wsAPProvIPAddress,
       "wsAPProvPrimarySwitchIP": wsAPProvPrimarySwitchIP,
       "wsAPProvBackupSwitchIP": wsAPProvBackupSwitchIP,
       "wsAPProvMutualAuthMode": wsAPProvMutualAuthMode,
       "wsAPProvUnmanagedAPReprovMode": wsAPProvUnmanagedAPReprovMode,
       "wsAPProvAge": wsAPProvAge,
       "wsAPProvNewPrimarySwitchIP": wsAPProvNewPrimarySwitchIP,
       "wsAPProvNewBackupSwitchIP": wsAPProvNewBackupSwitchIP,
       "wsAPProvNewProfileId": wsAPProvNewProfileId,
       "wsAPProvCommand": wsAPProvCommand,
       "wsAPProvStatus": wsAPProvStatus,
       "wsAPProvCertProfileTxStatus": wsAPProvCertProfileTxStatus,
       "wsAPProvEntryPurge": wsAPProvEntryPurge,
       "wsAPProvisioningInitiateAll": wsAPProvisioningInitiateAll,
       "wsAPProvisioningDeleteAll": wsAPProvisioningDeleteAll,
       "wsNetworkExchangeCertificates": wsNetworkExchangeCertificates,
       "wsSwitchProvIPAddress": wsSwitchProvIPAddress,
       "wsSwitchProvStatus": wsSwitchProvStatus,
       "wsSwitchCertReqTarget": wsSwitchCertReqTarget,
       "wsSwitchCertReqStatus": wsSwitchCertReqStatus,
       "wsSwitchProvisioningCommand": wsSwitchProvisioningCommand,
       "wsSwitchCertReqCommand": wsSwitchCertReqCommand,
       "wdsManagedAP": wdsManagedAP,
       "wsWDSAPGroupTable": wsWDSAPGroupTable,
       "wsWDSAPGroupEntry": wsWDSAPGroupEntry,
       "wsWDSAPGroupId": wsWDSAPGroupId,
       "wsWDSAPGroupName": wsWDSAPGroupName,
       "wsWDSAPGroupSpanningTree": wsWDSAPGroupSpanningTree,
       "wsWDSAPGroupPassword": wsWDSAPGroupPassword,
       "wsWDSAPGroupRowStatus": wsWDSAPGroupRowStatus,
       "wsWDSAPGroupAPTable": wsWDSAPGroupAPTable,
       "wsWDSAPGroupAPEntry": wsWDSAPGroupAPEntry,
       "wsWDSAPGroupAPMacAddress": wsWDSAPGroupAPMacAddress,
       "wsWDSAPGroupAPStpPriority": wsWDSAPGroupAPStpPriority,
       "wsWDSAPGroupAPEntryRowStatus": wsWDSAPGroupAPEntryRowStatus,
       "wsWDSAPLinkTable": wsWDSAPLinkTable,
       "wsWDSAPLinkEntry": wsWDSAPLinkEntry,
       "wsWDSAPLinkSourceMacAddr": wsWDSAPLinkSourceMacAddr,
       "wsWDSAPLinkSourceRadio": wsWDSAPLinkSourceRadio,
       "wsWDSAPLinkDestMacAddr": wsWDSAPLinkDestMacAddr,
       "wsWDSAPLinkDestRadio": wsWDSAPLinkDestRadio,
       "wsWDSAPLinkPathCost": wsWDSAPLinkPathCost,
       "wsWDSAPLinkRowStatus": wsWDSAPLinkRowStatus,
       "wsWDSAPGroupStatusTable": wsWDSAPGroupStatusTable,
       "wsWDSAPGroupStatusEntry": wsWDSAPGroupStatusEntry,
       "wsWDSConfigAPCount": wsWDSConfigAPCount,
       "wsWDSConnectedAPCount": wsWDSConnectedAPCount,
       "wsWDSRootAPCount": wsWDSRootAPCount,
       "wsWDSSatelliteAPCount": wsWDSSatelliteAPCount,
       "wsWDSAPRootBridge": wsWDSAPRootBridge,
       "wsWDSAPRootDeviceType": wsWDSAPRootDeviceType,
       "wsWDSConfigWDSLinkCount": wsWDSConfigWDSLinkCount,
       "wsWDSDetectedWDSLinkCount": wsWDSDetectedWDSLinkCount,
       "wsWDSBlockedWDSLinkCount": wsWDSBlockedWDSLinkCount,
       "wsWDSGroupNewPassword": wsWDSGroupNewPassword,
       "wsWDSGroupChangePasswdStart": wsWDSGroupChangePasswdStart,
       "wsWDSGroupChangePasswdStatus": wsWDSGroupChangePasswdStatus,
       "wsWDSAPStatusTable": wsWDSAPStatusTable,
       "wsWDSAPStatusEntry": wsWDSAPStatusEntry,
       "wsWDSAPMacAddr": wsWDSAPMacAddr,
       "wsWDSAPConnectionStatus": wsWDSAPConnectionStatus,
       "wsWDSAPSatelliteMode": wsWDSAPSatelliteMode,
       "wsWDSAPSTPRootMode": wsWDSAPSTPRootMode,
       "wsWDSAPSTPCost": wsWDSAPSTPCost,
       "wsWDSAPEthPortSTPStatus": wsWDSAPEthPortSTPStatus,
       "wsWDSAPEthPortMode": wsWDSAPEthPortMode,
       "wsWDSAPEthPortLinkState": wsWDSAPEthPortLinkState,
       "wsWDSLinkStatusTable": wsWDSLinkStatusTable,
       "wsWDSLinkStatusEntry": wsWDSLinkStatusEntry,
       "wsWDSSourceMacAddr": wsWDSSourceMacAddr,
       "wsWDSSourceRadio": wsWDSSourceRadio,
       "wsWDSDestMacAddr": wsWDSDestMacAddr,
       "wsWDSDestRadio": wsWDSDestRadio,
       "wsWDSLinkSourceEndPointDetected": wsWDSLinkSourceEndPointDetected,
       "wsWDSLinkDestEndPointDetected": wsWDSLinkDestEndPointDetected,
       "wsWDSLinkSourceSTPState": wsWDSLinkSourceSTPState,
       "wsWDSLinkDestSTPState": wsWDSLinkDestSTPState,
       "wsWDSLinkAggregationMode": wsWDSLinkAggregationMode,
       "wsWDSLinkStatisticsTable": wsWDSLinkStatisticsTable,
       "wsWDSLinkStatisticsEntry": wsWDSLinkStatisticsEntry,
       "wsWDSLinkSourceAPPktsSent": wsWDSLinkSourceAPPktsSent,
       "wsWDSLinkSourceAPBytesSent": wsWDSLinkSourceAPBytesSent,
       "wsWDSLinkSourceAPPktsRcvd": wsWDSLinkSourceAPPktsRcvd,
       "wsWDSLinkSourceAPBytesRcvd": wsWDSLinkSourceAPBytesRcvd,
       "wsWDSLinkDestAPPktsSent": wsWDSLinkDestAPPktsSent,
       "wsWDSLinkDestAPBytesSent": wsWDSLinkDestAPBytesSent,
       "wsWDSLinkDestAPPktsRcvd": wsWDSLinkDestAPPktsRcvd,
       "wsWDSLinkDestAPBytesRcvd": wsWDSLinkDestAPBytesRcvd,
       "wsWDSGroupConfigRequestAction": wsWDSGroupConfigRequestAction,
       "deviceLocation": deviceLocation,
       "wsDevLocBldngTable": wsDevLocBldngTable,
       "wsDevLocBldngEntry": wsDevLocBldngEntry,
       "wsDevLocBldngNum": wsDevLocBldngNum,
       "wsDevLocBldngDesc": wsDevLocBldngDesc,
       "wsDevLocFlrCount": wsDevLocFlrCount,
       "wsDevLocApCount": wsDevLocApCount,
       "wsDevLocBldngRowStatus": wsDevLocBldngRowStatus,
       "wsDevLocBldngFlrTable": wsDevLocBldngFlrTable,
       "wsDevLocBldngFlrEntry": wsDevLocBldngFlrEntry,
       "wsDevLocBldngFlrNum": wsDevLocBldngFlrNum,
       "wsDevLocBldngFlrDesc": wsDevLocBldngFlrDesc,
       "wsDevLocBldngFlrApCount": wsDevLocBldngFlrApCount,
       "wsDevLocFlrRowStatus": wsDevLocFlrRowStatus,
       "wsDevLocManagedApTable": wsDevLocManagedApTable,
       "wsDevLocManagedApEntry": wsDevLocManagedApEntry,
       "wsDevLocManagedApMac": wsDevLocManagedApMac,
       "wsDevLocMeasurementUnit": wsDevLocMeasurementUnit,
       "wsDevLocManagedApXCoord": wsDevLocManagedApXCoord,
       "wsDevLocManagedApYCoord": wsDevLocManagedApYCoord,
       "wsDevLocManagedApRowStatus": wsDevLocManagedApRowStatus,
       "wsOnDemandTrigger": wsOnDemandTrigger,
       "wsOnDemandTriggerDeviceType": wsOnDemandTriggerDeviceType,
       "wsOnDemandTriggerDeviceMACAddress": wsOnDemandTriggerDeviceMACAddress,
       "wsOnDemandTriggerBuildingNumber": wsOnDemandTriggerBuildingNumber,
       "wsOnDemandTriggerFloorNumber": wsOnDemandTriggerFloorNumber,
       "wsOnDemandTriggerUseRadios": wsOnDemandTriggerUseRadios,
       "wsOnDemandTriggerStatus": wsOnDemandTriggerStatus,
       "wsOnDemandTriggerNumOfAPs": wsOnDemandTriggerNumOfAPs,
       "wsOnDemandTriggerStart": wsOnDemandTriggerStart,
       "wsOnDemandTriggerGlobalStatus": wsOnDemandTriggerGlobalStatus,
       "wsOnDemandTriggerGlobalStatusDeviceType": wsOnDemandTriggerGlobalStatusDeviceType,
       "wsOnDemandTriggerGlobalStatusDeviceMACAddress": wsOnDemandTriggerGlobalStatusDeviceMACAddress,
       "wsOnDemandTriggerGlobalStatusBuildingNumber": wsOnDemandTriggerGlobalStatusBuildingNumber,
       "wsOnDemandTriggerGlobalStatusFloorNumber": wsOnDemandTriggerGlobalStatusFloorNumber,
       "wsOnDemandTriggerGlobalStatusUsedRadios": wsOnDemandTriggerGlobalStatusUsedRadios,
       "wsOnDemandTriggerGlobalStatusCurrentStatus": wsOnDemandTriggerGlobalStatusCurrentStatus,
       "wsOnDemandTriggerGlobalStatusSearchTime": wsOnDemandTriggerGlobalStatusSearchTime,
       "wsOnDemandTriggerGlobalStatusNumOfLocatorAPs": wsOnDemandTriggerGlobalStatusNumOfLocatorAPs,
       "wsOnDemandTriggerGlobalStatusNumOfDetectedAPs": wsOnDemandTriggerGlobalStatusNumOfDetectedAPs,
       "wsOnDemandTriggerGlobalStatusNumOfDetectedBuildings": wsOnDemandTriggerGlobalStatusNumOfDetectedBuildings,
       "wsOnDemandTriggerGlobalStatusNumOfDetectedFloors": wsOnDemandTriggerGlobalStatusNumOfDetectedFloors,
       "wsOnDemandTriggerGlobalStatusHighestSignalFoundBuilding": wsOnDemandTriggerGlobalStatusHighestSignalFoundBuilding,
       "wsOnDemandTriggerGlobalStatusHighestSignalFoundFloor": wsOnDemandTriggerGlobalStatusHighestSignalFoundFloor,
       "wsOnDemandTriggerFloorStatus": wsOnDemandTriggerFloorStatus,
       "wsOnDemandTriggerFloorStatusTable": wsOnDemandTriggerFloorStatusTable,
       "wsOnDemandTriggerFloorStatusEntry": wsOnDemandTriggerFloorStatusEntry,
       "wsOnDemandTriggerFloorStatusBuildingNum": wsOnDemandTriggerFloorStatusBuildingNum,
       "wsOnDemandTriggerFloorStatusFloorNum": wsOnDemandTriggerFloorStatusFloorNum,
       "wsOnDemandTriggerFloorStatusDeviceFound": wsOnDemandTriggerFloorStatusDeviceFound,
       "wsOnDemandTriggerFloorStatusNumOfAPs": wsOnDemandTriggerFloorStatusNumOfAPs,
       "wsOnDemandTriggerFloorStatusSolutionType": wsOnDemandTriggerFloorStatusSolutionType,
       "wsOnDemandTriggerFloorStatusXCoordinate": wsOnDemandTriggerFloorStatusXCoordinate,
       "wsOnDemandTriggerFloorStatusYCoordinate": wsOnDemandTriggerFloorStatusYCoordinate,
       "wsOnDemandTriggerFloorStatusCircleRadius": wsOnDemandTriggerFloorStatusCircleRadius,
       "wsOnDemandTriggerFloorStatusSigma": wsOnDemandTriggerFloorStatusSigma,
       "wsTriangulationLocStatusTable": wsTriangulationLocStatusTable,
       "wsTriangulationLocStatusEntry": wsTriangulationLocStatusEntry,
       "wsTriangLocMacAddress": wsTriangLocMacAddress,
       "wsTriangLocDataType": wsTriangLocDataType,
       "wsTriangLocStatus": wsTriangLocStatus,
       "wsTriangLocDeviceType": wsTriangLocDeviceType,
       "wsTriangLocAge": wsTriangLocAge,
       "wsTriangLocBldng": wsTriangLocBldng,
       "wsTriangLocFlr": wsTriangLocFlr,
       "wsTriangLocXCoord": wsTriangLocXCoord,
       "wsTriangLocYCoord": wsTriangLocYCoord,
       "authenticatedClient": authenticatedClient,
       "wsAuthenticatedClientStatusTable": wsAuthenticatedClientStatusTable,
       "wsAuthenticatedClientStatusEntry": wsAuthenticatedClientStatusEntry,
       "wsAuthenticatedClientMacAddress": wsAuthenticatedClientMacAddress,
       "wsAuthenticatedClientTunnelIpAddress": wsAuthenticatedClientTunnelIpAddress,
       "wsAuthenticatedClientUserName": wsAuthenticatedClientUserName,
       "wsAuthenticatedClientSSID": wsAuthenticatedClientSSID,
       "wsAuthenticatedClientVLAN": wsAuthenticatedClientVLAN,
       "wsAuthenticatedClientStatus": wsAuthenticatedClientStatus,
       "wsAuthenticatedClientTxDataRate": wsAuthenticatedClientTxDataRate,
       "wsAuthenticatedClientInactivePeriod": wsAuthenticatedClientInactivePeriod,
       "wsAuthenticatedClientDisassociateAction": wsAuthenticatedClientDisassociateAction,
       "wsAuthenticatedClientAge": wsAuthenticatedClientAge,
       "wsAuthenticatedClientAssociatingSwitch": wsAuthenticatedClientAssociatingSwitch,
       "wsAuthenticatedClientSwitchMacAddress": wsAuthenticatedClientSwitchMacAddress,
       "wsAuthenticatedClientSwitchIpAddress": wsAuthenticatedClientSwitchIpAddress,
       "wsAuthenticatedClientDot11nCapable": wsAuthenticatedClientDot11nCapable,
       "wsAuthenticatedClientStbcCapable": wsAuthenticatedClientStbcCapable,
       "wsAuthenticatedClientDistTunnelStatus": wsAuthenticatedClientDistTunnelStatus,
       "wsAuthenticatedClientDistTunnelRoamStatus": wsAuthenticatedClientDistTunnelRoamStatus,
       "wsAuthenticatedClientDistTunnelHomeAPMac": wsAuthenticatedClientDistTunnelHomeAPMac,
       "wsAuthenticatedClientDistTunnelAssocAPMac": wsAuthenticatedClientDistTunnelAssocAPMac,
       "wsAuthenticatedClientAPMacAddress": wsAuthenticatedClientAPMacAddress,
       "wsAuthenticatedClientBSSID": wsAuthenticatedClientBSSID,
       "wsAuthenticatedClientRadioInterface": wsAuthenticatedClientRadioInterface,
       "wsAuthenticatedClientChannel": wsAuthenticatedClientChannel,
       "wsAuthenticatedClientNwTime": wsAuthenticatedClientNwTime,
       "wsAuthenticatedClientIpAddress": wsAuthenticatedClientIpAddress,
       "wsAuthenticatedClientNetBiosName": wsAuthenticatedClientNetBiosName,
       "wsAuthenticatedClientRRMSupported": wsAuthenticatedClientRRMSupported,
       "wsAuthenticatedClientRRMLocationReportSupported": wsAuthenticatedClientRRMLocationReportSupported,
       "wsAuthenticatedClientRRMBeaconTableMeasurementSupported": wsAuthenticatedClientRRMBeaconTableMeasurementSupported,
       "wsAuthenticatedClientRRMBeaconActiveMeasurementSupported": wsAuthenticatedClientRRMBeaconActiveMeasurementSupported,
       "wsAuthenticatedClientRRMBeaconPassiveMeasurementSupported": wsAuthenticatedClientRRMBeaconPassiveMeasurementSupported,
       "wsAuthenticatedClientRRMChannelLoadMeasurementSupported": wsAuthenticatedClientRRMChannelLoadMeasurementSupported,
       "wsAuthenticatedClientDot11acCapable": wsAuthenticatedClientDot11acCapable,
       "wsAuthenticatedClientStatisticsTable": wsAuthenticatedClientStatisticsTable,
       "wsAuthenticatedClientStatisticsEntry": wsAuthenticatedClientStatisticsEntry,
       "wsAuthenticatedClientPktsRecvd": wsAuthenticatedClientPktsRecvd,
       "wsAuthenticatedClientBytesRecvd": wsAuthenticatedClientBytesRecvd,
       "wsAuthenticatedClientPktsTransmitted": wsAuthenticatedClientPktsTransmitted,
       "wsAuthenticatedClientBytesTransmitted": wsAuthenticatedClientBytesTransmitted,
       "wsAuthenticatedClientDuplicatePktsRecvd": wsAuthenticatedClientDuplicatePktsRecvd,
       "wsAuthenticatedClientFragmentedPktsRecvd": wsAuthenticatedClientFragmentedPktsRecvd,
       "wsAuthenticatedClientFragmentedPktsTransmitted": wsAuthenticatedClientFragmentedPktsTransmitted,
       "wsAuthenticatedClientTransmitRetryCount": wsAuthenticatedClientTransmitRetryCount,
       "wsAuthenticatedClientTransmitRetryFailedCount": wsAuthenticatedClientTransmitRetryFailedCount,
       "wsAuthenticatedClientPktsRecvDropped": wsAuthenticatedClientPktsRecvDropped,
       "wsAuthenticatedClientBytesRecvDropped": wsAuthenticatedClientBytesRecvDropped,
       "wsAuthenticatedClientPktsTransmitDropped": wsAuthenticatedClientPktsTransmitDropped,
       "wsAuthenticatedClientBytesTransmitDropped": wsAuthenticatedClientBytesTransmitDropped,
       "wsAuthenticatedClientTsViolatePktsRecvd": wsAuthenticatedClientTsViolatePktsRecvd,
       "wsAuthenticatedClientTsViolatePktsTransmitted": wsAuthenticatedClientTsViolatePktsTransmitted,
       "wsAuthenticatedClientNeighborManagedAPStatusTable": wsAuthenticatedClientNeighborManagedAPStatusTable,
       "wsAuthenticatedClientNeighborManagedAPStatusEntry": wsAuthenticatedClientNeighborManagedAPStatusEntry,
       "wsAuthenticatedClientStationMacAddress": wsAuthenticatedClientStationMacAddress,
       "wsAuthenticatedClientNeighborWSManagedAPMacAddress": wsAuthenticatedClientNeighborWSManagedAPMacAddress,
       "wsAuthenticatedClientNeighborWSManagedAPRadioInterface": wsAuthenticatedClientNeighborWSManagedAPRadioInterface,
       "wsAuthenticatedClientStationDiscoveryReason": wsAuthenticatedClientStationDiscoveryReason,
       "wsVAPAuthenticatedClientStatusTable": wsVAPAuthenticatedClientStatusTable,
       "wsVAPAuthenticatedClientStatusEntry": wsVAPAuthenticatedClientStatusEntry,
       "wsAuthenticatedVAPMacAddress": wsAuthenticatedVAPMacAddress,
       "wsVAPAuthenticatedClientMacAddress": wsVAPAuthenticatedClientMacAddress,
       "wsSSIDAuthenticatedClientStatusTable": wsSSIDAuthenticatedClientStatusTable,
       "wsSSIDAuthenticatedClientStatusEntry": wsSSIDAuthenticatedClientStatusEntry,
       "wsAuthenticatedSSID": wsAuthenticatedSSID,
       "wsSSIDAuthenticatedClientMacAddress": wsSSIDAuthenticatedClientMacAddress,
       "wsSwitchAuthenticatedClientStatusTable": wsSwitchAuthenticatedClientStatusTable,
       "wsSwitchAuthenticatedClientStatusEntry": wsSwitchAuthenticatedClientStatusEntry,
       "wsAuthenticatedClientSwitchIPAddress": wsAuthenticatedClientSwitchIPAddress,
       "wsSwitchAuthenticatedClientMacAddress": wsSwitchAuthenticatedClientMacAddress,
       "wsAuthenticatedClientQosStatusTable": wsAuthenticatedClientQosStatusTable,
       "wsAuthenticatedClientQosStatusEntry": wsAuthenticatedClientQosStatusEntry,
       "wsAuthenticatedClientQosBandwidthLimitDown": wsAuthenticatedClientQosBandwidthLimitDown,
       "wsAuthenticatedClientQosBandwidthLimitUp": wsAuthenticatedClientQosBandwidthLimitUp,
       "wsAuthenticatedClientQosAccessControlDownType": wsAuthenticatedClientQosAccessControlDownType,
       "wsAuthenticatedClientQosAccessControlDownName": wsAuthenticatedClientQosAccessControlDownName,
       "wsAuthenticatedClientQosAccessControlUpType": wsAuthenticatedClientQosAccessControlUpType,
       "wsAuthenticatedClientQosAccessControlUpName": wsAuthenticatedClientQosAccessControlUpName,
       "wsAuthenticatedClientQosDiffservPolicyDownType": wsAuthenticatedClientQosDiffservPolicyDownType,
       "wsAuthenticatedClientQosDiffservPolicyDownName": wsAuthenticatedClientQosDiffservPolicyDownName,
       "wsAuthenticatedClientQosDiffservPolicyUpType": wsAuthenticatedClientQosDiffservPolicyUpType,
       "wsAuthenticatedClientQosDiffservPolicyUpName": wsAuthenticatedClientQosDiffservPolicyUpName,
       "wsAuthenticatedClientQosOperStatus": wsAuthenticatedClientQosOperStatus,
       "wsAuthenticatedClientSessionStatisticsTable": wsAuthenticatedClientSessionStatisticsTable,
       "wsAuthenticatedClientSessionStatisticsEntry": wsAuthenticatedClientSessionStatisticsEntry,
       "wsAuthenticatedClientSessionPktsRecvd": wsAuthenticatedClientSessionPktsRecvd,
       "wsAuthenticatedClientSessionBytesRecvd": wsAuthenticatedClientSessionBytesRecvd,
       "wsAuthenticatedClientSessionPktsTransmitted": wsAuthenticatedClientSessionPktsTransmitted,
       "wsAuthenticatedClientSessionBytesTransmitted": wsAuthenticatedClientSessionBytesTransmitted,
       "wsAuthenticatedClientSessionDuplicatePktsRecvd": wsAuthenticatedClientSessionDuplicatePktsRecvd,
       "wsAuthenticatedClientSessionFragmentedPktsRecvd": wsAuthenticatedClientSessionFragmentedPktsRecvd,
       "wsAuthenticatedClientSessionFragmentedPktsTransmitted": wsAuthenticatedClientSessionFragmentedPktsTransmitted,
       "wsAuthenticatedClientSessionTransmitRetryCount": wsAuthenticatedClientSessionTransmitRetryCount,
       "wsAuthenticatedClientSessionTransmitRetryFailedCount": wsAuthenticatedClientSessionTransmitRetryFailedCount,
       "wsAuthenticatedClientSessionPktsRecvDropped": wsAuthenticatedClientSessionPktsRecvDropped,
       "wsAuthenticatedClientSessionBytesRecvDropped": wsAuthenticatedClientSessionBytesRecvDropped,
       "wsAuthenticatedClientSessionPktsTransmitDropped": wsAuthenticatedClientSessionPktsTransmitDropped,
       "wsAuthenticatedClientSessionBytesTransmitDropped": wsAuthenticatedClientSessionBytesTransmitDropped,
       "wsAuthenticatedClientSessionTSViolatePktsRecvd": wsAuthenticatedClientSessionTSViolatePktsRecvd,
       "wsAuthenticatedClientSessionTSViolatePktsTransmitted": wsAuthenticatedClientSessionTSViolatePktsTransmitted,
       "wsAuthenticatedClientQosCachedStatusTable": wsAuthenticatedClientQosCachedStatusTable,
       "wsAuthenticatedClientQosCachedStatusEntry": wsAuthenticatedClientQosCachedStatusEntry,
       "wsAuthenticatedClientQosCachedBandwidthLimitDown": wsAuthenticatedClientQosCachedBandwidthLimitDown,
       "wsAuthenticatedClientQosCachedBandwidthLimitUp": wsAuthenticatedClientQosCachedBandwidthLimitUp,
       "wsAuthenticatedClientQosCachedAccessControlDownType": wsAuthenticatedClientQosCachedAccessControlDownType,
       "wsAuthenticatedClientQosCachedAccessControlDownName": wsAuthenticatedClientQosCachedAccessControlDownName,
       "wsAuthenticatedClientQosCachedAccessControlUpType": wsAuthenticatedClientQosCachedAccessControlUpType,
       "wsAuthenticatedClientQosCachedAccessControlUpName": wsAuthenticatedClientQosCachedAccessControlUpName,
       "wsAuthenticatedClientQosCachedDiffservPolicyDownType": wsAuthenticatedClientQosCachedDiffservPolicyDownType,
       "wsAuthenticatedClientQosCachedDiffservPolicyDownName": wsAuthenticatedClientQosCachedDiffservPolicyDownName,
       "wsAuthenticatedClientQosCachedDiffservPolicyUpType": wsAuthenticatedClientQosCachedDiffservPolicyUpType,
       "wsAuthenticatedClientQosCachedDiffservPolicyUpName": wsAuthenticatedClientQosCachedDiffservPolicyUpName}
)
