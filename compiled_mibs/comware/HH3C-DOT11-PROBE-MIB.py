# SNMP MIB module (HH3C-DOT11-PROBE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-DOT11-PROBE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:31:06 2025
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

(hh3cDot11,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cDot11")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hh3cDot11PROBE = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17)
)
if mibBuilder.loadTexts:
    hh3cDot11PROBE.setRevisions(
        ("2016-03-28 09:51",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Hh3cDot11PROBEEnabledStatus(TextualConvention, Integer32):
    status = "current"
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



class Hh3cDot11PROBERadioType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64,
              128)
        )
    )
    namedValues = NamedValues(
        *(("dot11a", 1),
          ("dot11b", 2),
          ("dot11g", 4),
          ("dot11n", 8),
          ("dot11gn", 16),
          ("dot11an", 32),
          ("dot11ac", 64),
          ("dot11gac", 128))
    )



class Hh3cDot11PROBEDevStatus(TextualConvention, Integer32):
    status = "current"
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



class Hh3cDot11PROBEChannel(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 224),
    )



class Hh3cDot11PROBEEncryptMethod(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class Hh3cDot11PROBEAuthMethod(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class Hh3cDot11PROBESecurityType(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )



# MIB Managed Objects in the order of their OIDs

_Hh3cDot11PROBEConfigGroup_ObjectIdentity = ObjectIdentity
hh3cDot11PROBEConfigGroup = _Hh3cDot11PROBEConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 1)
)
_Hh3cDot11PROBERadioCfgTable_Object = MibTable
hh3cDot11PROBERadioCfgTable = _Hh3cDot11PROBERadioCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cDot11PROBERadioCfgTable.setStatus("current")
_Hh3cDot11PROBERadioCfgEntry_Object = MibTableRow
hh3cDot11PROBERadioCfgEntry = _Hh3cDot11PROBERadioCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 1, 1, 1)
)
hh3cDot11PROBERadioCfgEntry.setIndexNames(
    (0, "HH3C-DOT11-PROBE-MIB", "hh3cDot11PROBERadioCfgApName"),
    (0, "HH3C-DOT11-PROBE-MIB", "hh3cDot11PROBERadioCfgRadioId"),
)
if mibBuilder.loadTexts:
    hh3cDot11PROBERadioCfgEntry.setStatus("current")


class _Hh3cDot11PROBERadioCfgApName_Type(OctetString):
    """Custom type hh3cDot11PROBERadioCfgApName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_Hh3cDot11PROBERadioCfgApName_Type.__name__ = "OctetString"
_Hh3cDot11PROBERadioCfgApName_Object = MibTableColumn
hh3cDot11PROBERadioCfgApName = _Hh3cDot11PROBERadioCfgApName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 1, 1, 1, 1),
    _Hh3cDot11PROBERadioCfgApName_Type()
)
hh3cDot11PROBERadioCfgApName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11PROBERadioCfgApName.setStatus("current")


class _Hh3cDot11PROBERadioCfgRadioId_Type(Integer32):
    """Custom type hh3cDot11PROBERadioCfgRadioId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Hh3cDot11PROBERadioCfgRadioId_Type.__name__ = "Integer32"
_Hh3cDot11PROBERadioCfgRadioId_Object = MibTableColumn
hh3cDot11PROBERadioCfgRadioId = _Hh3cDot11PROBERadioCfgRadioId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 1, 1, 1, 2),
    _Hh3cDot11PROBERadioCfgRadioId_Type()
)
hh3cDot11PROBERadioCfgRadioId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11PROBERadioCfgRadioId.setStatus("current")
_Hh3cDot11PROBERadioCfgStatus_Type = Hh3cDot11PROBEEnabledStatus
_Hh3cDot11PROBERadioCfgStatus_Object = MibTableColumn
hh3cDot11PROBERadioCfgStatus = _Hh3cDot11PROBERadioCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 1, 1, 1, 3),
    _Hh3cDot11PROBERadioCfgStatus_Type()
)
hh3cDot11PROBERadioCfgStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11PROBERadioCfgStatus.setStatus("current")
_Hh3cDot11PROBEDataGroup_ObjectIdentity = ObjectIdentity
hh3cDot11PROBEDataGroup = _Hh3cDot11PROBEDataGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2)
)
_Hh3cDot11PROBEClientTable_Object = MibTable
hh3cDot11PROBEClientTable = _Hh3cDot11PROBEClientTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cDot11PROBEClientTable.setStatus("current")
_Hh3cDot11PROBEClientEntry_Object = MibTableRow
hh3cDot11PROBEClientEntry = _Hh3cDot11PROBEClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 1, 1)
)
hh3cDot11PROBEClientEntry.setIndexNames(
    (0, "HH3C-DOT11-PROBE-MIB", "hh3cDot11PROBEClientMac"),
)
if mibBuilder.loadTexts:
    hh3cDot11PROBEClientEntry.setStatus("current")
_Hh3cDot11PROBEClientMac_Type = MacAddress
_Hh3cDot11PROBEClientMac_Object = MibTableColumn
hh3cDot11PROBEClientMac = _Hh3cDot11PROBEClientMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 1, 1, 1),
    _Hh3cDot11PROBEClientMac_Type()
)
hh3cDot11PROBEClientMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11PROBEClientMac.setStatus("current")
_Hh3cDot11PROBEClientBSSID_Type = MacAddress
_Hh3cDot11PROBEClientBSSID_Object = MibTableColumn
hh3cDot11PROBEClientBSSID = _Hh3cDot11PROBEClientBSSID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 1, 1, 2),
    _Hh3cDot11PROBEClientBSSID_Type()
)
hh3cDot11PROBEClientBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11PROBEClientBSSID.setStatus("current")


