# SNMP MIB module (ALPINE-TDCM-EDFA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\alpineoe\ALPINE-TDCM-EDFA-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:17:46 2025
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

(alpineProducts,) = mibBuilder.importSymbols(
    "ALPINE-ROOT",
    "alpineProducts")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlpineTdcmEdfaSystem_ObjectIdentity = ObjectIdentity
alpineTdcmEdfaSystem = _AlpineTdcmEdfaSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52326, 2, 1)
)
_AlpineTESlotBasicInfoTable_Object = MibTable
alpineTESlotBasicInfoTable = _AlpineTESlotBasicInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 52326, 2, 1, 1)
)
if mibBuilder.loadTexts:
    alpineTESlotBasicInfoTable.setStatus("current")
_AlpineTESlotBasicInfoEntry_Object = MibTableRow
alpineTESlotBasicInfoEntry = _AlpineTESlotBasicInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 52326, 2, 1, 1, 1)
)
alpineTESlotBasicInfoEntry.setIndexNames(
    (0, "ALPINE-TDCM-EDFA-MIB", "alpineTESBISlotNum"),
)
if mibBuilder.loadTexts:
    alpineTESlotBasicInfoEntry.setStatus("current")


class _AlpineTESBISlotNum_Type(Integer32):
    """Custom type alpineTESBISlotNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AlpineTESBISlotNum_Type.__name__ = "Integer32"
_AlpineTESBISlotNum_Object = MibTableColumn
alpineTESBISlotNum = _AlpineTESBISlotNum_Object(
    (1, 3, 6, 1, 4, 1, 52326, 2, 1, 1, 1, 1),
    _AlpineTESBISlotNum_Type()
)
alpineTESBISlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpineTESBISlotNum.setStatus("current")
_AlpineTESBISlotType_Type = Integer32
_AlpineTESBISlotType_Object = MibTableColumn
alpineTESBISlotType = _AlpineTESBISlotType_Object(
    (1, 3, 6, 1, 4, 1, 52326, 2, 1, 1, 1, 2),
    _AlpineTESBISlotType_Type()
)
alpineTESBISlotType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpineTESBISlotType.setStatus("current")


class _AlpineTESBISlotHwVer_Type(OctetString):
    """Custom type alpineTESBISlotHwVer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_AlpineTESBISlotHwVer_Type.__name__ = "OctetString"
_AlpineTESBISlotHwVer_Object = MibTableColumn
alpineTESBISlotHwVer = _AlpineTESBISlotHwVer_Object(
    (1, 3, 6, 1, 4, 1, 52326, 2, 1, 1, 1, 3),
    _AlpineTESBISlotHwVer_Type()
)
alpineTESBISlotHwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpineTESBISlotHwVer.setStatus("current")


class _AlpineTESBISlotFwVer_Type(OctetString):
    """Custom type alpineTESBISlotFwVer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_AlpineTESBISlotFwVer_Type.__name__ = "OctetString"
_AlpineTESBISlotFwVer_Object = MibTableColumn
alpineTESBISlotFwVer = _AlpineTESBISlotFwVer_Object(
    (1, 3, 6, 1, 4, 1, 52326, 2, 1, 1, 1, 4),
    _AlpineTESBISlotFwVer_Type()
)
alpineTESBISlotFwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpineTESBISlotFwVer.setStatus("current")


class _AlpineTEBISlotPN_Type(OctetString):
    """Custom type alpineTEBISlotPN based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_AlpineTEBISlotPN_Type.__name__ = "OctetString"
_AlpineTEBISlotPN_Object = MibTableColumn
alpineTEBISlotPN = _AlpineTEBISlotPN_Object(
    (1, 3, 6, 1, 4, 1, 52326, 2, 1, 1, 1, 5),
    _AlpineTEBISlotPN_Type()
)
alpineTEBISlotPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpineTEBISlotPN.setStatus("current")


class _AlpineTEBISlotSN_Type(OctetString):
    """Custom type alpineTEBISlotSN based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_AlpineTEBISlotSN_Type.__name__ = "OctetString"
_AlpineTEBISlotSN_Object = MibTableColumn
alpineTEBISlotSN = _AlpineTEBISlotSN_Object(
    (1, 3, 6, 1, 4, 1, 52326, 2, 1, 1, 1, 6),
    _AlpineTEBISlotSN_Type()
)
alpineTEBISlotSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpineTEBISlotSN.setStatus("current")


class _AlpineTEBISlotManuDate_Type(OctetString):
    """Custom type alpineTEBISlotManuDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_AlpineTEBISlotManuDate_Type.__name__ = "OctetString"
