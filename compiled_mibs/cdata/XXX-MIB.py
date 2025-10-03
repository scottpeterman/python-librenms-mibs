# SNMP MIB module (XXX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cdata\XXX-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:24:07 2025
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

company = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 34592)
)
if mibBuilder.loadTexts:
    company.setRevisions(
        ("2009-03-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IpProduct_ObjectIdentity = ObjectIdentity
ipProduct = _IpProduct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1)
)
if mibBuilder.loadTexts:
    ipProduct.setStatus("current")
_Height2HU_ObjectIdentity = ObjectIdentity
height2HU = _Height2HU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1)
)
_SystemMIB_ObjectIdentity = ObjectIdentity
systemMIB = _SystemMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1)
)


class _ShelfNum_Type(Integer32):
    """Custom type shelfNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ShelfNum_Type.__name__ = "Integer32"
_ShelfNum_Object = MibScalar
shelfNum = _ShelfNum_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 1),
    _ShelfNum_Type()
)
shelfNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfNum.setStatus("current")
_ShelfTable_Object = MibTable
shelfTable = _ShelfTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    shelfTable.setStatus("current")
_ShelfEntry_Object = MibTableRow
shelfEntry = _ShelfEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 2, 1)
)
shelfEntry.setIndexNames(
    (0, "XXX-MIB", "shelfName"),
)
if mibBuilder.loadTexts:
    shelfEntry.setStatus("current")


class _ShelfName_Type(Integer32):
    """Custom type shelfName based on Integer32"""
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
        *(("master", 1),
          ("slave_1", 2),
          ("slave_2", 3),
          ("slave_3", 4))
    )


_ShelfName_Type.__name__ = "Integer32"
_ShelfName_Object = MibTableColumn
shelfName = _ShelfName_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 2, 1, 1),
    _ShelfName_Type()
)
shelfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfName.setStatus("current")


class _PsuA_Type(Integer32):
    """Custom type psuA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2),
          ("nc", 3))
    )


_PsuA_Type.__name__ = "Integer32"
_PsuA_Object = MibTableColumn
psuA = _PsuA_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 2, 1, 2),
    _PsuA_Type()
)
psuA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psuA.setStatus("current")


class _PsuB_Type(Integer32):
    """Custom type psuB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2),
          ("nc", 3))
    )


_PsuB_Type.__name__ = "Integer32"
_PsuB_Object = MibTableColumn
psuB = _PsuB_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 2, 1, 3),
    _PsuB_Type()
)
psuB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psuB.setStatus("current")


class _VolA_Type(Integer32):
    """Custom type volA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("abnormal", 2),
          ("nc", 3))
    )


_VolA_Type.__name__ = "Integer32"
_VolA_Object = MibTableColumn
volA = _VolA_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 2, 1, 4),
    _VolA_Type()
)
volA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volA.setStatus("current")


class _VolB_Type(Integer32):
    """Custom type volB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("abnormal", 2),
          ("nc", 3))
    )


_VolB_Type.__name__ = "Integer32"
_VolB_Object = MibTableColumn
volB = _VolB_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 2, 1, 5),
    _VolB_Type()
)
volB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volB.setStatus("current")


class _Fan_Type(Integer32):
    """Custom type fan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2),
          ("nc", 3))
    )


_Fan_Type.__name__ = "Integer32"
_Fan_Object = MibTableColumn
fan = _Fan_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 2, 1, 6),
    _Fan_Type()
)
fan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan.setStatus("current")
_Temperature_Type = Integer32
_Temperature_Object = MibTableColumn
temperature = _Temperature_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 2, 1, 7),
    _Temperature_Type()
)
temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature.setStatus("current")
if mibBuilder.loadTexts:
    temperature.setUnits(" °C")


class _CoCardNum_Type(Integer32):
    """Custom type coCardNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_CoCardNum_Type.__name__ = "Integer32"
_CoCardNum_Object = MibTableColumn
coCardNum = _CoCardNum_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 2, 1, 8),
    _CoCardNum_Type()
)
coCardNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coCardNum.setStatus("current")


class _RmtCardNum_Type(Integer32):
    """Custom type rmtCardNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_RmtCardNum_Type.__name__ = "Integer32"
_RmtCardNum_Object = MibTableColumn
rmtCardNum = _RmtCardNum_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 2, 1, 9),
    _RmtCardNum_Type()
)
rmtCardNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmtCardNum.setStatus("current")
_SlotObjects_ObjectIdentity = ObjectIdentity
slotObjects = _SlotObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 3)
)
_SlotTable_Object = MibTable
slotTable = _SlotTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    slotTable.setStatus("current")
_SlotEntry_Object = MibTableRow
slotEntry = _SlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 3, 1, 1)
)
slotEntry.setIndexNames(
    (0, "XXX-MIB", "shelfIdx"),
    (0, "XXX-MIB", "slotIdx"),
)
if mibBuilder.loadTexts:
    slotEntry.setStatus("current")


class _ShelfIdx_Type(Integer32):
    """Custom type shelfIdx based on Integer32"""
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
        *(("master", 1),
          ("slave_1", 2),
          ("slave_2", 3),
          ("slave_3", 4))
    )


_ShelfIdx_Type.__name__ = "Integer32"
_ShelfIdx_Object = MibTableColumn
shelfIdx = _ShelfIdx_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 3, 1, 1, 1),
    _ShelfIdx_Type()
)
shelfIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfIdx.setStatus("current")


class _SlotIdx_Type(Integer32):
    """Custom type slotIdx based on Integer32"""
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
              17)
        )
    )
    namedValues = NamedValues(
        *(("slot01", 1),
          ("slot02", 2),
          ("slot03", 3),
          ("slot04", 4),
          ("slot05", 5),
          ("slot06", 6),
          ("slot07", 7),
          ("slot08", 8),
          ("slot09", 9),
          ("slot10", 10),
          ("slot11", 11),
          ("slot12", 12),
          ("slot13", 13),
          ("slot14", 14),
          ("slot15", 15),
          ("slot16", 16),
          ("slot17", 17))
    )


_SlotIdx_Type.__name__ = "Integer32"
_SlotIdx_Object = MibTableColumn
slotIdx = _SlotIdx_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 3, 1, 1, 2),
    _SlotIdx_Type()
)
slotIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotIdx.setStatus("current")


