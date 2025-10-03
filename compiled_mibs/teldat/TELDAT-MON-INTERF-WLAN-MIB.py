# SNMP MIB module (TELDAT-MON-INTERF-WLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\teldat\TELDAT-MON-INTERF-WLAN-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:29:59 2025
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

(DisplayString,
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")

(telProdNpMonInterfRouter,) = mibBuilder.importSymbols(
    "TELDAT-SW-STRUCTURE-MIB",
    "telProdNpMonInterfRouter")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



class WlanRSSI(TextualConvention, Integer32):
    status = "mandatory"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-110, 0),
    )



class WlanRate(TextualConvention, Integer32):
    status = "mandatory"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )



# MIB Managed Objects in the order of their OIDs

_TelProdNpMonInterfWlan_ObjectIdentity = ObjectIdentity
telProdNpMonInterfWlan = _TelProdNpMonInterfWlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24)
)
_TelProdNpMonInterfWlanRadioTable_Object = MibTable
telProdNpMonInterfWlanRadioTable = _TelProdNpMonInterfWlanRadioTable_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 1)
)
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanRadioTable.setStatus("mandatory")
_TelProdNpMonInterfWlanRadioEntry_Object = MibTableRow
telProdNpMonInterfWlanRadioEntry = _TelProdNpMonInterfWlanRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 1, 1)
)
telProdNpMonInterfWlanRadioEntry.setIndexNames(
    (0, "TELDAT-MON-INTERF-WLAN-MIB", "telProdNpMonInterfWlanRadioIfIndex"),
)
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanRadioEntry.setStatus("mandatory")
_TelProdNpMonInterfWlanRadioIfIndex_Type = Integer32
_TelProdNpMonInterfWlanRadioIfIndex_Object = MibTableColumn
telProdNpMonInterfWlanRadioIfIndex = _TelProdNpMonInterfWlanRadioIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 1, 1, 1),
    _TelProdNpMonInterfWlanRadioIfIndex_Type()
)
telProdNpMonInterfWlanRadioIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanRadioIfIndex.setStatus("mandatory")


class _TelProdNpMonInterfWlanRadioIfMode_Type(Integer32):
    """Custom type telProdNpMonInterfWlanRadioIfMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              6,
              8,
              9,
              12,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("mode-11a", 1),
          ("mode-11b", 2),
          ("mode-11g", 4),
          ("mode-11b-11g", 6),
          ("mode-11n", 8),
          ("mode-11a-11n", 9),
          ("mode-11g-11n", 12),
          ("mode-11b-11g-11n", 14),
          ("mode-11a-11b-11g-11n", 15))
    )


_TelProdNpMonInterfWlanRadioIfMode_Type.__name__ = "Integer32"
_TelProdNpMonInterfWlanRadioIfMode_Object = MibTableColumn
telProdNpMonInterfWlanRadioIfMode = _TelProdNpMonInterfWlanRadioIfMode_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 1, 1, 2),
    _TelProdNpMonInterfWlanRadioIfMode_Type()
)
telProdNpMonInterfWlanRadioIfMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanRadioIfMode.setStatus("mandatory")
_TelProdNpMonInterfWlanRadioIfSpeed_Type = Integer32
_TelProdNpMonInterfWlanRadioIfSpeed_Object = MibTableColumn
telProdNpMonInterfWlanRadioIfSpeed = _TelProdNpMonInterfWlanRadioIfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 1, 1, 3),
    _TelProdNpMonInterfWlanRadioIfSpeed_Type()
)
telProdNpMonInterfWlanRadioIfSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanRadioIfSpeed.setStatus("mandatory")


class _TelProdNpMonInterfWlanRadioIfChannel_Type(Integer32):
    """Custom type telProdNpMonInterfWlanRadioIfChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 256),
    )


_TelProdNpMonInterfWlanRadioIfChannel_Type.__name__ = "Integer32"
_TelProdNpMonInterfWlanRadioIfChannel_Object = MibTableColumn
telProdNpMonInterfWlanRadioIfChannel = _TelProdNpMonInterfWlanRadioIfChannel_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 1, 1, 4),
    _TelProdNpMonInterfWlanRadioIfChannel_Type()
)
telProdNpMonInterfWlanRadioIfChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanRadioIfChannel.setStatus("mandatory")


class _TelProdNpMonInterfWlanRadioIfRtsThreshold_Type(Integer32):
    """Custom type telProdNpMonInterfWlanRadioIfRtsThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_TelProdNpMonInterfWlanRadioIfRtsThreshold_Type.__name__ = "Integer32"
_TelProdNpMonInterfWlanRadioIfRtsThreshold_Object = MibTableColumn
telProdNpMonInterfWlanRadioIfRtsThreshold = _TelProdNpMonInterfWlanRadioIfRtsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 1, 1, 5),
    _TelProdNpMonInterfWlanRadioIfRtsThreshold_Type()
)
telProdNpMonInterfWlanRadioIfRtsThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanRadioIfRtsThreshold.setStatus("mandatory")


class _TelProdNpMonInterfWlanRadioIfTxPower_Type(Integer32):
    """Custom type telProdNpMonInterfWlanRadioIfTxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_TelProdNpMonInterfWlanRadioIfTxPower_Type.__name__ = "Integer32"
_TelProdNpMonInterfWlanRadioIfTxPower_Object = MibTableColumn
telProdNpMonInterfWlanRadioIfTxPower = _TelProdNpMonInterfWlanRadioIfTxPower_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 1, 1, 6),
    _TelProdNpMonInterfWlanRadioIfTxPower_Type()
)
telProdNpMonInterfWlanRadioIfTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanRadioIfTxPower.setStatus("mandatory")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanRadioIfTxPower.setUnits("dBm")
_TelProdNpMonInterfWlanRadioIfBand_Type = Integer32
_TelProdNpMonInterfWlanRadioIfBand_Object = MibTableColumn
telProdNpMonInterfWlanRadioIfBand = _TelProdNpMonInterfWlanRadioIfBand_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 1, 1, 7),
    _TelProdNpMonInterfWlanRadioIfBand_Type()
)
telProdNpMonInterfWlanRadioIfBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanRadioIfBand.setStatus("mandatory")


class _TelProdNpMonInterfWlanRadioIfCountry_Type(DisplayString):
    """Custom type telProdNpMonInterfWlanRadioIfCountry based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_TelProdNpMonInterfWlanRadioIfCountry_Type.__name__ = "DisplayString"
_TelProdNpMonInterfWlanRadioIfCountry_Object = MibTableColumn
telProdNpMonInterfWlanRadioIfCountry = _TelProdNpMonInterfWlanRadioIfCountry_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 1, 1, 8),
    _TelProdNpMonInterfWlanRadioIfCountry_Type()
)
telProdNpMonInterfWlanRadioIfCountry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanRadioIfCountry.setStatus("mandatory")
_TelProdNpMonInterfWlanRadioIfAddress_Type = MacAddress
_TelProdNpMonInterfWlanRadioIfAddress_Object = MibTableColumn
telProdNpMonInterfWlanRadioIfAddress = _TelProdNpMonInterfWlanRadioIfAddress_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 1, 1, 9),
    _TelProdNpMonInterfWlanRadioIfAddress_Type()
)
telProdNpMonInterfWlanRadioIfAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanRadioIfAddress.setStatus("mandatory")


class _TelProdNpMonInterfWlanRadioIfRealChannel_Type(Integer32):
    """Custom type telProdNpMonInterfWlanRadioIfRealChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_TelProdNpMonInterfWlanRadioIfRealChannel_Type.__name__ = "Integer32"
_TelProdNpMonInterfWlanRadioIfRealChannel_Object = MibTableColumn
telProdNpMonInterfWlanRadioIfRealChannel = _TelProdNpMonInterfWlanRadioIfRealChannel_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 1, 1, 10),
    _TelProdNpMonInterfWlanRadioIfRealChannel_Type()
)
telProdNpMonInterfWlanRadioIfRealChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanRadioIfRealChannel.setStatus("mandatory")


