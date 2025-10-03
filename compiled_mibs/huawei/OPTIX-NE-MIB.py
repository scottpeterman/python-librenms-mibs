# SNMP MIB module (OPTIX-NE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\huawei\OPTIX-NE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:00:01 2025
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

(optixProvisionEqpt,) = mibBuilder.importSymbols(
    "OPTIX-OID-MIB",
    "optixProvisionEqpt")

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

optixNe = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 21)
)
if mibBuilder.loadTexts:
    optixNe.setRevisions(
        ("2012-04-24 00:00",
         "2012-04-24 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OptixNeGroup_ObjectIdentity = ObjectIdentity
optixNeGroup = _OptixNeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 21, 1)
)


class _OptixNeName_Type(OctetString):
    """Custom type optixNeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_OptixNeName_Type.__name__ = "OctetString"
_OptixNeName_Object = MibScalar
optixNeName = _OptixNeName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 21, 1, 1),
    _OptixNeName_Type()
)
optixNeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optixNeName.setStatus("current")


class _OptixNePosition_Type(OctetString):
    """Custom type optixNePosition based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OptixNePosition_Type.__name__ = "OctetString"
_OptixNePosition_Object = MibScalar
optixNePosition = _OptixNePosition_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 21, 1, 2),
    _OptixNePosition_Type()
)
optixNePosition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optixNePosition.setStatus("current")


class _OptixNeMemo_Type(OctetString):
    """Custom type optixNeMemo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OptixNeMemo_Type.__name__ = "OctetString"
_OptixNeMemo_Object = MibScalar
optixNeMemo = _OptixNeMemo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 21, 1, 3),
    _OptixNeMemo_Type()
)
optixNeMemo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optixNeMemo.setStatus("current")
_OptixNeH4mode_Type = Unsigned32
_OptixNeH4mode_Object = MibScalar
optixNeH4mode = _OptixNeH4mode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 21, 1, 4),
    _OptixNeH4mode_Type()
)
optixNeH4mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optixNeH4mode.setStatus("current")
_OptixNeDbBackupDelay_Type = Unsigned32
_OptixNeDbBackupDelay_Object = MibScalar
optixNeDbBackupDelay = _OptixNeDbBackupDelay_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 21, 1, 5),
    _OptixNeDbBackupDelay_Type()
)
optixNeDbBackupDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optixNeDbBackupDelay.setStatus("current")


class _OptixNeInsertmode_Type(Integer32):
    """Custom type optixNeInsertmode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("uneq", 0),
          ("ais", 1))
    )


_OptixNeInsertmode_Type.__name__ = "Integer32"
_OptixNeInsertmode_Object = MibScalar
optixNeInsertmode = _OptixNeInsertmode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 21, 1, 6),
    _OptixNeInsertmode_Type()
)
optixNeInsertmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optixNeInsertmode.setStatus("current")


class _OptixNeState_Type(Integer32):
    """Custom type optixNeState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("install", 0),
          ("running", 1))
    )


_OptixNeState_Type.__name__ = "Integer32"
_OptixNeState_Object = MibScalar
optixNeState = _OptixNeState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 21, 1, 7),
    _OptixNeState_Type()
)
optixNeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optixNeState.setStatus("current")


class _OptixNeDeviceType_Type(Integer32):
    """Custom type optixNeDeviceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(76,
              77,
              83,
              92,
              95,
              114,
              115,
              138,
              140,
              151,
              152,
              160,
              180,
              183,
              191)
        )
    )
    namedValues = NamedValues(
        *(("optixrtn910", 76),
          ("optixrtn950", 77),
          ("optixrtn980", 83),
          ("optixrtn310", 92),
          ("optixrtn905", 95),
          ("optixrtn950a", 114),
          ("optiXRTN380", 115),
          ("optixrtn360", 138),
          ("optiXRTN980L", 140),
          ("optixrtn320", 151),
          ("optixrtn910a", 152),
          ("optixrtn380H", 160),
          ("optixrtn380e", 180),
          ("optixrtn905e", 183),
          ("powercube500", 191))
    )


