# SNMP MIB module (TROPIC-SOFTWARE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\1830\TROPIC-SOFTWARE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:12:53 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(tnSoftwareMIB,
 tnSystemModules) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnSoftwareMIB",
    "tnSystemModules")

(tnShelfIndex,) = mibBuilder.importSymbols(
    "TROPIC-SHELF-MIB",
    "tnShelfIndex")

(tnSlotIndex,) = mibBuilder.importSymbols(
    "TROPIC-SLOT-MIB",
    "tnSlotIndex")

(AluWdmNewTransferProtocol,
 TnCommand,
 TropicShelfIndexType,
 TropicSlotIndexType) = mibBuilder.importSymbols(
    "TROPIC-TC",
    "AluWdmNewTransferProtocol",
    "TnCommand",
    "TropicShelfIndexType",
    "TropicSlotIndexType")


# MODULE-IDENTITY

tnSoftwareMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 1, 6)
)
if mibBuilder.loadTexts:
    tnSoftwareMibModule.setRevisions(
        ("2023-01-20 12:00",
         "2022-10-14 12:00",
         "2022-08-12 12:00",
         "2022-07-29 12:00",
         "2022-07-15 12:00",
         "2022-04-29 12:00",
         "2022-03-04 12:00",
         "2022-02-04 12:00",
         "2022-01-21 12:00",
         "2021-12-24 12:00",
         "2021-12-17 12:00",
         "2021-12-10 12:00",
         "2021-10-22 12:00",
         "2021-10-08 12:00",
         "2021-10-01 12:00",
         "2021-09-24 12:00",
         "2021-08-06 12:00",
         "2021-07-16 12:00",
         "2021-06-18 12:00",
         "2021-06-11 12:00",
         "2021-06-04 12:00",
         "2021-05-21 12:00",
         "2021-05-14 12:00",
         "2021-05-07 12:00",
         "2021-04-09 12:00",
         "2021-02-19 12:00",
         "2021-02-05 12:00",
         "2020-12-24 12:00",
         "2020-10-02 12:00",
         "2020-09-18 12:00",
         "2020-08-21 12:00",
         "2020-06-19 12:00",
         "2020-04-03 12:00",
         "2020-03-20 12:00",
         "2020-02-28 12:00",
         "2020-01-10 12:00",
         "2019-12-20 12:00",
         "2019-11-15 12:00",
         "2019-10-04 12:00",
         "2019-08-02 12:00",
         "2019-07-26 12:00",
         "2019-07-19 12:00",
         "2019-07-12 12:00",
         "2019-05-31 12:00",
         "2019-03-15 12:00",
         "2019-01-25 12:00",
         "2019-01-18 12:00",
         "2018-12-28 12:00",
         "2018-10-26 12:00",
         "2018-10-19 12:00",
         "2018-09-28 12:00",
         "2018-09-14 12:00",
         "2018-08-10 12:00",
         "2018-07-06 12:00",
         "2018-06-29 12:00",
         "2018-06-15 12:00",
         "2018-06-08 12:00",
         "2018-05-25 12:00",
         "2018-05-18 12:00",
         "2018-03-23 12:00",
         "2018-02-23 12:00",
         "2018-01-26 12:00",
         "2018-01-12 12:00",
         "2017-11-10 12:00",
         "2017-11-03 12:00",
         "2017-10-13 12:00",
         "2017-09-29 12:00",
         "2017-09-22 12:00",
         "2017-09-15 12:00",
         "2017-09-01 12:00",
         "2017-08-18 12:00",
         "2017-07-14 12:00",
         "2017-07-07 12:00",
         "2017-06-30 12:00",
         "2017-06-23 12:00",
         "2017-06-09 12:00",
         "2017-04-07 12:00",
         "2017-03-24 12:00",
         "2017-03-10 12:00",
         "2017-02-10 12:00",
         "2017-01-27 12:00",
         "2017-01-20 12:00",
         "2016-12-19 12:00",
         "2016-12-09 12:00",
         "2016-11-28 12:00",
         "2016-11-16 12:00",
         "2016-11-01 12:00",
         "2016-09-30 12:00",
         "2016-09-13 12:00",
         "2016-08-29 12:00",
         "2016-08-22 12:00",
         "2016-08-16 12:00",
         "2016-07-27 12:00",
         "2016-06-01 12:00",
         "2016-05-25 12:00",
         "2016-05-20 12:00",
         "2016-05-10 12:00",
         "2016-05-04 12:00",
         "2016-04-07 12:00",
         "2016-02-29 12:00",
         "2016-02-23 12:00",
         "2015-12-08 12:00",
         "2015-10-28 12:00",
         "2015-10-05 12:00",
         "2015-08-06 12:00",
         "2015-06-22 12:00",
         "2015-06-12 12:00",
         "2015-02-20 12:00",
         "2015-01-16 12:00",
         "2014-09-25 12:00",
         "2014-09-18 12:00",
         "2014-08-08 12:00",
         "2014-07-07 12:00",
         "2014-06-23 12:00",
         "2014-05-06 12:00",
         "2014-03-30 12:00",
         "2014-02-19 12:00",
         "2014-02-03 12:00",
         "2014-01-21 12:00",
         "2013-12-20 12:00",
         "2013-11-25 12:00",
         "2013-11-06 12:00",
         "2013-10-10 12:00",
         "2013-10-07 12:00",
         "2013-09-04 12:00",
         "2013-08-12 12:00",
         "2013-06-24 12:00",
         "2013-05-24 12:00",
         "2013-05-21 12:00",
         "2013-04-19 12:00",
         "2013-04-11 12:00",
         "2013-03-16 12:00",
         "2013-03-07 12:00",
         "2012-08-28 12:00",
         "2012-07-24 12:00",
         "2012-06-18 12:00",
         "2012-05-18 12:00",
         "2012-04-27 12:00",
         "2012-04-24 12:00",
         "2012-03-29 12:00",
         "2012-03-18 12:00",
         "2012-02-12 12:00",
         "2012-01-19 12:00",
         "2012-01-18 12:00",
         "2012-01-10 12:00",
         "2011-11-21 12:00",
         "2011-11-14 12:00",
         "2011-09-16 12:00",
         "2011-09-06 12:00",
         "2011-08-31 12:00",
         "2011-07-19 12:00",
         "2011-07-07 12:00",
         "2011-06-30 12:00",
         "2011-06-13 12:00",
         "2011-06-07 12:00",
         "2011-05-17 12:00",
         "2011-05-04 12:00",
         "2011-03-28 12:00",
         "2010-11-10 12:00",
         "2010-10-19 12:00",
         "2010-10-18 12:00",
         "2010-10-17 12:00",
         "2010-09-28 12:00",
         "2010-09-24 12:00",
         "2010-09-20 12:00",
         "2010-09-10 12:00",
         "2010-07-20 12:00",
         "2010-06-25 12:00",
         "2010-06-04 12:00",
         "2010-05-10 12:00",
         "2010-05-07 12:00",
         "2010-02-17 12:00",
         "2010-01-04 12:00",
         "2009-12-10 12:00",
         "2009-11-01 12:00",
         "2009-09-25 12:00",
         "2009-03-31 12:00",
         "2009-03-18 12:00",
         "2009-03-15 12:00",
         "2009-03-02 12:00",
         "2009-02-07 12:00",
         "2009-02-05 12:00",
         "2009-02-01 12:00",
         "2008-12-17 12:00",
         "2008-05-29 12:00",
         "2008-05-02 12:00",
         "2003-09-13 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TropicSwControl(TextualConvention, Integer32):
    status = "current"
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
        *(("noCmd", 1),
          ("unknown", 2),
          ("audit", 3),
          ("activate", 4),
          ("upgradeAuto", 5),
          ("commit", 6),
          ("backout", 7),
          ("load", 8),
          ("cardActivate", 9),
          ("cardLoad", 10),
          ("autoInstall", 11),
          ("autoIsuLoad", 12),
          ("autoActivate", 13),
          ("autoIsuCommit", 14),
          ("srosMigration", 15))
    )



class TropicSwBank(TextualConvention, Integer32):
    status = "current"
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
        *(("none", 1),
          ("application0", 2),
          ("application1", 3),
          ("userBoot", 4),
          ("emergencyBoot", 5))
    )



class TropicSwLastOperationStatus(TextualConvention, Integer32):
    status = "current"
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
        *(("completed", 1),
          ("inProgress", 2),
          ("failure", 3),
          ("none", 4))
    )



class TropicSwLastOperationResult(SnmpAdminString):
    status = "current"
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class TropicSwLastOperationPercentCompleted(TextualConvention, Unsigned32):
    status = "current"


class AluWdmPortGroupMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("pwrSv", 1),
          ("oth", 2),
          ("ethSth", 3),
          ("eth", 4),
          ("sth", 5),
          ("fc", 6))
    )



# MIB Managed Objects in the order of their OIDs

_TnSoftwareConf_ObjectIdentity = ObjectIdentity
tnSoftwareConf = _TnSoftwareConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 1)
)
_TnSoftwareGroups_ObjectIdentity = ObjectIdentity
tnSoftwareGroups = _TnSoftwareGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 1, 1)
)
_TnSoftwareCompliances_ObjectIdentity = ObjectIdentity
tnSoftwareCompliances = _TnSoftwareCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 1, 2)
)
_TnSoftwareObjs_ObjectIdentity = ObjectIdentity
tnSoftwareObjs = _TnSoftwareObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2)
)
_TnSoftwareBasics_ObjectIdentity = ObjectIdentity
tnSoftwareBasics = _TnSoftwareBasics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1)
)
_TnSoftwareNode_ObjectIdentity = ObjectIdentity
tnSoftwareNode = _TnSoftwareNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 1)
)


class _TnSwNodeReleaseRoot_Type(SnmpAdminString):
    """Custom type tnSwNodeReleaseRoot based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSwNodeReleaseRoot_Type.__name__ = "SnmpAdminString"
_TnSwNodeReleaseRoot_Object = MibScalar
tnSwNodeReleaseRoot = _TnSwNodeReleaseRoot_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 1, 2),
    _TnSwNodeReleaseRoot_Type()
)
tnSwNodeReleaseRoot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSwNodeReleaseRoot.setStatus("current")
_TnSwNodeControl_Type = TropicSwControl
_TnSwNodeControl_Object = MibScalar
tnSwNodeControl = _TnSwNodeControl_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 1, 3),
    _TnSwNodeControl_Type()
)
tnSwNodeControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSwNodeControl.setStatus("current")


class _TnSwNodeCommittedRelease_Type(SnmpAdminString):
    """Custom type tnSwNodeCommittedRelease based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TnSwNodeCommittedRelease_Type.__name__ = "SnmpAdminString"
_TnSwNodeCommittedRelease_Object = MibScalar
tnSwNodeCommittedRelease = _TnSwNodeCommittedRelease_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 1, 5),
    _TnSwNodeCommittedRelease_Type()
)
tnSwNodeCommittedRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwNodeCommittedRelease.setStatus("current")


class _TnSwNodeWorkingRelease_Type(SnmpAdminString):
    """Custom type tnSwNodeWorkingRelease based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TnSwNodeWorkingRelease_Type.__name__ = "SnmpAdminString"
_TnSwNodeWorkingRelease_Object = MibScalar
tnSwNodeWorkingRelease = _TnSwNodeWorkingRelease_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 1, 6),
    _TnSwNodeWorkingRelease_Type()
)
tnSwNodeWorkingRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwNodeWorkingRelease.setStatus("current")


class _TnSwNodeForce_Type(Integer32):
    """Custom type tnSwNodeForce based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("false", 2),
          ("true", 3))
    )


_TnSwNodeForce_Type.__name__ = "Integer32"
_TnSwNodeForce_Object = MibScalar
tnSwNodeForce = _TnSwNodeForce_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 1, 7),
    _TnSwNodeForce_Type()
)
tnSwNodeForce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSwNodeForce.setStatus("current")


class _TnSwNodeNoBackup_Type(Integer32):
    """Custom type tnSwNodeNoBackup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("false", 2),
          ("true", 3))
    )


_TnSwNodeNoBackup_Type.__name__ = "Integer32"
_TnSwNodeNoBackup_Object = MibScalar
tnSwNodeNoBackup = _TnSwNodeNoBackup_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 1, 8),
    _TnSwNodeNoBackup_Type()
)
tnSwNodeNoBackup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSwNodeNoBackup.setStatus("current")
_TnSwNodeUpgradePathAvailable_Type = TruthValue
_TnSwNodeUpgradePathAvailable_Object = MibScalar
tnSwNodeUpgradePathAvailable = _TnSwNodeUpgradePathAvailable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 1, 9),
    _TnSwNodeUpgradePathAvailable_Type()
)
tnSwNodeUpgradePathAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwNodeUpgradePathAvailable.setStatus("current")
_TnSwNodeLastControlOperation_Type = TropicSwControl
_TnSwNodeLastControlOperation_Object = MibScalar
tnSwNodeLastControlOperation = _TnSwNodeLastControlOperation_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 1, 10),
    _TnSwNodeLastControlOperation_Type()
)
tnSwNodeLastControlOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwNodeLastControlOperation.setStatus("current")
_TnSwNodeControlAbort_Type = TnCommand
_TnSwNodeControlAbort_Object = MibScalar
tnSwNodeControlAbort = _TnSwNodeControlAbort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 1, 11),
    _TnSwNodeControlAbort_Type()
)
tnSwNodeControlAbort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSwNodeControlAbort.setStatus("current")
_TnSwNodeLastControlOperationStatus_Type = TropicSwLastOperationStatus
_TnSwNodeLastControlOperationStatus_Object = MibScalar
tnSwNodeLastControlOperationStatus = _TnSwNodeLastControlOperationStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 1, 12),
    _TnSwNodeLastControlOperationStatus_Type()
)
tnSwNodeLastControlOperationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwNodeLastControlOperationStatus.setStatus("current")
_TnSwNodeLastControlOperationResult_Type = TropicSwLastOperationResult
_TnSwNodeLastControlOperationResult_Object = MibScalar
tnSwNodeLastControlOperationResult = _TnSwNodeLastControlOperationResult_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 1, 13),
    _TnSwNodeLastControlOperationResult_Type()
)
tnSwNodeLastControlOperationResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwNodeLastControlOperationResult.setStatus("current")
_TnSwNodeLastControlOperationIntegerResult_Type = Integer32
_TnSwNodeLastControlOperationIntegerResult_Object = MibScalar
tnSwNodeLastControlOperationIntegerResult = _TnSwNodeLastControlOperationIntegerResult_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 1, 14),
    _TnSwNodeLastControlOperationIntegerResult_Type()
)
tnSwNodeLastControlOperationIntegerResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwNodeLastControlOperationIntegerResult.setStatus("current")
_TnSwNodeLastControlOperationPercentCompleted_Type = TropicSwLastOperationPercentCompleted
_TnSwNodeLastControlOperationPercentCompleted_Object = MibScalar
tnSwNodeLastControlOperationPercentCompleted = _TnSwNodeLastControlOperationPercentCompleted_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 1, 15),
    _TnSwNodeLastControlOperationPercentCompleted_Type()
)
tnSwNodeLastControlOperationPercentCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwNodeLastControlOperationPercentCompleted.setStatus("current")
_TnSwNodeLastAuditTimeStamp_Type = Unsigned32
_TnSwNodeLastAuditTimeStamp_Object = MibScalar
tnSwNodeLastAuditTimeStamp = _TnSwNodeLastAuditTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 1, 16),
    _TnSwNodeLastAuditTimeStamp_Type()
)
tnSwNodeLastAuditTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSwNodeLastAuditTimeStamp.setStatus("current")


class _TnSwNodeWorkingReleaseDir_Type(SnmpAdminString):
    """Custom type tnSwNodeWorkingReleaseDir based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSwNodeWorkingReleaseDir_Type.__name__ = "SnmpAdminString"
_TnSwNodeWorkingReleaseDir_Object = MibScalar
tnSwNodeWorkingReleaseDir = _TnSwNodeWorkingReleaseDir_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 1, 18),
    _TnSwNodeWorkingReleaseDir_Type()
)
tnSwNodeWorkingReleaseDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSwNodeWorkingReleaseDir.setStatus("current")


class _TnSwNodeActiveRelease_Type(SnmpAdminString):
    """Custom type tnSwNodeActiveRelease based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TnSwNodeActiveRelease_Type.__name__ = "SnmpAdminString"
_TnSwNodeActiveRelease_Object = MibScalar
tnSwNodeActiveRelease = _TnSwNodeActiveRelease_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 1, 19),
    _TnSwNodeActiveRelease_Type()
)
tnSwNodeActiveRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwNodeActiveRelease.setStatus("current")


class _TnSwNodeSwdlServerProtocol_Type(Integer32):
    """Custom type tnSwNodeSwdlServerProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 1),
          ("sftp", 2),
          ("http", 4),
          ("https", 5))
    )


_TnSwNodeSwdlServerProtocol_Type.__name__ = "Integer32"
_TnSwNodeSwdlServerProtocol_Object = MibScalar
tnSwNodeSwdlServerProtocol = _TnSwNodeSwdlServerProtocol_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 1, 20),
    _TnSwNodeSwdlServerProtocol_Type()
)
tnSwNodeSwdlServerProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSwNodeSwdlServerProtocol.setStatus("current")
_TnSwNodeSwdlServerIp_Type = IpAddress
_TnSwNodeSwdlServerIp_Object = MibScalar
tnSwNodeSwdlServerIp = _TnSwNodeSwdlServerIp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 1, 21),
    _TnSwNodeSwdlServerIp_Type()
)
tnSwNodeSwdlServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSwNodeSwdlServerIp.setStatus("current")


class _TnSwNodeSwdlServerUserId_Type(SnmpAdminString):
    """Custom type tnSwNodeSwdlServerUserId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TnSwNodeSwdlServerUserId_Type.__name__ = "SnmpAdminString"
_TnSwNodeSwdlServerUserId_Object = MibScalar
tnSwNodeSwdlServerUserId = _TnSwNodeSwdlServerUserId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 1, 22),
    _TnSwNodeSwdlServerUserId_Type()
)
tnSwNodeSwdlServerUserId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSwNodeSwdlServerUserId.setStatus("current")


class _TnSwNodeSwdlServerPassword_Type(SnmpAdminString):
    """Custom type tnSwNodeSwdlServerPassword based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TnSwNodeSwdlServerPassword_Type.__name__ = "SnmpAdminString"