class _TelProdNpMonInterfWlanRadioIfFragmentThreshold_Type(Integer32):
    """Custom type telProdNpMonInterfWlanRadioIfFragmentThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 8000),
    )


_TelProdNpMonInterfWlanRadioIfFragmentThreshold_Type.__name__ = "Integer32"
_TelProdNpMonInterfWlanRadioIfFragmentThreshold_Object = MibTableColumn
telProdNpMonInterfWlanRadioIfFragmentThreshold = _TelProdNpMonInterfWlanRadioIfFragmentThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 1, 1, 11),
    _TelProdNpMonInterfWlanRadioIfFragmentThreshold_Type()
)
telProdNpMonInterfWlanRadioIfFragmentThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanRadioIfFragmentThreshold.setStatus("mandatory")
_TelProdNpMonInterfWlanBSSTable_Object = MibTable
telProdNpMonInterfWlanBSSTable = _TelProdNpMonInterfWlanBSSTable_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 2)
)
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanBSSTable.setStatus("mandatory")
_TelProdNpMonInterfWlanBSSEntry_Object = MibTableRow
telProdNpMonInterfWlanBSSEntry = _TelProdNpMonInterfWlanBSSEntry_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 2, 1)
)
telProdNpMonInterfWlanBSSEntry.setIndexNames(
    (0, "TELDAT-MON-INTERF-WLAN-MIB", "telProdNpMonInterfWlanBSSIfIndex"),
)
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanBSSEntry.setStatus("mandatory")
_TelProdNpMonInterfWlanBSSIfIndex_Type = Integer32
_TelProdNpMonInterfWlanBSSIfIndex_Object = MibTableColumn
telProdNpMonInterfWlanBSSIfIndex = _TelProdNpMonInterfWlanBSSIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 2, 1, 1),
    _TelProdNpMonInterfWlanBSSIfIndex_Type()
)
telProdNpMonInterfWlanBSSIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanBSSIfIndex.setStatus("mandatory")


class _TelProdNpMonInterfWlanBSSId_Type(DisplayString):
    """Custom type telProdNpMonInterfWlanBSSId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TelProdNpMonInterfWlanBSSId_Type.__name__ = "DisplayString"
_TelProdNpMonInterfWlanBSSId_Object = MibTableColumn
telProdNpMonInterfWlanBSSId = _TelProdNpMonInterfWlanBSSId_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 2, 1, 2),
    _TelProdNpMonInterfWlanBSSId_Type()
)
telProdNpMonInterfWlanBSSId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanBSSId.setStatus("mandatory")


class _TelProdNpMonInterfWlanBSSPrivInvoked_Type(Integer32):
    """Custom type telProdNpMonInterfWlanBSSPrivInvoked based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("enable", 2))
    )


_TelProdNpMonInterfWlanBSSPrivInvoked_Type.__name__ = "Integer32"
_TelProdNpMonInterfWlanBSSPrivInvoked_Object = MibTableColumn
telProdNpMonInterfWlanBSSPrivInvoked = _TelProdNpMonInterfWlanBSSPrivInvoked_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 2, 1, 3),
    _TelProdNpMonInterfWlanBSSPrivInvoked_Type()
)
telProdNpMonInterfWlanBSSPrivInvoked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanBSSPrivInvoked.setStatus("mandatory")


class _TelProdNpMonInterfWlanBSSRsn_Type(Integer32):
    """Custom type telProdNpMonInterfWlanBSSRsn based on Integer32"""
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
        *(("wpa", 0),
          ("wpa2", 1),
          ("none", 2),
          ("wpa-wpa2", 3))
    )


_TelProdNpMonInterfWlanBSSRsn_Type.__name__ = "Integer32"
_TelProdNpMonInterfWlanBSSRsn_Object = MibTableColumn
telProdNpMonInterfWlanBSSRsn = _TelProdNpMonInterfWlanBSSRsn_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 2, 1, 4),
    _TelProdNpMonInterfWlanBSSRsn_Type()
)
telProdNpMonInterfWlanBSSRsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanBSSRsn.setStatus("mandatory")


class _TelProdNpMonInterfWlanBSSAkm_Type(Integer32):
    """Custom type telProdNpMonInterfWlanBSSAkm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dot1x", 0),
          ("psk", 1))
    )


_TelProdNpMonInterfWlanBSSAkm_Type.__name__ = "Integer32"
_TelProdNpMonInterfWlanBSSAkm_Object = MibTableColumn
telProdNpMonInterfWlanBSSAkm = _TelProdNpMonInterfWlanBSSAkm_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 2, 1, 5),
    _TelProdNpMonInterfWlanBSSAkm_Type()
)
telProdNpMonInterfWlanBSSAkm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanBSSAkm.setStatus("mandatory")


class _TelProdNpMonInterfWlanBSSCipher_Type(Integer32):
    """Custom type telProdNpMonInterfWlanBSSCipher based on Integer32"""
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
          ("auto", 1),
          ("wep", 2),
          ("tkip", 3),
          ("aes-ccm", 4))
    )


_TelProdNpMonInterfWlanBSSCipher_Type.__name__ = "Integer32"
_TelProdNpMonInterfWlanBSSCipher_Object = MibTableColumn
telProdNpMonInterfWlanBSSCipher = _TelProdNpMonInterfWlanBSSCipher_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 2, 1, 6),
    _TelProdNpMonInterfWlanBSSCipher_Type()
)
telProdNpMonInterfWlanBSSCipher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanBSSCipher.setStatus("mandatory")


class _TelProdNpMonInterfWlanBSSDefaultKey_Type(Integer32):
    """Custom type telProdNpMonInterfWlanBSSDefaultKey based on Integer32"""
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
        *(("key1", 1),
          ("key2", 2),
          ("key3", 3),
          ("key4", 4))
    )


_TelProdNpMonInterfWlanBSSDefaultKey_Type.__name__ = "Integer32"
_TelProdNpMonInterfWlanBSSDefaultKey_Object = MibTableColumn
telProdNpMonInterfWlanBSSDefaultKey = _TelProdNpMonInterfWlanBSSDefaultKey_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 2, 1, 7),
    _TelProdNpMonInterfWlanBSSDefaultKey_Type()
)
telProdNpMonInterfWlanBSSDefaultKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanBSSDefaultKey.setStatus("mandatory")


class _TelProdNpMonInterfWlanBSSKey1_Type(OctetString):
    """Custom type telProdNpMonInterfWlanBSSKey1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TelProdNpMonInterfWlanBSSKey1_Type.__name__ = "OctetString"
_TelProdNpMonInterfWlanBSSKey1_Object = MibTableColumn
telProdNpMonInterfWlanBSSKey1 = _TelProdNpMonInterfWlanBSSKey1_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 2, 1, 8),
    _TelProdNpMonInterfWlanBSSKey1_Type()
)
telProdNpMonInterfWlanBSSKey1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanBSSKey1.setStatus("mandatory")


class _TelProdNpMonInterfWlanBSSKey2_Type(OctetString):
    """Custom type telProdNpMonInterfWlanBSSKey2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 33),
    )


_TelProdNpMonInterfWlanBSSKey2_Type.__name__ = "OctetString"
_TelProdNpMonInterfWlanBSSKey2_Object = MibTableColumn
telProdNpMonInterfWlanBSSKey2 = _TelProdNpMonInterfWlanBSSKey2_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 2, 1, 9),
    _TelProdNpMonInterfWlanBSSKey2_Type()
)
telProdNpMonInterfWlanBSSKey2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanBSSKey2.setStatus("mandatory")


class _TelProdNpMonInterfWlanBSSKey3_Type(OctetString):
    """Custom type telProdNpMonInterfWlanBSSKey3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 33),
    )


_TelProdNpMonInterfWlanBSSKey3_Type.__name__ = "OctetString"
_TelProdNpMonInterfWlanBSSKey3_Object = MibTableColumn
telProdNpMonInterfWlanBSSKey3 = _TelProdNpMonInterfWlanBSSKey3_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 2, 1, 10),
    _TelProdNpMonInterfWlanBSSKey3_Type()
)
telProdNpMonInterfWlanBSSKey3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanBSSKey3.setStatus("mandatory")


class _TelProdNpMonInterfWlanBSSKey4_Type(OctetString):
    """Custom type telProdNpMonInterfWlanBSSKey4 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 33),
    )


_TelProdNpMonInterfWlanBSSKey4_Type.__name__ = "OctetString"
_TelProdNpMonInterfWlanBSSKey4_Object = MibTableColumn
telProdNpMonInterfWlanBSSKey4 = _TelProdNpMonInterfWlanBSSKey4_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 2, 1, 11),
    _TelProdNpMonInterfWlanBSSKey4_Type()
)
telProdNpMonInterfWlanBSSKey4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanBSSKey4.setStatus("mandatory")