_AlpineTEBISlotManuDate_Object = MibTableColumn
alpineTEBISlotManuDate = _AlpineTEBISlotManuDate_Object(
    (1, 3, 6, 1, 4, 1, 52326, 2, 1, 1, 1, 7),
    _AlpineTEBISlotManuDate_Type()
)
alpineTEBISlotManuDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpineTEBISlotManuDate.setStatus("current")


class _AlpineTEBISlotTemperature_Type(OctetString):
    """Custom type alpineTEBISlotTemperature based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_AlpineTEBISlotTemperature_Type.__name__ = "OctetString"
_AlpineTEBISlotTemperature_Object = MibTableColumn
alpineTEBISlotTemperature = _AlpineTEBISlotTemperature_Object(
    (1, 3, 6, 1, 4, 1, 52326, 2, 1, 1, 1, 8),
    _AlpineTEBISlotTemperature_Type()
)
alpineTEBISlotTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpineTEBISlotTemperature.setStatus("current")


class _AlpineTEBISlotPower1Status_Type(Integer32):
    """Custom type alpineTEBISlotPower1Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AlpineTEBISlotPower1Status_Type.__name__ = "Integer32"
_AlpineTEBISlotPower1Status_Object = MibTableColumn
alpineTEBISlotPower1Status = _AlpineTEBISlotPower1Status_Object(
    (1, 3, 6, 1, 4, 1, 52326, 2, 1, 1, 1, 9),
    _AlpineTEBISlotPower1Status_Type()
)
alpineTEBISlotPower1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpineTEBISlotPower1Status.setStatus("current")


class _AlpineTEBISlotPower1Val_Type(OctetString):
    """Custom type alpineTEBISlotPower1Val based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_AlpineTEBISlotPower1Val_Type.__name__ = "OctetString"
_AlpineTEBISlotPower1Val_Object = MibTableColumn
alpineTEBISlotPower1Val = _AlpineTEBISlotPower1Val_Object(
    (1, 3, 6, 1, 4, 1, 52326, 2, 1, 1, 1, 10),
    _AlpineTEBISlotPower1Val_Type()
)
alpineTEBISlotPower1Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpineTEBISlotPower1Val.setStatus("current")
if mibBuilder.loadTexts:
    alpineTEBISlotPower1Val.setUnits("V")


class _AlpineTEBISlotPower2Status_Type(Integer32):
    """Custom type alpineTEBISlotPower2Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AlpineTEBISlotPower2Status_Type.__name__ = "Integer32"
_AlpineTEBISlotPower2Status_Object = MibTableColumn
alpineTEBISlotPower2Status = _AlpineTEBISlotPower2Status_Object(
    (1, 3, 6, 1, 4, 1, 52326, 2, 1, 1, 1, 11),
    _AlpineTEBISlotPower2Status_Type()
)
alpineTEBISlotPower2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpineTEBISlotPower2Status.setStatus("current")


class _AlpineTEBISlotPower2Val_Type(OctetString):
    """Custom type alpineTEBISlotPower2Val based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_AlpineTEBISlotPower2Val_Type.__name__ = "OctetString"
_AlpineTEBISlotPower2Val_Object = MibTableColumn
alpineTEBISlotPower2Val = _AlpineTEBISlotPower2Val_Object(
    (1, 3, 6, 1, 4, 1, 52326, 2, 1, 1, 1, 12),
    _AlpineTEBISlotPower2Val_Type()
)
alpineTEBISlotPower2Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpineTEBISlotPower2Val.setStatus("current")
_AlpineTEBISlotPowerTotalCnt_Type = Integer32
_AlpineTEBISlotPowerTotalCnt_Object = MibTableColumn
alpineTEBISlotPowerTotalCnt = _AlpineTEBISlotPowerTotalCnt_Object(
    (1, 3, 6, 1, 4, 1, 52326, 2, 1, 1, 1, 13),
    _AlpineTEBISlotPowerTotalCnt_Type()
)
alpineTEBISlotPowerTotalCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpineTEBISlotPowerTotalCnt.setStatus("current")
_AlpineTESlotStatusTable_Object = MibTable
alpineTESlotStatusTable = _AlpineTESlotStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 52326, 2, 1, 2)
)
if mibBuilder.loadTexts:
    alpineTESlotStatusTable.setStatus("current")
_AlpineTESlotStatusEntry_Object = MibTableRow
alpineTESlotStatusEntry = _AlpineTESlotStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 52326, 2, 1, 2, 1)
)
alpineTESlotStatusEntry.setIndexNames(
    (0, "ALPINE-TDCM-EDFA-MIB", "alpineTESlotNum"),
)
if mibBuilder.loadTexts:
    alpineTESlotStatusEntry.setStatus("current")


class _AlpineTESlotNum_Type(Integer32):
    """Custom type alpineTESlotNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AlpineTESlotNum_Type.__name__ = "Integer32"