_TnSwNodeSwdlServerPassword_Object = MibScalar
tnSwNodeSwdlServerPassword = _TnSwNodeSwdlServerPassword_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 1, 23),
    _TnSwNodeSwdlServerPassword_Type()
)
tnSwNodeSwdlServerPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSwNodeSwdlServerPassword.setStatus("current")


class _TnSwNodePartialLoadCommand_Type(Integer32):
    """Custom type tnSwNodePartialLoadCommand based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noCmd", 1),
          ("partialLoad", 2),
          ("forceDownload", 3))
    )


_TnSwNodePartialLoadCommand_Type.__name__ = "Integer32"
_TnSwNodePartialLoadCommand_Object = MibScalar
tnSwNodePartialLoadCommand = _TnSwNodePartialLoadCommand_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 1, 25),
    _TnSwNodePartialLoadCommand_Type()
)
tnSwNodePartialLoadCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSwNodePartialLoadCommand.setStatus("current")


class _TnSwNodePartialLoadSupportedCardTypes_Type(SnmpAdminString):
    """Custom type tnSwNodePartialLoadSupportedCardTypes based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2000),
    )


_TnSwNodePartialLoadSupportedCardTypes_Type.__name__ = "SnmpAdminString"
_TnSwNodePartialLoadSupportedCardTypes_Object = MibScalar
tnSwNodePartialLoadSupportedCardTypes = _TnSwNodePartialLoadSupportedCardTypes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 1, 26),
    _TnSwNodePartialLoadSupportedCardTypes_Type()
)
tnSwNodePartialLoadSupportedCardTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwNodePartialLoadSupportedCardTypes.setStatus("current")


class _TnSwNodePartialLoadImgInstalledCardTypes_Type(SnmpAdminString):
    """Custom type tnSwNodePartialLoadImgInstalledCardTypes based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2000),
    )


_TnSwNodePartialLoadImgInstalledCardTypes_Type.__name__ = "SnmpAdminString"
_TnSwNodePartialLoadImgInstalledCardTypes_Object = MibScalar
tnSwNodePartialLoadImgInstalledCardTypes = _TnSwNodePartialLoadImgInstalledCardTypes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 1, 27),
    _TnSwNodePartialLoadImgInstalledCardTypes_Type()
)
tnSwNodePartialLoadImgInstalledCardTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwNodePartialLoadImgInstalledCardTypes.setStatus("current")


class _TnSwNodePartialLoadImgToBeInstalledCardTypes_Type(SnmpAdminString):
    """Custom type tnSwNodePartialLoadImgToBeInstalledCardTypes based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2000),
    )


_TnSwNodePartialLoadImgToBeInstalledCardTypes_Type.__name__ = "SnmpAdminString"
_TnSwNodePartialLoadImgToBeInstalledCardTypes_Object = MibScalar
tnSwNodePartialLoadImgToBeInstalledCardTypes = _TnSwNodePartialLoadImgToBeInstalledCardTypes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 1, 28),
    _TnSwNodePartialLoadImgToBeInstalledCardTypes_Type()
)
tnSwNodePartialLoadImgToBeInstalledCardTypes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSwNodePartialLoadImgToBeInstalledCardTypes.setStatus("current")
_TnSwNodePartialLoadActionResult_Type = TropicSwLastOperationResult
_TnSwNodePartialLoadActionResult_Object = MibScalar
tnSwNodePartialLoadActionResult = _TnSwNodePartialLoadActionResult_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 1, 29),
    _TnSwNodePartialLoadActionResult_Type()
)
tnSwNodePartialLoadActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwNodePartialLoadActionResult.setStatus("current")
_TnSwNodePartialLoadActionPercentCompleted_Type = TropicSwLastOperationPercentCompleted
_TnSwNodePartialLoadActionPercentCompleted_Object = MibScalar
tnSwNodePartialLoadActionPercentCompleted = _TnSwNodePartialLoadActionPercentCompleted_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 1, 30),
    _TnSwNodePartialLoadActionPercentCompleted_Type()
)
tnSwNodePartialLoadActionPercentCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwNodePartialLoadActionPercentCompleted.setStatus("current")


class _TnSwNodeSwdlServerInetAddressType_Type(InetAddressType):
    """Custom type tnSwNodeSwdlServerInetAddressType based on InetAddressType"""
    defaultValue = 0


_TnSwNodeSwdlServerInetAddressType_Type.__name__ = "InetAddressType"
_TnSwNodeSwdlServerInetAddressType_Object = MibScalar
tnSwNodeSwdlServerInetAddressType = _TnSwNodeSwdlServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 1, 31),
    _TnSwNodeSwdlServerInetAddressType_Type()
)
tnSwNodeSwdlServerInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSwNodeSwdlServerInetAddressType.setStatus("current")


class _TnSwNodeSwdlServerInetAddress_Type(InetAddress):
    """Custom type tnSwNodeSwdlServerInetAddress based on InetAddress"""
    defaultHexValue = ""


_TnSwNodeSwdlServerInetAddress_Type.__name__ = "InetAddress"
_TnSwNodeSwdlServerInetAddress_Object = MibScalar
tnSwNodeSwdlServerInetAddress = _TnSwNodeSwdlServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 1, 32),
    _TnSwNodeSwdlServerInetAddress_Type()
)
tnSwNodeSwdlServerInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSwNodeSwdlServerInetAddress.setStatus("current")


class _TnSwNodeControlStatus_Type(Integer32):
    """Custom type tnSwNodeControlStatus based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("autoLoad", 1),
          ("autoActivate", 2),
          ("autoCommit", 3),
          ("manual", 4),
          ("autoRefresh", 5),
          ("manualRefresh", 6))
    )


_TnSwNodeControlStatus_Type.__name__ = "Integer32"
_TnSwNodeControlStatus_Object = MibScalar
tnSwNodeControlStatus = _TnSwNodeControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 1, 33),
    _TnSwNodeControlStatus_Type()
)
tnSwNodeControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwNodeControlStatus.setStatus("current")


class _TnSwNodePort_Type(Unsigned32):
    """Custom type tnSwNodePort based on Unsigned32"""
    defaultValue = 21

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TnSwNodePort_Type.__name__ = "Unsigned32"
_TnSwNodePort_Object = MibScalar
tnSwNodePort = _TnSwNodePort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 1, 34),
    _TnSwNodePort_Type()
)
tnSwNodePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSwNodePort.setStatus("current")


class _TnSwNodeUrl_Type(SnmpAdminString):
    """Custom type tnSwNodeUrl based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSwNodeUrl_Type.__name__ = "SnmpAdminString"
_TnSwNodeUrl_Object = MibScalar
tnSwNodeUrl = _TnSwNodeUrl_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 1, 35),
    _TnSwNodeUrl_Type()
)
tnSwNodeUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSwNodeUrl.setStatus("current")


class _TnSwNodeLoadType_Type(Integer32):
    """Custom type tnSwNodeLoadType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("dynamic", 2),
          ("static", 3))
    )


_TnSwNodeLoadType_Type.__name__ = "Integer32"
_TnSwNodeLoadType_Object = MibScalar
tnSwNodeLoadType = _TnSwNodeLoadType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 1, 36),
    _TnSwNodeLoadType_Type()
)
tnSwNodeLoadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSwNodeLoadType.setStatus("current")


class _TnSwNodeUrlLoadType_Type(Integer32):
    """Custom type tnSwNodeUrlLoadType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("full", 2))
    )


_TnSwNodeUrlLoadType_Type.__name__ = "Integer32"
_TnSwNodeUrlLoadType_Object = MibScalar
tnSwNodeUrlLoadType = _TnSwNodeUrlLoadType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 1, 37),
    _TnSwNodeUrlLoadType_Type()
)
tnSwNodeUrlLoadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSwNodeUrlLoadType.setStatus("current")


class _TnSwNodeMigrateFileName_Type(SnmpAdminString):
    """Custom type tnSwNodeMigrateFileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSwNodeMigrateFileName_Type.__name__ = "SnmpAdminString"
_TnSwNodeMigrateFileName_Object = MibScalar
tnSwNodeMigrateFileName = _TnSwNodeMigrateFileName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 1, 38),
    _TnSwNodeMigrateFileName_Type()
)
tnSwNodeMigrateFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSwNodeMigrateFileName.setStatus("current")
_TnSwCardTable_Object = MibTable
tnSwCardTable = _TnSwCardTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 2)
)
if mibBuilder.loadTexts:
    tnSwCardTable.setStatus("current")
_TnSwCardEntry_Object = MibTableRow
tnSwCardEntry = _TnSwCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 2, 1)
)
tnSwCardEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnSwCardEntry.setStatus("current")


class _TnSwCardAppBank0_Type(SnmpAdminString):
    """Custom type tnSwCardAppBank0 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TnSwCardAppBank0_Type.__name__ = "SnmpAdminString"
_TnSwCardAppBank0_Object = MibTableColumn
tnSwCardAppBank0 = _TnSwCardAppBank0_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 2, 1, 1),
    _TnSwCardAppBank0_Type()
)
tnSwCardAppBank0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwCardAppBank0.setStatus("current")


class _TnSwCardAppBank1_Type(SnmpAdminString):
    """Custom type tnSwCardAppBank1 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TnSwCardAppBank1_Type.__name__ = "SnmpAdminString"
_TnSwCardAppBank1_Object = MibTableColumn
tnSwCardAppBank1 = _TnSwCardAppBank1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 2, 1, 2),
    _TnSwCardAppBank1_Type()
)
tnSwCardAppBank1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwCardAppBank1.setStatus("current")


class _TnSwCardEmergBootBank_Type(SnmpAdminString):
    """Custom type tnSwCardEmergBootBank based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TnSwCardEmergBootBank_Type.__name__ = "SnmpAdminString"
_TnSwCardEmergBootBank_Object = MibTableColumn
tnSwCardEmergBootBank = _TnSwCardEmergBootBank_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 2, 1, 3),
    _TnSwCardEmergBootBank_Type()
)
tnSwCardEmergBootBank.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwCardEmergBootBank.setStatus("current")


class _TnSwCardUserBootBank_Type(SnmpAdminString):
    """Custom type tnSwCardUserBootBank based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TnSwCardUserBootBank_Type.__name__ = "SnmpAdminString"
_TnSwCardUserBootBank_Object = MibTableColumn
tnSwCardUserBootBank = _TnSwCardUserBootBank_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 2, 1, 4),
    _TnSwCardUserBootBank_Type()
)
tnSwCardUserBootBank.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwCardUserBootBank.setStatus("current")
_TnSwCardActiveBank_Type = TropicSwBank
_TnSwCardActiveBank_Object = MibTableColumn
tnSwCardActiveBank = _TnSwCardActiveBank_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 2, 1, 5),
    _TnSwCardActiveBank_Type()
)
tnSwCardActiveBank.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwCardActiveBank.setStatus("current")
_TnSwCardNextBootBank_Type = TropicSwBank
_TnSwCardNextBootBank_Object = MibTableColumn
tnSwCardNextBootBank = _TnSwCardNextBootBank_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 2, 1, 6),
    _TnSwCardNextBootBank_Type()
)
tnSwCardNextBootBank.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwCardNextBootBank.setStatus("current")
_TnSwCardBankToActivate_Type = TropicSwBank
_TnSwCardBankToActivate_Object = MibTableColumn
tnSwCardBankToActivate = _TnSwCardBankToActivate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 2, 1, 7),
    _TnSwCardBankToActivate_Type()
)
tnSwCardBankToActivate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSwCardBankToActivate.setStatus("current")


class _TnSwCardBankToLoad_Type(Integer32):
    """Custom type tnSwCardBankToLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("application", 2),
          ("boot", 3))
    )


_TnSwCardBankToLoad_Type.__name__ = "Integer32"
_TnSwCardBankToLoad_Object = MibTableColumn
tnSwCardBankToLoad = _TnSwCardBankToLoad_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 2, 1, 8),
    _TnSwCardBankToLoad_Type()
)
tnSwCardBankToLoad.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSwCardBankToLoad.setStatus("current")
_TnSwCardControl_Type = TropicSwControl
_TnSwCardControl_Object = MibTableColumn
tnSwCardControl = _TnSwCardControl_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 2, 1, 9),
    _TnSwCardControl_Type()
)
tnSwCardControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSwCardControl.setStatus("current")


class _TnSwCardReleaseDir_Type(SnmpAdminString):
    """Custom type tnSwCardReleaseDir based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSwCardReleaseDir_Type.__name__ = "SnmpAdminString"
_TnSwCardReleaseDir_Object = MibTableColumn
tnSwCardReleaseDir = _TnSwCardReleaseDir_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 2, 1, 17),
    _TnSwCardReleaseDir_Type()
)
tnSwCardReleaseDir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSwCardReleaseDir.setStatus("current")
_TnSwCardCurrentDscRpmCount_Type = Integer32
_TnSwCardCurrentDscRpmCount_Object = MibTableColumn
tnSwCardCurrentDscRpmCount = _TnSwCardCurrentDscRpmCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 2, 1, 18),
    _TnSwCardCurrentDscRpmCount_Type()
)
tnSwCardCurrentDscRpmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwCardCurrentDscRpmCount.setStatus("current")
_TnSwCardCurrentFsRpmCount_Type = Integer32
_TnSwCardCurrentFsRpmCount_Object = MibTableColumn
tnSwCardCurrentFsRpmCount = _TnSwCardCurrentFsRpmCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 2, 1, 19),
    _TnSwCardCurrentFsRpmCount_Type()
)
tnSwCardCurrentFsRpmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwCardCurrentFsRpmCount.setStatus("current")
_TnSwCardStandByDscRpmCount_Type = Integer32
_TnSwCardStandByDscRpmCount_Object = MibTableColumn
tnSwCardStandByDscRpmCount = _TnSwCardStandByDscRpmCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 2, 1, 20),
    _TnSwCardStandByDscRpmCount_Type()
)
tnSwCardStandByDscRpmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwCardStandByDscRpmCount.setStatus("current")
_TnSwCardStandByFsRpmCount_Type = Integer32
_TnSwCardStandByFsRpmCount_Object = MibTableColumn
tnSwCardStandByFsRpmCount = _TnSwCardStandByFsRpmCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 2, 1, 21),
    _TnSwCardStandByFsRpmCount_Type()
)
tnSwCardStandByFsRpmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwCardStandByFsRpmCount.setStatus("current")
_TnSwAuditScriptTable_Object = MibTable
tnSwAuditScriptTable = _TnSwAuditScriptTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 3)
)
if mibBuilder.loadTexts:
    tnSwAuditScriptTable.setStatus("current")
_TnSwAuditScriptEntry_Object = MibTableRow
tnSwAuditScriptEntry = _TnSwAuditScriptEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 3, 1)
)
tnSwAuditScriptEntry.setIndexNames(
    (0, "TROPIC-SOFTWARE-MIB", "tnSwAuditScriptStage"),
    (0, "TROPIC-SOFTWARE-MIB", "tnSwAuditScriptStep"),
)
if mibBuilder.loadTexts:
    tnSwAuditScriptEntry.setStatus("current")
_TnSwAuditScriptStage_Type = Unsigned32
_TnSwAuditScriptStage_Object = MibTableColumn
tnSwAuditScriptStage = _TnSwAuditScriptStage_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 3, 1, 1),
    _TnSwAuditScriptStage_Type()
)
tnSwAuditScriptStage.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSwAuditScriptStage.setStatus("current")
_TnSwAuditScriptStep_Type = Unsigned32
_TnSwAuditScriptStep_Object = MibTableColumn
tnSwAuditScriptStep = _TnSwAuditScriptStep_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 3, 1, 2),
    _TnSwAuditScriptStep_Type()
)
tnSwAuditScriptStep.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSwAuditScriptStep.setStatus("current")
_TnSwAuditScriptShelf_Type = TropicShelfIndexType
_TnSwAuditScriptShelf_Object = MibTableColumn
tnSwAuditScriptShelf = _TnSwAuditScriptShelf_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 3, 1, 3),
    _TnSwAuditScriptShelf_Type()
)
tnSwAuditScriptShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwAuditScriptShelf.setStatus("current")
_TnSwAuditScriptSlot_Type = TropicSlotIndexType
_TnSwAuditScriptSlot_Object = MibTableColumn
tnSwAuditScriptSlot = _TnSwAuditScriptSlot_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 3, 1, 4),
    _TnSwAuditScriptSlot_Type()
)
tnSwAuditScriptSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwAuditScriptSlot.setStatus("current")
_TnSwAuditScriptCardType_Type = ObjectIdentifier
_TnSwAuditScriptCardType_Object = MibTableColumn
tnSwAuditScriptCardType = _TnSwAuditScriptCardType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 3, 1, 5),
    _TnSwAuditScriptCardType_Type()
)
tnSwAuditScriptCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwAuditScriptCardType.setStatus("current")


class _TnSwAuditScriptAction_Type(SnmpAdminString):
    """Custom type tnSwAuditScriptAction based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSwAuditScriptAction_Type.__name__ = "SnmpAdminString"
_TnSwAuditScriptAction_Object = MibTableColumn
tnSwAuditScriptAction = _TnSwAuditScriptAction_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 3, 1, 7),
    _TnSwAuditScriptAction_Type()
)
tnSwAuditScriptAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwAuditScriptAction.setStatus("current")


