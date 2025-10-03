# SNMP MIB module (ZTE-AN-OPTICAL-MODULE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\zte\ZTE-AN-OPTICAL-MODULE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:35:43 2025
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

(ifAdminStatus,
 ifIndex,
 ifOperStatus,
 ifType) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifAdminStatus",
    "ifIndex",
    "ifOperStatus",
    "ifType")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(zxAnInterface,) = mibBuilder.importSymbols(
    "ZTE-AN-SMI",
    "zxAnInterface")


# MODULE-IDENTITY

zxAnOpticalModuleMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40)
)
if mibBuilder.loadTexts:
    zxAnOpticalModuleMib.setRevisions(
        ("2011-09-13 20:00",
         "2011-09-10 11:00",
         "2011-08-23 09:00",
         "2011-05-31 15:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZxAnOpticalModuleGlobalObjects_ObjectIdentity = ObjectIdentity
zxAnOpticalModuleGlobalObjects = _ZxAnOpticalModuleGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 1)
)


class _ZxAnOpticalModuleCapabilities_Type(Bits):
    """Custom type zxAnOpticalModuleCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("opticalModuleConfClass", 0),
          ("opticalAlarmPrfUnit", 1),
          ("opticalModuleConfTechNorms", 2))
    )

_ZxAnOpticalModuleCapabilities_Type.__name__ = "Bits"
_ZxAnOpticalModuleCapabilities_Object = MibScalar
zxAnOpticalModuleCapabilities = _ZxAnOpticalModuleCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 1, 1),
    _ZxAnOpticalModuleCapabilities_Type()
)
zxAnOpticalModuleCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnOpticalModuleCapabilities.setStatus("current")


class _ZxAnOptModuleIfShutdownUnplugEn_Type(Integer32):
    """Custom type zxAnOptModuleIfShutdownUnplugEn based on Integer32"""
    defaultValue = 2

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


_ZxAnOptModuleIfShutdownUnplugEn_Type.__name__ = "Integer32"
_ZxAnOptModuleIfShutdownUnplugEn_Object = MibScalar
zxAnOptModuleIfShutdownUnplugEn = _ZxAnOptModuleIfShutdownUnplugEn_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 1, 2),
    _ZxAnOptModuleIfShutdownUnplugEn_Type()
)
zxAnOptModuleIfShutdownUnplugEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnOptModuleIfShutdownUnplugEn.setStatus("current")


class _ZxAnOptModuleFstUnpluggedRptEn_Type(Integer32):
    """Custom type zxAnOptModuleFstUnpluggedRptEn based on Integer32"""
    defaultValue = 2

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


_ZxAnOptModuleFstUnpluggedRptEn_Type.__name__ = "Integer32"
_ZxAnOptModuleFstUnpluggedRptEn_Object = MibScalar
zxAnOptModuleFstUnpluggedRptEn = _ZxAnOptModuleFstUnpluggedRptEn_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 1, 3),
    _ZxAnOptModuleFstUnpluggedRptEn_Type()
)
zxAnOptModuleFstUnpluggedRptEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnOptModuleFstUnpluggedRptEn.setStatus("current")
_ZxAnOpticalModuleObjects_ObjectIdentity = ObjectIdentity
zxAnOpticalModuleObjects = _ZxAnOpticalModuleObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2)
)
_ZxAnOpticalModuleAlmPrfTable_Object = MibTable
zxAnOpticalModuleAlmPrfTable = _ZxAnOpticalModuleAlmPrfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 2)
)
if mibBuilder.loadTexts:
    zxAnOpticalModuleAlmPrfTable.setStatus("current")
_ZxAnOpticalModuleAlmPrfEntry_Object = MibTableRow
zxAnOpticalModuleAlmPrfEntry = _ZxAnOpticalModuleAlmPrfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 2, 1)
)
zxAnOpticalModuleAlmPrfEntry.setIndexNames(
    (0, "ZTE-AN-OPTICAL-MODULE-MIB", "zxAnOpticalModuleAlmPrfName"),
)
if mibBuilder.loadTexts:
    zxAnOpticalModuleAlmPrfEntry.setStatus("current")


class _ZxAnOpticalModuleAlmPrfName_Type(DisplayString):
    """Custom type zxAnOpticalModuleAlmPrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnOpticalModuleAlmPrfName_Type.__name__ = "DisplayString"
_ZxAnOpticalModuleAlmPrfName_Object = MibTableColumn
zxAnOpticalModuleAlmPrfName = _ZxAnOpticalModuleAlmPrfName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 2, 1, 1),
    _ZxAnOpticalModuleAlmPrfName_Type()
)
zxAnOpticalModuleAlmPrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnOpticalModuleAlmPrfName.setStatus("current")
_ZxAnOpticalRxPwrLowerThresh_Type = Integer32
_ZxAnOpticalRxPwrLowerThresh_Object = MibTableColumn
zxAnOpticalRxPwrLowerThresh = _ZxAnOpticalRxPwrLowerThresh_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 2, 1, 2),
    _ZxAnOpticalRxPwrLowerThresh_Type()
)
zxAnOpticalRxPwrLowerThresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnOpticalRxPwrLowerThresh.setStatus("current")
if mibBuilder.loadTexts:
    zxAnOpticalRxPwrLowerThresh.setUnits("1dBm")
_ZxAnOpticalRxPwrUpperThresh_Type = Integer32
_ZxAnOpticalRxPwrUpperThresh_Object = MibTableColumn
zxAnOpticalRxPwrUpperThresh = _ZxAnOpticalRxPwrUpperThresh_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 2, 1, 3),
    _ZxAnOpticalRxPwrUpperThresh_Type()
)
zxAnOpticalRxPwrUpperThresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnOpticalRxPwrUpperThresh.setStatus("current")
if mibBuilder.loadTexts:
    zxAnOpticalRxPwrUpperThresh.setUnits("1dBm")
_ZxAnOpticalTxPwrLowerThresh_Type = Integer32
_ZxAnOpticalTxPwrLowerThresh_Object = MibTableColumn
zxAnOpticalTxPwrLowerThresh = _ZxAnOpticalTxPwrLowerThresh_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 2, 1, 4),
    _ZxAnOpticalTxPwrLowerThresh_Type()
)
zxAnOpticalTxPwrLowerThresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnOpticalTxPwrLowerThresh.setStatus("current")
if mibBuilder.loadTexts:
    zxAnOpticalTxPwrLowerThresh.setUnits("1dBm")
_ZxAnOpticalTxPwrUpperThresh_Type = Integer32
_ZxAnOpticalTxPwrUpperThresh_Object = MibTableColumn
zxAnOpticalTxPwrUpperThresh = _ZxAnOpticalTxPwrUpperThresh_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 2, 1, 5),
    _ZxAnOpticalTxPwrUpperThresh_Type()
)
zxAnOpticalTxPwrUpperThresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnOpticalTxPwrUpperThresh.setStatus("current")
if mibBuilder.loadTexts:
    zxAnOpticalTxPwrUpperThresh.setUnits("1dBm")


class _ZxAnOpticalBiasCurrLowerThresh_Type(Integer32):
    """Custom type zxAnOpticalBiasCurrLowerThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_ZxAnOpticalBiasCurrLowerThresh_Type.__name__ = "Integer32"
_ZxAnOpticalBiasCurrLowerThresh_Object = MibTableColumn
zxAnOpticalBiasCurrLowerThresh = _ZxAnOpticalBiasCurrLowerThresh_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 2, 1, 6),
    _ZxAnOpticalBiasCurrLowerThresh_Type()
)
zxAnOpticalBiasCurrLowerThresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnOpticalBiasCurrLowerThresh.setStatus("current")
if mibBuilder.loadTexts:
    zxAnOpticalBiasCurrLowerThresh.setUnits("1mA")


class _ZxAnOpticalBiasCurrUpperThresh_Type(Integer32):
    """Custom type zxAnOpticalBiasCurrUpperThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_ZxAnOpticalBiasCurrUpperThresh_Type.__name__ = "Integer32"
_ZxAnOpticalBiasCurrUpperThresh_Object = MibTableColumn
zxAnOpticalBiasCurrUpperThresh = _ZxAnOpticalBiasCurrUpperThresh_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 2, 1, 7),
    _ZxAnOpticalBiasCurrUpperThresh_Type()
)
zxAnOpticalBiasCurrUpperThresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnOpticalBiasCurrUpperThresh.setStatus("current")
if mibBuilder.loadTexts:
    zxAnOpticalBiasCurrUpperThresh.setUnits("1mA")