class _TelProdNpMonInterfWlanBSSMaxAsoc_Type(Integer32):
    """Custom type telProdNpMonInterfWlanBSSMaxAsoc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_TelProdNpMonInterfWlanBSSMaxAsoc_Type.__name__ = "Integer32"
_TelProdNpMonInterfWlanBSSMaxAsoc_Object = MibTableColumn
telProdNpMonInterfWlanBSSMaxAsoc = _TelProdNpMonInterfWlanBSSMaxAsoc_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 2, 1, 12),
    _TelProdNpMonInterfWlanBSSMaxAsoc_Type()
)
telProdNpMonInterfWlanBSSMaxAsoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanBSSMaxAsoc.setStatus("mandatory")


class _TelProdNpMonInterfWlanBSSAcl_Type(Integer32):
    """Custom type telProdNpMonInterfWlanBSSAcl based on Integer32"""
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
          ("deny-entries", 1),
          ("allow-entries", 2))
    )


_TelProdNpMonInterfWlanBSSAcl_Type.__name__ = "Integer32"
_TelProdNpMonInterfWlanBSSAcl_Object = MibTableColumn
telProdNpMonInterfWlanBSSAcl = _TelProdNpMonInterfWlanBSSAcl_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 2, 1, 13),
    _TelProdNpMonInterfWlanBSSAcl_Type()
)
telProdNpMonInterfWlanBSSAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanBSSAcl.setStatus("mandatory")


class _TelProdNpMonInterfWlanBSSClientIsolation_Type(Integer32):
    """Custom type telProdNpMonInterfWlanBSSClientIsolation based on Integer32"""
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


_TelProdNpMonInterfWlanBSSClientIsolation_Type.__name__ = "Integer32"
_TelProdNpMonInterfWlanBSSClientIsolation_Object = MibTableColumn
telProdNpMonInterfWlanBSSClientIsolation = _TelProdNpMonInterfWlanBSSClientIsolation_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 2, 1, 14),
    _TelProdNpMonInterfWlanBSSClientIsolation_Type()
)
telProdNpMonInterfWlanBSSClientIsolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanBSSClientIsolation.setStatus("mandatory")


class _TelProdNpMonInterfWlanBSSHidden_Type(Integer32):
    """Custom type telProdNpMonInterfWlanBSSHidden based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TelProdNpMonInterfWlanBSSHidden_Type.__name__ = "Integer32"
_TelProdNpMonInterfWlanBSSHidden_Object = MibTableColumn
telProdNpMonInterfWlanBSSHidden = _TelProdNpMonInterfWlanBSSHidden_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 2, 1, 15),
    _TelProdNpMonInterfWlanBSSHidden_Type()
)
telProdNpMonInterfWlanBSSHidden.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanBSSHidden.setStatus("mandatory")
_TelProdNpMonInterfWlanBSSBssId_Type = MacAddress
_TelProdNpMonInterfWlanBSSBssId_Object = MibTableColumn
telProdNpMonInterfWlanBSSBssId = _TelProdNpMonInterfWlanBSSBssId_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 2, 1, 16),
    _TelProdNpMonInterfWlanBSSBssId_Type()
)
telProdNpMonInterfWlanBSSBssId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanBSSBssId.setStatus("mandatory")


class _TelProdNpMonInterfWlanBSSBeaconPeriod_Type(Integer32):
    """Custom type telProdNpMonInterfWlanBSSBeaconPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TelProdNpMonInterfWlanBSSBeaconPeriod_Type.__name__ = "Integer32"
_TelProdNpMonInterfWlanBSSBeaconPeriod_Object = MibTableColumn
telProdNpMonInterfWlanBSSBeaconPeriod = _TelProdNpMonInterfWlanBSSBeaconPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 2, 1, 17),
    _TelProdNpMonInterfWlanBSSBeaconPeriod_Type()
)
telProdNpMonInterfWlanBSSBeaconPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanBSSBeaconPeriod.setStatus("mandatory")


class _TelProdNpMonInterfWlanBSSDTIMPeriod_Type(Integer32):
    """Custom type telProdNpMonInterfWlanBSSDTIMPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TelProdNpMonInterfWlanBSSDTIMPeriod_Type.__name__ = "Integer32"
_TelProdNpMonInterfWlanBSSDTIMPeriod_Object = MibTableColumn
telProdNpMonInterfWlanBSSDTIMPeriod = _TelProdNpMonInterfWlanBSSDTIMPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 2, 1, 18),
    _TelProdNpMonInterfWlanBSSDTIMPeriod_Type()
)
telProdNpMonInterfWlanBSSDTIMPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanBSSDTIMPeriod.setStatus("mandatory")
_TelProdNpMonInterfWlanBSSMSDUTx_Type = Counter32
_TelProdNpMonInterfWlanBSSMSDUTx_Object = MibTableColumn
telProdNpMonInterfWlanBSSMSDUTx = _TelProdNpMonInterfWlanBSSMSDUTx_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 2, 1, 19),
    _TelProdNpMonInterfWlanBSSMSDUTx_Type()
)
telProdNpMonInterfWlanBSSMSDUTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanBSSMSDUTx.setStatus("mandatory")
_TelProdNpMonInterfWlanBSSMSDURx_Type = Counter32
_TelProdNpMonInterfWlanBSSMSDURx_Object = MibTableColumn
telProdNpMonInterfWlanBSSMSDURx = _TelProdNpMonInterfWlanBSSMSDURx_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 2, 1, 20),
    _TelProdNpMonInterfWlanBSSMSDURx_Type()
)
telProdNpMonInterfWlanBSSMSDURx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanBSSMSDURx.setStatus("mandatory")
_TelProdNpMonInterfWlanBSSBytesTx_Type = Counter32
_TelProdNpMonInterfWlanBSSBytesTx_Object = MibTableColumn
telProdNpMonInterfWlanBSSBytesTx = _TelProdNpMonInterfWlanBSSBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 2, 1, 21),
    _TelProdNpMonInterfWlanBSSBytesTx_Type()
)
telProdNpMonInterfWlanBSSBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanBSSBytesTx.setStatus("mandatory")
_TelProdNpMonInterfWlanBSSBytesRx_Type = Counter32
_TelProdNpMonInterfWlanBSSBytesRx_Object = MibTableColumn
telProdNpMonInterfWlanBSSBytesRx = _TelProdNpMonInterfWlanBSSBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 2, 1, 22),
    _TelProdNpMonInterfWlanBSSBytesRx_Type()
)
telProdNpMonInterfWlanBSSBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanBSSBytesRx.setStatus("mandatory")
_TelProdNpMonInterfWlanBSSCurrent_Type = Integer32
_TelProdNpMonInterfWlanBSSCurrent_Object = MibTableColumn
telProdNpMonInterfWlanBSSCurrent = _TelProdNpMonInterfWlanBSSCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 2, 1, 23),
    _TelProdNpMonInterfWlanBSSCurrent_Type()
)
telProdNpMonInterfWlanBSSCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanBSSCurrent.setStatus("mandatory")


class _TelProdNpMonInterfWlanBSSOpMode_Type(Integer32):
    """Custom type telProdNpMonInterfWlanBSSOpMode based on Integer32"""
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
        *(("access-point", 0),
          ("station", 1),
          ("wbr", 2),
          ("repeater", 3))
    )


_TelProdNpMonInterfWlanBSSOpMode_Type.__name__ = "Integer32"
_TelProdNpMonInterfWlanBSSOpMode_Object = MibTableColumn
telProdNpMonInterfWlanBSSOpMode = _TelProdNpMonInterfWlanBSSOpMode_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 2, 1, 24),
    _TelProdNpMonInterfWlanBSSOpMode_Type()
)
telProdNpMonInterfWlanBSSOpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanBSSOpMode.setStatus("mandatory")