class _Hh3cDot11PROBEClientSSID_Type(OctetString):
    """Custom type hh3cDot11PROBEClientSSID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cDot11PROBEClientSSID_Type.__name__ = "OctetString"
_Hh3cDot11PROBEClientSSID_Object = MibTableColumn
hh3cDot11PROBEClientSSID = _Hh3cDot11PROBEClientSSID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 1, 1, 3),
    _Hh3cDot11PROBEClientSSID_Type()
)
hh3cDot11PROBEClientSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11PROBEClientSSID.setStatus("current")
_Hh3cDot11PROBEClientIsDiss_Type = TruthValue
_Hh3cDot11PROBEClientIsDiss_Object = MibTableColumn
hh3cDot11PROBEClientIsDiss = _Hh3cDot11PROBEClientIsDiss_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 1, 1, 4),
    _Hh3cDot11PROBEClientIsDiss_Type()
)
hh3cDot11PROBEClientIsDiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11PROBEClientIsDiss.setStatus("current")
_Hh3cDot11PROBEClientStatus_Type = Hh3cDot11PROBEDevStatus
_Hh3cDot11PROBEClientStatus_Object = MibTableColumn
hh3cDot11PROBEClientStatus = _Hh3cDot11PROBEClientStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 1, 1, 5),
    _Hh3cDot11PROBEClientStatus_Type()
)
hh3cDot11PROBEClientStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11PROBEClientStatus.setStatus("current")
_Hh3cDot11PROBEClientDuratTime_Type = TimeTicks
_Hh3cDot11PROBEClientDuratTime_Object = MibTableColumn
hh3cDot11PROBEClientDuratTime = _Hh3cDot11PROBEClientDuratTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 1, 1, 6),
    _Hh3cDot11PROBEClientDuratTime_Type()
)
hh3cDot11PROBEClientDuratTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11PROBEClientDuratTime.setStatus("current")


class _Hh3cDot11PROBEClientVendor_Type(OctetString):
    """Custom type hh3cDot11PROBEClientVendor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cDot11PROBEClientVendor_Type.__name__ = "OctetString"
_Hh3cDot11PROBEClientVendor_Object = MibTableColumn
hh3cDot11PROBEClientVendor = _Hh3cDot11PROBEClientVendor_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 1, 1, 7),
    _Hh3cDot11PROBEClientVendor_Type()
)
hh3cDot11PROBEClientVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11PROBEClientVendor.setStatus("current")
_Hh3cDot11PROBEClientRptApNum_Type = Integer32
_Hh3cDot11PROBEClientRptApNum_Object = MibTableColumn
hh3cDot11PROBEClientRptApNum = _Hh3cDot11PROBEClientRptApNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 1, 1, 8),
    _Hh3cDot11PROBEClientRptApNum_Type()
)
hh3cDot11PROBEClientRptApNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11PROBEClientRptApNum.setStatus("current")
_Hh3cDot11PROBEClientWorkChannel_Type = Hh3cDot11PROBEChannel
_Hh3cDot11PROBEClientWorkChannel_Object = MibTableColumn
hh3cDot11PROBEClientWorkChannel = _Hh3cDot11PROBEClientWorkChannel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 1, 1, 9),
    _Hh3cDot11PROBEClientWorkChannel_Type()
)
hh3cDot11PROBEClientWorkChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11PROBEClientWorkChannel.setStatus("current")
_Hh3cDot11PROBEClientRSSIMax_Type = Integer32
_Hh3cDot11PROBEClientRSSIMax_Object = MibTableColumn
hh3cDot11PROBEClientRSSIMax = _Hh3cDot11PROBEClientRSSIMax_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 1, 1, 10),
    _Hh3cDot11PROBEClientRSSIMax_Type()
)
hh3cDot11PROBEClientRSSIMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11PROBEClientRSSIMax.setStatus("current")
_Hh3cDot11PROBEClientRSSIMin_Type = Integer32
_Hh3cDot11PROBEClientRSSIMin_Object = MibTableColumn
hh3cDot11PROBEClientRSSIMin = _Hh3cDot11PROBEClientRSSIMin_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 1, 1, 11),
    _Hh3cDot11PROBEClientRSSIMin_Type()
)
hh3cDot11PROBEClientRSSIMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11PROBEClientRSSIMin.setStatus("current")
_Hh3cDot11PROBEClientRSSI_Type = Integer32
_Hh3cDot11PROBEClientRSSI_Object = MibTableColumn
hh3cDot11PROBEClientRSSI = _Hh3cDot11PROBEClientRSSI_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 1, 1, 12),
    _Hh3cDot11PROBEClientRSSI_Type()
)
hh3cDot11PROBEClientRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11PROBEClientRSSI.setStatus("current")


class _Hh3cDot11PROBEClientFirstTime_Type(OctetString):
    """Custom type hh3cDot11PROBEClientFirstTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_Hh3cDot11PROBEClientFirstTime_Type.__name__ = "OctetString"
_Hh3cDot11PROBEClientFirstTime_Object = MibTableColumn
hh3cDot11PROBEClientFirstTime = _Hh3cDot11PROBEClientFirstTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 1, 1, 13),
    _Hh3cDot11PROBEClientFirstTime_Type()
)
hh3cDot11PROBEClientFirstTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11PROBEClientFirstTime.setStatus("current")


class _Hh3cDot11PROBEClientLastTime_Type(OctetString):
    """Custom type hh3cDot11PROBEClientLastTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_Hh3cDot11PROBEClientLastTime_Type.__name__ = "OctetString"
_Hh3cDot11PROBEClientLastTime_Object = MibTableColumn
hh3cDot11PROBEClientLastTime = _Hh3cDot11PROBEClientLastTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 1, 1, 14),
    _Hh3cDot11PROBEClientLastTime_Type()
)
hh3cDot11PROBEClientLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11PROBEClientLastTime.setStatus("current")
_Hh3cDot11PROBEStatTable_Object = MibTable
hh3cDot11PROBEStatTable = _Hh3cDot11PROBEStatTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cDot11PROBEStatTable.setStatus("current")
_Hh3cDot11PROBEStatEntry_Object = MibTableRow
hh3cDot11PROBEStatEntry = _Hh3cDot11PROBEStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 2, 1)
)
hh3cDot11PROBEStatEntry.setIndexNames(
    (0, "HH3C-DOT11-PROBE-MIB", "hh3cDot11PROBEStatTime"),
)
if mibBuilder.loadTexts:
    hh3cDot11PROBEStatEntry.setStatus("current")


