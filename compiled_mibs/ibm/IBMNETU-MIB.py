# SNMP MIB module (IBMNETU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ibm\IBMNETU-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:01:06 2025
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

_Ibm_ObjectIdentity = ObjectIdentity
ibm = _Ibm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2)
)
_IbmProd_ObjectIdentity = ObjectIdentity
ibmProd = _IbmProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6)
)
_Ibmnetu_ObjectIdentity = ObjectIdentity
ibmnetu = _Ibmnetu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 150)
)
_Ibmnetuadmin_ObjectIdentity = ObjectIdentity
ibmnetuadmin = _Ibmnetuadmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 150, 1)
)
_Ibmnetuadminproducts_ObjectIdentity = ObjectIdentity
ibmnetuadminproducts = _Ibmnetuadminproducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 150, 1, 1)
)
_Ibmnetumod400_ObjectIdentity = ObjectIdentity
ibmnetumod400 = _Ibmnetumod400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 150, 1, 1, 1)
)
_IbmnetuadminOID_ObjectIdentity = ObjectIdentity
ibmnetuadminOID = _IbmnetuadminOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 150, 1, 2)
)
_IbmnetuEnetChipSet_ObjectIdentity = ObjectIdentity
ibmnetuEnetChipSet = _IbmnetuEnetChipSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 150, 1, 2, 1)
)
_EnetChipSetToshiba_ObjectIdentity = ObjectIdentity
enetChipSetToshiba = _EnetChipSetToshiba_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 150, 1, 2, 1, 1)
)
_EnetChipSetAMD_ObjectIdentity = ObjectIdentity
enetChipSetAMD = _EnetChipSetAMD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 150, 1, 2, 1, 2)
)
_IbmnetuadminDebug_ObjectIdentity = ObjectIdentity
ibmnetuadminDebug = _IbmnetuadminDebug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 150, 1, 3)
)
_Ibmnetusystem_ObjectIdentity = ObjectIdentity
ibmnetusystem = _Ibmnetusystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 150, 2)
)
_IbmnetusystemInfo_ObjectIdentity = ObjectIdentity
ibmnetusystemInfo = _IbmnetusystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 150, 2, 1)
)
_IbmnetucfgInfo_ObjectIdentity = ObjectIdentity
ibmnetucfgInfo = _IbmnetucfgInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 150, 2, 2)
)
_Ibmnetuhardware_ObjectIdentity = ObjectIdentity
ibmnetuhardware = _Ibmnetuhardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 150, 3)
)
_IbmnetuhardwareGeneral_ObjectIdentity = ObjectIdentity
ibmnetuhardwareGeneral = _IbmnetuhardwareGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 150, 3, 1)
)
_IbmnetuPCIAdapTable_Object = MibTable
ibmnetuPCIAdapTable = _IbmnetuPCIAdapTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 150, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ibmnetuPCIAdapTable.setStatus("mandatory")
_IbmnetuPCIAdapEntry_Object = MibTableRow
ibmnetuPCIAdapEntry = _IbmnetuPCIAdapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 150, 3, 1, 1, 1)
)
ibmnetuPCIAdapEntry.setIndexNames(
    (0, "IBMNETU-MIB", "ibmnetuPCIAdapSlotNum"),
)
if mibBuilder.loadTexts:
    ibmnetuPCIAdapEntry.setStatus("mandatory")


class _IbmnetuPCIAdapSlotNum_Type(Integer32):
    """Custom type ibmnetuPCIAdapSlotNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IbmnetuPCIAdapSlotNum_Type.__name__ = "Integer32"
_IbmnetuPCIAdapSlotNum_Object = MibTableColumn
ibmnetuPCIAdapSlotNum = _IbmnetuPCIAdapSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 150, 3, 1, 1, 1, 1),
    _IbmnetuPCIAdapSlotNum_Type()
)
ibmnetuPCIAdapSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmnetuPCIAdapSlotNum.setStatus("mandatory")


class _IbmnetuPCIAdapType_Type(Integer32):
    """Custom type ibmnetuPCIAdapType based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("not-present", 2),
          ("atm-mmf-lic294", 3),
          ("reserved1", 4),
          ("atm-smf-lic295", 5),
          ("reserved2", 6),
          ("token-ring-lic280", 7),
          ("escon-lic287", 8),
          ("reserved3", 9),
          ("reserved4", 10),
          ("serial-rs232-lic282", 11),
          ("serial-v35-lic290", 12),
          ("serial-x21-lic291", 13),
          ("ethernet-lic281", 14),
          ("ethernet-fast-lic288", 15),
          ("serial-hssi-lic289", 16),
          ("fddi-lic286", 17),
          ("reserved5", 18),
          ("reserved6", 19),
          ("parallel-channel-lic299", 20))
    )


_IbmnetuPCIAdapType_Type.__name__ = "Integer32"
_IbmnetuPCIAdapType_Object = MibTableColumn
ibmnetuPCIAdapType = _IbmnetuPCIAdapType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 150, 3, 1, 1, 1, 2),
    _IbmnetuPCIAdapType_Type()
)
ibmnetuPCIAdapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmnetuPCIAdapType.setStatus("mandatory")