class _TelProdNpMonInterfwlanBSSPassPhrase_Type(OctetString):
    """Custom type telProdNpMonInterfwlanBSSPassPhrase based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TelProdNpMonInterfwlanBSSPassPhrase_Type.__name__ = "OctetString"
_TelProdNpMonInterfwlanBSSPassPhrase_Object = MibTableColumn
telProdNpMonInterfwlanBSSPassPhrase = _TelProdNpMonInterfwlanBSSPassPhrase_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 2, 1, 25),
    _TelProdNpMonInterfwlanBSSPassPhrase_Type()
)
telProdNpMonInterfwlanBSSPassPhrase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfwlanBSSPassPhrase.setStatus("mandatory")
_TelProdNpMonInterfWlanStationTable_Object = MibTable
telProdNpMonInterfWlanStationTable = _TelProdNpMonInterfWlanStationTable_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 3)
)
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanStationTable.setStatus("mandatory")
_TelProdNpMonInterfWlanStationEntry_Object = MibTableRow
telProdNpMonInterfWlanStationEntry = _TelProdNpMonInterfWlanStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 3, 1)
)
telProdNpMonInterfWlanStationEntry.setIndexNames(
    (0, "TELDAT-MON-INTERF-WLAN-MIB", "telProdNpMonInterfWlanStationIfIndex"),
    (0, "TELDAT-MON-INTERF-WLAN-MIB", "telProdNpMonInterfWlanStationAddress"),
)
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanStationEntry.setStatus("mandatory")
_TelProdNpMonInterfWlanStationIfIndex_Type = Integer32
_TelProdNpMonInterfWlanStationIfIndex_Object = MibTableColumn
telProdNpMonInterfWlanStationIfIndex = _TelProdNpMonInterfWlanStationIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 3, 1, 1),
    _TelProdNpMonInterfWlanStationIfIndex_Type()
)
telProdNpMonInterfWlanStationIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanStationIfIndex.setStatus("mandatory")
_TelProdNpMonInterfWlanStationAddress_Type = MacAddress
_TelProdNpMonInterfWlanStationAddress_Object = MibTableColumn
telProdNpMonInterfWlanStationAddress = _TelProdNpMonInterfWlanStationAddress_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 3, 1, 2),
    _TelProdNpMonInterfWlanStationAddress_Type()
)
telProdNpMonInterfWlanStationAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanStationAddress.setStatus("mandatory")
_TelProdNpMonInterfWlanStationState_Type = Integer32
_TelProdNpMonInterfWlanStationState_Object = MibTableColumn
telProdNpMonInterfWlanStationState = _TelProdNpMonInterfWlanStationState_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 3, 1, 3),
    _TelProdNpMonInterfWlanStationState_Type()
)
telProdNpMonInterfWlanStationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanStationState.setStatus("mandatory")


class _TelProdNpMonInterfWlanStationSecurity_Type(Integer32):
    """Custom type telProdNpMonInterfWlanStationSecurity based on Integer32"""
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
          ("wep40", 2),
          ("wep104", 3),
          ("wpa-psk", 4),
          ("wpa", 5),
          ("wpa2", 6),
          ("wpa2-psk", 7))
    )


_TelProdNpMonInterfWlanStationSecurity_Type.__name__ = "Integer32"
_TelProdNpMonInterfWlanStationSecurity_Object = MibTableColumn
telProdNpMonInterfWlanStationSecurity = _TelProdNpMonInterfWlanStationSecurity_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 3, 1, 4),
    _TelProdNpMonInterfWlanStationSecurity_Type()
)
telProdNpMonInterfWlanStationSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanStationSecurity.setStatus("mandatory")


class _TelProdNpMonInterfWlanStationNode_Type(Integer32):
    """Custom type telProdNpMonInterfWlanStationNode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("access-point", 2),
          ("client", 3))
    )


_TelProdNpMonInterfWlanStationNode_Type.__name__ = "Integer32"
_TelProdNpMonInterfWlanStationNode_Object = MibTableColumn
telProdNpMonInterfWlanStationNode = _TelProdNpMonInterfWlanStationNode_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 3, 1, 5),
    _TelProdNpMonInterfWlanStationNode_Type()
)
telProdNpMonInterfWlanStationNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanStationNode.setStatus("mandatory")
_TelProdNpMonInterfWlanStationMSDUTx_Type = Counter32
_TelProdNpMonInterfWlanStationMSDUTx_Object = MibTableColumn
telProdNpMonInterfWlanStationMSDUTx = _TelProdNpMonInterfWlanStationMSDUTx_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 3, 1, 6),
    _TelProdNpMonInterfWlanStationMSDUTx_Type()
)
telProdNpMonInterfWlanStationMSDUTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanStationMSDUTx.setStatus("mandatory")
_TelProdNpMonInterfWlanStationMSDURx_Type = Counter32
_TelProdNpMonInterfWlanStationMSDURx_Object = MibTableColumn
telProdNpMonInterfWlanStationMSDURx = _TelProdNpMonInterfWlanStationMSDURx_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 3, 1, 7),
    _TelProdNpMonInterfWlanStationMSDURx_Type()
)
telProdNpMonInterfWlanStationMSDURx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanStationMSDURx.setStatus("mandatory")
_TelProdNpMonInterfWlanStationBytesTx_Type = Counter32
_TelProdNpMonInterfWlanStationBytesTx_Object = MibTableColumn
telProdNpMonInterfWlanStationBytesTx = _TelProdNpMonInterfWlanStationBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 3, 1, 8),
    _TelProdNpMonInterfWlanStationBytesTx_Type()
)
telProdNpMonInterfWlanStationBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanStationBytesTx.setStatus("mandatory")
_TelProdNpMonInterfWlanStationBytesRx_Type = Counter32
_TelProdNpMonInterfWlanStationBytesRx_Object = MibTableColumn
telProdNpMonInterfWlanStationBytesRx = _TelProdNpMonInterfWlanStationBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 3, 1, 9),
    _TelProdNpMonInterfWlanStationBytesRx_Type()
)
telProdNpMonInterfWlanStationBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanStationBytesRx.setStatus("mandatory")
_TelProdNpMonInterfWlanStationRate_Type = WlanRate
_TelProdNpMonInterfWlanStationRate_Object = MibTableColumn
telProdNpMonInterfWlanStationRate = _TelProdNpMonInterfWlanStationRate_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 3, 1, 10),
    _TelProdNpMonInterfWlanStationRate_Type()
)
telProdNpMonInterfWlanStationRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanStationRate.setStatus("mandatory")
_TelProdNpMonInterfWlanStationSignal_Type = WlanRSSI
_TelProdNpMonInterfWlanStationSignal_Object = MibTableColumn
telProdNpMonInterfWlanStationSignal = _TelProdNpMonInterfWlanStationSignal_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 3, 1, 11),
    _TelProdNpMonInterfWlanStationSignal_Type()
)
telProdNpMonInterfWlanStationSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanStationSignal.setStatus("mandatory")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanStationSignal.setUnits("dBm")
_TelProdNpMonInterfWlanStationNoise_Type = WlanRSSI
_TelProdNpMonInterfWlanStationNoise_Object = MibTableColumn
telProdNpMonInterfWlanStationNoise = _TelProdNpMonInterfWlanStationNoise_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 3, 1, 12),
    _TelProdNpMonInterfWlanStationNoise_Type()
)
telProdNpMonInterfWlanStationNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanStationNoise.setStatus("mandatory")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanStationNoise.setUnits("dBm")
_TelProdNpMonInterfWlanStationConnectTime_Type = Counter32
_TelProdNpMonInterfWlanStationConnectTime_Object = MibTableColumn
telProdNpMonInterfWlanStationConnectTime = _TelProdNpMonInterfWlanStationConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 3, 1, 13),
    _TelProdNpMonInterfWlanStationConnectTime_Type()
)
telProdNpMonInterfWlanStationConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanStationConnectTime.setStatus("mandatory")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanStationConnectTime.setUnits("s")
_TelProdNpMonInterfWlanACLTable_Object = MibTable
telProdNpMonInterfWlanACLTable = _TelProdNpMonInterfWlanACLTable_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 4)
)
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanACLTable.setStatus("mandatory")
_TelProdNpMonInterfWlanACLEntry_Object = MibTableRow
telProdNpMonInterfWlanACLEntry = _TelProdNpMonInterfWlanACLEntry_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 4, 1)
)
telProdNpMonInterfWlanACLEntry.setIndexNames(
    (0, "TELDAT-MON-INTERF-WLAN-MIB", "telProdNpMonInterfWlanACLIfIndex"),
    (0, "TELDAT-MON-INTERF-WLAN-MIB", "telProdNpMonInterfWlanACLAddress"),
)
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanACLEntry.setStatus("mandatory")
_TelProdNpMonInterfWlanACLIfIndex_Type = Integer32
_TelProdNpMonInterfWlanACLIfIndex_Object = MibTableColumn
telProdNpMonInterfWlanACLIfIndex = _TelProdNpMonInterfWlanACLIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 4, 1, 1),
    _TelProdNpMonInterfWlanACLIfIndex_Type()
)
telProdNpMonInterfWlanACLIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanACLIfIndex.setStatus("mandatory")
_TelProdNpMonInterfWlanACLAddress_Type = MacAddress
_TelProdNpMonInterfWlanACLAddress_Object = MibTableColumn
telProdNpMonInterfWlanACLAddress = _TelProdNpMonInterfWlanACLAddress_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 4, 1, 2),
    _TelProdNpMonInterfWlanACLAddress_Type()
)
telProdNpMonInterfWlanACLAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanACLAddress.setStatus("mandatory")
_TelProdNpMonInterfWlanScanResultsTable_Object = MibTable
telProdNpMonInterfWlanScanResultsTable = _TelProdNpMonInterfWlanScanResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 5)
)
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanScanResultsTable.setStatus("mandatory")
_TelProdNpMonInterfWlanScanResultsEntry_Object = MibTableRow
telProdNpMonInterfWlanScanResultsEntry = _TelProdNpMonInterfWlanScanResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 5, 1)
)
telProdNpMonInterfWlanScanResultsEntry.setIndexNames(
    (0, "TELDAT-MON-INTERF-WLAN-MIB", "telProdNpMonInterfWlanScanResultsIfIndex"),
    (0, "TELDAT-MON-INTERF-WLAN-MIB", "telProdNpMonInterfWlanScanResultsIndex"),
)
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanScanResultsEntry.setStatus("mandatory")
_TelProdNpMonInterfWlanScanResultsIfIndex_Type = Integer32
_TelProdNpMonInterfWlanScanResultsIfIndex_Object = MibTableColumn
telProdNpMonInterfWlanScanResultsIfIndex = _TelProdNpMonInterfWlanScanResultsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 5, 1, 1),
    _TelProdNpMonInterfWlanScanResultsIfIndex_Type()
)
telProdNpMonInterfWlanScanResultsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanScanResultsIfIndex.setStatus("mandatory")
_TelProdNpMonInterfWlanScanResultsIndex_Type = Integer32
_TelProdNpMonInterfWlanScanResultsIndex_Object = MibTableColumn
telProdNpMonInterfWlanScanResultsIndex = _TelProdNpMonInterfWlanScanResultsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 5, 1, 2),
    _TelProdNpMonInterfWlanScanResultsIndex_Type()
)
telProdNpMonInterfWlanScanResultsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanScanResultsIndex.setStatus("mandatory")
_TelProdNpMonInterfWlanScanResultsBSSID_Type = MacAddress
_TelProdNpMonInterfWlanScanResultsBSSID_Object = MibTableColumn
telProdNpMonInterfWlanScanResultsBSSID = _TelProdNpMonInterfWlanScanResultsBSSID_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 5, 1, 3),
    _TelProdNpMonInterfWlanScanResultsBSSID_Type()
)
telProdNpMonInterfWlanScanResultsBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanScanResultsBSSID.setStatus("mandatory")
_TelProdNpMonInterfWlanScanResultsSSID_Type = DisplayString
_TelProdNpMonInterfWlanScanResultsSSID_Object = MibTableColumn
telProdNpMonInterfWlanScanResultsSSID = _TelProdNpMonInterfWlanScanResultsSSID_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 5, 1, 4),
    _TelProdNpMonInterfWlanScanResultsSSID_Type()
)
telProdNpMonInterfWlanScanResultsSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanScanResultsSSID.setStatus("mandatory")