_OptixNeDeviceType_Type.__name__ = "Integer32"
_OptixNeDeviceType_Object = MibScalar
optixNeDeviceType = _OptixNeDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 21, 1, 8),
    _OptixNeDeviceType_Type()
)
optixNeDeviceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optixNeDeviceType.setStatus("current")


class _OptixNeShelfType_Type(Integer32):
    """Custom type optixNeShelfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              146,
              148,
              150,
              163,
              167,
              175,
              177,
              184)
        )
    )
    namedValues = NamedValues(
        *(("subracki1A", 1),
          ("subrackii2A", 2),
          ("subracki1C", 3),
          ("subracki1E", 4),
          ("subrackii2E", 5),
          ("standard310320360380380H910", 146),
          ("standard950950A", 148),
          ("standard980", 150),
          ("standardOutdoor", 163),
          ("split310320", 167),
          ("standard910A", 175),
          ("standardIndoor", 177),
          ("subracki", 184))
    )


_OptixNeShelfType_Type.__name__ = "Integer32"
_OptixNeShelfType_Object = MibScalar
optixNeShelfType = _OptixNeShelfType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 21, 1, 9),
    _OptixNeShelfType_Type()
)
optixNeShelfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optixNeShelfType.setStatus("current")


class _OptixNeAutoLoad_Type(Integer32):
    """Custom type optixNeAutoLoad based on Integer32"""
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


_OptixNeAutoLoad_Type.__name__ = "Integer32"
_OptixNeAutoLoad_Object = MibScalar
optixNeAutoLoad = _OptixNeAutoLoad_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 21, 1, 10),
    _OptixNeAutoLoad_Type()
)
optixNeAutoLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optixNeAutoLoad.setStatus("current")


class _OptixNeOdcDeviceType_Type(Integer32):
    """Custom type optixNeOdcDeviceType based on Integer32"""
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
        *(("null", 0),
          ("apm30Ac", 1),
          ("apm30Dc", 2),
          ("ombAc", 3),
          ("ombDc", 4))
    )


_OptixNeOdcDeviceType_Type.__name__ = "Integer32"
_OptixNeOdcDeviceType_Object = MibScalar
optixNeOdcDeviceType = _OptixNeOdcDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 21, 1, 11),
    _OptixNeOdcDeviceType_Type()
)
optixNeOdcDeviceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optixNeOdcDeviceType.setStatus("current")
_OptixNeGcpNodeId_Type = IpAddress
_OptixNeGcpNodeId_Object = MibScalar
optixNeGcpNodeId = _OptixNeGcpNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 21, 1, 12),
    _OptixNeGcpNodeId_Type()
)
optixNeGcpNodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optixNeGcpNodeId.setStatus("current")


class _OptixNeSmokeAlm_Type(Integer32):
    """Custom type optixNeSmokeAlm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("invalid", 255))
    )


_OptixNeSmokeAlm_Type.__name__ = "Integer32"
_OptixNeSmokeAlm_Object = MibScalar
optixNeSmokeAlm = _OptixNeSmokeAlm_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 21, 1, 13),
    _OptixNeSmokeAlm_Type()
)
optixNeSmokeAlm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optixNeSmokeAlm.setStatus("current")
_OptixNePnpFilePath_Type = OctetString
_OptixNePnpFilePath_Object = MibScalar
optixNePnpFilePath = _OptixNePnpFilePath_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 21, 1, 14),
    _OptixNePnpFilePath_Type()
)
optixNePnpFilePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optixNePnpFilePath.setStatus("current")


class _OptixNe1j1status_Type(Integer32):
    """Custom type optixNe1j1status based on Integer32"""
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
        *(("unknow", 0),
          ("start", 1),
          ("running", 2),
          ("finished", 3))
    )