_AlpineTESlotNum_Object = MibTableColumn
alpineTESlotNum = _AlpineTESlotNum_Object(
    (1, 3, 6, 1, 4, 1, 52326, 2, 1, 2, 1, 1),
    _AlpineTESlotNum_Type()
)
alpineTESlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpineTESlotNum.setStatus("current")


class _AlpineTESlotStatus_Type(Integer32):
    """Custom type alpineTESlotStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AlpineTESlotStatus_Type.__name__ = "Integer32"
_AlpineTESlotStatus_Object = MibTableColumn
alpineTESlotStatus = _AlpineTESlotStatus_Object(
    (1, 3, 6, 1, 4, 1, 52326, 2, 1, 2, 1, 2),
    _AlpineTESlotStatus_Type()
)
alpineTESlotStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpineTESlotStatus.setStatus("current")
_AlpineTEAlarm_ObjectIdentity = ObjectIdentity
alpineTEAlarm = _AlpineTEAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52326, 2, 1, 3)
)
_AlpineTEAlarmThldTable_Object = MibTable
alpineTEAlarmThldTable = _AlpineTEAlarmThldTable_Object(
    (1, 3, 6, 1, 4, 1, 52326, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    alpineTEAlarmThldTable.setStatus("current")
_AlpineTEAlarmThldEntry_Object = MibTableRow
alpineTEAlarmThldEntry = _AlpineTEAlarmThldEntry_Object(
    (1, 3, 6, 1, 4, 1, 52326, 2, 1, 3, 1, 1)
)
alpineTEAlarmThldEntry.setIndexNames(
    (0, "ALPINE-TDCM-EDFA-MIB", "alpineTeatSlotNum"),
)
if mibBuilder.loadTexts:
    alpineTEAlarmThldEntry.setStatus("current")


class _AlpineTeatSlotNum_Type(Integer32):
    """Custom type alpineTeatSlotNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AlpineTeatSlotNum_Type.__name__ = "Integer32"
_AlpineTeatSlotNum_Object = MibTableColumn
alpineTeatSlotNum = _AlpineTeatSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 52326, 2, 1, 3, 1, 1, 1),
    _AlpineTeatSlotNum_Type()
)
alpineTeatSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpineTeatSlotNum.setStatus("current")


class _AlpineTeatTempHighAlarmThld_Type(OctetString):
    """Custom type alpineTeatTempHighAlarmThld based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_AlpineTeatTempHighAlarmThld_Type.__name__ = "OctetString"
_AlpineTeatTempHighAlarmThld_Object = MibTableColumn
alpineTeatTempHighAlarmThld = _AlpineTeatTempHighAlarmThld_Object(
    (1, 3, 6, 1, 4, 1, 52326, 2, 1, 3, 1, 1, 2),
    _AlpineTeatTempHighAlarmThld_Type()
)
alpineTeatTempHighAlarmThld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alpineTeatTempHighAlarmThld.setStatus("current")


class _AlpineTeatTempHighWarningThld_Type(OctetString):
    """Custom type alpineTeatTempHighWarningThld based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_AlpineTeatTempHighWarningThld_Type.__name__ = "OctetString"
_AlpineTeatTempHighWarningThld_Object = MibTableColumn
alpineTeatTempHighWarningThld = _AlpineTeatTempHighWarningThld_Object(
    (1, 3, 6, 1, 4, 1, 52326, 2, 1, 3, 1, 1, 3),
    _AlpineTeatTempHighWarningThld_Type()
)
alpineTeatTempHighWarningThld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alpineTeatTempHighWarningThld.setStatus("current")