class _TelProdNpMonInterfWlanScanResultsChannel_Type(Integer32):
    """Custom type telProdNpMonInterfWlanScanResultsChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_TelProdNpMonInterfWlanScanResultsChannel_Type.__name__ = "Integer32"
_TelProdNpMonInterfWlanScanResultsChannel_Object = MibTableColumn
telProdNpMonInterfWlanScanResultsChannel = _TelProdNpMonInterfWlanScanResultsChannel_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 5, 1, 5),
    _TelProdNpMonInterfWlanScanResultsChannel_Type()
)
telProdNpMonInterfWlanScanResultsChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanScanResultsChannel.setStatus("mandatory")
_TelProdNpMonInterfWlanScanResultsSignal_Type = WlanRSSI
_TelProdNpMonInterfWlanScanResultsSignal_Object = MibTableColumn
telProdNpMonInterfWlanScanResultsSignal = _TelProdNpMonInterfWlanScanResultsSignal_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 5, 1, 6),
    _TelProdNpMonInterfWlanScanResultsSignal_Type()
)
telProdNpMonInterfWlanScanResultsSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanScanResultsSignal.setStatus("mandatory")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanScanResultsSignal.setUnits("dBm")
_TelProdNpMonInterfWlanScanResultsNoise_Type = WlanRSSI
_TelProdNpMonInterfWlanScanResultsNoise_Object = MibTableColumn
telProdNpMonInterfWlanScanResultsNoise = _TelProdNpMonInterfWlanScanResultsNoise_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 5, 1, 7),
    _TelProdNpMonInterfWlanScanResultsNoise_Type()
)
telProdNpMonInterfWlanScanResultsNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanScanResultsNoise.setStatus("mandatory")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanScanResultsNoise.setUnits("dBm")


class _TelProdNpMonInterfWlanScanResultsBeaconPeriod_Type(Integer32):
    """Custom type telProdNpMonInterfWlanScanResultsBeaconPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TelProdNpMonInterfWlanScanResultsBeaconPeriod_Type.__name__ = "Integer32"
_TelProdNpMonInterfWlanScanResultsBeaconPeriod_Object = MibTableColumn
telProdNpMonInterfWlanScanResultsBeaconPeriod = _TelProdNpMonInterfWlanScanResultsBeaconPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 5, 1, 8),
    _TelProdNpMonInterfWlanScanResultsBeaconPeriod_Type()
)
telProdNpMonInterfWlanScanResultsBeaconPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanScanResultsBeaconPeriod.setStatus("mandatory")
_TelProdNpMonInterfWlanScanResultsRates_Type = DisplayString
_TelProdNpMonInterfWlanScanResultsRates_Object = MibTableColumn
telProdNpMonInterfWlanScanResultsRates = _TelProdNpMonInterfWlanScanResultsRates_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 5, 1, 9),
    _TelProdNpMonInterfWlanScanResultsRates_Type()
)
telProdNpMonInterfWlanScanResultsRates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanScanResultsRates.setStatus("mandatory")
_TelProdNpMonInterfWlanScanResultsBasicRates_Type = DisplayString
_TelProdNpMonInterfWlanScanResultsBasicRates_Object = MibTableColumn
telProdNpMonInterfWlanScanResultsBasicRates = _TelProdNpMonInterfWlanScanResultsBasicRates_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 5, 1, 10),
    _TelProdNpMonInterfWlanScanResultsBasicRates_Type()
)
telProdNpMonInterfWlanScanResultsBasicRates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanScanResultsBasicRates.setStatus("mandatory")
_TelProdNpMonInterfWlanScanResultsExtendedRates_Type = DisplayString
_TelProdNpMonInterfWlanScanResultsExtendedRates_Object = MibTableColumn
telProdNpMonInterfWlanScanResultsExtendedRates = _TelProdNpMonInterfWlanScanResultsExtendedRates_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 5, 1, 11),
    _TelProdNpMonInterfWlanScanResultsExtendedRates_Type()
)
telProdNpMonInterfWlanScanResultsExtendedRates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanScanResultsExtendedRates.setStatus("mandatory")
_TelProdNpMonInterfWlanWMMTable_Object = MibTable
telProdNpMonInterfWlanWMMTable = _TelProdNpMonInterfWlanWMMTable_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 6)
)
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanWMMTable.setStatus("mandatory")
_TelProdNpMonInterfWlanWMMEntry_Object = MibTableRow
telProdNpMonInterfWlanWMMEntry = _TelProdNpMonInterfWlanWMMEntry_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 6, 1)
)
telProdNpMonInterfWlanWMMEntry.setIndexNames(
    (0, "TELDAT-MON-INTERF-WLAN-MIB", "telProdNpMonInterfWlanWMMAccCat"),
    (0, "TELDAT-MON-INTERF-WLAN-MIB", "telProdNpMonInterfWlanWMMwlanIf"),
    (0, "TELDAT-MON-INTERF-WLAN-MIB", "telProdNpMonInterfWlanWMMType"),
)
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanWMMEntry.setStatus("mandatory")
_TelProdNpMonInterfWlanWMMwlanIf_Type = Integer32
_TelProdNpMonInterfWlanWMMwlanIf_Object = MibTableColumn
telProdNpMonInterfWlanWMMwlanIf = _TelProdNpMonInterfWlanWMMwlanIf_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 6, 1, 1),
    _TelProdNpMonInterfWlanWMMwlanIf_Type()
)
telProdNpMonInterfWlanWMMwlanIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanWMMwlanIf.setStatus("mandatory")