class _CoCardType_Type(Integer32):
    """Custom type coCardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              100,
              101,
              102)
        )
    )
    namedValues = NamedValues(
        *(("no_card", 0),
          ("ip113s", 1),
          ("ip113f", 2),
          ("mc_1g_e2o", 3),
          ("mc_1g_o2o", 4),
          ("fr600f-mm", 100),
          ("fr600f-ms", 101),
          ("not-support", 102))
    )


_CoCardType_Type.__name__ = "Integer32"
_CoCardType_Object = MibTableColumn
coCardType = _CoCardType_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 3, 1, 1, 3),
    _CoCardType_Type()
)
coCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coCardType.setStatus("current")
_CoCardDesc_Type = DisplayString
_CoCardDesc_Object = MibTableColumn
coCardDesc = _CoCardDesc_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 3, 1, 1, 4),
    _CoCardDesc_Type()
)
coCardDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coCardDesc.setStatus("current")


class _RmtCardType_Type(Integer32):
    """Custom type rmtCardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              100,
              101,
              102)
        )
    )
    namedValues = NamedValues(
        *(("no_card", 0),
          ("ip113sr", 1),
          ("ip113f", 2),
          ("mc_1g_e2o", 3),
          ("mc_1g_o2o", 4),
          ("fr600f-mm", 100),
          ("fr600f-ms", 101),
          ("not-support", 102))
    )


_RmtCardType_Type.__name__ = "Integer32"
_RmtCardType_Object = MibTableColumn
rmtCardType = _RmtCardType_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 3, 1, 1, 5),
    _RmtCardType_Type()
)
rmtCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmtCardType.setStatus("current")
_RmtCardDesc_Type = DisplayString
_RmtCardDesc_Object = MibTableColumn
rmtCardDesc = _RmtCardDesc_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 3, 1, 1, 6),
    _RmtCardDesc_Type()
)
rmtCardDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmtCardDesc.setStatus("current")
_CardObjects_ObjectIdentity = ObjectIdentity
cardObjects = _CardObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4)
)
_NmuObjects_ObjectIdentity = ObjectIdentity
nmuObjects = _NmuObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 1)
)
_NmuConfig_ObjectIdentity = ObjectIdentity
nmuConfig = _NmuConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 1, 1)
)


class _NmuType_Type(Integer32):
    """Custom type nmuType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              101,
              102)
        )
    )
    namedValues = NamedValues(
        *(("fr600f-mm", 100),
          ("fr600f-ms", 101),
          ("not-support", 102))
    )


_NmuType_Type.__name__ = "Integer32"
_NmuType_Object = MibScalar
nmuType = _NmuType_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 1, 1, 1),
    _NmuType_Type()
)
nmuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmuType.setStatus("current")
_Ipaddr_Type = IpAddress
_Ipaddr_Object = MibScalar
ipaddr = _Ipaddr_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 1, 1, 2),
    _Ipaddr_Type()
)
ipaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipaddr.setStatus("current")
_Subnet_Type = IpAddress
_Subnet_Object = MibScalar
subnet = _Subnet_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 1, 1, 3),
    _Subnet_Type()
)
subnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subnet.setStatus("current")
_Gateway_Type = IpAddress
_Gateway_Object = MibScalar
gateway = _Gateway_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 1, 1, 4),
    _Gateway_Type()
)
gateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gateway.setStatus("current")
_SysContact_Type = DisplayString
_SysContact_Object = MibScalar
sysContact = _SysContact_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 1, 1, 5),
    _SysContact_Type()
)
sysContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysContact.setStatus("current")
_SysName_Type = DisplayString
_SysName_Object = MibScalar
sysName = _SysName_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 1, 1, 6),
    _SysName_Type()
)
sysName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysName.setStatus("current")
_SysLocation_Type = DisplayString
_SysLocation_Object = MibScalar
sysLocation = _SysLocation_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 1, 1, 7),
    _SysLocation_Type()
)
sysLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLocation.setStatus("current")
_TrapHost1_Type = IpAddress
_TrapHost1_Object = MibScalar
trapHost1 = _TrapHost1_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 1, 1, 8),
    _TrapHost1_Type()
)
trapHost1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapHost1.setStatus("current")
_TrapHost2_Type = IpAddress
_TrapHost2_Object = MibScalar
trapHost2 = _TrapHost2_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 1, 1, 9),
    _TrapHost2_Type()
)
trapHost2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapHost2.setStatus("current")
_TrapHost3_Type = IpAddress
_TrapHost3_Object = MibScalar
trapHost3 = _TrapHost3_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 1, 1, 10),
    _TrapHost3_Type()
)
trapHost3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapHost3.setStatus("current")
_TrapHost4_Type = IpAddress
_TrapHost4_Object = MibScalar
trapHost4 = _TrapHost4_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 1, 1, 11),
    _TrapHost4_Type()
)
trapHost4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapHost4.setStatus("current")
_McCmObjects_ObjectIdentity = ObjectIdentity
mcCmObjects = _McCmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 2)
)
_McCmTable_Object = MibTable
mcCmTable = _McCmTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    mcCmTable.setStatus("current")
_McCmEntry_Object = MibTableRow
mcCmEntry = _McCmEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 2, 1, 1)
)
mcCmEntry.setIndexNames(
    (0, "XXX-MIB", "mcShelfIdx"),
    (0, "XXX-MIB", "mcCardIdx"),
)
if mibBuilder.loadTexts:
    mcCmEntry.setStatus("current")


class _McShelfIdx_Type(Integer32):
    """Custom type mcShelfIdx based on Integer32"""
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
        *(("master", 1),
          ("slave1", 2),
          ("slave2", 3),
          ("slave3", 4))
    )


_McShelfIdx_Type.__name__ = "Integer32"
_McShelfIdx_Object = MibTableColumn
mcShelfIdx = _McShelfIdx_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 2, 1, 1, 1),
    _McShelfIdx_Type()
)
mcShelfIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcShelfIdx.setStatus("current")


class _McCardIdx_Type(Integer32):
    """Custom type mcCardIdx based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("card01", 1),
          ("card02", 2),
          ("card03", 3),
          ("card04", 4),
          ("card05", 5),
          ("card06", 6),
          ("card07", 7),
          ("card08", 8),
          ("card09", 9),
          ("card10", 10),
          ("card11", 11),
          ("card12", 12),
          ("card13", 13),
          ("card14", 14),
          ("card15", 15),
          ("card16", 16))
    )