_OptixNe1j1status_Type.__name__ = "Integer32"
_OptixNe1j1status_Object = MibScalar
optixNe1j1status = _OptixNe1j1status_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 21, 1, 15),
    _OptixNe1j1status_Type()
)
optixNe1j1status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optixNe1j1status.setStatus("current")
_OptixNe1j1cfgcheck_Type = Unsigned32
_OptixNe1j1cfgcheck_Object = MibScalar
optixNe1j1cfgcheck = _OptixNe1j1cfgcheck_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 21, 1, 17),
    _OptixNe1j1cfgcheck_Type()
)
optixNe1j1cfgcheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optixNe1j1cfgcheck.setStatus("current")


class _OptixNeInitAll_Type(Integer32):
    """Custom type optixNeInitAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("init", 0)
    )


_OptixNeInitAll_Type.__name__ = "Integer32"
_OptixNeInitAll_Object = MibScalar
optixNeInitAll = _OptixNeInitAll_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 21, 1, 18),
    _OptixNeInitAll_Type()
)
optixNeInitAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optixNeInitAll.setStatus("current")
_OptixNeFeatureNum_Type = Unsigned32
_OptixNeFeatureNum_Object = MibScalar
optixNeFeatureNum = _OptixNeFeatureNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 21, 1, 20),
    _OptixNeFeatureNum_Type()
)
optixNeFeatureNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optixNeFeatureNum.setStatus("current")
_OptixNeFeatureList_Type = OctetString
_OptixNeFeatureList_Object = MibScalar
optixNeFeatureList = _OptixNeFeatureList_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 21, 1, 21),
    _OptixNeFeatureList_Type()
)
optixNeFeatureList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optixNeFeatureList.setStatus("current")
_OptixNeTableGroup_ObjectIdentity = ObjectIdentity
optixNeTableGroup = _OptixNeTableGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 21, 2)
)
_OptixNe1j1ResultTrapMember_ObjectIdentity = ObjectIdentity
optixNe1j1ResultTrapMember = _OptixNe1j1ResultTrapMember_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 21, 2, 1)
)


class _OptixNe1j1Resultinfo_Type(Integer32):
    """Custom type optixNe1j1Resultinfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("success", 0),
          ("failed", 1))
    )


_OptixNe1j1Resultinfo_Type.__name__ = "Integer32"
_OptixNe1j1Resultinfo_Object = MibScalar
optixNe1j1Resultinfo = _OptixNe1j1Resultinfo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 21, 2, 1, 1),
    _OptixNe1j1Resultinfo_Type()
)
optixNe1j1Resultinfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    optixNe1j1Resultinfo.setStatus("current")
_OptixNeLicenseTable_Object = MibTable
optixNeLicenseTable = _OptixNeLicenseTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 21, 2, 2)
)
if mibBuilder.loadTexts:
    optixNeLicenseTable.setStatus("current")
_OptixNeLicenseEntry_Object = MibTableRow
optixNeLicenseEntry = _OptixNeLicenseEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 21, 2, 2, 1)
)
optixNeLicenseEntry.setIndexNames(
    (0, "OPTIX-NE-MIB", "optixNeLicenseFuncID"),
)
if mibBuilder.loadTexts:
    optixNeLicenseEntry.setStatus("current")


class _OptixNeLicenseFuncID_Type(Integer32):
    """Custom type optixNeLicenseFuncID based on Integer32"""
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
              100)
        )
    )
    namedValues = NamedValues(
        *(("tpbasic", 1),
          ("tpenhance", 2),
          ("tpinterwork", 3),
          ("sanaccess", 4),
          ("sdhfee", 5),
          ("pktfee", 6),
          ("t32sup100g", 7),
          ("flexgrid", 8),
          ("snmp7500sup10g", 100))
    )


_OptixNeLicenseFuncID_Type.__name__ = "Integer32"
_OptixNeLicenseFuncID_Object = MibTableColumn
optixNeLicenseFuncID = _OptixNeLicenseFuncID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 21, 2, 2, 1, 1),
    _OptixNeLicenseFuncID_Type()
)
optixNeLicenseFuncID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    optixNeLicenseFuncID.setStatus("current")


