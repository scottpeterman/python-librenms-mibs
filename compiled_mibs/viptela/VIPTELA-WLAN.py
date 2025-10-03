# SNMP MIB module (VIPTELA-WLAN) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\viptela\VIPTELA-WLAN
# Produced by pysmi-1.6.2 at Thu Oct  2 12:34:10 2025
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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(viptela,) = mibBuilder.importSymbols(
    "VIPTELA-GLOBAL",
    "viptela")


# MODULE-IDENTITY

viptela_wlan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 18)
)
if mibBuilder.loadTexts:
    viptela_wlan.setRevisions(
        ("2020-07-01 00:00",
         "2020-02-24 00:00",
         "2019-11-15 00:00",
         "2019-08-15 00:00",
         "2018-11-01 00:00",
         "2018-08-20 00:00",
         "2018-06-25 00:00",
         "2018-04-25 00:00",
         "2018-03-15 00:00",
         "2018-01-16 00:00",
         "2017-11-01 00:00",
         "2017-08-01 00:00",
         "2017-05-25 00:00",
         "2017-04-06 00:00",
         "2017-02-15 00:00",
         "2017-02-06 00:00",
         "2016-11-16 00:00",
         "2016-10-25 00:00",
         "2016-10-24 00:00",
         "2016-08-10 00:00",
         "2016-08-01 00:00",
         "2016-06-09 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class UnsignedByte(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class ConfdString(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class InetAddressIP(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )



class String(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class HexList(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x:"


class CountryCode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(36,
              40,
              56,
              76,
              100,
              124,
              144,
              156,
              158,
              188,
              191,
              196,
              203,
              208,
              233,
              246,
              250,
              276,
              300,
              344,
              348,
              352,
              356,
              360,
              372,
              380,
              392,
              412,
              428,
              438,
              440,
              442,
              458,
              470,
              484,
              528,
              554,
              578,
              586,
              591,
              608,
              616,
              620,
              630,
              642,
              682,
              702,
              703,
              704,
              705,
              710,
              724,
              752,
              756,
              764,
              792,
              826,
              843)
        )
    )
    namedValues = NamedValues(
        *(("australia", 36),
          ("austria", 40),
          ("belgium", 56),
          ("brazil", 76),
          ("bulgaria", 100),
          ("canada", 124),
          ("sri-Lanka", 144),
          ("china", 156),
          ("taiwan", 158),
          ("costa-Rica", 188),
          ("croatia", 191),
          ("cyprus", 196),
          ("czech-Republic", 203),
          ("denmark", 208),
          ("estonia", 233),
          ("finland", 246),
          ("france", 250),
          ("germany", 276),
          ("greece", 300),
          ("hong-Kong", 344),
          ("hungary", 348),
          ("iceland", 352),
          ("india", 356),
          ("indonesia", 360),
          ("ireland", 372),
          ("italy", 380),
          ("japan", 392),
          ("south-Korea", 412),
          ("latvia", 428),
          ("liechtenstein", 438),
          ("lithuania", 440),
          ("luxembourg", 442),
          ("malaysia", 458),
          ("malta", 470),
          ("mexico", 484),
          ("netherlands", 528),
          ("new-Zealand", 554),
          ("norway", 578),
          ("pakistan", 586),
          ("panama", 591),
          ("philippines", 608),
          ("poland", 616),
          ("portugal", 620),
          ("puerto-Rico", 630),
          ("romania", 642),
          ("saudi-Arabia", 682),
          ("singapore", 702),
          ("slovakia", 703),
          ("vietnam", 704),
          ("slovenia", 705),
          ("south-Africa", 710),
          ("spain", 724),
          ("sweden", 752),
          ("switzerland", 756),
          ("thailand", 764),
          ("turkey", 792),
          ("united-Kingdom", 826),
          ("united-States", 843))
    )



class WlanSecurityType(TextualConvention, Integer32):
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
        *(("none", 0),
          ("wpa-personal", 1),
          ("wpa2-personal", 2),
          ("wpa-wpa2-personal", 3),
          ("wpa-enterprise", 4),
          ("wpa2-enterprise", 5),
          ("wpa-wpa2-enterprise", 6))
    )



class WlanBandStr(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("five-GHz", 0),
          ("twofour-GHz", 1))
    )



class WlanPmfType(TextualConvention, Integer32):
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
        *(("none", 0),
          ("optional", 1),
          ("required", 2))
    )



class RadiusServers(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class WlanBand(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fiveGHz", 0),
          ("twofourGHz", 1))
    )



class RadiusServers1(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class WlanGi(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(400,
              800)
        )
    )
    namedValues = NamedValues(
        *(("gi400", 400),
          ("gi800", 800))
    )



class WlanBw(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(20,
              40,
              80)
        )
    )
    namedValues = NamedValues(
        *(("bw20", 20),
          ("bw40", 40),
          ("bw80", 80))
    )



# MIB Managed Objects in the order of their OIDs

