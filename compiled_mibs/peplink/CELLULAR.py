# SNMP MIB module (CELLULAR) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\peplink\CELLULAR
# Produced by pysmi-1.6.2 at Thu Oct  2 12:20:39 2025
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

(DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cellularMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 12)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Peplink_ObjectIdentity = ObjectIdentity
peplink = _Peplink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23695)
)
_ProductMib_ObjectIdentity = ObjectIdentity
productMib = _ProductMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23695, 200)
)
_GeneralMib_ObjectIdentity = ObjectIdentity
generalMib = _GeneralMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1)
)
_CellularSignalInfo_ObjectIdentity = ObjectIdentity
cellularSignalInfo = _CellularSignalInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 12, 1)
)
_CellularSignalInfoTable_Object = MibTable
cellularSignalInfoTable = _CellularSignalInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 12, 1, 1)
)
if mibBuilder.loadTexts:
    cellularSignalInfoTable.setStatus("current")
_CellularSignalInfoEntry_Object = MibTableRow
cellularSignalInfoEntry = _CellularSignalInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 12, 1, 1, 1)
)
cellularSignalInfoEntry.setIndexNames(
    (0, "CELLULAR", "cellularSignalInfoId"),
)
if mibBuilder.loadTexts:
    cellularSignalInfoEntry.setStatus("current")
_CellularSignalInfoId_Type = Integer32
_CellularSignalInfoId_Object = MibTableColumn
cellularSignalInfoId = _CellularSignalInfoId_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 12, 1, 1, 1, 1),
    _CellularSignalInfoId_Type()
)
cellularSignalInfoId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularSignalInfoId.setStatus("current")
_CellularSignalInfoWanId_Type = Integer32
_CellularSignalInfoWanId_Object = MibTableColumn
cellularSignalInfoWanId = _CellularSignalInfoWanId_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 12, 1, 1, 1, 2),
    _CellularSignalInfoWanId_Type()
)
cellularSignalInfoWanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularSignalInfoWanId.setStatus("current")
_CellularSignalRssi_Type = Integer32
_CellularSignalRssi_Object = MibTableColumn
cellularSignalRssi = _CellularSignalRssi_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 12, 1, 1, 1, 3),
    _CellularSignalRssi_Type()
)
cellularSignalRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularSignalRssi.setStatus("current")
if mibBuilder.loadTexts:
    cellularSignalRssi.setUnits("dBm")
_CellularSignalSnr_Type = Integer32
_CellularSignalSnr_Object = MibTableColumn
cellularSignalSnr = _CellularSignalSnr_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 12, 1, 1, 1, 4),
    _CellularSignalSnr_Type()
)
cellularSignalSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularSignalSnr.setStatus("current")
if mibBuilder.loadTexts:
    cellularSignalSnr.setUnits("dB")
_CellularSignalSinr_Type = Integer32
_CellularSignalSinr_Object = MibTableColumn
cellularSignalSinr = _CellularSignalSinr_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 12, 1, 1, 1, 5),
    _CellularSignalSinr_Type()
)
cellularSignalSinr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularSignalSinr.setStatus("current")
if mibBuilder.loadTexts:
    cellularSignalSinr.setUnits("dB")
_CellularSignalEcio_Type = Integer32
_CellularSignalEcio_Object = MibTableColumn
cellularSignalEcio = _CellularSignalEcio_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 12, 1, 1, 1, 6),
    _CellularSignalEcio_Type()
)
cellularSignalEcio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularSignalEcio.setStatus("current")
if mibBuilder.loadTexts:
    cellularSignalEcio.setUnits("dB")
_CellularSignalRsrp_Type = Integer32
_CellularSignalRsrp_Object = MibTableColumn
cellularSignalRsrp = _CellularSignalRsrp_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 12, 1, 1, 1, 7),
    _CellularSignalRsrp_Type()
)
cellularSignalRsrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularSignalRsrp.setStatus("current")
if mibBuilder.loadTexts:
    cellularSignalRsrp.setUnits("dBm")
_CellularSignalRsrq_Type = Integer32
_CellularSignalRsrq_Object = MibTableColumn
cellularSignalRsrq = _CellularSignalRsrq_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 12, 1, 1, 1, 8),
    _CellularSignalRsrq_Type()
)
cellularSignalRsrq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularSignalRsrq.setStatus("current")
if mibBuilder.loadTexts:
    cellularSignalRsrq.setUnits("dB")