class _ZxAnOpticalVoltageLowerThresh_Type(Integer32):
    """Custom type zxAnOpticalVoltageLowerThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZxAnOpticalVoltageLowerThresh_Type.__name__ = "Integer32"
_ZxAnOpticalVoltageLowerThresh_Object = MibTableColumn
zxAnOpticalVoltageLowerThresh = _ZxAnOpticalVoltageLowerThresh_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 2, 1, 8),
    _ZxAnOpticalVoltageLowerThresh_Type()
)
zxAnOpticalVoltageLowerThresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnOpticalVoltageLowerThresh.setStatus("current")
if mibBuilder.loadTexts:
    zxAnOpticalVoltageLowerThresh.setUnits("1 Volt")


class _ZxAnOpticalVoltageUpperThresh_Type(Integer32):
    """Custom type zxAnOpticalVoltageUpperThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZxAnOpticalVoltageUpperThresh_Type.__name__ = "Integer32"
_ZxAnOpticalVoltageUpperThresh_Object = MibTableColumn
zxAnOpticalVoltageUpperThresh = _ZxAnOpticalVoltageUpperThresh_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 2, 1, 9),
    _ZxAnOpticalVoltageUpperThresh_Type()
)
zxAnOpticalVoltageUpperThresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnOpticalVoltageUpperThresh.setStatus("current")
if mibBuilder.loadTexts:
    zxAnOpticalVoltageUpperThresh.setUnits("1 Volt")


class _ZxAnOpticalTempLowerThresh_Type(Integer32):
    """Custom type zxAnOpticalTempLowerThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 100),
    )


_ZxAnOpticalTempLowerThresh_Type.__name__ = "Integer32"
_ZxAnOpticalTempLowerThresh_Object = MibTableColumn
zxAnOpticalTempLowerThresh = _ZxAnOpticalTempLowerThresh_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 2, 1, 10),
    _ZxAnOpticalTempLowerThresh_Type()
)
zxAnOpticalTempLowerThresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnOpticalTempLowerThresh.setStatus("current")
if mibBuilder.loadTexts:
    zxAnOpticalTempLowerThresh.setUnits("Centigrade")


class _ZxAnOpticalTempUpperThresh_Type(Integer32):
    """Custom type zxAnOpticalTempUpperThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 100),
    )


_ZxAnOpticalTempUpperThresh_Type.__name__ = "Integer32"
_ZxAnOpticalTempUpperThresh_Object = MibTableColumn
zxAnOpticalTempUpperThresh = _ZxAnOpticalTempUpperThresh_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 2, 1, 11),
    _ZxAnOpticalTempUpperThresh_Type()
)
zxAnOpticalTempUpperThresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnOpticalTempUpperThresh.setStatus("current")
if mibBuilder.loadTexts:
    zxAnOpticalTempUpperThresh.setUnits("Centigrade")


class _ZxAnOpticalOfflineTrapEnable_Type(Integer32):
    """Custom type zxAnOpticalOfflineTrapEnable based on Integer32"""
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


_ZxAnOpticalOfflineTrapEnable_Type.__name__ = "Integer32"
_ZxAnOpticalOfflineTrapEnable_Object = MibTableColumn
zxAnOpticalOfflineTrapEnable = _ZxAnOpticalOfflineTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 2, 1, 12),
    _ZxAnOpticalOfflineTrapEnable_Type()
)
zxAnOpticalOfflineTrapEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnOpticalOfflineTrapEnable.setStatus("current")


class _ZxAnOpticalModuleConfClass_Type(DisplayString):
    """Custom type zxAnOpticalModuleConfClass based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnOpticalModuleConfClass_Type.__name__ = "DisplayString"
_ZxAnOpticalModuleConfClass_Object = MibTableColumn
zxAnOpticalModuleConfClass = _ZxAnOpticalModuleConfClass_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 2, 1, 13),
    _ZxAnOpticalModuleConfClass_Type()
)
zxAnOpticalModuleConfClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnOpticalModuleConfClass.setStatus("current")
_ZxAnOpticalModuleAlmPrfRowStatus_Type = RowStatus
_ZxAnOpticalModuleAlmPrfRowStatus_Object = MibTableColumn
zxAnOpticalModuleAlmPrfRowStatus = _ZxAnOpticalModuleAlmPrfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 2, 1, 50),
    _ZxAnOpticalModuleAlmPrfRowStatus_Type()
)
zxAnOpticalModuleAlmPrfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnOpticalModuleAlmPrfRowStatus.setStatus("current")
_ZxAnOpticalAlmPrfIfConfTable_Object = MibTable
zxAnOpticalAlmPrfIfConfTable = _ZxAnOpticalAlmPrfIfConfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 3)
)
if mibBuilder.loadTexts:
    zxAnOpticalAlmPrfIfConfTable.setStatus("current")
_ZxAnOpticalAlmPrfIfConfEntry_Object = MibTableRow
zxAnOpticalAlmPrfIfConfEntry = _ZxAnOpticalAlmPrfIfConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 3, 1)
)
zxAnOpticalAlmPrfIfConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxAnOpticalAlmPrfIfConfEntry.setStatus("current")


class _ZxAnOpticalIfAlmPrf_Type(DisplayString):
    """Custom type zxAnOpticalIfAlmPrf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnOpticalIfAlmPrf_Type.__name__ = "DisplayString"
_ZxAnOpticalIfAlmPrf_Object = MibTableColumn
zxAnOpticalIfAlmPrf = _ZxAnOpticalIfAlmPrf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 3, 1, 2),
    _ZxAnOpticalIfAlmPrf_Type()
)
zxAnOpticalIfAlmPrf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnOpticalIfAlmPrf.setStatus("current")
_ZxAnOpticalModuleInfoTable_Object = MibTable
zxAnOpticalModuleInfoTable = _ZxAnOpticalModuleInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 4)
)
if mibBuilder.loadTexts:
    zxAnOpticalModuleInfoTable.setStatus("current")
_ZxAnOpticalModuleInfoEntry_Object = MibTableRow
zxAnOpticalModuleInfoEntry = _ZxAnOpticalModuleInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 4, 1)
)
zxAnOpticalModuleInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxAnOpticalModuleInfoEntry.setStatus("current")
_ZxAnOpticalIfRxPwrCurrValue_Type = Integer32
_ZxAnOpticalIfRxPwrCurrValue_Object = MibTableColumn
zxAnOpticalIfRxPwrCurrValue = _ZxAnOpticalIfRxPwrCurrValue_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 4, 1, 2),
    _ZxAnOpticalIfRxPwrCurrValue_Type()
)
zxAnOpticalIfRxPwrCurrValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnOpticalIfRxPwrCurrValue.setStatus("current")
if mibBuilder.loadTexts:
    zxAnOpticalIfRxPwrCurrValue.setUnits("0.001dBm")
_ZxAnOpticalIfTxPwrCurrValue_Type = Integer32
_ZxAnOpticalIfTxPwrCurrValue_Object = MibTableColumn
zxAnOpticalIfTxPwrCurrValue = _ZxAnOpticalIfTxPwrCurrValue_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 4, 1, 3),
    _ZxAnOpticalIfTxPwrCurrValue_Type()
)
zxAnOpticalIfTxPwrCurrValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnOpticalIfTxPwrCurrValue.setStatus("current")
if mibBuilder.loadTexts:
    zxAnOpticalIfTxPwrCurrValue.setUnits("0.001dBm")
_ZxAnOpticalIfRate_Type = Integer32
_ZxAnOpticalIfRate_Object = MibTableColumn
zxAnOpticalIfRate = _ZxAnOpticalIfRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 4, 1, 4),
    _ZxAnOpticalIfRate_Type()
)
zxAnOpticalIfRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnOpticalIfRate.setStatus("current")
if mibBuilder.loadTexts:
    zxAnOpticalIfRate.setUnits("0.1Gbps")
_ZxAnOpticalBiasCurrent_Type = Integer32
_ZxAnOpticalBiasCurrent_Object = MibTableColumn
zxAnOpticalBiasCurrent = _ZxAnOpticalBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 4, 1, 5),
    _ZxAnOpticalBiasCurrent_Type()
)
zxAnOpticalBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnOpticalBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    zxAnOpticalBiasCurrent.setUnits("0.001mA")
_ZxAnOpticalSupplyVoltage_Type = Integer32
_ZxAnOpticalSupplyVoltage_Object = MibTableColumn
zxAnOpticalSupplyVoltage = _ZxAnOpticalSupplyVoltage_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 4, 1, 6),
    _ZxAnOpticalSupplyVoltage_Type()
)
zxAnOpticalSupplyVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnOpticalSupplyVoltage.setStatus("current")
if mibBuilder.loadTexts:
    zxAnOpticalSupplyVoltage.setUnits("0.001 Volts")