class _AlpineTeatTempLowAlarmThld_Type(OctetString):
    """Custom type alpineTeatTempLowAlarmThld based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_AlpineTeatTempLowAlarmThld_Type.__name__ = "OctetString"
_AlpineTeatTempLowAlarmThld_Object = MibTableColumn
alpineTeatTempLowAlarmThld = _AlpineTeatTempLowAlarmThld_Object(
    (1, 3, 6, 1, 4, 1, 52326, 2, 1, 3, 1, 1, 4),
    _AlpineTeatTempLowAlarmThld_Type()
)
alpineTeatTempLowAlarmThld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alpineTeatTempLowAlarmThld.setStatus("current")


class _AlpineTeatTempLowWarningThld_Type(OctetString):
    """Custom type alpineTeatTempLowWarningThld based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_AlpineTeatTempLowWarningThld_Type.__name__ = "OctetString"
_AlpineTeatTempLowWarningThld_Object = MibTableColumn
alpineTeatTempLowWarningThld = _AlpineTeatTempLowWarningThld_Object(
    (1, 3, 6, 1, 4, 1, 52326, 2, 1, 3, 1, 1, 5),
    _AlpineTeatTempLowWarningThld_Type()
)
alpineTeatTempLowWarningThld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alpineTeatTempLowWarningThld.setStatus("current")
_AlpineTESystemPowerTable_Object = MibTable
alpineTESystemPowerTable = _AlpineTESystemPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 52326, 2, 1, 4)
)
if mibBuilder.loadTexts:
    alpineTESystemPowerTable.setStatus("current")
_AlpineTESystemPowerEntry_Object = MibTableRow
alpineTESystemPowerEntry = _AlpineTESystemPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 52326, 2, 1, 4, 1)
)
alpineTESystemPowerEntry.setIndexNames(
    (0, "ALPINE-TDCM-EDFA-MIB", "alpineTEPowerCardId"),
)
if mibBuilder.loadTexts:
    alpineTESystemPowerEntry.setStatus("current")
_AlpineTEPowerCardId_Type = Integer32
_AlpineTEPowerCardId_Object = MibTableColumn
alpineTEPowerCardId = _AlpineTEPowerCardId_Object(
    (1, 3, 6, 1, 4, 1, 52326, 2, 1, 4, 1, 1),
    _AlpineTEPowerCardId_Type()
)
alpineTEPowerCardId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpineTEPowerCardId.setStatus("current")


class _AlpineTEPowerCardType_Type(Integer32):
    """Custom type alpineTEPowerCardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AlpineTEPowerCardType_Type.__name__ = "Integer32"
_AlpineTEPowerCardType_Object = MibTableColumn
alpineTEPowerCardType = _AlpineTEPowerCardType_Object(
    (1, 3, 6, 1, 4, 1, 52326, 2, 1, 4, 1, 2),
    _AlpineTEPowerCardType_Type()
)
alpineTEPowerCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpineTEPowerCardType.setStatus("current")


class _AlpineTEPowerCardHwVer_Type(OctetString):
    """Custom type alpineTEPowerCardHwVer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_AlpineTEPowerCardHwVer_Type.__name__ = "OctetString"
_AlpineTEPowerCardHwVer_Object = MibTableColumn
alpineTEPowerCardHwVer = _AlpineTEPowerCardHwVer_Object(
    (1, 3, 6, 1, 4, 1, 52326, 2, 1, 4, 1, 3),
    _AlpineTEPowerCardHwVer_Type()
)
alpineTEPowerCardHwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpineTEPowerCardHwVer.setStatus("current")


class _AlpineTEPowerCardFwVer_Type(OctetString):
    """Custom type alpineTEPowerCardFwVer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_AlpineTEPowerCardFwVer_Type.__name__ = "OctetString"
_AlpineTEPowerCardFwVer_Object = MibTableColumn
alpineTEPowerCardFwVer = _AlpineTEPowerCardFwVer_Object(
    (1, 3, 6, 1, 4, 1, 52326, 2, 1, 4, 1, 4),
    _AlpineTEPowerCardFwVer_Type()
)
alpineTEPowerCardFwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpineTEPowerCardFwVer.setStatus("current")


class _AlpineTEPowerCardPN_Type(OctetString):
    """Custom type alpineTEPowerCardPN based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_AlpineTEPowerCardPN_Type.__name__ = "OctetString"