_CellularNetworkType_Type = OctetString
_CellularNetworkType_Object = MibTableColumn
cellularNetworkType = _CellularNetworkType_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 12, 1, 1, 1, 9),
    _CellularNetworkType_Type()
)
cellularNetworkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularNetworkType.setStatus("current")
_CellularBand_Type = OctetString
_CellularBand_Object = MibTableColumn
cellularBand = _CellularBand_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 12, 1, 1, 1, 10),
    _CellularBand_Type()
)
cellularBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularBand.setStatus("current")
_CellularLac_Type = Integer32
_CellularLac_Object = MibTableColumn
cellularLac = _CellularLac_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 12, 1, 1, 1, 11),
    _CellularLac_Type()
)
cellularLac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularLac.setStatus("current")
_CellularTac_Type = Integer32
_CellularTac_Object = MibTableColumn
cellularTac = _CellularTac_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 12, 1, 1, 1, 12),
    _CellularTac_Type()
)
cellularTac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularTac.setStatus("current")
_CellularENodeBId_Type = Integer32
_CellularENodeBId_Object = MibTableColumn
cellularENodeBId = _CellularENodeBId_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 12, 1, 1, 1, 13),
    _CellularENodeBId_Type()
)
cellularENodeBId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularENodeBId.setStatus("current")
_CellularIdentityInfo_ObjectIdentity = ObjectIdentity
cellularIdentityInfo = _CellularIdentityInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 12, 2)
)
_CellularIdentityInfoTable_Object = MibTable
cellularIdentityInfoTable = _CellularIdentityInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 12, 2, 1)
)
if mibBuilder.loadTexts:
    cellularIdentityInfoTable.setStatus("current")
_CellularIdentityInfoEntry_Object = MibTableRow
cellularIdentityInfoEntry = _CellularIdentityInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 12, 2, 1, 1)
)
cellularIdentityInfoEntry.setIndexNames(
    (0, "CELLULAR", "cellularIdentityInfoId"),
)
if mibBuilder.loadTexts:
    cellularIdentityInfoEntry.setStatus("current")
_CellularIdentityInfoId_Type = Integer32
_CellularIdentityInfoId_Object = MibTableColumn
cellularIdentityInfoId = _CellularIdentityInfoId_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 12, 2, 1, 1, 1),
    _CellularIdentityInfoId_Type()
)
cellularIdentityInfoId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularIdentityInfoId.setStatus("current")
_CellularIdentityInfoImei_Type = OctetString
_CellularIdentityInfoImei_Object = MibTableColumn
cellularIdentityInfoImei = _CellularIdentityInfoImei_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 12, 2, 1, 1, 2),
    _CellularIdentityInfoImei_Type()
)
cellularIdentityInfoImei.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularIdentityInfoImei.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CELLULAR",
    **{"peplink": peplink,
       "productMib": productMib,
       "generalMib": generalMib,
       "cellularMib": cellularMib,
       "cellularSignalInfo": cellularSignalInfo,
       "cellularSignalInfoTable": cellularSignalInfoTable,
       "cellularSignalInfoEntry": cellularSignalInfoEntry,
       "cellularSignalInfoId": cellularSignalInfoId,
       "cellularSignalInfoWanId": cellularSignalInfoWanId,
       "cellularSignalRssi": cellularSignalRssi,
       "cellularSignalSnr": cellularSignalSnr,
       "cellularSignalSinr": cellularSignalSinr,
       "cellularSignalEcio": cellularSignalEcio,
       "cellularSignalRsrp": cellularSignalRsrp,
       "cellularSignalRsrq": cellularSignalRsrq,
       "cellularNetworkType": cellularNetworkType,
       "cellularBand": cellularBand,
       "cellularLac": cellularLac,
       "cellularTac": cellularTac,
       "cellularENodeBId": cellularENodeBId,
       "cellularIdentityInfo": cellularIdentityInfo,
       "cellularIdentityInfoTable": cellularIdentityInfoTable,
       "cellularIdentityInfoEntry": cellularIdentityInfoEntry,
       "cellularIdentityInfoId": cellularIdentityInfoId,
       "cellularIdentityInfoImei": cellularIdentityInfoImei}
)