_ZxAnOpticalWavelength_Type = Integer32
_ZxAnOpticalWavelength_Object = MibTableColumn
zxAnOpticalWavelength = _ZxAnOpticalWavelength_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 4, 1, 7),
    _ZxAnOpticalWavelength_Type()
)
zxAnOpticalWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnOpticalWavelength.setStatus("current")
if mibBuilder.loadTexts:
    zxAnOpticalWavelength.setUnits("nm")
_ZxAnOpticalTemperature_Type = Integer32
_ZxAnOpticalTemperature_Object = MibTableColumn
zxAnOpticalTemperature = _ZxAnOpticalTemperature_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 4, 1, 8),
    _ZxAnOpticalTemperature_Type()
)
zxAnOpticalTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnOpticalTemperature.setStatus("current")
if mibBuilder.loadTexts:
    zxAnOpticalTemperature.setUnits("0.001Degrees")


class _ZxAnOpticalFiberType_Type(Integer32):
    """Custom type zxAnOpticalFiberType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("singleMode", 1),
          ("multiMode", 2),
          ("unknown", 3))
    )


_ZxAnOpticalFiberType_Type.__name__ = "Integer32"
_ZxAnOpticalFiberType_Object = MibTableColumn
zxAnOpticalFiberType = _ZxAnOpticalFiberType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 4, 1, 9),
    _ZxAnOpticalFiberType_Type()
)
zxAnOpticalFiberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnOpticalFiberType.setStatus("current")


class _ZxAnOpticalVersionLevel_Type(DisplayString):
    """Custom type zxAnOpticalVersionLevel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ZxAnOpticalVersionLevel_Type.__name__ = "DisplayString"
_ZxAnOpticalVersionLevel_Object = MibTableColumn
zxAnOpticalVersionLevel = _ZxAnOpticalVersionLevel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 4, 1, 10),
    _ZxAnOpticalVersionLevel_Type()
)
zxAnOpticalVersionLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnOpticalVersionLevel.setStatus("current")


class _ZxAnOpticalVendorPn_Type(DisplayString):
    """Custom type zxAnOpticalVendorPn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnOpticalVendorPn_Type.__name__ = "DisplayString"
_ZxAnOpticalVendorPn_Object = MibTableColumn
zxAnOpticalVendorPn = _ZxAnOpticalVendorPn_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 4, 1, 11),
    _ZxAnOpticalVendorPn_Type()
)
zxAnOpticalVendorPn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnOpticalVendorPn.setStatus("current")


class _ZxAnOpticalVendorName_Type(DisplayString):
    """Custom type zxAnOpticalVendorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnOpticalVendorName_Type.__name__ = "DisplayString"
_ZxAnOpticalVendorName_Object = MibTableColumn
zxAnOpticalVendorName = _ZxAnOpticalVendorName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 4, 1, 12),
    _ZxAnOpticalVendorName_Type()
)
zxAnOpticalVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnOpticalVendorName.setStatus("current")


class _ZxAnOpticalVendorSn_Type(DisplayString):
    """Custom type zxAnOpticalVendorSn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ZxAnOpticalVendorSn_Type.__name__ = "DisplayString"
_ZxAnOpticalVendorSn_Object = MibTableColumn
zxAnOpticalVendorSn = _ZxAnOpticalVendorSn_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 4, 1, 13),
    _ZxAnOpticalVendorSn_Type()
)
zxAnOpticalVendorSn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnOpticalVendorSn.setStatus("current")


class _ZxAnOpticalProductionDate_Type(DisplayString):
    """Custom type zxAnOpticalProductionDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_ZxAnOpticalProductionDate_Type.__name__ = "DisplayString"
_ZxAnOpticalProductionDate_Object = MibTableColumn
zxAnOpticalProductionDate = _ZxAnOpticalProductionDate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 4, 1, 14),
    _ZxAnOpticalProductionDate_Type()
)
zxAnOpticalProductionDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnOpticalProductionDate.setStatus("current")


class _ZxAnOpticalModuleType_Type(DisplayString):
    """Custom type zxAnOpticalModuleType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ZxAnOpticalModuleType_Type.__name__ = "DisplayString"
_ZxAnOpticalModuleType_Object = MibTableColumn
zxAnOpticalModuleType = _ZxAnOpticalModuleType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 4, 1, 15),
    _ZxAnOpticalModuleType_Type()
)
zxAnOpticalModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnOpticalModuleType.setStatus("current")


class _ZxAnOpticalFiberInterfaceType_Type(DisplayString):
    """Custom type zxAnOpticalFiberInterfaceType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ZxAnOpticalFiberInterfaceType_Type.__name__ = "DisplayString"
_ZxAnOpticalFiberInterfaceType_Object = MibTableColumn
zxAnOpticalFiberInterfaceType = _ZxAnOpticalFiberInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 4, 1, 16),
    _ZxAnOpticalFiberInterfaceType_Type()
)
zxAnOpticalFiberInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnOpticalFiberInterfaceType.setStatus("current")


class _ZxAnOpticalMaterialNumber_Type(OctetString):
    """Custom type zxAnOpticalMaterialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ZxAnOpticalMaterialNumber_Type.__name__ = "OctetString"
_ZxAnOpticalMaterialNumber_Object = MibTableColumn
zxAnOpticalMaterialNumber = _ZxAnOpticalMaterialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 4, 1, 17),
    _ZxAnOpticalMaterialNumber_Type()
)
zxAnOpticalMaterialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnOpticalMaterialNumber.setStatus("current")


class _ZxAnOpticalRegisterData_Type(OctetString):
    """Custom type zxAnOpticalRegisterData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ZxAnOpticalRegisterData_Type.__name__ = "OctetString"
_ZxAnOpticalRegisterData_Object = MibTableColumn
zxAnOpticalRegisterData = _ZxAnOpticalRegisterData_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 4, 1, 18),
    _ZxAnOpticalRegisterData_Type()
)
zxAnOpticalRegisterData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnOpticalRegisterData.setStatus("current")


class _ZxAnOpticalOtdrSupport_Type(Integer32):
    """Custom type zxAnOpticalOtdrSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("supported", 1),
          ("unsupported", 2),
          ("unknown", 255))
    )


_ZxAnOpticalOtdrSupport_Type.__name__ = "Integer32"
_ZxAnOpticalOtdrSupport_Object = MibTableColumn
zxAnOpticalOtdrSupport = _ZxAnOpticalOtdrSupport_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 4, 1, 19),
    _ZxAnOpticalOtdrSupport_Type()
)
zxAnOpticalOtdrSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnOpticalOtdrSupport.setStatus("current")


class _ZxAnOpticalModuleActualClass_Type(DisplayString):
    """Custom type zxAnOpticalModuleActualClass based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnOpticalModuleActualClass_Type.__name__ = "DisplayString"
_ZxAnOpticalModuleActualClass_Object = MibTableColumn
zxAnOpticalModuleActualClass = _ZxAnOpticalModuleActualClass_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 4, 1, 20),
    _ZxAnOpticalModuleActualClass_Type()
)
zxAnOpticalModuleActualClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnOpticalModuleActualClass.setStatus("current")