_Wlan_ObjectIdentity = ObjectIdentity
wlan = _Wlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1)
)
_WlanRadiosTable_Object = MibTable
wlanRadiosTable = _WlanRadiosTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 1)
)
if mibBuilder.loadTexts:
    wlanRadiosTable.setStatus("current")
_WlanRadiosEntry_Object = MibTableRow
wlanRadiosEntry = _WlanRadiosEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 1, 1)
)
wlanRadiosEntry.setIndexNames(
    (1, "VIPTELA-WLAN", "wlanRadiosRadioName"),
)
if mibBuilder.loadTexts:
    wlanRadiosEntry.setStatus("current")


class _WlanRadiosRadioName_Type(String):
    """Custom type wlanRadiosRadioName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_WlanRadiosRadioName_Type.__name__ = "String"
_WlanRadiosRadioName_Object = MibTableColumn
wlanRadiosRadioName = _WlanRadiosRadioName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 1, 1, 1),
    _WlanRadiosRadioName_Type()
)
wlanRadiosRadioName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wlanRadiosRadioName.setStatus("current")


class _WlanRadiosMode_Type(String):
    """Custom type wlanRadiosMode based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 18),
    )


_WlanRadiosMode_Type.__name__ = "String"
_WlanRadiosMode_Object = MibTableColumn
wlanRadiosMode = _WlanRadiosMode_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 1, 1, 2),
    _WlanRadiosMode_Type()
)
wlanRadiosMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanRadiosMode.setStatus("current")
_WlanRadiosBand_Type = WlanBandStr
_WlanRadiosBand_Object = MibTableColumn
wlanRadiosBand = _WlanRadiosBand_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 1, 1, 3),
    _WlanRadiosBand_Type()
)
wlanRadiosBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanRadiosBand.setStatus("current")


class _WlanRadiosMac_Type(String):
    """Custom type wlanRadiosMac based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 18),
    )


_WlanRadiosMac_Type.__name__ = "String"
_WlanRadiosMac_Object = MibTableColumn
wlanRadiosMac = _WlanRadiosMac_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 1, 1, 4),
    _WlanRadiosMac_Type()
)
wlanRadiosMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanRadiosMac.setStatus("current")
_WlanRadiosCountry_Type = CountryCode
_WlanRadiosCountry_Object = MibTableColumn
wlanRadiosCountry = _WlanRadiosCountry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 1, 1, 5),
    _WlanRadiosCountry_Type()
)
wlanRadiosCountry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanRadiosCountry.setStatus("current")
_WlanRadiosChannel_Type = UnsignedByte
_WlanRadiosChannel_Object = MibTableColumn
wlanRadiosChannel = _WlanRadiosChannel_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 1, 1, 6),
    _WlanRadiosChannel_Type()
)
wlanRadiosChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanRadiosChannel.setStatus("current")
_WlanRadiosChannelBandwidth_Type = WlanBw
_WlanRadiosChannelBandwidth_Object = MibTableColumn
wlanRadiosChannelBandwidth = _WlanRadiosChannelBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 1, 1, 7),
    _WlanRadiosChannelBandwidth_Type()
)
wlanRadiosChannelBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanRadiosChannelBandwidth.setStatus("current")
_WlanRadiosFrequency_Type = Unsigned32
_WlanRadiosFrequency_Object = MibTableColumn
wlanRadiosFrequency = _WlanRadiosFrequency_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 1, 1, 8),
    _WlanRadiosFrequency_Type()
)
wlanRadiosFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanRadiosFrequency.setStatus("current")
_WlanRadiosGuardInterval_Type = WlanGi
_WlanRadiosGuardInterval_Object = MibTableColumn
wlanRadiosGuardInterval = _WlanRadiosGuardInterval_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 1, 1, 9),
    _WlanRadiosGuardInterval_Type()
)
wlanRadiosGuardInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanRadiosGuardInterval.setStatus("current")
_WlanRadiosVaps_Type = UnsignedByte
_WlanRadiosVaps_Object = MibTableColumn
wlanRadiosVaps = _WlanRadiosVaps_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 1, 1, 10),
    _WlanRadiosVaps_Type()
)
wlanRadiosVaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanRadiosVaps.setStatus("current")
_WlanInterfacesTable_Object = MibTable
wlanInterfacesTable = _WlanInterfacesTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 2)
)
if mibBuilder.loadTexts:
    wlanInterfacesTable.setStatus("current")
_WlanInterfacesEntry_Object = MibTableRow
wlanInterfacesEntry = _WlanInterfacesEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 2, 1)
)
wlanInterfacesEntry.setIndexNames(
    (1, "VIPTELA-WLAN", "wlanInterfacesVap"),
)
if mibBuilder.loadTexts:
    wlanInterfacesEntry.setStatus("current")


class _WlanInterfacesVap_Type(String):
    """Custom type wlanInterfacesVap based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_WlanInterfacesVap_Type.__name__ = "String"