class _Hh3cDot11PROBEStatTime_Type(OctetString):
    """Custom type hh3cDot11PROBEStatTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_Hh3cDot11PROBEStatTime_Type.__name__ = "OctetString"
_Hh3cDot11PROBEStatTime_Object = MibTableColumn
hh3cDot11PROBEStatTime = _Hh3cDot11PROBEStatTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 2, 1, 1),
    _Hh3cDot11PROBEStatTime_Type()
)
hh3cDot11PROBEStatTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11PROBEStatTime.setStatus("current")
_Hh3cDot11PROBEStatRssiMaxNum_Type = Integer32
_Hh3cDot11PROBEStatRssiMaxNum_Object = MibTableColumn
hh3cDot11PROBEStatRssiMaxNum = _Hh3cDot11PROBEStatRssiMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 2, 1, 2),
    _Hh3cDot11PROBEStatRssiMaxNum_Type()
)
hh3cDot11PROBEStatRssiMaxNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11PROBEStatRssiMaxNum.setStatus("current")
_Hh3cDot11PROBEStatRssiMiddleNum_Type = Integer32
_Hh3cDot11PROBEStatRssiMiddleNum_Object = MibTableColumn
hh3cDot11PROBEStatRssiMiddleNum = _Hh3cDot11PROBEStatRssiMiddleNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 2, 1, 3),
    _Hh3cDot11PROBEStatRssiMiddleNum_Type()
)
hh3cDot11PROBEStatRssiMiddleNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11PROBEStatRssiMiddleNum.setStatus("current")
_Hh3cDot11PROBEStatRssiMinNum_Type = Integer32
_Hh3cDot11PROBEStatRssiMinNum_Object = MibTableColumn
hh3cDot11PROBEStatRssiMinNum = _Hh3cDot11PROBEStatRssiMinNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 2, 1, 4),
    _Hh3cDot11PROBEStatRssiMinNum_Type()
)
hh3cDot11PROBEStatRssiMinNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11PROBEStatRssiMinNum.setStatus("current")
_Hh3cDot11PROBEStatTotalNum_Type = Integer32
_Hh3cDot11PROBEStatTotalNum_Object = MibTableColumn
hh3cDot11PROBEStatTotalNum = _Hh3cDot11PROBEStatTotalNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 2, 1, 5),
    _Hh3cDot11PROBEStatTotalNum_Type()
)
hh3cDot11PROBEStatTotalNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11PROBEStatTotalNum.setStatus("current")
_Hh3cDot11PROBEStatAssocNum_Type = Integer32
_Hh3cDot11PROBEStatAssocNum_Object = MibTableColumn
hh3cDot11PROBEStatAssocNum = _Hh3cDot11PROBEStatAssocNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 2, 1, 6),
    _Hh3cDot11PROBEStatAssocNum_Type()
)
hh3cDot11PROBEStatAssocNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11PROBEStatAssocNum.setStatus("current")
_Hh3cDot11PROBEStatDissocNum_Type = Integer32
_Hh3cDot11PROBEStatDissocNum_Object = MibTableColumn
hh3cDot11PROBEStatDissocNum = _Hh3cDot11PROBEStatDissocNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 2, 1, 7),
    _Hh3cDot11PROBEStatDissocNum_Type()
)
hh3cDot11PROBEStatDissocNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11PROBEStatDissocNum.setStatus("current")
_Hh3cDot11PROBEApTable_Object = MibTable
hh3cDot11PROBEApTable = _Hh3cDot11PROBEApTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 3)
)
if mibBuilder.loadTexts:
    hh3cDot11PROBEApTable.setStatus("current")
_Hh3cDot11PROBEApEntry_Object = MibTableRow
hh3cDot11PROBEApEntry = _Hh3cDot11PROBEApEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 3, 1)
)
hh3cDot11PROBEApEntry.setIndexNames(
    (0, "HH3C-DOT11-PROBE-MIB", "hh3cDot11PROBEApMacAddress"),
)
if mibBuilder.loadTexts:
    hh3cDot11PROBEApEntry.setStatus("current")
_Hh3cDot11PROBEApMacAddress_Type = MacAddress
_Hh3cDot11PROBEApMacAddress_Object = MibTableColumn
hh3cDot11PROBEApMacAddress = _Hh3cDot11PROBEApMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 3, 1, 1),
    _Hh3cDot11PROBEApMacAddress_Type()
)
hh3cDot11PROBEApMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11PROBEApMacAddress.setStatus("current")


class _Hh3cDot11PROBEApSsid_Type(OctetString):
    """Custom type hh3cDot11PROBEApSsid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cDot11PROBEApSsid_Type.__name__ = "OctetString"
_Hh3cDot11PROBEApSsid_Object = MibTableColumn
hh3cDot11PROBEApSsid = _Hh3cDot11PROBEApSsid_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 3, 1, 2),
    _Hh3cDot11PROBEApSsid_Type()
)
hh3cDot11PROBEApSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11PROBEApSsid.setStatus("current")
_Hh3cDot11PROBEApStatus_Type = Hh3cDot11PROBEDevStatus
_Hh3cDot11PROBEApStatus_Object = MibTableColumn
hh3cDot11PROBEApStatus = _Hh3cDot11PROBEApStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 3, 1, 3),
    _Hh3cDot11PROBEApStatus_Type()
)
hh3cDot11PROBEApStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11PROBEApStatus.setStatus("current")
_Hh3cDot11PROBEApStatusDuTime_Type = TimeTicks
_Hh3cDot11PROBEApStatusDuTime_Object = MibTableColumn
hh3cDot11PROBEApStatusDuTime = _Hh3cDot11PROBEApStatusDuTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 3, 1, 4),
    _Hh3cDot11PROBEApStatusDuTime_Type()
)
hh3cDot11PROBEApStatusDuTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11PROBEApStatusDuTime.setStatus("current")