class _ZxAnOpticalOtdrVersion_Type(DisplayString):
    """Custom type zxAnOpticalOtdrVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ZxAnOpticalOtdrVersion_Type.__name__ = "DisplayString"
_ZxAnOpticalOtdrVersion_Object = MibTableColumn
zxAnOpticalOtdrVersion = _ZxAnOpticalOtdrVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 4, 1, 21),
    _ZxAnOpticalOtdrVersion_Type()
)
zxAnOpticalOtdrVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnOpticalOtdrVersion.setStatus("current")
_ZxAnOpticalTransDistanceSmLongR_Type = Integer32
_ZxAnOpticalTransDistanceSmLongR_Object = MibTableColumn
zxAnOpticalTransDistanceSmLongR = _ZxAnOpticalTransDistanceSmLongR_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 4, 1, 40),
    _ZxAnOpticalTransDistanceSmLongR_Type()
)
zxAnOpticalTransDistanceSmLongR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnOpticalTransDistanceSmLongR.setStatus("current")
if mibBuilder.loadTexts:
    zxAnOpticalTransDistanceSmLongR.setUnits("km")
_ZxAnOpticalTransDistanceSmShortR_Type = Integer32
_ZxAnOpticalTransDistanceSmShortR_Object = MibTableColumn
zxAnOpticalTransDistanceSmShortR = _ZxAnOpticalTransDistanceSmShortR_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 4, 1, 41),
    _ZxAnOpticalTransDistanceSmShortR_Type()
)
zxAnOpticalTransDistanceSmShortR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnOpticalTransDistanceSmShortR.setStatus("current")
if mibBuilder.loadTexts:
    zxAnOpticalTransDistanceSmShortR.setUnits("100m")
_ZxAnOpticalTransDistanceOm1_Type = Integer32
_ZxAnOpticalTransDistanceOm1_Object = MibTableColumn
zxAnOpticalTransDistanceOm1 = _ZxAnOpticalTransDistanceOm1_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 4, 1, 42),
    _ZxAnOpticalTransDistanceOm1_Type()
)
zxAnOpticalTransDistanceOm1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnOpticalTransDistanceOm1.setStatus("current")
if mibBuilder.loadTexts:
    zxAnOpticalTransDistanceOm1.setUnits("10m")
_ZxAnOpticalTransDistanceOm2_Type = Integer32
_ZxAnOpticalTransDistanceOm2_Object = MibTableColumn
zxAnOpticalTransDistanceOm2 = _ZxAnOpticalTransDistanceOm2_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 4, 1, 43),
    _ZxAnOpticalTransDistanceOm2_Type()
)
zxAnOpticalTransDistanceOm2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnOpticalTransDistanceOm2.setStatus("current")
if mibBuilder.loadTexts:
    zxAnOpticalTransDistanceOm2.setUnits("10m")
_ZxAnOpticalTransDistanceOm3_Type = Integer32
_ZxAnOpticalTransDistanceOm3_Object = MibTableColumn
zxAnOpticalTransDistanceOm3 = _ZxAnOpticalTransDistanceOm3_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 4, 1, 44),
    _ZxAnOpticalTransDistanceOm3_Type()
)
zxAnOpticalTransDistanceOm3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnOpticalTransDistanceOm3.setStatus("current")
if mibBuilder.loadTexts:
    zxAnOpticalTransDistanceOm3.setUnits("10m")
_ZxAnOpticalTransDistanceCopper_Type = Integer32
_ZxAnOpticalTransDistanceCopper_Object = MibTableColumn
zxAnOpticalTransDistanceCopper = _ZxAnOpticalTransDistanceCopper_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 4, 1, 45),
    _ZxAnOpticalTransDistanceCopper_Type()
)
zxAnOpticalTransDistanceCopper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnOpticalTransDistanceCopper.setStatus("current")
if mibBuilder.loadTexts:
    zxAnOpticalTransDistanceCopper.setUnits("m")


class _ZxAnOpticalPartNumber_Type(DisplayString):
    """Custom type zxAnOpticalPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnOpticalPartNumber_Type.__name__ = "DisplayString"
_ZxAnOpticalPartNumber_Object = MibTableColumn
zxAnOpticalPartNumber = _ZxAnOpticalPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 4, 1, 48),
    _ZxAnOpticalPartNumber_Type()
)
zxAnOpticalPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnOpticalPartNumber.setStatus("current")
_ZxAnOpticalAlsIfConfTable_Object = MibTable
zxAnOpticalAlsIfConfTable = _ZxAnOpticalAlsIfConfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 5)
)
if mibBuilder.loadTexts:
    zxAnOpticalAlsIfConfTable.setStatus("current")
_ZxAnOpticalAlsIfConfEntry_Object = MibTableRow
zxAnOpticalAlsIfConfEntry = _ZxAnOpticalAlsIfConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 5, 1)
)
zxAnOpticalAlsIfConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxAnOpticalAlsIfConfEntry.setStatus("current")


class _ZxAnOptAlsEnable_Type(Integer32):
    """Custom type zxAnOptAlsEnable based on Integer32"""
    defaultValue = 2

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


_ZxAnOptAlsEnable_Type.__name__ = "Integer32"
_ZxAnOptAlsEnable_Object = MibTableColumn
zxAnOptAlsEnable = _ZxAnOptAlsEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 5, 1, 1),
    _ZxAnOptAlsEnable_Type()
)
zxAnOptAlsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnOptAlsEnable.setStatus("current")


class _ZxAnOptAlsLaserLosDuration_Type(Integer32):
    """Custom type zxAnOptAlsLaserLosDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 200000),
    )


_ZxAnOptAlsLaserLosDuration_Type.__name__ = "Integer32"
_ZxAnOptAlsLaserLosDuration_Object = MibTableColumn
zxAnOptAlsLaserLosDuration = _ZxAnOptAlsLaserLosDuration_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 5, 1, 2),
    _ZxAnOptAlsLaserLosDuration_Type()
)
zxAnOptAlsLaserLosDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnOptAlsLaserLosDuration.setStatus("current")
if mibBuilder.loadTexts:
    zxAnOptAlsLaserLosDuration.setUnits("100ms")


class _ZxAnOptAlsLaserShutdownDuration_Type(Integer32):
    """Custom type zxAnOptAlsLaserShutdownDuration based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 200000),
    )


_ZxAnOptAlsLaserShutdownDuration_Type.__name__ = "Integer32"
_ZxAnOptAlsLaserShutdownDuration_Object = MibTableColumn
zxAnOptAlsLaserShutdownDuration = _ZxAnOptAlsLaserShutdownDuration_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 5, 1, 3),
    _ZxAnOptAlsLaserShutdownDuration_Type()
)
zxAnOptAlsLaserShutdownDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnOptAlsLaserShutdownDuration.setStatus("current")
if mibBuilder.loadTexts:
    zxAnOptAlsLaserShutdownDuration.setUnits("100ms")


class _ZxAnOptAlsLaserStartUpDuration_Type(Integer32):
    """Custom type zxAnOptAlsLaserStartUpDuration based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 200000),
    )


_ZxAnOptAlsLaserStartUpDuration_Type.__name__ = "Integer32"
_ZxAnOptAlsLaserStartUpDuration_Object = MibTableColumn
zxAnOptAlsLaserStartUpDuration = _ZxAnOptAlsLaserStartUpDuration_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 5, 1, 4),
    _ZxAnOptAlsLaserStartUpDuration_Type()
)
zxAnOptAlsLaserStartUpDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnOptAlsLaserStartUpDuration.setStatus("current")
if mibBuilder.loadTexts:
    zxAnOptAlsLaserStartUpDuration.setUnits("100ms")
_ZxAnOpticalModuleConfTable_Object = MibTable
zxAnOpticalModuleConfTable = _ZxAnOpticalModuleConfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 6)
)
if mibBuilder.loadTexts:
    zxAnOpticalModuleConfTable.setStatus("current")
_ZxAnOpticalModuleConfEntry_Object = MibTableRow
zxAnOpticalModuleConfEntry = _ZxAnOpticalModuleConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 6, 1)
)
zxAnOpticalModuleConfEntry.setIndexNames(
    (0, "ZTE-AN-OPTICAL-MODULE-MIB", "zxAnOpticalModuleConfVendorName"),
    (0, "ZTE-AN-OPTICAL-MODULE-MIB", "zxAnOpticalModuleConfVendorPn"),
)
if mibBuilder.loadTexts:
    zxAnOpticalModuleConfEntry.setStatus("current")


class _ZxAnOpticalModuleConfVendorName_Type(DisplayString):
    """Custom type zxAnOpticalModuleConfVendorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnOpticalModuleConfVendorName_Type.__name__ = "DisplayString"
_ZxAnOpticalModuleConfVendorName_Object = MibTableColumn
zxAnOpticalModuleConfVendorName = _ZxAnOpticalModuleConfVendorName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 6, 1, 1),
    _ZxAnOpticalModuleConfVendorName_Type()
)
zxAnOpticalModuleConfVendorName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnOpticalModuleConfVendorName.setStatus("current")


class _ZxAnOpticalModuleConfVendorPn_Type(DisplayString):
    """Custom type zxAnOpticalModuleConfVendorPn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnOpticalModuleConfVendorPn_Type.__name__ = "DisplayString"
_ZxAnOpticalModuleConfVendorPn_Object = MibTableColumn
zxAnOpticalModuleConfVendorPn = _ZxAnOpticalModuleConfVendorPn_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 6, 1, 2),
    _ZxAnOpticalModuleConfVendorPn_Type()
)
zxAnOpticalModuleConfVendorPn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnOpticalModuleConfVendorPn.setStatus("current")


class _ZxAnOpticalModuleConfiguredClass_Type(DisplayString):
    """Custom type zxAnOpticalModuleConfiguredClass based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnOpticalModuleConfiguredClass_Type.__name__ = "DisplayString"
_ZxAnOpticalModuleConfiguredClass_Object = MibTableColumn
zxAnOpticalModuleConfiguredClass = _ZxAnOpticalModuleConfiguredClass_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 6, 1, 3),
    _ZxAnOpticalModuleConfiguredClass_Type()
)
zxAnOpticalModuleConfiguredClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnOpticalModuleConfiguredClass.setStatus("current")