class _TnSwAuditScriptActionStatus_Type(SnmpAdminString):
    """Custom type tnSwAuditScriptActionStatus based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSwAuditScriptActionStatus_Type.__name__ = "SnmpAdminString"
_TnSwAuditScriptActionStatus_Object = MibTableColumn
tnSwAuditScriptActionStatus = _TnSwAuditScriptActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 3, 1, 8),
    _TnSwAuditScriptActionStatus_Type()
)
tnSwAuditScriptActionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwAuditScriptActionStatus.setStatus("current")
_TnSwAuditScriptActionResult_Type = TropicSwLastOperationResult
_TnSwAuditScriptActionResult_Object = MibTableColumn
tnSwAuditScriptActionResult = _TnSwAuditScriptActionResult_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 3, 1, 9),
    _TnSwAuditScriptActionResult_Type()
)
tnSwAuditScriptActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwAuditScriptActionResult.setStatus("current")
_TnSwAuditScriptActionPercentCompleted_Type = TropicSwLastOperationPercentCompleted
_TnSwAuditScriptActionPercentCompleted_Object = MibTableColumn
tnSwAuditScriptActionPercentCompleted = _TnSwAuditScriptActionPercentCompleted_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 3, 1, 10),
    _TnSwAuditScriptActionPercentCompleted_Type()
)
tnSwAuditScriptActionPercentCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwAuditScriptActionPercentCompleted.setStatus("current")
_TnSwAuditScriptResultTimeStamp_Type = Unsigned32
_TnSwAuditScriptResultTimeStamp_Object = MibTableColumn
tnSwAuditScriptResultTimeStamp = _TnSwAuditScriptResultTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 3, 1, 11),
    _TnSwAuditScriptResultTimeStamp_Type()
)
tnSwAuditScriptResultTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwAuditScriptResultTimeStamp.setStatus("current")
_TnSwCpldTable_Object = MibTable
tnSwCpldTable = _TnSwCpldTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 4)
)
if mibBuilder.loadTexts:
    tnSwCpldTable.setStatus("current")
_TnSwCpldEntry_Object = MibTableRow
tnSwCpldEntry = _TnSwCpldEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 4, 1)
)
tnSwCpldEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnSwCpldEntry.setStatus("current")


class _TnSwCpldProgramControl_Type(Integer32):
    """Custom type tnSwCpldProgramControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noCmd", 1),
          ("gentle", 2),
          ("force", 3))
    )


_TnSwCpldProgramControl_Type.__name__ = "Integer32"
_TnSwCpldProgramControl_Object = MibTableColumn
tnSwCpldProgramControl = _TnSwCpldProgramControl_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 4, 1, 1),
    _TnSwCpldProgramControl_Type()
)
tnSwCpldProgramControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSwCpldProgramControl.setStatus("current")
_TnFwCardTable_Object = MibTable
tnFwCardTable = _TnFwCardTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 5)
)
if mibBuilder.loadTexts:
    tnFwCardTable.setStatus("current")
_TnFwCardEntry_Object = MibTableRow
tnFwCardEntry = _TnFwCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 5, 1)
)
tnFwCardEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnFwCardEntry.setStatus("current")


class _TnFwCardCurrentBundle_Type(SnmpAdminString):
    """Custom type tnFwCardCurrentBundle based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TnFwCardCurrentBundle_Type.__name__ = "SnmpAdminString"
_TnFwCardCurrentBundle_Object = MibTableColumn
tnFwCardCurrentBundle = _TnFwCardCurrentBundle_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 5, 1, 1),
    _TnFwCardCurrentBundle_Type()
)
tnFwCardCurrentBundle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnFwCardCurrentBundle.setStatus("current")
_TnFwCardLoadedAt_Type = Unsigned32
_TnFwCardLoadedAt_Object = MibTableColumn
tnFwCardLoadedAt = _TnFwCardLoadedAt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 5, 1, 2),
    _TnFwCardLoadedAt_Type()
)
tnFwCardLoadedAt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnFwCardLoadedAt.setStatus("current")


class _TnFwCardLoadBundle_Type(SnmpAdminString):
    """Custom type tnFwCardLoadBundle based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnFwCardLoadBundle_Type.__name__ = "SnmpAdminString"
_TnFwCardLoadBundle_Object = MibTableColumn
tnFwCardLoadBundle = _TnFwCardLoadBundle_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 5, 1, 3),
    _TnFwCardLoadBundle_Type()
)
tnFwCardLoadBundle.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnFwCardLoadBundle.setStatus("current")
_TnFwCardProvisionedAt_Type = Unsigned32
_TnFwCardProvisionedAt_Object = MibTableColumn
tnFwCardProvisionedAt = _TnFwCardProvisionedAt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 5, 1, 4),
    _TnFwCardProvisionedAt_Type()
)
tnFwCardProvisionedAt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnFwCardProvisionedAt.setStatus("current")


class _TnFwCardLoadState_Type(Integer32):
    """Custom type tnFwCardLoadState based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("loaded", 2),
          ("init1", 3),
          ("init2", 4),
          ("init3", 5),
          ("init4", 6),
          ("init5", 7),
          ("init6", 8),
          ("init7", 9),
          ("init8", 10),
          ("init9", 11),
          ("init10", 12),
          ("failed", 13),
          ("timeOut", 14))
    )


_TnFwCardLoadState_Type.__name__ = "Integer32"
_TnFwCardLoadState_Object = MibTableColumn
tnFwCardLoadState = _TnFwCardLoadState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 5, 1, 5),
    _TnFwCardLoadState_Type()
)
tnFwCardLoadState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnFwCardLoadState.setStatus("current")
_TnFwCardWatchDog_Type = Unsigned32
_TnFwCardWatchDog_Object = MibTableColumn
tnFwCardWatchDog = _TnFwCardWatchDog_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 5, 1, 6),
    _TnFwCardWatchDog_Type()
)
tnFwCardWatchDog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnFwCardWatchDog.setStatus("current")


class _TnFwCardProvisioningInfo_Type(SnmpAdminString):
    """Custom type tnFwCardProvisioningInfo based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_TnFwCardProvisioningInfo_Type.__name__ = "SnmpAdminString"
_TnFwCardProvisioningInfo_Object = MibTableColumn
tnFwCardProvisioningInfo = _TnFwCardProvisioningInfo_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 5, 1, 7),
    _TnFwCardProvisioningInfo_Type()
)
tnFwCardProvisioningInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnFwCardProvisioningInfo.setStatus("current")


class _TnFwCardFpgaCapability_Type(SnmpAdminString):
    """Custom type tnFwCardFpgaCapability based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_TnFwCardFpgaCapability_Type.__name__ = "SnmpAdminString"
_TnFwCardFpgaCapability_Object = MibTableColumn
tnFwCardFpgaCapability = _TnFwCardFpgaCapability_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 5, 1, 8),
    _TnFwCardFpgaCapability_Type()
)
tnFwCardFpgaCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnFwCardFpgaCapability.setStatus("current")
_TnInstalledFwTable_Object = MibTable
tnInstalledFwTable = _TnInstalledFwTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 6)
)
if mibBuilder.loadTexts:
    tnInstalledFwTable.setStatus("current")
_TnInstalledFwEntry_Object = MibTableRow
tnInstalledFwEntry = _TnInstalledFwEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 6, 1)
)
tnInstalledFwEntry.setIndexNames(
    (0, "TROPIC-SOFTWARE-MIB", "tnInstalledFwCardType"),
    (0, "TROPIC-SOFTWARE-MIB", "tnInstalledFwFileName"),
)
if mibBuilder.loadTexts:
    tnInstalledFwEntry.setStatus("current")
_TnInstalledFwCardType_Type = Unsigned32
_TnInstalledFwCardType_Object = MibTableColumn
tnInstalledFwCardType = _TnInstalledFwCardType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 6, 1, 1),
    _TnInstalledFwCardType_Type()
)
tnInstalledFwCardType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnInstalledFwCardType.setStatus("current")
_TnInstalledFwFileName_Type = SnmpAdminString
_TnInstalledFwFileName_Object = MibTableColumn
tnInstalledFwFileName = _TnInstalledFwFileName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 6, 1, 2),
    _TnInstalledFwFileName_Type()
)
tnInstalledFwFileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnInstalledFwFileName.setStatus("current")


class _TnInstalledFwIsDefault_Type(TruthValue):
    """Custom type tnInstalledFwIsDefault based on TruthValue"""
    defaultValue = 2


_TnInstalledFwIsDefault_Type.__name__ = "TruthValue"
_TnInstalledFwIsDefault_Object = MibTableColumn
tnInstalledFwIsDefault = _TnInstalledFwIsDefault_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 6, 1, 3),
    _TnInstalledFwIsDefault_Type()
)
tnInstalledFwIsDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnInstalledFwIsDefault.setStatus("current")
_TnPortGroupTable_Object = MibTable
tnPortGroupTable = _TnPortGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 7)
)
if mibBuilder.loadTexts:
    tnPortGroupTable.setStatus("current")
_TnPortGroupEntry_Object = MibTableRow
tnPortGroupEntry = _TnPortGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 7, 1)
)
tnPortGroupEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnPortGroupEntry.setStatus("current")
_TnPortGroupMode_Type = AluWdmPortGroupMode
_TnPortGroupMode_Object = MibTableColumn
tnPortGroupMode = _TnPortGroupMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 7, 1, 1),
    _TnPortGroupMode_Type()
)
tnPortGroupMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPortGroupMode.setStatus("current")


class _TnPortGroupFwDownload_Type(SnmpAdminString):
    """Custom type tnPortGroupFwDownload based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnPortGroupFwDownload_Type.__name__ = "SnmpAdminString"
_TnPortGroupFwDownload_Object = MibTableColumn
tnPortGroupFwDownload = _TnPortGroupFwDownload_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 7, 1, 2),
    _TnPortGroupFwDownload_Type()
)
tnPortGroupFwDownload.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPortGroupFwDownload.setStatus("current")


class _TnPortGroupFwCurrent_Type(SnmpAdminString):
    """Custom type tnPortGroupFwCurrent based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnPortGroupFwCurrent_Type.__name__ = "SnmpAdminString"
_TnPortGroupFwCurrent_Object = MibTableColumn
tnPortGroupFwCurrent = _TnPortGroupFwCurrent_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 7, 1, 3),
    _TnPortGroupFwCurrent_Type()
)
tnPortGroupFwCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortGroupFwCurrent.setStatus("current")
_TnInstalledFwPortGroupTable_Object = MibTable
tnInstalledFwPortGroupTable = _TnInstalledFwPortGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 8)
)
if mibBuilder.loadTexts:
    tnInstalledFwPortGroupTable.setStatus("current")
_TnInstalledFwPortGroupEntry_Object = MibTableRow
tnInstalledFwPortGroupEntry = _TnInstalledFwPortGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 8, 1)
)
tnInstalledFwPortGroupEntry.setIndexNames(
    (0, "TROPIC-SOFTWARE-MIB", "tnInstalledFwCardType"),
    (0, "TROPIC-SOFTWARE-MIB", "tnInstalledFwFileName"),
    (0, "TROPIC-SOFTWARE-MIB", "tnInstalledFwPortGroupMode"),
    (0, "TROPIC-SOFTWARE-MIB", "tnInstalledFwPortGroupFw"),
)
if mibBuilder.loadTexts:
    tnInstalledFwPortGroupEntry.setStatus("current")
_TnInstalledFwPortGroupMode_Type = AluWdmPortGroupMode
_TnInstalledFwPortGroupMode_Object = MibTableColumn
tnInstalledFwPortGroupMode = _TnInstalledFwPortGroupMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 8, 1, 1),
    _TnInstalledFwPortGroupMode_Type()
)
tnInstalledFwPortGroupMode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnInstalledFwPortGroupMode.setStatus("current")


class _TnInstalledFwPortGroupFw_Type(SnmpAdminString):
    """Custom type tnInstalledFwPortGroupFw based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnInstalledFwPortGroupFw_Type.__name__ = "SnmpAdminString"
_TnInstalledFwPortGroupFw_Object = MibTableColumn
tnInstalledFwPortGroupFw = _TnInstalledFwPortGroupFw_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 8, 1, 2),
    _TnInstalledFwPortGroupFw_Type()
)
tnInstalledFwPortGroupFw.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnInstalledFwPortGroupFw.setStatus("current")
_TnInstalledFwPortGroupIsDefault_Type = TruthValue
_TnInstalledFwPortGroupIsDefault_Object = MibTableColumn
tnInstalledFwPortGroupIsDefault = _TnInstalledFwPortGroupIsDefault_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 8, 1, 3),
    _TnInstalledFwPortGroupIsDefault_Type()
)
tnInstalledFwPortGroupIsDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnInstalledFwPortGroupIsDefault.setStatus("current")
_TnFwHitlessCardTable_Object = MibTable
tnFwHitlessCardTable = _TnFwHitlessCardTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 9)
)
if mibBuilder.loadTexts:
    tnFwHitlessCardTable.setStatus("current")
_TnFwHitlessCardEntry_Object = MibTableRow
tnFwHitlessCardEntry = _TnFwHitlessCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 9, 1)
)
tnFwHitlessCardEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnFwHitlessCardEntry.setStatus("current")
_TnFwHitlessCardTrigger_Type = TruthValue
_TnFwHitlessCardTrigger_Object = MibTableColumn
tnFwHitlessCardTrigger = _TnFwHitlessCardTrigger_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 9, 1, 1),
    _TnFwHitlessCardTrigger_Type()
)
tnFwHitlessCardTrigger.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnFwHitlessCardTrigger.setStatus("current")


class _TnFwHitlessCardLoadState_Type(Integer32):
    """Custom type tnFwHitlessCardLoadState based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("loaded", 2),
          ("initNsa1", 3),
          ("initNsa2", 4),
          ("initNsa3", 5),
          ("initNsa4", 6),
          ("initNsa5", 7),
          ("initNsa6", 8),
          ("initNsa7", 9),
          ("initNsa8", 10),
          ("initNsa9", 11),
          ("initNsa10", 12),
          ("failed", 13),
          ("timeOut", 14))
    )


_TnFwHitlessCardLoadState_Type.__name__ = "Integer32"
_TnFwHitlessCardLoadState_Object = MibTableColumn
tnFwHitlessCardLoadState = _TnFwHitlessCardLoadState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 9, 1, 2),
    _TnFwHitlessCardLoadState_Type()
)
tnFwHitlessCardLoadState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnFwHitlessCardLoadState.setStatus("current")
_TnFwHitlessCardWatchDog_Type = Unsigned32
_TnFwHitlessCardWatchDog_Object = MibTableColumn
tnFwHitlessCardWatchDog = _TnFwHitlessCardWatchDog_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 9, 1, 3),
    _TnFwHitlessCardWatchDog_Type()
)
tnFwHitlessCardWatchDog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnFwHitlessCardWatchDog.setStatus("current")
_TnPortFwTable_Object = MibTable
tnPortFwTable = _TnPortFwTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 10)
)
if mibBuilder.loadTexts:
    tnPortFwTable.setStatus("current")
_TnPortFwEntry_Object = MibTableRow
tnPortFwEntry = _TnPortFwEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 10, 1)
)
tnPortFwEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnPortFwEntry.setStatus("current")


class _TnPortFwFunction_Type(SnmpAdminString):
    """Custom type tnPortFwFunction based on SnmpAdminString"""
    defaultValue = OctetString("profile")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnPortFwFunction_Type.__name__ = "SnmpAdminString"
_TnPortFwFunction_Object = MibTableColumn
tnPortFwFunction = _TnPortFwFunction_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 10, 1, 1),
    _TnPortFwFunction_Type()
)
tnPortFwFunction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPortFwFunction.setStatus("current")


class _TnPortFwLoadBundle_Type(SnmpAdminString):
    """Custom type tnPortFwLoadBundle based on SnmpAdminString"""
    defaultValue = OctetString("default")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnPortFwLoadBundle_Type.__name__ = "SnmpAdminString"
_TnPortFwLoadBundle_Object = MibTableColumn
tnPortFwLoadBundle = _TnPortFwLoadBundle_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 10, 1, 2),
    _TnPortFwLoadBundle_Type()
)
tnPortFwLoadBundle.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPortFwLoadBundle.setStatus("current")


class _TnPortFwHitless_Type(TruthValue):
    """Custom type tnPortFwHitless based on TruthValue"""
    defaultValue = 2


_TnPortFwHitless_Type.__name__ = "TruthValue"
_TnPortFwHitless_Object = MibTableColumn
tnPortFwHitless = _TnPortFwHitless_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 10, 1, 3),
    _TnPortFwHitless_Type()
)
tnPortFwHitless.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPortFwHitless.setStatus("current")


class _TnPortFwHitlessLoadState_Type(Integer32):
    """Custom type tnPortFwHitlessLoadState based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("loaded", 2),
          ("initNsa1", 3),
          ("initNsa2", 4),
          ("initNsa3", 5),
          ("initNsa4", 6),
          ("initNsa5", 7),
          ("initNsa6", 8),
          ("initNsa7", 9),
          ("initNsa8", 10),
          ("initNsa9", 11),
          ("initNsa10", 12),
          ("failed", 13),
          ("timeOut", 14))
    )


_TnPortFwHitlessLoadState_Type.__name__ = "Integer32"
_TnPortFwHitlessLoadState_Object = MibTableColumn
tnPortFwHitlessLoadState = _TnPortFwHitlessLoadState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 10, 1, 4),
    _TnPortFwHitlessLoadState_Type()
)
tnPortFwHitlessLoadState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortFwHitlessLoadState.setStatus("current")


class _TnPortFwLoadState_Type(Integer32):
    """Custom type tnPortFwLoadState based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("loaded", 2),
          ("init1", 3),
          ("init2", 4),
          ("init3", 5),
          ("init4", 6),
          ("init5", 7),
          ("init6", 8),
          ("init7", 9),
          ("init8", 10),
          ("init9", 11),
          ("init10", 12),
          ("failed", 13),
          ("timeOut", 14))
    )


_TnPortFwLoadState_Type.__name__ = "Integer32"
_TnPortFwLoadState_Object = MibTableColumn
tnPortFwLoadState = _TnPortFwLoadState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 10, 1, 5),
    _TnPortFwLoadState_Type()
)
tnPortFwLoadState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortFwLoadState.setStatus("current")


class _TnPortFwCurrentBundle_Type(SnmpAdminString):
    """Custom type tnPortFwCurrentBundle based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TnPortFwCurrentBundle_Type.__name__ = "SnmpAdminString"
_TnPortFwCurrentBundle_Object = MibTableColumn
tnPortFwCurrentBundle = _TnPortFwCurrentBundle_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 10, 1, 6),
    _TnPortFwCurrentBundle_Type()
)
tnPortFwCurrentBundle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortFwCurrentBundle.setStatus("current")
_TnPortFwLoadedAt_Type = Unsigned32
_TnPortFwLoadedAt_Object = MibTableColumn
tnPortFwLoadedAt = _TnPortFwLoadedAt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 10, 1, 7),
    _TnPortFwLoadedAt_Type()
)
tnPortFwLoadedAt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortFwLoadedAt.setStatus("current")
_TnPortFwProvisionedAt_Type = Unsigned32
_TnPortFwProvisionedAt_Object = MibTableColumn
tnPortFwProvisionedAt = _TnPortFwProvisionedAt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 10, 1, 8),
    _TnPortFwProvisionedAt_Type()
)
tnPortFwProvisionedAt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortFwProvisionedAt.setStatus("current")
_TnPortFwLoadTimeOut_Type = Unsigned32
_TnPortFwLoadTimeOut_Object = MibTableColumn
tnPortFwLoadTimeOut = _TnPortFwLoadTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 10, 1, 9),
    _TnPortFwLoadTimeOut_Type()
)
tnPortFwLoadTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortFwLoadTimeOut.setStatus("current")
_TnPortFwHitlessLoadTimeOut_Type = Unsigned32
_TnPortFwHitlessLoadTimeOut_Object = MibTableColumn
tnPortFwHitlessLoadTimeOut = _TnPortFwHitlessLoadTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 10, 1, 10),
    _TnPortFwHitlessLoadTimeOut_Type()
)
tnPortFwHitlessLoadTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortFwHitlessLoadTimeOut.setStatus("current")