_WlanInterfacesVap_Object = MibTableColumn
wlanInterfacesVap = _WlanInterfacesVap_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 2, 1, 1),
    _WlanInterfacesVap_Type()
)
wlanInterfacesVap.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wlanInterfacesVap.setStatus("current")


class _WlanInterfacesSsid_Type(String):
    """Custom type wlanInterfacesSsid based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 32),
    )


_WlanInterfacesSsid_Type.__name__ = "String"
_WlanInterfacesSsid_Object = MibTableColumn
wlanInterfacesSsid = _WlanInterfacesSsid_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 2, 1, 2),
    _WlanInterfacesSsid_Type()
)
wlanInterfacesSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanInterfacesSsid.setStatus("current")


class _WlanInterfacesBssid_Type(String):
    """Custom type wlanInterfacesBssid based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 18),
    )


_WlanInterfacesBssid_Type.__name__ = "String"
_WlanInterfacesBssid_Object = MibTableColumn
wlanInterfacesBssid = _WlanInterfacesBssid_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 2, 1, 3),
    _WlanInterfacesBssid_Type()
)
wlanInterfacesBssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanInterfacesBssid.setStatus("current")
_WlanInterfacesDataSecurity_Type = WlanSecurityType
_WlanInterfacesDataSecurity_Object = MibTableColumn
wlanInterfacesDataSecurity = _WlanInterfacesDataSecurity_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 2, 1, 4),
    _WlanInterfacesDataSecurity_Type()
)
wlanInterfacesDataSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanInterfacesDataSecurity.setStatus("current")
_WlanInterfacesMgmtSecurity_Type = WlanPmfType
_WlanInterfacesMgmtSecurity_Object = MibTableColumn
wlanInterfacesMgmtSecurity = _WlanInterfacesMgmtSecurity_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 2, 1, 5),
    _WlanInterfacesMgmtSecurity_Type()
)
wlanInterfacesMgmtSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanInterfacesMgmtSecurity.setStatus("current")
_WlanInterfacesBand_Type = WlanBandStr
_WlanInterfacesBand_Object = MibTableColumn
wlanInterfacesBand = _WlanInterfacesBand_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 2, 1, 6),
    _WlanInterfacesBand_Type()
)
wlanInterfacesBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanInterfacesBand.setStatus("current")


class _WlanInterfacesMode_Type(String):
    """Custom type wlanInterfacesMode based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 18),
    )


_WlanInterfacesMode_Type.__name__ = "String"
_WlanInterfacesMode_Object = MibTableColumn
wlanInterfacesMode = _WlanInterfacesMode_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 2, 1, 7),
    _WlanInterfacesMode_Type()
)
wlanInterfacesMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanInterfacesMode.setStatus("current")


class _WlanInterfacesDescription_Type(String):
    """Custom type wlanInterfacesDescription based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 64),
    )


_WlanInterfacesDescription_Type.__name__ = "String"
_WlanInterfacesDescription_Object = MibTableColumn
wlanInterfacesDescription = _WlanInterfacesDescription_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 2, 1, 8),
    _WlanInterfacesDescription_Type()
)
wlanInterfacesDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanInterfacesDescription.setStatus("current")
_WlanInterfacesBitRate_Type = Unsigned32
_WlanInterfacesBitRate_Object = MibTableColumn
wlanInterfacesBitRate = _WlanInterfacesBitRate_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 2, 1, 9),
    _WlanInterfacesBitRate_Type()
)
wlanInterfacesBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanInterfacesBitRate.setStatus("current")
_WlanInterfacesTxPower_Type = Unsigned32
_WlanInterfacesTxPower_Object = MibTableColumn
wlanInterfacesTxPower = _WlanInterfacesTxPower_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 2, 1, 10),
    _WlanInterfacesTxPower_Type()
)
wlanInterfacesTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanInterfacesTxPower.setStatus("current")
_WlanInterfacesMaxClients_Type = UnsignedByte
_WlanInterfacesMaxClients_Object = MibTableColumn
wlanInterfacesMaxClients = _WlanInterfacesMaxClients_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 2, 1, 11),
    _WlanInterfacesMaxClients_Type()
)
wlanInterfacesMaxClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanInterfacesMaxClients.setStatus("current")


class _WlanInterfacesAdminStatus_Type(String):
    """Custom type wlanInterfacesAdminStatus based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_WlanInterfacesAdminStatus_Type.__name__ = "String"
_WlanInterfacesAdminStatus_Object = MibTableColumn
wlanInterfacesAdminStatus = _WlanInterfacesAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 2, 1, 12),
    _WlanInterfacesAdminStatus_Type()
)
wlanInterfacesAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanInterfacesAdminStatus.setStatus("current")


class _WlanInterfacesOperStatus_Type(String):
    """Custom type wlanInterfacesOperStatus based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_WlanInterfacesOperStatus_Type.__name__ = "String"
