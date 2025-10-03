# SNMP MIB module (Axos-Card-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\calix\Axos-Card-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:22:45 2025
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

(axosModules,) = mibBuilder.importSymbols(
    "CALIX-PRODUCT-MIB",
    "axosModules")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

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

axosCardModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 4)
)
if mibBuilder.loadTexts:
    axosCardModule.setRevisions(
        ("2020-10-23 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AxosCardTable_Object = MibTable
axosCardTable = _AxosCardTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 4, 1)
)
if mibBuilder.loadTexts:
    axosCardTable.setStatus("current")
_AxosCardEntry_Object = MibTableRow
axosCardEntry = _AxosCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 4, 1, 1)
)
axosCardEntry.setIndexNames(
    (0, "Axos-Card-MIB", "axosCardShelf"),
    (0, "Axos-Card-MIB", "axosCardSlot"),
)
if mibBuilder.loadTexts:
    axosCardEntry.setStatus("current")
_AxosCardShelf_Type = Integer32
_AxosCardShelf_Object = MibTableColumn
axosCardShelf = _AxosCardShelf_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 4, 1, 1, 1),
    _AxosCardShelf_Type()
)
axosCardShelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axosCardShelf.setStatus("current")
_AxosCardSlot_Type = Integer32
_AxosCardSlot_Object = MibTableColumn
axosCardSlot = _AxosCardSlot_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 4, 1, 1, 2),
    _AxosCardSlot_Type()
)
axosCardSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axosCardSlot.setStatus("current")


class _AxosCardAdminStatus_Type(Integer32):
    """Custom type axosCardAdminStatus based on Integer32"""
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
        *(("unknown", 0),
          ("enabled", 1),
          ("alarmsuppress", 2),
          ("disabled", 3))
    )


_AxosCardAdminStatus_Type.__name__ = "Integer32"
_AxosCardAdminStatus_Object = MibTableColumn
axosCardAdminStatus = _AxosCardAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 4, 1, 1, 3),
    _AxosCardAdminStatus_Type()
)
axosCardAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axosCardAdminStatus.setStatus("current")


class _AxosCardProvType_Type(Integer32):
    """Custom type axosCardProvType based on Integer32"""
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
              21,
              22,
              23)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("clx3001", 1),
          ("ng1601", 2),
          ("gp1601", 3),
          ("gp1611", 4),
          ("vdsl2r2", 5),
          ("ngpon2x4", 6),
          ("gpon8r2", 7),
          ("ge12", 8),
          ("ge24r2", 9),
          ("epon", 10),
          ("gpon", 11),
          ("eponmacsec", 12),
          ("e32ngpon", 13),
          ("asm3001", 14),
          ("gp1612", 15),
          ("xg801", 16),
          ("ce201", 17),
          ("e32xgs", 18),
          ("frwy", 19),
          ("xg3201", 21),
          ("asm5001", 22),
          ("xg1601", 23))
    )


_AxosCardProvType_Type.__name__ = "Integer32"
_AxosCardProvType_Object = MibTableColumn
axosCardProvType = _AxosCardProvType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 4, 1, 1, 4),
    _AxosCardProvType_Type()
)
axosCardProvType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axosCardProvType.setStatus("current")


class _AxosCardActualType_Type(Integer32):
    """Custom type axosCardActualType based on Integer32"""
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
              21,
              22,
              23)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("clx3001", 1),
          ("ng1601", 2),
          ("gp1601", 3),
          ("gp1611", 4),
          ("vdsl2r2", 5),
          ("ngpon2x4", 6),
          ("gpon8r2", 7),
          ("ge12", 8),
          ("ge24r2", 9),
          ("epon", 10),
          ("gpon", 11),
          ("eponmacsec", 12),
          ("e32ngpon", 13),
          ("asm3001", 14),
          ("gp1612", 15),
          ("xg801", 16),
          ("ce201", 17),
          ("e32xgs", 18),
          ("frwy", 19),
          ("xg3201", 21),
          ("asm5001", 22),
          ("xg1601", 23))
    )