class _TnPortFwProvisioningInfo_Type(SnmpAdminString):
    """Custom type tnPortFwProvisioningInfo based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 520),
    )


_TnPortFwProvisioningInfo_Type.__name__ = "SnmpAdminString"
_TnPortFwProvisioningInfo_Object = MibTableColumn
tnPortFwProvisioningInfo = _TnPortFwProvisioningInfo_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 10, 1, 11),
    _TnPortFwProvisioningInfo_Type()
)
tnPortFwProvisioningInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPortFwProvisioningInfo.setStatus("current")
_TnInstalledFwPortTable_Object = MibTable
tnInstalledFwPortTable = _TnInstalledFwPortTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 11)
)
if mibBuilder.loadTexts:
    tnInstalledFwPortTable.setStatus("current")
_TnInstalledFwPortEntry_Object = MibTableRow
tnInstalledFwPortEntry = _TnInstalledFwPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 11, 1)
)
tnInstalledFwPortEntry.setIndexNames(
    (0, "TROPIC-SOFTWARE-MIB", "tnInstalledFwPortModuleType"),
    (0, "TROPIC-SOFTWARE-MIB", "tnInstalledFwPortFileName"),
)
if mibBuilder.loadTexts:
    tnInstalledFwPortEntry.setStatus("current")
_TnInstalledFwPortModuleType_Type = Unsigned32
_TnInstalledFwPortModuleType_Object = MibTableColumn
tnInstalledFwPortModuleType = _TnInstalledFwPortModuleType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 11, 1, 1),
    _TnInstalledFwPortModuleType_Type()
)
tnInstalledFwPortModuleType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnInstalledFwPortModuleType.setStatus("current")
_TnInstalledFwPortFileName_Type = SnmpAdminString
_TnInstalledFwPortFileName_Object = MibTableColumn
tnInstalledFwPortFileName = _TnInstalledFwPortFileName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 11, 1, 2),
    _TnInstalledFwPortFileName_Type()
)
tnInstalledFwPortFileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnInstalledFwPortFileName.setStatus("current")


class _TnInstalledFwPortIsDefault_Type(TruthValue):
    """Custom type tnInstalledFwPortIsDefault based on TruthValue"""
    defaultValue = 2


_TnInstalledFwPortIsDefault_Type.__name__ = "TruthValue"
_TnInstalledFwPortIsDefault_Object = MibTableColumn
tnInstalledFwPortIsDefault = _TnInstalledFwPortIsDefault_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 11, 1, 3),
    _TnInstalledFwPortIsDefault_Type()
)
tnInstalledFwPortIsDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnInstalledFwPortIsDefault.setStatus("current")
_TnSwCardDynamicTable_Object = MibTable
tnSwCardDynamicTable = _TnSwCardDynamicTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 12)
)
if mibBuilder.loadTexts:
    tnSwCardDynamicTable.setStatus("current")
_TnSwCardDynamicEntry_Object = MibTableRow
tnSwCardDynamicEntry = _TnSwCardDynamicEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 12, 1)
)
tnSwCardDynamicEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnSwCardDynamicEntry.setStatus("current")


class _TnSwCardDynamicFeatureFullCurrent1_Type(SnmpAdminString):
    """Custom type tnSwCardDynamicFeatureFullCurrent1 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_TnSwCardDynamicFeatureFullCurrent1_Type.__name__ = "SnmpAdminString"
_TnSwCardDynamicFeatureFullCurrent1_Object = MibTableColumn
tnSwCardDynamicFeatureFullCurrent1 = _TnSwCardDynamicFeatureFullCurrent1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 12, 1, 1),
    _TnSwCardDynamicFeatureFullCurrent1_Type()
)
tnSwCardDynamicFeatureFullCurrent1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwCardDynamicFeatureFullCurrent1.setStatus("current")


class _TnSwCardDynamicFeatureFullCurrent2_Type(SnmpAdminString):
    """Custom type tnSwCardDynamicFeatureFullCurrent2 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_TnSwCardDynamicFeatureFullCurrent2_Type.__name__ = "SnmpAdminString"
_TnSwCardDynamicFeatureFullCurrent2_Object = MibTableColumn
tnSwCardDynamicFeatureFullCurrent2 = _TnSwCardDynamicFeatureFullCurrent2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 12, 1, 2),
    _TnSwCardDynamicFeatureFullCurrent2_Type()
)
tnSwCardDynamicFeatureFullCurrent2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwCardDynamicFeatureFullCurrent2.setStatus("current")


class _TnSwCardDynamicFeatureFullStandby1_Type(SnmpAdminString):
    """Custom type tnSwCardDynamicFeatureFullStandby1 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_TnSwCardDynamicFeatureFullStandby1_Type.__name__ = "SnmpAdminString"
_TnSwCardDynamicFeatureFullStandby1_Object = MibTableColumn
tnSwCardDynamicFeatureFullStandby1 = _TnSwCardDynamicFeatureFullStandby1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 12, 1, 3),
    _TnSwCardDynamicFeatureFullStandby1_Type()
)
tnSwCardDynamicFeatureFullStandby1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwCardDynamicFeatureFullStandby1.setStatus("current")


class _TnSwCardDynamicFeatureFullStandby2_Type(SnmpAdminString):
    """Custom type tnSwCardDynamicFeatureFullStandby2 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_TnSwCardDynamicFeatureFullStandby2_Type.__name__ = "SnmpAdminString"
_TnSwCardDynamicFeatureFullStandby2_Object = MibTableColumn
tnSwCardDynamicFeatureFullStandby2 = _TnSwCardDynamicFeatureFullStandby2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 12, 1, 4),
    _TnSwCardDynamicFeatureFullStandby2_Type()
)
tnSwCardDynamicFeatureFullStandby2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwCardDynamicFeatureFullStandby2.setStatus("current")


class _TnSwCardDynamicFeatureAvailableCurrent1_Type(SnmpAdminString):
    """Custom type tnSwCardDynamicFeatureAvailableCurrent1 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_TnSwCardDynamicFeatureAvailableCurrent1_Type.__name__ = "SnmpAdminString"
_TnSwCardDynamicFeatureAvailableCurrent1_Object = MibTableColumn
tnSwCardDynamicFeatureAvailableCurrent1 = _TnSwCardDynamicFeatureAvailableCurrent1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 12, 1, 5),
    _TnSwCardDynamicFeatureAvailableCurrent1_Type()
)
tnSwCardDynamicFeatureAvailableCurrent1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwCardDynamicFeatureAvailableCurrent1.setStatus("current")


class _TnSwCardDynamicFeatureAvailableCurrent2_Type(SnmpAdminString):
    """Custom type tnSwCardDynamicFeatureAvailableCurrent2 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_TnSwCardDynamicFeatureAvailableCurrent2_Type.__name__ = "SnmpAdminString"
_TnSwCardDynamicFeatureAvailableCurrent2_Object = MibTableColumn
tnSwCardDynamicFeatureAvailableCurrent2 = _TnSwCardDynamicFeatureAvailableCurrent2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 12, 1, 6),
    _TnSwCardDynamicFeatureAvailableCurrent2_Type()
)
tnSwCardDynamicFeatureAvailableCurrent2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwCardDynamicFeatureAvailableCurrent2.setStatus("current")


class _TnSwCardDynamicFeatureAvailableStandby1_Type(SnmpAdminString):
    """Custom type tnSwCardDynamicFeatureAvailableStandby1 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_TnSwCardDynamicFeatureAvailableStandby1_Type.__name__ = "SnmpAdminString"
_TnSwCardDynamicFeatureAvailableStandby1_Object = MibTableColumn
tnSwCardDynamicFeatureAvailableStandby1 = _TnSwCardDynamicFeatureAvailableStandby1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 12, 1, 7),
    _TnSwCardDynamicFeatureAvailableStandby1_Type()
)
tnSwCardDynamicFeatureAvailableStandby1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwCardDynamicFeatureAvailableStandby1.setStatus("current")


class _TnSwCardDynamicFeatureAvailableStandby2_Type(SnmpAdminString):
    """Custom type tnSwCardDynamicFeatureAvailableStandby2 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_TnSwCardDynamicFeatureAvailableStandby2_Type.__name__ = "SnmpAdminString"
_TnSwCardDynamicFeatureAvailableStandby2_Object = MibTableColumn
tnSwCardDynamicFeatureAvailableStandby2 = _TnSwCardDynamicFeatureAvailableStandby2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 12, 1, 8),
    _TnSwCardDynamicFeatureAvailableStandby2_Type()
)
tnSwCardDynamicFeatureAvailableStandby2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwCardDynamicFeatureAvailableStandby2.setStatus("current")


class _TnSwCardDynamicFeatureExcludedCurrent1_Type(SnmpAdminString):
    """Custom type tnSwCardDynamicFeatureExcludedCurrent1 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_TnSwCardDynamicFeatureExcludedCurrent1_Type.__name__ = "SnmpAdminString"
_TnSwCardDynamicFeatureExcludedCurrent1_Object = MibTableColumn
tnSwCardDynamicFeatureExcludedCurrent1 = _TnSwCardDynamicFeatureExcludedCurrent1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 12, 1, 9),
    _TnSwCardDynamicFeatureExcludedCurrent1_Type()
)
tnSwCardDynamicFeatureExcludedCurrent1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwCardDynamicFeatureExcludedCurrent1.setStatus("current")


class _TnSwCardDynamicFeatureExcludedCurrent2_Type(SnmpAdminString):
    """Custom type tnSwCardDynamicFeatureExcludedCurrent2 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_TnSwCardDynamicFeatureExcludedCurrent2_Type.__name__ = "SnmpAdminString"
_TnSwCardDynamicFeatureExcludedCurrent2_Object = MibTableColumn
tnSwCardDynamicFeatureExcludedCurrent2 = _TnSwCardDynamicFeatureExcludedCurrent2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 12, 1, 10),
    _TnSwCardDynamicFeatureExcludedCurrent2_Type()
)
tnSwCardDynamicFeatureExcludedCurrent2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwCardDynamicFeatureExcludedCurrent2.setStatus("current")


class _TnSwCardDynamicFeatureExcludedStandby1_Type(SnmpAdminString):
    """Custom type tnSwCardDynamicFeatureExcludedStandby1 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_TnSwCardDynamicFeatureExcludedStandby1_Type.__name__ = "SnmpAdminString"
_TnSwCardDynamicFeatureExcludedStandby1_Object = MibTableColumn
tnSwCardDynamicFeatureExcludedStandby1 = _TnSwCardDynamicFeatureExcludedStandby1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 12, 1, 11),
    _TnSwCardDynamicFeatureExcludedStandby1_Type()
)
tnSwCardDynamicFeatureExcludedStandby1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwCardDynamicFeatureExcludedStandby1.setStatus("current")


class _TnSwCardDynamicFeatureExcludedStandby2_Type(SnmpAdminString):
    """Custom type tnSwCardDynamicFeatureExcludedStandby2 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_TnSwCardDynamicFeatureExcludedStandby2_Type.__name__ = "SnmpAdminString"
_TnSwCardDynamicFeatureExcludedStandby2_Object = MibTableColumn
tnSwCardDynamicFeatureExcludedStandby2 = _TnSwCardDynamicFeatureExcludedStandby2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 12, 1, 12),
    _TnSwCardDynamicFeatureExcludedStandby2_Type()
)
tnSwCardDynamicFeatureExcludedStandby2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwCardDynamicFeatureExcludedStandby2.setStatus("current")
_TnSwCardDynamicDscRpmCountFullCurrent_Type = Integer32
_TnSwCardDynamicDscRpmCountFullCurrent_Object = MibTableColumn
tnSwCardDynamicDscRpmCountFullCurrent = _TnSwCardDynamicDscRpmCountFullCurrent_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 12, 1, 13),
    _TnSwCardDynamicDscRpmCountFullCurrent_Type()
)
tnSwCardDynamicDscRpmCountFullCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwCardDynamicDscRpmCountFullCurrent.setStatus("current")
_TnSwCardDynamicFsRpmCountFullCurrent_Type = Integer32
_TnSwCardDynamicFsRpmCountFullCurrent_Object = MibTableColumn
tnSwCardDynamicFsRpmCountFullCurrent = _TnSwCardDynamicFsRpmCountFullCurrent_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 12, 1, 14),
    _TnSwCardDynamicFsRpmCountFullCurrent_Type()
)
tnSwCardDynamicFsRpmCountFullCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwCardDynamicFsRpmCountFullCurrent.setStatus("current")


class _TnSwCardDynamicActiveReleaseFullCurrent_Type(SnmpAdminString):
    """Custom type tnSwCardDynamicActiveReleaseFullCurrent based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TnSwCardDynamicActiveReleaseFullCurrent_Type.__name__ = "SnmpAdminString"
_TnSwCardDynamicActiveReleaseFullCurrent_Object = MibTableColumn
tnSwCardDynamicActiveReleaseFullCurrent = _TnSwCardDynamicActiveReleaseFullCurrent_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 12, 1, 15),
    _TnSwCardDynamicActiveReleaseFullCurrent_Type()
)
tnSwCardDynamicActiveReleaseFullCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwCardDynamicActiveReleaseFullCurrent.setStatus("current")
_TnSwCardDynamicDscRpmCountFullStandby_Type = Integer32
_TnSwCardDynamicDscRpmCountFullStandby_Object = MibTableColumn
tnSwCardDynamicDscRpmCountFullStandby = _TnSwCardDynamicDscRpmCountFullStandby_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 12, 1, 16),
    _TnSwCardDynamicDscRpmCountFullStandby_Type()
)
tnSwCardDynamicDscRpmCountFullStandby.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwCardDynamicDscRpmCountFullStandby.setStatus("current")
_TnSwCardDynamicFsRpmCountFullStandby_Type = Integer32
_TnSwCardDynamicFsRpmCountFullStandby_Object = MibTableColumn
tnSwCardDynamicFsRpmCountFullStandby = _TnSwCardDynamicFsRpmCountFullStandby_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 12, 1, 17),
    _TnSwCardDynamicFsRpmCountFullStandby_Type()
)
tnSwCardDynamicFsRpmCountFullStandby.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwCardDynamicFsRpmCountFullStandby.setStatus("current")


class _TnSwCardDynamicActiveReleaseFullStandby_Type(SnmpAdminString):
    """Custom type tnSwCardDynamicActiveReleaseFullStandby based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TnSwCardDynamicActiveReleaseFullStandby_Type.__name__ = "SnmpAdminString"
_TnSwCardDynamicActiveReleaseFullStandby_Object = MibTableColumn
tnSwCardDynamicActiveReleaseFullStandby = _TnSwCardDynamicActiveReleaseFullStandby_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 12, 1, 18),
    _TnSwCardDynamicActiveReleaseFullStandby_Type()
)
tnSwCardDynamicActiveReleaseFullStandby.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwCardDynamicActiveReleaseFullStandby.setStatus("current")
_TnSwCardDynamicDscRpmCountAvailableCurrent_Type = Integer32
_TnSwCardDynamicDscRpmCountAvailableCurrent_Object = MibTableColumn
tnSwCardDynamicDscRpmCountAvailableCurrent = _TnSwCardDynamicDscRpmCountAvailableCurrent_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 12, 1, 19),
    _TnSwCardDynamicDscRpmCountAvailableCurrent_Type()
)
tnSwCardDynamicDscRpmCountAvailableCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwCardDynamicDscRpmCountAvailableCurrent.setStatus("current")
_TnSwCardDynamicFsRpmCountAvailableCurrent_Type = Integer32
_TnSwCardDynamicFsRpmCountAvailableCurrent_Object = MibTableColumn
tnSwCardDynamicFsRpmCountAvailableCurrent = _TnSwCardDynamicFsRpmCountAvailableCurrent_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 12, 1, 20),
    _TnSwCardDynamicFsRpmCountAvailableCurrent_Type()
)
tnSwCardDynamicFsRpmCountAvailableCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwCardDynamicFsRpmCountAvailableCurrent.setStatus("current")


class _TnSwCardDynamicActiveReleaseAvailableCurrent_Type(SnmpAdminString):
    """Custom type tnSwCardDynamicActiveReleaseAvailableCurrent based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TnSwCardDynamicActiveReleaseAvailableCurrent_Type.__name__ = "SnmpAdminString"
_TnSwCardDynamicActiveReleaseAvailableCurrent_Object = MibTableColumn
tnSwCardDynamicActiveReleaseAvailableCurrent = _TnSwCardDynamicActiveReleaseAvailableCurrent_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 12, 1, 21),
    _TnSwCardDynamicActiveReleaseAvailableCurrent_Type()
)
tnSwCardDynamicActiveReleaseAvailableCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwCardDynamicActiveReleaseAvailableCurrent.setStatus("current")
_TnSwCardDynamicDscRpmCountAvailableStandby_Type = Integer32
_TnSwCardDynamicDscRpmCountAvailableStandby_Object = MibTableColumn
tnSwCardDynamicDscRpmCountAvailableStandby = _TnSwCardDynamicDscRpmCountAvailableStandby_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 12, 1, 22),
    _TnSwCardDynamicDscRpmCountAvailableStandby_Type()
)
tnSwCardDynamicDscRpmCountAvailableStandby.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwCardDynamicDscRpmCountAvailableStandby.setStatus("current")
_TnSwCardDynamicFsRpmCountAvailableStandby_Type = Integer32
_TnSwCardDynamicFsRpmCountAvailableStandby_Object = MibTableColumn
tnSwCardDynamicFsRpmCountAvailableStandby = _TnSwCardDynamicFsRpmCountAvailableStandby_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 12, 1, 23),
    _TnSwCardDynamicFsRpmCountAvailableStandby_Type()
)
tnSwCardDynamicFsRpmCountAvailableStandby.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwCardDynamicFsRpmCountAvailableStandby.setStatus("current")