class _Hh3cDot11PROBEApVendor_Type(OctetString):
    """Custom type hh3cDot11PROBEApVendor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cDot11PROBEApVendor_Type.__name__ = "OctetString"
_Hh3cDot11PROBEApVendor_Object = MibTableColumn
hh3cDot11PROBEApVendor = _Hh3cDot11PROBEApVendor_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 3, 1, 5),
    _Hh3cDot11PROBEApVendor_Type()
)
hh3cDot11PROBEApVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11PROBEApVendor.setStatus("current")
_Hh3cDot11PROBEApRadioType_Type = Hh3cDot11PROBERadioType
_Hh3cDot11PROBEApRadioType_Object = MibTableColumn
hh3cDot11PROBEApRadioType = _Hh3cDot11PROBEApRadioType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 3, 1, 6),
    _Hh3cDot11PROBEApRadioType_Type()
)
hh3cDot11PROBEApRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11PROBEApRadioType.setStatus("current")
_Hh3cDot11PROBEApSecurityType_Type = Hh3cDot11PROBESecurityType
_Hh3cDot11PROBEApSecurityType_Object = MibTableColumn
hh3cDot11PROBEApSecurityType = _Hh3cDot11PROBEApSecurityType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 3, 1, 7),
    _Hh3cDot11PROBEApSecurityType_Type()
)
hh3cDot11PROBEApSecurityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11PROBEApSecurityType.setStatus("current")
_Hh3cDot11PROBEApEncryMethod_Type = Hh3cDot11PROBEEncryptMethod
_Hh3cDot11PROBEApEncryMethod_Object = MibTableColumn
hh3cDot11PROBEApEncryMethod = _Hh3cDot11PROBEApEncryMethod_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 3, 1, 8),
    _Hh3cDot11PROBEApEncryMethod_Type()
)
hh3cDot11PROBEApEncryMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11PROBEApEncryMethod.setStatus("current")
_Hh3cDot11PROBEApAuthMethod_Type = Hh3cDot11PROBEAuthMethod
_Hh3cDot11PROBEApAuthMethod_Object = MibTableColumn
hh3cDot11PROBEApAuthMethod = _Hh3cDot11PROBEApAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 3, 1, 9),
    _Hh3cDot11PROBEApAuthMethod_Type()
)
hh3cDot11PROBEApAuthMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11PROBEApAuthMethod.setStatus("current")
_Hh3cDot11PROBEApIsBroadSSID_Type = TruthValue
_Hh3cDot11PROBEApIsBroadSSID_Object = MibTableColumn
hh3cDot11PROBEApIsBroadSSID = _Hh3cDot11PROBEApIsBroadSSID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 3, 1, 10),
    _Hh3cDot11PROBEApIsBroadSSID_Type()
)
hh3cDot11PROBEApIsBroadSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11PROBEApIsBroadSSID.setStatus("current")
_Hh3cDot11PROBEApQosSupport_Type = TruthValue
_Hh3cDot11PROBEApQosSupport_Object = MibTableColumn
hh3cDot11PROBEApQosSupport = _Hh3cDot11PROBEApQosSupport_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 3, 1, 11),
    _Hh3cDot11PROBEApQosSupport_Type()
)
hh3cDot11PROBEApQosSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11PROBEApQosSupport.setStatus("current")
_Hh3cDot11PROBEApBeaconIntvl_Type = Integer32
_Hh3cDot11PROBEApBeaconIntvl_Object = MibTableColumn
hh3cDot11PROBEApBeaconIntvl = _Hh3cDot11PROBEApBeaconIntvl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 3, 1, 12),
    _Hh3cDot11PROBEApBeaconIntvl_Type()
)
hh3cDot11PROBEApBeaconIntvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11PROBEApBeaconIntvl.setStatus("current")
_Hh3cDot11PROBEApUpDuration_Type = TimeTicks
_Hh3cDot11PROBEApUpDuration_Object = MibTableColumn
hh3cDot11PROBEApUpDuration = _Hh3cDot11PROBEApUpDuration_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 3, 1, 13),
    _Hh3cDot11PROBEApUpDuration_Type()
)
hh3cDot11PROBEApUpDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11PROBEApUpDuration.setStatus("current")
_Hh3cDot11PROBEApSCWS_Type = TruthValue
_Hh3cDot11PROBEApSCWS_Object = MibTableColumn
hh3cDot11PROBEApSCWS = _Hh3cDot11PROBEApSCWS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 3, 1, 14),
    _Hh3cDot11PROBEApSCWS_Type()
)
hh3cDot11PROBEApSCWS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11PROBEApSCWS.setStatus("current")
_Hh3cDot11PROBEApRptSensorNum_Type = Integer32
_Hh3cDot11PROBEApRptSensorNum_Object = MibTableColumn
hh3cDot11PROBEApRptSensorNum = _Hh3cDot11PROBEApRptSensorNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 3, 1, 15),
    _Hh3cDot11PROBEApRptSensorNum_Type()
)
hh3cDot11PROBEApRptSensorNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11PROBEApRptSensorNum.setStatus("current")
_Hh3cDot11PROBEApChannel_Type = Hh3cDot11PROBEChannel
_Hh3cDot11PROBEApChannel_Object = MibTableColumn
hh3cDot11PROBEApChannel = _Hh3cDot11PROBEApChannel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 3, 1, 16),
    _Hh3cDot11PROBEApChannel_Type()
)
hh3cDot11PROBEApChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11PROBEApChannel.setStatus("current")
_Hh3cDot11PROBEApRSSIMax_Type = Integer32
_Hh3cDot11PROBEApRSSIMax_Object = MibTableColumn
hh3cDot11PROBEApRSSIMax = _Hh3cDot11PROBEApRSSIMax_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 3, 1, 17),
    _Hh3cDot11PROBEApRSSIMax_Type()
)
hh3cDot11PROBEApRSSIMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11PROBEApRSSIMax.setStatus("current")
_Hh3cDot11PROBEApRSSIMin_Type = Integer32
_Hh3cDot11PROBEApRSSIMin_Object = MibTableColumn
hh3cDot11PROBEApRSSIMin = _Hh3cDot11PROBEApRSSIMin_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 3, 1, 18),
    _Hh3cDot11PROBEApRSSIMin_Type()
)
hh3cDot11PROBEApRSSIMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11PROBEApRSSIMin.setStatus("current")
_Hh3cDot11PROBEApRSSI_Type = Integer32
_Hh3cDot11PROBEApRSSI_Object = MibTableColumn
hh3cDot11PROBEApRSSI = _Hh3cDot11PROBEApRSSI_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 3, 1, 19),
    _Hh3cDot11PROBEApRSSI_Type()
)
hh3cDot11PROBEApRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11PROBEApRSSI.setStatus("current")


class _Hh3cDot11PROBEApFirstRptTime_Type(OctetString):
    """Custom type hh3cDot11PROBEApFirstRptTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_Hh3cDot11PROBEApFirstRptTime_Type.__name__ = "OctetString"