_WlanInterfacesOperStatus_Object = MibTableColumn
wlanInterfacesOperStatus = _WlanInterfacesOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 2, 1, 13),
    _WlanInterfacesOperStatus_Type()
)
wlanInterfacesOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanInterfacesOperStatus.setStatus("current")
_WlanInterfacesNumClients_Type = UnsignedByte
_WlanInterfacesNumClients_Object = MibTableColumn
wlanInterfacesNumClients = _WlanInterfacesNumClients_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 2, 1, 14),
    _WlanInterfacesNumClients_Type()
)
wlanInterfacesNumClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanInterfacesNumClients.setStatus("current")
_WlanClientsTable_Object = MibTable
wlanClientsTable = _WlanClientsTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 3)
)
if mibBuilder.loadTexts:
    wlanClientsTable.setStatus("current")
_WlanClientsEntry_Object = MibTableRow
wlanClientsEntry = _WlanClientsEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 3, 1)
)
wlanClientsEntry.setIndexNames(
    (0, "VIPTELA-WLAN", "wlanClientsVap"),
    (0, "VIPTELA-WLAN", "wlanClientsClientId"),
)
if mibBuilder.loadTexts:
    wlanClientsEntry.setStatus("current")


class _WlanClientsVap_Type(String):
    """Custom type wlanClientsVap based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_WlanClientsVap_Type.__name__ = "String"
_WlanClientsVap_Object = MibTableColumn
wlanClientsVap = _WlanClientsVap_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 3, 1, 1),
    _WlanClientsVap_Type()
)
wlanClientsVap.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wlanClientsVap.setStatus("current")
_WlanClientsClientId_Type = Unsigned32
_WlanClientsClientId_Object = MibTableColumn
wlanClientsClientId = _WlanClientsClientId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 3, 1, 2),
    _WlanClientsClientId_Type()
)
wlanClientsClientId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wlanClientsClientId.setStatus("current")


class _WlanClientsMac_Type(String):
    """Custom type wlanClientsMac based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 18),
    )


_WlanClientsMac_Type.__name__ = "String"
_WlanClientsMac_Object = MibTableColumn
wlanClientsMac = _WlanClientsMac_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 3, 1, 3),
    _WlanClientsMac_Type()
)
wlanClientsMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanClientsMac.setStatus("current")


class _WlanClientsMode_Type(String):
    """Custom type wlanClientsMode based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 18),
    )


_WlanClientsMode_Type.__name__ = "String"
_WlanClientsMode_Object = MibTableColumn
wlanClientsMode = _WlanClientsMode_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 3, 1, 4),
    _WlanClientsMode_Type()
)
wlanClientsMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanClientsMode.setStatus("current")
_WlanClientsBand_Type = WlanBandStr
_WlanClientsBand_Object = MibTableColumn
wlanClientsBand = _WlanClientsBand_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 3, 1, 5),
    _WlanClientsBand_Type()
)
wlanClientsBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanClientsBand.setStatus("current")
_WlanClientsChannel_Type = Unsigned32
_WlanClientsChannel_Object = MibTableColumn
wlanClientsChannel = _WlanClientsChannel_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 3, 1, 6),
    _WlanClientsChannel_Type()
)
wlanClientsChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanClientsChannel.setStatus("current")
_WlanClientsChannelBandwidth_Type = WlanBw
_WlanClientsChannelBandwidth_Object = MibTableColumn
wlanClientsChannelBandwidth = _WlanClientsChannelBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 3, 1, 7),
    _WlanClientsChannelBandwidth_Type()
)
wlanClientsChannelBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanClientsChannelBandwidth.setStatus("current")
_WlanClientsDataSecurity_Type = WlanSecurityType
_WlanClientsDataSecurity_Object = MibTableColumn
wlanClientsDataSecurity = _WlanClientsDataSecurity_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 3, 1, 8),
    _WlanClientsDataSecurity_Type()
)
wlanClientsDataSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanClientsDataSecurity.setStatus("current")
_WlanClientsRxRate_Type = Unsigned32
_WlanClientsRxRate_Object = MibTableColumn
wlanClientsRxRate = _WlanClientsRxRate_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 3, 1, 9),
    _WlanClientsRxRate_Type()
)
wlanClientsRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanClientsRxRate.setStatus("current")
_WlanClientsRssi_Type = Unsigned32
_WlanClientsRssi_Object = MibTableColumn
wlanClientsRssi = _WlanClientsRssi_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 3, 1, 10),
    _WlanClientsRssi_Type()
)
wlanClientsRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanClientsRssi.setStatus("current")


class _WlanClientsAssocTime_Type(String):
    """Custom type wlanClientsAssocTime based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_WlanClientsAssocTime_Type.__name__ = "String"
_WlanClientsAssocTime_Object = MibTableColumn
wlanClientsAssocTime = _WlanClientsAssocTime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 3, 1, 11),
    _WlanClientsAssocTime_Type()
)
wlanClientsAssocTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanClientsAssocTime.setStatus("current")
_WlanRadiusTable_Object = MibTable
wlanRadiusTable = _WlanRadiusTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 4)
)
if mibBuilder.loadTexts:
    wlanRadiusTable.setStatus("current")