class _TnSwCardDynamicActiveReleaseAvailableStandby_Type(SnmpAdminString):
    """Custom type tnSwCardDynamicActiveReleaseAvailableStandby based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TnSwCardDynamicActiveReleaseAvailableStandby_Type.__name__ = "SnmpAdminString"
_TnSwCardDynamicActiveReleaseAvailableStandby_Object = MibTableColumn
tnSwCardDynamicActiveReleaseAvailableStandby = _TnSwCardDynamicActiveReleaseAvailableStandby_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 12, 1, 24),
    _TnSwCardDynamicActiveReleaseAvailableStandby_Type()
)
tnSwCardDynamicActiveReleaseAvailableStandby.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwCardDynamicActiveReleaseAvailableStandby.setStatus("current")
_TnSwCardDynamicDscRpmCountExcludedCurrent_Type = Integer32
_TnSwCardDynamicDscRpmCountExcludedCurrent_Object = MibTableColumn
tnSwCardDynamicDscRpmCountExcludedCurrent = _TnSwCardDynamicDscRpmCountExcludedCurrent_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 12, 1, 25),
    _TnSwCardDynamicDscRpmCountExcludedCurrent_Type()
)
tnSwCardDynamicDscRpmCountExcludedCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwCardDynamicDscRpmCountExcludedCurrent.setStatus("current")
_TnSwCardDynamicFsRpmCountExcludedCurrent_Type = Integer32
_TnSwCardDynamicFsRpmCountExcludedCurrent_Object = MibTableColumn
tnSwCardDynamicFsRpmCountExcludedCurrent = _TnSwCardDynamicFsRpmCountExcludedCurrent_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 12, 1, 26),
    _TnSwCardDynamicFsRpmCountExcludedCurrent_Type()
)
tnSwCardDynamicFsRpmCountExcludedCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwCardDynamicFsRpmCountExcludedCurrent.setStatus("current")


class _TnSwCardDynamicActiveReleaseExcludedCurrent_Type(SnmpAdminString):
    """Custom type tnSwCardDynamicActiveReleaseExcludedCurrent based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TnSwCardDynamicActiveReleaseExcludedCurrent_Type.__name__ = "SnmpAdminString"
_TnSwCardDynamicActiveReleaseExcludedCurrent_Object = MibTableColumn
tnSwCardDynamicActiveReleaseExcludedCurrent = _TnSwCardDynamicActiveReleaseExcludedCurrent_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 12, 1, 27),
    _TnSwCardDynamicActiveReleaseExcludedCurrent_Type()
)
tnSwCardDynamicActiveReleaseExcludedCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwCardDynamicActiveReleaseExcludedCurrent.setStatus("current")
_TnSwCardDynamicDscRpmCountExcludedStandby_Type = Integer32
_TnSwCardDynamicDscRpmCountExcludedStandby_Object = MibTableColumn
tnSwCardDynamicDscRpmCountExcludedStandby = _TnSwCardDynamicDscRpmCountExcludedStandby_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 12, 1, 28),
    _TnSwCardDynamicDscRpmCountExcludedStandby_Type()
)
tnSwCardDynamicDscRpmCountExcludedStandby.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwCardDynamicDscRpmCountExcludedStandby.setStatus("current")
_TnSwCardDynamicFsRpmCountExcludedStandby_Type = Integer32
_TnSwCardDynamicFsRpmCountExcludedStandby_Object = MibTableColumn
tnSwCardDynamicFsRpmCountExcludedStandby = _TnSwCardDynamicFsRpmCountExcludedStandby_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 12, 1, 29),
    _TnSwCardDynamicFsRpmCountExcludedStandby_Type()
)
tnSwCardDynamicFsRpmCountExcludedStandby.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwCardDynamicFsRpmCountExcludedStandby.setStatus("current")


class _TnSwCardDynamicActiveReleaseExcludedStandby_Type(SnmpAdminString):
    """Custom type tnSwCardDynamicActiveReleaseExcludedStandby based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TnSwCardDynamicActiveReleaseExcludedStandby_Type.__name__ = "SnmpAdminString"
_TnSwCardDynamicActiveReleaseExcludedStandby_Object = MibTableColumn
tnSwCardDynamicActiveReleaseExcludedStandby = _TnSwCardDynamicActiveReleaseExcludedStandby_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 12, 1, 30),
    _TnSwCardDynamicActiveReleaseExcludedStandby_Type()
)
tnSwCardDynamicActiveReleaseExcludedStandby.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwCardDynamicActiveReleaseExcludedStandby.setStatus("current")


class _TnSwCardDynamicFeatureUnavailableCurrent1_Type(SnmpAdminString):
    """Custom type tnSwCardDynamicFeatureUnavailableCurrent1 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_TnSwCardDynamicFeatureUnavailableCurrent1_Type.__name__ = "SnmpAdminString"
_TnSwCardDynamicFeatureUnavailableCurrent1_Object = MibTableColumn
tnSwCardDynamicFeatureUnavailableCurrent1 = _TnSwCardDynamicFeatureUnavailableCurrent1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 12, 1, 31),
    _TnSwCardDynamicFeatureUnavailableCurrent1_Type()
)
tnSwCardDynamicFeatureUnavailableCurrent1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwCardDynamicFeatureUnavailableCurrent1.setStatus("current")


class _TnSwCardDynamicFeatureUnavailableCurrent2_Type(SnmpAdminString):
    """Custom type tnSwCardDynamicFeatureUnavailableCurrent2 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_TnSwCardDynamicFeatureUnavailableCurrent2_Type.__name__ = "SnmpAdminString"
_TnSwCardDynamicFeatureUnavailableCurrent2_Object = MibTableColumn
tnSwCardDynamicFeatureUnavailableCurrent2 = _TnSwCardDynamicFeatureUnavailableCurrent2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 12, 1, 32),
    _TnSwCardDynamicFeatureUnavailableCurrent2_Type()
)
tnSwCardDynamicFeatureUnavailableCurrent2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwCardDynamicFeatureUnavailableCurrent2.setStatus("current")


class _TnSwCardDynamicFeatureUnknownCurrent1_Type(SnmpAdminString):
    """Custom type tnSwCardDynamicFeatureUnknownCurrent1 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_TnSwCardDynamicFeatureUnknownCurrent1_Type.__name__ = "SnmpAdminString"
_TnSwCardDynamicFeatureUnknownCurrent1_Object = MibTableColumn
tnSwCardDynamicFeatureUnknownCurrent1 = _TnSwCardDynamicFeatureUnknownCurrent1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 12, 1, 33),
    _TnSwCardDynamicFeatureUnknownCurrent1_Type()
)
tnSwCardDynamicFeatureUnknownCurrent1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwCardDynamicFeatureUnknownCurrent1.setStatus("current")


class _TnSwCardDynamicFeatureUnknownCurrent2_Type(SnmpAdminString):
    """Custom type tnSwCardDynamicFeatureUnknownCurrent2 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_TnSwCardDynamicFeatureUnknownCurrent2_Type.__name__ = "SnmpAdminString"
_TnSwCardDynamicFeatureUnknownCurrent2_Object = MibTableColumn
tnSwCardDynamicFeatureUnknownCurrent2 = _TnSwCardDynamicFeatureUnknownCurrent2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 12, 1, 34),
    _TnSwCardDynamicFeatureUnknownCurrent2_Type()
)
tnSwCardDynamicFeatureUnknownCurrent2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwCardDynamicFeatureUnknownCurrent2.setStatus("current")
_TnSwCardDynamicDscRpmCountUnavailableCurrent_Type = Integer32
_TnSwCardDynamicDscRpmCountUnavailableCurrent_Object = MibTableColumn
tnSwCardDynamicDscRpmCountUnavailableCurrent = _TnSwCardDynamicDscRpmCountUnavailableCurrent_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 12, 1, 35),
    _TnSwCardDynamicDscRpmCountUnavailableCurrent_Type()
)
tnSwCardDynamicDscRpmCountUnavailableCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwCardDynamicDscRpmCountUnavailableCurrent.setStatus("current")
_TnSwCardDynamicFsRpmCountUnavailableCurrent_Type = Integer32
_TnSwCardDynamicFsRpmCountUnavailableCurrent_Object = MibTableColumn
tnSwCardDynamicFsRpmCountUnavailableCurrent = _TnSwCardDynamicFsRpmCountUnavailableCurrent_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 12, 1, 36),
    _TnSwCardDynamicFsRpmCountUnavailableCurrent_Type()
)
tnSwCardDynamicFsRpmCountUnavailableCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwCardDynamicFsRpmCountUnavailableCurrent.setStatus("current")


class _TnSwCardDynamicActiveReleaseUnavailableCurrent_Type(SnmpAdminString):
    """Custom type tnSwCardDynamicActiveReleaseUnavailableCurrent based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TnSwCardDynamicActiveReleaseUnavailableCurrent_Type.__name__ = "SnmpAdminString"
_TnSwCardDynamicActiveReleaseUnavailableCurrent_Object = MibTableColumn
tnSwCardDynamicActiveReleaseUnavailableCurrent = _TnSwCardDynamicActiveReleaseUnavailableCurrent_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 12, 1, 37),
    _TnSwCardDynamicActiveReleaseUnavailableCurrent_Type()
)
tnSwCardDynamicActiveReleaseUnavailableCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwCardDynamicActiveReleaseUnavailableCurrent.setStatus("current")
_TnSwCardDynamicDscRpmCountUnknownCurrent_Type = Integer32
_TnSwCardDynamicDscRpmCountUnknownCurrent_Object = MibTableColumn
tnSwCardDynamicDscRpmCountUnknownCurrent = _TnSwCardDynamicDscRpmCountUnknownCurrent_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 12, 1, 38),
    _TnSwCardDynamicDscRpmCountUnknownCurrent_Type()
)
tnSwCardDynamicDscRpmCountUnknownCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwCardDynamicDscRpmCountUnknownCurrent.setStatus("current")
_TnSwCardDynamicFsRpmCountUnknownCurrent_Type = Integer32
_TnSwCardDynamicFsRpmCountUnknownCurrent_Object = MibTableColumn
tnSwCardDynamicFsRpmCountUnknownCurrent = _TnSwCardDynamicFsRpmCountUnknownCurrent_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 12, 1, 39),
    _TnSwCardDynamicFsRpmCountUnknownCurrent_Type()
)
tnSwCardDynamicFsRpmCountUnknownCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwCardDynamicFsRpmCountUnknownCurrent.setStatus("current")


class _TnSwCardDynamicActiveReleaseUnknownCurrent_Type(SnmpAdminString):
    """Custom type tnSwCardDynamicActiveReleaseUnknownCurrent based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TnSwCardDynamicActiveReleaseUnknownCurrent_Type.__name__ = "SnmpAdminString"
_TnSwCardDynamicActiveReleaseUnknownCurrent_Object = MibTableColumn
tnSwCardDynamicActiveReleaseUnknownCurrent = _TnSwCardDynamicActiveReleaseUnknownCurrent_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 12, 1, 40),
    _TnSwCardDynamicActiveReleaseUnknownCurrent_Type()
)
tnSwCardDynamicActiveReleaseUnknownCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwCardDynamicActiveReleaseUnknownCurrent.setStatus("current")
_TnSwDynamicInfoTable_Object = MibTable
tnSwDynamicInfoTable = _TnSwDynamicInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 13)
)
if mibBuilder.loadTexts:
    tnSwDynamicInfoTable.setStatus("current")
_TnSwDynamicInfoEntry_Object = MibTableRow
tnSwDynamicInfoEntry = _TnSwDynamicInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 13, 1)
)
tnSwDynamicInfoEntry.setIndexNames(
    (0, "TROPIC-SOFTWARE-MIB", "tnSwDynamicInfoEntries"),
)
if mibBuilder.loadTexts:
    tnSwDynamicInfoEntry.setStatus("current")
_TnSwDynamicInfoEntries_Type = Unsigned32
_TnSwDynamicInfoEntries_Object = MibTableColumn
tnSwDynamicInfoEntries = _TnSwDynamicInfoEntries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 13, 1, 1),
    _TnSwDynamicInfoEntries_Type()
)
tnSwDynamicInfoEntries.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSwDynamicInfoEntries.setStatus("current")


class _TnSwDynamicInfoDetails_Type(SnmpAdminString):
    """Custom type tnSwDynamicInfoDetails based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_TnSwDynamicInfoDetails_Type.__name__ = "SnmpAdminString"
_TnSwDynamicInfoDetails_Object = MibTableColumn
tnSwDynamicInfoDetails = _TnSwDynamicInfoDetails_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 13, 1, 2),
    _TnSwDynamicInfoDetails_Type()
)
tnSwDynamicInfoDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwDynamicInfoDetails.setStatus("current")
_TnSoftwareDynamic_ObjectIdentity = ObjectIdentity
tnSoftwareDynamic = _TnSoftwareDynamic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 2)
)


class _TnSwDynamicServerInetAddressType_Type(InetAddressType):
    """Custom type tnSwDynamicServerInetAddressType based on InetAddressType"""
    defaultValue = 0


_TnSwDynamicServerInetAddressType_Type.__name__ = "InetAddressType"
_TnSwDynamicServerInetAddressType_Object = MibScalar
tnSwDynamicServerInetAddressType = _TnSwDynamicServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 2, 1),
    _TnSwDynamicServerInetAddressType_Type()
)
tnSwDynamicServerInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSwDynamicServerInetAddressType.setStatus("current")


class _TnSwDynamicServerInetAddress_Type(InetAddress):
    """Custom type tnSwDynamicServerInetAddress based on InetAddress"""
    defaultHexValue = ""


_TnSwDynamicServerInetAddress_Type.__name__ = "InetAddress"
_TnSwDynamicServerInetAddress_Object = MibScalar
tnSwDynamicServerInetAddress = _TnSwDynamicServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 2, 2),
    _TnSwDynamicServerInetAddress_Type()
)
tnSwDynamicServerInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSwDynamicServerInetAddress.setStatus("current")
_TnSwDynamicServerIp_Type = IpAddress
_TnSwDynamicServerIp_Object = MibScalar
tnSwDynamicServerIp = _TnSwDynamicServerIp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 2, 3),
    _TnSwDynamicServerIp_Type()
)
tnSwDynamicServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSwDynamicServerIp.setStatus("current")


class _TnSwDynamicRoot_Type(SnmpAdminString):
    """Custom type tnSwDynamicRoot based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSwDynamicRoot_Type.__name__ = "SnmpAdminString"
_TnSwDynamicRoot_Object = MibScalar
tnSwDynamicRoot = _TnSwDynamicRoot_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 2, 4),
    _TnSwDynamicRoot_Type()
)
tnSwDynamicRoot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSwDynamicRoot.setStatus("current")
_TnSwDynamicRefresh_Type = TruthValue
_TnSwDynamicRefresh_Object = MibScalar
tnSwDynamicRefresh = _TnSwDynamicRefresh_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 2, 5),
    _TnSwDynamicRefresh_Type()
)
tnSwDynamicRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSwDynamicRefresh.setStatus("current")


class _TnSwDynamicServerUserId_Type(SnmpAdminString):
    """Custom type tnSwDynamicServerUserId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TnSwDynamicServerUserId_Type.__name__ = "SnmpAdminString"
_TnSwDynamicServerUserId_Object = MibScalar
tnSwDynamicServerUserId = _TnSwDynamicServerUserId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 2, 6),
    _TnSwDynamicServerUserId_Type()
)
tnSwDynamicServerUserId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSwDynamicServerUserId.setStatus("current")


class _TnSwDynamicServerPassword_Type(SnmpAdminString):
    """Custom type tnSwDynamicServerPassword based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TnSwDynamicServerPassword_Type.__name__ = "SnmpAdminString"
_TnSwDynamicServerPassword_Object = MibScalar
tnSwDynamicServerPassword = _TnSwDynamicServerPassword_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 2, 7),
    _TnSwDynamicServerPassword_Type()
)
tnSwDynamicServerPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSwDynamicServerPassword.setStatus("current")


class _TnSwDynamicPort_Type(Unsigned32):
    """Custom type tnSwDynamicPort based on Unsigned32"""
    defaultValue = 21

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TnSwDynamicPort_Type.__name__ = "Unsigned32"
_TnSwDynamicPort_Object = MibScalar
tnSwDynamicPort = _TnSwDynamicPort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 2, 8),
    _TnSwDynamicPort_Type()
)
tnSwDynamicPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSwDynamicPort.setStatus("current")


class _TnSwDynamicServerProtocol_Type(AluWdmNewTransferProtocol):
    """Custom type tnSwDynamicServerProtocol based on AluWdmNewTransferProtocol"""
    defaultValue = 1


_TnSwDynamicServerProtocol_Type.__name__ = "AluWdmNewTransferProtocol"
_TnSwDynamicServerProtocol_Object = MibScalar
tnSwDynamicServerProtocol = _TnSwDynamicServerProtocol_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 2, 9),
    _TnSwDynamicServerProtocol_Type()
)
tnSwDynamicServerProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSwDynamicServerProtocol.setStatus("current")


class _TnSwDynamicLoadType_Type(Integer32):
    """Custom type tnSwDynamicLoadType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("dynamic", 2),
          ("static", 3))
    )


_TnSwDynamicLoadType_Type.__name__ = "Integer32"
_TnSwDynamicLoadType_Object = MibScalar
tnSwDynamicLoadType = _TnSwDynamicLoadType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 2, 10),
    _TnSwDynamicLoadType_Type()
)
tnSwDynamicLoadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSwDynamicLoadType.setStatus("current")


class _TnSwDynamicFeature_Type(Integer32):
    """Custom type tnSwDynamicFeature based on Integer32"""
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
        *(("get", 1),
          ("delete", 2),
          ("add", 3),
          ("addForce", 4),
          ("clear", 5))
    )


_TnSwDynamicFeature_Type.__name__ = "Integer32"
_TnSwDynamicFeature_Object = MibScalar
tnSwDynamicFeature = _TnSwDynamicFeature_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 2, 11),
    _TnSwDynamicFeature_Type()
)
tnSwDynamicFeature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSwDynamicFeature.setStatus("current")