_Hh3cDot11PROBEApFirstRptTime_Object = MibTableColumn
hh3cDot11PROBEApFirstRptTime = _Hh3cDot11PROBEApFirstRptTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 3, 1, 20),
    _Hh3cDot11PROBEApFirstRptTime_Type()
)
hh3cDot11PROBEApFirstRptTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11PROBEApFirstRptTime.setStatus("current")


class _Hh3cDot11PROBEApLastRptTime_Type(OctetString):
    """Custom type hh3cDot11PROBEApLastRptTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_Hh3cDot11PROBEApLastRptTime_Type.__name__ = "OctetString"
_Hh3cDot11PROBEApLastRptTime_Object = MibTableColumn
hh3cDot11PROBEApLastRptTime = _Hh3cDot11PROBEApLastRptTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 3, 1, 21),
    _Hh3cDot11PROBEApLastRptTime_Type()
)
hh3cDot11PROBEApLastRptTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11PROBEApLastRptTime.setStatus("current")
_Hh3cDot11PROBEApAssoCltTable_Object = MibTable
hh3cDot11PROBEApAssoCltTable = _Hh3cDot11PROBEApAssoCltTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 4)
)
if mibBuilder.loadTexts:
    hh3cDot11PROBEApAssoCltTable.setStatus("current")
_Hh3cDot11PROBEApAssoCltEntry_Object = MibTableRow
hh3cDot11PROBEApAssoCltEntry = _Hh3cDot11PROBEApAssoCltEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 4, 1)
)
hh3cDot11PROBEApAssoCltEntry.setIndexNames(
    (0, "HH3C-DOT11-PROBE-MIB", "hh3cDot11PROBEApAssoCltApMac"),
    (0, "HH3C-DOT11-PROBE-MIB", "hh3cDot11PROBEApAssoCltCltMac"),
)
if mibBuilder.loadTexts:
    hh3cDot11PROBEApAssoCltEntry.setStatus("current")
_Hh3cDot11PROBEApAssoCltApMac_Type = MacAddress
_Hh3cDot11PROBEApAssoCltApMac_Object = MibTableColumn
hh3cDot11PROBEApAssoCltApMac = _Hh3cDot11PROBEApAssoCltApMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 4, 1, 1),
    _Hh3cDot11PROBEApAssoCltApMac_Type()
)
hh3cDot11PROBEApAssoCltApMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11PROBEApAssoCltApMac.setStatus("current")
_Hh3cDot11PROBEApAssoCltCltMac_Type = MacAddress
_Hh3cDot11PROBEApAssoCltCltMac_Object = MibTableColumn
hh3cDot11PROBEApAssoCltCltMac = _Hh3cDot11PROBEApAssoCltCltMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 4, 1, 2),
    _Hh3cDot11PROBEApAssoCltCltMac_Type()
)
hh3cDot11PROBEApAssoCltCltMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11PROBEApAssoCltCltMac.setStatus("current")
_Hh3cDot11PROBEApAssoCltIsAsso_Type = TruthValue
_Hh3cDot11PROBEApAssoCltIsAsso_Object = MibTableColumn
hh3cDot11PROBEApAssoCltIsAsso = _Hh3cDot11PROBEApAssoCltIsAsso_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 4, 1, 3),
    _Hh3cDot11PROBEApAssoCltIsAsso_Type()
)
hh3cDot11PROBEApAssoCltIsAsso.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11PROBEApAssoCltIsAsso.setStatus("current")
_Hh3cDot11PROBEApRepSenTable_Object = MibTable
hh3cDot11PROBEApRepSenTable = _Hh3cDot11PROBEApRepSenTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 5)
)
if mibBuilder.loadTexts:
    hh3cDot11PROBEApRepSenTable.setStatus("current")
_Hh3cDot11PROBEApRepSenEntry_Object = MibTableRow
hh3cDot11PROBEApRepSenEntry = _Hh3cDot11PROBEApRepSenEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 5, 1)
)
hh3cDot11PROBEApRepSenEntry.setIndexNames(
    (0, "HH3C-DOT11-PROBE-MIB", "hh3cDot11PROBEApRepSenApMac"),
    (0, "HH3C-DOT11-PROBE-MIB", "hh3cDot11PROBEApRepSenSenName"),
)
if mibBuilder.loadTexts:
    hh3cDot11PROBEApRepSenEntry.setStatus("current")
_Hh3cDot11PROBEApRepSenApMac_Type = MacAddress
_Hh3cDot11PROBEApRepSenApMac_Object = MibTableColumn
hh3cDot11PROBEApRepSenApMac = _Hh3cDot11PROBEApRepSenApMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 5, 1, 1),
    _Hh3cDot11PROBEApRepSenApMac_Type()
)
hh3cDot11PROBEApRepSenApMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11PROBEApRepSenApMac.setStatus("current")


class _Hh3cDot11PROBEApRepSenSenName_Type(OctetString):
    """Custom type hh3cDot11PROBEApRepSenSenName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_Hh3cDot11PROBEApRepSenSenName_Type.__name__ = "OctetString"