_AlpineTEPowerCardPN_Object = MibTableColumn
alpineTEPowerCardPN = _AlpineTEPowerCardPN_Object(
    (1, 3, 6, 1, 4, 1, 52326, 2, 1, 4, 1, 5),
    _AlpineTEPowerCardPN_Type()
)
alpineTEPowerCardPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpineTEPowerCardPN.setStatus("current")


class _AlpineTEPowerCardSN_Type(OctetString):
    """Custom type alpineTEPowerCardSN based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_AlpineTEPowerCardSN_Type.__name__ = "OctetString"
_AlpineTEPowerCardSN_Object = MibTableColumn
alpineTEPowerCardSN = _AlpineTEPowerCardSN_Object(
    (1, 3, 6, 1, 4, 1, 52326, 2, 1, 4, 1, 6),
    _AlpineTEPowerCardSN_Type()
)
alpineTEPowerCardSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpineTEPowerCardSN.setStatus("current")


class _AlpineTEPowerCardManuDate_Type(OctetString):
    """Custom type alpineTEPowerCardManuDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_AlpineTEPowerCardManuDate_Type.__name__ = "OctetString"
_AlpineTEPowerCardManuDate_Object = MibTableColumn
alpineTEPowerCardManuDate = _AlpineTEPowerCardManuDate_Object(
    (1, 3, 6, 1, 4, 1, 52326, 2, 1, 4, 1, 7),
    _AlpineTEPowerCardManuDate_Type()
)
alpineTEPowerCardManuDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpineTEPowerCardManuDate.setStatus("current")


class _AlpineTEPowerCardPowerInStatus_Type(Integer32):
    """Custom type alpineTEPowerCardPowerInStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AlpineTEPowerCardPowerInStatus_Type.__name__ = "Integer32"
_AlpineTEPowerCardPowerInStatus_Object = MibTableColumn
alpineTEPowerCardPowerInStatus = _AlpineTEPowerCardPowerInStatus_Object(
    (1, 3, 6, 1, 4, 1, 52326, 2, 1, 4, 1, 8),
    _AlpineTEPowerCardPowerInStatus_Type()
)
alpineTEPowerCardPowerInStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpineTEPowerCardPowerInStatus.setStatus("current")


class _AlpineTEPowerCardPowerOutVal_Type(OctetString):
    """Custom type alpineTEPowerCardPowerOutVal based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_AlpineTEPowerCardPowerOutVal_Type.__name__ = "OctetString"
_AlpineTEPowerCardPowerOutVal_Object = MibTableColumn
alpineTEPowerCardPowerOutVal = _AlpineTEPowerCardPowerOutVal_Object(
    (1, 3, 6, 1, 4, 1, 52326, 2, 1, 4, 1, 9),
    _AlpineTEPowerCardPowerOutVal_Type()
)
alpineTEPowerCardPowerOutVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpineTEPowerCardPowerOutVal.setStatus("current")
if mibBuilder.loadTexts:
    alpineTEPowerCardPowerOutVal.setUnits("V")


class _AlpineTEPowerCardPowerOutStatus_Type(Integer32):
    """Custom type alpineTEPowerCardPowerOutStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AlpineTEPowerCardPowerOutStatus_Type.__name__ = "Integer32"
_AlpineTEPowerCardPowerOutStatus_Object = MibTableColumn
alpineTEPowerCardPowerOutStatus = _AlpineTEPowerCardPowerOutStatus_Object(
    (1, 3, 6, 1, 4, 1, 52326, 2, 1, 4, 1, 10),
    _AlpineTEPowerCardPowerOutStatus_Type()
)
alpineTEPowerCardPowerOutStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpineTEPowerCardPowerOutStatus.setStatus("current")
_AlpineTESystemFanTable_Object = MibTable
alpineTESystemFanTable = _AlpineTESystemFanTable_Object(
    (1, 3, 6, 1, 4, 1, 52326, 2, 1, 5)
)
if mibBuilder.loadTexts:
    alpineTESystemFanTable.setStatus("current")
_AlpineTESystemFanEntry_Object = MibTableRow
alpineTESystemFanEntry = _AlpineTESystemFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 52326, 2, 1, 5, 1)
)
alpineTESystemFanEntry.setIndexNames(
    (0, "ALPINE-TDCM-EDFA-MIB", "alpineTEFanCardId"),
)
if mibBuilder.loadTexts:
    alpineTESystemFanEntry.setStatus("current")
_AlpineTEFanCardId_Type = Integer32
_AlpineTEFanCardId_Object = MibTableColumn
alpineTEFanCardId = _AlpineTEFanCardId_Object(
    (1, 3, 6, 1, 4, 1, 52326, 2, 1, 5, 1, 1),
    _AlpineTEFanCardId_Type()
)
alpineTEFanCardId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpineTEFanCardId.setStatus("current")
_AlpineTEFanCardFansTotalCnt_Type = Integer32
_AlpineTEFanCardFansTotalCnt_Object = MibTableColumn
alpineTEFanCardFansTotalCnt = _AlpineTEFanCardFansTotalCnt_Object(
    (1, 3, 6, 1, 4, 1, 52326, 2, 1, 5, 1, 2),
    _AlpineTEFanCardFansTotalCnt_Type()
)
alpineTEFanCardFansTotalCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpineTEFanCardFansTotalCnt.setStatus("current")


class _AlpineTEFanCardHwVer_Type(OctetString):
    """Custom type alpineTEFanCardHwVer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_AlpineTEFanCardHwVer_Type.__name__ = "OctetString"