class _TnSwDynamicLoadEntities_Type(SnmpAdminString):
    """Custom type tnSwDynamicLoadEntities based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_TnSwDynamicLoadEntities_Type.__name__ = "SnmpAdminString"
_TnSwDynamicLoadEntities_Object = MibScalar
tnSwDynamicLoadEntities = _TnSwDynamicLoadEntities_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 2, 12),
    _TnSwDynamicLoadEntities_Type()
)
tnSwDynamicLoadEntities.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSwDynamicLoadEntities.setStatus("current")
_TnSwDynamicAutoRefresh_Type = TruthValue
_TnSwDynamicAutoRefresh_Object = MibScalar
tnSwDynamicAutoRefresh = _TnSwDynamicAutoRefresh_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 2, 13),
    _TnSwDynamicAutoRefresh_Type()
)
tnSwDynamicAutoRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSwDynamicAutoRefresh.setStatus("current")


class _TnSwDynamicUnavailableCurrent1_Type(SnmpAdminString):
    """Custom type tnSwDynamicUnavailableCurrent1 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_TnSwDynamicUnavailableCurrent1_Type.__name__ = "SnmpAdminString"
_TnSwDynamicUnavailableCurrent1_Object = MibScalar
tnSwDynamicUnavailableCurrent1 = _TnSwDynamicUnavailableCurrent1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 2, 14),
    _TnSwDynamicUnavailableCurrent1_Type()
)
tnSwDynamicUnavailableCurrent1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwDynamicUnavailableCurrent1.setStatus("current")


class _TnSwDynamicUnavailableCurrent2_Type(SnmpAdminString):
    """Custom type tnSwDynamicUnavailableCurrent2 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_TnSwDynamicUnavailableCurrent2_Type.__name__ = "SnmpAdminString"
_TnSwDynamicUnavailableCurrent2_Object = MibScalar
tnSwDynamicUnavailableCurrent2 = _TnSwDynamicUnavailableCurrent2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 2, 15),
    _TnSwDynamicUnavailableCurrent2_Type()
)
tnSwDynamicUnavailableCurrent2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwDynamicUnavailableCurrent2.setStatus("current")


class _TnSwDynamicUnknownCurrent1_Type(SnmpAdminString):
    """Custom type tnSwDynamicUnknownCurrent1 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_TnSwDynamicUnknownCurrent1_Type.__name__ = "SnmpAdminString"
_TnSwDynamicUnknownCurrent1_Object = MibScalar
tnSwDynamicUnknownCurrent1 = _TnSwDynamicUnknownCurrent1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 2, 16),
    _TnSwDynamicUnknownCurrent1_Type()
)
tnSwDynamicUnknownCurrent1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwDynamicUnknownCurrent1.setStatus("current")


class _TnSwDynamicUnknownCurrent2_Type(SnmpAdminString):
    """Custom type tnSwDynamicUnknownCurrent2 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_TnSwDynamicUnknownCurrent2_Type.__name__ = "SnmpAdminString"
_TnSwDynamicUnknownCurrent2_Object = MibScalar
tnSwDynamicUnknownCurrent2 = _TnSwDynamicUnknownCurrent2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 2, 17),
    _TnSwDynamicUnknownCurrent2_Type()
)
tnSwDynamicUnknownCurrent2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwDynamicUnknownCurrent2.setStatus("current")


class _TnSwDynamicFullCurrent1_Type(SnmpAdminString):
    """Custom type tnSwDynamicFullCurrent1 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_TnSwDynamicFullCurrent1_Type.__name__ = "SnmpAdminString"
_TnSwDynamicFullCurrent1_Object = MibScalar
tnSwDynamicFullCurrent1 = _TnSwDynamicFullCurrent1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 2, 18),
    _TnSwDynamicFullCurrent1_Type()
)
tnSwDynamicFullCurrent1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwDynamicFullCurrent1.setStatus("current")


class _TnSwDynamicFullCurrent2_Type(SnmpAdminString):
    """Custom type tnSwDynamicFullCurrent2 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_TnSwDynamicFullCurrent2_Type.__name__ = "SnmpAdminString"
_TnSwDynamicFullCurrent2_Object = MibScalar
tnSwDynamicFullCurrent2 = _TnSwDynamicFullCurrent2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 2, 19),
    _TnSwDynamicFullCurrent2_Type()
)
tnSwDynamicFullCurrent2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwDynamicFullCurrent2.setStatus("current")


class _TnSwDynamicAvailableCurrent1_Type(SnmpAdminString):
    """Custom type tnSwDynamicAvailableCurrent1 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_TnSwDynamicAvailableCurrent1_Type.__name__ = "SnmpAdminString"
_TnSwDynamicAvailableCurrent1_Object = MibScalar
tnSwDynamicAvailableCurrent1 = _TnSwDynamicAvailableCurrent1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 2, 20),
    _TnSwDynamicAvailableCurrent1_Type()
)
tnSwDynamicAvailableCurrent1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwDynamicAvailableCurrent1.setStatus("current")


class _TnSwDynamicAvailableCurrent2_Type(SnmpAdminString):
    """Custom type tnSwDynamicAvailableCurrent2 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_TnSwDynamicAvailableCurrent2_Type.__name__ = "SnmpAdminString"
_TnSwDynamicAvailableCurrent2_Object = MibScalar
tnSwDynamicAvailableCurrent2 = _TnSwDynamicAvailableCurrent2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 2, 21),
    _TnSwDynamicAvailableCurrent2_Type()
)
tnSwDynamicAvailableCurrent2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwDynamicAvailableCurrent2.setStatus("current")


class _TnSwDynamicExcludedCurrent1_Type(SnmpAdminString):
    """Custom type tnSwDynamicExcludedCurrent1 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_TnSwDynamicExcludedCurrent1_Type.__name__ = "SnmpAdminString"
_TnSwDynamicExcludedCurrent1_Object = MibScalar
tnSwDynamicExcludedCurrent1 = _TnSwDynamicExcludedCurrent1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 2, 22),
    _TnSwDynamicExcludedCurrent1_Type()
)
tnSwDynamicExcludedCurrent1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwDynamicExcludedCurrent1.setStatus("current")


class _TnSwDynamicExcludedCurrent2_Type(SnmpAdminString):
    """Custom type tnSwDynamicExcludedCurrent2 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_TnSwDynamicExcludedCurrent2_Type.__name__ = "SnmpAdminString"
_TnSwDynamicExcludedCurrent2_Object = MibScalar
tnSwDynamicExcludedCurrent2 = _TnSwDynamicExcludedCurrent2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 2, 23),
    _TnSwDynamicExcludedCurrent2_Type()
)
tnSwDynamicExcludedCurrent2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwDynamicExcludedCurrent2.setStatus("current")


class _TnSwDynamicFullCurrentRelease_Type(SnmpAdminString):
    """Custom type tnSwDynamicFullCurrentRelease based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TnSwDynamicFullCurrentRelease_Type.__name__ = "SnmpAdminString"
_TnSwDynamicFullCurrentRelease_Object = MibScalar
tnSwDynamicFullCurrentRelease = _TnSwDynamicFullCurrentRelease_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 2, 24),
    _TnSwDynamicFullCurrentRelease_Type()
)
tnSwDynamicFullCurrentRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwDynamicFullCurrentRelease.setStatus("current")


class _TnSwDynamicAvailableCurrentRelease_Type(SnmpAdminString):
    """Custom type tnSwDynamicAvailableCurrentRelease based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TnSwDynamicAvailableCurrentRelease_Type.__name__ = "SnmpAdminString"
_TnSwDynamicAvailableCurrentRelease_Object = MibScalar
tnSwDynamicAvailableCurrentRelease = _TnSwDynamicAvailableCurrentRelease_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 2, 25),
    _TnSwDynamicAvailableCurrentRelease_Type()
)
tnSwDynamicAvailableCurrentRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwDynamicAvailableCurrentRelease.setStatus("current")


class _TnSwDynamicExcludedCurrentRelease_Type(SnmpAdminString):
    """Custom type tnSwDynamicExcludedCurrentRelease based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TnSwDynamicExcludedCurrentRelease_Type.__name__ = "SnmpAdminString"
_TnSwDynamicExcludedCurrentRelease_Object = MibScalar
tnSwDynamicExcludedCurrentRelease = _TnSwDynamicExcludedCurrentRelease_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 2, 26),
    _TnSwDynamicExcludedCurrentRelease_Type()
)
tnSwDynamicExcludedCurrentRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwDynamicExcludedCurrentRelease.setStatus("current")


class _TnSwDynamicUnavailableCurrentRelease_Type(SnmpAdminString):
    """Custom type tnSwDynamicUnavailableCurrentRelease based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TnSwDynamicUnavailableCurrentRelease_Type.__name__ = "SnmpAdminString"
_TnSwDynamicUnavailableCurrentRelease_Object = MibScalar
tnSwDynamicUnavailableCurrentRelease = _TnSwDynamicUnavailableCurrentRelease_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 2, 27),
    _TnSwDynamicUnavailableCurrentRelease_Type()
)
tnSwDynamicUnavailableCurrentRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwDynamicUnavailableCurrentRelease.setStatus("current")


class _TnSwDynamicUnknownCurrentRelease_Type(SnmpAdminString):
    """Custom type tnSwDynamicUnknownCurrentRelease based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TnSwDynamicUnknownCurrentRelease_Type.__name__ = "SnmpAdminString"
_TnSwDynamicUnknownCurrentRelease_Object = MibScalar
tnSwDynamicUnknownCurrentRelease = _TnSwDynamicUnknownCurrentRelease_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 2, 28),
    _TnSwDynamicUnknownCurrentRelease_Type()
)
tnSwDynamicUnknownCurrentRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwDynamicUnknownCurrentRelease.setStatus("current")
_TnSwDynamicFullCurrentTotalRpms_Type = Integer32
_TnSwDynamicFullCurrentTotalRpms_Object = MibScalar
tnSwDynamicFullCurrentTotalRpms = _TnSwDynamicFullCurrentTotalRpms_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 2, 29),
    _TnSwDynamicFullCurrentTotalRpms_Type()
)
tnSwDynamicFullCurrentTotalRpms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwDynamicFullCurrentTotalRpms.setStatus("current")
_TnSwDynamicAvailableCurrentTotalRpms_Type = Integer32
_TnSwDynamicAvailableCurrentTotalRpms_Object = MibScalar
tnSwDynamicAvailableCurrentTotalRpms = _TnSwDynamicAvailableCurrentTotalRpms_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 2, 30),
    _TnSwDynamicAvailableCurrentTotalRpms_Type()
)
tnSwDynamicAvailableCurrentTotalRpms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwDynamicAvailableCurrentTotalRpms.setStatus("current")
_TnSwDynamicExcludedCurrentTotalRpms_Type = Integer32
_TnSwDynamicExcludedCurrentTotalRpms_Object = MibScalar
tnSwDynamicExcludedCurrentTotalRpms = _TnSwDynamicExcludedCurrentTotalRpms_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 2, 31),
    _TnSwDynamicExcludedCurrentTotalRpms_Type()
)
tnSwDynamicExcludedCurrentTotalRpms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwDynamicExcludedCurrentTotalRpms.setStatus("current")
_TnSwDynamicUnavailableCurrentTotalRpms_Type = Integer32
_TnSwDynamicUnavailableCurrentTotalRpms_Object = MibScalar
tnSwDynamicUnavailableCurrentTotalRpms = _TnSwDynamicUnavailableCurrentTotalRpms_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 2, 32),
    _TnSwDynamicUnavailableCurrentTotalRpms_Type()
)
tnSwDynamicUnavailableCurrentTotalRpms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwDynamicUnavailableCurrentTotalRpms.setStatus("current")
_TnSwDynamicUnknownCurrentTotalRpms_Type = Integer32
_TnSwDynamicUnknownCurrentTotalRpms_Object = MibScalar
tnSwDynamicUnknownCurrentTotalRpms = _TnSwDynamicUnknownCurrentTotalRpms_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 2, 33),
    _TnSwDynamicUnknownCurrentTotalRpms_Type()
)
tnSwDynamicUnknownCurrentTotalRpms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwDynamicUnknownCurrentTotalRpms.setStatus("current")
_TnSwDynamicFullCurrentRpmsLoaded_Type = Integer32
_TnSwDynamicFullCurrentRpmsLoaded_Object = MibScalar
tnSwDynamicFullCurrentRpmsLoaded = _TnSwDynamicFullCurrentRpmsLoaded_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 2, 34),
    _TnSwDynamicFullCurrentRpmsLoaded_Type()
)
tnSwDynamicFullCurrentRpmsLoaded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwDynamicFullCurrentRpmsLoaded.setStatus("current")
_TnSwDynamicAvailableCurrentRpmsLoaded_Type = Integer32
_TnSwDynamicAvailableCurrentRpmsLoaded_Object = MibScalar
tnSwDynamicAvailableCurrentRpmsLoaded = _TnSwDynamicAvailableCurrentRpmsLoaded_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 2, 35),
    _TnSwDynamicAvailableCurrentRpmsLoaded_Type()
)
tnSwDynamicAvailableCurrentRpmsLoaded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwDynamicAvailableCurrentRpmsLoaded.setStatus("current")
_TnSwDynamicExcludedCurrentRpmsLoaded_Type = Integer32
_TnSwDynamicExcludedCurrentRpmsLoaded_Object = MibScalar
tnSwDynamicExcludedCurrentRpmsLoaded = _TnSwDynamicExcludedCurrentRpmsLoaded_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 2, 36),
    _TnSwDynamicExcludedCurrentRpmsLoaded_Type()
)
tnSwDynamicExcludedCurrentRpmsLoaded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwDynamicExcludedCurrentRpmsLoaded.setStatus("current")
_TnSwDynamicUnavailableCurrentRpmsLoaded_Type = Integer32
_TnSwDynamicUnavailableCurrentRpmsLoaded_Object = MibScalar
tnSwDynamicUnavailableCurrentRpmsLoaded = _TnSwDynamicUnavailableCurrentRpmsLoaded_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 2, 37),
    _TnSwDynamicUnavailableCurrentRpmsLoaded_Type()
)
tnSwDynamicUnavailableCurrentRpmsLoaded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwDynamicUnavailableCurrentRpmsLoaded.setStatus("current")
_TnSwDynamicUnknownCurrentRpmsLoaded_Type = Integer32
_TnSwDynamicUnknownCurrentRpmsLoaded_Object = MibScalar
tnSwDynamicUnknownCurrentRpmsLoaded = _TnSwDynamicUnknownCurrentRpmsLoaded_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 2, 38),
    _TnSwDynamicUnknownCurrentRpmsLoaded_Type()
)
tnSwDynamicUnknownCurrentRpmsLoaded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwDynamicUnknownCurrentRpmsLoaded.setStatus("current")

# Managed Objects groups

tnSwNodeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 1, 1, 1)
)
tnSwNodeGroup.setObjects(
      *(("TROPIC-SOFTWARE-MIB", "tnSwNodeReleaseRoot"),
        ("TROPIC-SOFTWARE-MIB", "tnSwNodeControl"),
        ("TROPIC-SOFTWARE-MIB", "tnSwNodeCommittedRelease"),
        ("TROPIC-SOFTWARE-MIB", "tnSwNodeWorkingRelease"),
        ("TROPIC-SOFTWARE-MIB", "tnSwNodeForce"),
        ("TROPIC-SOFTWARE-MIB", "tnSwNodeNoBackup"),
        ("TROPIC-SOFTWARE-MIB", "tnSwNodeUpgradePathAvailable"),
        ("TROPIC-SOFTWARE-MIB", "tnSwNodeLastControlOperation"),
        ("TROPIC-SOFTWARE-MIB", "tnSwNodeControlAbort"),
        ("TROPIC-SOFTWARE-MIB", "tnSwNodeLastControlOperationStatus"),
        ("TROPIC-SOFTWARE-MIB", "tnSwNodeLastControlOperationResult"),
        ("TROPIC-SOFTWARE-MIB", "tnSwNodeLastControlOperationIntegerResult"),
        ("TROPIC-SOFTWARE-MIB", "tnSwNodeLastControlOperationPercentCompleted"),
        ("TROPIC-SOFTWARE-MIB", "tnSwNodeLastAuditTimeStamp"),
        ("TROPIC-SOFTWARE-MIB", "tnSwNodeWorkingReleaseDir"),
        ("TROPIC-SOFTWARE-MIB", "tnSwNodeActiveRelease"),
        ("TROPIC-SOFTWARE-MIB", "tnSwNodeSwdlServerProtocol"),
        ("TROPIC-SOFTWARE-MIB", "tnSwNodeSwdlServerIp"),
        ("TROPIC-SOFTWARE-MIB", "tnSwNodeSwdlServerUserId"),
        ("TROPIC-SOFTWARE-MIB", "tnSwNodeSwdlServerPassword"),
        ("TROPIC-SOFTWARE-MIB", "tnSwNodePartialLoadCommand"),
        ("TROPIC-SOFTWARE-MIB", "tnSwNodePartialLoadSupportedCardTypes"),
        ("TROPIC-SOFTWARE-MIB", "tnSwNodePartialLoadImgInstalledCardTypes"),
        ("TROPIC-SOFTWARE-MIB", "tnSwNodePartialLoadImgToBeInstalledCardTypes"),
        ("TROPIC-SOFTWARE-MIB", "tnSwNodePartialLoadActionResult"),
        ("TROPIC-SOFTWARE-MIB", "tnSwNodePartialLoadActionPercentCompleted"),
        ("TROPIC-SOFTWARE-MIB", "tnSwNodeSwdlServerInetAddressType"),
        ("TROPIC-SOFTWARE-MIB", "tnSwNodeSwdlServerInetAddress"),
        ("TROPIC-SOFTWARE-MIB", "tnSwNodeControlStatus"),
        ("TROPIC-SOFTWARE-MIB", "tnSwNodePort"),
        ("TROPIC-SOFTWARE-MIB", "tnSwNodeUrl"),
        ("TROPIC-SOFTWARE-MIB", "tnSwNodeLoadType"),
        ("TROPIC-SOFTWARE-MIB", "tnSwNodeUrlLoadType"),
        ("TROPIC-SOFTWARE-MIB", "tnSwNodeMigrateFileName"))
)
if mibBuilder.loadTexts:
    tnSwNodeGroup.setStatus("current")

tnSwCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 1, 1, 2)
)
tnSwCardGroup.setObjects(
      *(("TROPIC-SOFTWARE-MIB", "tnSwCardAppBank0"),
        ("TROPIC-SOFTWARE-MIB", "tnSwCardAppBank1"),
        ("TROPIC-SOFTWARE-MIB", "tnSwCardEmergBootBank"),
        ("TROPIC-SOFTWARE-MIB", "tnSwCardUserBootBank"),
        ("TROPIC-SOFTWARE-MIB", "tnSwCardActiveBank"),
        ("TROPIC-SOFTWARE-MIB", "tnSwCardNextBootBank"),
        ("TROPIC-SOFTWARE-MIB", "tnSwCardBankToActivate"),
        ("TROPIC-SOFTWARE-MIB", "tnSwCardBankToLoad"),
        ("TROPIC-SOFTWARE-MIB", "tnSwCardControl"),
        ("TROPIC-SOFTWARE-MIB", "tnSwCardReleaseDir"),
        ("TROPIC-SOFTWARE-MIB", "tnSwCardCurrentDscRpmCount"),
        ("TROPIC-SOFTWARE-MIB", "tnSwCardCurrentFsRpmCount"),
        ("TROPIC-SOFTWARE-MIB", "tnSwCardStandByDscRpmCount"),
        ("TROPIC-SOFTWARE-MIB", "tnSwCardStandByFsRpmCount"))
)
if mibBuilder.loadTexts:
    tnSwCardGroup.setStatus("current")

tnSwAuditScriptGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 1, 1, 3)
)
tnSwAuditScriptGroup.setObjects(
      *(("TROPIC-SOFTWARE-MIB", "tnSwAuditScriptShelf"),
        ("TROPIC-SOFTWARE-MIB", "tnSwAuditScriptSlot"),
        ("TROPIC-SOFTWARE-MIB", "tnSwAuditScriptCardType"),
        ("TROPIC-SOFTWARE-MIB", "tnSwAuditScriptAction"),
        ("TROPIC-SOFTWARE-MIB", "tnSwAuditScriptActionStatus"),
        ("TROPIC-SOFTWARE-MIB", "tnSwAuditScriptActionResult"),
        ("TROPIC-SOFTWARE-MIB", "tnSwAuditScriptActionPercentCompleted"),
        ("TROPIC-SOFTWARE-MIB", "tnSwAuditScriptResultTimeStamp"))
)
if mibBuilder.loadTexts:
    tnSwAuditScriptGroup.setStatus("current")

tnSwCpldGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 1, 1, 4)
)
tnSwCpldGroup.setObjects(
    ("TROPIC-SOFTWARE-MIB", "tnSwCpldProgramControl")
)
if mibBuilder.loadTexts:
    tnSwCpldGroup.setStatus("current")

tnFwCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 1, 1, 5)
)
tnFwCardGroup.setObjects(
      *(("TROPIC-SOFTWARE-MIB", "tnFwCardCurrentBundle"),
        ("TROPIC-SOFTWARE-MIB", "tnFwCardLoadedAt"),
        ("TROPIC-SOFTWARE-MIB", "tnFwCardLoadBundle"),
        ("TROPIC-SOFTWARE-MIB", "tnFwCardProvisionedAt"),
        ("TROPIC-SOFTWARE-MIB", "tnFwCardLoadState"),
        ("TROPIC-SOFTWARE-MIB", "tnFwCardWatchDog"),
        ("TROPIC-SOFTWARE-MIB", "tnFwCardProvisioningInfo"),
        ("TROPIC-SOFTWARE-MIB", "tnFwCardFpgaCapability"))
)
if mibBuilder.loadTexts:
    tnFwCardGroup.setStatus("current")

tnInstalledFwGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 1, 1, 6)
)
tnInstalledFwGroup.setObjects(
    ("TROPIC-SOFTWARE-MIB", "tnInstalledFwIsDefault")
)
if mibBuilder.loadTexts:
    tnInstalledFwGroup.setStatus("current")

tnPortGroupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 1, 1, 7)
)
tnPortGroupGroup.setObjects(
      *(("TROPIC-SOFTWARE-MIB", "tnPortGroupMode"),
        ("TROPIC-SOFTWARE-MIB", "tnPortGroupFwDownload"),
        ("TROPIC-SOFTWARE-MIB", "tnPortGroupFwCurrent"))
)
if mibBuilder.loadTexts:
    tnPortGroupGroup.setStatus("current")

tnInstalledFwPortGroupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 1, 1, 8)
)
tnInstalledFwPortGroupGroup.setObjects(
    ("TROPIC-SOFTWARE-MIB", "tnInstalledFwPortGroupIsDefault")
)
if mibBuilder.loadTexts:
    tnInstalledFwPortGroupGroup.setStatus("current")

tnFwHitlessCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 1, 1, 9)
)
tnFwHitlessCardGroup.setObjects(
      *(("TROPIC-SOFTWARE-MIB", "tnFwHitlessCardTrigger"),
        ("TROPIC-SOFTWARE-MIB", "tnFwHitlessCardLoadState"),
        ("TROPIC-SOFTWARE-MIB", "tnFwHitlessCardWatchDog"))
)
if mibBuilder.loadTexts:
    tnFwHitlessCardGroup.setStatus("current")

tnPortFwGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 1, 1, 10)
)
tnPortFwGroup.setObjects(
      *(("TROPIC-SOFTWARE-MIB", "tnPortFwFunction"),
        ("TROPIC-SOFTWARE-MIB", "tnPortFwLoadBundle"),
        ("TROPIC-SOFTWARE-MIB", "tnPortFwHitless"),
        ("TROPIC-SOFTWARE-MIB", "tnPortFwHitlessLoadState"),
        ("TROPIC-SOFTWARE-MIB", "tnPortFwLoadState"),
        ("TROPIC-SOFTWARE-MIB", "tnPortFwCurrentBundle"),
        ("TROPIC-SOFTWARE-MIB", "tnPortFwLoadedAt"),
        ("TROPIC-SOFTWARE-MIB", "tnPortFwProvisionedAt"),
        ("TROPIC-SOFTWARE-MIB", "tnPortFwLoadTimeOut"),
        ("TROPIC-SOFTWARE-MIB", "tnPortFwHitlessLoadTimeOut"),
        ("TROPIC-SOFTWARE-MIB", "tnPortFwProvisioningInfo"))
)
if mibBuilder.loadTexts:
    tnPortFwGroup.setStatus("current")

tnInstalledFwPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 1, 1, 11)
)
tnInstalledFwPortGroup.setObjects(
    ("TROPIC-SOFTWARE-MIB", "tnInstalledFwPortIsDefault")
)
if mibBuilder.loadTexts:
    tnInstalledFwPortGroup.setStatus("current")

tnSwDynamicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 1, 1, 12)
)
tnSwDynamicGroup.setObjects(
      *(("TROPIC-SOFTWARE-MIB", "tnSwDynamicServerInetAddressType"),
        ("TROPIC-SOFTWARE-MIB", "tnSwDynamicServerInetAddress"),
        ("TROPIC-SOFTWARE-MIB", "tnSwDynamicServerIp"),
        ("TROPIC-SOFTWARE-MIB", "tnSwDynamicRoot"),
        ("TROPIC-SOFTWARE-MIB", "tnSwDynamicRefresh"),
        ("TROPIC-SOFTWARE-MIB", "tnSwDynamicServerUserId"),
        ("TROPIC-SOFTWARE-MIB", "tnSwDynamicServerPassword"),
        ("TROPIC-SOFTWARE-MIB", "tnSwDynamicPort"),
        ("TROPIC-SOFTWARE-MIB", "tnSwDynamicServerProtocol"),
        ("TROPIC-SOFTWARE-MIB", "tnSwDynamicLoadType"),
        ("TROPIC-SOFTWARE-MIB", "tnSwDynamicFeature"),
        ("TROPIC-SOFTWARE-MIB", "tnSwDynamicLoadEntities"),
        ("TROPIC-SOFTWARE-MIB", "tnSwDynamicAutoRefresh"),
        ("TROPIC-SOFTWARE-MIB", "tnSwDynamicUnavailableCurrent1"),
        ("TROPIC-SOFTWARE-MIB", "tnSwDynamicUnavailableCurrent2"),
        ("TROPIC-SOFTWARE-MIB", "tnSwDynamicUnknownCurrent1"),
        ("TROPIC-SOFTWARE-MIB", "tnSwDynamicUnknownCurrent2"),
        ("TROPIC-SOFTWARE-MIB", "tnSwDynamicFullCurrent1"),
        ("TROPIC-SOFTWARE-MIB", "tnSwDynamicFullCurrent2"),
        ("TROPIC-SOFTWARE-MIB", "tnSwDynamicAvailableCurrent1"),
        ("TROPIC-SOFTWARE-MIB", "tnSwDynamicAvailableCurrent2"),
        ("TROPIC-SOFTWARE-MIB", "tnSwDynamicExcludedCurrent1"),
        ("TROPIC-SOFTWARE-MIB", "tnSwDynamicExcludedCurrent2"),
        ("TROPIC-SOFTWARE-MIB", "tnSwDynamicFullCurrentRelease"),
        ("TROPIC-SOFTWARE-MIB", "tnSwDynamicAvailableCurrentRelease"),
        ("TROPIC-SOFTWARE-MIB", "tnSwDynamicExcludedCurrentRelease"),
        ("TROPIC-SOFTWARE-MIB", "tnSwDynamicUnavailableCurrentRelease"),
        ("TROPIC-SOFTWARE-MIB", "tnSwDynamicUnknownCurrentRelease"),
        ("TROPIC-SOFTWARE-MIB", "tnSwDynamicFullCurrentTotalRpms"),
        ("TROPIC-SOFTWARE-MIB", "tnSwDynamicAvailableCurrentTotalRpms"),
        ("TROPIC-SOFTWARE-MIB", "tnSwDynamicExcludedCurrentTotalRpms"),
        ("TROPIC-SOFTWARE-MIB", "tnSwDynamicUnavailableCurrentTotalRpms"),
        ("TROPIC-SOFTWARE-MIB", "tnSwDynamicUnknownCurrentTotalRpms"),
        ("TROPIC-SOFTWARE-MIB", "tnSwDynamicFullCurrentRpmsLoaded"),
        ("TROPIC-SOFTWARE-MIB", "tnSwDynamicAvailableCurrentRpmsLoaded"),
        ("TROPIC-SOFTWARE-MIB", "tnSwDynamicExcludedCurrentRpmsLoaded"),
        ("TROPIC-SOFTWARE-MIB", "tnSwDynamicUnavailableCurrentRpmsLoaded"),
        ("TROPIC-SOFTWARE-MIB", "tnSwDynamicUnknownCurrentRpmsLoaded"))
)
if mibBuilder.loadTexts:
    tnSwDynamicGroup.setStatus("current")

tnSwCardDynamicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 1, 1, 13)
)
tnSwCardDynamicGroup.setObjects(
      *(("TROPIC-SOFTWARE-MIB", "tnSwCardDynamicFeatureFullCurrent1"),
        ("TROPIC-SOFTWARE-MIB", "tnSwCardDynamicFeatureFullCurrent2"),
        ("TROPIC-SOFTWARE-MIB", "tnSwCardDynamicFeatureFullStandby1"),
        ("TROPIC-SOFTWARE-MIB", "tnSwCardDynamicFeatureFullStandby2"),
        ("TROPIC-SOFTWARE-MIB", "tnSwCardDynamicFeatureAvailableCurrent1"),
        ("TROPIC-SOFTWARE-MIB", "tnSwCardDynamicFeatureAvailableCurrent2"),
        ("TROPIC-SOFTWARE-MIB", "tnSwCardDynamicFeatureAvailableStandby1"),
        ("TROPIC-SOFTWARE-MIB", "tnSwCardDynamicFeatureAvailableStandby2"),
        ("TROPIC-SOFTWARE-MIB", "tnSwCardDynamicFeatureExcludedCurrent1"),
        ("TROPIC-SOFTWARE-MIB", "tnSwCardDynamicFeatureExcludedCurrent2"),
        ("TROPIC-SOFTWARE-MIB", "tnSwCardDynamicFeatureExcludedStandby1"),
        ("TROPIC-SOFTWARE-MIB", "tnSwCardDynamicFeatureExcludedStandby2"),
        ("TROPIC-SOFTWARE-MIB", "tnSwCardDynamicDscRpmCountFullCurrent"),
        ("TROPIC-SOFTWARE-MIB", "tnSwCardDynamicFsRpmCountFullCurrent"),
        ("TROPIC-SOFTWARE-MIB", "tnSwCardDynamicActiveReleaseFullCurrent"),
        ("TROPIC-SOFTWARE-MIB", "tnSwCardDynamicDscRpmCountFullStandby"),
        ("TROPIC-SOFTWARE-MIB", "tnSwCardDynamicFsRpmCountFullStandby"),
        ("TROPIC-SOFTWARE-MIB", "tnSwCardDynamicActiveReleaseFullStandby"),
        ("TROPIC-SOFTWARE-MIB", "tnSwCardDynamicDscRpmCountAvailableCurrent"),
        ("TROPIC-SOFTWARE-MIB", "tnSwCardDynamicFsRpmCountAvailableCurrent"),
        ("TROPIC-SOFTWARE-MIB", "tnSwCardDynamicActiveReleaseAvailableCurrent"),
        ("TROPIC-SOFTWARE-MIB", "tnSwCardDynamicDscRpmCountAvailableStandby"),
        ("TROPIC-SOFTWARE-MIB", "tnSwCardDynamicFsRpmCountAvailableStandby"),
        ("TROPIC-SOFTWARE-MIB", "tnSwCardDynamicActiveReleaseAvailableStandby"),
        ("TROPIC-SOFTWARE-MIB", "tnSwCardDynamicDscRpmCountExcludedCurrent"),
        ("TROPIC-SOFTWARE-MIB", "tnSwCardDynamicFsRpmCountExcludedCurrent"),
        ("TROPIC-SOFTWARE-MIB", "tnSwCardDynamicActiveReleaseExcludedCurrent"),
        ("TROPIC-SOFTWARE-MIB", "tnSwCardDynamicDscRpmCountExcludedStandby"),
        ("TROPIC-SOFTWARE-MIB", "tnSwCardDynamicFsRpmCountExcludedStandby"),
        ("TROPIC-SOFTWARE-MIB", "tnSwCardDynamicActiveReleaseExcludedStandby"),
        ("TROPIC-SOFTWARE-MIB", "tnSwCardDynamicFeatureUnavailableCurrent1"),
        ("TROPIC-SOFTWARE-MIB", "tnSwCardDynamicFeatureUnavailableCurrent2"),
        ("TROPIC-SOFTWARE-MIB", "tnSwCardDynamicFeatureUnknownCurrent1"),
        ("TROPIC-SOFTWARE-MIB", "tnSwCardDynamicFeatureUnknownCurrent2"),
        ("TROPIC-SOFTWARE-MIB", "tnSwCardDynamicDscRpmCountUnavailableCurrent"),
        ("TROPIC-SOFTWARE-MIB", "tnSwCardDynamicFsRpmCountUnavailableCurrent"),
        ("TROPIC-SOFTWARE-MIB", "tnSwCardDynamicActiveReleaseUnavailableCurrent"),
        ("TROPIC-SOFTWARE-MIB", "tnSwCardDynamicDscRpmCountUnknownCurrent"),
        ("TROPIC-SOFTWARE-MIB", "tnSwCardDynamicFsRpmCountUnknownCurrent"),
        ("TROPIC-SOFTWARE-MIB", "tnSwCardDynamicActiveReleaseUnknownCurrent"))
)
if mibBuilder.loadTexts:
    tnSwCardDynamicGroup.setStatus("current")

tnSwDynamicInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 1, 1, 14)
)
tnSwDynamicInfoGroup.setObjects(
    ("TROPIC-SOFTWARE-MIB", "tnSwDynamicInfoDetails")
)
if mibBuilder.loadTexts:
    tnSwDynamicInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tnSoftwareCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 1, 2, 1)
)
tnSoftwareCompliance.setObjects(
      *(("TROPIC-SOFTWARE-MIB", "tnSwNodeGroup"),
        ("TROPIC-SOFTWARE-MIB", "tnSwCardGroup"),
        ("TROPIC-SOFTWARE-MIB", "tnSwAuditScriptGroup"),
        ("TROPIC-SOFTWARE-MIB", "tnSwCpldGroup"),
        ("TROPIC-SOFTWARE-MIB", "tnFwCardGroup"),
        ("TROPIC-SOFTWARE-MIB", "tnInstalledFwGroup"),
        ("TROPIC-SOFTWARE-MIB", "tnPortGroupGroup"),
        ("TROPIC-SOFTWARE-MIB", "tnInstalledFwPortGroupGroup"),
        ("TROPIC-SOFTWARE-MIB", "tnFwHitlessCardGroup"),
        ("TROPIC-SOFTWARE-MIB", "tnPortFwGroup"),
        ("TROPIC-SOFTWARE-MIB", "tnInstalledFwPortGroup"),
        ("TROPIC-SOFTWARE-MIB", "tnSwDynamicGroup"),
        ("TROPIC-SOFTWARE-MIB", "tnSwCardDynamicGroup"),
        ("TROPIC-SOFTWARE-MIB", "tnSwDynamicInfoGroup"))
)
if mibBuilder.loadTexts:
    tnSoftwareCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TROPIC-SOFTWARE-MIB",
    **{"TropicSwControl": TropicSwControl,
       "TropicSwBank": TropicSwBank,
       "TropicSwLastOperationStatus": TropicSwLastOperationStatus,
       "TropicSwLastOperationResult": TropicSwLastOperationResult,
       "TropicSwLastOperationPercentCompleted": TropicSwLastOperationPercentCompleted,
       "AluWdmPortGroupMode": AluWdmPortGroupMode,
       "tnSoftwareMibModule": tnSoftwareMibModule,
       "tnSoftwareConf": tnSoftwareConf,
       "tnSoftwareGroups": tnSoftwareGroups,
       "tnSwNodeGroup": tnSwNodeGroup,
       "tnSwCardGroup": tnSwCardGroup,
       "tnSwAuditScriptGroup": tnSwAuditScriptGroup,
       "tnSwCpldGroup": tnSwCpldGroup,
       "tnFwCardGroup": tnFwCardGroup,
       "tnInstalledFwGroup": tnInstalledFwGroup,
       "tnPortGroupGroup": tnPortGroupGroup,
       "tnInstalledFwPortGroupGroup": tnInstalledFwPortGroupGroup,
       "tnFwHitlessCardGroup": tnFwHitlessCardGroup,
       "tnPortFwGroup": tnPortFwGroup,
       "tnInstalledFwPortGroup": tnInstalledFwPortGroup,
       "tnSwDynamicGroup": tnSwDynamicGroup,
       "tnSwCardDynamicGroup": tnSwCardDynamicGroup,
       "tnSwDynamicInfoGroup": tnSwDynamicInfoGroup,
       "tnSoftwareCompliances": tnSoftwareCompliances,
       "tnSoftwareCompliance": tnSoftwareCompliance,
       "tnSoftwareObjs": tnSoftwareObjs,
       "tnSoftwareBasics": tnSoftwareBasics,
       "tnSoftwareNode": tnSoftwareNode,
       "tnSwNodeReleaseRoot": tnSwNodeReleaseRoot,
       "tnSwNodeControl": tnSwNodeControl,
       "tnSwNodeCommittedRelease": tnSwNodeCommittedRelease,
       "tnSwNodeWorkingRelease": tnSwNodeWorkingRelease,
       "tnSwNodeForce": tnSwNodeForce,
       "tnSwNodeNoBackup": tnSwNodeNoBackup,
       "tnSwNodeUpgradePathAvailable": tnSwNodeUpgradePathAvailable,
       "tnSwNodeLastControlOperation": tnSwNodeLastControlOperation,
       "tnSwNodeControlAbort": tnSwNodeControlAbort,
       "tnSwNodeLastControlOperationStatus": tnSwNodeLastControlOperationStatus,
       "tnSwNodeLastControlOperationResult": tnSwNodeLastControlOperationResult,
       "tnSwNodeLastControlOperationIntegerResult": tnSwNodeLastControlOperationIntegerResult,
       "tnSwNodeLastControlOperationPercentCompleted": tnSwNodeLastControlOperationPercentCompleted,
       "tnSwNodeLastAuditTimeStamp": tnSwNodeLastAuditTimeStamp,
       "tnSwNodeWorkingReleaseDir": tnSwNodeWorkingReleaseDir,
       "tnSwNodeActiveRelease": tnSwNodeActiveRelease,
       "tnSwNodeSwdlServerProtocol": tnSwNodeSwdlServerProtocol,
       "tnSwNodeSwdlServerIp": tnSwNodeSwdlServerIp,
       "tnSwNodeSwdlServerUserId": tnSwNodeSwdlServerUserId,
       "tnSwNodeSwdlServerPassword": tnSwNodeSwdlServerPassword,
       "tnSwNodePartialLoadCommand": tnSwNodePartialLoadCommand,
       "tnSwNodePartialLoadSupportedCardTypes": tnSwNodePartialLoadSupportedCardTypes,
       "tnSwNodePartialLoadImgInstalledCardTypes": tnSwNodePartialLoadImgInstalledCardTypes,
       "tnSwNodePartialLoadImgToBeInstalledCardTypes": tnSwNodePartialLoadImgToBeInstalledCardTypes,
       "tnSwNodePartialLoadActionResult": tnSwNodePartialLoadActionResult,
       "tnSwNodePartialLoadActionPercentCompleted": tnSwNodePartialLoadActionPercentCompleted,
       "tnSwNodeSwdlServerInetAddressType": tnSwNodeSwdlServerInetAddressType,
       "tnSwNodeSwdlServerInetAddress": tnSwNodeSwdlServerInetAddress,
       "tnSwNodeControlStatus": tnSwNodeControlStatus,
       "tnSwNodePort": tnSwNodePort,
       "tnSwNodeUrl": tnSwNodeUrl,
       "tnSwNodeLoadType": tnSwNodeLoadType,
       "tnSwNodeUrlLoadType": tnSwNodeUrlLoadType,
       "tnSwNodeMigrateFileName": tnSwNodeMigrateFileName,
       "tnSwCardTable": tnSwCardTable,
       "tnSwCardEntry": tnSwCardEntry,
       "tnSwCardAppBank0": tnSwCardAppBank0,
       "tnSwCardAppBank1": tnSwCardAppBank1,
       "tnSwCardEmergBootBank": tnSwCardEmergBootBank,
       "tnSwCardUserBootBank": tnSwCardUserBootBank,
       "tnSwCardActiveBank": tnSwCardActiveBank,
       "tnSwCardNextBootBank": tnSwCardNextBootBank,
       "tnSwCardBankToActivate": tnSwCardBankToActivate,
       "tnSwCardBankToLoad": tnSwCardBankToLoad,
       "tnSwCardControl": tnSwCardControl,
       "tnSwCardReleaseDir": tnSwCardReleaseDir,
       "tnSwCardCurrentDscRpmCount": tnSwCardCurrentDscRpmCount,
       "tnSwCardCurrentFsRpmCount": tnSwCardCurrentFsRpmCount,
       "tnSwCardStandByDscRpmCount": tnSwCardStandByDscRpmCount,
       "tnSwCardStandByFsRpmCount": tnSwCardStandByFsRpmCount,
       "tnSwAuditScriptTable": tnSwAuditScriptTable,
       "tnSwAuditScriptEntry": tnSwAuditScriptEntry,
       "tnSwAuditScriptStage": tnSwAuditScriptStage,
       "tnSwAuditScriptStep": tnSwAuditScriptStep,
       "tnSwAuditScriptShelf": tnSwAuditScriptShelf,
       "tnSwAuditScriptSlot": tnSwAuditScriptSlot,
       "tnSwAuditScriptCardType": tnSwAuditScriptCardType,
       "tnSwAuditScriptAction": tnSwAuditScriptAction,
       "tnSwAuditScriptActionStatus": tnSwAuditScriptActionStatus,
       "tnSwAuditScriptActionResult": tnSwAuditScriptActionResult,
       "tnSwAuditScriptActionPercentCompleted": tnSwAuditScriptActionPercentCompleted,
       "tnSwAuditScriptResultTimeStamp": tnSwAuditScriptResultTimeStamp,
       "tnSwCpldTable": tnSwCpldTable,
       "tnSwCpldEntry": tnSwCpldEntry,
       "tnSwCpldProgramControl": tnSwCpldProgramControl,
       "tnFwCardTable": tnFwCardTable,
       "tnFwCardEntry": tnFwCardEntry,
       "tnFwCardCurrentBundle": tnFwCardCurrentBundle,
       "tnFwCardLoadedAt": tnFwCardLoadedAt,
       "tnFwCardLoadBundle": tnFwCardLoadBundle,
       "tnFwCardProvisionedAt": tnFwCardProvisionedAt,
       "tnFwCardLoadState": tnFwCardLoadState,
       "tnFwCardWatchDog": tnFwCardWatchDog,
       "tnFwCardProvisioningInfo": tnFwCardProvisioningInfo,
       "tnFwCardFpgaCapability": tnFwCardFpgaCapability,
       "tnInstalledFwTable": tnInstalledFwTable,
       "tnInstalledFwEntry": tnInstalledFwEntry,
       "tnInstalledFwCardType": tnInstalledFwCardType,
       "tnInstalledFwFileName": tnInstalledFwFileName,
       "tnInstalledFwIsDefault": tnInstalledFwIsDefault,
       "tnPortGroupTable": tnPortGroupTable,
       "tnPortGroupEntry": tnPortGroupEntry,
       "tnPortGroupMode": tnPortGroupMode,
       "tnPortGroupFwDownload": tnPortGroupFwDownload,
       "tnPortGroupFwCurrent": tnPortGroupFwCurrent,
       "tnInstalledFwPortGroupTable": tnInstalledFwPortGroupTable,
       "tnInstalledFwPortGroupEntry": tnInstalledFwPortGroupEntry,
       "tnInstalledFwPortGroupMode": tnInstalledFwPortGroupMode,
       "tnInstalledFwPortGroupFw": tnInstalledFwPortGroupFw,
       "tnInstalledFwPortGroupIsDefault": tnInstalledFwPortGroupIsDefault,
       "tnFwHitlessCardTable": tnFwHitlessCardTable,
       "tnFwHitlessCardEntry": tnFwHitlessCardEntry,
       "tnFwHitlessCardTrigger": tnFwHitlessCardTrigger,
       "tnFwHitlessCardLoadState": tnFwHitlessCardLoadState,
       "tnFwHitlessCardWatchDog": tnFwHitlessCardWatchDog,
       "tnPortFwTable": tnPortFwTable,
       "tnPortFwEntry": tnPortFwEntry,
       "tnPortFwFunction": tnPortFwFunction,
       "tnPortFwLoadBundle": tnPortFwLoadBundle,
       "tnPortFwHitless": tnPortFwHitless,
       "tnPortFwHitlessLoadState": tnPortFwHitlessLoadState,
       "tnPortFwLoadState": tnPortFwLoadState,
       "tnPortFwCurrentBundle": tnPortFwCurrentBundle,
       "tnPortFwLoadedAt": tnPortFwLoadedAt,
       "tnPortFwProvisionedAt": tnPortFwProvisionedAt,
       "tnPortFwLoadTimeOut": tnPortFwLoadTimeOut,
       "tnPortFwHitlessLoadTimeOut": tnPortFwHitlessLoadTimeOut,
       "tnPortFwProvisioningInfo": tnPortFwProvisioningInfo,
       "tnInstalledFwPortTable": tnInstalledFwPortTable,
       "tnInstalledFwPortEntry": tnInstalledFwPortEntry,
       "tnInstalledFwPortModuleType": tnInstalledFwPortModuleType,
       "tnInstalledFwPortFileName": tnInstalledFwPortFileName,
       "tnInstalledFwPortIsDefault": tnInstalledFwPortIsDefault,
       "tnSwCardDynamicTable": tnSwCardDynamicTable,
       "tnSwCardDynamicEntry": tnSwCardDynamicEntry,
       "tnSwCardDynamicFeatureFullCurrent1": tnSwCardDynamicFeatureFullCurrent1,
       "tnSwCardDynamicFeatureFullCurrent2": tnSwCardDynamicFeatureFullCurrent2,
       "tnSwCardDynamicFeatureFullStandby1": tnSwCardDynamicFeatureFullStandby1,
       "tnSwCardDynamicFeatureFullStandby2": tnSwCardDynamicFeatureFullStandby2,
       "tnSwCardDynamicFeatureAvailableCurrent1": tnSwCardDynamicFeatureAvailableCurrent1,
       "tnSwCardDynamicFeatureAvailableCurrent2": tnSwCardDynamicFeatureAvailableCurrent2,
       "tnSwCardDynamicFeatureAvailableStandby1": tnSwCardDynamicFeatureAvailableStandby1,
       "tnSwCardDynamicFeatureAvailableStandby2": tnSwCardDynamicFeatureAvailableStandby2,
       "tnSwCardDynamicFeatureExcludedCurrent1": tnSwCardDynamicFeatureExcludedCurrent1,
       "tnSwCardDynamicFeatureExcludedCurrent2": tnSwCardDynamicFeatureExcludedCurrent2,
       "tnSwCardDynamicFeatureExcludedStandby1": tnSwCardDynamicFeatureExcludedStandby1,
       "tnSwCardDynamicFeatureExcludedStandby2": tnSwCardDynamicFeatureExcludedStandby2,
       "tnSwCardDynamicDscRpmCountFullCurrent": tnSwCardDynamicDscRpmCountFullCurrent,
       "tnSwCardDynamicFsRpmCountFullCurrent": tnSwCardDynamicFsRpmCountFullCurrent,
       "tnSwCardDynamicActiveReleaseFullCurrent": tnSwCardDynamicActiveReleaseFullCurrent,
       "tnSwCardDynamicDscRpmCountFullStandby": tnSwCardDynamicDscRpmCountFullStandby,
       "tnSwCardDynamicFsRpmCountFullStandby": tnSwCardDynamicFsRpmCountFullStandby,
       "tnSwCardDynamicActiveReleaseFullStandby": tnSwCardDynamicActiveReleaseFullStandby,
       "tnSwCardDynamicDscRpmCountAvailableCurrent": tnSwCardDynamicDscRpmCountAvailableCurrent,
       "tnSwCardDynamicFsRpmCountAvailableCurrent": tnSwCardDynamicFsRpmCountAvailableCurrent,
       "tnSwCardDynamicActiveReleaseAvailableCurrent": tnSwCardDynamicActiveReleaseAvailableCurrent,
       "tnSwCardDynamicDscRpmCountAvailableStandby": tnSwCardDynamicDscRpmCountAvailableStandby,
       "tnSwCardDynamicFsRpmCountAvailableStandby": tnSwCardDynamicFsRpmCountAvailableStandby,
       "tnSwCardDynamicActiveReleaseAvailableStandby": tnSwCardDynamicActiveReleaseAvailableStandby,
       "tnSwCardDynamicDscRpmCountExcludedCurrent": tnSwCardDynamicDscRpmCountExcludedCurrent,
       "tnSwCardDynamicFsRpmCountExcludedCurrent": tnSwCardDynamicFsRpmCountExcludedCurrent,
       "tnSwCardDynamicActiveReleaseExcludedCurrent": tnSwCardDynamicActiveReleaseExcludedCurrent,
       "tnSwCardDynamicDscRpmCountExcludedStandby": tnSwCardDynamicDscRpmCountExcludedStandby,
       "tnSwCardDynamicFsRpmCountExcludedStandby": tnSwCardDynamicFsRpmCountExcludedStandby,
       "tnSwCardDynamicActiveReleaseExcludedStandby": tnSwCardDynamicActiveReleaseExcludedStandby,
       "tnSwCardDynamicFeatureUnavailableCurrent1": tnSwCardDynamicFeatureUnavailableCurrent1,
       "tnSwCardDynamicFeatureUnavailableCurrent2": tnSwCardDynamicFeatureUnavailableCurrent2,
       "tnSwCardDynamicFeatureUnknownCurrent1": tnSwCardDynamicFeatureUnknownCurrent1,
       "tnSwCardDynamicFeatureUnknownCurrent2": tnSwCardDynamicFeatureUnknownCurrent2,
       "tnSwCardDynamicDscRpmCountUnavailableCurrent": tnSwCardDynamicDscRpmCountUnavailableCurrent,
       "tnSwCardDynamicFsRpmCountUnavailableCurrent": tnSwCardDynamicFsRpmCountUnavailableCurrent,
       "tnSwCardDynamicActiveReleaseUnavailableCurrent": tnSwCardDynamicActiveReleaseUnavailableCurrent,
       "tnSwCardDynamicDscRpmCountUnknownCurrent": tnSwCardDynamicDscRpmCountUnknownCurrent,
       "tnSwCardDynamicFsRpmCountUnknownCurrent": tnSwCardDynamicFsRpmCountUnknownCurrent,
       "tnSwCardDynamicActiveReleaseUnknownCurrent": tnSwCardDynamicActiveReleaseUnknownCurrent,
       "tnSwDynamicInfoTable": tnSwDynamicInfoTable,
       "tnSwDynamicInfoEntry": tnSwDynamicInfoEntry,
       "tnSwDynamicInfoEntries": tnSwDynamicInfoEntries,
       "tnSwDynamicInfoDetails": tnSwDynamicInfoDetails,
       "tnSoftwareDynamic": tnSoftwareDynamic,
       "tnSwDynamicServerInetAddressType": tnSwDynamicServerInetAddressType,
       "tnSwDynamicServerInetAddress": tnSwDynamicServerInetAddress,
       "tnSwDynamicServerIp": tnSwDynamicServerIp,
       "tnSwDynamicRoot": tnSwDynamicRoot,
       "tnSwDynamicRefresh": tnSwDynamicRefresh,
       "tnSwDynamicServerUserId": tnSwDynamicServerUserId,
       "tnSwDynamicServerPassword": tnSwDynamicServerPassword,
       "tnSwDynamicPort": tnSwDynamicPort,
       "tnSwDynamicServerProtocol": tnSwDynamicServerProtocol,
       "tnSwDynamicLoadType": tnSwDynamicLoadType,
       "tnSwDynamicFeature": tnSwDynamicFeature,
       "tnSwDynamicLoadEntities": tnSwDynamicLoadEntities,
       "tnSwDynamicAutoRefresh": tnSwDynamicAutoRefresh,
       "tnSwDynamicUnavailableCurrent1": tnSwDynamicUnavailableCurrent1,
       "tnSwDynamicUnavailableCurrent2": tnSwDynamicUnavailableCurrent2,
       "tnSwDynamicUnknownCurrent1": tnSwDynamicUnknownCurrent1,
       "tnSwDynamicUnknownCurrent2": tnSwDynamicUnknownCurrent2,
       "tnSwDynamicFullCurrent1": tnSwDynamicFullCurrent1,
       "tnSwDynamicFullCurrent2": tnSwDynamicFullCurrent2,
       "tnSwDynamicAvailableCurrent1": tnSwDynamicAvailableCurrent1,
       "tnSwDynamicAvailableCurrent2": tnSwDynamicAvailableCurrent2,
       "tnSwDynamicExcludedCurrent1": tnSwDynamicExcludedCurrent1,
       "tnSwDynamicExcludedCurrent2": tnSwDynamicExcludedCurrent2,
       "tnSwDynamicFullCurrentRelease": tnSwDynamicFullCurrentRelease,
       "tnSwDynamicAvailableCurrentRelease": tnSwDynamicAvailableCurrentRelease,
       "tnSwDynamicExcludedCurrentRelease": tnSwDynamicExcludedCurrentRelease,
       "tnSwDynamicUnavailableCurrentRelease": tnSwDynamicUnavailableCurrentRelease,
       "tnSwDynamicUnknownCurrentRelease": tnSwDynamicUnknownCurrentRelease,
       "tnSwDynamicFullCurrentTotalRpms": tnSwDynamicFullCurrentTotalRpms,
       "tnSwDynamicAvailableCurrentTotalRpms": tnSwDynamicAvailableCurrentTotalRpms,
       "tnSwDynamicExcludedCurrentTotalRpms": tnSwDynamicExcludedCurrentTotalRpms,
       "tnSwDynamicUnavailableCurrentTotalRpms": tnSwDynamicUnavailableCurrentTotalRpms,
       "tnSwDynamicUnknownCurrentTotalRpms": tnSwDynamicUnknownCurrentTotalRpms,
       "tnSwDynamicFullCurrentRpmsLoaded": tnSwDynamicFullCurrentRpmsLoaded,
       "tnSwDynamicAvailableCurrentRpmsLoaded": tnSwDynamicAvailableCurrentRpmsLoaded,
       "tnSwDynamicExcludedCurrentRpmsLoaded": tnSwDynamicExcludedCurrentRpmsLoaded,
       "tnSwDynamicUnavailableCurrentRpmsLoaded": tnSwDynamicUnavailableCurrentRpmsLoaded,
       "tnSwDynamicUnknownCurrentRpmsLoaded": tnSwDynamicUnknownCurrentRpmsLoaded}
)