_Hh3cDot11PROBEApRepSenSenName_Object = MibTableColumn
hh3cDot11PROBEApRepSenSenName = _Hh3cDot11PROBEApRepSenSenName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 5, 1, 2),
    _Hh3cDot11PROBEApRepSenSenName_Type()
)
hh3cDot11PROBEApRepSenSenName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11PROBEApRepSenSenName.setStatus("current")


class _Hh3cDot11PROBEApRepSenRadioId_Type(Integer32):
    """Custom type hh3cDot11PROBEApRepSenRadioId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Hh3cDot11PROBEApRepSenRadioId_Type.__name__ = "Integer32"
_Hh3cDot11PROBEApRepSenRadioId_Object = MibTableColumn
hh3cDot11PROBEApRepSenRadioId = _Hh3cDot11PROBEApRepSenRadioId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 5, 1, 3),
    _Hh3cDot11PROBEApRepSenRadioId_Type()
)
hh3cDot11PROBEApRepSenRadioId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11PROBEApRepSenRadioId.setStatus("current")
_Hh3cDot11PROBEApRepSenRssi_Type = Integer32
_Hh3cDot11PROBEApRepSenRssi_Object = MibTableColumn
hh3cDot11PROBEApRepSenRssi = _Hh3cDot11PROBEApRepSenRssi_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 5, 1, 4),
    _Hh3cDot11PROBEApRepSenRssi_Type()
)
hh3cDot11PROBEApRepSenRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11PROBEApRepSenRssi.setStatus("current")
_Hh3cDot11PROBEApRepSenChannel_Type = Hh3cDot11PROBEChannel
_Hh3cDot11PROBEApRepSenChannel_Object = MibTableColumn
hh3cDot11PROBEApRepSenChannel = _Hh3cDot11PROBEApRepSenChannel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 5, 1, 5),
    _Hh3cDot11PROBEApRepSenChannel_Type()
)
hh3cDot11PROBEApRepSenChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11PROBEApRepSenChannel.setStatus("current")


class _Hh3cDot11PROBEApRepSenFirRepTim_Type(OctetString):
    """Custom type hh3cDot11PROBEApRepSenFirRepTim based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_Hh3cDot11PROBEApRepSenFirRepTim_Type.__name__ = "OctetString"
_Hh3cDot11PROBEApRepSenFirRepTim_Object = MibTableColumn
hh3cDot11PROBEApRepSenFirRepTim = _Hh3cDot11PROBEApRepSenFirRepTim_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 5, 1, 6),
    _Hh3cDot11PROBEApRepSenFirRepTim_Type()
)
hh3cDot11PROBEApRepSenFirRepTim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11PROBEApRepSenFirRepTim.setStatus("current")


class _Hh3cDot11PROBEApRepSenLasRepTim_Type(OctetString):
    """Custom type hh3cDot11PROBEApRepSenLasRepTim based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_Hh3cDot11PROBEApRepSenLasRepTim_Type.__name__ = "OctetString"
_Hh3cDot11PROBEApRepSenLasRepTim_Object = MibTableColumn
hh3cDot11PROBEApRepSenLasRepTim = _Hh3cDot11PROBEApRepSenLasRepTim_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 5, 1, 7),
    _Hh3cDot11PROBEApRepSenLasRepTim_Type()
)
hh3cDot11PROBEApRepSenLasRepTim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11PROBEApRepSenLasRepTim.setStatus("current")
_Hh3cDot11PROBECliRepSenTable_Object = MibTable
hh3cDot11PROBECliRepSenTable = _Hh3cDot11PROBECliRepSenTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 6)
)
if mibBuilder.loadTexts:
    hh3cDot11PROBECliRepSenTable.setStatus("current")
_Hh3cDot11PROBECliRepSenEntry_Object = MibTableRow
hh3cDot11PROBECliRepSenEntry = _Hh3cDot11PROBECliRepSenEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 6, 1)
)
hh3cDot11PROBECliRepSenEntry.setIndexNames(
    (0, "HH3C-DOT11-PROBE-MIB", "hh3cDot11PROBECliRepSenCliMac"),
    (0, "HH3C-DOT11-PROBE-MIB", "hh3cDot11PROBECliRepSenSenName"),
)
if mibBuilder.loadTexts:
    hh3cDot11PROBECliRepSenEntry.setStatus("current")
_Hh3cDot11PROBECliRepSenCliMac_Type = MacAddress
_Hh3cDot11PROBECliRepSenCliMac_Object = MibTableColumn
hh3cDot11PROBECliRepSenCliMac = _Hh3cDot11PROBECliRepSenCliMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 6, 1, 1),
    _Hh3cDot11PROBECliRepSenCliMac_Type()
)
hh3cDot11PROBECliRepSenCliMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11PROBECliRepSenCliMac.setStatus("current")


class _Hh3cDot11PROBECliRepSenSenName_Type(OctetString):
    """Custom type hh3cDot11PROBECliRepSenSenName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_Hh3cDot11PROBECliRepSenSenName_Type.__name__ = "OctetString"
_Hh3cDot11PROBECliRepSenSenName_Object = MibTableColumn
hh3cDot11PROBECliRepSenSenName = _Hh3cDot11PROBECliRepSenSenName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 6, 1, 2),
    _Hh3cDot11PROBECliRepSenSenName_Type()
)
hh3cDot11PROBECliRepSenSenName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11PROBECliRepSenSenName.setStatus("current")