_AxosCardActualType_Type.__name__ = "Integer32"
_AxosCardActualType_Object = MibTableColumn
axosCardActualType = _AxosCardActualType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 4, 1, 1, 5),
    _AxosCardActualType_Type()
)
axosCardActualType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axosCardActualType.setStatus("current")
_AxosCardSoftwareVersion_Type = OctetString
_AxosCardSoftwareVersion_Object = MibTableColumn
axosCardSoftwareVersion = _AxosCardSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 4, 1, 1, 6),
    _AxosCardSoftwareVersion_Type()
)
axosCardSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axosCardSoftwareVersion.setStatus("current")
_AxosCardSerialNumber_Type = DisplayString
_AxosCardSerialNumber_Object = MibTableColumn
axosCardSerialNumber = _AxosCardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 4, 1, 1, 7),
    _AxosCardSerialNumber_Type()
)
axosCardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axosCardSerialNumber.setStatus("current")


class _AxosCardCurrentPowerLevel_Type(Integer32):
    """Custom type axosCardCurrentPowerLevel based on Integer32"""
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
        *(("notSet", 0),
          ("powerLevelLow", 1),
          ("powerLevel2", 2),
          ("powerLevel3", 3),
          ("powerLevel4", 4),
          ("powerLevelFull", 5))
    )


_AxosCardCurrentPowerLevel_Type.__name__ = "Integer32"
_AxosCardCurrentPowerLevel_Object = MibTableColumn
axosCardCurrentPowerLevel = _AxosCardCurrentPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 4, 1, 1, 8),
    _AxosCardCurrentPowerLevel_Type()
)
axosCardCurrentPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axosCardCurrentPowerLevel.setStatus("current")
_AxosCardCleiCode_Type = OctetString
_AxosCardCleiCode_Object = MibTableColumn
axosCardCleiCode = _AxosCardCleiCode_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 4, 1, 1, 9),
    _AxosCardCleiCode_Type()
)
axosCardCleiCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axosCardCleiCode.setStatus("current")
_AxosCardPartNumber_Type = OctetString
_AxosCardPartNumber_Object = MibTableColumn
axosCardPartNumber = _AxosCardPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 4, 1, 1, 10),
    _AxosCardPartNumber_Type()
)
axosCardPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axosCardPartNumber.setStatus("current")
_AxosCardStartMacRange_Type = OctetString
_AxosCardStartMacRange_Object = MibTableColumn
axosCardStartMacRange = _AxosCardStartMacRange_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 4, 1, 1, 11),
    _AxosCardStartMacRange_Type()
)
axosCardStartMacRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axosCardStartMacRange.setStatus("current")
_AxosCardEndMacRange_Type = OctetString
_AxosCardEndMacRange_Object = MibTableColumn
axosCardEndMacRange = _AxosCardEndMacRange_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 4, 1, 1, 12),
    _AxosCardEndMacRange_Type()
)
axosCardEndMacRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axosCardEndMacRange.setStatus("current")
_AxosOltPonPortTable_Object = MibTable
axosOltPonPortTable = _AxosOltPonPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 4, 2)
)
if mibBuilder.loadTexts:
    axosOltPonPortTable.setStatus("current")
_AxosOltPonPortEntry_Object = MibTableRow
axosOltPonPortEntry = _AxosOltPonPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 4, 2, 1)
)
axosOltPonPortEntry.setIndexNames(
    (0, "Axos-Card-MIB", "axosOltPonPortIfindex"),
)
if mibBuilder.loadTexts:
    axosOltPonPortEntry.setStatus("current")
_AxosOltPonPortIfindex_Type = Integer32
_AxosOltPonPortIfindex_Object = MibTableColumn
axosOltPonPortIfindex = _AxosOltPonPortIfindex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 4, 2, 1, 1),
    _AxosOltPonPortIfindex_Type()
)
axosOltPonPortIfindex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axosOltPonPortIfindex.setStatus("current")
_AxosOltPonPortName_Type = OctetString
_AxosOltPonPortName_Object = MibTableColumn
axosOltPonPortName = _AxosOltPonPortName_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 4, 2, 1, 2),
    _AxosOltPonPortName_Type()
)
axosOltPonPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axosOltPonPortName.setStatus("current")