class _ZxAnOpticalModuleConfProperty_Type(Integer32):
    """Custom type zxAnOpticalModuleConfProperty based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("userDefined", 2))
    )


_ZxAnOpticalModuleConfProperty_Type.__name__ = "Integer32"
_ZxAnOpticalModuleConfProperty_Object = MibTableColumn
zxAnOpticalModuleConfProperty = _ZxAnOpticalModuleConfProperty_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 6, 1, 4),
    _ZxAnOpticalModuleConfProperty_Type()
)
zxAnOpticalModuleConfProperty.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnOpticalModuleConfProperty.setStatus("current")


class _ZxAnOpticalModuleConfTechNorms_Type(DisplayString):
    """Custom type zxAnOpticalModuleConfTechNorms based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnOpticalModuleConfTechNorms_Type.__name__ = "DisplayString"
_ZxAnOpticalModuleConfTechNorms_Object = MibTableColumn
zxAnOpticalModuleConfTechNorms = _ZxAnOpticalModuleConfTechNorms_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 6, 1, 11),
    _ZxAnOpticalModuleConfTechNorms_Type()
)
zxAnOpticalModuleConfTechNorms.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnOpticalModuleConfTechNorms.setStatus("current")
_ZxAnOpticalModuleConfRowStatus_Type = RowStatus
_ZxAnOpticalModuleConfRowStatus_Object = MibTableColumn
zxAnOpticalModuleConfRowStatus = _ZxAnOpticalModuleConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 6, 1, 50),
    _ZxAnOpticalModuleConfRowStatus_Type()
)
zxAnOpticalModuleConfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnOpticalModuleConfRowStatus.setStatus("current")
_ZxAnOpticalModuleChanInfoTable_Object = MibTable
zxAnOpticalModuleChanInfoTable = _ZxAnOpticalModuleChanInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 10)
)
if mibBuilder.loadTexts:
    zxAnOpticalModuleChanInfoTable.setStatus("current")
_ZxAnOpticalModuleChanInfoEntry_Object = MibTableRow
zxAnOpticalModuleChanInfoEntry = _ZxAnOpticalModuleChanInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 10, 1)
)
zxAnOpticalModuleChanInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxAnOpticalModuleChanInfoEntry.setStatus("current")


class _ZxAnOpticalChanLaserSwitch_Type(Integer32):
    """Custom type zxAnOpticalChanLaserSwitch based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("close", 2))
    )


_ZxAnOpticalChanLaserSwitch_Type.__name__ = "Integer32"
_ZxAnOpticalChanLaserSwitch_Object = MibTableColumn
zxAnOpticalChanLaserSwitch = _ZxAnOpticalChanLaserSwitch_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 10, 1, 1),
    _ZxAnOpticalChanLaserSwitch_Type()
)
zxAnOpticalChanLaserSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnOpticalChanLaserSwitch.setStatus("current")
_ZxAnOpticalChanWavelength_Type = Integer32
_ZxAnOpticalChanWavelength_Object = MibTableColumn
zxAnOpticalChanWavelength = _ZxAnOpticalChanWavelength_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 10, 1, 2),
    _ZxAnOpticalChanWavelength_Type()
)
zxAnOpticalChanWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnOpticalChanWavelength.setStatus("current")
if mibBuilder.loadTexts:
    zxAnOpticalChanWavelength.setUnits("0.01nm")
_ZxAnOpticalChanCurrTxPwr_Type = Integer32
_ZxAnOpticalChanCurrTxPwr_Object = MibTableColumn
zxAnOpticalChanCurrTxPwr = _ZxAnOpticalChanCurrTxPwr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 10, 1, 3),
    _ZxAnOpticalChanCurrTxPwr_Type()
)
zxAnOpticalChanCurrTxPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnOpticalChanCurrTxPwr.setStatus("current")
if mibBuilder.loadTexts:
    zxAnOpticalChanCurrTxPwr.setUnits("0.001dBm")
_ZxAnOpticalChanBiasCurrent_Type = Integer32
_ZxAnOpticalChanBiasCurrent_Object = MibTableColumn
zxAnOpticalChanBiasCurrent = _ZxAnOpticalChanBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 10, 1, 4),
    _ZxAnOpticalChanBiasCurrent_Type()
)
zxAnOpticalChanBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnOpticalChanBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    zxAnOpticalChanBiasCurrent.setUnits("0.001mA")
_ZxAnOpticalModuleClassValueTable_Object = MibTable
zxAnOpticalModuleClassValueTable = _ZxAnOpticalModuleClassValueTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 20)
)
if mibBuilder.loadTexts:
    zxAnOpticalModuleClassValueTable.setStatus("current")
_ZxAnOpticalModuleClassValueEntry_Object = MibTableRow
zxAnOpticalModuleClassValueEntry = _ZxAnOpticalModuleClassValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 20, 1)
)
zxAnOpticalModuleClassValueEntry.setIndexNames(
    (0, "ZTE-AN-OPTICAL-MODULE-MIB", "zxAnOpticalModuleClassId"),
)
if mibBuilder.loadTexts:
    zxAnOpticalModuleClassValueEntry.setStatus("current")


class _ZxAnOpticalModuleClassId_Type(Integer32):
    """Custom type zxAnOpticalModuleClassId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_ZxAnOpticalModuleClassId_Type.__name__ = "Integer32"
_ZxAnOpticalModuleClassId_Object = MibTableColumn
zxAnOpticalModuleClassId = _ZxAnOpticalModuleClassId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 20, 1, 1),
    _ZxAnOpticalModuleClassId_Type()
)
zxAnOpticalModuleClassId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnOpticalModuleClassId.setStatus("current")