_WlanRadiusEntry_Object = MibTableRow
wlanRadiusEntry = _WlanRadiusEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 4, 1)
)
wlanRadiusEntry.setIndexNames(
    (0, "VIPTELA-WLAN", "wlanRadiusVapIfname"),
    (0, "VIPTELA-WLAN", "wlanRadiusPreference"),
)
if mibBuilder.loadTexts:
    wlanRadiusEntry.setStatus("current")


class _WlanRadiusVapIfname_Type(String):
    """Custom type wlanRadiusVapIfname based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_WlanRadiusVapIfname_Type.__name__ = "String"
_WlanRadiusVapIfname_Object = MibTableColumn
wlanRadiusVapIfname = _WlanRadiusVapIfname_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 4, 1, 1),
    _WlanRadiusVapIfname_Type()
)
wlanRadiusVapIfname.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wlanRadiusVapIfname.setStatus("current")
_WlanRadiusPreference_Type = Unsigned32
_WlanRadiusPreference_Object = MibTableColumn
wlanRadiusPreference = _WlanRadiusPreference_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 4, 1, 2),
    _WlanRadiusPreference_Type()
)
wlanRadiusPreference.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wlanRadiusPreference.setStatus("current")
_WlanRadiusIpAddress_Type = InetAddressIP
_WlanRadiusIpAddress_Object = MibTableColumn
wlanRadiusIpAddress = _WlanRadiusIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 4, 1, 3),
    _WlanRadiusIpAddress_Type()
)
wlanRadiusIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanRadiusIpAddress.setStatus("current")


class _WlanRadiusVpnId_Type(Unsigned32):
    """Custom type wlanRadiusVpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_WlanRadiusVpnId_Type.__name__ = "Unsigned32"
_WlanRadiusVpnId_Object = MibTableColumn
wlanRadiusVpnId = _WlanRadiusVpnId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 4, 1, 4),
    _WlanRadiusVpnId_Type()
)
wlanRadiusVpnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanRadiusVpnId.setStatus("current")
_WlanRadiusPriority_Type = Unsigned32
_WlanRadiusPriority_Object = MibTableColumn
wlanRadiusPriority = _WlanRadiusPriority_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 4, 1, 5),
    _WlanRadiusPriority_Type()
)
wlanRadiusPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanRadiusPriority.setStatus("current")


class _WlanRadiusSourceInterface_Type(String):
    """Custom type wlanRadiusSourceInterface based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WlanRadiusSourceInterface_Type.__name__ = "String"
_WlanRadiusSourceInterface_Object = MibTableColumn
wlanRadiusSourceInterface = _WlanRadiusSourceInterface_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 4, 1, 6),
    _WlanRadiusSourceInterface_Type()
)
wlanRadiusSourceInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanRadiusSourceInterface.setStatus("current")
_WlanRadiusSourceAddress_Type = InetAddressIP
_WlanRadiusSourceAddress_Object = MibTableColumn
wlanRadiusSourceAddress = _WlanRadiusSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 4, 1, 7),
    _WlanRadiusSourceAddress_Type()
)
wlanRadiusSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanRadiusSourceAddress.setStatus("current")


class _WlanRadiusTag_Type(String):
    """Custom type wlanRadiusTag based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 16),
    )