class _Hh3cDot11PROBECliRepSenRadioId_Type(Integer32):
    """Custom type hh3cDot11PROBECliRepSenRadioId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Hh3cDot11PROBECliRepSenRadioId_Type.__name__ = "Integer32"
_Hh3cDot11PROBECliRepSenRadioId_Object = MibTableColumn
hh3cDot11PROBECliRepSenRadioId = _Hh3cDot11PROBECliRepSenRadioId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 6, 1, 3),
    _Hh3cDot11PROBECliRepSenRadioId_Type()
)
hh3cDot11PROBECliRepSenRadioId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11PROBECliRepSenRadioId.setStatus("current")
_Hh3cDot11PROBECliRepSenRssi_Type = Integer32
_Hh3cDot11PROBECliRepSenRssi_Object = MibTableColumn
hh3cDot11PROBECliRepSenRssi = _Hh3cDot11PROBECliRepSenRssi_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 6, 1, 4),
    _Hh3cDot11PROBECliRepSenRssi_Type()
)
hh3cDot11PROBECliRepSenRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11PROBECliRepSenRssi.setStatus("current")
_Hh3cDot11PROBECliRepSenChannel_Type = Hh3cDot11PROBEChannel
_Hh3cDot11PROBECliRepSenChannel_Object = MibTableColumn
hh3cDot11PROBECliRepSenChannel = _Hh3cDot11PROBECliRepSenChannel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 6, 1, 5),
    _Hh3cDot11PROBECliRepSenChannel_Type()
)
hh3cDot11PROBECliRepSenChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11PROBECliRepSenChannel.setStatus("current")


class _Hh3cDot11PROBECliRepSenFRepTime_Type(OctetString):
    """Custom type hh3cDot11PROBECliRepSenFRepTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_Hh3cDot11PROBECliRepSenFRepTime_Type.__name__ = "OctetString"
_Hh3cDot11PROBECliRepSenFRepTime_Object = MibTableColumn
hh3cDot11PROBECliRepSenFRepTime = _Hh3cDot11PROBECliRepSenFRepTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 6, 1, 6),
    _Hh3cDot11PROBECliRepSenFRepTime_Type()
)
hh3cDot11PROBECliRepSenFRepTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11PROBECliRepSenFRepTime.setStatus("current")