_AlpineTEFanCardHwVer_Object = MibTableColumn
alpineTEFanCardHwVer = _AlpineTEFanCardHwVer_Object(
    (1, 3, 6, 1, 4, 1, 52326, 2, 1, 5, 1, 3),
    _AlpineTEFanCardHwVer_Type()
)
alpineTEFanCardHwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpineTEFanCardHwVer.setStatus("current")


class _AlpineTEFanCardFwVer_Type(OctetString):
    """Custom type alpineTEFanCardFwVer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_AlpineTEFanCardFwVer_Type.__name__ = "OctetString"
_AlpineTEFanCardFwVer_Object = MibTableColumn
alpineTEFanCardFwVer = _AlpineTEFanCardFwVer_Object(
    (1, 3, 6, 1, 4, 1, 52326, 2, 1, 5, 1, 4),
    _AlpineTEFanCardFwVer_Type()
)
alpineTEFanCardFwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpineTEFanCardFwVer.setStatus("current")


class _AlpineTEFanCardPN_Type(OctetString):
    """Custom type alpineTEFanCardPN based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_AlpineTEFanCardPN_Type.__name__ = "OctetString"
_AlpineTEFanCardPN_Object = MibTableColumn
alpineTEFanCardPN = _AlpineTEFanCardPN_Object(
    (1, 3, 6, 1, 4, 1, 52326, 2, 1, 5, 1, 5),
    _AlpineTEFanCardPN_Type()
)
alpineTEFanCardPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpineTEFanCardPN.setStatus("current")


class _AlpineTEFanCardSN_Type(OctetString):
    """Custom type alpineTEFanCardSN based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_AlpineTEFanCardSN_Type.__name__ = "OctetString"
_AlpineTEFanCardSN_Object = MibTableColumn
alpineTEFanCardSN = _AlpineTEFanCardSN_Object(
    (1, 3, 6, 1, 4, 1, 52326, 2, 1, 5, 1, 6),
    _AlpineTEFanCardSN_Type()
)
alpineTEFanCardSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpineTEFanCardSN.setStatus("current")


class _AlpineTEFanCardManuDate_Type(OctetString):
    """Custom type alpineTEFanCardManuDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_AlpineTEFanCardManuDate_Type.__name__ = "OctetString"
_AlpineTEFanCardManuDate_Object = MibTableColumn
alpineTEFanCardManuDate = _AlpineTEFanCardManuDate_Object(
    (1, 3, 6, 1, 4, 1, 52326, 2, 1, 5, 1, 7),
    _AlpineTEFanCardManuDate_Type()
)
alpineTEFanCardManuDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpineTEFanCardManuDate.setStatus("current")