_McCardIdx_Type.__name__ = "Integer32"
_McCardIdx_Object = MibTableColumn
mcCardIdx = _McCardIdx_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 2, 1, 1, 2),
    _McCardIdx_Type()
)
mcCardIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcCardIdx.setStatus("current")


class _McType_Type(Integer32):
    """Custom type mcType based on Integer32"""
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
        *(("ip113s", 1),
          ("ip113f", 2),
          ("mc_1g_e2o", 3),
          ("mc_1g_o2o", 4),
          ("not-support", 5))
    )


_McType_Type.__name__ = "Integer32"
_McType_Object = MibTableColumn
mcType = _McType_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 2, 1, 1, 3),
    _McType_Type()
)
mcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcType.setStatus("current")


class _McTransceiverMode_Type(Integer32):
    """Custom type mcTransceiverMode based on Integer32"""
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
        *(("bidi", 1),
          ("duplex_fiber", 2),
          ("sfp", 3),
          ("not-support", 4))
    )


_McTransceiverMode_Type.__name__ = "Integer32"
_McTransceiverMode_Object = MibTableColumn
mcTransceiverMode = _McTransceiverMode_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 2, 1, 1, 4),
    _McTransceiverMode_Type()
)
mcTransceiverMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcTransceiverMode.setStatus("current")


class _McTransceiverDist_Type(Integer32):
    """Custom type mcTransceiverDist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_McTransceiverDist_Type.__name__ = "Integer32"
_McTransceiverDist_Object = MibTableColumn
mcTransceiverDist = _McTransceiverDist_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 2, 1, 1, 5),
    _McTransceiverDist_Type()
)
mcTransceiverDist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcTransceiverDist.setStatus("current")


class _McPortState_Type(Integer32):
    """Custom type mcPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("locked", 1),
          ("unlocked", 2),
          ("not-support", 3))
    )


_McPortState_Type.__name__ = "Integer32"
_McPortState_Object = MibTableColumn
mcPortState = _McPortState_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 2, 1, 1, 6),
    _McPortState_Type()
)
mcPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcPortState.setStatus("current")


class _McTransmitMode_Type(Integer32):
    """Custom type mcTransmitMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cut-through", 1),
          ("store-forward", 2),
          ("not-support", 3))
    )


_McTransmitMode_Type.__name__ = "Integer32"
_McTransmitMode_Object = MibTableColumn
mcTransmitMode = _McTransmitMode_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 2, 1, 1, 7),
    _McTransmitMode_Type()
)
mcTransmitMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcTransmitMode.setStatus("current")


class _McCurWorkMode_Type(Integer32):
    """Custom type mcCurWorkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("m100-full", 2),
          ("m100-half", 3),
          ("m10-full", 4),
          ("m10-half", 5),
          ("m1G-full", 6),
          ("not-support", 7))
    )


_McCurWorkMode_Type.__name__ = "Integer32"
_McCurWorkMode_Object = MibTableColumn
mcCurWorkMode = _McCurWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 2, 1, 1, 8),
    _McCurWorkMode_Type()
)
mcCurWorkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcCurWorkMode.setStatus("mandatory")


class _McCfgWorkMode_Type(Integer32):
    """Custom type mcCfgWorkMode based on Integer32"""
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
        *(("mAuto", 1),
          ("m100-full", 2),
          ("m100-half", 3),
          ("m10-full", 4),
          ("m10-half", 5),
          ("m1G-full", 6),
          ("not-support", 7))
    )


_McCfgWorkMode_Type.__name__ = "Integer32"
_McCfgWorkMode_Object = MibTableColumn
mcCfgWorkMode = _McCfgWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 2, 1, 1, 9),
    _McCfgWorkMode_Type()
)
mcCfgWorkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcCfgWorkMode.setStatus("mandatory")


class _McLFPCfg_Type(Integer32):
    """Custom type mcLFPCfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2),
          ("not-support", 3))
    )


_McLFPCfg_Type.__name__ = "Integer32"
_McLFPCfg_Object = MibTableColumn
mcLFPCfg = _McLFPCfg_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 2, 1, 1, 10),
    _McLFPCfg_Type()
)
mcLFPCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcLFPCfg.setStatus("current")
_McUpStream_Type = Gauge32
_McUpStream_Object = MibTableColumn
mcUpStream = _McUpStream_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 2, 1, 1, 11),
    _McUpStream_Type()
)
mcUpStream.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcUpStream.setStatus("current")
_McDownStream_Type = Gauge32
_McDownStream_Object = MibTableColumn
mcDownStream = _McDownStream_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 2, 1, 1, 12),
    _McDownStream_Type()
)
mcDownStream.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcDownStream.setStatus("current")


class _McTxlink_Type(Integer32):
    """Custom type mcTxlink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("not-support", 3))
    )


_McTxlink_Type.__name__ = "Integer32"
_McTxlink_Object = MibTableColumn
mcTxlink = _McTxlink_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 2, 1, 1, 13),
    _McTxlink_Type()
)
mcTxlink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcTxlink.setStatus("current")


class _McFxlink_Type(Integer32):
    """Custom type mcFxlink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("not-support", 3))
    )


_McFxlink_Type.__name__ = "Integer32"
_McFxlink_Object = MibTableColumn
mcFxlink = _McFxlink_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 2, 1, 1, 14),
    _McFxlink_Type()
)
mcFxlink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcFxlink.setStatus("current")


class _McHWLFP_Type(Integer32):
    """Custom type mcHWLFP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2),
          ("not-support", 3))
    )


_McHWLFP_Type.__name__ = "Integer32"
_McHWLFP_Object = MibTableColumn
mcHWLFP = _McHWLFP_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 2, 1, 1, 15),
    _McHWLFP_Type()
)
mcHWLFP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcHWLFP.setStatus("current")