class _OptixNeLicenseLevel_Type(Integer32):
    """Custom type optixNeLicenseLevel based on Integer32"""
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
        *(("ne", 1),
          ("shelf", 2),
          ("board", 3),
          ("subcard", 4),
          ("port", 5))
    )


_OptixNeLicenseLevel_Type.__name__ = "Integer32"
_OptixNeLicenseLevel_Object = MibTableColumn
optixNeLicenseLevel = _OptixNeLicenseLevel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 21, 2, 2, 1, 2),
    _OptixNeLicenseLevel_Type()
)
optixNeLicenseLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optixNeLicenseLevel.setStatus("current")
_OptixNeLicenseState_Type = Unsigned32
_OptixNeLicenseState_Object = MibTableColumn
optixNeLicenseState = _OptixNeLicenseState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 21, 2, 2, 1, 3),
    _OptixNeLicenseState_Type()
)
optixNeLicenseState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optixNeLicenseState.setStatus("current")
_OptixNeLicenseNum_Type = Unsigned32
_OptixNeLicenseNum_Object = MibTableColumn
optixNeLicenseNum = _OptixNeLicenseNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 21, 2, 2, 1, 4),
    _OptixNeLicenseNum_Type()
)
optixNeLicenseNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optixNeLicenseNum.setStatus("current")
_OptixNe1j1ResultTrapReport_ObjectIdentity = ObjectIdentity
optixNe1j1ResultTrapReport = _OptixNe1j1ResultTrapReport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 21, 2, 3)
)

# Managed Objects groups


# Notification objects

optixNe1j1ResultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 21, 2, 3, 1)
)
optixNe1j1ResultTrap.setObjects(
    ("OPTIX-NE-MIB", "optixNe1j1Resultinfo")
)
if mibBuilder.loadTexts:
    optixNe1j1ResultTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OPTIX-NE-MIB",
    **{"optixNe": optixNe,
       "optixNeGroup": optixNeGroup,
       "optixNeName": optixNeName,
       "optixNePosition": optixNePosition,
       "optixNeMemo": optixNeMemo,
       "optixNeH4mode": optixNeH4mode,
       "optixNeDbBackupDelay": optixNeDbBackupDelay,
       "optixNeInsertmode": optixNeInsertmode,
       "optixNeState": optixNeState,
       "optixNeDeviceType": optixNeDeviceType,
       "optixNeShelfType": optixNeShelfType,
       "optixNeAutoLoad": optixNeAutoLoad,
       "optixNeOdcDeviceType": optixNeOdcDeviceType,
       "optixNeGcpNodeId": optixNeGcpNodeId,
       "optixNeSmokeAlm": optixNeSmokeAlm,
       "optixNePnpFilePath": optixNePnpFilePath,
       "optixNe1j1status": optixNe1j1status,
       "optixNe1j1cfgcheck": optixNe1j1cfgcheck,
       "optixNeInitAll": optixNeInitAll,
       "optixNeFeatureNum": optixNeFeatureNum,
       "optixNeFeatureList": optixNeFeatureList,
       "optixNeTableGroup": optixNeTableGroup,
       "optixNe1j1ResultTrapMember": optixNe1j1ResultTrapMember,
       "optixNe1j1Resultinfo": optixNe1j1Resultinfo,
       "optixNeLicenseTable": optixNeLicenseTable,
       "optixNeLicenseEntry": optixNeLicenseEntry,
       "optixNeLicenseFuncID": optixNeLicenseFuncID,
       "optixNeLicenseLevel": optixNeLicenseLevel,
       "optixNeLicenseState": optixNeLicenseState,
       "optixNeLicenseNum": optixNeLicenseNum,
       "optixNe1j1ResultTrapReport": optixNe1j1ResultTrapReport,
       "optixNe1j1ResultTrap": optixNe1j1ResultTrap}
)