class _TelProdNpMonInterfWlanWMMAccCat_Type(Integer32):
    """Custom type telProdNpMonInterfWlanWMMAccCat based on Integer32"""
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
        *(("besteffort", 1),
          ("background", 2),
          ("video", 3),
          ("voice", 4))
    )


_TelProdNpMonInterfWlanWMMAccCat_Type.__name__ = "Integer32"
_TelProdNpMonInterfWlanWMMAccCat_Object = MibTableColumn
telProdNpMonInterfWlanWMMAccCat = _TelProdNpMonInterfWlanWMMAccCat_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 6, 1, 2),
    _TelProdNpMonInterfWlanWMMAccCat_Type()
)
telProdNpMonInterfWlanWMMAccCat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanWMMAccCat.setStatus("mandatory")


class _TelProdNpMonInterfWlanWMMType_Type(Integer32):
    """Custom type telProdNpMonInterfWlanWMMType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("access-point", 1),
          ("station", 2))
    )


_TelProdNpMonInterfWlanWMMType_Type.__name__ = "Integer32"
_TelProdNpMonInterfWlanWMMType_Object = MibTableColumn
telProdNpMonInterfWlanWMMType = _TelProdNpMonInterfWlanWMMType_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 6, 1, 3),
    _TelProdNpMonInterfWlanWMMType_Type()
)
telProdNpMonInterfWlanWMMType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanWMMType.setStatus("mandatory")
_TelProdNpMonInterfWlanWMMaCWmin_Type = Integer32
_TelProdNpMonInterfWlanWMMaCWmin_Object = MibTableColumn
telProdNpMonInterfWlanWMMaCWmin = _TelProdNpMonInterfWlanWMMaCWmin_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 6, 1, 4),
    _TelProdNpMonInterfWlanWMMaCWmin_Type()
)
telProdNpMonInterfWlanWMMaCWmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanWMMaCWmin.setStatus("mandatory")
_TelProdNpMonInterfWlanWMMaCWmax_Type = Integer32
_TelProdNpMonInterfWlanWMMaCWmax_Object = MibTableColumn
telProdNpMonInterfWlanWMMaCWmax = _TelProdNpMonInterfWlanWMMaCWmax_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 6, 1, 5),
    _TelProdNpMonInterfWlanWMMaCWmax_Type()
)
telProdNpMonInterfWlanWMMaCWmax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanWMMaCWmax.setStatus("mandatory")


class _TelProdNpMonInterfWlanWMMAifsn_Type(Integer32):
    """Custom type telProdNpMonInterfWlanWMMAifsn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_TelProdNpMonInterfWlanWMMAifsn_Type.__name__ = "Integer32"
_TelProdNpMonInterfWlanWMMAifsn_Object = MibTableColumn
telProdNpMonInterfWlanWMMAifsn = _TelProdNpMonInterfWlanWMMAifsn_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 6, 1, 6),
    _TelProdNpMonInterfWlanWMMAifsn_Type()
)
telProdNpMonInterfWlanWMMAifsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanWMMAifsn.setStatus("mandatory")


class _TelProdNpMonInterfWlanWMMTxopLimit_Type(Integer32):
    """Custom type telProdNpMonInterfWlanWMMTxopLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_TelProdNpMonInterfWlanWMMTxopLimit_Type.__name__ = "Integer32"
_TelProdNpMonInterfWlanWMMTxopLimit_Object = MibTableColumn
telProdNpMonInterfWlanWMMTxopLimit = _TelProdNpMonInterfWlanWMMTxopLimit_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 6, 1, 7),
    _TelProdNpMonInterfWlanWMMTxopLimit_Type()
)
telProdNpMonInterfWlanWMMTxopLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanWMMTxopLimit.setStatus("mandatory")


class _TelProdNpMonInterfWlanWMMAckPolicy_Type(Integer32):
    """Custom type telProdNpMonInterfWlanWMMAckPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ack", 1),
          ("noAck", 2))
    )


_TelProdNpMonInterfWlanWMMAckPolicy_Type.__name__ = "Integer32"
_TelProdNpMonInterfWlanWMMAckPolicy_Object = MibTableColumn
telProdNpMonInterfWlanWMMAckPolicy = _TelProdNpMonInterfWlanWMMAckPolicy_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 6, 1, 8),
    _TelProdNpMonInterfWlanWMMAckPolicy_Type()
)
telProdNpMonInterfWlanWMMAckPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanWMMAckPolicy.setStatus("mandatory")


class _TelProdNpMonInterfWlanWMMACM_Type(Integer32):
    """Custom type telProdNpMonInterfWlanWMMACM based on Integer32"""
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


_TelProdNpMonInterfWlanWMMACM_Type.__name__ = "Integer32"
_TelProdNpMonInterfWlanWMMACM_Object = MibTableColumn
telProdNpMonInterfWlanWMMACM = _TelProdNpMonInterfWlanWMMACM_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 6, 1, 9),
    _TelProdNpMonInterfWlanWMMACM_Type()
)
telProdNpMonInterfWlanWMMACM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanWMMACM.setStatus("mandatory")
_TelProdNpMonInterfWlanClientTable_Object = MibTable
telProdNpMonInterfWlanClientTable = _TelProdNpMonInterfWlanClientTable_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 7)
)
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanClientTable.setStatus("mandatory")
_TelProdNpMonInterfwlanClientEntry_Object = MibTableRow
telProdNpMonInterfwlanClientEntry = _TelProdNpMonInterfwlanClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 7, 1)
)
telProdNpMonInterfwlanClientEntry.setIndexNames(
    (0, "TELDAT-MON-INTERF-WLAN-MIB", "telProdNpMonInterfWlanClientIfIndex"),
    (0, "TELDAT-MON-INTERF-WLAN-MIB", "telProdNpMonInterfWlanClientSSID"),
)
if mibBuilder.loadTexts:
    telProdNpMonInterfwlanClientEntry.setStatus("mandatory")


class _TelProdNpMonInterfWlanClientIfIndex_Type(Integer32):
    """Custom type telProdNpMonInterfWlanClientIfIndex based on Integer32"""
    defaultValue = 0


_TelProdNpMonInterfWlanClientIfIndex_Type.__name__ = "Integer32"
_TelProdNpMonInterfWlanClientIfIndex_Object = MibTableColumn
telProdNpMonInterfWlanClientIfIndex = _TelProdNpMonInterfWlanClientIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 7, 1, 1),
    _TelProdNpMonInterfWlanClientIfIndex_Type()
)
telProdNpMonInterfWlanClientIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanClientIfIndex.setStatus("mandatory")
_TelProdNpMonInterfWlanClientSSID_Type = DisplayString
_TelProdNpMonInterfWlanClientSSID_Object = MibTableColumn
telProdNpMonInterfWlanClientSSID = _TelProdNpMonInterfWlanClientSSID_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 7, 1, 2),
    _TelProdNpMonInterfWlanClientSSID_Type()
)
telProdNpMonInterfWlanClientSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanClientSSID.setStatus("mandatory")


class _TelProdNpMonInterfWlanClientPriority_Type(Integer32):
    """Custom type telProdNpMonInterfWlanClientPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("enable", 2))
    )


_TelProdNpMonInterfWlanClientPriority_Type.__name__ = "Integer32"
_TelProdNpMonInterfWlanClientPriority_Object = MibTableColumn
telProdNpMonInterfWlanClientPriority = _TelProdNpMonInterfWlanClientPriority_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 7, 1, 3),
    _TelProdNpMonInterfWlanClientPriority_Type()
)
telProdNpMonInterfWlanClientPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanClientPriority.setStatus("mandatory")


class _TelProdNpMonInterfWlanClientPrivInvoked_Type(Integer32):
    """Custom type telProdNpMonInterfWlanClientPrivInvoked based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("enable", 2))
    )


_TelProdNpMonInterfWlanClientPrivInvoked_Type.__name__ = "Integer32"
_TelProdNpMonInterfWlanClientPrivInvoked_Object = MibTableColumn
telProdNpMonInterfWlanClientPrivInvoked = _TelProdNpMonInterfWlanClientPrivInvoked_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 7, 1, 4),
    _TelProdNpMonInterfWlanClientPrivInvoked_Type()
)
telProdNpMonInterfWlanClientPrivInvoked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanClientPrivInvoked.setStatus("mandatory")


class _TelProdNpMonInterfWlanClientRsn_Type(Integer32):
    """Custom type telProdNpMonInterfWlanClientRsn based on Integer32"""
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
        *(("wpa", 0),
          ("wpa2", 1),
          ("none", 2),
          ("wpa-wpa2", 3))
    )