class _McHWTransmitMode_Type(Integer32):
    """Custom type mcHWTransmitMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cut-through", 1),
          ("store-forward", 2),
          ("not-support", 3))
    )


_McHWTransmitMode_Type.__name__ = "Integer32"
_McHWTransmitMode_Object = MibTableColumn
mcHWTransmitMode = _McHWTransmitMode_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 2, 1, 1, 16),
    _McHWTransmitMode_Type()
)
mcHWTransmitMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcHWTransmitMode.setStatus("current")


class _McHWWorkMode_Type(Integer32):
    """Custom type mcHWWorkMode based on Integer32"""
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
        *(("mAuto", 1),
          ("m100-full", 2),
          ("m100-half", 3),
          ("m10-full", 4),
          ("m10-half", 5),
          ("m1G-full", 6),
          ("not-support", 7))
    )


_McHWWorkMode_Type.__name__ = "Integer32"
_McHWWorkMode_Object = MibTableColumn
mcHWWorkMode = _McHWWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 2, 1, 1, 17),
    _McHWWorkMode_Type()
)
mcHWWorkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcHWWorkMode.setStatus("current")


class _McHWRmtCtrlMode_Type(Integer32):
    """Custom type mcHWRmtCtrlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2),
          ("not-support", 3))
    )


_McHWRmtCtrlMode_Type.__name__ = "Integer32"
_McHWRmtCtrlMode_Object = MibTableColumn
mcHWRmtCtrlMode = _McHWRmtCtrlMode_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 2, 1, 1, 18),
    _McHWRmtCtrlMode_Type()
)
mcHWRmtCtrlMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcHWRmtCtrlMode.setStatus("current")


class _McNtwSfpExist_Type(Integer32):
    """Custom type mcNtwSfpExist based on Integer32"""
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
        *(("inserted", 1),
          ("removed", 2),
          ("na", 3),
          ("not-support", 4))
    )


_McNtwSfpExist_Type.__name__ = "Integer32"
_McNtwSfpExist_Object = MibTableColumn
mcNtwSfpExist = _McNtwSfpExist_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 2, 1, 1, 19),
    _McNtwSfpExist_Type()
)
mcNtwSfpExist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcNtwSfpExist.setStatus("current")


class _McAccSfpExist_Type(Integer32):
    """Custom type mcAccSfpExist based on Integer32"""
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
        *(("inserted", 1),
          ("removed", 2),
          ("na", 3),
          ("not-support", 4))
    )


_McAccSfpExist_Type.__name__ = "Integer32"
_McAccSfpExist_Object = MibTableColumn
mcAccSfpExist = _McAccSfpExist_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 2, 1, 1, 20),
    _McAccSfpExist_Type()
)
mcAccSfpExist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcAccSfpExist.setStatus("current")


class _McUtility_Type(Integer32):
    """Custom type mcUtility based on Integer32"""
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
        *(("idle", 1),
          ("reset", 2),
          ("default", 3),
          ("set2hw", 4),
          ("not-support", 5))
    )


_McUtility_Type.__name__ = "Integer32"
_McUtility_Object = MibTableColumn
mcUtility = _McUtility_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 2, 1, 1, 21),
    _McUtility_Type()
)
mcUtility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcUtility.setStatus("current")


class _McRmtDetect_Type(Integer32):
    """Custom type mcRmtDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no_remote", 0),
          ("yes", 1),
          ("not-support", 2))
    )


_McRmtDetect_Type.__name__ = "Integer32"
_McRmtDetect_Object = MibTableColumn
mcRmtDetect = _McRmtDetect_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 2, 1, 1, 22),
    _McRmtDetect_Type()
)
mcRmtDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcRmtDetect.setStatus("current")


class _McRmtType_Type(Integer32):
    """Custom type mcRmtType based on Integer32"""
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
        *(("no_card", 0),
          ("ip113sr", 1),
          ("ip113f", 2),
          ("mc_1g_e2or", 3),
          ("mc_1g_o2or", 4),
          ("not-support", 5))
    )


_McRmtType_Type.__name__ = "Integer32"
_McRmtType_Object = MibTableColumn
mcRmtType = _McRmtType_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 2, 1, 1, 23),
    _McRmtType_Type()
)
mcRmtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcRmtType.setStatus("current")


class _McRmtTransmitMode_Type(Integer32):
    """Custom type mcRmtTransmitMode based on Integer32"""
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
        *(("no_card", 0),
          ("cut-through", 1),
          ("store-forward", 2),
          ("not-support", 3))
    )


_McRmtTransmitMode_Type.__name__ = "Integer32"
_McRmtTransmitMode_Object = MibTableColumn
mcRmtTransmitMode = _McRmtTransmitMode_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 2, 1, 1, 24),
    _McRmtTransmitMode_Type()
)
mcRmtTransmitMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcRmtTransmitMode.setStatus("current")


class _McRmtCurWorkMode_Type(Integer32):
    """Custom type mcRmtCurWorkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("no_card", 0),
          ("m100-full", 2),
          ("m100-half", 3),
          ("m10-full", 4),
          ("m10-half", 5),
          ("m1G-full", 6),
          ("not-support", 7))
    )


_McRmtCurWorkMode_Type.__name__ = "Integer32"
_McRmtCurWorkMode_Object = MibTableColumn
mcRmtCurWorkMode = _McRmtCurWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 2, 1, 1, 25),
    _McRmtCurWorkMode_Type()
)
mcRmtCurWorkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcRmtCurWorkMode.setStatus("mandatory")