_WlanRadiusTag_Type.__name__ = "String"
_WlanRadiusTag_Object = MibTableColumn
wlanRadiusTag = _WlanRadiusTag_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 4, 1, 8),
    _WlanRadiusTag_Type()
)
wlanRadiusTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanRadiusTag.setStatus("current")
_WlanRadiusAuthPort_Type = Unsigned32
_WlanRadiusAuthPort_Object = MibTableColumn
wlanRadiusAuthPort = _WlanRadiusAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 4, 1, 9),
    _WlanRadiusAuthPort_Type()
)
wlanRadiusAuthPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanRadiusAuthPort.setStatus("current")
_WlanRadiusAuthActive_Type = TruthValue
_WlanRadiusAuthActive_Object = MibTableColumn
wlanRadiusAuthActive = _WlanRadiusAuthActive_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 4, 1, 10),
    _WlanRadiusAuthActive_Type()
)
wlanRadiusAuthActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanRadiusAuthActive.setStatus("current")
_WlanRadiusAuthRTT_Type = Unsigned32
_WlanRadiusAuthRTT_Object = MibTableColumn
wlanRadiusAuthRTT = _WlanRadiusAuthRTT_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 4, 1, 11),
    _WlanRadiusAuthRTT_Type()
)
wlanRadiusAuthRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanRadiusAuthRTT.setStatus("current")
_WlanRadiusAuthRequests_Type = Unsigned32
_WlanRadiusAuthRequests_Object = MibTableColumn
wlanRadiusAuthRequests = _WlanRadiusAuthRequests_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 4, 1, 12),
    _WlanRadiusAuthRequests_Type()
)
wlanRadiusAuthRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanRadiusAuthRequests.setStatus("current")
_WlanRadiusAuthRetrans_Type = Unsigned32
_WlanRadiusAuthRetrans_Object = MibTableColumn
wlanRadiusAuthRetrans = _WlanRadiusAuthRetrans_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 4, 1, 13),
    _WlanRadiusAuthRetrans_Type()
)
wlanRadiusAuthRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanRadiusAuthRetrans.setStatus("current")
_WlanRadiusAuthAccepts_Type = Unsigned32
_WlanRadiusAuthAccepts_Object = MibTableColumn
wlanRadiusAuthAccepts = _WlanRadiusAuthAccepts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 4, 1, 14),
    _WlanRadiusAuthAccepts_Type()
)
wlanRadiusAuthAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanRadiusAuthAccepts.setStatus("current")
_WlanRadiusAuthRejects_Type = Unsigned32
_WlanRadiusAuthRejects_Object = MibTableColumn
wlanRadiusAuthRejects = _WlanRadiusAuthRejects_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 4, 1, 15),
    _WlanRadiusAuthRejects_Type()
)
wlanRadiusAuthRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanRadiusAuthRejects.setStatus("current")
_WlanRadiusAuthChallenges_Type = Unsigned32
_WlanRadiusAuthChallenges_Object = MibTableColumn
wlanRadiusAuthChallenges = _WlanRadiusAuthChallenges_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 4, 1, 16),
    _WlanRadiusAuthChallenges_Type()
)
wlanRadiusAuthChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanRadiusAuthChallenges.setStatus("current")
_WlanRadiusAuthMalResp_Type = Unsigned32
_WlanRadiusAuthMalResp_Object = MibTableColumn
wlanRadiusAuthMalResp = _WlanRadiusAuthMalResp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 4, 1, 17),
    _WlanRadiusAuthMalResp_Type()
)
wlanRadiusAuthMalResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanRadiusAuthMalResp.setStatus("current")
_WlanRadiusAuthBadAuth_Type = Unsigned32
_WlanRadiusAuthBadAuth_Object = MibTableColumn
wlanRadiusAuthBadAuth = _WlanRadiusAuthBadAuth_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 4, 1, 18),
    _WlanRadiusAuthBadAuth_Type()
)
wlanRadiusAuthBadAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanRadiusAuthBadAuth.setStatus("current")
_WlanRadiusAuthPendReqs_Type = Unsigned32
_WlanRadiusAuthPendReqs_Object = MibTableColumn
wlanRadiusAuthPendReqs = _WlanRadiusAuthPendReqs_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 4, 1, 19),
    _WlanRadiusAuthPendReqs_Type()
)
wlanRadiusAuthPendReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanRadiusAuthPendReqs.setStatus("current")
_WlanRadiusAuthTimeouts_Type = Unsigned32
_WlanRadiusAuthTimeouts_Object = MibTableColumn
wlanRadiusAuthTimeouts = _WlanRadiusAuthTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 4, 1, 20),
    _WlanRadiusAuthTimeouts_Type()
)
wlanRadiusAuthTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanRadiusAuthTimeouts.setStatus("current")
_WlanRadiusAuthUnkTypes_Type = Unsigned32
_WlanRadiusAuthUnkTypes_Object = MibTableColumn
wlanRadiusAuthUnkTypes = _WlanRadiusAuthUnkTypes_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 4, 1, 21),
    _WlanRadiusAuthUnkTypes_Type()
)
wlanRadiusAuthUnkTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanRadiusAuthUnkTypes.setStatus("current")
_WlanRadiusAuthPktsDrop_Type = Unsigned32
_WlanRadiusAuthPktsDrop_Object = MibTableColumn
wlanRadiusAuthPktsDrop = _WlanRadiusAuthPktsDrop_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 4, 1, 22),
    _WlanRadiusAuthPktsDrop_Type()
)
wlanRadiusAuthPktsDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanRadiusAuthPktsDrop.setStatus("current")
_WlanRadiusAcctPort_Type = Unsigned32
_WlanRadiusAcctPort_Object = MibTableColumn
wlanRadiusAcctPort = _WlanRadiusAcctPort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 4, 1, 23),
    _WlanRadiusAcctPort_Type()
)
wlanRadiusAcctPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanRadiusAcctPort.setStatus("current")
_WlanRadiusAcctActive_Type = TruthValue
_WlanRadiusAcctActive_Object = MibTableColumn
wlanRadiusAcctActive = _WlanRadiusAcctActive_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 4, 1, 24),
    _WlanRadiusAcctActive_Type()
)
wlanRadiusAcctActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanRadiusAcctActive.setStatus("current")
_WlanRadiusAcctRTT_Type = Unsigned32
_WlanRadiusAcctRTT_Object = MibTableColumn
wlanRadiusAcctRTT = _WlanRadiusAcctRTT_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 4, 1, 25),
    _WlanRadiusAcctRTT_Type()
)
wlanRadiusAcctRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanRadiusAcctRTT.setStatus("current")
_WlanRadiusAcctRequests_Type = Unsigned32
_WlanRadiusAcctRequests_Object = MibTableColumn
wlanRadiusAcctRequests = _WlanRadiusAcctRequests_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 4, 1, 26),
    _WlanRadiusAcctRequests_Type()
)
wlanRadiusAcctRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanRadiusAcctRequests.setStatus("current")
_WlanRadiusAcctRetrans_Type = Unsigned32
_WlanRadiusAcctRetrans_Object = MibTableColumn
wlanRadiusAcctRetrans = _WlanRadiusAcctRetrans_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 4, 1, 27),
    _WlanRadiusAcctRetrans_Type()
)
wlanRadiusAcctRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanRadiusAcctRetrans.setStatus("current")
_WlanRadiusAcctResponses_Type = Unsigned32
_WlanRadiusAcctResponses_Object = MibTableColumn
wlanRadiusAcctResponses = _WlanRadiusAcctResponses_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 4, 1, 28),
    _WlanRadiusAcctResponses_Type()
)
wlanRadiusAcctResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanRadiusAcctResponses.setStatus("current")
_WlanRadiusAcctMalResp_Type = Unsigned32
_WlanRadiusAcctMalResp_Object = MibTableColumn
wlanRadiusAcctMalResp = _WlanRadiusAcctMalResp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 4, 1, 29),
    _WlanRadiusAcctMalResp_Type()
)
wlanRadiusAcctMalResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanRadiusAcctMalResp.setStatus("current")
_WlanRadiusAcctBadAuth_Type = Unsigned32
_WlanRadiusAcctBadAuth_Object = MibTableColumn
wlanRadiusAcctBadAuth = _WlanRadiusAcctBadAuth_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 4, 1, 30),
    _WlanRadiusAcctBadAuth_Type()
)
wlanRadiusAcctBadAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanRadiusAcctBadAuth.setStatus("current")
_WlanRadiusAcctPendReqs_Type = Unsigned32
_WlanRadiusAcctPendReqs_Object = MibTableColumn
wlanRadiusAcctPendReqs = _WlanRadiusAcctPendReqs_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 4, 1, 31),
    _WlanRadiusAcctPendReqs_Type()
)
wlanRadiusAcctPendReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanRadiusAcctPendReqs.setStatus("current")
_WlanRadiusAcctTimeouts_Type = Unsigned32
_WlanRadiusAcctTimeouts_Object = MibTableColumn
wlanRadiusAcctTimeouts = _WlanRadiusAcctTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 4, 1, 32),
    _WlanRadiusAcctTimeouts_Type()
)
wlanRadiusAcctTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanRadiusAcctTimeouts.setStatus("current")
_WlanRadiusAcctUnkTypes_Type = Unsigned32
_WlanRadiusAcctUnkTypes_Object = MibTableColumn
wlanRadiusAcctUnkTypes = _WlanRadiusAcctUnkTypes_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 4, 1, 33),
    _WlanRadiusAcctUnkTypes_Type()
)
wlanRadiusAcctUnkTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanRadiusAcctUnkTypes.setStatus("current")
_WlanRadiusAcctPktsDrop_Type = Unsigned32
_WlanRadiusAcctPktsDrop_Object = MibTableColumn
wlanRadiusAcctPktsDrop = _WlanRadiusAcctPktsDrop_Object(
    (1, 3, 6, 1, 4, 1, 41916, 18, 1, 4, 1, 34),
    _WlanRadiusAcctPktsDrop_Type()
)
wlanRadiusAcctPktsDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanRadiusAcctPktsDrop.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VIPTELA-WLAN",
    **{"UnsignedByte": UnsignedByte,
       "ConfdString": ConfdString,
       "InetAddressIP": InetAddressIP,
       "String": String,
       "HexList": HexList,
       "CountryCode": CountryCode,
       "WlanSecurityType": WlanSecurityType,
       "WlanBandStr": WlanBandStr,
       "WlanPmfType": WlanPmfType,
       "RadiusServers": RadiusServers,
       "WlanBand": WlanBand,
       "RadiusServers1": RadiusServers1,
       "WlanGi": WlanGi,
       "WlanBw": WlanBw,
       "viptela-wlan": viptela_wlan,
       "wlan": wlan,
       "wlanRadiosTable": wlanRadiosTable,
       "wlanRadiosEntry": wlanRadiosEntry,
       "wlanRadiosRadioName": wlanRadiosRadioName,
       "wlanRadiosMode": wlanRadiosMode,
       "wlanRadiosBand": wlanRadiosBand,
       "wlanRadiosMac": wlanRadiosMac,
       "wlanRadiosCountry": wlanRadiosCountry,
       "wlanRadiosChannel": wlanRadiosChannel,
       "wlanRadiosChannelBandwidth": wlanRadiosChannelBandwidth,
       "wlanRadiosFrequency": wlanRadiosFrequency,
       "wlanRadiosGuardInterval": wlanRadiosGuardInterval,
       "wlanRadiosVaps": wlanRadiosVaps,
       "wlanInterfacesTable": wlanInterfacesTable,
       "wlanInterfacesEntry": wlanInterfacesEntry,
       "wlanInterfacesVap": wlanInterfacesVap,
       "wlanInterfacesSsid": wlanInterfacesSsid,
       "wlanInterfacesBssid": wlanInterfacesBssid,
       "wlanInterfacesDataSecurity": wlanInterfacesDataSecurity,
       "wlanInterfacesMgmtSecurity": wlanInterfacesMgmtSecurity,
       "wlanInterfacesBand": wlanInterfacesBand,
       "wlanInterfacesMode": wlanInterfacesMode,
       "wlanInterfacesDescription": wlanInterfacesDescription,
       "wlanInterfacesBitRate": wlanInterfacesBitRate,
       "wlanInterfacesTxPower": wlanInterfacesTxPower,
       "wlanInterfacesMaxClients": wlanInterfacesMaxClients,
       "wlanInterfacesAdminStatus": wlanInterfacesAdminStatus,
       "wlanInterfacesOperStatus": wlanInterfacesOperStatus,
       "wlanInterfacesNumClients": wlanInterfacesNumClients,
       "wlanClientsTable": wlanClientsTable,
       "wlanClientsEntry": wlanClientsEntry,
       "wlanClientsVap": wlanClientsVap,
       "wlanClientsClientId": wlanClientsClientId,
       "wlanClientsMac": wlanClientsMac,
       "wlanClientsMode": wlanClientsMode,
       "wlanClientsBand": wlanClientsBand,
       "wlanClientsChannel": wlanClientsChannel,
       "wlanClientsChannelBandwidth": wlanClientsChannelBandwidth,
       "wlanClientsDataSecurity": wlanClientsDataSecurity,
       "wlanClientsRxRate": wlanClientsRxRate,
       "wlanClientsRssi": wlanClientsRssi,
       "wlanClientsAssocTime": wlanClientsAssocTime,
       "wlanRadiusTable": wlanRadiusTable,
       "wlanRadiusEntry": wlanRadiusEntry,
       "wlanRadiusVapIfname": wlanRadiusVapIfname,
       "wlanRadiusPreference": wlanRadiusPreference,
       "wlanRadiusIpAddress": wlanRadiusIpAddress,
       "wlanRadiusVpnId": wlanRadiusVpnId,
       "wlanRadiusPriority": wlanRadiusPriority,
       "wlanRadiusSourceInterface": wlanRadiusSourceInterface,
       "wlanRadiusSourceAddress": wlanRadiusSourceAddress,
       "wlanRadiusTag": wlanRadiusTag,
       "wlanRadiusAuthPort": wlanRadiusAuthPort,
       "wlanRadiusAuthActive": wlanRadiusAuthActive,
       "wlanRadiusAuthRTT": wlanRadiusAuthRTT,
       "wlanRadiusAuthRequests": wlanRadiusAuthRequests,
       "wlanRadiusAuthRetrans": wlanRadiusAuthRetrans,
       "wlanRadiusAuthAccepts": wlanRadiusAuthAccepts,
       "wlanRadiusAuthRejects": wlanRadiusAuthRejects,
       "wlanRadiusAuthChallenges": wlanRadiusAuthChallenges,
       "wlanRadiusAuthMalResp": wlanRadiusAuthMalResp,
       "wlanRadiusAuthBadAuth": wlanRadiusAuthBadAuth,
       "wlanRadiusAuthPendReqs": wlanRadiusAuthPendReqs,
       "wlanRadiusAuthTimeouts": wlanRadiusAuthTimeouts,
       "wlanRadiusAuthUnkTypes": wlanRadiusAuthUnkTypes,
       "wlanRadiusAuthPktsDrop": wlanRadiusAuthPktsDrop,
       "wlanRadiusAcctPort": wlanRadiusAcctPort,
       "wlanRadiusAcctActive": wlanRadiusAcctActive,
       "wlanRadiusAcctRTT": wlanRadiusAcctRTT,
       "wlanRadiusAcctRequests": wlanRadiusAcctRequests,
       "wlanRadiusAcctRetrans": wlanRadiusAcctRetrans,
       "wlanRadiusAcctResponses": wlanRadiusAcctResponses,
       "wlanRadiusAcctMalResp": wlanRadiusAcctMalResp,
       "wlanRadiusAcctBadAuth": wlanRadiusAcctBadAuth,
       "wlanRadiusAcctPendReqs": wlanRadiusAcctPendReqs,
       "wlanRadiusAcctTimeouts": wlanRadiusAcctTimeouts,
       "wlanRadiusAcctUnkTypes": wlanRadiusAcctUnkTypes,
       "wlanRadiusAcctPktsDrop": wlanRadiusAcctPktsDrop}
)