class _ZxAnOpticalModuleClassValue_Type(DisplayString):
    """Custom type zxAnOpticalModuleClassValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnOpticalModuleClassValue_Type.__name__ = "DisplayString"
_ZxAnOpticalModuleClassValue_Object = MibTableColumn
zxAnOpticalModuleClassValue = _ZxAnOpticalModuleClassValue_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 2, 20, 1, 2),
    _ZxAnOpticalModuleClassValue_Type()
)
zxAnOpticalModuleClassValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnOpticalModuleClassValue.setStatus("current")
_ZxAnOpticalModuleNotifications_ObjectIdentity = ObjectIdentity
zxAnOpticalModuleNotifications = _ZxAnOpticalModuleNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 3)
)
_ZxAnOpticalModuleConformance_ObjectIdentity = ObjectIdentity
zxAnOpticalModuleConformance = _ZxAnOpticalModuleConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 4)
)

# Managed Objects groups


# Notification objects

zxAnOptRxPwrUnderThreshAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 3, 1)
)
zxAnOptRxPwrUnderThreshAlm.setObjects(
      *(("ZTE-AN-OPTICAL-MODULE-MIB", "zxAnOpticalIfRxPwrCurrValue"),
        ("ZTE-AN-OPTICAL-MODULE-MIB", "zxAnOpticalRxPwrLowerThresh"))
)
if mibBuilder.loadTexts:
    zxAnOptRxPwrUnderThreshAlm.setStatus(
        "current"
    )

zxAnOptRxPwrUnderThreshClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 3, 2)
)
zxAnOptRxPwrUnderThreshClr.setObjects(
      *(("ZTE-AN-OPTICAL-MODULE-MIB", "zxAnOpticalIfRxPwrCurrValue"),
        ("ZTE-AN-OPTICAL-MODULE-MIB", "zxAnOpticalRxPwrLowerThresh"))
)
if mibBuilder.loadTexts:
    zxAnOptRxPwrUnderThreshClr.setStatus(
        "current"
    )

zxAnOptRxPwrOverThreshAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 3, 3)
)
zxAnOptRxPwrOverThreshAlm.setObjects(
      *(("ZTE-AN-OPTICAL-MODULE-MIB", "zxAnOpticalIfRxPwrCurrValue"),
        ("ZTE-AN-OPTICAL-MODULE-MIB", "zxAnOpticalRxPwrUpperThresh"))
)
if mibBuilder.loadTexts:
    zxAnOptRxPwrOverThreshAlm.setStatus(
        "current"
    )

zxAnOptRxPwrOverThreshClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 3, 4)
)
zxAnOptRxPwrOverThreshClr.setObjects(
      *(("ZTE-AN-OPTICAL-MODULE-MIB", "zxAnOpticalIfRxPwrCurrValue"),
        ("ZTE-AN-OPTICAL-MODULE-MIB", "zxAnOpticalRxPwrUpperThresh"))
)
if mibBuilder.loadTexts:
    zxAnOptRxPwrOverThreshClr.setStatus(
        "current"
    )

zxAnOptTxPwrUnderThreshAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 3, 5)
)
zxAnOptTxPwrUnderThreshAlm.setObjects(
      *(("ZTE-AN-OPTICAL-MODULE-MIB", "zxAnOpticalIfTxPwrCurrValue"),
        ("ZTE-AN-OPTICAL-MODULE-MIB", "zxAnOpticalTxPwrLowerThresh"))
)
if mibBuilder.loadTexts:
    zxAnOptTxPwrUnderThreshAlm.setStatus(
        "current"
    )

zxAnOptTxPwrUnderThreshClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 3, 6)
)
zxAnOptTxPwrUnderThreshClr.setObjects(
      *(("ZTE-AN-OPTICAL-MODULE-MIB", "zxAnOpticalIfTxPwrCurrValue"),
        ("ZTE-AN-OPTICAL-MODULE-MIB", "zxAnOpticalTxPwrLowerThresh"))
)
if mibBuilder.loadTexts:
    zxAnOptTxPwrUnderThreshClr.setStatus(
        "current"
    )

zxAnOptTxPwrOverThreshAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 3, 7)
)
zxAnOptTxPwrOverThreshAlm.setObjects(
      *(("ZTE-AN-OPTICAL-MODULE-MIB", "zxAnOpticalIfTxPwrCurrValue"),
        ("ZTE-AN-OPTICAL-MODULE-MIB", "zxAnOpticalTxPwrUpperThresh"))
)
if mibBuilder.loadTexts:
    zxAnOptTxPwrOverThreshAlm.setStatus(
        "current"
    )

zxAnOptTxPwrOverThreshClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 3, 8)
)
zxAnOptTxPwrOverThreshClr.setObjects(
      *(("ZTE-AN-OPTICAL-MODULE-MIB", "zxAnOpticalIfTxPwrCurrValue"),
        ("ZTE-AN-OPTICAL-MODULE-MIB", "zxAnOpticalTxPwrUpperThresh"))
)
if mibBuilder.loadTexts:
    zxAnOptTxPwrOverThreshClr.setStatus(
        "current"
    )

zxAnOptBiasCurrUnderThreshAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 3, 9)
)
zxAnOptBiasCurrUnderThreshAlm.setObjects(
      *(("ZTE-AN-OPTICAL-MODULE-MIB", "zxAnOpticalBiasCurrent"),
        ("ZTE-AN-OPTICAL-MODULE-MIB", "zxAnOpticalBiasCurrLowerThresh"))
)
if mibBuilder.loadTexts:
    zxAnOptBiasCurrUnderThreshAlm.setStatus(
        "current"
    )

zxAnOptBiasCurrUnderThreshClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 3, 10)
)
zxAnOptBiasCurrUnderThreshClr.setObjects(
      *(("ZTE-AN-OPTICAL-MODULE-MIB", "zxAnOpticalBiasCurrent"),
        ("ZTE-AN-OPTICAL-MODULE-MIB", "zxAnOpticalBiasCurrLowerThresh"))
)
if mibBuilder.loadTexts:
    zxAnOptBiasCurrUnderThreshClr.setStatus(
        "current"
    )

zxAnOptBiasCurrOverThreshAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 3, 11)
)
zxAnOptBiasCurrOverThreshAlm.setObjects(
      *(("ZTE-AN-OPTICAL-MODULE-MIB", "zxAnOpticalBiasCurrent"),
        ("ZTE-AN-OPTICAL-MODULE-MIB", "zxAnOpticalBiasCurrUpperThresh"))
)
if mibBuilder.loadTexts:
    zxAnOptBiasCurrOverThreshAlm.setStatus(
        "current"
    )

zxAnOptBiasCurrOverThreshClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 3, 12)
)
zxAnOptBiasCurrOverThreshClr.setObjects(
      *(("ZTE-AN-OPTICAL-MODULE-MIB", "zxAnOpticalBiasCurrent"),
        ("ZTE-AN-OPTICAL-MODULE-MIB", "zxAnOpticalBiasCurrUpperThresh"))
)
if mibBuilder.loadTexts:
    zxAnOptBiasCurrOverThreshClr.setStatus(
        "current"
    )

zxAnOptVoltageUnderThreshAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 3, 13)
)
zxAnOptVoltageUnderThreshAlm.setObjects(
      *(("ZTE-AN-OPTICAL-MODULE-MIB", "zxAnOpticalSupplyVoltage"),
        ("ZTE-AN-OPTICAL-MODULE-MIB", "zxAnOpticalVoltageLowerThresh"))
)
if mibBuilder.loadTexts:
    zxAnOptVoltageUnderThreshAlm.setStatus(
        "current"
    )

zxAnOptVoltageUnderThreshClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 3, 14)
)
zxAnOptVoltageUnderThreshClr.setObjects(
      *(("ZTE-AN-OPTICAL-MODULE-MIB", "zxAnOpticalSupplyVoltage"),
        ("ZTE-AN-OPTICAL-MODULE-MIB", "zxAnOpticalVoltageLowerThresh"))
)
if mibBuilder.loadTexts:
    zxAnOptVoltageUnderThreshClr.setStatus(
        "current"
    )

zxAnOptVoltageOverThreshAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 3, 15)
)
zxAnOptVoltageOverThreshAlm.setObjects(
      *(("ZTE-AN-OPTICAL-MODULE-MIB", "zxAnOpticalSupplyVoltage"),
        ("ZTE-AN-OPTICAL-MODULE-MIB", "zxAnOpticalVoltageUpperThresh"))
)
if mibBuilder.loadTexts:
    zxAnOptVoltageOverThreshAlm.setStatus(
        "current"
    )

zxAnOptVoltageOverThreshClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 3, 16)
)
zxAnOptVoltageOverThreshClr.setObjects(
      *(("ZTE-AN-OPTICAL-MODULE-MIB", "zxAnOpticalSupplyVoltage"),
        ("ZTE-AN-OPTICAL-MODULE-MIB", "zxAnOpticalVoltageUpperThresh"))
)
if mibBuilder.loadTexts:
    zxAnOptVoltageOverThreshClr.setStatus(
        "current"
    )

zxAnOptTempUnderThreshAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 3, 17)
)
zxAnOptTempUnderThreshAlm.setObjects(
      *(("ZTE-AN-OPTICAL-MODULE-MIB", "zxAnOpticalTemperature"),
        ("ZTE-AN-OPTICAL-MODULE-MIB", "zxAnOpticalTempLowerThresh"))
)
if mibBuilder.loadTexts:
    zxAnOptTempUnderThreshAlm.setStatus(
        "current"
    )

zxAnOptTempUnderThreshClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 3, 18)
)
zxAnOptTempUnderThreshClr.setObjects(
      *(("ZTE-AN-OPTICAL-MODULE-MIB", "zxAnOpticalTemperature"),
        ("ZTE-AN-OPTICAL-MODULE-MIB", "zxAnOpticalTempLowerThresh"))
)
if mibBuilder.loadTexts:
    zxAnOptTempUnderThreshClr.setStatus(
        "current"
    )

zxAnOptTempOverThreshAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 3, 19)
)
zxAnOptTempOverThreshAlm.setObjects(
      *(("ZTE-AN-OPTICAL-MODULE-MIB", "zxAnOpticalTemperature"),
        ("ZTE-AN-OPTICAL-MODULE-MIB", "zxAnOpticalTempUpperThresh"))
)
if mibBuilder.loadTexts:
    zxAnOptTempOverThreshAlm.setStatus(
        "current"
    )

zxAnOptTempOverThreshClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 3, 20)
)
zxAnOptTempOverThreshClr.setObjects(
      *(("ZTE-AN-OPTICAL-MODULE-MIB", "zxAnOpticalTemperature"),
        ("ZTE-AN-OPTICAL-MODULE-MIB", "zxAnOpticalTempUpperThresh"))
)
if mibBuilder.loadTexts:
    zxAnOptTempOverThreshClr.setStatus(
        "current"
    )

zxAnOpticalModuleUnpluggedAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 3, 21)
)
zxAnOpticalModuleUnpluggedAlm.setObjects(
      *(("IF-MIB", "ifAdminStatus"),
        ("IF-MIB", "ifOperStatus"),
        ("IF-MIB", "ifType"))
)
if mibBuilder.loadTexts:
    zxAnOpticalModuleUnpluggedAlm.setStatus(
        "current"
    )

zxAnOpticalModuleUnpluggedClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 3, 22)
)
zxAnOpticalModuleUnpluggedClr.setObjects(
      *(("IF-MIB", "ifAdminStatus"),
        ("IF-MIB", "ifOperStatus"),
        ("IF-MIB", "ifType"))
)
if mibBuilder.loadTexts:
    zxAnOpticalModuleUnpluggedClr.setStatus(
        "current"
    )

zxAnOptModuleClassMismatchAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 3, 23)
)
zxAnOptModuleClassMismatchAlm.setObjects(
      *(("ZTE-AN-OPTICAL-MODULE-MIB", "zxAnOpticalModuleConfClass"),
        ("ZTE-AN-OPTICAL-MODULE-MIB", "zxAnOpticalModuleActualClass"))
)
if mibBuilder.loadTexts:
    zxAnOptModuleClassMismatchAlm.setStatus(
        "current"
    )

zxAnOptModuleClassMismatchClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 3, 24)
)
zxAnOptModuleClassMismatchClr.setObjects(
      *(("ZTE-AN-OPTICAL-MODULE-MIB", "zxAnOpticalModuleConfClass"),
        ("ZTE-AN-OPTICAL-MODULE-MIB", "zxAnOpticalModuleActualClass"))
)
if mibBuilder.loadTexts:
    zxAnOptModuleClassMismatchClr.setStatus(
        "current"
    )

zxAnOptChanTxPwrUnderThreshAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 3, 51)
)
zxAnOptChanTxPwrUnderThreshAlm.setObjects(
      *(("ZTE-AN-OPTICAL-MODULE-MIB", "zxAnOpticalChanCurrTxPwr"),
        ("ZTE-AN-OPTICAL-MODULE-MIB", "zxAnOpticalTxPwrLowerThresh"))
)
if mibBuilder.loadTexts:
    zxAnOptChanTxPwrUnderThreshAlm.setStatus(
        "current"
    )

zxAnOptChanTxPwrUnderThreshClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 3, 52)
)
zxAnOptChanTxPwrUnderThreshClr.setObjects(
      *(("ZTE-AN-OPTICAL-MODULE-MIB", "zxAnOpticalChanCurrTxPwr"),
        ("ZTE-AN-OPTICAL-MODULE-MIB", "zxAnOpticalTxPwrLowerThresh"))
)
if mibBuilder.loadTexts:
    zxAnOptChanTxPwrUnderThreshClr.setStatus(
        "current"
    )

zxAnOptChanTxPwrOverThreshAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 3, 53)
)
zxAnOptChanTxPwrOverThreshAlm.setObjects(
      *(("ZTE-AN-OPTICAL-MODULE-MIB", "zxAnOpticalChanCurrTxPwr"),
        ("ZTE-AN-OPTICAL-MODULE-MIB", "zxAnOpticalTxPwrUpperThresh"))
)
if mibBuilder.loadTexts:
    zxAnOptChanTxPwrOverThreshAlm.setStatus(
        "current"
    )

zxAnOptChanTxPwrOverThreshClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 3, 54)
)
zxAnOptChanTxPwrOverThreshClr.setObjects(
      *(("ZTE-AN-OPTICAL-MODULE-MIB", "zxAnOpticalChanCurrTxPwr"),
        ("ZTE-AN-OPTICAL-MODULE-MIB", "zxAnOpticalTxPwrUpperThresh"))
)
if mibBuilder.loadTexts:
    zxAnOptChanTxPwrOverThreshClr.setStatus(
        "current"
    )

zxAnOptChanBiasUnderThreshAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 3, 55)
)
zxAnOptChanBiasUnderThreshAlm.setObjects(
      *(("ZTE-AN-OPTICAL-MODULE-MIB", "zxAnOpticalChanBiasCurrent"),
        ("ZTE-AN-OPTICAL-MODULE-MIB", "zxAnOpticalBiasCurrLowerThresh"))
)
if mibBuilder.loadTexts:
    zxAnOptChanBiasUnderThreshAlm.setStatus(
        "current"
    )

zxAnOptChanBiasUnderThreshClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 3, 56)
)
zxAnOptChanBiasUnderThreshClr.setObjects(
      *(("ZTE-AN-OPTICAL-MODULE-MIB", "zxAnOpticalChanBiasCurrent"),
        ("ZTE-AN-OPTICAL-MODULE-MIB", "zxAnOpticalBiasCurrLowerThresh"))
)
if mibBuilder.loadTexts:
    zxAnOptChanBiasUnderThreshClr.setStatus(
        "current"
    )

zxAnOptChanBiasOverThreshAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 3, 57)
)
zxAnOptChanBiasOverThreshAlm.setObjects(
      *(("ZTE-AN-OPTICAL-MODULE-MIB", "zxAnOpticalChanBiasCurrent"),
        ("ZTE-AN-OPTICAL-MODULE-MIB", "zxAnOpticalBiasCurrUpperThresh"))
)
if mibBuilder.loadTexts:
    zxAnOptChanBiasOverThreshAlm.setStatus(
        "current"
    )

zxAnOptChanBiasOverThreshClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 3, 58)
)
zxAnOptChanBiasOverThreshClr.setObjects(
      *(("ZTE-AN-OPTICAL-MODULE-MIB", "zxAnOpticalChanBiasCurrent"),
        ("ZTE-AN-OPTICAL-MODULE-MIB", "zxAnOpticalBiasCurrUpperThresh"))
)
if mibBuilder.loadTexts:
    zxAnOptChanBiasOverThreshClr.setStatus(
        "current"
    )

zxAnOptEponGponMismatchAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 3, 59)
)
zxAnOptEponGponMismatchAlm.setObjects(
    ("ZTE-AN-OPTICAL-MODULE-MIB", "zxAnOpticalModuleType")
)
if mibBuilder.loadTexts:
    zxAnOptEponGponMismatchAlm.setStatus(
        "current"
    )

zxAnOptEponGponMismatchClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30, 40, 3, 60)
)
zxAnOptEponGponMismatchClr.setObjects(
    ("ZTE-AN-OPTICAL-MODULE-MIB", "zxAnOpticalModuleType")
)
if mibBuilder.loadTexts:
    zxAnOptEponGponMismatchClr.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-OPTICAL-MODULE-MIB",
    **{"zxAnOpticalModuleMib": zxAnOpticalModuleMib,
       "zxAnOpticalModuleGlobalObjects": zxAnOpticalModuleGlobalObjects,
       "zxAnOpticalModuleCapabilities": zxAnOpticalModuleCapabilities,
       "zxAnOptModuleIfShutdownUnplugEn": zxAnOptModuleIfShutdownUnplugEn,
       "zxAnOptModuleFstUnpluggedRptEn": zxAnOptModuleFstUnpluggedRptEn,
       "zxAnOpticalModuleObjects": zxAnOpticalModuleObjects,
       "zxAnOpticalModuleAlmPrfTable": zxAnOpticalModuleAlmPrfTable,
       "zxAnOpticalModuleAlmPrfEntry": zxAnOpticalModuleAlmPrfEntry,
       "zxAnOpticalModuleAlmPrfName": zxAnOpticalModuleAlmPrfName,
       "zxAnOpticalRxPwrLowerThresh": zxAnOpticalRxPwrLowerThresh,
       "zxAnOpticalRxPwrUpperThresh": zxAnOpticalRxPwrUpperThresh,
       "zxAnOpticalTxPwrLowerThresh": zxAnOpticalTxPwrLowerThresh,
       "zxAnOpticalTxPwrUpperThresh": zxAnOpticalTxPwrUpperThresh,
       "zxAnOpticalBiasCurrLowerThresh": zxAnOpticalBiasCurrLowerThresh,
       "zxAnOpticalBiasCurrUpperThresh": zxAnOpticalBiasCurrUpperThresh,
       "zxAnOpticalVoltageLowerThresh": zxAnOpticalVoltageLowerThresh,
       "zxAnOpticalVoltageUpperThresh": zxAnOpticalVoltageUpperThresh,
       "zxAnOpticalTempLowerThresh": zxAnOpticalTempLowerThresh,
       "zxAnOpticalTempUpperThresh": zxAnOpticalTempUpperThresh,
       "zxAnOpticalOfflineTrapEnable": zxAnOpticalOfflineTrapEnable,
       "zxAnOpticalModuleConfClass": zxAnOpticalModuleConfClass,
       "zxAnOpticalModuleAlmPrfRowStatus": zxAnOpticalModuleAlmPrfRowStatus,
       "zxAnOpticalAlmPrfIfConfTable": zxAnOpticalAlmPrfIfConfTable,
       "zxAnOpticalAlmPrfIfConfEntry": zxAnOpticalAlmPrfIfConfEntry,
       "zxAnOpticalIfAlmPrf": zxAnOpticalIfAlmPrf,
       "zxAnOpticalModuleInfoTable": zxAnOpticalModuleInfoTable,
       "zxAnOpticalModuleInfoEntry": zxAnOpticalModuleInfoEntry,
       "zxAnOpticalIfRxPwrCurrValue": zxAnOpticalIfRxPwrCurrValue,
       "zxAnOpticalIfTxPwrCurrValue": zxAnOpticalIfTxPwrCurrValue,
       "zxAnOpticalIfRate": zxAnOpticalIfRate,
       "zxAnOpticalBiasCurrent": zxAnOpticalBiasCurrent,
       "zxAnOpticalSupplyVoltage": zxAnOpticalSupplyVoltage,
       "zxAnOpticalWavelength": zxAnOpticalWavelength,
       "zxAnOpticalTemperature": zxAnOpticalTemperature,
       "zxAnOpticalFiberType": zxAnOpticalFiberType,
       "zxAnOpticalVersionLevel": zxAnOpticalVersionLevel,
       "zxAnOpticalVendorPn": zxAnOpticalVendorPn,
       "zxAnOpticalVendorName": zxAnOpticalVendorName,
       "zxAnOpticalVendorSn": zxAnOpticalVendorSn,
       "zxAnOpticalProductionDate": zxAnOpticalProductionDate,
       "zxAnOpticalModuleType": zxAnOpticalModuleType,
       "zxAnOpticalFiberInterfaceType": zxAnOpticalFiberInterfaceType,
       "zxAnOpticalMaterialNumber": zxAnOpticalMaterialNumber,
       "zxAnOpticalRegisterData": zxAnOpticalRegisterData,
       "zxAnOpticalOtdrSupport": zxAnOpticalOtdrSupport,
       "zxAnOpticalModuleActualClass": zxAnOpticalModuleActualClass,
       "zxAnOpticalOtdrVersion": zxAnOpticalOtdrVersion,
       "zxAnOpticalTransDistanceSmLongR": zxAnOpticalTransDistanceSmLongR,
       "zxAnOpticalTransDistanceSmShortR": zxAnOpticalTransDistanceSmShortR,
       "zxAnOpticalTransDistanceOm1": zxAnOpticalTransDistanceOm1,
       "zxAnOpticalTransDistanceOm2": zxAnOpticalTransDistanceOm2,
       "zxAnOpticalTransDistanceOm3": zxAnOpticalTransDistanceOm3,
       "zxAnOpticalTransDistanceCopper": zxAnOpticalTransDistanceCopper,
       "zxAnOpticalPartNumber": zxAnOpticalPartNumber,
       "zxAnOpticalAlsIfConfTable": zxAnOpticalAlsIfConfTable,
       "zxAnOpticalAlsIfConfEntry": zxAnOpticalAlsIfConfEntry,
       "zxAnOptAlsEnable": zxAnOptAlsEnable,
       "zxAnOptAlsLaserLosDuration": zxAnOptAlsLaserLosDuration,
       "zxAnOptAlsLaserShutdownDuration": zxAnOptAlsLaserShutdownDuration,
       "zxAnOptAlsLaserStartUpDuration": zxAnOptAlsLaserStartUpDuration,
       "zxAnOpticalModuleConfTable": zxAnOpticalModuleConfTable,
       "zxAnOpticalModuleConfEntry": zxAnOpticalModuleConfEntry,
       "zxAnOpticalModuleConfVendorName": zxAnOpticalModuleConfVendorName,
       "zxAnOpticalModuleConfVendorPn": zxAnOpticalModuleConfVendorPn,
       "zxAnOpticalModuleConfiguredClass": zxAnOpticalModuleConfiguredClass,
       "zxAnOpticalModuleConfProperty": zxAnOpticalModuleConfProperty,
       "zxAnOpticalModuleConfTechNorms": zxAnOpticalModuleConfTechNorms,
       "zxAnOpticalModuleConfRowStatus": zxAnOpticalModuleConfRowStatus,
       "zxAnOpticalModuleChanInfoTable": zxAnOpticalModuleChanInfoTable,
       "zxAnOpticalModuleChanInfoEntry": zxAnOpticalModuleChanInfoEntry,
       "zxAnOpticalChanLaserSwitch": zxAnOpticalChanLaserSwitch,
       "zxAnOpticalChanWavelength": zxAnOpticalChanWavelength,
       "zxAnOpticalChanCurrTxPwr": zxAnOpticalChanCurrTxPwr,
       "zxAnOpticalChanBiasCurrent": zxAnOpticalChanBiasCurrent,
       "zxAnOpticalModuleClassValueTable": zxAnOpticalModuleClassValueTable,
       "zxAnOpticalModuleClassValueEntry": zxAnOpticalModuleClassValueEntry,
       "zxAnOpticalModuleClassId": zxAnOpticalModuleClassId,
       "zxAnOpticalModuleClassValue": zxAnOpticalModuleClassValue,
       "zxAnOpticalModuleNotifications": zxAnOpticalModuleNotifications,
       "zxAnOptRxPwrUnderThreshAlm": zxAnOptRxPwrUnderThreshAlm,
       "zxAnOptRxPwrUnderThreshClr": zxAnOptRxPwrUnderThreshClr,
       "zxAnOptRxPwrOverThreshAlm": zxAnOptRxPwrOverThreshAlm,
       "zxAnOptRxPwrOverThreshClr": zxAnOptRxPwrOverThreshClr,
       "zxAnOptTxPwrUnderThreshAlm": zxAnOptTxPwrUnderThreshAlm,
       "zxAnOptTxPwrUnderThreshClr": zxAnOptTxPwrUnderThreshClr,
       "zxAnOptTxPwrOverThreshAlm": zxAnOptTxPwrOverThreshAlm,
       "zxAnOptTxPwrOverThreshClr": zxAnOptTxPwrOverThreshClr,
       "zxAnOptBiasCurrUnderThreshAlm": zxAnOptBiasCurrUnderThreshAlm,
       "zxAnOptBiasCurrUnderThreshClr": zxAnOptBiasCurrUnderThreshClr,
       "zxAnOptBiasCurrOverThreshAlm": zxAnOptBiasCurrOverThreshAlm,
       "zxAnOptBiasCurrOverThreshClr": zxAnOptBiasCurrOverThreshClr,
       "zxAnOptVoltageUnderThreshAlm": zxAnOptVoltageUnderThreshAlm,
       "zxAnOptVoltageUnderThreshClr": zxAnOptVoltageUnderThreshClr,
       "zxAnOptVoltageOverThreshAlm": zxAnOptVoltageOverThreshAlm,
       "zxAnOptVoltageOverThreshClr": zxAnOptVoltageOverThreshClr,
       "zxAnOptTempUnderThreshAlm": zxAnOptTempUnderThreshAlm,
       "zxAnOptTempUnderThreshClr": zxAnOptTempUnderThreshClr,
       "zxAnOptTempOverThreshAlm": zxAnOptTempOverThreshAlm,
       "zxAnOptTempOverThreshClr": zxAnOptTempOverThreshClr,
       "zxAnOpticalModuleUnpluggedAlm": zxAnOpticalModuleUnpluggedAlm,
       "zxAnOpticalModuleUnpluggedClr": zxAnOpticalModuleUnpluggedClr,
       "zxAnOptModuleClassMismatchAlm": zxAnOptModuleClassMismatchAlm,
       "zxAnOptModuleClassMismatchClr": zxAnOptModuleClassMismatchClr,
       "zxAnOptChanTxPwrUnderThreshAlm": zxAnOptChanTxPwrUnderThreshAlm,
       "zxAnOptChanTxPwrUnderThreshClr": zxAnOptChanTxPwrUnderThreshClr,
       "zxAnOptChanTxPwrOverThreshAlm": zxAnOptChanTxPwrOverThreshAlm,
       "zxAnOptChanTxPwrOverThreshClr": zxAnOptChanTxPwrOverThreshClr,
       "zxAnOptChanBiasUnderThreshAlm": zxAnOptChanBiasUnderThreshAlm,
       "zxAnOptChanBiasUnderThreshClr": zxAnOptChanBiasUnderThreshClr,
       "zxAnOptChanBiasOverThreshAlm": zxAnOptChanBiasOverThreshAlm,
       "zxAnOptChanBiasOverThreshClr": zxAnOptChanBiasOverThreshClr,
       "zxAnOptEponGponMismatchAlm": zxAnOptEponGponMismatchAlm,
       "zxAnOptEponGponMismatchClr": zxAnOptEponGponMismatchClr,
       "zxAnOpticalModuleConformance": zxAnOpticalModuleConformance}
)