class _McRmtCfgWorkMode_Type(Integer32):
    """Custom type mcRmtCfgWorkMode based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("no_card", 0),
          ("mAuto", 1),
          ("m100-full", 2),
          ("m100-half", 3),
          ("m10-full", 4),
          ("m10-half", 5),
          ("m1G-full", 6),
          ("not-support", 7))
    )


_McRmtCfgWorkMode_Type.__name__ = "Integer32"
_McRmtCfgWorkMode_Object = MibTableColumn
mcRmtCfgWorkMode = _McRmtCfgWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 2, 1, 1, 26),
    _McRmtCfgWorkMode_Type()
)
mcRmtCfgWorkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcRmtCfgWorkMode.setStatus("mandatory")


class _McRmtLFP_Type(Integer32):
    """Custom type mcRmtLFP based on Integer32"""
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
        *(("no_card", 0),
          ("enable", 1),
          ("disable", 2),
          ("not-support", 3))
    )


_McRmtLFP_Type.__name__ = "Integer32"
_McRmtLFP_Object = MibTableColumn
mcRmtLFP = _McRmtLFP_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 2, 1, 1, 27),
    _McRmtLFP_Type()
)
mcRmtLFP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcRmtLFP.setStatus("current")


class _McRmtTxlink_Type(Integer32):
    """Custom type mcRmtTxlink based on Integer32"""
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
        *(("no_card", 0),
          ("up", 1),
          ("down", 2),
          ("not-support", 3))
    )


_McRmtTxlink_Type.__name__ = "Integer32"
_McRmtTxlink_Object = MibTableColumn
mcRmtTxlink = _McRmtTxlink_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 2, 1, 1, 28),
    _McRmtTxlink_Type()
)
mcRmtTxlink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcRmtTxlink.setStatus("current")


class _McRmtHWLFP_Type(Integer32):
    """Custom type mcRmtHWLFP based on Integer32"""
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
        *(("no_card", 0),
          ("enable", 1),
          ("disable", 2),
          ("not-support", 3))
    )


_McRmtHWLFP_Type.__name__ = "Integer32"
_McRmtHWLFP_Object = MibTableColumn
mcRmtHWLFP = _McRmtHWLFP_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 2, 1, 1, 29),
    _McRmtHWLFP_Type()
)
mcRmtHWLFP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcRmtHWLFP.setStatus("current")


class _McRmtHWTransmitMode_Type(Integer32):
    """Custom type mcRmtHWTransmitMode based on Integer32"""
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
        *(("no_card", 0),
          ("cut-through", 1),
          ("store-forward", 2),
          ("not-support", 3))
    )


_McRmtHWTransmitMode_Type.__name__ = "Integer32"
_McRmtHWTransmitMode_Object = MibTableColumn
mcRmtHWTransmitMode = _McRmtHWTransmitMode_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 2, 1, 1, 30),
    _McRmtHWTransmitMode_Type()
)
mcRmtHWTransmitMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcRmtHWTransmitMode.setStatus("current")


class _McRmtHWWorkMode_Type(Integer32):
    """Custom type mcRmtHWWorkMode based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("no_card", 0),
          ("mAuto", 1),
          ("m100-full", 2),
          ("m100-half", 3),
          ("m10-full", 4),
          ("m10-half", 5),
          ("m1G-full", 6),
          ("not-support", 7))
    )


_McRmtHWWorkMode_Type.__name__ = "Integer32"
_McRmtHWWorkMode_Object = MibTableColumn
mcRmtHWWorkMode = _McRmtHWWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 2, 1, 1, 31),
    _McRmtHWWorkMode_Type()
)
mcRmtHWWorkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcRmtHWWorkMode.setStatus("current")


class _McRmtLoopback_Type(Integer32):
    """Custom type mcRmtLoopback based on Integer32"""
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
        *(("no_card", 0),
          ("enable", 1),
          ("disable", 2),
          ("not-support", 3))
    )


_McRmtLoopback_Type.__name__ = "Integer32"
_McRmtLoopback_Object = MibTableColumn
mcRmtLoopback = _McRmtLoopback_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 2, 1, 1, 32),
    _McRmtLoopback_Type()
)
mcRmtLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcRmtLoopback.setStatus("current")


class _McRmtPwrDown_Type(Integer32):
    """Custom type mcRmtPwrDown based on Integer32"""
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
        *(("no_card", 0),
          ("powerdown", 1),
          ("normal", 2),
          ("not-support", 3))
    )


_McRmtPwrDown_Type.__name__ = "Integer32"
_McRmtPwrDown_Object = MibTableColumn
mcRmtPwrDown = _McRmtPwrDown_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 2, 1, 1, 33),
    _McRmtPwrDown_Type()
)
mcRmtPwrDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcRmtPwrDown.setStatus("current")


class _McRmtAccSfpExist_Type(Integer32):
    """Custom type mcRmtAccSfpExist based on Integer32"""
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
        *(("no_card", 0),
          ("inserted", 1),
          ("removed", 2),
          ("na", 3),
          ("support", 4))
    )


_McRmtAccSfpExist_Type.__name__ = "Integer32"
_McRmtAccSfpExist_Object = MibTableColumn
mcRmtAccSfpExist = _McRmtAccSfpExist_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 2, 1, 1, 34),
    _McRmtAccSfpExist_Type()
)
mcRmtAccSfpExist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcRmtAccSfpExist.setStatus("current")


class _McRmtUtility_Type(Integer32):
    """Custom type mcRmtUtility based on Integer32"""
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
        *(("no_card", 0),
          ("idle", 1),
          ("reset", 2),
          ("default", 3),
          ("set2hw", 4),
          ("not-support", 5))
    )


_McRmtUtility_Type.__name__ = "Integer32"
_McRmtUtility_Object = MibTableColumn
mcRmtUtility = _McRmtUtility_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 2, 1, 1, 35),
    _McRmtUtility_Type()
)
mcRmtUtility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcRmtUtility.setStatus("current")
_McCm1gSpecificObjects_ObjectIdentity = ObjectIdentity
mcCm1gSpecificObjects = _McCm1gSpecificObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 2, 2)
)
_McCm1gIpObjects_ObjectIdentity = ObjectIdentity
mcCm1gIpObjects = _McCm1gIpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 2, 2, 1)
)
_McCm1gIpTable_Object = MibTable
mcCm1gIpTable = _McCm1gIpTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    mcCm1gIpTable.setStatus("current")
_McCm1gIpEntry_Object = MibTableRow
mcCm1gIpEntry = _McCm1gIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 2, 2, 1, 1, 1)
)
mcCm1gIpEntry.setIndexNames(
    (0, "XXX-MIB", "mcShelfIdx"),
    (0, "XXX-MIB", "mcCardIdx"),
    (0, "XXX-MIB", "mcLoOrRmtFg"),
)
if mibBuilder.loadTexts:
    mcCm1gIpEntry.setStatus("current")