class _AxosOltPonPortStatus_Type(Integer32):
    """Custom type axosOltPonPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("linkUp", 1),
          ("linkDown", 2))
    )


_AxosOltPonPortStatus_Type.__name__ = "Integer32"
_AxosOltPonPortStatus_Object = MibTableColumn
axosOltPonPortStatus = _AxosOltPonPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 4, 2, 1, 3),
    _AxosOltPonPortStatus_Type()
)
axosOltPonPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axosOltPonPortStatus.setStatus("current")
_AxosOltPonPortTemperature_Type = Integer32
_AxosOltPonPortTemperature_Object = MibTableColumn
axosOltPonPortTemperature = _AxosOltPonPortTemperature_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 4, 2, 1, 4),
    _AxosOltPonPortTemperature_Type()
)
axosOltPonPortTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axosOltPonPortTemperature.setStatus("current")
_AxosOltPonPortTxBias_Type = Integer32
_AxosOltPonPortTxBias_Object = MibTableColumn
axosOltPonPortTxBias = _AxosOltPonPortTxBias_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 4, 2, 1, 5),
    _AxosOltPonPortTxBias_Type()
)
axosOltPonPortTxBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axosOltPonPortTxBias.setStatus("current")
_AxosOltPonPortTxPower_Type = Integer32
_AxosOltPonPortTxPower_Object = MibTableColumn
axosOltPonPortTxPower = _AxosOltPonPortTxPower_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 4, 2, 1, 6),
    _AxosOltPonPortTxPower_Type()
)
axosOltPonPortTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axosOltPonPortTxPower.setStatus("current")
_AxosOltPonPortRxPower_Type = Integer32
_AxosOltPonPortRxPower_Object = MibTableColumn
axosOltPonPortRxPower = _AxosOltPonPortRxPower_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 4, 2, 1, 7),
    _AxosOltPonPortRxPower_Type()
)
axosOltPonPortRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axosOltPonPortRxPower.setStatus("current")
_AxosOltPonPortVoltage_Type = Integer32
_AxosOltPonPortVoltage_Object = MibTableColumn
axosOltPonPortVoltage = _AxosOltPonPortVoltage_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 4, 2, 1, 8),
    _AxosOltPonPortVoltage_Type()
)
axosOltPonPortVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axosOltPonPortVoltage.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Axos-Card-MIB",
    **{"axosCardModule": axosCardModule,
       "axosCardTable": axosCardTable,
       "axosCardEntry": axosCardEntry,
       "axosCardShelf": axosCardShelf,
       "axosCardSlot": axosCardSlot,
       "axosCardAdminStatus": axosCardAdminStatus,
       "axosCardProvType": axosCardProvType,
       "axosCardActualType": axosCardActualType,
       "axosCardSoftwareVersion": axosCardSoftwareVersion,
       "axosCardSerialNumber": axosCardSerialNumber,
       "axosCardCurrentPowerLevel": axosCardCurrentPowerLevel,
       "axosCardCleiCode": axosCardCleiCode,
       "axosCardPartNumber": axosCardPartNumber,
       "axosCardStartMacRange": axosCardStartMacRange,
       "axosCardEndMacRange": axosCardEndMacRange,
       "axosOltPonPortTable": axosOltPonPortTable,
       "axosOltPonPortEntry": axosOltPonPortEntry,
       "axosOltPonPortIfindex": axosOltPonPortIfindex,
       "axosOltPonPortName": axosOltPonPortName,
       "axosOltPonPortStatus": axosOltPonPortStatus,
       "axosOltPonPortTemperature": axosOltPonPortTemperature,
       "axosOltPonPortTxBias": axosOltPonPortTxBias,
       "axosOltPonPortTxPower": axosOltPonPortTxPower,
       "axosOltPonPortRxPower": axosOltPonPortRxPower,
       "axosOltPonPortVoltage": axosOltPonPortVoltage}
)