class _IbmnetuPCIAdapOperStatus_Type(Integer32):
    """Custom type ibmnetuPCIAdapOperStatus based on Integer32"""
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
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("not-configured", 2),
          ("not-present", 3),
          ("does-not-apply", 4),
          ("enable-pending", 5),
          ("enabled", 6),
          ("disable-pending", 7),
          ("disabled", 8),
          ("not-initialized", 9),
          ("unknown-device", 10),
          ("hardware-error", 11),
          ("not-powered", 12),
          ("diagnostics", 13),
          ("wrs-available", 14),
          ("mis-configured", 15))
    )


_IbmnetuPCIAdapOperStatus_Type.__name__ = "Integer32"
_IbmnetuPCIAdapOperStatus_Object = MibTableColumn
ibmnetuPCIAdapOperStatus = _IbmnetuPCIAdapOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 150, 3, 1, 1, 1, 3),
    _IbmnetuPCIAdapOperStatus_Type()
)
ibmnetuPCIAdapOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmnetuPCIAdapOperStatus.setStatus("mandatory")
_IbmnetuGraphicTable_Object = MibTable
ibmnetuGraphicTable = _IbmnetuGraphicTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 150, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ibmnetuGraphicTable.setStatus("mandatory")
_IbmnetuGraphicEntry_Object = MibTableRow
ibmnetuGraphicEntry = _IbmnetuGraphicEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 150, 3, 1, 2, 1)
)
ibmnetuGraphicEntry.setIndexNames(
    (0, "IBMNETU-MIB", "ibmnetuGraphicSlotNum"),
    (0, "IBMNETU-MIB", "ibmnetuGraphicPortNum"),
)
if mibBuilder.loadTexts:
    ibmnetuGraphicEntry.setStatus("mandatory")
_IbmnetuGraphicSlotNum_Type = Integer32
_IbmnetuGraphicSlotNum_Object = MibTableColumn
ibmnetuGraphicSlotNum = _IbmnetuGraphicSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 150, 3, 1, 2, 1, 1),
    _IbmnetuGraphicSlotNum_Type()
)
ibmnetuGraphicSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmnetuGraphicSlotNum.setStatus("mandatory")
_IbmnetuGraphicPortNum_Type = Integer32
_IbmnetuGraphicPortNum_Object = MibTableColumn
ibmnetuGraphicPortNum = _IbmnetuGraphicPortNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 150, 3, 1, 2, 1, 2),
    _IbmnetuGraphicPortNum_Type()
)
ibmnetuGraphicPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmnetuGraphicPortNum.setStatus("mandatory")
_IbmnetuGraphicifIndex_Type = Integer32
_IbmnetuGraphicifIndex_Object = MibTableColumn
ibmnetuGraphicifIndex = _IbmnetuGraphicifIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 150, 3, 1, 2, 1, 3),
    _IbmnetuGraphicifIndex_Type()
)
ibmnetuGraphicifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmnetuGraphicifIndex.setStatus("mandatory")
_Ibmnetuhardware400Specific_ObjectIdentity = ObjectIdentity
ibmnetuhardware400Specific = _Ibmnetuhardware400Specific_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 150, 3, 2)
)
_Ibmneturouting_ObjectIdentity = ObjectIdentity
ibmneturouting = _Ibmneturouting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 150, 4)
)
_Ibmnetuswitching_ObjectIdentity = ObjectIdentity
ibmnetuswitching = _Ibmnetuswitching_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 150, 5)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IBMNETU-MIB",
    **{"ibm": ibm,
       "ibmProd": ibmProd,
       "ibmnetu": ibmnetu,
       "ibmnetuadmin": ibmnetuadmin,
       "ibmnetuadminproducts": ibmnetuadminproducts,
       "ibmnetumod400": ibmnetumod400,
       "ibmnetuadminOID": ibmnetuadminOID,
       "ibmnetuEnetChipSet": ibmnetuEnetChipSet,
       "enetChipSetToshiba": enetChipSetToshiba,
       "enetChipSetAMD": enetChipSetAMD,
       "ibmnetuadminDebug": ibmnetuadminDebug,
       "ibmnetusystem": ibmnetusystem,
       "ibmnetusystemInfo": ibmnetusystemInfo,
       "ibmnetucfgInfo": ibmnetucfgInfo,
       "ibmnetuhardware": ibmnetuhardware,
       "ibmnetuhardwareGeneral": ibmnetuhardwareGeneral,
       "ibmnetuPCIAdapTable": ibmnetuPCIAdapTable,
       "ibmnetuPCIAdapEntry": ibmnetuPCIAdapEntry,
       "ibmnetuPCIAdapSlotNum": ibmnetuPCIAdapSlotNum,
       "ibmnetuPCIAdapType": ibmnetuPCIAdapType,
       "ibmnetuPCIAdapOperStatus": ibmnetuPCIAdapOperStatus,
       "ibmnetuGraphicTable": ibmnetuGraphicTable,
       "ibmnetuGraphicEntry": ibmnetuGraphicEntry,
       "ibmnetuGraphicSlotNum": ibmnetuGraphicSlotNum,
       "ibmnetuGraphicPortNum": ibmnetuGraphicPortNum,
       "ibmnetuGraphicifIndex": ibmnetuGraphicifIndex,
       "ibmnetuhardware400Specific": ibmnetuhardware400Specific,
       "ibmneturouting": ibmneturouting,
       "ibmnetuswitching": ibmnetuswitching}
)