class _McLoOrRmtFg_Type(Integer32):
    """Custom type mcLoOrRmtFg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_McLoOrRmtFg_Type.__name__ = "Integer32"
_McLoOrRmtFg_Object = MibTableColumn
mcLoOrRmtFg = _McLoOrRmtFg_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 2, 2, 1, 1, 1, 1),
    _McLoOrRmtFg_Type()
)
mcLoOrRmtFg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcLoOrRmtFg.setStatus("current")
_McIpAddr_Type = IpAddress
_McIpAddr_Object = MibTableColumn
mcIpAddr = _McIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 2, 2, 1, 1, 1, 2),
    _McIpAddr_Type()
)
mcIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcIpAddr.setStatus("current")
_McCm1gSfpObjects_ObjectIdentity = ObjectIdentity
mcCm1gSfpObjects = _McCm1gSfpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 2, 2, 2)
)
_McCm1gSfpTable_Object = MibTable
mcCm1gSfpTable = _McCm1gSfpTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mcCm1gSfpTable.setStatus("current")
_McCm1gSfpEntry_Object = MibTableRow
mcCm1gSfpEntry = _McCm1gSfpEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 2, 2, 2, 1, 1)
)
mcCm1gSfpEntry.setIndexNames(
    (0, "XXX-MIB", "mcShelfIdx"),
    (0, "XXX-MIB", "mcCardIdx"),
    (0, "XXX-MIB", "mcLoOrRmtFg"),
)
if mibBuilder.loadTexts:
    mcCm1gSfpEntry.setStatus("current")


class _GetSfpCmd_Type(Integer32):
    """Custom type getSfpCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("local", 1),
          ("remote", 2))
    )


_GetSfpCmd_Type.__name__ = "Integer32"
_GetSfpCmd_Object = MibTableColumn
getSfpCmd = _GetSfpCmd_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 2, 2, 2, 1, 1, 1),
    _GetSfpCmd_Type()
)
getSfpCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    getSfpCmd.setStatus("current")
_SfpCompliance_Type = Integer32
_SfpCompliance_Object = MibTableColumn
sfpCompliance = _SfpCompliance_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 2, 2, 2, 1, 1, 2),
    _SfpCompliance_Type()
)
sfpCompliance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpCompliance.setStatus("current")
_SfpConnector_Type = Integer32
_SfpConnector_Object = MibTableColumn
sfpConnector = _SfpConnector_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 2, 2, 2, 1, 1, 3),
    _SfpConnector_Type()
)
sfpConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConnector.setStatus("current")
_SfpTransCode_Type = Integer32
_SfpTransCode_Object = MibTableColumn
sfpTransCode = _SfpTransCode_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 2, 2, 2, 1, 1, 4),
    _SfpTransCode_Type()
)
sfpTransCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpTransCode.setStatus("current")
_SfpSmLength_Type = Integer32
_SfpSmLength_Object = MibTableColumn
sfpSmLength = _SfpSmLength_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 2, 2, 2, 1, 1, 5),
    _SfpSmLength_Type()
)
sfpSmLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpSmLength.setStatus("current")
_SfpMmLength_Type = Integer32
_SfpMmLength_Object = MibTableColumn
sfpMmLength = _SfpMmLength_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 2, 2, 2, 1, 1, 6),
    _SfpMmLength_Type()
)
sfpMmLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpMmLength.setStatus("current")
_SfpCopperLength_Type = Integer32
_SfpCopperLength_Object = MibTableColumn
sfpCopperLength = _SfpCopperLength_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 2, 2, 2, 1, 1, 7),
    _SfpCopperLength_Type()
)
sfpCopperLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpCopperLength.setStatus("current")
_SfpBrSpeed_Type = Integer32
_SfpBrSpeed_Object = MibTableColumn
sfpBrSpeed = _SfpBrSpeed_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 2, 2, 2, 1, 1, 8),
    _SfpBrSpeed_Type()
)
sfpBrSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpBrSpeed.setStatus("current")
_SfpWavelength_Type = Integer32
_SfpWavelength_Object = MibTableColumn
sfpWavelength = _SfpWavelength_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 2, 2, 2, 1, 1, 9),
    _SfpWavelength_Type()
)
sfpWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpWavelength.setStatus("current")
_SfpTemperature_Type = Integer32
_SfpTemperature_Object = MibTableColumn
sfpTemperature = _SfpTemperature_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 2, 2, 2, 1, 1, 10),
    _SfpTemperature_Type()
)
sfpTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpTemperature.setStatus("current")
_SfpTranPower_Type = Integer32
_SfpTranPower_Object = MibTableColumn
sfpTranPower = _SfpTranPower_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 2, 2, 2, 1, 1, 11),
    _SfpTranPower_Type()
)
sfpTranPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpTranPower.setStatus("current")
_SfpRecvPower_Type = Integer32
_SfpRecvPower_Object = MibTableColumn
sfpRecvPower = _SfpRecvPower_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 2, 2, 2, 1, 1, 12),
    _SfpRecvPower_Type()
)
sfpRecvPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpRecvPower.setStatus("current")
_SfpVoltage_Type = Integer32
_SfpVoltage_Object = MibTableColumn
sfpVoltage = _SfpVoltage_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 2, 2, 2, 1, 1, 13),
    _SfpVoltage_Type()
)
sfpVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpVoltage.setStatus("current")
_McPmObjects_ObjectIdentity = ObjectIdentity
mcPmObjects = _McPmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 3)
)
_McPmTable_Object = MibTable
mcPmTable = _McPmTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 3, 1)
)
if mibBuilder.loadTexts:
    mcPmTable.setStatus("current")
_McPmEntry_Object = MibTableRow
mcPmEntry = _McPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 3, 1, 1)
)
mcPmEntry.setIndexNames(
    (0, "XXX-MIB", "mcShelfIdx"),
    (0, "XXX-MIB", "mcCardIdx"),
)
if mibBuilder.loadTexts:
    mcPmEntry.setStatus("current")
_McRxByteHi_Type = Counter32
_McRxByteHi_Object = MibTableColumn
mcRxByteHi = _McRxByteHi_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 3, 1, 1, 1),
    _McRxByteHi_Type()
)
mcRxByteHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcRxByteHi.setStatus("current")
_McRxByteLo_Type = Counter32
_McRxByteLo_Object = MibTableColumn
mcRxByteLo = _McRxByteLo_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 3, 1, 1, 2),
    _McRxByteLo_Type()
)
mcRxByteLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcRxByteLo.setStatus("current")
_McTxByteHi_Type = Counter32
_McTxByteHi_Object = MibTableColumn
mcTxByteHi = _McTxByteHi_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 3, 1, 1, 3),
    _McTxByteHi_Type()
)
mcTxByteHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcTxByteHi.setStatus("current")
_McTxByteLo_Type = Counter32
_McTxByteLo_Object = MibTableColumn
mcTxByteLo = _McTxByteLo_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 3, 1, 1, 4),
    _McTxByteLo_Type()
)
mcTxByteLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcTxByteLo.setStatus("current")