class _Hh3cDot11PROBECliRepSenLRepTime_Type(OctetString):
    """Custom type hh3cDot11PROBECliRepSenLRepTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_Hh3cDot11PROBECliRepSenLRepTime_Type.__name__ = "OctetString"
_Hh3cDot11PROBECliRepSenLRepTime_Object = MibTableColumn
hh3cDot11PROBECliRepSenLRepTime = _Hh3cDot11PROBECliRepSenLRepTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 6, 1, 7),
    _Hh3cDot11PROBECliRepSenLRepTime_Type()
)
hh3cDot11PROBECliRepSenLRepTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11PROBECliRepSenLRepTime.setStatus("current")
_Hh3cDot11PROBECliRepSenAssAPMac_Type = MacAddress
_Hh3cDot11PROBECliRepSenAssAPMac_Object = MibTableColumn
hh3cDot11PROBECliRepSenAssAPMac = _Hh3cDot11PROBECliRepSenAssAPMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 17, 2, 6, 1, 8),
    _Hh3cDot11PROBECliRepSenAssAPMac_Type()
)
hh3cDot11PROBECliRepSenAssAPMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11PROBECliRepSenAssAPMac.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-DOT11-PROBE-MIB",
    **{"Hh3cDot11PROBEEnabledStatus": Hh3cDot11PROBEEnabledStatus,
       "Hh3cDot11PROBERadioType": Hh3cDot11PROBERadioType,
       "Hh3cDot11PROBEDevStatus": Hh3cDot11PROBEDevStatus,
       "Hh3cDot11PROBEChannel": Hh3cDot11PROBEChannel,
       "Hh3cDot11PROBEEncryptMethod": Hh3cDot11PROBEEncryptMethod,
       "Hh3cDot11PROBEAuthMethod": Hh3cDot11PROBEAuthMethod,
       "Hh3cDot11PROBESecurityType": Hh3cDot11PROBESecurityType,
       "hh3cDot11PROBE": hh3cDot11PROBE,
       "hh3cDot11PROBEConfigGroup": hh3cDot11PROBEConfigGroup,
       "hh3cDot11PROBERadioCfgTable": hh3cDot11PROBERadioCfgTable,
       "hh3cDot11PROBERadioCfgEntry": hh3cDot11PROBERadioCfgEntry,
       "hh3cDot11PROBERadioCfgApName": hh3cDot11PROBERadioCfgApName,
       "hh3cDot11PROBERadioCfgRadioId": hh3cDot11PROBERadioCfgRadioId,
       "hh3cDot11PROBERadioCfgStatus": hh3cDot11PROBERadioCfgStatus,
       "hh3cDot11PROBEDataGroup": hh3cDot11PROBEDataGroup,
       "hh3cDot11PROBEClientTable": hh3cDot11PROBEClientTable,
       "hh3cDot11PROBEClientEntry": hh3cDot11PROBEClientEntry,
       "hh3cDot11PROBEClientMac": hh3cDot11PROBEClientMac,
       "hh3cDot11PROBEClientBSSID": hh3cDot11PROBEClientBSSID,
       "hh3cDot11PROBEClientSSID": hh3cDot11PROBEClientSSID,
       "hh3cDot11PROBEClientIsDiss": hh3cDot11PROBEClientIsDiss,
       "hh3cDot11PROBEClientStatus": hh3cDot11PROBEClientStatus,
       "hh3cDot11PROBEClientDuratTime": hh3cDot11PROBEClientDuratTime,
       "hh3cDot11PROBEClientVendor": hh3cDot11PROBEClientVendor,
       "hh3cDot11PROBEClientRptApNum": hh3cDot11PROBEClientRptApNum,
       "hh3cDot11PROBEClientWorkChannel": hh3cDot11PROBEClientWorkChannel,
       "hh3cDot11PROBEClientRSSIMax": hh3cDot11PROBEClientRSSIMax,
       "hh3cDot11PROBEClientRSSIMin": hh3cDot11PROBEClientRSSIMin,
       "hh3cDot11PROBEClientRSSI": hh3cDot11PROBEClientRSSI,
       "hh3cDot11PROBEClientFirstTime": hh3cDot11PROBEClientFirstTime,
       "hh3cDot11PROBEClientLastTime": hh3cDot11PROBEClientLastTime,
       "hh3cDot11PROBEStatTable": hh3cDot11PROBEStatTable,
       "hh3cDot11PROBEStatEntry": hh3cDot11PROBEStatEntry,
       "hh3cDot11PROBEStatTime": hh3cDot11PROBEStatTime,
       "hh3cDot11PROBEStatRssiMaxNum": hh3cDot11PROBEStatRssiMaxNum,
       "hh3cDot11PROBEStatRssiMiddleNum": hh3cDot11PROBEStatRssiMiddleNum,
       "hh3cDot11PROBEStatRssiMinNum": hh3cDot11PROBEStatRssiMinNum,
       "hh3cDot11PROBEStatTotalNum": hh3cDot11PROBEStatTotalNum,
       "hh3cDot11PROBEStatAssocNum": hh3cDot11PROBEStatAssocNum,
       "hh3cDot11PROBEStatDissocNum": hh3cDot11PROBEStatDissocNum,
       "hh3cDot11PROBEApTable": hh3cDot11PROBEApTable,
       "hh3cDot11PROBEApEntry": hh3cDot11PROBEApEntry,
       "hh3cDot11PROBEApMacAddress": hh3cDot11PROBEApMacAddress,
       "hh3cDot11PROBEApSsid": hh3cDot11PROBEApSsid,
       "hh3cDot11PROBEApStatus": hh3cDot11PROBEApStatus,
       "hh3cDot11PROBEApStatusDuTime": hh3cDot11PROBEApStatusDuTime,
       "hh3cDot11PROBEApVendor": hh3cDot11PROBEApVendor,
       "hh3cDot11PROBEApRadioType": hh3cDot11PROBEApRadioType,
       "hh3cDot11PROBEApSecurityType": hh3cDot11PROBEApSecurityType,
       "hh3cDot11PROBEApEncryMethod": hh3cDot11PROBEApEncryMethod,
       "hh3cDot11PROBEApAuthMethod": hh3cDot11PROBEApAuthMethod,
       "hh3cDot11PROBEApIsBroadSSID": hh3cDot11PROBEApIsBroadSSID,
       "hh3cDot11PROBEApQosSupport": hh3cDot11PROBEApQosSupport,
       "hh3cDot11PROBEApBeaconIntvl": hh3cDot11PROBEApBeaconIntvl,
       "hh3cDot11PROBEApUpDuration": hh3cDot11PROBEApUpDuration,
       "hh3cDot11PROBEApSCWS": hh3cDot11PROBEApSCWS,
       "hh3cDot11PROBEApRptSensorNum": hh3cDot11PROBEApRptSensorNum,
       "hh3cDot11PROBEApChannel": hh3cDot11PROBEApChannel,
       "hh3cDot11PROBEApRSSIMax": hh3cDot11PROBEApRSSIMax,
       "hh3cDot11PROBEApRSSIMin": hh3cDot11PROBEApRSSIMin,
       "hh3cDot11PROBEApRSSI": hh3cDot11PROBEApRSSI,
       "hh3cDot11PROBEApFirstRptTime": hh3cDot11PROBEApFirstRptTime,
       "hh3cDot11PROBEApLastRptTime": hh3cDot11PROBEApLastRptTime,
       "hh3cDot11PROBEApAssoCltTable": hh3cDot11PROBEApAssoCltTable,
       "hh3cDot11PROBEApAssoCltEntry": hh3cDot11PROBEApAssoCltEntry,
       "hh3cDot11PROBEApAssoCltApMac": hh3cDot11PROBEApAssoCltApMac,
       "hh3cDot11PROBEApAssoCltCltMac": hh3cDot11PROBEApAssoCltCltMac,
       "hh3cDot11PROBEApAssoCltIsAsso": hh3cDot11PROBEApAssoCltIsAsso,
       "hh3cDot11PROBEApRepSenTable": hh3cDot11PROBEApRepSenTable,
       "hh3cDot11PROBEApRepSenEntry": hh3cDot11PROBEApRepSenEntry,
       "hh3cDot11PROBEApRepSenApMac": hh3cDot11PROBEApRepSenApMac,
       "hh3cDot11PROBEApRepSenSenName": hh3cDot11PROBEApRepSenSenName,
       "hh3cDot11PROBEApRepSenRadioId": hh3cDot11PROBEApRepSenRadioId,
       "hh3cDot11PROBEApRepSenRssi": hh3cDot11PROBEApRepSenRssi,
       "hh3cDot11PROBEApRepSenChannel": hh3cDot11PROBEApRepSenChannel,
       "hh3cDot11PROBEApRepSenFirRepTim": hh3cDot11PROBEApRepSenFirRepTim,
       "hh3cDot11PROBEApRepSenLasRepTim": hh3cDot11PROBEApRepSenLasRepTim,
       "hh3cDot11PROBECliRepSenTable": hh3cDot11PROBECliRepSenTable,
       "hh3cDot11PROBECliRepSenEntry": hh3cDot11PROBECliRepSenEntry,
       "hh3cDot11PROBECliRepSenCliMac": hh3cDot11PROBECliRepSenCliMac,
       "hh3cDot11PROBECliRepSenSenName": hh3cDot11PROBECliRepSenSenName,
       "hh3cDot11PROBECliRepSenRadioId": hh3cDot11PROBECliRepSenRadioId,
       "hh3cDot11PROBECliRepSenRssi": hh3cDot11PROBECliRepSenRssi,
       "hh3cDot11PROBECliRepSenChannel": hh3cDot11PROBECliRepSenChannel,
       "hh3cDot11PROBECliRepSenFRepTime": hh3cDot11PROBECliRepSenFRepTime,
       "hh3cDot11PROBECliRepSenLRepTime": hh3cDot11PROBECliRepSenLRepTime,
       "hh3cDot11PROBECliRepSenAssAPMac": hh3cDot11PROBECliRepSenAssAPMac}
)