class _AlpineTEFanCardPower1Val_Type(OctetString):
    """Custom type alpineTEFanCardPower1Val based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_AlpineTEFanCardPower1Val_Type.__name__ = "OctetString"
_AlpineTEFanCardPower1Val_Object = MibTableColumn
alpineTEFanCardPower1Val = _AlpineTEFanCardPower1Val_Object(
    (1, 3, 6, 1, 4, 1, 52326, 2, 1, 5, 1, 8),
    _AlpineTEFanCardPower1Val_Type()
)
alpineTEFanCardPower1Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpineTEFanCardPower1Val.setStatus("current")
if mibBuilder.loadTexts:
    alpineTEFanCardPower1Val.setUnits("V")
_AlpineTEFanCardFan1Speed_Type = Integer32
_AlpineTEFanCardFan1Speed_Object = MibTableColumn
alpineTEFanCardFan1Speed = _AlpineTEFanCardFan1Speed_Object(
    (1, 3, 6, 1, 4, 1, 52326, 2, 1, 5, 1, 9),
    _AlpineTEFanCardFan1Speed_Type()
)
alpineTEFanCardFan1Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpineTEFanCardFan1Speed.setStatus("current")
if mibBuilder.loadTexts:
    alpineTEFanCardFan1Speed.setUnits("RPM")


class _AlpineTEFanCardFan1Status_Type(Integer32):
    """Custom type alpineTEFanCardFan1Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AlpineTEFanCardFan1Status_Type.__name__ = "Integer32"
_AlpineTEFanCardFan1Status_Object = MibTableColumn
alpineTEFanCardFan1Status = _AlpineTEFanCardFan1Status_Object(
    (1, 3, 6, 1, 4, 1, 52326, 2, 1, 5, 1, 10),
    _AlpineTEFanCardFan1Status_Type()
)
alpineTEFanCardFan1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpineTEFanCardFan1Status.setStatus("current")
_AlpineTEFanCardFan2Speed_Type = Integer32
_AlpineTEFanCardFan2Speed_Object = MibTableColumn
alpineTEFanCardFan2Speed = _AlpineTEFanCardFan2Speed_Object(
    (1, 3, 6, 1, 4, 1, 52326, 2, 1, 5, 1, 11),
    _AlpineTEFanCardFan2Speed_Type()
)
alpineTEFanCardFan2Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpineTEFanCardFan2Speed.setStatus("current")
if mibBuilder.loadTexts:
    alpineTEFanCardFan2Speed.setUnits("RPM")


class _AlpineTEFanCardFan2Status_Type(Integer32):
    """Custom type alpineTEFanCardFan2Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AlpineTEFanCardFan2Status_Type.__name__ = "Integer32"
_AlpineTEFanCardFan2Status_Object = MibTableColumn
alpineTEFanCardFan2Status = _AlpineTEFanCardFan2Status_Object(
    (1, 3, 6, 1, 4, 1, 52326, 2, 1, 5, 1, 12),
    _AlpineTEFanCardFan2Status_Type()
)
alpineTEFanCardFan2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpineTEFanCardFan2Status.setStatus("current")
_AlpineTEFanCardFan3Speed_Type = Integer32
_AlpineTEFanCardFan3Speed_Object = MibTableColumn
alpineTEFanCardFan3Speed = _AlpineTEFanCardFan3Speed_Object(
    (1, 3, 6, 1, 4, 1, 52326, 2, 1, 5, 1, 13),
    _AlpineTEFanCardFan3Speed_Type()
)
alpineTEFanCardFan3Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpineTEFanCardFan3Speed.setStatus("current")
if mibBuilder.loadTexts:
    alpineTEFanCardFan3Speed.setUnits("RPM")


class _AlpineTEFanCardFan3Status_Type(Integer32):
    """Custom type alpineTEFanCardFan3Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AlpineTEFanCardFan3Status_Type.__name__ = "Integer32"
_AlpineTEFanCardFan3Status_Object = MibTableColumn
alpineTEFanCardFan3Status = _AlpineTEFanCardFan3Status_Object(
    (1, 3, 6, 1, 4, 1, 52326, 2, 1, 5, 1, 14),
    _AlpineTEFanCardFan3Status_Type()
)
alpineTEFanCardFan3Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpineTEFanCardFan3Status.setStatus("current")

# Managed Objects groups


# Notification objects

alpineTEAlarmTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 52326, 2, 1, 3, 2)
)
alpineTEAlarmTemperature.setObjects(
    ("ALPINE-TDCM-EDFA-MIB", "alpineTEBISlotTemperature")
)
if mibBuilder.loadTexts:
    alpineTEAlarmTemperature.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALPINE-TDCM-EDFA-MIB",
    **{"alpineTdcmEdfaSystem": alpineTdcmEdfaSystem,
       "alpineTESlotBasicInfoTable": alpineTESlotBasicInfoTable,
       "alpineTESlotBasicInfoEntry": alpineTESlotBasicInfoEntry,
       "alpineTESBISlotNum": alpineTESBISlotNum,
       "alpineTESBISlotType": alpineTESBISlotType,
       "alpineTESBISlotHwVer": alpineTESBISlotHwVer,
       "alpineTESBISlotFwVer": alpineTESBISlotFwVer,
       "alpineTEBISlotPN": alpineTEBISlotPN,
       "alpineTEBISlotSN": alpineTEBISlotSN,
       "alpineTEBISlotManuDate": alpineTEBISlotManuDate,
       "alpineTEBISlotTemperature": alpineTEBISlotTemperature,
       "alpineTEBISlotPower1Status": alpineTEBISlotPower1Status,
       "alpineTEBISlotPower1Val": alpineTEBISlotPower1Val,
       "alpineTEBISlotPower2Status": alpineTEBISlotPower2Status,
       "alpineTEBISlotPower2Val": alpineTEBISlotPower2Val,
       "alpineTEBISlotPowerTotalCnt": alpineTEBISlotPowerTotalCnt,
       "alpineTESlotStatusTable": alpineTESlotStatusTable,
       "alpineTESlotStatusEntry": alpineTESlotStatusEntry,
       "alpineTESlotNum": alpineTESlotNum,
       "alpineTESlotStatus": alpineTESlotStatus,
       "alpineTEAlarm": alpineTEAlarm,
       "alpineTEAlarmThldTable": alpineTEAlarmThldTable,
       "alpineTEAlarmThldEntry": alpineTEAlarmThldEntry,
       "alpineTeatSlotNum": alpineTeatSlotNum,
       "alpineTeatTempHighAlarmThld": alpineTeatTempHighAlarmThld,
       "alpineTeatTempHighWarningThld": alpineTeatTempHighWarningThld,
       "alpineTeatTempLowAlarmThld": alpineTeatTempLowAlarmThld,
       "alpineTeatTempLowWarningThld": alpineTeatTempLowWarningThld,
       "alpineTEAlarmTemperature": alpineTEAlarmTemperature,
       "alpineTESystemPowerTable": alpineTESystemPowerTable,
       "alpineTESystemPowerEntry": alpineTESystemPowerEntry,
       "alpineTEPowerCardId": alpineTEPowerCardId,
       "alpineTEPowerCardType": alpineTEPowerCardType,
       "alpineTEPowerCardHwVer": alpineTEPowerCardHwVer,
       "alpineTEPowerCardFwVer": alpineTEPowerCardFwVer,
       "alpineTEPowerCardPN": alpineTEPowerCardPN,
       "alpineTEPowerCardSN": alpineTEPowerCardSN,
       "alpineTEPowerCardManuDate": alpineTEPowerCardManuDate,
       "alpineTEPowerCardPowerInStatus": alpineTEPowerCardPowerInStatus,
       "alpineTEPowerCardPowerOutVal": alpineTEPowerCardPowerOutVal,
       "alpineTEPowerCardPowerOutStatus": alpineTEPowerCardPowerOutStatus,
       "alpineTESystemFanTable": alpineTESystemFanTable,
       "alpineTESystemFanEntry": alpineTESystemFanEntry,
       "alpineTEFanCardId": alpineTEFanCardId,
       "alpineTEFanCardFansTotalCnt": alpineTEFanCardFansTotalCnt,
       "alpineTEFanCardHwVer": alpineTEFanCardHwVer,
       "alpineTEFanCardFwVer": alpineTEFanCardFwVer,
       "alpineTEFanCardPN": alpineTEFanCardPN,
       "alpineTEFanCardSN": alpineTEFanCardSN,
       "alpineTEFanCardManuDate": alpineTEFanCardManuDate,
       "alpineTEFanCardPower1Val": alpineTEFanCardPower1Val,
       "alpineTEFanCardFan1Speed": alpineTEFanCardFan1Speed,
       "alpineTEFanCardFan1Status": alpineTEFanCardFan1Status,
       "alpineTEFanCardFan2Speed": alpineTEFanCardFan2Speed,
       "alpineTEFanCardFan2Status": alpineTEFanCardFan2Status,
       "alpineTEFanCardFan3Speed": alpineTEFanCardFan3Speed,
       "alpineTEFanCardFan3Status": alpineTEFanCardFan3Status}
)