_TelProdNpMonInterfWlanClientRsn_Type.__name__ = "Integer32"
_TelProdNpMonInterfWlanClientRsn_Object = MibTableColumn
telProdNpMonInterfWlanClientRsn = _TelProdNpMonInterfWlanClientRsn_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 7, 1, 5),
    _TelProdNpMonInterfWlanClientRsn_Type()
)
telProdNpMonInterfWlanClientRsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanClientRsn.setStatus("mandatory")


class _TelProdNpMonInterfWlanClientAkm_Type(Integer32):
    """Custom type telProdNpMonInterfWlanClientAkm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dot1x", 0),
          ("psk", 1))
    )


_TelProdNpMonInterfWlanClientAkm_Type.__name__ = "Integer32"
_TelProdNpMonInterfWlanClientAkm_Object = MibTableColumn
telProdNpMonInterfWlanClientAkm = _TelProdNpMonInterfWlanClientAkm_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 7, 1, 6),
    _TelProdNpMonInterfWlanClientAkm_Type()
)
telProdNpMonInterfWlanClientAkm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanClientAkm.setStatus("mandatory")


class _TelProdNpMonInterfWlanClientCipher_Type(Integer32):
    """Custom type telProdNpMonInterfWlanClientCipher based on Integer32"""
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
          ("auto", 1),
          ("wep", 2),
          ("tkip", 3),
          ("aes-ccm", 4))
    )


_TelProdNpMonInterfWlanClientCipher_Type.__name__ = "Integer32"
_TelProdNpMonInterfWlanClientCipher_Object = MibTableColumn
telProdNpMonInterfWlanClientCipher = _TelProdNpMonInterfWlanClientCipher_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 7, 1, 7),
    _TelProdNpMonInterfWlanClientCipher_Type()
)
telProdNpMonInterfWlanClientCipher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanClientCipher.setStatus("mandatory")


class _TelProdNpMonInterfWlanClientDefaultKey_Type(Integer32):
    """Custom type telProdNpMonInterfWlanClientDefaultKey based on Integer32"""
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
        *(("key1", 1),
          ("key2", 2),
          ("key3", 3),
          ("key4", 4))
    )


_TelProdNpMonInterfWlanClientDefaultKey_Type.__name__ = "Integer32"
_TelProdNpMonInterfWlanClientDefaultKey_Object = MibTableColumn
telProdNpMonInterfWlanClientDefaultKey = _TelProdNpMonInterfWlanClientDefaultKey_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 7, 1, 8),
    _TelProdNpMonInterfWlanClientDefaultKey_Type()
)
telProdNpMonInterfWlanClientDefaultKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanClientDefaultKey.setStatus("mandatory")


class _TelProdNpMonInterfWlanClientKey1_Type(OctetString):
    """Custom type telProdNpMonInterfWlanClientKey1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 33),
    )


_TelProdNpMonInterfWlanClientKey1_Type.__name__ = "OctetString"
_TelProdNpMonInterfWlanClientKey1_Object = MibTableColumn
telProdNpMonInterfWlanClientKey1 = _TelProdNpMonInterfWlanClientKey1_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 7, 1, 9),
    _TelProdNpMonInterfWlanClientKey1_Type()
)
telProdNpMonInterfWlanClientKey1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanClientKey1.setStatus("mandatory")


class _TelProdNpMonInterfWlanClientKey2_Type(OctetString):
    """Custom type telProdNpMonInterfWlanClientKey2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 33),
    )


_TelProdNpMonInterfWlanClientKey2_Type.__name__ = "OctetString"
_TelProdNpMonInterfWlanClientKey2_Object = MibTableColumn
telProdNpMonInterfWlanClientKey2 = _TelProdNpMonInterfWlanClientKey2_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 7, 1, 10),
    _TelProdNpMonInterfWlanClientKey2_Type()
)
telProdNpMonInterfWlanClientKey2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanClientKey2.setStatus("mandatory")


class _TelProdNpMonInterfWlanClientKey3_Type(OctetString):
    """Custom type telProdNpMonInterfWlanClientKey3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 33),
    )


_TelProdNpMonInterfWlanClientKey3_Type.__name__ = "OctetString"
_TelProdNpMonInterfWlanClientKey3_Object = MibTableColumn
telProdNpMonInterfWlanClientKey3 = _TelProdNpMonInterfWlanClientKey3_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 7, 1, 11),
    _TelProdNpMonInterfWlanClientKey3_Type()
)
telProdNpMonInterfWlanClientKey3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanClientKey3.setStatus("mandatory")


class _TelProdNpMonInterfWlanClientKey4_Type(OctetString):
    """Custom type telProdNpMonInterfWlanClientKey4 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 33),
    )


_TelProdNpMonInterfWlanClientKey4_Type.__name__ = "OctetString"
_TelProdNpMonInterfWlanClientKey4_Object = MibTableColumn
telProdNpMonInterfWlanClientKey4 = _TelProdNpMonInterfWlanClientKey4_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 7, 1, 12),
    _TelProdNpMonInterfWlanClientKey4_Type()
)
telProdNpMonInterfWlanClientKey4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfWlanClientKey4.setStatus("mandatory")


class _TelProdNpMonInterfwlanClientPassPhrase_Type(OctetString):
    """Custom type telProdNpMonInterfwlanClientPassPhrase based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TelProdNpMonInterfwlanClientPassPhrase_Type.__name__ = "OctetString"