class _McPmRest_Type(Integer32):
    """Custom type mcPmRest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("reset", 2),
          ("not-support", 3))
    )


_McPmRest_Type.__name__ = "Integer32"
_McPmRest_Object = MibTableColumn
mcPmRest = _McPmRest_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 1, 4, 3, 1, 1, 5),
    _McPmRest_Type()
)
mcPmRest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcPmRest.setStatus("current")
_AlarmMIB_ObjectIdentity = ObjectIdentity
alarmMIB = _AlarmMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 2)
)

# Managed Objects groups


# Notification objects

shelf_Detected = NotificationType(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 2, 1)
)
shelf_Detected.setObjects(
    ("XXX-MIB", "shelfIdx")
)
if mibBuilder.loadTexts:
    shelf_Detected.setStatus(
        "current"
    )

shelf_Lost = NotificationType(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 2, 2)
)
shelf_Lost.setObjects(
    ("XXX-MIB", "shelfIdx")
)
if mibBuilder.loadTexts:
    shelf_Lost.setStatus(
        "current"
    )

shelf_psuA_On = NotificationType(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 2, 3)
)
shelf_psuA_On.setObjects(
    ("XXX-MIB", "shelfIdx")
)
if mibBuilder.loadTexts:
    shelf_psuA_On.setStatus(
        "current"
    )

shelf_psuA_Off = NotificationType(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 2, 4)
)
shelf_psuA_Off.setObjects(
    ("XXX-MIB", "shelfIdx")
)
if mibBuilder.loadTexts:
    shelf_psuA_Off.setStatus(
        "current"
    )

shelf_psuB_On = NotificationType(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 2, 5)
)
shelf_psuB_On.setObjects(
    ("XXX-MIB", "shelfIdx")
)
if mibBuilder.loadTexts:
    shelf_psuB_On.setStatus(
        "current"
    )

shelf_psuB_Off = NotificationType(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 2, 6)
)
shelf_psuB_Off.setObjects(
    ("XXX-MIB", "shelfIdx")
)
if mibBuilder.loadTexts:
    shelf_psuB_Off.setStatus(
        "current"
    )

shelf_fan_On = NotificationType(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 2, 7)
)
shelf_fan_On.setObjects(
    ("XXX-MIB", "shelfIdx")
)
if mibBuilder.loadTexts:
    shelf_fan_On.setStatus(
        "current"
    )

shelf_fan_Off = NotificationType(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 2, 8)
)
shelf_fan_Off.setObjects(
    ("XXX-MIB", "shelfIdx")
)
if mibBuilder.loadTexts:
    shelf_fan_Off.setStatus(
        "current"
    )

card_Detected = NotificationType(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 2, 20)
)
card_Detected.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_Detected.setStatus(
        "current"
    )

card_Lost = NotificationType(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 2, 21)
)
card_Lost.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_Lost.setStatus(
        "current"
    )

card_MC_Co_Tx_Up = NotificationType(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 2, 30)
)
card_MC_Co_Tx_Up.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_Tx_Up.setStatus(
        "current"
    )

card_MC_Co_Tx_Down = NotificationType(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 2, 31)
)
card_MC_Co_Tx_Down.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_Tx_Down.setStatus(
        "current"
    )

card_MC_Co_Fx_Up = NotificationType(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 2, 32)
)
card_MC_Co_Fx_Up.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_Fx_Up.setStatus(
        "current"
    )

card_MC_Co_Fx_Down = NotificationType(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 2, 33)
)
card_MC_Co_Fx_Down.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_Fx_Down.setStatus(
        "current"
    )

card_MC_Rmt_Tx_Up = NotificationType(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 2, 34)
)
card_MC_Rmt_Tx_Up.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Rmt_Tx_Up.setStatus(
        "current"
    )

card_MC_Rmt_Tx_Down = NotificationType(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 2, 35)
)
card_MC_Rmt_Tx_Down.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Rmt_Tx_Down.setStatus(
        "current"
    )

card_MC_Rmt_PwrDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 2, 36)
)
card_MC_Rmt_PwrDown.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Rmt_PwrDown.setStatus(
        "current"
    )

card_MC_Co_Ntw_SFP_Inserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 2, 37)
)
card_MC_Co_Ntw_SFP_Inserted.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_Ntw_SFP_Inserted.setStatus(
        "current"
    )

card_MC_Co_Ntw_SFP_Removed = NotificationType(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 2, 38)
)
card_MC_Co_Ntw_SFP_Removed.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_Ntw_SFP_Removed.setStatus(
        "current"
    )

card_MC_Co_Acc_SFP_Inserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 2, 39)
)
card_MC_Co_Acc_SFP_Inserted.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_Acc_SFP_Inserted.setStatus(
        "current"
    )

card_MC_Co_Acc_SFP_Removed = NotificationType(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 2, 40)
)
card_MC_Co_Acc_SFP_Removed.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_Acc_SFP_Removed.setStatus(
        "current"
    )

card_MC_Rmt_Acc_SFP_Inserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 2, 41)
)
card_MC_Rmt_Acc_SFP_Inserted.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Rmt_Acc_SFP_Inserted.setStatus(
        "current"
    )

card_MC_Rmt_Acc_SFP_Removed = NotificationType(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1, 2, 42)
)
card_MC_Rmt_Acc_SFP_Removed.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Rmt_Acc_SFP_Removed.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XXX-MIB",
    **{"company": company,
       "ipProduct": ipProduct,
       "height2HU": height2HU,
       "systemMIB": systemMIB,
       "shelfNum": shelfNum,
       "shelfTable": shelfTable,
       "shelfEntry": shelfEntry,
       "shelfName": shelfName,
       "psuA": psuA,
       "psuB": psuB,
       "volA": volA,
       "volB": volB,
       "fan": fan,
       "temperature": temperature,
       "coCardNum": coCardNum,
       "rmtCardNum": rmtCardNum,
       "slotObjects": slotObjects,
       "slotTable": slotTable,
       "slotEntry": slotEntry,
       "shelfIdx": shelfIdx,
       "slotIdx": slotIdx,
       "coCardType": coCardType,
       "coCardDesc": coCardDesc,
       "rmtCardType": rmtCardType,
       "rmtCardDesc": rmtCardDesc,
       "cardObjects": cardObjects,
       "nmuObjects": nmuObjects,
       "nmuConfig": nmuConfig,
       "nmuType": nmuType,
       "ipaddr": ipaddr,
       "subnet": subnet,
       "gateway": gateway,
       "sysContact": sysContact,
       "sysName": sysName,
       "sysLocation": sysLocation,
       "trapHost1": trapHost1,
       "trapHost2": trapHost2,
       "trapHost3": trapHost3,
       "trapHost4": trapHost4,
       "mcCmObjects": mcCmObjects,
       "mcCmTable": mcCmTable,
       "mcCmEntry": mcCmEntry,
       "mcShelfIdx": mcShelfIdx,
       "mcCardIdx": mcCardIdx,
       "mcType": mcType,
       "mcTransceiverMode": mcTransceiverMode,
       "mcTransceiverDist": mcTransceiverDist,
       "mcPortState": mcPortState,
       "mcTransmitMode": mcTransmitMode,
       "mcCurWorkMode": mcCurWorkMode,
       "mcCfgWorkMode": mcCfgWorkMode,
       "mcLFPCfg": mcLFPCfg,
       "mcUpStream": mcUpStream,
       "mcDownStream": mcDownStream,
       "mcTxlink": mcTxlink,
       "mcFxlink": mcFxlink,
       "mcHWLFP": mcHWLFP,
       "mcHWTransmitMode": mcHWTransmitMode,
       "mcHWWorkMode": mcHWWorkMode,
       "mcHWRmtCtrlMode": mcHWRmtCtrlMode,
       "mcNtwSfpExist": mcNtwSfpExist,
       "mcAccSfpExist": mcAccSfpExist,
       "mcUtility": mcUtility,
       "mcRmtDetect": mcRmtDetect,
       "mcRmtType": mcRmtType,
       "mcRmtTransmitMode": mcRmtTransmitMode,
       "mcRmtCurWorkMode": mcRmtCurWorkMode,
       "mcRmtCfgWorkMode": mcRmtCfgWorkMode,
       "mcRmtLFP": mcRmtLFP,
       "mcRmtTxlink": mcRmtTxlink,
       "mcRmtHWLFP": mcRmtHWLFP,
       "mcRmtHWTransmitMode": mcRmtHWTransmitMode,
       "mcRmtHWWorkMode": mcRmtHWWorkMode,
       "mcRmtLoopback": mcRmtLoopback,
       "mcRmtPwrDown": mcRmtPwrDown,
       "mcRmtAccSfpExist": mcRmtAccSfpExist,
       "mcRmtUtility": mcRmtUtility,
       "mcCm1gSpecificObjects": mcCm1gSpecificObjects,
       "mcCm1gIpObjects": mcCm1gIpObjects,
       "mcCm1gIpTable": mcCm1gIpTable,
       "mcCm1gIpEntry": mcCm1gIpEntry,
       "mcLoOrRmtFg": mcLoOrRmtFg,
       "mcIpAddr": mcIpAddr,
       "mcCm1gSfpObjects": mcCm1gSfpObjects,
       "mcCm1gSfpTable": mcCm1gSfpTable,
       "mcCm1gSfpEntry": mcCm1gSfpEntry,
       "getSfpCmd": getSfpCmd,
       "sfpCompliance": sfpCompliance,
       "sfpConnector": sfpConnector,
       "sfpTransCode": sfpTransCode,
       "sfpSmLength": sfpSmLength,
       "sfpMmLength": sfpMmLength,
       "sfpCopperLength": sfpCopperLength,
       "sfpBrSpeed": sfpBrSpeed,
       "sfpWavelength": sfpWavelength,
       "sfpTemperature": sfpTemperature,
       "sfpTranPower": sfpTranPower,
       "sfpRecvPower": sfpRecvPower,
       "sfpVoltage": sfpVoltage,
       "mcPmObjects": mcPmObjects,
       "mcPmTable": mcPmTable,
       "mcPmEntry": mcPmEntry,
       "mcRxByteHi": mcRxByteHi,
       "mcRxByteLo": mcRxByteLo,
       "mcTxByteHi": mcTxByteHi,
       "mcTxByteLo": mcTxByteLo,
       "mcPmRest": mcPmRest,
       "alarmMIB": alarmMIB,
       "shelf-Detected": shelf_Detected,
       "shelf-Lost": shelf_Lost,
       "shelf-psuA-On": shelf_psuA_On,
       "shelf-psuA-Off": shelf_psuA_Off,
       "shelf-psuB-On": shelf_psuB_On,
       "shelf-psuB-Off": shelf_psuB_Off,
       "shelf-fan-On": shelf_fan_On,
       "shelf-fan-Off": shelf_fan_Off,
       "card-Detected": card_Detected,
       "card-Lost": card_Lost,
       "card-MC-Co-Tx-Up": card_MC_Co_Tx_Up,
       "card-MC-Co-Tx-Down": card_MC_Co_Tx_Down,
       "card-MC-Co-Fx-Up": card_MC_Co_Fx_Up,
       "card-MC-Co-Fx-Down": card_MC_Co_Fx_Down,
       "card-MC-Rmt-Tx-Up": card_MC_Rmt_Tx_Up,
       "card-MC-Rmt-Tx-Down": card_MC_Rmt_Tx_Down,
       "card-MC-Rmt-PwrDown": card_MC_Rmt_PwrDown,
       "card-MC-Co-Ntw-SFP-Inserted": card_MC_Co_Ntw_SFP_Inserted,
       "card-MC-Co-Ntw-SFP-Removed": card_MC_Co_Ntw_SFP_Removed,
       "card-MC-Co-Acc-SFP-Inserted": card_MC_Co_Acc_SFP_Inserted,
       "card-MC-Co-Acc-SFP-Removed": card_MC_Co_Acc_SFP_Removed,
       "card-MC-Rmt-Acc-SFP-Inserted": card_MC_Rmt_Acc_SFP_Inserted,
       "card-MC-Rmt-Acc-SFP-Removed": card_MC_Rmt_Acc_SFP_Removed}
)