_TelProdNpMonInterfwlanClientPassPhrase_Object = MibTableColumn
telProdNpMonInterfwlanClientPassPhrase = _TelProdNpMonInterfwlanClientPassPhrase_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 24, 7, 1, 13),
    _TelProdNpMonInterfwlanClientPassPhrase_Type()
)
telProdNpMonInterfwlanClientPassPhrase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfwlanClientPassPhrase.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TELDAT-MON-INTERF-WLAN-MIB",
    **{"WlanRSSI": WlanRSSI,
       "WlanRate": WlanRate,
       "telProdNpMonInterfWlan": telProdNpMonInterfWlan,
       "telProdNpMonInterfWlanRadioTable": telProdNpMonInterfWlanRadioTable,
       "telProdNpMonInterfWlanRadioEntry": telProdNpMonInterfWlanRadioEntry,
       "telProdNpMonInterfWlanRadioIfIndex": telProdNpMonInterfWlanRadioIfIndex,
       "telProdNpMonInterfWlanRadioIfMode": telProdNpMonInterfWlanRadioIfMode,
       "telProdNpMonInterfWlanRadioIfSpeed": telProdNpMonInterfWlanRadioIfSpeed,
       "telProdNpMonInterfWlanRadioIfChannel": telProdNpMonInterfWlanRadioIfChannel,
       "telProdNpMonInterfWlanRadioIfRtsThreshold": telProdNpMonInterfWlanRadioIfRtsThreshold,
       "telProdNpMonInterfWlanRadioIfTxPower": telProdNpMonInterfWlanRadioIfTxPower,
       "telProdNpMonInterfWlanRadioIfBand": telProdNpMonInterfWlanRadioIfBand,
       "telProdNpMonInterfWlanRadioIfCountry": telProdNpMonInterfWlanRadioIfCountry,
       "telProdNpMonInterfWlanRadioIfAddress": telProdNpMonInterfWlanRadioIfAddress,
       "telProdNpMonInterfWlanRadioIfRealChannel": telProdNpMonInterfWlanRadioIfRealChannel,
       "telProdNpMonInterfWlanRadioIfFragmentThreshold": telProdNpMonInterfWlanRadioIfFragmentThreshold,
       "telProdNpMonInterfWlanBSSTable": telProdNpMonInterfWlanBSSTable,
       "telProdNpMonInterfWlanBSSEntry": telProdNpMonInterfWlanBSSEntry,
       "telProdNpMonInterfWlanBSSIfIndex": telProdNpMonInterfWlanBSSIfIndex,
       "telProdNpMonInterfWlanBSSId": telProdNpMonInterfWlanBSSId,
       "telProdNpMonInterfWlanBSSPrivInvoked": telProdNpMonInterfWlanBSSPrivInvoked,
       "telProdNpMonInterfWlanBSSRsn": telProdNpMonInterfWlanBSSRsn,
       "telProdNpMonInterfWlanBSSAkm": telProdNpMonInterfWlanBSSAkm,
       "telProdNpMonInterfWlanBSSCipher": telProdNpMonInterfWlanBSSCipher,
       "telProdNpMonInterfWlanBSSDefaultKey": telProdNpMonInterfWlanBSSDefaultKey,
       "telProdNpMonInterfWlanBSSKey1": telProdNpMonInterfWlanBSSKey1,
       "telProdNpMonInterfWlanBSSKey2": telProdNpMonInterfWlanBSSKey2,
       "telProdNpMonInterfWlanBSSKey3": telProdNpMonInterfWlanBSSKey3,
       "telProdNpMonInterfWlanBSSKey4": telProdNpMonInterfWlanBSSKey4,
       "telProdNpMonInterfWlanBSSMaxAsoc": telProdNpMonInterfWlanBSSMaxAsoc,
       "telProdNpMonInterfWlanBSSAcl": telProdNpMonInterfWlanBSSAcl,
       "telProdNpMonInterfWlanBSSClientIsolation": telProdNpMonInterfWlanBSSClientIsolation,
       "telProdNpMonInterfWlanBSSHidden": telProdNpMonInterfWlanBSSHidden,
       "telProdNpMonInterfWlanBSSBssId": telProdNpMonInterfWlanBSSBssId,
       "telProdNpMonInterfWlanBSSBeaconPeriod": telProdNpMonInterfWlanBSSBeaconPeriod,
       "telProdNpMonInterfWlanBSSDTIMPeriod": telProdNpMonInterfWlanBSSDTIMPeriod,
       "telProdNpMonInterfWlanBSSMSDUTx": telProdNpMonInterfWlanBSSMSDUTx,
       "telProdNpMonInterfWlanBSSMSDURx": telProdNpMonInterfWlanBSSMSDURx,
       "telProdNpMonInterfWlanBSSBytesTx": telProdNpMonInterfWlanBSSBytesTx,
       "telProdNpMonInterfWlanBSSBytesRx": telProdNpMonInterfWlanBSSBytesRx,
       "telProdNpMonInterfWlanBSSCurrent": telProdNpMonInterfWlanBSSCurrent,
       "telProdNpMonInterfWlanBSSOpMode": telProdNpMonInterfWlanBSSOpMode,
       "telProdNpMonInterfwlanBSSPassPhrase": telProdNpMonInterfwlanBSSPassPhrase,
       "telProdNpMonInterfWlanStationTable": telProdNpMonInterfWlanStationTable,
       "telProdNpMonInterfWlanStationEntry": telProdNpMonInterfWlanStationEntry,
       "telProdNpMonInterfWlanStationIfIndex": telProdNpMonInterfWlanStationIfIndex,
       "telProdNpMonInterfWlanStationAddress": telProdNpMonInterfWlanStationAddress,
       "telProdNpMonInterfWlanStationState": telProdNpMonInterfWlanStationState,
       "telProdNpMonInterfWlanStationSecurity": telProdNpMonInterfWlanStationSecurity,
       "telProdNpMonInterfWlanStationNode": telProdNpMonInterfWlanStationNode,
       "telProdNpMonInterfWlanStationMSDUTx": telProdNpMonInterfWlanStationMSDUTx,
       "telProdNpMonInterfWlanStationMSDURx": telProdNpMonInterfWlanStationMSDURx,
       "telProdNpMonInterfWlanStationBytesTx": telProdNpMonInterfWlanStationBytesTx,
       "telProdNpMonInterfWlanStationBytesRx": telProdNpMonInterfWlanStationBytesRx,
       "telProdNpMonInterfWlanStationRate": telProdNpMonInterfWlanStationRate,
       "telProdNpMonInterfWlanStationSignal": telProdNpMonInterfWlanStationSignal,
       "telProdNpMonInterfWlanStationNoise": telProdNpMonInterfWlanStationNoise,
       "telProdNpMonInterfWlanStationConnectTime": telProdNpMonInterfWlanStationConnectTime,
       "telProdNpMonInterfWlanACLTable": telProdNpMonInterfWlanACLTable,
       "telProdNpMonInterfWlanACLEntry": telProdNpMonInterfWlanACLEntry,
       "telProdNpMonInterfWlanACLIfIndex": telProdNpMonInterfWlanACLIfIndex,
       "telProdNpMonInterfWlanACLAddress": telProdNpMonInterfWlanACLAddress,
       "telProdNpMonInterfWlanScanResultsTable": telProdNpMonInterfWlanScanResultsTable,
       "telProdNpMonInterfWlanScanResultsEntry": telProdNpMonInterfWlanScanResultsEntry,
       "telProdNpMonInterfWlanScanResultsIfIndex": telProdNpMonInterfWlanScanResultsIfIndex,
       "telProdNpMonInterfWlanScanResultsIndex": telProdNpMonInterfWlanScanResultsIndex,
       "telProdNpMonInterfWlanScanResultsBSSID": telProdNpMonInterfWlanScanResultsBSSID,
       "telProdNpMonInterfWlanScanResultsSSID": telProdNpMonInterfWlanScanResultsSSID,
       "telProdNpMonInterfWlanScanResultsChannel": telProdNpMonInterfWlanScanResultsChannel,
       "telProdNpMonInterfWlanScanResultsSignal": telProdNpMonInterfWlanScanResultsSignal,
       "telProdNpMonInterfWlanScanResultsNoise": telProdNpMonInterfWlanScanResultsNoise,
       "telProdNpMonInterfWlanScanResultsBeaconPeriod": telProdNpMonInterfWlanScanResultsBeaconPeriod,
       "telProdNpMonInterfWlanScanResultsRates": telProdNpMonInterfWlanScanResultsRates,
       "telProdNpMonInterfWlanScanResultsBasicRates": telProdNpMonInterfWlanScanResultsBasicRates,
       "telProdNpMonInterfWlanScanResultsExtendedRates": telProdNpMonInterfWlanScanResultsExtendedRates,
       "telProdNpMonInterfWlanWMMTable": telProdNpMonInterfWlanWMMTable,
       "telProdNpMonInterfWlanWMMEntry": telProdNpMonInterfWlanWMMEntry,
       "telProdNpMonInterfWlanWMMwlanIf": telProdNpMonInterfWlanWMMwlanIf,
       "telProdNpMonInterfWlanWMMAccCat": telProdNpMonInterfWlanWMMAccCat,
       "telProdNpMonInterfWlanWMMType": telProdNpMonInterfWlanWMMType,
       "telProdNpMonInterfWlanWMMaCWmin": telProdNpMonInterfWlanWMMaCWmin,
       "telProdNpMonInterfWlanWMMaCWmax": telProdNpMonInterfWlanWMMaCWmax,
       "telProdNpMonInterfWlanWMMAifsn": telProdNpMonInterfWlanWMMAifsn,
       "telProdNpMonInterfWlanWMMTxopLimit": telProdNpMonInterfWlanWMMTxopLimit,
       "telProdNpMonInterfWlanWMMAckPolicy": telProdNpMonInterfWlanWMMAckPolicy,
       "telProdNpMonInterfWlanWMMACM": telProdNpMonInterfWlanWMMACM,
       "telProdNpMonInterfWlanClientTable": telProdNpMonInterfWlanClientTable,
       "telProdNpMonInterfwlanClientEntry": telProdNpMonInterfwlanClientEntry,
       "telProdNpMonInterfWlanClientIfIndex": telProdNpMonInterfWlanClientIfIndex,
       "telProdNpMonInterfWlanClientSSID": telProdNpMonInterfWlanClientSSID,
       "telProdNpMonInterfWlanClientPriority": telProdNpMonInterfWlanClientPriority,
       "telProdNpMonInterfWlanClientPrivInvoked": telProdNpMonInterfWlanClientPrivInvoked,
       "telProdNpMonInterfWlanClientRsn": telProdNpMonInterfWlanClientRsn,
       "telProdNpMonInterfWlanClientAkm": telProdNpMonInterfWlanClientAkm,
       "telProdNpMonInterfWlanClientCipher": telProdNpMonInterfWlanClientCipher,
       "telProdNpMonInterfWlanClientDefaultKey": telProdNpMonInterfWlanClientDefaultKey,
       "telProdNpMonInterfWlanClientKey1": telProdNpMonInterfWlanClientKey1,
       "telProdNpMonInterfWlanClientKey2": telProdNpMonInterfWlanClientKey2,
       "telProdNpMonInterfWlanClientKey3": telProdNpMonInterfWlanClientKey3,
       "telProdNpMonInterfWlanClientKey4": telProdNpMonInterfWlanClientKey4,
       "telProdNpMonInterfwlanClientPassPhrase": telProdNpMonInterfwlanClientPassPhrase}
)
